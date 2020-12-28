from flask import Blueprint, render_template
from flask.globals import request

from .all_models import get_cancer_preds

bcancer = Blueprint("bcancer", __name__)

@bcancer.route("/")
def home():
    return render_template("bcancer.html")

@bcancer.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        concave_points_mean = float(request.form['concave_points_mean'])
        area_mean = float(request.form['area_mean'])
        radius_mean = float(request.form['radius_mean'])
        perimeter_mean = float(request.form['perimeter_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        
        values = [concave_points_mean, area_mean, radius_mean, perimeter_mean, concavity_mean]
        
        preds = get_cancer_preds(values)
        if preds == 1:
            return render_template("bcancer.html", prediction_text = "Malignant")
        elif preds == 0:
            return render_template("bcancer.html", prediction_text = "Benigh")
        else:
            return render_template("bcancer.html", prediction_text = "Error!")
    else:
        return render_template("bcancer.html")