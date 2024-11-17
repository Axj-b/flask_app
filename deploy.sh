#!/bin/bash

# Define remote server details
REMOTE_USER="axj"
REMOTE_HOST="192.168.178.118"
REMOTE_DIR="/home/axj/web/flask_app"

# Upload all files in the current directory to the remote server
scp -r ./* "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_DIR}"

echo "Upload complete!"
