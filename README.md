# Car-Api - Simple REST API for NetGuru

### Requirements
- python3 ```$ sudo apt install python3```
- pip ```$ sudo apt install python3-pip```
- docker.io ```$ sudo apt install docker.io```
- docker-compose ```$ sudo pip install docker-compose```

### How to use
To run the Car-Api simply run this command inside the project directory:
```
$ docker-compose up --build
```

### Endpoints:

-------------------------------------------------------------

**POST /cars/**

Content-Type: application/json;charset=UTF-8

{

  "make" : "Volkswagen",

  "model" : "Golf",

}

-------------------------------------------------------------

**DELETE /cars/{  id }/**

-------------------------------------------------------------

**POST /rate/**

Content-Type: application/json;charset=UTF-8

{

  "car_id" : 1,

  "rating" : 5,

}

-------------------------------------------------------------

**GET /cars/**

-------------------------------------------------------------

**GET /popular/**

-------------------------------------------------------------


### Stack:
Python, Django, REST framework and Docker(docker-compose).


### Files description
1. `Dockerfile` - Text document that contains all the commands a user could call on the command line to assemble an image.
2. `manage.py` - Django application entry point (This file is used basically as a command-line utility and for deploying, debugging, or running the web application).
3. `docker-compose.yml` - Tool for defining and running multi-container Docker applications. Generic application entry point.
3. `db.sqlite3` - Main API sqlite3 database.
4. `requirements.txt` - Text file specifies what python packages are required to run the project you are looking at.