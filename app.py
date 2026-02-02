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
    <title>I Love You</title>
    <style>
        body {
            background-color: white; /* พื้นหลังสีขาวตามคำขอ */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
        }
        .container {
            text-align: center;
            animation: fadeIn 2s;
        }
        h1 {
            color: #ff1a75;
            font-size: 5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        p {
            color: #555;
            font-size: 1.5rem;
        }
        .heart {
            color: #ff1a75;
            font-size: 4rem;
            animation: beat 1s infinite;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes beat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤️</div>
        <h1>I LOVE YOU</h1>
        <p>คุณคือคนพิเศษที่สุดของเค้านะ 😊</p>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
