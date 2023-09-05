# Base image for your challenge
FROM python:3.9-slim
 # Set the working directory
WORKDIR /app
 # Copy the necessary files to the container
COPY requirements.txt .
COPY server.py .
COPY flag.txt .
 # Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 # Expose the necessary port(s)
EXPOSE 5000
 # Set the command to run your application
CMD [ "python", "server.py" ]