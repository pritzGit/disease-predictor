from flask import Blueprint, render_template
from flask.globals import request

from .all_models import get_kidney_preds

kidney = Blueprint("kidney", __name__)

@kidney.route("/")
def home():
    return render_template("kidney.html")

@kidney.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        age = float(request.form['age'])
        bp = float(request.form['bp'])
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        su = float(request.form['su'])
        rbc = float(request.form['rbc'])
        pc = float(request.form['pc'])
        pcc = float(request.form['pcc'])
        ba = float(request.form['ba'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])
        sod = float(request.form['sod'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        pcv = float(request.form['pcv'])
        wc = float(request.form['wc'])
        rc = float(request.form['rc'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        cad = float(request.form['cad'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        ane = float(request.form['ane'])
        
        values = [age, bp,sg,al,su,rbc, pc, pcc, ba, bgr,bu, sc, sod,pot,hemo,pcv,wc, rc, htn, dm, cad, appet, pe, ane]
        
        preds = get_kidney_preds(values)
        if preds == 1:
            return render_template("result_neg.html", preds = "YES, you are suffering from Chronic Kidney Disease.")
        elif preds == 0:
            return render_template("result.html", preds = "NO, you are not suffering from Chronic Kidney Disease.")
        else:
            return render_template("error.html")
    else:
        return render_template("kidney.html")