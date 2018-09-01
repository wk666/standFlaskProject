# coding:utf-8

from flask import Flask
from MainApp import views

app = Flask(__name__)
app.env = 'development'

# 向'app中注册蓝图对象'
app.register_blueprint(views.blue)