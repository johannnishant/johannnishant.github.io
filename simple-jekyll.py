#!/usr/bin/env python3
"""
Simple Jekyll-like static site generator for local development
This script processes Markdown files and serves them locally
"""

import os
import re
import json
import http.server
import socketserver
from datetime import datetime
from pathlib import Path
import markdown
from jinja2 import Template

class SimpleJekyll:
    def __init__(self, source_dir=".", dest_dir="_site"):
        self.source_dir = Path(source_dir)
        self.dest_dir = Path(dest_dir)
        self.config = self.load_config()
        
    def load_config(self):
        """Load _config.yml"""
        config_file = self.source_dir / "_config.yml"
        if config_file.exists():
            # Simple YAML parser for basic config
            config = {}
            with open(config_file, 'r') as f:
                for line in f:
                    if ':' in line and not line.strip().startswith('#'):
                        key, value = line.split(':', 1)
                        config[key.strip()] = value.strip().strip('"\'')
            return config
        return {"title": "My Site", "url": "http://localhost:8000"}
    
    def process_markdown(self, content):
        """Process Markdown with front matter"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1].strip()
                markdown_content = parts[2].strip()
                
                # Simple front matter parser
                metadata = {}
                for line in front_matter.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip().strip('"\'')
                
                return metadata, markdown_content
        return {}, content
    
    def build_site(self):
        """Build the static site"""
        print("Building site...")
        
        # Create destination directory
        self.dest_dir.mkdir(exist_ok=True)
        
        # Process pages
        for md_file in self.source_dir.glob("*.md"):
            if md_file.name.startswith('_'):
                continue
                
            print(f"Processing {md_file.name}")
            
            with open(md_file, 'r') as f:
                content = f.read()
            
            metadata, markdown_content = self.process_markdown(content)
            
            # Convert markdown to HTML
            html_content = markdown.markdown(markdown_content, extensions=['codehilite', 'fenced_code'])
            
            # Simple template processing
            template = self.get_template(metadata.get('layout', 'default'))
            html = template.render(
                content=html_content,
                page=metadata,
                site=self.config,
                posts=self.get_posts()
            )
            
            # Write output
            output_file = self.dest_dir / f"{md_file.stem}.html"
            with open(output_file, 'w') as f:
                f.write(html)
        
        # Copy assets
        assets_dir = self.source_dir / "assets"
        if assets_dir.exists():
            import shutil
            dest_assets = self.dest_dir / "assets"
            if dest_assets.exists():
                shutil.rmtree(dest_assets)
            shutil.copytree(assets_dir, dest_assets)
        
        print(f"Site built in {self.dest_dir}")
    
    def get_template(self, layout_name):
        """Get template for layout"""
        layout_file = self.source_dir / "_layouts" / f"{layout_name}.html"
        
        if layout_file.exists():
            with open(layout_file, 'r') as f:
                return Template(f.read())
        else:
            # Default template
            return Template("""
<!DOCTYPE html>
<html>
<head>
    <title>{{ page.title if page.title else site.title }}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/assets/css/main.css">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about.html">About</a>
        </nav>
    </header>
    <main>
        {{ content }}
    </main>
    <footer>
        <p>&copy; {{ site.title }}</p>
    </footer>
</body>
</html>
            """)
    
    def get_posts(self):
        """Get blog posts"""
        posts = []
        posts_dir = self.source_dir / "_posts"
        if posts_dir.exists():
            for post_file in posts_dir.glob("*.md"):
                with open(post_file, 'r') as f:
                    content = f.read()
                metadata, _ = self.process_markdown(content)
                metadata['url'] = f"/{post_file.stem}.html"
                posts.append(metadata)
        return sorted(posts, key=lambda x: x.get('date', ''), reverse=True)

def serve_site(port=8000):
    """Serve the built site"""
    os.chdir("_site")
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory="_site", **kwargs)
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Server running at http://localhost:{port}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        serve_site()
    else:
        jekyll = SimpleJekyll()
        jekyll.build_site()
        print("\nTo serve the site, run: python3 simple-jekyll.py serve")
