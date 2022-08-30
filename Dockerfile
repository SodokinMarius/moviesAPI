# pull official base image
#Image slim-buster de python
FROM python:3.9.5-slim-buster 

# set working directory | Repertoire de travail 
WORKDIR /usr/src/drf_learningProject

# set environment variables | Deux variables d'environnnements ==( python -B et python -u)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# install system dependencies  | for the database configuration
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

#copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/drf_learningProject/entrypoint.sh
RUN chmod +x /usr/src/drf_learningProject/entrypoint.sh       

# add app | Copie du projet django même
COPY drf_learningProject .


#Execution du entrypoint.sh
ENTRYPOINT ["/usr/src/drf_learningProject/entrypoint.sh" ]

# set working directory | ceci est en fonction de l'environnement (Donc optionel)
#RUN mkdir -p /usr/src/drf_learningProject
#WORKDIR /usr/src/drf_learningProject