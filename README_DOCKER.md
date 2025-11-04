
# FastAPI Calculator: Docker Add-on

## Quick Start
Place these files in the **root** of your FastAPI Calculator repo (same level as `app/` and `requirements.txt`).

### 1) Build & Run
```bash
docker-compose up --build
```
- API: http://localhost:8000
- pgAdmin: http://localhost:5050

### 2) Connect pgAdmin
Login with the credentials from `.env`.
Create a new server:
- Host: `db` (Docker service name)
- Port: `5432`
- User: `postgres`
- Password: `postgres`

Choose database: `fastapi_db`.

### 3) Run SQL (in pgAdmin → Query Tool)
Use the assignment’s SQL blocks to create tables, insert, query, update, and delete.
Take screenshots of the result grid or “X rows affected”.

### Tips
- Reset database: `docker-compose down -v` then `docker-compose up --build`
- If your repo lacks `requirements.txt`, the Dockerfile installs FastAPI/uvicorn automatically.
