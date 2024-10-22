# Use Node.js 20 image
FROM node:20

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Bind to port
EXPOSE 5000

# Start the application
CMD [ "npm", "start" ]
