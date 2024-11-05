import fastapi
from fastapi import Response
import uvicorn, os



app = fastapi.FastAPI()



@app.get("/")
async def main_page(response: Response):
    return {"sdsd": "sdsdsd"}



if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=int(os.environ.get("PORT")))
    except KeyboardInterrupt:
        print("stoped!")
