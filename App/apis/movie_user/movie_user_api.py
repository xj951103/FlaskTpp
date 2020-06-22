import uuid

from flask_restful import Resource, reqparse, abort, fields, marshal_with, marshal
from App.models.movie_user import MovieUser
from App.apis.movie_user.model_utils import get_user
from App.apis.api_constant import HTTP_CREATE_SUCCESS, USER_ACTION_LOGIN, USER_ACTION_REGISTER, HTTP_SUCCESS
from App.ext import cache

base_parse = reqparse.RequestParser()
base_parse.add_argument("password", type=str, required=True, help="请输入密码！")
base_parse.add_argument("action", type=str, required=True, help="请确认请求参数！")

register_parse = reqparse.deepcopy(base_parse)
register_parse.add_argument("phone", type=str, required=True, help="请输入手机号！")
register_parse.add_argument("username", type=str, required=True, help="请输入用户名！")

login_parse = reqparse.deepcopy(base_parse)
login_parse.add_argument("phone", type=str, help="请输入手机号！")
login_parse.add_argument("username", type=str, help="请输入用户名！")

movie_fields = {
    "username": fields.String(attribute="user_name"),
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
        args = base_parse.parse_args()

        password = args.get("password")
        action = args.get("action").lower()

        if action == USER_ACTION_REGISTER:
            register_args = register_parse.parse_args()
            username = register_args.get("username")
            phone = register_args.get("phone")

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

        elif action == USER_ACTION_LOGIN:
            login_args = login_parse.parse_args()
            username = login_args.get("username")
            phone = login_args.get("phone")
            user = get_user(username) or get_user(phone)
            if not user or user.is_delete:
                abort(400, msg="用户不存在!")
            if not user.check_password(password):
                abort(401, msg="密码错误!")
            token = uuid.uuid4().hex

            cache.set(token, user.id, timeout=60 * 60 * 24 * 7)

            data = {
                "msg": "login success",
                "status": HTTP_SUCCESS,
                "token": token
            }

            return data

        else:
            abort(400, msg="请提供正确的参数！")


