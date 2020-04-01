from flask import Flask
from server.config import Configuration
from server.server.blueprint import servers

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(servers, url_prefix='/server')

