# Stage 1: Build stage
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


# Stage 2: Runtime stage
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
EXPOSE 3000
CMD ["python", "app.py"]