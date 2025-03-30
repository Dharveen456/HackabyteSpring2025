from flask import Flask, render_template, Response, request, jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json['image']
    
    # Decode base64 image
    encoded_data = data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Save or process the image
    cv2.imwrite("user_webcam.jpg", img)

    return jsonify({"message": "Image received and saved."})
            

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lunchboxes")
def lunchboxes():
    return render_template("lunchbox.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    # Add Form Submission Logic Here
    return render_template("contact.html", message="Thank you for your message!")

if __name__ == "__main__":
    app.run(debug=True)