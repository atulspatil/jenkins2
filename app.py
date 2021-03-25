from flask import Flask
server = Flask(__name__)


@server.route("/")
def hello():
    return "This is first Jenkins project !"


if __name__ == "__main__":
    server.run()
