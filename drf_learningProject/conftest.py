import os

from django.conf import settings

import pytest 

DEFAULT_ENGINE="django.db.backends.postgresql_psycopg2"

#fonction definissant les infos de la BD

@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES['default']={
        "ENGINE":os.environ.get("DB_TEST_ENGINE",DEFAULT_ENGINE),
       
        "HOST":os.environ.get("DB_TEST_HOST"),    
        "NAME":os.environ.get("DB_TEST_NAME"),
        "PORT":os.environ.get("DB_TEST_PORT"),

        "USER":os.environ.get("DB_TEST_USER"),
        "PASSWORD":os.environ.get("DB_TEST_PASSWORD"),
    }
    
@pytest.fixture(scope="module")
def foo():
    
    yield "bar"