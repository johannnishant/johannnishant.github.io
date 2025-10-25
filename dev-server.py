#!/usr/bin/env python3
"""
Simple local development server for Jekyll sites with live reload
Serves Markdown files directly without full Jekyll processing
"""

import os
import http.server
import socketserver
from pathlib import Path
import markdown
import re
import threading
import time
from urllib.parse import urlparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Global variable to track file changes
file_changed = False

class FileChangeHandler(FileSystemEventHandler):
    """Handle file system events for live reload"""
    def on_modified(self, event):
        global file_changed
        if not event.is_directory:
            # Only watch for markdown, css, js, and html files
            if event.src_path.endswith(('.md', '.css', '.js', '.html')):
                file_changed = True
                print(f"📝 File changed: {event.src_path}")

class JekyllDevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Handle live reload check endpoint
        if path == '/live-reload-check':
            self.handle_live_reload_check()
        # Serve index.md as index.html
        elif path == '/' or path == '/index.html':
            self.serve_markdown_file('index.md')
        elif path == '/about' or path == '/about.html':
            self.serve_markdown_file('about.md')
        else:
            # Try to serve the file normally
            super().do_GET()
    
    def handle_live_reload_check(self):
        """Handle live reload check requests"""
        global file_changed
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {'changed': file_changed}
        if file_changed:
            file_changed = False  # Reset the flag
        
        self.wfile.write(str(response).replace("'", '"').encode('utf-8'))
    
    def serve_markdown_file(self, filename):
        """Serve a Markdown file as HTML"""
        file_path = Path(filename)
        
        if not file_path.exists():
            self.send_error(404, f"File {filename} not found")
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process front matter
            metadata, markdown_content = self.process_front_matter(content)
            
            # Convert markdown to HTML
            html_content = markdown.markdown(markdown_content, extensions=['codehilite', 'fenced_code'])
            
            # Create full HTML page
            html = self.create_html_page(html_content, metadata)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, f"Error processing {filename}: {str(e)}")
    
    def process_front_matter(self, content):
        """Extract front matter from content"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1].strip()
                markdown_content = parts[2].strip()
                
                # Simple front matter parser
                metadata = {}
                for line in front_matter.split('\n'):
                    if ':' in line and not line.strip().startswith('#'):
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip().strip('"\'')
                
                return metadata, markdown_content
        return {}, content
    
    def create_html_page(self, content, metadata):
        """Create a complete HTML page"""
        title = metadata.get('title', 'My Jekyll Site')
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/assets/css/main.css">
    <style>
        /* Basic styling for development */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3 {{ color: #2c3e50; }}
        pre {{ background: #f8f9fa; padding: 15px; border-radius: 4px; overflow-x: auto; }}
        code {{ background: #f8f9fa; padding: 2px 4px; border-radius: 3px; }}
        nav {{ margin-bottom: 30px; }}
        nav a {{ margin-right: 20px; color: #3498db; text-decoration: none; }}
        nav a:hover {{ text-decoration: underline; }}
        footer {{ margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; color: #666; }}
        .live-reload-indicator {{
            position: fixed;
            top: 10px;
            right: 10px;
            background: #28a745;
            color: white;
            padding: 5px 10px;
            border-radius: 3px;
            font-size: 12px;
            z-index: 1000;
        }}
    </style>
</head>
<body>
    <div class="live-reload-indicator">🔄 Live Reload Active</div>
    
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        {content}
    </main>
    
    <footer>
        <p>&copy; 2024 {title}. Local development server.</p>
    </footer>
    
    <script>
        // Live reload functionality
        let lastModified = null;
        
        function checkForChanges() {{
            fetch('/live-reload-check', {{
                method: 'GET',
                cache: 'no-cache'
            }})
            .then(response => response.json())
            .then(data => {{
                if (data.changed) {{
                    console.log('🔄 File changed, reloading page...');
                    window.location.reload();
                }}
            }})
            .catch(error => {{
                console.log('Live reload check failed:', error);
            }});
        }}
        
        // Check for changes every 1 second
        setInterval(checkForChanges, 1000);
        
        // Initial check
        checkForChanges();
    </script>
</body>
</html>"""
        return html

def serve_site(port=8000):
    """Serve the Jekyll site locally with live reload"""
    print(f"🚀 Starting Jekyll development server with live reload...")
    print(f"📁 Serving from: {os.getcwd()}")
    print(f"🌐 Server running at http://localhost:{port}")
    print("📝 Supported files: index.md, about.md")
    print("🔄 Live reload: Active (watches .md, .css, .js, .html files)")
    print("🛑 Press Ctrl+C to stop")
    print("-" * 50)
    
    # Set up file watching
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        with socketserver.TCPServer(("", port), JekyllDevHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        observer.stop()
    finally:
        observer.join()

if __name__ == "__main__":
    serve_site()
