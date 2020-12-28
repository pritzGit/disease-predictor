import numpy as np
import pickle

from sklearn import preprocessing
scaler=preprocessing.StandardScaler()

c_model_file = "models/bCancer_model.pkl"
d_model_file = "models/diabetes_model.pkl"
h_model_file = "models/heart_disease_model.pkl"
k_model_file = "models/kidney_model1.pkl"
li_model_file = "models/liver_model.pkl"
lu_model_file = "models/lung_model.pkl"


cancer_model = pickle.load(open(c_model_file, 'rb'))
diabetes_model = pickle.load(open(d_model_file, 'rb'))
heart_model = pickle.load(open(h_model_file, 'rb'))
kidney_model = pickle.load(open(k_model_file, 'rb'))
liver_model = pickle.load(open(li_model_file, 'rb'))
lung_model = pickle.load(open(lu_model_file, 'rb'))

def get_cancer_preds(values):
    
    preds = cancer_model.predict(np.array(values).reshape(1, -1)) 
    return preds[0]

def get_diabetes_preds(values):
    
    preds = diabetes_model.predict(np.array(values).reshape(1, -1)) 
    return preds[0]

def get_heart_preds(values):
    
    preds = heart_model.predict(np.array(values).reshape(1, -1)) 
    return preds[0]

def get_kidney_preds(values):
    
    a = scaler.fit_transform(np.array(values).reshape(1, -1))
    preds = kidney_model.predict(a)
    return preds[0]

def get_liver_preds(values):
    
    a = scaler.fit_transform(np.array(values).reshape(1, -1))
    preds = liver_model.predict(a)
    return preds[0]

def get_lung_preds(values):
    
    a = scaler.fit_transform(np.array(values).reshape(1, -1))
    preds = lung_model.predict(a)
    return preds[0]