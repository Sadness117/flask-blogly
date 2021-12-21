"""Blogly application."""

from threading import current_thread
from flask import Flask, redirect, request
from flask.templating import render_template
from models import db, connect_db
from models import User, Post
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'blab'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
db.drop_all()
db.create_all()
test_user = User(first_name='logan', last_name = 'needham', img_url='url_placeholder')
db.session.add(test_user)
db.session.commit()
test_post = Post(title = "test", content = 'test content', post_user = test_user.id)
test_post2 = Post(title = "test2", content = 'test2 content', post_user = test_user.id)
print(test_post.post_user)
db.session.add(test_post)
db.session.add(test_post2)
db.session.commit()


@app.route('/')
def home():
    '''Home page and diplays all users in the database'''
    person = User.query.all()
    return render_template('home.html', person = person)

@app.route('/add_user_page')
def add_page():
    '''brings user to the page to create a new user'''
    return render_template('add_user.html')

@app.route('/add_user', methods = ['POST'])
def add_user():
    '''adds user to database'''
    first = request.form['first']
    last = request.form['last']
    img = request.form['img_url']
    new_user = User(first_name = first, last_name = last, img_url = img)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/post_post', methods = ['POST'])
def post_the_post():
    return redirect('/')

@app.route('/<int:user_id>')
def user_information(user_id):
    '''gets information about selected user'''
    current_user = User.query.get(user_id)
    # current_posts = Post.query.filter(Post.post_user == user_id)
    current_posts = Post.query.all()
    print('sssssssssssssssssssssssssssssssssssssssssssssssss')
    print(current_posts)
    return render_template('info.html', current_user = current_user, current_posts = current_posts)

@app.route('/edit/<int:user_id>')
def edit(user_id):
    '''goes to edit page to edit a user'''
    current_user = User.query.get(user_id)
    return render_template('edit_user.html', current_user = current_user)

@app.route('/add_post/<int:user_id>')
def add_post(user_id):
    '''goes to edit page to edit a user'''
    current_user = User.query.get(user_id)
    return render_template('add_post.html', current_user = current_user)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    '''deletes user'''
    User.query.filter_by(id = user_id).delete()
    db.session.commit()
    return redirect('/')

@app.route('/commit_changes/<int:user_id>',methods = ['POST'])
def commit_change(user_id):
    '''changes the info on a seleced user'''
    first = request.form['first']
    last = request.form['last']
    img = request.form['img_url']
    current_user = User.query.get(user_id)
    current_user.first_name = first
    current_user.last_name = last
    current_user.img_url = img
    db.session.add(current_user)
    db.session.commit()
    return redirect(f'/{current_user.id}')

@app.route('/info/<int:post_id>')
def post_info(post_id):
    current_post = User.query.get(post_id)
    return render_template('current_post.html', current_post = current_post)

