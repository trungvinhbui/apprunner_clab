from flask import Flask, render_template, request, redirect, url_for, session, Response
import os
application = Flask(__name__)

@application.route('/')
@application.route('/index')
def register():
	username = os.environ.get("Username")
	version = "This is version 2 of our application"
	return render_template('index.html', username = username, version = version)

if __name__ == '__main__':
     application.run(host="0.0.0.0", port=5000, debug=True)
