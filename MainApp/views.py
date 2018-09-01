# coding:utf-8
from flask import Blueprint, render_template, request

blue = Blueprint('main', __name__)


@blue.route('/')
def home():
    return '<h3> wang zhe rong yao<h3>'


@blue.route('/login/')
def login():
    return render_template('login.html')


@blue.route('/user/<int:id>/<string:name>/')
def get_user(id, name):
    print(type(id), type(name))
    return '你查询的用户id为:{},姓名为{}'.format(id, name)


@blue.route('/blob/<any(update,delete,add):method>/<uuid:id>/')
def modefyBlob(method, id):
    return '你要执行,<strong>{}</strong>操作:{}'.format(method, id)


@blue.route('/admin/<path:url>/')
def admingMgr(url):
    print(url)
    return '正在请求后台的url地址:{}'.format(url)


# methods=('POST', 'PUT', 'DELETE')指定请求允许的方法(默认'GET','OPTIONS','HEAD')
@blue.route('/cart/')
def cart():
    print(request.method)  # request请求对象
    print(request.args)  # args是url中请求参数
    print(request.remote_addr)  # remote_addr 是请求客户端的IP
    print(request.base_url)  # 服务器的host和port
    return '''<p>除了查询以后的所有功能:</p>
            <ul><li>请求方法:{}</li>
                <li>GET请求参数:{}</li>
                <li>客户端IP地址:{}</li>
            </ul>
    '''.format(request.method, request.args, request.remote_addr, request.base_url)


@blue.route('/regist/',methods=['POST'])
def regist():
    if request.method == 'GET':
        username = request.args.get('username')
    elif request.method =="POST":
        username = request.form.get('username')
    return '{}注册成功'.format(username)
