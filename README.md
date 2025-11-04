
# FastAPI Calculator (with Tests, Logging, CI)

## Quickstart (Windows + VS Code)
```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install --with-deps
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

### Run tests
```powershell
pytest -q --cov=app --cov-report=term-missing --cov-fail-under=100
pytest -q -m e2e
```

Open http://localhost:5050

Pg admin setup 

General

Name: Local Postgres (any label you like)
Connection
Host name/address: db (Docker service name; use localhost if you’re connecting to a local Postgres outside Compose)\
Port: 5432
Maintenance database: postgres
Username: postgres
Password: postgres

SSL
SSL mode: Prefer (default) or Disable for local dev with no TLS
