import hmac
import logging

from fastapi import APIRouter, Header, HTTPException, Request

from app.core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/{source}")
async def receive(
    source: str,
    request: Request,
    x_webhook_secret: str | None = Header(default=None),
) -> dict:
    if settings.webhook_secret and not hmac.compare_digest(
        x_webhook_secret or "", settings.webhook_secret
    ):
        raise HTTPException(status_code=401, detail="invalid secret")

    payload = await request.json()
    logger.info("webhook %s: %s", source, payload)
    return {"received": True, "source": source}
