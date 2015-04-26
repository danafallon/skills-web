from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
	return render_template("index.html")

@app.route("/application-form")
def application_page():
	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def acknowledge_application():
	job_titles = {"swe": "Software Engineer", "qae": "QA Engineer", "pm": "Product Manager"}
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	name = firstname + " " + lastname
	job = request.form.get("job")
	job_title = job_titles[job]
	salary = request.form.get("salary")
	return render_template("acknowledge.html", name=name, job=job_title, salary=salary)

if __name__ == "__main__":
    app.run(debug=True)