from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"status": 200, "msg": "hello"}
