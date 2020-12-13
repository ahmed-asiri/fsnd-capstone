import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
from datetime import datetime
from auth import AuthError, requires_auth


def create_app(test_config=None):

    # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')

        return response

    @app.route('/actors')
    def get_actors():
        actors = Actor.query.all()
        if len(actors) == 0:
            abort(404)

        return jsonify({'success': True, 'actors': [actor.format()
                       for actor in actors]})

    @app.route('/movies')
    def get_movies():
        movies = Movie.query.all()
        if len(movies) == 0:
            abort(404)

        return jsonify({'success': True, 'actors': [movie.format()
                       for movie in movies]})

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({'success': True, 'actor_id': actor_id})

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({'success': True, 'movie_id': movie_id})

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(jwt):
        request_data = request.get_json()

        if ('name' not in request_data or
                'age' not in request_data
                or 'gender' not in request_data):
            abort(400)

        actor = Actor(name=request_data['name'], age=request_data['age'],
                      gender=request_data['gender'])
        actor.insert()

        return jsonify({'success': True, 'actor': actor.format(),
                       'actor_id': actor.id})

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        request_data = request.get_json()
        release = datetime.utcnow()
        if 'title' not in request_data:
            abort(400)

        if 'release_date' in request_data:
            release = request_data['release_date']

        movie = Movie(title=request_data['title'], release=release)
        movie.insert()

        return jsonify({'success': True, 'movie': movie.format(),
                       'movie_id': movie.id})

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(jwt, actor_id):
        request_data = request.get_json()

        actor = Actor.query.get(actor_id)

        if actor is None:
            abort(404)

        if 'name' in request_data:
            actor.name = request_data['name']

        if 'age' in request_data:
            actor.age = request_data['age']

        if 'gender' in request_data:
            actor.gender = request_data['gender']

        actor.update()

        return jsonify({'success': True, 'actor': actor.format(),
                       'actor_id': actor_id})

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def edit_movie(jwt, movie_id):
        request_data = request.get_json()

        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        if 'title' in request_data:
            movie.title = request_data['title']

        if 'release_date' in request_data:
            movie.release = request_data['release_date']

        movie.update()

        return jsonify({'success': True, 'movie': movie.format(),
                       'movie_id': movie_id})

    # Error handlers for 422, 400 and 404

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'unprocessable request'}), 422)

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'bad request'}), 400)

    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'resource not found'}), 404)

    @app.errorhandler(401)
    def unauthorized(error):
        return (jsonify({'success': False, 'error': 401,
                'message': 'unauthorized access'}), 401)

    @app.errorhandler(AuthError)
    def auth_error(error):
        return (jsonify({'success': False, 'error': error.status_code,
                'message': error.error['description']}),
                error.status_code)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
