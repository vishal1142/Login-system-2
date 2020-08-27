from flask import Flask

app = Flask(__name__)


@app.route('/')
def index() :
	return "hello"


if__name__== '__main__'
	app.run(debug=True)