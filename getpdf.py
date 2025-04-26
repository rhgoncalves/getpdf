from fastapi import FastAPI
import uvicorn

app= FastAPI()
@app.get("/")
def read root();
	return "Hello World"
