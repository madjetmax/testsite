import fastapi
from fastapi import Response
import uvicorn, os



app = fastapi.FastAPI()



@app.get("/")
async def main_page(response: Response):
    return {"sdsd": "sdsdsd"}



