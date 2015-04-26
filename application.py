from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index_page():
	return render_template("index.html")

@app.route("/")

if __name__ == "__main__":
    app.run(debug=True)