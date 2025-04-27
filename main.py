from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")  # Use @app.get() instead of @app.route()
def root():
    return JSONResponse(content={"message": "Hello World"})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
