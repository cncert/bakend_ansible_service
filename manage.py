# encoding: utf-8
import os
from flask_script import Manager
from app1 import app_create
from flask_migrate import Migrate, MigrateCommand
from app1 import db, socketio


app = app_create(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)  # 使用Migrate将app与db关联


manager.add_command('db',MigrateCommand)
manager.add_command('run', socketio.run(app=app, host='0.0.0.0', port=5000))  # 新加入的内容，重写manager的run命令


if __name__ == '__main__':
    manager.run()
