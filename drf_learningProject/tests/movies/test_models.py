import pytest

from movies.models  import Movie

@pytest.mark.django_db #<--------  Important pour donner accès à la BD 
def test_movie_model():
    movie=Movie(title="Sparta Curs",genre="comique", year="1900")
    movie.save()
    
    assert movie.title=="Sparta Curs"
    assert movie.genre=="comique"
    assert movie.year=="1900"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie)==movie.title