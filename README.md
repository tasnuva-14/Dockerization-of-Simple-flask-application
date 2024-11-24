# Flask App with Docker

This is a simple Flask Application that displays a form on the homepage and processes user input to display a result. The application is Dockerized for easy deployment and portability.

## Features
- Displays a form with fields for user input (`name` and `color`).
- Processes the form submission and renders a result page.
- Suppose one has input his/her name and selected a color, the output will print the name in that color.
- Dockerized for seamless setup and deployment.

## File Structure
├── app.py # Main Flask application 

├── templates/ │ ├── form.html # HTML template for the form │ ├── result.html # HTML template for the result 
├── Dockerfile # Docker configuration file  
├── requirements.txt # Python dependencies


## Build the Docker Image
docker build -t final-color .

## Run the Container
docker run -d -p 3000:5000 final-color

## The application will be accessible at
http://localhost:3000

## Preview
![Preview of the Flask App](preview.PNG)
