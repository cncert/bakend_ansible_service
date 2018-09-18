# encoding: utf-8

from flask import Flask
from flask_moment import Moment
from config import config
from flask_restful import Api
from flask_cors import CORS # 解决跨域请求
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO


moment = Moment()
api = Api()
async_mode = None  # 新添加支持websocket
socketio = SocketIO()  # 新添加支持websocket


def app_create(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    jwt = JWTManager(app)

    # 路由和其他处理程序定义
    # 注册蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    api.init_app(app)  # api初始化必须放在路由注册之后
    CORS(app)  # 跨域请求
    socketio.init_app(app=app, async_mode=async_mode)  # 新添加支持websocket

    return app
