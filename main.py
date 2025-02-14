from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime
app = FastAPI()

#Consualtar datos
class Movie(BaseModel):
    id: int
    title: str  
    overview: str  
    year: int  
    rating: float  
    categoria: str 

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)  
    overview: str = Field(min_length=15, max_length=60)
    year: int  =Field(le=datetime.date.today().year, ge=1999)
    rating: float  = Field(ge=1, le=10)
    categoria: str = Field(min_length=5, max_length=20)
#gt greater than
#ge greater than or equal
#lt less than
#le less than or equal menor o igual


# datos por defecto
    model_config = {
        'json_schema_extra':{
            'example':{
                'id':1,
                'title':'My movie',
                'overview':'esta vaina es seria compare..',
                'year':2000,
                'rating':8,
                'categoria':'Acción'
            }
        }
    }



class MovieUpdate(BaseModel):
    title: str  
    overview: str  
    year: int  
    rating: float  
    categoria: str 


movies: List[Movie] = []

@app.get("/", tags=['Home'])
async def home():
    return {"message": "Hello WorldPress"}

@app.get("/movies", tags=['Movies'])
async def get_movies() -> List[Movie]:
    return [movie.model_dump()for movie in movies]

@app.get("/movies/{id}", tags=['Movies'])

async def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie["id"] == id:
            return movie.model_dump()
    return[]
    
@app.get("/movies/", tags=['Movies'])

async def get_movie_by_category(category: str, year: int) -> Movie:
     for movie in movies:
        if movie["category"] == category:
            return movie.model_dump()
        
     return[]

@app.post('/movies', tags=['Movies'])

def create_movie(movie: MovieCreate)-> List[Movie]:

    movies.append(movie)
    return [movie.model_dump()for movie in movies]

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate)-> List[Movie]:
  for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.categoria
  return [movie.model_dump()for movie in movies]

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int)-> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return [movie.model_dump()for movie in movies]