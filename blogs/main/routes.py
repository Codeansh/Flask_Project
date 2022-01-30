
from flask import render_template, request, Blueprint
from blogs.models import Post

main=Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page=request.args.get('page',1, type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html', posts=posts, title="HOMEPAGE")

@main.route("/about")
def about():
    m = "hello from script"
    return render_template('about.html', msg=m, title="working")


@main.route("/about/ath")
def good():
    return "<h1>yes i have learning more about the flask🥳🥳🥳</h1>safal is a very good "