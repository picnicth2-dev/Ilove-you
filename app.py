from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>รักนะคุณแฟน</title>
    <style>
        body {
            background-color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Tahoma', sans-serif;
            overflow: hidden;
        }
        .heart {
            font-size: 100px;
            color: #ff1a75;
            animation: beat 0.8s infinite;
            margin-bottom: 20px;
        }
        .message {
            font-size: 24px;
            font-weight: bold;
            color: #ff3385;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #ff3385;
            width: 0;
            animation: typing 3s steps(30) forwards, blink 0.5s step-end infinite;
        }
        .sub-message {
            margin-top: 15px;
            color: #666;
            font-size: 18px;
            opacity: 0;
            animation: fadeIn 2s forwards 3.5s;
        }
        @keyframes beat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        @keyframes blink {
            from, to { border-color: transparent; }
            50% { border-color: #ff3385; }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="heart">❤️</div>
    <div class="message">รักเธอที่สุดในจักรวาล 💖</div>
    <div class="sub-message">เธอน่าร๊ากที่สุดดดดดดเลยละ ✨</div>
    <div class="sub-message" style="color: red; animation-delay: 5s;">อยู่ด้วยกันไปนานๆน้าาอ้วนน จุ๊บมั่ว❤️</div>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
