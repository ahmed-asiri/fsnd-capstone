#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import unittest
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class AgencyTestCase(unittest.TestCase):

    """This class represents the agency's test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstone_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
                             'postgres', 'admin',
                             'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # binds the app to the current context

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()

            # create all tables

            self.db.create_all()

        self.new_actor = {'name': 'Joe Paiden', 'age': 35,
                          'gender': 'male'}
        self.new_movie = {'title': 'Titanic',
                          'release': datetime.utcnow()}

        # initiate the test database with dummy records.

        for i in range(5):
            actor = Actor(name=self.new_actor['name'],
                          age=self.new_actor['age'],
                          gender=self.new_actor['gender'])
            actor.insert()
        for i in range(5):
            movie = Movie(title=self.new_movie['title'],
                          release=self.new_movie['release'])
            movie.insert()

        self.director_token = os.getenv('CASTING_DIRECTOR_TOKEN')
        self.producer_token = os.getenv('EXECUTIVE_PRODUCER_TOKEN')

    def producer_header(self):
        return {'Authorization': 'Bearer {}'.format(self.producer_token)}

    def director_header(self):
        return {'Authorization': 'Bearer {}'.format(self.director_token)}

    def tearDown(self):
        """Executed after reach test"""

        pass

    # MOVIE API Endpoint TEST cases

    def test_creating_movie_success(self):

        # adding movie with the PRODUCER TOKEN, he have the permissions

        response = self.client().post(
                                      '/movies',
                                      headers=self.producer_header(),
                                      json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_creating_movie_failure(self):

        # trying to create movie with DIRECTOR TOKEN,
        # where he does not have permissions

        response = self.client().post(
                                      '/movies',
                                      headers=self.director_header(),
                                      json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie_success(self):

        # deleting movie with the PRODUCER TOKEN, he have the permissions

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.producer_header())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_failure(self):

        # trying to delete movie with DIRECTOR TOKEN,
        # where he does not have permissions

        movie = Movie.query.all()[0]
        response = self.client().delete('/movies/{}'.format(movie.id),
                                        headers=self.director_header())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movies_success(self):

        # patching movie with the PRODUCER TOKEN, he have the permissions

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       headers=self.producer_header(),
                                       json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_failure(self):

        # patching movie with no TOKEN, its not public, so 401

        movie = Movie.query.all()[0]
        response = self.client().patch('/movies/{}'.format(movie.id),
                                       json=self.new_movie)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    # ACTOR API Endpoint TEST cases

    def test_creating_actor_success(self):

        # adding actor with the PRODUCER TOKEN, he have the permissions

        response = self.client().post('/actors',
                                      headers=self.producer_header(),
                                      json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_creating_actor_failure(self):

        # trying to create actor with NO TOKEN, where its not PUBLIC API

        response = self.client().post('/actors', json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor_success(self):

        # deleting actor with the PRODUCER TOKEN, he have the permissions

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id),
                                        headers=self.producer_header())
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_failure(self):

        # trying to delete actor with NO TOKEN, where its not PUBLIC API

        actor = Actor.query.all()[0]
        response = self.client().delete('/actors/{}'.format(actor.id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_actor_success(self):

        # patching actor with the PRODUCER TOKEN, he have the permissions

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       headers=self.producer_header(),
                                       json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor_failure(self):

        # patching actor with no TOKEN, its not public, so 401

        actor = Actor.query.all()[0]
        response = self.client().patch('/actors/{}'.format(actor.id),
                                       json=self.new_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)

    # PUBLIC API

    def test_getting_movies_success(self):

        # public endpoint that can be accessed without token

        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_getting_actors_success(self):

        # public endpoint that can be accessed without token

        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


if __name__ == '__main__':
    unittest.main()
