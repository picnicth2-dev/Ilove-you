from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For You</title>
    <style>
        body {
            background-color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            /* ใช้ Font แบบตัวเหลี่ยม (Monospace) */
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            text-align: center;
        }
        .container {
            width: 90%; /* คุมขนาดไม่ให้ล้นขอบมือถือ */
        }
        .heart {
            font-size: 60px;
            color: #ff1a75;
            animation: beat 0.8s infinite;
            margin-bottom: 10px;
        }
        h1 {
            color: #ff3385;
            /* ปรับขนาดตัวอักษรให้พอดีมือถืออัตโนมัติ */
            font-size: 10vw; 
            font-weight: bold;
            letter-spacing: -2px;
            margin: 0;
            text-transform: uppercase;
        }
        .message {
            margin-top: 15px;
            color: #666;
            font-size: 14px;
            letter-spacing: 1px;
            opacity: 0;
            animation: fadeIn 2s forwards 1s;
        }
        @keyframes beat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤️</div>
        <h1>I LOVE YOU SO</h1>
        <div class="message">YOU ARE MY EVERYTHING</div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
