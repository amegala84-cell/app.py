from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Sakshain</h1>
    <p>My first cloud website!</p>
    <a href='/about'>About</a><br>
    <a href='/contact'>Contact</a>
    """

@app.route("/about")
def about():
    return """
    <h1>About Us</h1>
    <p>This website is hosted on Render using Python Flask.</p>
    <a href='/'>Home</a>
    """

@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>
    <p>Email: example@email.com</p>
    <a href='/'>Home</a>
    """

if __name__ == "__main__":
    app.run()
