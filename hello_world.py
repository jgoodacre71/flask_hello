from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<first_name>/<last_name>")
def jedi(first_name,last_name):
    html = """
        <h1>
            Jedi Name !
        </h1>
        <p>
            Your jedi name is {}
        </p>
        
    """
    name = last_name[:2]+first_name[:3]
    return html.format(name.title())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
