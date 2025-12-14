# Importing
from flask import Flask
from flask import render_template

#Interaction
app = Flask(__name__)

# Mapping
@app.route("/")

#Inputs
def first():
    return render_template("home.html")

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