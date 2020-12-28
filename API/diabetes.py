from flask import Blueprint, render_template
from flask.globals import request

from .all_models import get_diabetes_preds

diabetes = Blueprint("diabetes", __name__)

@diabetes.route("/")
def home():
    return render_template("diabetes.html")

@diabetes.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])
        
        values = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin ,BMI ,DiabetesPedigreeFunction ,Age]
        
        preds = get_diabetes_preds(values)
        if preds == 1:
            return render_template("diabetes.html", prediction_text = "YES")
        elif preds == 0:
            return render_template("diabetes.html", prediction_text = "NO")
        else:
            return render_template("error.html")
    else:
        return render_template("diabetes.html")