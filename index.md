---
layout: default
title: Home
---

# Welcome to Johann Nishant's GitHub Page

This is a simple GitHub Pages site built with Jekyll. Here you can find information about web development and deployment.

## System Architecture Example

Here's an example of a modern web application architecture:

![System Architecture Flow]({{ '/assets/images/system-architecture.svg' | relative_url }})

*This diagram shows the flow from client requests through Cloudflare Workers to AWS infrastructure.*

## Adding Images to Your Jekyll Site

To add images to your Jekyll site, follow these steps:

1. **Place images in the `assets/images/` directory**
2. **Use Jekyll's `relative_url` filter for proper linking**:
   ```markdown
   ![Alt text]({{ '/assets/images/your-image.jpg' | relative_url }})
   ```
3. **Supported formats**: JPG, PNG, GIF, SVG, WebP
4. **Best practices**:
   - Use descriptive alt text for accessibility
   - Optimize images for web (compress before uploading)
   - Use SVG for diagrams and simple graphics
   - Consider responsive images for mobile devices

## Simple Web Server Deployment Guide

Here's a basic guide for deploying a simple web server:

### 1. Choose Your Web Server
- **Apache HTTP Server** - Popular, feature-rich
- **Nginx** - High-performance, lightweight
- **Node.js** - JavaScript-based server
- **Python HTTP Server** - Simple for development

### 2. Basic Setup Steps
1. Install your chosen web server
2. Configure the server settings
3. Place your HTML/CSS/JS files in the web root directory
4. Start the server
5. Test your site in a browser

### 3. Example Commands
```bash
# Python simple server (for development)
python -m http.server 8000

# Node.js simple server
npx http-server

# Apache (Ubuntu/Debian)
sudo apt install apache2
sudo systemctl start apache2

# Nginx (Ubuntu/Debian)
sudo apt install nginx
sudo systemctl start nginx
```

### 4. Security Considerations
- Keep your server software updated
- Use HTTPS with SSL certificates
- Configure firewall rules
- Regular security audits

## Recent Posts

{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}