from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os

def upload_image(app):
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
            print(save_path)
            file.save(save_path)
            # You can save the file path to a database or perform other actions here
            return redirect(url_for('uploaded_file', filename=filename))

    return render_template("upload.html")


from flask import send_from_directory


def show_uploaded_file(app, filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)