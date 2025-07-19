# Use Python 3.13 base image
FROM python:3.13.3-slim

# Set working directory
WORKDIR /project

# Copy requirements file first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY ./app /project/app

# Set working directory inside app folder
WORKDIR /project/app

# Run FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
