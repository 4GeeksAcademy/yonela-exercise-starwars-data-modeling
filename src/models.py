from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Association tables for many-to-many relationships
films_people_association = Table(
    'films_people', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('person_id', Integer, ForeignKey('people.id'))
)

films_starships_association = Table(
    'films_starships', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

films_vehicles_association = Table(
    'films_vehicles', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

films_species_association = Table(
    'films_species', Base.metadata,
    Column('film_id', Integer, ForeignKey('species.id')),
    Column('species_id', Integer, ForeignKey('species.id'))
)

films_planets_association = Table(
    'films_planets', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

people_species_association = Table(
    'people_species', Base.metadata,
    Column('person_id', Integer, ForeignKey('people.id')),
    Column('species_id', Integer, ForeignKey('species.id'))
)

# Association tables for user favorites
user_favorite_planets = Table(
    'user_favorite_planets', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

user_favorite_species = Table(
    'user_favorite_species', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('species_id', Integer, ForeignKey('species.id'))
)

user_favorite_vehicles = Table(
    'user_favorite_vehicles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

user_favorite_starships = Table(
    'user_favorite_starships', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

user_favorite_films = Table(
    'user_favorite_films', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('film_id', Integer, ForeignKey('films.id'))
)

# People Model
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(10))
    eye_color = Column(String(50))
    gender = Column(String(10))
    hair_color = Column(String(50))
    height = Column(Integer)
    mass = Column(Float)
    skin_color = Column(String(50))
    homeworld = Column(String(250))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

    films = relationship("Films", secondary=films_people_association, back_populates="characters")
    species = relationship("Species", secondary=people_species_association, back_populates="people")
    starships = relationship("Starships", secondary=films_starships_association, back_populates="pilots")
    vehicles = relationship("Vehicles", secondary=films_vehicles_association, back_populates="pilots")


# Films Model
class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode_id = Column(Integer)
    opening_crawl = Column(String(500))
    director = Column(String(100))
    producer = Column(String(100))
    release_date = Column(DateTime)
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

    characters = relationship("People", secondary=films_people_association, back_populates="films")
    planets = relationship("Planets", secondary=films_planets_association, back_populates="films")
    starships = relationship("Starships", secondary=films_starships_association, back_populates="films")
    vehicles = relationship("Vehicles", secondary=films_vehicles_association, back_populates="films")
    species = relationship("Species", secondary=films_species_association, back_populates="films")


# Starships Model
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    hyperdrive_rating = Column(String(50))
    MGLT = Column(String(50))
    starship_class = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

    films = relationship("Films", secondary=films_starships_association, back_populates="starships")
    pilots = relationship("People", secondary=films_starships_association, back_populates="starships")


# Vehicles Model
class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    vehicle_class = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

    films = relationship("Films", secondary=films_vehicles_association, back_populates="vehicles")
    pilots = relationship("People", secondary=films_vehicles_association, back_populates="vehicles")


# Species Model
class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(100))
    designation = Column(String(50))
    average_height = Column(String(50))
    skin_colors = Column(String(100))
    hair_colors = Column(String(100))
    eye_colors = Column(String(100))
    average_lifespan = Column(String(50))
    homeworld = Column(String(250))
    language = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

    people = relationship("People", secondary=people_species_association, back_populates="species")
    films = relationship("Films", secondary=films_species_association, back_populates="species")


# Planets Model
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(50))
    diameter = Column(String(50))
    gravity = Column(String(50))
    orbital_period = Column(String(50))
    population = Column(String(50))
    rotation_period = Column(String(50))
    surface_water = Column(String(50))
    terrain = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String(250))

    films = relationship("Films", secondary=films_planets_association, back_populates="planets")
    residents = relationship("People", back_populates="homeworld")


# User Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime)

    # Relationships with the favorites
    favorite_planets = relationship('Planets', secondary=user_favorite_planets, back_populates='favorited_by_users')
    favorite_species = relationship('Species', secondary=user_favorite_species, back_populates='favorited_by_users')
    favorite_vehicles = relationship('Vehicles', secondary=user_favorite_vehicles, back_populates='favorited_by_users')
    favorite_starships = relationship('Starships', secondary=user_favorite_starships, back_populates='favorited_by_users')
    favorite_films = relationship('Films', secondary=user_favorite_films, back_populates='favorited_by_users')


# Update Planets, Species, Vehicles, etc., to include 'favorited_by_users'
Planets.favorited_by_users = relationship('User', secondary=user_favorite_planets, back_populates='favorite_planets')
Species.favorited_by_users = relationship('User', secondary=user_favorite_species, back_populates='favorite_species')
Vehicles.favorited_by_users = relationship('User', secondary=user_favorite_vehicles, back_populates='favorite_vehicles')
Starships.favorited_by_users = relationship('User', secondary=user_favorite_starships, back_populates='favorite_starships')
Films.favorited_by_users = relationship('User', secondary=user_favorite_films, back_populates='favorite_films')