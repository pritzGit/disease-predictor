from flask import Blueprint, render_template
from flask.globals import request

from .all_models import get_liver_preds

liver = Blueprint("liver", __name__)

@liver.route("/")
def home():
    return render_template("liver.html")

@liver.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        Age = float(request.form['Age'])
        Gender = float(request.form['Gender'])
        Direct_Bilirubin = float(request.form['Direct_Bilirubin'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Alkaline_Phosphotase = float(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = float(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = float(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])
        
        values = [Age,Gender,Total_Bilirubin, Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]
        
        preds = get_liver_preds(values)
        if preds == 1:
            return render_template("result_neg.html", preds = "YES, you are suffering from liver disease.")
        elif preds == 0:
            return render_template("result.html", preds = "NO, you are safe as of now.")
        else:
            return render_template("error.html")
    else:
        return render_template("liver.html")