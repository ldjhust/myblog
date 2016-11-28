#coding=utf-8

from datetime import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap(app)
Moment(app)

@app.route('/')
def index():
    context = {
        'current_time': datetime.utcnow()
    }
    return render_template('index.html', **context)

@app.route('/user/<name>/')
def user(name):
    context = {
        'name': name
    }
    return render_template('user.html', **context)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
