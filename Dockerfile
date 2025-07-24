FROM --platform=linux/amd64 python:3.10-slim


WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libtesseract-dev \
    libleptonica-dev \
    poppler-utils \
    build-essential \
    && apt-get clean

COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]
