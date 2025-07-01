from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

my_name = "Krishna"
my_bio = "I'm an aspiring Python developer working on cool internship tasks."

# Temporary list to store messages
messages = []

@app.route("/")
def index():
    return render_template("index.html", name=my_name, bio=my_bio, messages=messages)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    messages.append({"name": name, "email": email, "message": message})

    return redirect(url_for('index'))  # Redirect back to home page
