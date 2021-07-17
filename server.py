from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'did not sabe to database'
    else:
        return 'something went wrong'


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
