# Leaf Disease Detection

This project is a **Deep Learning application** built with **TensorFlow/Keras** and **Flask**. It accurately identifies various plant diseases from leaf images using a Convolutional Neural Network (CNN).

## 🚀 Features
- **High Accuracy:** Trained on the PlantVillage dataset with 15 different classes.
- **Fast Inference:** Optimized architecture (MobileNetV2) for quick results.
- **Web Interface:** Easy-to-use drag-and-drop upload system.

## 📊 Model Performance (Latest Training)
- **Training Accuracy:** ~90%
- **Validation Accuracy:** ~92%
- **Loss:** < 0.3

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **AI/ML:** TensorFlow, Keras, NumPy
- **Frontend:** HTML5, CSS3 (Custom Design), JavaScript

## 📁 Project Structure
- `app.py`: Main Flask server.
- `models/`: Contains the trained `.h5` model and class indices.
- `src/`: Source files for the web interface (templates, CSS).
- `static/`: Storage for user uploads.
- `notebooks/`: Jupyter Notebook used for training the model.

## ⚙️ How to run
1. Clone the repository:
   `git clone <your-repository-link>`
2. Install dependencies:
   `pip install flask tensorflow numpy`
3. Run the application:
   `python app.py`
4. Open your browser at: `http://127.0.0.1:5000`
