#!/usr/bin/env bash
set -e

# Cài Tesseract OCR và các thư viện hệ thống cần thiết cho OpenCV
apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-vie \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Cài Python packages
pip install --upgrade pip
pip install -r requirements.txt
