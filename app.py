from flask import Flask, render_template_string
import os

app = Flask(__name__)

# หน้าตาเว็บ (HTML + CSS + JS) ที่แปลงมาจาก GitHub ต้นฉบับ
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Will You Be My Valentine?</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #ffe6e6;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .container {
            padding: 20px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        h1 { color: #ff4d94; font-size: 2.5rem; }
        .buttons { margin-top: 30px; position: relative; width: 300px; height: 100px; }
        button {
            padding: 15px 30px;
            font-size: 1.2rem;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
        }
        #yesBtn { background-color: #ff4d94; color: white; margin-right: 10px; }
        #noBtn { background-color: #808080; color: white; position: absolute; }
        img { width: 200px; border-radius: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/c76IJLufpN762clOW7/giphy.gif" alt="cute bear">
        <h1>Will you be my Valentine? ❤️</h1>
        <div class="buttons">
            <button id="yesBtn" onclick="celebrate()">Yes</button>
            <button id="noBtn" onmouseover="moveButton()">No</button>
        </div>
    </div>

    <script>
        function moveButton() {
            const btn = document.getElementById('noBtn');
            const x = Math.random() * (window.innerWidth - btn.offsetWidth);
            const y = Math.random() * (window.innerHeight - btn.offsetHeight);
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        }

        function celebrate() {
            document.body.innerHTML = `
                <div style="text-align:center;">
                    <h1 style="font-size:4rem;">YAYYY! ❤️</h1>
                    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMngxbmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3bmZ3JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/MDJ9Nmc1MlhM424pSi/giphy.gif" width="300">
                    <p style="font-size:1.5rem; color:#ff4d94;">I Love You So Much!</p>
                </div>
            `;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
