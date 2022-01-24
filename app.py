# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 21:24:38 2022

@author: n7568
"""

from flask import Flask, render_template, request

from PIL import Image 
import numpy as np 
from tensorflow.keras.models import load_model
import tensorflow as tf


app = Flask(__name__) 
model = load_model("C:/Users/n7568/Desktop/Project/models/mnistCNN.h5")


@app.route('/')
def upload_file():
   return render_template('main.html')
@app.route('/about')
def upload_file1():
   return render_template('main.html') 
@app.route('/upload') 
def upload_file2():
   return render_template('index6.html')


@app.route('/predict', methods = ['POST']) 
def upload_image_file():
   if request.method == 'POST': 
      img = Image.open(request.files['file'].stream).convert("L")
      img = img.resize((28,28))
      im2arr = np.array(img)
      im2arr = im2arr.reshape(1,28,28,1)
      pred = model.predict(im2arr)
      y_pred= np.argmax(pred)
      print(y_pred) 
      
      if(y_pred == 0) :
        return render_template("0.html",showcase =  str(y_pred))
      elif(y_pred == 1) :
        return render_template("1.html",showcase =  str(y_pred))
      elif(y_pred == 2) :
        return render_template("2.html",showcase =  str(y_pred))
      elif(y_pred == 3) :
        return render_template("3.html",showcase =  str(y_pred))
      elif(y_pred == 4) :
        return render_template("4.html",showcase =  str(y_pred))
      elif(y_pred == 5) :
        return render_template("5.html",showcase =  str(y_pred))
      elif(y_pred == 6) :
        return render_template("6.html",showcase =  str(y_pred))
      elif(y_pred == 7) :
        return render_template("7.html",showcase =  str(y_pred))
      elif(y_pred == 8) :
        return render_template("8.html",showcase =  str(y_pred))
      else :
        return render_template("9.html",showcase =  str(y_pred))
   else:
        return None
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug =False)
      
     