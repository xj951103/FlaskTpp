from App.ext import db
from App.models import BaseModel

from werkzeug.security import check_password_hash, generate_password_hash

from App.models.movie_user.model_constant import PERMISSION_NONE

COMMON_USER = 0
BLACK_USER = 1
VIP_USER = 2

class MovieUser(BaseModel):
    user_name = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_NONE)

    @property
    def password(self):
        raise Exception("Can't access")

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)

    def check_password(self, val):
        return check_password_hash(self._password, password=val)

    def check_permission(self, permission):
        if BLACK_USER & self.permission == BLACK_USER:
            return False
        else:
            return permission & self.permission == permission
