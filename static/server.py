from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
		return "Hello World!"

@app.route("/home")
def home():
		return render_template("index.html")

@app.route("/process", methods=['GET', 'POST'])
def process():
	name = request.form['student_name']

	message = "Hello " + name

	return message

if __name__ == "__main__":
	app.run()
