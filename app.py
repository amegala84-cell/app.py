from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
    <style>
    .card{
        width:300px;
        border:1px solid #ddd;
        padding:20px;
        margin:20px auto;
        text-align:center;
        border-radius:10px;
    }
    img{
        width:250px;
        border-radius:10px;
    }
    a{
        text-decoration:none;
        padding:10px 15px;
        background:blue;
        color:white;
        border-radius:5px;
        margin:5px;
    }
    </style>
    </head>
    <body>

    <h1 align='center'>Arduino Projects Store</h1>

    <div class='card'>
        <img src='https://via.placeholder.com/250'>
        <h2>Automatic Fish Feeder</h2>
        <h3>₹999</h3>

        <a href='https://youtube.com' target='_blank'>
        Watch Video
        </a>

        <a href='https://wa.me/918012285342' target='_blank'>
        Buy Now
        </a>
    </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
