from flask import Blueprint, render_template
from flask.globals import request

from .all_models import get_lung_preds

lung = Blueprint("lung", __name__)

@lung.route("/")
def home():
    return render_template("lung.html")

@lung.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        Air_Pollution = int(request.form['Air_Pollution'])
        Alcohol_use = int(request.form['Alcohol_use'])
        Dust_Allergy = int(request.form['Dust_Allergy'])
        OccuPational_Hazards = int(request.form['OccuPational_Hazards'])
        Genetic_Risk = int(request.form['Genetic_Risk'])
        chronic_Lung_Disease = float(request.form['chronic_Lung_Disease'])
        Balanced_Diet = float(request.form['Balanced_Diet'])
        Obesity = int(request.form['Obesity'])
        Smoking = int(request.form['Smoking'])
        Passive_Smoker = int(request.form['Passive_Smoker'])
        Chest_Pain = float(request.form['Chest_Pain'])
        Coughing_of_Blood = float(request.form['Coughing_of_Blood'])
        Fatigue = int(request.form['Fatigue'])
        
        values = [Air_Pollution, Alcohol_use,Dust_Allergy,OccuPational_Hazards,Genetic_Risk,chronic_Lung_Disease,Balanced_Diet,
                  Obesity,Smoking,Passive_Smoker,Chest_Pain,Coughing_of_Blood,Fatigue]
        
        preds = get_lung_preds(values)
        if preds == 'Low':
            return render_template("lung.html", prediction_text = "YES")
        elif preds == 'Medium':
            return render_template("lung.html", prediction_text = "NO")
        elif preds == 'High':
            return render_template("lung.html", prediction_text = "NO")
        else:
            return render_template("error.html")
    else:
        return render_template("lung.html")