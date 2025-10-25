# Local Development Guide

This guide will help you run your Jekyll site locally for development and testing.

## Method 1: Python Development Server (Recommended)

This method uses a simple Python server that processes Markdown files directly, avoiding Ruby/Jekyll installation issues.

### Prerequisites
- Python 3.6+ installed (usually pre-installed on macOS)
- Required Python packages: `markdown`

### Steps
1. **Install required packages**:
   ```bash
   pip3 install markdown
   ```

2. **Start the development server**:
   ```bash
   python3 dev-server.py
   ```

3. **Open your browser** and go to `http://localhost:8000`

4. **Stop the server** by pressing `Ctrl+C`

### Benefits
- ✅ No Ruby installation required
- ✅ Works on any system with Python
- ✅ Processes Markdown files directly
- ✅ Includes basic styling
- ✅ Supports front matter parsing

## Method 2: Using Docker (Alternative)

This method avoids Ruby installation issues and works consistently across different systems.

### Prerequisites
- Docker installed on your system
- Visit [Docker Installation Guide](https://docs.docker.com/get-docker/) if you don't have it

### Steps
1. **Run the local development server**:
   ```bash
   ./run-local.sh
   ```

2. **Open your browser** and go to `http://localhost:4000`

3. **Stop the server** by pressing `Ctrl+C`

### Benefits
- ✅ No Ruby installation required
- ✅ Consistent environment across systems
- ✅ Automatic live reload when files change
- ✅ Works on Windows, macOS, and Linux

## Method 3: Using Ruby/Bundler (Advanced)

If you prefer to use Ruby directly and have resolved the eventmachine compilation issues.

### Prerequisites
- Ruby 3.1+ installed via rbenv
- Bundler gem installed

### Steps
1. **Set up rbenv** (if not already done):
   ```bash
   export PATH="$HOME/.rbenv/bin:$PATH"
   eval "$(rbenv init -)"
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   ```

3. **Start the Jekyll server**:
   ```bash
   bundle exec jekyll serve --livereload
   ```

4. **Open your browser** and go to `http://localhost:4000`

## Development Workflow

1. **Make changes** to your Markdown files, CSS, or layouts
2. **Save the files** - The server will automatically serve updated content
3. **Refresh your browser** to see changes
4. **Test your changes** before committing

## File Structure for Development

```
├── _config.yml          # Site configuration
├── _layouts/            # HTML templates
├── _posts/              # Blog posts
├── assets/              # CSS, JS, images
├── index.md             # Home page
├── about.md             # About page
├── dev-server.py        # Python development server
├── run-local.sh         # Docker development script
└── Gemfile              # Ruby dependencies
```

## Common Commands

### Python Development Server
- **Start server**: `python3 dev-server.py`
- **Stop server**: `Ctrl+C`

### Docker Development
- **Start server**: `./run-local.sh`
- **Stop server**: `Ctrl+C`

### Ruby/Jekyll Development
- **Build site**: `bundle exec jekyll build`
- **Serve locally**: `bundle exec jekyll serve`
- **Serve with live reload**: `bundle exec jekyll serve --livereload`
- **Clean build**: `bundle exec jekyll clean && bundle exec jekyll build`

## Troubleshooting

### Python Server Issues
- Make sure Python 3.6+ is installed: `python3 --version`
- Install required packages: `pip3 install markdown`
- Check if port 8000 is available
- Verify Markdown files exist in the root directory

### Docker Issues
- Make sure Docker is running
- Check if port 4000 is available
- Try `docker system prune` to clean up

### Ruby Issues
- Use rbenv for Ruby version management
- Check Ruby version: `ruby --version`
- Try `bundle update` to update dependencies
- The eventmachine gem may have compilation issues on some systems

### Build Issues
- Delete `_site` folder and rebuild
- Check `_config.yml` for syntax errors
- Verify all required files exist

## Deployment

When you're ready to deploy:
1. **Commit your changes**: `git add . && git commit -m "Your changes"`
2. **Push to GitHub**: `git push origin main`
3. **GitHub Actions** will automatically build and deploy your site

Your site will be available at `https://johannnishant.github.io`

## Quick Start

For the fastest local development experience:

```bash
# Install Python dependencies
pip3 install markdown

# Start development server
python3 dev-server.py

# Open http://localhost:8000 in your browser
```