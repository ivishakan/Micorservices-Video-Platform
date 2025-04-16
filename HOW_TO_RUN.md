# How to Run the Video Streaming System

This guide will help you set up and run the video streaming system on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- Docker (version 20.10.0 or higher)
- Docker Compose (version 2.0.0 or higher)

You can check your installations by running:
```bash
docker --version
docker compose version
```

## Step 1: Clone the Repository

Clone the repository to your local machine:
```bash
git clone <repository-url>
cd Containerized-Microservices-System
```

## Step 2: Build and Start the Services

Run the following command to build and start all services:
```bash
docker compose up --build
```

This will:
1. Build all service containers
2. Start the MySQL database
3. Start all microservices
4. Start the UI service

## Step 3: Access the System

Once all services are running, you can access the system through:

1. **Web Interface**: Open your browser and go to `http://localhost:8501`
   - This is the main user interface for the system
   - You can upload, view, and stream videos here

2. **API Endpoints**:
   - Upload Service: `http://localhost:5001`
   - Stream Service: `http://localhost:5002`
   - File System Service: `http://localhost:5004`

## Step 4: Using the System

### Uploading a Video

1. Open the web interface at `http://localhost:8501`
2. Click on "Upload Video" in the sidebar
3. Select a video file (MP4 format)
4. Click "Upload"

### Viewing Available Videos

1. Open the web interface at `http://localhost:8501`
2. Click on "View Videos" in the sidebar
3. You'll see a list of all uploaded videos

### Streaming a Video

1. Open the web interface at `http://localhost:8501`
2. Click on "Stream Video" in the sidebar
3. Select a video from the dropdown
4. Click "Stream Video"

## Step 5: Stopping the System

To stop all services, press `Ctrl+C` in the terminal where you started the services, or run:
```bash
docker compose down
```

## Troubleshooting

### Common Issues

1. **Port Conflicts**
   - If you get port conflict errors, make sure no other services are using ports 5001, 5002, 5003, 5004, 8501, or 3306
   - You can modify the ports in `docker-compose.yml` if needed

2. **Database Issues**
   - If the database isn't initializing properly, try:
     ```bash
     docker compose down -v
     docker compose up --build
     ```

3. **File Upload Issues**
   - Make sure you're using MP4 format videos
   - Check that the file size is reasonable (the system is configured for typical video sizes)

### Checking Service Logs

To check logs for a specific service:
```bash
docker logs containerized-microservices-system-<service-name>-1
```

Replace `<service-name>` with:
- `upload-service`
- `stream-service`
- `file-system-service`
- `mysql-db`
- `ui-service`

## Development

### Modifying Services

1. Make your changes to the service code
2. Rebuild and restart the services:
   ```bash
   docker compose up --build
   ```

### Adding New Features

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## Support

If you encounter any issues or have questions, please:
1. Check the logs of the relevant service
2. Review the troubleshooting section
3. Create an issue in the repository 