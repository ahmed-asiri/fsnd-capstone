import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app)
  

  @app.after_request
  def after_request(response):
      response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type,Authorization,true'
      )
      response.headers.add(
          'Access-Control-Allow-Methods',
          'GET,PATCH,POST,DELETE,OPTIONS'
      )

      return response
  

  @app.route('/actors')
  def get_actors():
      pass


  @app.route('/movies')
  def get_movies():
      pass


  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  def delete_actor(actor_id):
      pass


  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):
      pass


  @app.route('/movies', methods=['POST'])
  def create_movie():
      pass


  @app.route('/actors', methods=['POST'])
  def create_actor():
      pass
  

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  def edit_actor(actor_id):
      pass


  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  def edit_movie(movie_id):
      pass

  return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)