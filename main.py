from flask import Flask, render_template


app = Flask(__name__)

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