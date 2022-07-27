from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "nevo"
password = "1234"
facebook_friends=["Eitan","Yuval","Tal", "Niv", "Asil", "Amin"]

@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		if request.form['username'] == username and request.form['password'] == password:
			return redirect(url_for('home'))
	else:
		return render_template('login.html')
  
@app.route('/home')
def home():
	return render_template('home.html', facebook_friends= facebook_friends)

@app.route('/friend_exists/<string:name>', methods = ['GET','POST'])
def friends(name):
	if name in facebook_friends:
		boolian1 = "True"
	else:
		boolian1 = "False"
	return render_template('friend_exists.html', n = name, boolian = boolian1)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)