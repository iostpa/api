from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from random import randint
from werkzeug.middleware.proxy_fix import ProxyFix
import json
import os


app = Flask(__name__, static_url_path='/static')
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
api = Api(app)
cors = CORS(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri=(os.getenv("MONGO")),
    strategy="fixed-window",
)

class Page(Resource):
    def get(self):
        return {'message': 'This is the home page! The following endpoints are available below this message. If you have any issues or want me to add more then please contact me.',
                'endpoints': "/uma /touhou /horse"}
        
# thanks https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files
class Horse(Resource):
    @limiter.limit("3/second", error_message="Slow down! You've reached the rate limit.")
    def get(self):
       return {'image_url': f'https://api.iostpa.com/static/horse/{randint(1,10)}.jpg'}
        
# thanks https://stackoverflow.com/questions/52645142/selecting-random-values-from-a-json-file
class Uma(Resource):
    @limiter.limit("3/second", error_message="Slow down! You've reached the rate limit.")
    def get(self):
        def random_uma():
            with open('api/json/uma.json') as fp:
                data = json.load(fp)
                result = data["results"]
                random_index = randint(0, len(result)-1)
                return result[random_index]
        return random_uma()

class Touhou(Resource):
    @limiter.limit("3/second", error_message="Slow down! You've reached the rate limit.")
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

@app.errorhandler(404)
def not_found(error):
    return {'message': 'This does not exist!',
            'code': 404}, 404