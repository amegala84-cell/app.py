from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Megala Portfolio</title>
        <style>
            body{
                font-family: Arial;
                text-align:center;
                background:#f4f4f4;
                padding:50px;
            }
            .card{
                background:white;
                padding:30px;
                border-radius:15px;
                max-width:700px;
                margin:auto;
                box-shadow:0 0 10px rgba(0,0,0,0.2);
            }
            a{
                text-decoration:none;
                color:white;
                background:#007bff;
                padding:10px 20px;
                border-radius:5px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>MEGALA A</h1>
            <h3>Mathematics Professor</h3>

            <p>
            Welcome to my professional portfolio website.
            </p>

            <h2>Skills</h2>
            <p>Mathematics | Teaching | Research | Python | Arduino</p>

            <h2>Education</h2>
            <p>M.Sc Mathematics</p>

            <h2>Projects</h2>
            <p>Arduino Fish Feeder, Python Applications, Academic Research</p>

            <br>
            <a href="/contact">Contact Me</a>
        </div>
    </body>
    </html>
    """

@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>
    <p>Email: amegala84@gmail.com</p>
    <p>contact : 8012285342</p>
    <a href="/">Back Home</a>
    """

if __name__ == "__main__":
    app.run()
