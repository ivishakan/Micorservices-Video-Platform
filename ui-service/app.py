import streamlit as st
import requests
import io
from pathlib import Path

# Configure the page
st.set_page_config(
    page_title="Video Streaming System",
    page_icon="🎥",
    layout="wide"
)

# Constants
UPLOAD_SERVICE_URL = "http://upload-service:5001"
STREAM_SERVICE_URL = "http://stream-service:5002"

# Title
st.title("🎥 Video Streaming System")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Video", "View Videos", "Stream Video"])

if page == "Upload Video":
    st.header("Upload a Video")
    uploaded_file = st.file_uploader("Choose a video file", type=['mp4'])
    
    if uploaded_file is not None:
        if st.button("Upload"):
            try:
                # Prepare the file for upload
                files = {'file': (uploaded_file.name, uploaded_file, 'video/mp4')}
                response = requests.post(f"{UPLOAD_SERVICE_URL}/upload", files=files)
                
                if response.status_code == 200:
                    st.success("Video uploaded successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Upload failed: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

elif page == "View Videos":
    st.header("Available Videos")
    try:
        response = requests.get(f"{STREAM_SERVICE_URL}/videos")
        if response.status_code == 200:
            videos = response.json()
            if videos:
                st.write("### List of Videos")
                for video in videos:
                    st.write(f"ID: {video['id']} - Path: {video['path']}")
            else:
                st.info("No videos available yet.")
        else:
            st.error(f"Failed to fetch videos: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif page == "Stream Video":
    st.header("Stream a Video")
    try:
        # Get list of videos
        response = requests.get(f"{STREAM_SERVICE_URL}/videos")
        if response.status_code == 200:
            videos = response.json()
            if videos:
                video_options = {f"Video {video['id']}": video['id'] for video in videos}
                selected_video = st.selectbox("Select a video to stream", options=list(video_options.keys()))
                
                if st.button("Stream Video"):
                    video_id = video_options[selected_video]
                    try:
                        response = requests.get(f"{STREAM_SERVICE_URL}/video/{video_id}")
                        if response.status_code == 200:
                            # Save the video temporarily
                            video_path = f"temp_video_{video_id}.mp4"
                            with open(video_path, "wb") as f:
                                f.write(response.content)
                            
                            # Display the video
                            st.video(video_path)
                            
                            # Clean up
                            Path(video_path).unlink()
                        else:
                            st.error(f"Failed to stream video: {response.text}")
                    except Exception as e:
                        st.error(f"An error occurred while streaming: {str(e)}")
            else:
                st.info("No videos available to stream.")
        else:
            st.error(f"Failed to fetch videos: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}") 