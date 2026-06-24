```python
from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

HTML = """

<!DOCTYPE html>

<html>

<head>

<title>CyberShield</title>

<style>

body{
font-family:Arial;
background:#0d1117;
color:white;
margin:0;
padding:0;
}

header{
background:#161b22;
padding:20px;
text-align:center;
}

.container{
width:90%;
margin:auto;
padding:20px;
}

.card{
background:#161b22;
padding:20px;
margin:20px 0;
border-radius:10px;
}

button{
padding:10px 20px;
background:#238636;
color:white;
border:none;
border-radius:5px;
cursor:pointer;
}

input{
padding:10px;
width:70%;
margin:10px;
}

a{
color:#58a6ff;
text-decoration:none;
}

footer{
background:#161b22;
padding:20px;
text-align:center;
margin-top:40px;
}

</style>

</head>

<body>

<header>

<h1>🛡 CyberShield</h1>

<h2>ICT FOR CYBERSECURITY</h2>

</header>

<div class="container">

<div class="card">

<h2>🔒 Password Strength Checker</h2>

<form method="POST">

<input type="hidden" name="tool" value="password">

<input type="password" name="password" placeholder="Enter password">

<button type="submit">Check</button>

</form>

<p>{{password_result}}</p>

</div>

<div class="card">

<h2>🎣 Phishing Detector</h2>

<form method="POST">

<input type="hidden" name="tool" value="phishing">

<input type="text" name="url" placeholder="Paste URL">

<button type="submit">Check</button>

</form>

<p>{{phishing_result}}</p>

</div>

<div class="card">

<h2>🦠 Malware Detector</h2>

<form method="POST">

<input type="hidden" name="tool" value="malware">

<input type="text" name="filename" placeholder="example.exe">

<button type="submit">Check</button>

</form>

<p>{{malware_result}}</p>

</div>

<div class="card">

<h2>🔐 Hacker Detection</h2>

<form method="POST">

<input type="hidden" name="tool" value="hacker">

<input type="number" name="attempts" placeholder="Failed Login Attempts">

<button type="submit">Analyze</button>

</form>

<p>{{hacker_result}}</p>

</div>

<div class="card">

<h2>🏭 Industry Benefits</h2>

<ul>

<li>Protects sensitive data</li>

<li>Prevents cyber attacks</li>

<li>Secures online transactions</li>

<li>Improves business trust</li>

<li>Reduces financial losses</li>

</ul>

</div>

<div class="card">

<h2>📊 Cybersecurity Facts</h2>

<p>95% of cyberattacks occur due to human error.</p>

<p>Every 39 seconds a cyberattack happens.</p>

<p>80% of breaches involve weak passwords.</p>

</div>

</div>

<footer>

<h3>University ICT Project</h3>

<p>Muhammad Sameer - 25-ME-151</p>

<p>Shabaz Malik - 25-ME-155</p>

<p>Zain Abbas - 25-ME-159</p>

</footer>

</body>

</html>

"""

@app.route("/", methods=["GET","POST"])

def home():

    password_result=""
    phishing_result=""
    malware_result=""
    hacker_result=""

    if request.method=="POST":

        tool=request.form["tool"]

        if tool=="password":

            password=request.form["password"]

            score=0

            if len(password)>=8:
                score+=1

            if re.search(r"[A-Z]",password):
                score+=1

            if re.search(r"[a-z]",password):
                score+=1

            if re.search(r"\d",password):
                score+=1

            if re.search(r"[@$!%*?&]",password):
                score+=1

            if score<=2:
                password_result="❌ Weak Password"

            elif score<=4:
                password_result="⚠ Medium Password"

            else:
                password_result="✅ Strong Password"

        if tool=="phishing":

            url=request.form["url"]

            words=["login","verify","free","update","secure"]

            if "@" in url or any(w in url.lower() for w in words):

                phishing_result="⚠ Suspicious URL"

            else:

                phishing_result="✅ URL Looks Safe"

        if tool=="malware":

            filename=request.form["filename"]

            dangerous=[".exe",".bat",".scr",".vbs",".ps1"]

            if any(filename.lower().endswith(x) for x in dangerous):

                malware_result="⚠ Potential Malware"

            else:

                malware_result="✅ Safe File"

        if tool=="hacker":

            attempts=int(request.form["attempts"])

            if attempts<5:

                hacker_result="🟢 Safe"

            elif attempts<10:

                hacker_result="🟡 Suspicious"

            else:

                hacker_result="🔴 High Risk"

    return render_template_string(
        HTML,
        password_result=password_result,
        phishing_result=phishing_result,
        malware_result=malware_result,
        hacker_result=hacker_result
    )

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
```
