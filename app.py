# FLask API is a tool which helps to connect webs servers to your project

from flask import Flask, render_template,url_for,request,jsonify
import joblib
import os
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/result',methods=['POST','GET'])
def result():
    cylinders=int(request.form["cylinders"])
    displacement=int(request.form["displacement"])
    horsepower=int(request.form["horsepower"])
    weight=int(request.form["weight"])
    acceleration=int(request.form["acceleration"])
    model_year=int(request.form["model_year"])
    origin=int(request.form["origin"])

    values=[[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]]

    models=os.path.join(os.path.dirname('E:\kushi\My projects\Fuel Efficiency prediction\models/'),'scaler.pkl')

   
    sc=None
    with open(models,'rb') as f:
     sc=pickle.load(f)
    
    values=sc.transform(values)

    model=load_model(r"E:\kushi\My projects\Fuel Efficiency prediction\models\model.h5")

    prediction=model.predict(values)
    prediction=float(prediction)
    if  prediction<0:
            return render_template('home.html',prediction_texts="Sorry you car has least fuel efficiency")
    else:
            return render_template('home.html',prediction_text="You car fuel effiecncy is {}".format( prediction))


if __name__=="__main__":
    app.run(debug=True)