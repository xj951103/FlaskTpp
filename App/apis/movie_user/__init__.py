from flask_restful import Api

from App.apis.movie_user.hello_api import Hello

client_api = Api(prefix="/user")

client_api.add_resource(Hello, "/hello")