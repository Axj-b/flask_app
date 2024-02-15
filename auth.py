from flask import render_template, request, redirect, url_for, session
import config_main
def login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check your username and password (you might want to connect to a database here)
        with open("login_try.txt", '+a') as f:
            f.writelines(f"\nusername: {username}, password: {username}")
        # For demonstration purposes, let's use a simple check
        if username == 'afödafjq23pqriqnfa' and password == 'afdawe9üqwejfwioepföas':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template("login.html", error="Invalid username or password")
    
    #session['logged_in'] = False
    #return redirect(url_for('home'))
    
    return render_template("login.html",title=config_main.website_title)



def logout_route():
    session.pop('logged_in', None)
    return redirect(url_for('home'))