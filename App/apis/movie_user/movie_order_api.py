from flask_restful import Resource
from App.apis.movie_user.utils import login_require, require_permission
from App.models.movie_user.movie_user_model import VIP_USER


class MovieOrdersResource(Resource):

    @login_require
    def post(self):
        return {"status": "200", "msg": "log"}


class MovieOrderResource(Resource):

    @require_permission(VIP_USER)
    def put(self, order_id):
        return {"status": 200, "msg": "update success"}