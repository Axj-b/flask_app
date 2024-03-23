from flask import Flask, render_template, request, redirect, url_for, session
import config_main
from auth import login_route , logout_route
from upload import upload_image, show_uploaded_file

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure, random key
app.config['UPLOAD_FOLDER'] = 'uploads' 


@app.route("/")
def home():
    if 'logged_in' in session:
        return render_template("index.html", content="Welcome to my homepage!", title=config_main.website_title)
    else:
        return redirect(url_for('login'))

@app.route("/about")
def about():
    if 'logged_in' in session:
        return render_template("about.html", content="This is some information about me.", title=config_main.website_title)
    else:
        return redirect(url_for('login'))

@app.route("/projects")
def projects():
    if 'logged_in' in session:
        return render_template("projects.html", content="These are my projects!", title=config_main.website_title)
    else:
        return redirect(url_for('login'))
    
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    return upload_image(app)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return show_uploaded_file(app, filename)
#auth routes
@app.route("/login", methods=['GET', 'POST'])
def login():
    return login_route()


@app.route("/logout")
def logout():
    return logout_route()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
