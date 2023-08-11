# Use an official Python runtime as a parent image
FROM python:3.11.4

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y libpq-dev gcc

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

COPY ./static /app/static

