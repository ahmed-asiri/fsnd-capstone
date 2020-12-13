# Full Stack Nanodegree Casting Agency Capstone Project
The Casting Agency is a full stack project that include backend and third-party Auth0 service. This project builded by me as a challenge to complete the requirments to finish the FSND scholarship nanodegree.
The idea of the project is to demonstrate my backend skills. So, i have create a varies API endpoints, testing them, integrate a third party auth0 service and deploying into Heroku.
The Technology used to build the project are Python and Flask micro-framework. For this Back-end i have applied the PEP-8 style.

## Getting Started

### Installing Dependencies

To start the project locally, you need to have the following tools:
1. Python3 and PIP (Back-end)

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the root of the directory and run:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

From within the `root` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```

#### Testing

To run the tests, run
```
dropdb capstone_test
createdb capstone_test
python test_app.py
```

## API Reference

### Introduction

The API builded to make users eable to perform CRUD operations on Casting Agency database easily. It have been builded using Flask micro-framework, which is Python framework.
This API was builded for the requirments of graduating of the FSND nanodegree of Udactiy.
All the responses of the API is in JSON format.

### Getting Started

#### Base URL

This project is deployed and available on Heroku:
```
https://fsnd-capstone-asiri.herokuapp.com
```

### Error

The API have clear and defined errors that will make the debug process easier for developers.

#### Error Types:

- 404 - Not Found
- 400 - Bad Request
- 422 - Unprocesaable
- 401 - Unauthorized

#### Error Response Example:

```
{
    "success": False,
    "error": 404,
    "message": "Resource Not Found"
}
```

### Endpoints Library

This section will contain all the endpoints with their response examples to make everything clear for the users of our API

#### GET /actors

- Return: return list of all the available actors.

- Sample Request: ```curl https://fsnd-capstone-asiri.herokuapp.com/actors```

- Arguments: None

- Sample Response:
    ```
    {
          "success": True,
          "actors": [
            {
              "id": 1,
              "name": "Ahmed Asiri",
              "gender": "male",
              "age": 22
            }, 
            {
              "id": 5,
              "name": "Fares Hadi",
              "gender": "male",
              "age": 26
            }
          ]
    }
    ```
#### GET /movies

- Return: return list of all the available movies.

- Sample Request: ```curl https://fsnd-capstone-asiri.herokuapp.com/movies```

- Arguments: None

- Sample Response:
    ```
    {
          "success": True,
          "movies": [
            {
              "id": 1,
              "title": "Titanic",
              "release": "6 Oct, 1988"
            }, 
            {
              "id": 4,
              "title": "Cyper Bunk",
              "release": "21 Nov, 2020"
            }
          ]
    }
    ```

#### DELETE /actors/id

- Return: 
    - the deleted actor ID and result of success state.

- Sample Request: ```curl -X "DELETE" https://fsnd-capstone-asiri.herokuapp.com/actors/2```

- Arguments: 
    - it take the id of the actor in the URL after the ```actors/```

- Sample Response:
    ```
    {
        "success": True,
        "actor_id": 2
    }
    ```

#### DELETE /movies/id

- Return: 
    - the deleted movie ID and result of success state.

- Sample Request: ```curl -X "DELETE" https://fsnd-capstone-asiri.herokuapp.com/movies/5```

- Arguments: 
    - it take the id of the movie in the URL after the ```movies/```

- Sample Response:
    ```
    {
        "success": True,
        "movie_id": 2
    }
    ```

#### POST /actors

- Return: 
    - the request success state.
    - the created actor object.
    - the ID of the created actor.

- Sample Request: 
    ```curl -d '{"name": "Omar Mohammed", "age": 30, "gender": "Male"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://fsnd-capstone-asiri.herokuapp.com/actors```

- Arguments: 
    - None

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 15,
            "name": "Omar Mohammed",
            "gender": "Male",
            "age": 30
        },
        "actor_id": 15
    }
    ```

#### POST /movies

- Return: 
    - the request success state.
    - the created movie object.
    - the ID of the created movie.

- Sample Request: 
    ```curl -d '{"title": "Lockdown"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://fsnd-capstone-asiri.herokuapp.com/movies```

- Arguments: 
    - None

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 87,
            "title": "Lockdown",
            "release": "7 Oct, 2020"
        },
        "movie_id": 87
    }
    ```

#### PATCH /actors

- Return:
    - the request success state.
    - the modified actor object.
    - the ID of the modified actor.

- Sample Request: 
    ```curl -d '{"name": "omar mohammed", "age": 28, "gender": "male"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://fsnd-capstone-asiri.herokuapp.com/actors/15```

- Arguments: 
    - the ID of the actor that need to modified.

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 15,
            "name": "omar mohammed",
            "gender": "male",
            "age": 28
        },
        "actor_id": 15
    }
    ```

#### PATCH /movies

- Return:
    - the request success state.
    - the modified movie object.
    - the ID of the modified movie.

- Sample Request: 
    ```curl -d '{"title": "lockdown"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://fsnd-capstone-asiri.herokuapp.com/movies/87```

- Arguments: 
    - the ID of the movie that need to modified.

- Required Headers:
    - the request need to include authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 87,
            "title": "lockdown",
            "release": "7 Oct, 2020"
        },
        "movie_id": 87
    }
    ```

## Authors

Ahmed Asiri authored the API endpoints at the (app.py) file, the unittest at the (test_app.py), the database models at (models.py), auth check at (auth.py) and the README.md file.
