# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install virtualenv globally
RUN pip install --no-cache-dir virtualenv

# Copy the requirements file into the container
COPY requirements.txt .

# Create and activate a virtual environment, then install dependencies
RUN virtualenv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure the routes directory exists
RUN mkdir -p routes

# Expose port 5000
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Use the virtual environment to run the application
CMD ["/bin/sh", "-c", ". venv/bin/activate && flask run --host=0.0.0.0"]
