#!/usr/bin/env bash
# Script to set up web servers for deploying web_static

# Update package list
sudo apt-get update

# Install nginx
sudo apt-get -y install nginx

# Allow Nginx HTTP through firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories for web_static
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a test HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Set ownership of directories
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve web_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx service
sudo service nginx restart
