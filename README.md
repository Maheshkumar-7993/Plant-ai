# o🌿 Plant Disease Detection Website

This project is a web-based application for detecting plant diseases using AI vision. Users can upload images of plant leaves, and the system will predict the disease and display possible solutions. The project leverages machine learning, Flask, and a user-friendly frontend for seamless interaction.

---

## 🚀 Features

- Upload images of plant leaves for disease detection.
- AI-based model (`cnn_model.h5`) for accurate predictions.
- Responsive web design with an intuitive interface.
- Additional resources such as pest control, disease descriptions, and more.

---

## 🗂️ Project Structure

```
.
├── .dist/           # Build/Distribution files
├── .vscode/         # VSCode workspace settings
├── static/          # Static files (CSS, JS, images)
│   ├── css/         # Stylesheets
│   ├── js/          # JavaScript files
│   ├── images/      # Images used in the project
├── templates/       # HTML templates for web pages
│   ├── about.html   # About page
│   ├── chatbot.html # Chatbot page
│   ├── contact.html # Contact page
│   ├── diseases.html # Plant diseases info
│   ├── index.html   # Homepage
│   ├── pestmart.html # Pest control resources
│   ├── resource.html # Additional resources
│   ├── result.html  # Display results of predictions
│   ├── upload.html  # Upload image form
├── uploads/         # Uploaded files
├── app.py           # Flask application
├── cnn_model.h5     # Pre-trained AI model
```

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/
   cd plant-disease-detection
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:

   ```bash
   python app.py
   ```

5. Open your browser and visit:

   ```
   http://127.0.0.1:5000
   ```

---

## 📚 How to Use

1. Navigate to the **Upload** page to upload an image of a plant leaf.
2. View the prediction result 
3. Explore the additional pages for pest control tips, disease details, and chatbot support.

---

## 🧠 Model Details

- **File**: `cnn_model.h5`
- **Model Architecture**: CNN
- **Framework**: TensorFlow/Keras
- **Accuracy**: 94% on test data

---

## 🌟 Features & Enhancements

- **Responsive Design**: CSS and JS for a smooth, user-friendly experience.
- **Multiple Pages**: Detailed information on diseases, pest control, and contact support.
- **Chatbot Integration**: Assist users with common queries

---



## 🌟 Acknowledgments

- Infosys Springboard for project guidance.
- Open-source tools and libraries used in the project.



