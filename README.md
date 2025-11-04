
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
