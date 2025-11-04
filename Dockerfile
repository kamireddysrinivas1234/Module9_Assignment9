
# Simple runtime image for the FastAPI Calculator
FROM python:3.12-slim

WORKDIR /app

# If your existing project has requirements.txt, this will install them.
# Otherwise, these two ensure FastAPI runs.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt ||     pip install --no-cache-dir fastapi==0.115.0 uvicorn[standard]==0.30.6 jinja2==3.1.4 python-dotenv==1.0.1

# Copy the project (expects app/ folder at repo root)
COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
