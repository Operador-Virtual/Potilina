# Potilina

Backend FastAPI.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

- Health: `GET /health`
- Webhooks: `POST /webhooks/{source}` (header `X-Webhook-Secret` si `WEBHOOK_SECRET` está definido)

## Tests

```bash
pytest
```
