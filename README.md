# React App with Backend

This is an example of a full-stack application that includes a **React frontend** and an **Express backend**, both containerized using Docker. The setup leverages **Docker Compose** to manage and orchestrate the two services.

### Table of Contents
1. [Project Structure](#project-structure)
2. [Services](#services)
   - [Backend](#backend)
   - [Frontend](#frontend)
3. [Prerequisites](#prerequisites)
4. [Setup and Running](#setup-and-running)
5. [Environment Variables](#environment-variables)
6. [Accessing the Application](#accessing-the-application)
7. [Useful Commands](#useful-commands)

## Project Structure

```
my-app/
├── backend/
│   ├── Dockerfile
│   ├── index.js
│   ├── package.json
│   └── README.md
├── frontend/
│   ├── Dockerfile
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── .env
│   ├── package.json
│   └── README.md
├── docker-compose.yml
└── README.md
```

## Services

### Backend
- **Service Name**: `backend`
- **Port**: `5000`
- **Description**: An Express.js backend service that exposes an API at `/api/hello` that returns "Hello from backend!".
- **Dockerfile**: Located in `./backend/Dockerfile`.

### Frontend
- **Service Name**: `frontend`
- **Port**: `3000`
- **Description**: A React.js frontend that fetches data from the backend service and displays the message returned by the API.
- **Dockerfile**: Located in `./frontend/Dockerfile`.

### Docker Compose Setup

The `docker-compose.yml` file defines two services:

- **`backend`**: Runs the Express backend and is accessible on port `5000`.
- **`frontend`**: Runs the React frontend on port `3000`, and it depends on the `backend` service to be available before it starts. It uses an environment variable (`REACT_APP_API_URL`) to interact with the backend.

### Excerpt from `docker-compose.yml`
```yaml
services:
  backend:
    build: ./backend
    ports:
      - '5000:5000'
    environment:
      - NODE_ENV=production

  frontend:
    build: ./frontend
    ports:
      - '3000:3000'
    environment:
      - REACT_APP_API_URL=http://backend:5000
    depends_on:
      - backend
```

## Prerequisites
Make sure you have the following installed on your machine:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup and Running

To build and run the application, follow these steps:

1. Clone the repository or download the project files.
2. Open a terminal in the root directory (where the `docker-compose.yml` file is located).
3. Run the following command to build and start both the frontend and backend services:

   ```bash
   docker-compose up --build
   ```

4. Docker will build the images for both services, start the containers, and expose them on the following ports:
   - **Backend**: `http://localhost:5000`
   - **Frontend**: `http://localhost:3000`

   The frontend will automatically fetch data from the backend and display it.

## Environment Variables

- The React frontend uses the `REACT_APP_API_URL` environment variable to interact with the backend service. This is defined in the `docker-compose.yml` as `http://backend:5000` where `backend` refers to the service name in the Docker network.
  
- The backend service can run in production mode using the `NODE_ENV=production` environment variable.

## Accessing the Application

- **Frontend**: Open a browser and go to `http://localhost:3000` to access the React app.
- **Backend**: You can directly access the backend API at `http://localhost:5000/api/hello` to verify the backend service is running.

## Useful Commands

- **Shut down the services**:
  ```bash
  docker-compose down
  ```

- **Rebuild the services** (if changes are made):
  ```bash
  docker-compose up --build
  ```

- **View logs** for both services:
  ```bash
  docker-compose logs -f
  ```

- **Run the services in the background** (detached mode):
  ```bash
  docker-compose up -d
  ```

---

This setup provides a complete Dockerized full-stack application. You can extend the backend API, add more frontend features, or introduce additional services into this Docker Compose setup based on your project needs.
