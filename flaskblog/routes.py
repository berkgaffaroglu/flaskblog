from flask import render_template,redirect, url_for,request
from flaskblog import app,db
from flaskblog.models import Post
from flaskblog.forms import CreatePostForm,DeleteForm,EditForm

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/posts')
@app.route('/posts/')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@app.route('/admin/', methods=['GET','POST'])
def admin():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post(title=request.form['title'], content=request.form['content'])
        db.session.add(post)
        db.session.commit()
        return redirect(f'/post/{post.id}')
        
    
    return render_template('admin.html', form=form)

@app.route('/post/<postid>', methods=['GET','POST'])
def post(postid):
    
    post = Post.query.get_or_404(postid)
    if post:
        return render_template('post.html', post=post)
    else:
        return f"404 not found"
@app.route('/post/delete/<postid>', methods=['GET','POST'])
def delete(postid):
    post = Post.query.get_or_404(postid)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')
@app.route('/post/edit/<postid>', methods=['GET','POST'])
def edit(postid):
    post = Post.query.get_or_404(postid)
    form = EditForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.content = form.content.data
        db.session.commit()
        return redirect(f'/post/{post.id}')
    return render_template('edit.html', form=form, post=post)
    
    
    




