import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


filepath = r'C:\Users\Sahil\Desktop\IT\SEM 7\Final yr project\Main Code\model.h5'
model = load_model(filepath)


print("Model Loaded Successfully")


maize_plant = cv2.imread(r'C:\Users\Sahil\Desktop\IT\SEM 7\Final yr project\Main Code\dataset\Blight\Corn_Blight (9).jpg')

test_image = cv2.resize(maize_plant, (224,224)) # load image 
  
test_image = img_to_array(test_image)# convert image to np array and normalize
test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
result = model.predict(test_image) # predict diseased plant or not
  
pred = np.argmax(result, axis=1)
# print(np.argmax(result))

# img=image.load_img(r'C:\Users\Sahil\Desktop\IT\SEM 7\Final yr project\Main Code\dataset\Blight\Corn_Blight (3).jpg',target_size=(224,224))
# x=image.img_to_array(img)
# x.shape
# x = x.reshape(1,224,224,3)
# pred = model.predict(x)

# preds = np.argmax(pred,axis=1)
# preds
print(pred)

if pred == 0:
   print ("The Leaf is diseased with Common Rust")
elif pred == 1:
   print ("The Leaf is healthy")
elif pred == 2:
   print ("The Leaf is Blight")
else:
   print ("The Leaf has the disease of Gray leaf spot")