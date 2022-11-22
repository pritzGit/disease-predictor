from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from API.bcancer import bcancer
from API.diabetes import diabetes
from API.heart import heart
from API.kidney import kidney
from API.liver import liver
from API.lung import lung

app = Flask(__name__)
app.register_blueprint(bcancer, url_prefix="/bcancer")
app.register_blueprint(diabetes, url_prefix="/diabetes")
app.register_blueprint(heart, url_prefix="/heart")
app.register_blueprint(kidney, url_prefix="/kidney")
app.register_blueprint(liver, url_prefix="/liver")
app.register_blueprint(lung, url_prefix="/lung")

@app.route('/', methods=['GET'])
def index():
    # HOMEPAGE
    return render_template('index.html')

@app.route('/privacyterms', methods=['GET'])
def privacy():
    return render_template('privacy_policy.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(500)
def not_found(e):
    return render_template('error.html'), 500
