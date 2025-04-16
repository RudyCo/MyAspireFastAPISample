import logging
import os
from fastapi import FastAPI, HTTPException, Response
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

debug = os.environ.get("DEBUG", "False").lower() == "true"
logging.basicConfig(
    level=logging.DEBUG if debug else logging.INFO
)
logger = logging.getLogger(__name__)
logger.info("Debug mode is %s", "ON" if debug else "OFF")

logger.info("Starting FastAPI application...")

app = FastAPI(title="FastAPI application")

@app.get("/")
async def read_root():
    msg = "Hello World!"
    logger.info(msg)
    return Response(content=str(msg), media_type="text/plain")

@app.get("/debug")
async def test_debug():
    msg = "Debug!"
    logger.debug(msg)
    return Response(content=str(msg), media_type="text/plain")

@app.get("/info")
async def test_info():
    msg = "Info!"
    logger.info(msg)
    return Response(content=str(msg), media_type="text/plain")

@app.get("/warning")
async def test_warning():
    msg = "Warning!"
    logger.warning(msg)
    raise HTTPException(status_code=500, detail=msg)

@app.get("/error")
async def test_error():
    msg = "Error!"
    logger.error(msg)
    raise HTTPException(status_code=500, detail=msg)

@app.get("/critical")
async def test_critical():
    msg = "Critical!"
    logger.critical(msg)
    raise HTTPException(status_code=500, detail=msg)