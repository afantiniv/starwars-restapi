from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    climate = db.Column(db.String(150), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(150), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Planet {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "population": self.population,
            "gravity": self.gravity,
            "orbital period": self.orbital_period,
            "rotation period": self.rotation_period,
            "surface water": self.surface_water
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    birth_year = db.Column(db.String(150), nullable=False)
    eye_color = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(150), nullable=False)
    hair_color = db.Column(db.String(150), nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    skin_color = db.Column(db.String(150), nullable=False)
    homeworld = db.Column(db.Integer, db.ForeignKey("planets.id"))
    planets = db.relationship(Planets)

    def __repr__(self):
        return f'<People {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            "name":self.name,
            "birth year":self.birth_year,
            "eye color":self.eye_color,
            "gender":self.gender,
            "hair color":self.hair_color,
            "mass":self.mass,
            "height":self.height,
            "skin color":self.skin_color,
            "homeworld":self.homeworld
        }



class FavPeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    people = db.relationship(People)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    user=db.relationship(User)

    def __repr__(self):
        return '<Favorites %r>' % self.id
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "people_fav id": self.people_id
        }

class FavPlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    planets = db.relationship(Planets)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    user=db.relationship(User)

    def __repr__(self):
        return '<Favorites %r>' % self.id
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "planets fav id": self.planets_id
        }