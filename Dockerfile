# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files to container
COPY ./app ./app

# Expose the port your FastAPI app will run on
EXPOSE 10000

# Environment variable (optional default)
ENV PORT=10000

# Run Uvicorn to start your app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
