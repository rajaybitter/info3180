"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:   http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, jsonify, session
from forms import *
from models import *
from image_scrapper import scrape

db.create_all()

###
# Routing for your application.
###

@app.route('/api/users/home')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

#######################    FUNCTIONALITIES    ###########################
@app.route('/api/users/register',  methods =['GET', 'POST'])
def register(): 
    if request.method == 'POST':
        data = request.get_json()
        if not User.query.filter_by(email=data['email']).first():
            user = User(name=data['name'], email=data['email'], password=data['password'], 
                        age=data['age'], gender=data['gender'])
            db.session.add(user)
            db.session.commit()
            return jsonify(data = user.serialize())
        else:
            return jsonify(error="User already exists")
    else:
        return render_template('register.html')


@app.route('/api/users/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = User(email= data['email'], password = data['password'])
        if user.validate():
            session['email'] = user.email
            return jsonify(status = "Success")
        return jsonify(error = "User not found")
    else:
        return render_template('login.html')

@app.route('/api/users/new_item', methods=['GET'])
def addItem():
    if session.has_key('email'):
        return render_template('new_item.html')
    return render_template('login.html')

@app.route('/api/users/<int:userid>/wishlist', methods=['GET','POST'])
def wishlist(userid):
    if session.has_key('email'):
        #Add to list    
        if request.method == 'POST':
            data = request.get_json()
            item = Item(title  = data['name'], url = data['url'] , description = data['description'], 
                owner = data['owner'], thumbnail_url = data['thumbnail_url'])
            db.session.add(item)
            db.session.commit()
        elif request.method == 'GET':
            #return users wish list
            items = Item.query.filter(Item.owner == userid).all()
            temp = {}
            temp['items'] = [item.serialize() for item in items]
            print temp
            return jsonify(errors= 'null', data = temp, message = 'success')
    return render_template('login.html')

@app.route('/api/thumbnails', methods = ['GET'])
def thumbnails():
    try:
        url = request.args['url']
        ls = scrape(url)
        data = {'thumbnails': ls}
        return jsonify(error = "null", data = data, message="success")
    except:
        return jsonify(error = "true", data = {}, message="failed")

@app.route('/api/users/<int:userid>/wishlist/<int:itemid>', methods=['DELETE','GET'])
def delete(userid, itemid):
    if session.has_key('email'):    
        try:
            item = Item.query.filter(Item.id == itemid).first()
            if item.owner == userid:
                db.session.delete(item)
                db.session.commit()
                return jsonify(error = "null", data = {}, message = "success")
        except:
            return jsonify(error = "true", data = {}, message = "failed")
    return render_template('login.html')
                
    
@app.route('/api/user', methods = ['GET'])
def getUserInfo():
    user = User.query.filter(User.email == session['email']).first()
    if user == None:
        return jsonify(error = "true")
    else:
        return jsonify(user = user.serialize())
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