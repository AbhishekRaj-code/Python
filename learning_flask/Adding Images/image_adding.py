# Importing

from flask import Flask
from flask import render_template
import os

#Interaction
app = Flask(__name__)

picfolder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = picfolder

# Mapping
@app.route("/")

#Inputs
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'waterfall.jpg')
    return render_template("home1.html", user_image=pic)

# Mapping
@app.route("/second")

#Inputs
def second():
    return "This is the second page."

#Mapping
@app.route("/third")

#Inputs
def third():
    return render_template("third.html")


# MAIN
if __name__ == "__main__":
    app.run(debug=True)