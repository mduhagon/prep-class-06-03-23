import os
from flask_mongoengine import MongoEngine

# library documentation: https://pypi.org/project/flask-mongoengine/
# tutorial on how to do simple things with it: https://pythonbasics.org/flask-mongodb/#MongoDB-example
db = MongoEngine()

'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    database_path = os.getenv('DATABASE_USER')
    app.config['MONGODB_SETTINGS'] = {
        'host': os.getenv('DATABASE_HOST'),
        'username': os.getenv('DATABASE_USER'),
        'password': os.getenv('DATABASE_PASS')
    }
    db.init_app(app)

'''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    # TODO: reimplement this for flask_mongoengine
    pass


class SampleLocation(db.Document):
    id = db.StringField()
    description = db.StringField(primary_key=True)
    location_longitude = db.FloatField()
    location_latitude = db.FloatField()
    
    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "geom": self.geom
        }

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'location': {
                'lng': self.location_longitude,
                'lat': self.location_latitude
            }
        }         

    @staticmethod
    def get_items_within_radius(lat, lng, radius):  
        # Because flask_mongoengine does not really support geo-spatial functions or fields,
        # we cannot query MongoDB relative to a lat - lng and a max radious.
        # we get all locations all the time, which is extremely inneficient :(
        return [l.to_dict() for l in SampleLocation.objects]
     