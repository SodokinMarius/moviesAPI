from movies.serializers import MovieSerializer

def test_valid_movie_serializer():
    valid_serializer_data={
         "title":"Sparta curs",
         "genre":"combat",
         "year": "2000"
         
     }
     
    serializer=MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data==valid_serializer_data
    assert serializer.data==valid_serializer_data
    assert serializer.errors=={}


def test_invalid_movie_serializer():
    invalid_serializer_data={
         "title":"Sparta curs",
         "genre":"combat",
         }
     
    serializer=MovieSerializer(data=invalid_serializer_data)
    assert not  serializer.is_valid()
    assert serializer.validated_data=={}
    assert serializer.data==invalid_serializer_data
    assert serializer.errors!={'year':"This field is required." }
    

     