from flask_restful import Resource, reqparse, abort, fields, marshal_with, marshal
from App.models.movie_user import MovieUser
from App.apis.api_constant import HTTP_CREATE_SUCCESS

parse = reqparse.RequestParser()
parse.add_argument("username", type=str, required=True, help="请输入用户名！")
parse.add_argument("password", type=str, required=True, help="请输入密码！")
parse.add_argument("phone", type=str, required=True, help="请输入手机号！")

movie_fields = {
    "username": fields.String,
    "password": fields.String(attribute="_password"),
    "phone": fields.String
}

singe_movie_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(movie_fields)
}


class MovieUsersResource(Resource):

    def post(self):
        args = parse.parse_args()

        username = args.get("username")
        password = args.get("password")
        phone = args.get("phone")

        movie_user = MovieUser()
        movie_user.user_name = username
        movie_user.password = password
        movie_user.phone = phone

        if not movie_user.save():
            abort(400, msg="create fail")

        data = {
            "status": HTTP_CREATE_SUCCESS,
            "msg": "用户创建成功",
            "data": movie_user
        }

        return marshal(data, singe_movie_user_fields)
