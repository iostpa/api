from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from random import randint
import json


app = Flask(__name__, static_url_path='/static')
api = Api(app)
CORS(app)

class Page(Resource):
    def get(self):
        return {'message': 'This is the home page! The following endpoints are available below this message',
                'endpoints': "/uma /touhou /horse"}
        
# thanks https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files
class Horse(Resource):
   def get(self):
       return {'image_url': f'http://127.0.0.1:8000/static/horse/{randint(1,10)}.jpg'}
        
# thanks https://stackoverflow.com/questions/52645142/selecting-random-values-from-a-json-file
class Uma(Resource):
    def get(self):
        def random_uma():
            with open('api/json/uma.json') as fp:
                data = json.load(fp)
                result = data["results"]
                random_index = randint(0, len(result)-1)
                return result[random_index]
        return random_uma()

class Touhou(Resource):
    def get(self):
        def random_touhou():
            with open('api/json/touhou.json') as fp:
                data = json.load(fp)
                result = data["results"]
                random_index = randint(0, len(result)-1)
                return result[random_index]
        return random_touhou()

api.add_resource(Page, '/')
api.add_resource(Uma, '/uma')
api.add_resource(Touhou, '/touhou')
api.add_resource(Horse, '/horse')

# Add 404 error handler
@app.errorhandler(404)
def not_found(error):
    return {'message': 'This does not exist!',
            'code': 404}, 404