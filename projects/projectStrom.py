from flask import Blueprint, render_template, session, redirect, url_for
import config_main
def create_prj_strom_blueprint(app):
    #blueprint = Flask(__name__)
    blueprint = Blueprint('auth', __name__)

    @blueprint.route("/strom")
    def prjStrom():
        print("strom")
        if 'logged_in' in session:
            return render_template("projects/prj_Strom/overview.html", content="Project Strom!", title=config_main.website_title)
        else:
            return redirect(url_for('login'))

    return blueprint