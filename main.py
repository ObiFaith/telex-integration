from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/integration.json")
async def get_integration():
    """Serves the integration.json file."""
    return FileResponse("integration.json", media_type="application/json")