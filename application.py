from flask import Flask, render_template, request, redirect, url_for, session, Response
import os
application = Flask(__name__)

@application.route('/')
@application.route('/index')
def register():
	username = os.environ.get("Username")
	return render_template('index.html', username = username)

if __name__ == '__main__':
    application.run(host="0.0.0.0",port=3000)