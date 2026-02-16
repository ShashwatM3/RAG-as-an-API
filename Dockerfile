# sets python version
FROM python:3.11-slim

# sets the current directory inside the container
WORKDIR /app

# runs a shell command to update package list and installs curl
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# copying / moving files from host machine to container
COPY app.py chroma_client.py k8s.txt ./

# installs the essential python packages
RUN pip install fastapi uvicorn chromadb ollama

# Running any initialization scripts (nothing for us)
# RUN __.py

# Tells docker which port to listen on at RUNTIME
EXPOSE 8000

# Setting the DEFAULT COMMAND that runs when container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]