# Containerized Microservices Video Streaming System

A distributed system for video upload and streaming, built using microservices architecture and containerized with Docker.

## System Architecture

The system consists of the following microservices:

1. **Upload Service** (Port: 5001)
   - Handles video file uploads
   - Saves files to the file system
   - Stores metadata in the database

2. **Stream Service** (Port: 5002)
   - Lists available videos
   - Streams video content
   - Retrieves video metadata

3. **File System Service** (Port: 5004)
   - Manages file storage
   - Handles file retrieval
   - Provides file system operations

4. **MySQL Database** (Port: 3306)
   - Stores video metadata
   - Manages video information

5. **UI Service** (Port: 8501)
   - Provides a user-friendly interface
   - Handles video uploads
   - Enables video streaming
   - Lists available videos

## Features

- Video file upload
- Video streaming
- Video listing
- User-friendly web interface
- Containerized deployment
- Microservices architecture

## Technology Stack

- Python
- Flask
- MySQL
- Docker
- Docker Compose
- Streamlit (for UI)

## Directory Structure

```
.
├── auth-service/          # Authentication service
├── file-system-service/   # File storage service
├── mysql-db/             # Database service
├── stream-service/       # Video streaming service
├── upload-service/       # Video upload service
├── ui-service/          # Web interface service
├── docker-compose.yml   # Docker Compose configuration
└── README.md           # This file
```

## Getting Started

For detailed instructions on how to run the system, please refer to [HOW_TO_RUN.md](HOW_TO_RUN.md). 