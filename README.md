# Dockerized Flask + PostgreSQL Project

This project demonstrates a simple Dockerized backend web application using Python Flask connected to a PostgreSQL database. It showcases how to:

- Dockerize your application components using Dockerfiles
- Use Docker Compose to manage multi-container services
- Inject environment variables securely using an external `.env` file
- Ensure database persistence with Docker volumes
- Control service dependencies and startup order
- Set restart policies for robustness

## Project Structure

```
project-root/
│
├── backend/
│   ├── app.py                # Flask application code
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Docker image definition for backend
│   └── wait-for-postgres.sh  # Script to wait for DB readiness before starting backend
│
├── .env                      # Environment variables (not committed to version control)
├── docker-compose.yml        # Docker Compose file to define and run services
└── README.md                 # This file
```

## Setting up Environment Variables with .env

The `.env` file contains your environment variables such as database connection credentials. It is **important NOT to commit** this file to public repositories to keep sensitive data secure.

### How to create the `.env` file

1. In the **project root** directory, create a file named `.env` (no filename prefix, just `.env`).

2. Add the following content (edit values as needed):

```
POSTGRES_DB=testdb
POSTGRES_USER=testuser
POSTGRES_PASSWORD=testpass
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

- `POSTGRES_DB`: The name of your PostgreSQL database.
- `POSTGRES_USER`: The username to connect as.
- `POSTGRES_PASSWORD`: The password for the user.
- `POSTGRES_HOST`: Hostname for the database (matches the Docker Compose service name `db`).
- `POSTGRES_PORT`: PostgreSQL port (default 5432).

3. **Add `.env` to your `.gitignore`** file to prevent committing it:

```
# .gitignore
.env
```

4. Optionally, create a `.env.example` file with placeholder or dummy values for reference:

```
POSTGRES_DB=your_db_name
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

This serves as a template for anyone setting up the project.

## How to Build and Run the Project

### Prerequisites

- Docker installed: https://docs.docker.com/get-docker/
- Docker Compose installed (often included with Docker Desktop)

### Steps

1. Clone or download the project source code.

2. Create the `.env` file as described above.

3. Open a terminal in the project root directory.

4. Run the following command to build and start the containers:

```bash
docker compose up --build
```

This will:

- Build the backend Docker image.
- Pull the PostgreSQL image.
- Start the database and backend services.
- The backend service uses `wait-for-postgres.sh` script to wait for the database to be ready before launching.

5. The Flask backend will be exposed on port `5000`.

## How to Use the Application

### API Endpoints

- **Add a name**

```
POST http://localhost:5000/add
Content-Type: application/json

{
  "name": "Alice"
}
```

Response:

```json
{
  "status": "name added",
  "name": "Alice"
}
```

- **Get all names**

```
GET http://localhost:5000/names
```

Response:

```json
{
  "names": ["Alice", "Bob", "Charlie"]
}
```

You can test the API with tools like `curl`, Postman, or any HTTP client.

Example with `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"Alice"}' http://localhost:5000/add
curl http://localhost:5000/names
```

## Notes

- The database data is persisted across container restarts using Docker volumes.
- You can stop the project with `docker compose down`.
- The backend automatically restarts on failure because of the restart policy.
- Ensure your `wait-for-postgres.sh` script is executable:

```bash
chmod +x backend/wait-for-postgres.sh
```

- For production use, consider using more robust database readiness checks or Docker healthchecks as needed.

## References

- Docker Compose environment variables: [https://docs.docker.com/compose/environment-variables/](https://docs.docker.com/compose/environment-variables/)
- Waiting for PostgreSQL readiness: [StackOverflow discussion](https://stackoverflow.com/questions/35069027/docker-wait-for-postgresql-to-be-running)
