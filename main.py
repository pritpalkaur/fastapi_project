from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/anime/{title}")
def get_anime(title: str):
    return {"title": title, "status": "searching..."}
