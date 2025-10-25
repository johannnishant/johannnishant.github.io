#!/bin/bash

# Jekyll Local Development Script
echo "🚀 Starting Jekyll local development server..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Build the Docker image
echo "📦 Building Jekyll Docker image..."
docker build -t jekyll-local .

# Run the Jekyll server
echo "🌐 Starting Jekyll server at http://localhost:4000"
echo "Press Ctrl+C to stop the server"
docker run --rm -p 4000:4000 -v "$(pwd)":/srv/jekyll jekyll-local
