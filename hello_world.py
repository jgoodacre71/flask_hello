from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html',
                           my_string=name)

@app.route("/jedi/<first_name>/<last_name>")
def jedi(first_name,last_name):
    name = last_name[:2]+first_name[:3]
    return render_template('jedi.html',
                           my_string=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
