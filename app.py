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
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
}

body {
    background: white;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

svg {
    width: 90vw;
    max-width: 900px;
}

path {
    fill: none;
    stroke: #ff1a75;
    stroke-width: 6;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
    animation: draw 4s ease forwards;
}

path:nth-child(2) { animation-delay: 0.4s; }
path:nth-child(3) { animation-delay: 0.8s; }
path:nth-child(4) { animation-delay: 1.2s; }
path:nth-child(5) { animation-delay: 1.6s; }
path:nth-child(6) { animation-delay: 2.0s; }

@keyframes draw {
    to {
        stroke-dashoffset: 0;
    }
}

.subtitle {
    position: fixed;
    bottom: 10%;
    text-align: center;
    color: #555;
    font-size: 1.2rem;
    opacity: 0;
    animation: fadeIn 1.5s ease forwards;
    animation-delay: 4.2s;
}

@keyframes fadeIn {
    to { opacity: 1; }
}
</style>
</head>

<body>

<!-- SVG เขียนคำว่า I LOVE YOU -->
<svg viewBox="0 0 900 200">
    <!-- I -->
    <path d="M50 40 L50 160" />

    <!-- L -->
    <path d="M150 40 L150 160 L220 160" />

    <!-- O -->
    <path d="M320 100
             m -40, 0
             a 40,40 0 1,0 80,0
             a 40,40 0 1,0 -80,0" />

    <!-- V -->
    <path d="M420 40 L460 160 L500 40" />

    <!-- E -->
    <path d="M600 40 L600 160
             M600 40 L680 40
             M600 100 L660 100
             M600 160 L680 160" />

    <!-- YOU -->
    <path d="M760 40 L800 100 L840 40
             M800 100 L800 160
             M860 100
             a 30,30 0 1,0 0.1,0" />
</svg>

<div class="subtitle">
    ร๊ากเธอตลอดไปจุ๊บมั่วว ❤️
</div>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)