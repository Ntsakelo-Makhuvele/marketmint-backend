# Use a slim Python image for faster cold starts
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the app with Uvicorn
# Cloud Run injects the PORT env var, so we must bind to it
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]