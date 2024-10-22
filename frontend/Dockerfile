# Use Node.js 20 image
FROM node:20

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app files
COPY . .

# Build the app
RUN npm run build

# Expose port 3000 for the React app
EXPOSE 3000

# Start the application
CMD [ "npm", "start" ]
