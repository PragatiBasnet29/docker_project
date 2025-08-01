#!/bin/sh
# Wait until PostgreSQL is ready
echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "Postgres started"

# Run the backend
exec python app.py
