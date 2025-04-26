from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root_root():
    return "Hello World"
    
