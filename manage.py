from flask_script import Manager
from MainApp import app

manager = Manager(app)  # 创建Manager管理器

if __name__ == '__main__':
    manager.run()
