# Arogo AI Tasks: Shipment Delay Prediction & Image Captioning

## Overview

This repository contains the solutions for two tasks assigned by Arogo AI, as part of the recruitement assignment of an AI/ML Engineer Internship. The tasks involved:

1.  **Shipment Delay Prediction:** Analyzing shipment data, building binary classification models to predict delays, and developing a Flask API for predictions.
2.  **Image Captioning Web Application:** Creating a web application that accepts user-uploaded images and generates descriptive captions using a pre-trained model.

## Features

### Shipment Delay Prediction

* **Data Analysis:** Performed Exploratory Data Analysis (EDA) on shipment data (`AI ML Internship Training Data.xlsx - freight_delivery_realistic_data.csv`). Handled missing 'Vehicle Type' values by imputing based on the most frequent vehicle for each origin-destination pair.
* **Feature Engineering:** Reduced dimensionality by dropping less predictive features like Shipment ID, Distance (km), and Shipment Date. Used Label Encoding for categorical features. Focused final models on 'Weather Conditions' and 'Traffic Conditions'.
* **Modeling:** Implemented and evaluated Artificial Neural Networks (ANN), Random Forest, and XGBoost models.
* **Performance:** Achieved approximately 91% test accuracy across the final models (ANN, Random Forest, XGBoost).
* **API:** Developed a Flask API (`delay-task/app.py`) that takes JSON input for weather and traffic conditions and returns predictions from all three models. Includes a test script (`delay-task/use-app.py`).

### Image Captioning Web Application

* **Functionality:** Allows users to upload an image and receive an AI-generated text caption describing the image content.
* **Model:** Utilizes the `blip-image-captioning-base` model from HuggingFace (approx. 900MB) locally for caption generation.
* **Technology Stack:**
    * **Backend:** Flask (`image_describe/app.py`) handles image uploads, processing via the BLIP model, and returning captions.
    * **Frontend:** HTML, CSS, and JavaScript (`image_describe/templates/`, `image_describe/static/`) provide a user-friendly interface for uploading images and viewing results.

### Shipment Delay Prediction API

1.  Ensure necessary libraries (Flask, Pandas, Tensorflow/Keras, Scikit-learn, XGBoost, joblib) are installed.
2.  Navigate to the `delay-task/` directory.
3.  Run the Flask API: `python app.py`
4.  Send POST requests to `http://127.0.0.1:5000/predict` (or the deployed URL) with JSON payloads containing "Weather Conditions" and "Traffic Conditions". Example using `use-app.py` or `curl`:
    ```json
    {
        "Weather Conditions": "Clear",
        "Traffic Conditions": "Moderate"
    }
    ```
5.  The API will return a JSON response with predictions ('Delayed' or 'On Time') from the Neural Network, RandomForest, and XGBoost models.

### Image Captioning Web Application

1.  Ensure necessary libraries (Flask, PyTorch, PIL, Transformers) are installed.
2.  Download the `blip-image-captioning-base` model files from HuggingFace or ensure they are accessible locally.
3.  Navigate to the `image_describe/` directory.
4.  Run the Flask application: `python app.py` 
5.  Open a web browser and go to `http://127.0.0.1:5000` (or the deployed URL).
6.  Upload an image using the interface and click "Generate Caption" to see the AI-generated description.
