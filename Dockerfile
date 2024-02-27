# Use an existing docker image as a base
FROM python:3.10.12

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
