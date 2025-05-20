from fastapi import FastAPI

from models import MoviesResponse
from data import movies_data  # Import the movies_data

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/v1/movies", response_model=MoviesResponse)
def get_movies():
    return movies_data
