import json
from urllib import response 
import pytest 

from movies.models  import Movie 

@pytest.mark.django_db
def test_add_movie(client):
    url="/api/movies"
    movies=Movie.objects.all()
    
    #Verifions qu'il n'y a aucun film enregistré
    assert len(movies)==0
    
    data={
        "title":"Film Nigérian",
        "genre":"Education",
        "year":"2006",
    }
    
    response=client.post(url,data,content_type="application/json")
    
    #testons le retour de la requete
    
    assert response.status_code==201
    assert response.data["title"]=="Film Nigérian"
    
    #verifions que le nombre d'enregistrement est passé à 1
    movies=Movie.objects.all()
    
    assert len(movies)==1

#tests for getting a single movie

@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    url="/api/movies"    
    movies=Movie.objects.all()
    assert len(movies)==0
    
    response=client.post(url,{},content_type="application/json")
    
    assert response.status_code==400
    movies=Movie.objects.all()
    
    assert len(movies)==0

@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    url="/api/movies"    
    movies=Movie.objects.all()
    assert len(movies)==0
    data={ 
    "title":"Film Nigérian",
    "genre":"Education",
        }

    content_type="applcation/json"
    
    response=client.post(url,data,content_type)
    
    assert response.status_code==400
    movies=Movie.objects.all()
    assert len(movies)==0


    #test_get a sigle movie
    # Tests pour movies de val


'''def test_get_single_movie(client):
    url="/api/movies" 
    movie=Movie.objects.create(title="Encore du nouveau",genre="actuality",year='2000')
    response=client.get(f"{url}/{movie.id}/")
    assert response.status_code==200
    assert response.data["title"]=="Encore du nouveau" 
'''

#Now we are going to use the fixture created for adding new movie
@pytest.mark.django_db
def test_get_single_movie(client,add_movie):
    url="/api/movies" 
    movie=add_movie(title="Encore du nouveau",genre="actuality",year='2000')
    response=client.get(f"{url}/{movie.id}/")
    assert response.status_code==200
    assert response.data["title"]=="Encore du nouveau"
    
    
def test_get_single_movie_incorrect_id(client):
    url="/api/movies"
    response=client.get(f"{url}/foo/")
    assert response.status_code==404





    
    
    



    

