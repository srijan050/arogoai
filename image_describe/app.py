import os
import io
from PIL import Image
from flask import Flask, request, jsonify, render_template

import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)


def generate_caption(image_bytes):
    """
    Generate a descriptive caption for the given image bytes using the BLIP model.
    """
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.generate(**inputs, max_length=50, num_beams=5, early_stopping=True)
    caption = processor.tokenizer.decode(out[0], skip_special_tokens=True)
    return caption


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/describe", methods=["POST"])
def describe_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    image_bytes = file.read()

    try:
        _ = Image.open(io.BytesIO(image_bytes))
    except Exception:
        return jsonify({"error": "Invalid image file."}), 400

    try:
        caption = generate_caption(image_bytes)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error generating description."}), 500

    return jsonify({"description": caption}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
