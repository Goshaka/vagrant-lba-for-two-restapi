# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app2.py /app/app2.py
COPY requirenments.txt /app/requirenments.txt


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /app/requirenments.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app2.py when the container launches
#CMD ["python", "app2.py"]
ENTRYPOINT ["python"]
CMD ["app2.py"]