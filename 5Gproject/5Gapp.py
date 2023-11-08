# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:38:00 2023

@author: hp
"""

from flask import Flask, render_template,request
app = Flask(__name__)
import pickle
import joblib
model=pickle.load(open('resalloc.pkl','rb'))
ct=joblib.load('column')
@app.route('/')
def hello_world():
    return render_template("5Gindex.html")
@app.route('/task',methods =["POST"])
def task():
    at = request.form["at"]
    ss = request.form["ss"]
    l = request.form["l"]
    r = request.form["r"]
    ab = request.form["ab"]
    data=[at,ss,l,r,ab]
    prediction=model.predict([ct.fit_transform(data)])
    
    val=prediction[0]
    percentage=val*100
    
    return render_template("5Gindex.html", y=percentage)
    
app.run(debug = True)