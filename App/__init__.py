from flask import Flask

from App.settings import envs
from App.ext import init_ext
from App.apis import init_api


def create_app(env):
    app = Flask(__name__)

    # 初始化项目配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库
    init_ext(app)
    init_api(app)
    return app
