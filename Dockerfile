FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements-search.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-search.txt

# Copy application code
COPY search/ search/
COPY search.py .

# Create directory for database
RUN mkdir -p lancedb

# Set environment variables for better Python behavior
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Default command
CMD ["python", "search.py", "--help"]
