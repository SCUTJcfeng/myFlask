from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import flash, redirect, url_for


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

app = Flask(__name__)
app.config['SECRET_KEY'] = '3ef6ffg4'

@app.route('/home',methods=['get'])
@app.route('/',methods=['get'])
def home():
    user = {'nickname':'Jcfeng'} # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('home.html',
                           title = 'home',
                           user = user,
                           posts = posts)

@app.route('/login',methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # post && everything is all right it will return True
        flash('Login requested for user={}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run()
