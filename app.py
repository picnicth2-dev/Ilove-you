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
}

/* ---------- SVG ---------- */
svg {
    width: 100vw;
    max-height: 40vh;
}

/* เส้นเงาด้านหลัง (เส้นหนา) */
.shade {
    fill: none;
    stroke: #ff9bbd;
    stroke-width: 10;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 1200;
    stroke-dashoffset: 1200;
    animation: draw 4s ease forwards;
}

/* เส้นหลักด้านหน้า */
.draw {
    fill: none;
    stroke: #ff1a75;
    stroke-width: 5;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 1200;
    stroke-dashoffset: 1200;
    animation: draw 4s ease forwards;
    animation-delay: 0.15s;
}

@keyframes draw {
    to {
        stroke-dashoffset: 0;
    }
}
</style>
</head>

<body>

<svg viewBox="0 0 900 360" preserveAspectRatio="xMidYMid meet">

    <!-- ===== เงา ===== -->
    <path class="shade" d="
        M50 80 L50 260
        M120 80 L120 260
        M120 80 L200 80
        M120 170 L200 170
        M120 260 L200 260

        M260 80 L260 260
        M260 80 Q340 80 340 170
        M340 170 Q340 260 260 260

        M380 80 L380 260
        M380 260 L460 260
        M460 260 L460 80

        M520 80 L560 260
        M560 260 L600 80

        M650 80 L650 260
        M650 260 L720 170
        M720 170 L790 260
    "/>

    <!-- ===== เส้นจริง ===== -->
    <path class="draw" d="
        M50 80 L50 260
        M120 80 L120 260
        M120 80 L200 80
        M120 170 L200 170
        M120 260 L200 260

        M260 80 L260 260
        M260 80 Q340 80 340 170
        M340 170 Q340 260 260 260

        M380 80 L380 260
        M380 260 L460 260
        M460 260 L460 80

        M520 80 L560 260
        M560 260 L600 80

        M650 80 L650 260
        M650 260 L720 170
        M720 170 L790 260
    "/>

</svg>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)