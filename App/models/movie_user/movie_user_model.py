from App.ext import db
from App.models import BaseModel

from werkzeug.security import check_password_hash, generate_password_hash


class MovieUser(BaseModel):
    user_name = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=None)


    @property
    def password(self):
        raise Exception("Can't access")

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)