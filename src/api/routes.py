"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Planets, FavPeople, FavPlanet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/people/', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify({
        "people":list(map(lambda item: item.__repr__(),people))
            }), 200

@api.route('/people/<int:user_param>', methods=['GET'])
def get_people_id(user_param):
    people = People.query.filter(People.id==user_param).all()
    people_data= people[0].serialize()
    return jsonify({
        "people":people_data
            }), 200

@api.route('/planets/', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    return jsonify({
        "planets":list(map(lambda item: item.__repr__(),planets))
            }), 200

@api.route('/planets/<int:user_param>', methods=['GET'])
def get_planets_id(user_param):
    planets = Planets.query.filter(Planets.id==user_param).all()
    planets_data= planets[0].serialize()
    return jsonify({
        "planet":planets_data
            }), 200

@api.route('/users/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({
        "users": list(map(lambda item: item.serialize(), users))
    }), 200

@api.route('/users/<int:user_param>/favorite', methods=['GET'])
def get_favorites(user_param):
    user_fav_people = FavPeople.query.filter(FavPeople.user_id==user_param).all()
    user_fav_planets = FavPlanet.query.filter(FavPlanet.user_id==user_param).all()
    return jsonify({
        "Favorites People": list(map(lambda item: item.serialize(), user_fav_people)),
        "Favorites Planets": list(map(lambda item: item.serialize(), user_fav_planets))
    }), 200

@api.route('/users/<int:user_param>/favorite/people', methods=['GET'])
def get_favorites_people(user_param):
    user_fav_people = FavPeople.query.filter(FavPeople.user_id==user_param).all()
    return jsonify({
        "Favorites People": list(map(lambda item: item.serialize(), user_fav_people)),
    }), 200

@api.route('/users/<int:user_param>/favorite/planets', methods=['GET'])
def get_favorites_planets(user_param):
    user_fav_planets = FavPlanet.query.filter(FavPlanet.user_id==user_param).all()
    return jsonify({
        "Favorites Planets": list(map(lambda item: item.serialize(), user_fav_planets))
    }), 200

@api.route('/users/<int:user_param>/favorite/planet/<int:planet_id>', methods=['POST'])
def post_fav_planet(user_param, planet_id):
    newFavPlanet=FavPlanet(user_id=user_param, planets_id=planet_id)
    db.session.add(newFavPlanet)
    db.session.commit()

    return jsonify({"resp":"Todo creado con exito"}), 201

@api.route('/users/<int:user_param>/favorite/people/<int:people_index>', methods=['POST'])
def post_fav_people(user_param, people_index):
    newFavPeople=FavPeople(user_id=user_param, people_id=people_index)
    db.session.add(newFavPeople)
    db.session.commit()

    return jsonify({"resp":"Todo creado con exito"}), 201

@api.route('/users/<int:user_param>/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(user_param, planet_id):
    users_fav_planets = FavPlanet.query.filter(FavPlanet.user_id==user_param and FavPlanet.planets_id==planet_id).all()
    fav_planet_delete = users_fav_planets[0]
    db.session.delete(fav_planet_delete)
    db.session.commit()
    return jsonify({"resp":"Todo eliminado con exito"}), 200

@api.route('/users/<int:user_param>/favorite/people/<int:pple_id>', methods=['DELETE'])
def delete_people(user_param, pple_id):
    users_fav_people = FavPeople.query.filter(FavPeople.user_id==user_param and FavPeople.people_id==pple_id).all()
    fav_people_delete = users_fav_people[0]
    db.session.delete(fav_people_delete)
    db.session.commit()
    return jsonify({"resp":"Todo eliminado con exito"}), 200