from flask import Blueprint, render_template
from flask.globals import request


kidney = Blueprint("kidney", __name__)

@kidney.route("/")
def home():
    return render_template("kidney.html")

@kidney.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = int(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = int(request.form['thal'])
        print(sex)
        values = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        
        preds = get_preds(values)
        if preds == 1:
            return render_template("heart.html", prediction_text = "YES")
        elif preds == 0:
            return render_template("heart.html", prediction_text = "NO")
        else:
            return render_template("heart.html", prediction_text = "Error!")
    else:
        return render_template("heart.html")