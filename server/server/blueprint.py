from flask import Blueprint
from flask import render_template
from flask import request
import jarvis

jarvis = jarvis.Jarvis()
servers = Blueprint('server', __name__, template_folder='templates')

@servers.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jarvis.callback(request.form['text'])
        return 'ok'
    elif request.method == 'GET':
        return render_template('recognition.html')
