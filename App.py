from flask import Flask, render_template, request, url_for
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__, template_folder="templates", static_folder="static")

# Load trained model
model = tf.keras.models.load_model('best_model.keras')

# Tumor classes
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file:
        img = preprocess_image(file)
        prediction = model.predict(np.expand_dims(img, axis=0))
        predicted_class = class_names[np.argmax(prediction)]
        return render_template('result.html', prediction=predicted_class)
    return render_template('index.html', error="No file uploaded.")

def preprocess_image(file):
    img = Image.open(file.stream).convert("RGB")
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    return img_array

if __name__ == '__main__':
    app.run(debug=True)
