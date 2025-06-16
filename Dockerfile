FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    transformers \
    onnxruntime \
    flask \
    gunicorn

# Copy application
COPY app.py ./

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--timeout", "300"]
