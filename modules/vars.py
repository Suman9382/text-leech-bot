import os

API_ID    = os.environ.get("API_ID", "28578880")
API_HASH  = os.environ.get("API_HASH", "5f8c87efde57e01d12c0ce98ffdf5928")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
