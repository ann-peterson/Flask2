from flask import Flask, request, render_template
from random import choice, randint


COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/lucky')
def lucky_number():
    lucky_num = randint(1, 10)

    return render_template("lucky.html", num=lucky_num)


@app.route('/form')
def show_form():
    return render_template("form.html")
    # add your code here



@app.route('/greet')
def offer_greeting():
    person=request.args.get("person")
    nice_thing = choice(COMPLIMENTS)
    return render_template("compliment.html", name=person, compliment=nice_thing)


if __name__ == "__main__":
    app.run(debug=True)
