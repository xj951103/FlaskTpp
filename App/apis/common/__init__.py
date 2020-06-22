from flask_restful import Api
from App.apis.common.common_cities_api import CitiesResource


common_api = Api(prefix="/common")

common_api.add_resource(CitiesResource, "/cities")


