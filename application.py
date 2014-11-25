from sunlight import congress
from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', 'False') == 'True'


@app.route("/")
def index():
    input_age = request.args.get('birthday', '')
    legislators = congress.legislators(birthday__gte=input_age) if input_age else []
    return render_template('base.html', legislators=legislators, birthday=input_age)

if __name__ == "__main__":
    app.run(debug=True)
