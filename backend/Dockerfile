FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x wait-for-postgres.sh

CMD ["./wait-for-postgres.sh"]
