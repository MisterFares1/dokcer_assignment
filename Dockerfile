# Use the official Python image as the base image
FROM python:3.10.14-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app/app.py

# Copy the file 'paragraphs.txt' into the container
COPY paragraphs.txt /app/paragraphs.txt

# Install NLTK and its required resources
RUN pip install nltk && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader stopwords

# Run the Python script when the container starts
CMD ["python", "app.py"]
