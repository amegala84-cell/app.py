from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Arduino Projects Store</title>

<style>
body{
    font-family:Arial,sans-serif;
    background:#f2f2f2;
    margin:0;
    padding:15px;
}

.header{
    text-align:center;
    color:#0066cc;
}

.card{
    background:white;
    max-width:500px;
    margin:auto;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.2);
}

.price{
    color:green;
    font-size:32px;
    font-weight:bold;
}

.stock{
    color:white;
    background:green;
    display:inline-block;
    padding:8px 15px;
    border-radius:20px;
    margin-top:10px;
}

.btn{
    display:block;
    text-align:center;
    padding:15px;
    margin-top:15px;
    text-decoration:none;
    color:white;
    border-radius:10px;
    font-size:18px;
}

.video{
    background:#ff0000;
}

.buy{
    background:#25D366;
}

.warranty{
    margin-top:20px;
    background:#eef5ff;
    padding:15px;
    border-radius:10px;
    text-align:center;
}
</style>
</head>

<body>

<h1 class="header">Arduino Projects Store</h1>

<div class="card">

<h2>🐟 Automatic Fish Feeder</h2>

<p>
Automatic Fish Feeder using Arduino UNO and Servo Motor.
Feeds fish automatically at scheduled timings.
</p>

<div class="price">₹599</div>

<div class="stock">
🔥 Only 1 Left In Stock
</div>

<br><br>

<a class="btn video"
href="https://www.youtube.com/shorts/nkrd7me6-q0?feature=share"
target="_blank">
▶ Watch Demo Video
</a>

<a class="btn buy"
href="https://wa.me/918012285342"
target="_blank">
🛒 Buy on WhatsApp
</a>

<div class="quality">
✅ Arduino Code Included<br>
✅ Project Support Available
</div>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
