from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()

# Define your routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Keep your uvicorn runner
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)