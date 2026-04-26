import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("notebooks\models\plant_model_v1.h5")

folder = "real_world_test_PlantDoc"

for img_name in os.listdir(folder):
    img_path = os.path.join(folder, img_name)
    
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    pred = model.predict(img_array, verbose=0)
    predicted_class = np.argmax(pred)
    confidence = np.max(pred) * 100
    
    print(f"{img_name} → klasa {predicted_class} ({confidence:.2f}%)")