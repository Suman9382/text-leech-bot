import os

API_ID    = os.environ.get("API_ID", "39256507")
API_HASH  = os.environ.get("API_HASH", "d9f88a9d3d207b8f6dfb08b762c30965")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
