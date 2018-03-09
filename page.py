from flask import Flask
from flask import render_template

app = Flask(__name__)

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

@app.route('/login',methods=['get'])
def login():
    return 'login'


if __name__ == '__main__':
    app.run()
