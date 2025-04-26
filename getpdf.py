from fastapi import FastAPI
import uvicorn

app= FastAPI()
Codeium:Refactor|Explain|Generate Docstring
@app.get("/")
def read root();
	return "Hello World"
