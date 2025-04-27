from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")  # Use @app.get() instead of @app.route() (FastAPI's convention)
def root():
    return JSONResponse(content={"Ricardo": "Hello World"})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # Allow binding to any IP address in a container
