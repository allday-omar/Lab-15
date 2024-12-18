# Omar Gastelum
# Lab 15

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# GitHub Repository: https://github.com/<your-username>/Flask-Acronym-App

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def acro():
  return '''<p>Aaron: ikr</p>'''

@app.route('/Omar')
def temp():
    return render_template('template.html')

if __name__ == "__main__":
    app.run(debug=True)



