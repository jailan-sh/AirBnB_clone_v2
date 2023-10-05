#!usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y nginx

mkdir -p /data/web_static/releases/test/ 
mkdir -p /data/web_static/shared/

echo "Hello world" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current 

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        location /hbnb_static {
            alias /data/web_static/current/;
            autoindex off;
        }
}" > /etc/nginx/sites-available/default

sudo chown -R ubuntu:ubuntu /data/

service nginx restart

exit 0
