# Use a slim version of Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to /app
COPY . .

# Expose port 8080 (if your application uses it)
EXPOSE 8080

# Command to run your application
CMD ["python", "main.py"]
