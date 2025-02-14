from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List
app = FastAPI()

#Consualtar datos
class Movie(BaseModel):
    id: int
    title: str  
    overview: str  
    year: int  
    rating: float  
    categoria: str 

class MovieUpdate(BaseModel):
    title: str  
    overview: str  
    year: int  
    rating: float  
    categoria: str 


movies = [
    {
        "id":1,
        "title":"Avatar",
        "overview":"En un exuberante planeta llamado pandora viven los Na vi ...",
        "year": "2009",
        "rating": 7.9,
        "category":"Accion"

    },
    {
        "id":2,
        "title":"Avater",
        "overview":"En un exuberante planeta llamado pandora viven los Na vi ...",
        "year": "2009",
        "rating": 7.9,
        "category":"Comedia*"

    }
]

@app.get("/", tags=['Home'])
async def home():
    return {"message": "Hello WorldPress"}

@app.get("/movies", tags=['Movies'])
async def get_movies() -> List[Movie]:
    return movies

@app.get("/movies/{id}", tags=['Movies'])

async def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie["id"] == id:
            return movie
    return[]
    
@app.get("/movies/", tags=['Movies'])

async def get_movie_by_category(category: str, year: int) -> Movie:
     for movie in movies:
        if movie["category"] == category:
            return movie
        
     return[]

@app.post('/movies', tags=['Movies'])

def create_movie(movie: Movie)-> List[Movie]:

    movies.append(movie.model_dump())
    return movies

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate)-> List[Movie]:
  for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.categoria
  return movies

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int)-> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return movies