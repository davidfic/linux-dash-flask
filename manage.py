from flask.ext.script import Manager
from app import app
from app import data_gathering

manager = Manager(app)

@manager.command
def run():
    app.run(debug=True, host='0.0.0.0')

@manager.command
def test_os():
    print data_gathering.get_os()

@manager.command
def get_disk_usage():
    return data_gathering.get_disk_usage()

if __name__ == '__main__':
        manager.run()
