#!/bin/bash

 # Build the vuln image
cd server

if docker build -t api-cmd-injection . ; then
    # Running the image
    docker run -p 5000:5000 -d --name api-cmd api-cmd-injection:latest
else
    echo "Build failed. Docker run command will not be executed."
fi