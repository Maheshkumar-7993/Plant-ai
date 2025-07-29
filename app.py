from flask import Flask, request, render_template, send_from_directory, jsonify
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
from PIL import Image

# Load the pre-trained CNN model
cnn = tf.keras.models.load_model('cnn_model.h5')

# List of class names corresponding to the plant diseases
class_names = [
    'Apple__Apple_scab', 'Apple_Black_rot', 'Apple_Cedar_apple_rust', 'Apple__healthy',
    'Blueberry__healthy', 'Cherry(including_sour)Powdery_mildew', 'Cherry(including_sour)_healthy',
    'Corn_(maize)Cercospora_leaf_spot Gray_leaf_spot', 'Corn(maize)Common_rust', 'Corn_(maize)_Northern_Leaf_Blight',
    'Corn_(maize)healthy', 'Grape_Black_rot', 'Grape_Esca(Black_Measles)', 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)',
    'Grape__healthy', 'Orange_Haunglongbing(Citrus_greening)', 'Peach__Bacterial_spot', 'Peach__healthy',
    'Pepper,bell_Bacterial_spot', 'Pepper,_bell_healthy', 'Potato_Early_blight', 'Potato_Late_blight', 'Potato__healthy',
    'Raspberry__healthy', 'Soybean_healthy', 'Squash_Powdery_mildew', 'Strawberry_Leaf_scorch', 'Strawberry__healthy',
    'Tomato__Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato__Septoria_leaf_spot',
    'Tomato__Spider_mites Two-spotted_spider_mite', 'Tomato_Target_Spot', 'Tomato__Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato__Tomato_mosaic_virus', 'Tomato__healthy'
]

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure the uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to render the HTML page for uploading images
@app.route('/')
def index():
    return render_template('index.html')  # HTML form for uploading images

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route to process the image and display prediction
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    if file and allowed_file(file.filename):
        # Save the uploaded image
        filename = secure_filename(file.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)

        # Preprocess the image for the model
        image = tf.keras.preprocessing.image.load_img(img_path, target_size=(128, 128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to a batch

        # Predict the disease
        predictions = cnn.predict(input_arr)
        result_index = np.argmax(predictions)
        model_prediction = class_names[result_index]
        confidence_score = np.max(predictions) * 100  # Confidence in percentage

        # Render result in a new HTML page (or return JSON response)
        return render_template(
            'result.html',
            image_path=f'/uploads/{filename}',
            prediction=model_prediction,
            confidence=f"{confidence_score:.2f}%"
        )

    return "No image uploaded or invalid file format", 400

# Routes for additional pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
@app.route('/pestmart')
def pestmart():
    return render_template('pestmart.html')

@app.route('/resource')
def resource():
    return render_template('resource.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/diseases')
def diseases():
    return render_template('diseases.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5007)
