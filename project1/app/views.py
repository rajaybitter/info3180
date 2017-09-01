"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from profileForm import profileForm
from flask import render_template, request, redirect, url_for, jsonify
from ddatetime import ddatetime


###
# Routing for your application.
###



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
	form = profileForm()

	if request.method == 'POST':
		if form.validat(): 
			current_date = datetime.now().strftime("%a %d %b ")
			 user = User(form.firstname.data, form.lastname.data,
                        form.age.data, form.sex.data, form.image.data, current_date, form.username.data, form.biography.data)
            db.session.add(user)
            db.session.commit()
			return render_template('profileForm.html', form=form)
	else:
		return render_template('profileForm.html', form=form)


@app.route('/profiles', methods = ['GET', 'POST'])
def profiles():
	users = User.query.all()

    if request.headers.get('Content-Type') == 'application/json':
        user_dic = []
        for x in users:
            user_dic.append(
                {'id': x.id, 'username': x.username})
        return jsonify(users=user_dic)
    else:
        return render_template('profile.html', users=users)

@app.route('/profile/<int:userid>', methods = ['GET', 'POST'])
def userProfile(userid):
	users = User.query.filter_by(id=userid)
    if request.headers.get('Content-Type') == 'application/json':
        user_dic = []
        for x in users:
	    	if x.id == userid:        
	            user_dic.append(
	                {'id': x.id, 'age': x.age, 'sex': x.sex, 'image': x.image, 'username': x.username, 'biography': x.biography})
	            return jsonify(users=user_dic)
    else:
        return render_template('profile.html', users=users)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")