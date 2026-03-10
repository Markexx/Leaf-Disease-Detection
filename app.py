from flask import Flask, render_template, request, send_from_directory
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

# Definiramo putanje
template_dir = os.path.join(base_dir, 'src', 'templates')
static_dir = os.path.join(base_dir, 'static')
css_dir = os.path.join(base_dir, 'src', 'css')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Ruta za dohvaćanje CSS-a iz src/css foldera
@app.route('/css/<path:filename>')
def custom_css(filename):
    return send_from_directory(css_dir, filename)

MODEL_PATH = 'models/plant_model_v1.h5'
JSON_PATH = 'models/class_indices.json'

model = tf.keras.models.load_model(MODEL_PATH)
with open(JSON_PATH, 'r') as f:
    class_names = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    img_name = None
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            if not os.path.exists(static_dir): 
                os.makedirs(static_dir)
            
            # Spremi sliku u /static/
            img_path = os.path.join(static_dir, file.filename)
            file.save(img_path)
            img_name = file.filename
            
            # Obrada za AI
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            preds = model.predict(img_array)
            raw_result = class_names[np.argmax(preds)]
            result = raw_result.replace('___', ' - ').replace('_', ' ')
            
    return render_template('index.html', result=result, image=img_name)

if __name__ == '__main__':
    app.run(debug=True)