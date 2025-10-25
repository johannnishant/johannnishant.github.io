# Use the official Jekyll image
FROM jekyll/jekyll:4.3.0

# Set the working directory
WORKDIR /srv/jekyll

# Copy the Gemfile and Gemfile.lock
COPY Gemfile Gemfile.lock ./

# Install dependencies
RUN bundle install

# Copy the site files
COPY . .

# Expose port 4000
EXPOSE 4000

# Start Jekyll server
CMD ["jekyll", "serve", "--host", "0.0.0.0", "--port", "4000", "--livereload"]
