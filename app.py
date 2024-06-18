#Import necessary libraries
from flask import Flask, redirect, render_template, request, url_for

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = r'C:\Users\Sahil\Desktop\IT\SEM 7\Final yr project\Main Code\model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_maize_disease(maize_plant):
  test_image = load_img(maize_plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image) # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased plant or not
  print('@@ Raw result = ', result)
  
  preds = np.argmax(result, axis=1)
  print(preds)
  if preds == 0:
    return "The Leaf is Diseased with Common Rust", 'Common_rust.html'
  elif preds == 1:
    return "The Leaf is Healthy", 'Healthy.html'
  elif preds == 2:
    return "The Leaf is Blight",'Blight.html'
  else:
    return "The Leaf has the Disease of Gray Leaf Spot",'Gray_leaf_spot.html'

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fetch input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        file_path = os.path.join(r'static\upload', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        preds, output_page = pred_maize_disease(maize_plant=file_path)
              
        return render_template(output_page, pred_output = preds, user_image = file_path)
    
@app.route('/About', methods=['GET', 'POST'])
def About():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
      return redirect(url_for('About'))
        # show the form, it wasn't submitted
    return render_template('About.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # do stuff when the form is submitted
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
      return redirect(url_for('index'))
        # show the form, it wasn't submitted
    return render_template('index.html')
  
 
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
