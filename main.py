from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise Exception("Could not open video device")

def generate_frames():
    while True:
        success, frame = camera.read()  # Capture frame-by-frame
        if not success:
            break
        else:
            # Convert frame to JPEG format
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Display frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
@app.route('/video_feed')
def video_feed():
    #sets to a continuously updating dynamic stream with a frame boundary string
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

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