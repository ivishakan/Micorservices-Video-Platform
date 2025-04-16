# MySQL official image
FROM mysql:8.0

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=video_db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

# Copy initialization script
COPY init-db.sql /docker-entrypoint-initdb.d/

# Expose port
EXPOSE 3306

