from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI "}

# To run 
# uvicorn main:app --reload
uvicorn main:app --reload
# Or
python -m uvicorn main:app --reload
