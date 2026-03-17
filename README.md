---

# Week 3 - Docker and PostgreSQL

## Overview

This week containerises the application using Docker and connects it to a PostgreSQL database using Docker Compose.

---

## Features

- Dockerfile for Flask app  
- Docker Compose setup  
- PostgreSQL integration  
- Environment-based database configuration  

---

## How to Run (Docker)

```bash
docker compose up --build
## Test API

```bash
curl http://127.0.0.1:6400/api/v1/health
```

---

## Example

### Create a todo:

```bash
curl -X POST http://127.0.0.1:6400/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"week3 docker"}'
```

### Get todos:

```bash
curl http://127.0.0.1:6400/api/v1/todos
```


