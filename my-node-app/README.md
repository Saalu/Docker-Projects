# Simple Node.js Docker Image Documentation

This document explains a basic Node.js application running in a Docker container, designed for beginners.

## Application Overview

This is a simple web server that displays a welcome message when you visit its homepage.

## app.js Explanation
const express = require('express');
const app = express();

-   **express**: A popular web framework for Node.js that makes creating servers easier
    
-   We import the express module and create an express application instance called  `app`

app.get('/', (req,res) => {
    res.send("Welcome to my Generation-GH AWS cloud Intensive program")
})

-   Sets up a route for the homepage (`/`)
    
-   When someone visits the homepage, the server responds with the welcome message
    
-   `req`  is the request object (incoming data)
    
-   `res`  is the response object (how we send data back)
   

const PORT = 3000;
const HOST = '0.0.0.0'; // Listen on all interface

-   `PORT`: The server will listen on port 3000
    
-   `HOST`: '0.0.0.0' means the server will accept connections from any network interface
    

app.listen(PORT, HOST, () => {
  console.log(`Server running at http://${HOST}:${PORT}/`);
});

-   Starts the server on the specified port and host
    
-   Prints a message to the console when the server starts successfully
    

## Dockerfile Explanation

FROM node:23-alpine

-   Starts with the official Node.js image (version 23) using Alpine Linux (a lightweight Linux distribution)


WORKDIR /app

-   Creates and sets  `/app`  as the working directory inside the container

COPY package.json /app/
COPY src /app/

-   Copies  `package.json`  from your local machine to  `/app/`  in the container
    
-   Copies the entire  `src`  directory (where your app.js is located) to  `/app/`  in the container

RUN npm install

-   Runs  `npm install`  inside the container to install all dependencies listed in package.json

CMD [ "node", "app.js" ]

-   Specifies the command to run when the container starts - in this case,  `node app.js`
    

## How It All Works Together

1.  The Dockerfile creates a container with Node.js installed
    
2.  It copies your application code into the container
    
3.  It installs dependencies (like Express)
    
4.  When the container starts, it runs your Node.js server
    
5.  The server listens on port 3000 and responds to requests
    

## Running the Application

To use this application:

1.  Build the Docker image:  `docker build -t my-node-app .`
    
2.  Run the container:  `docker run -p 3000:3000 my-node-app`
    
3.  Visit  `http://localhost:3000`  in your browser to see the welcome message
    

The  `-p 3000:3000`  maps port 3000 in the container to port 3000 on your host machine.