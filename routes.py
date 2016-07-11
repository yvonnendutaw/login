import os
from flask import Flask, flash, redirect, render_template, request, session, abort


app = Flask(__name__)

#displays the login screen ie the home screen
@app.route("/")
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello Boss!"


#validates the variables on login
@app.route('/login', methods=['POST'])
def admin_login():
	if request.form['password'] == 'python' and request.form['username'] == 'python':
		session['logged_in'] = True
	else:
		flash('wrong password! try again')
	return home()

@app.route('/test')
def test():
    POST_USERNAME = "python"
    POST_PASSWORD = "python"
    Session = sessionmaker(bind = engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        return "Object found"
    else:
        return "Object not found " + POST_USERNAME + " " + POST_PASSWORD
@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,
		host='0.0.0.0',
		port=4000)


