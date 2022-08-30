from django.urls import reverse 
import json

def test_hello():
    assert "hello_world"=="hello_world"
    assert "two" != "bar"


def test_ping(client):
    url=reverse("ping")
    response=client.get(url)
    content=json.loads(response.content)

    assert response.status_code==200
    assert content["ping"]=="Bonjour, Bien j'espère !!!"
   