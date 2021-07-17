from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


"""
@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/work.html')
def work():
    return render_template('./works.html')


@app.route('/works.html')
def works():
    return render_template('./works.html')


@app.route('/contact.html')
def contact():
    return render_template('./contact.html')


@app.route('/components.html')
def components():
    return render_template('./components.html')
"""




"""
@app.route('/blog/<int:post_id>')
def blog_post(post_id=None):
    return render_template('./blog_post.html', post_id=post_id)


@app.route('/blog/<topic>/<subtopic>')
def blog2(topic=None, subtopic=None):
    return render_template('./blog_post_topic.html', topic=topic, subtopic=subtopic)
"""
