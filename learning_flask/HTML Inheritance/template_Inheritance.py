# Importing
from flask import Flask
from flask import render_template

#Interaction
app = Flask(__name__)

# Mapping
@app.route("/")

#Inputs
def home():
    return render_template("index.html")




# MAIN
if __name__ == "__main__":
    app.run(debug=True)