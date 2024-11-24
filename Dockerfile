# Use a base image with Python
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your project files to the container
COPY . /app

EXPOSE 5000

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run your Flask app
CMD ["python", "app.py"]
