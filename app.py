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
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
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

/* ทำให้ SVG พอดีจอมือถือ */
svg {
    width: 100vw;
    height: auto;
    max-height: 60vh;
}

/* เส้นหลัก */
.draw {
    fill: none;
    stroke: #ff1a75;
    stroke-width: 4;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 800;
    stroke-dashoffset: 800;
    animation: draw 4s ease forwards;
}

/* เส้นเงา (แรเงา) */
.shade {
    fill: none;
    stroke: rgba(255, 26, 117, 0.25);
    stroke-width: 6;
    stroke-linecap: round;
    stroke-linejoin: round;
}

/* delay ทีละคำ */
.draw:nth-child(2) { animation-delay: 0.3s; }
.draw:nth-child(3) { animation-delay: 0.6s; }
.draw:nth-child(4) { animation-delay: 0.9s; }
.draw:nth-child(5) { animation-delay: 1.2s; }
.draw:nth-child(6) { animation-delay: 1.5s; }

@keyframes draw {
    to {
        stroke-dashoffset: 0;
    }
}

.subtitle {
    position: fixed;
    bottom: 8%;
    width: 100%;
    text-align: center;
    font-family: Arial, sans-serif;
    color: #555;
    font-size: 1.1rem;
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

<svg viewBox="0 0 900 200" preserveAspectRatio="xMidYMid meet">

    <!-- เงา -->
    <g transform="translate(2,2)">
        <path class="shade" d="M50 40 L50 160" />
        <path class="shade" d="M150 40 L150 160 L220 160" />
        <path class="shade" d="M320 100 m -35,0 a 35,35 0 1,0 70,0 a 35,35 0 1,0 -70,0" />
        <path class="shade" d="M420 40 L460 160 L500 40" />
        <path class="shade" d="M600 40 L600 160
                                M600 40 L680 40
                                M600 100 L660 100
                                M600 160 L680 160" />
        <path class="shade" d="M760 40 L800 100 L840 40
                                M800 100 L800 160
                                M860 100 a 25,25 0 1,0 0.1,0" />
    </g>

    <!-- เส้นจริง -->
    <path class="draw" d="M50 40 L50 160" />
    <path class="draw" d="M150 40 L150 160 L220 160" />
    <path class="draw" d="M320 100 m -35,0 a 35,35 0 1,0 70,0 a 35,35 0 1,0 -70,0" />
    <path class="draw" d="M420 40 L460 160 L500 40" />
    <path class="draw" d="M600 40 L600 160
                           M600 40 L680 40
                           M600 100 L660 100
                           M600 160 L680 160" />
    <path class="draw" d="M760 40 L800 100 L840 40
                           M800 100 L800 160
                           M860 100 a 25,25 0 1,0 0.1,0" />
</svg>

<div class="subtitle">
    ร๊ากเธอตลอดไปนะค้าบบ❤️ จุ๊บมั่ว😘😘☺️ 
</div>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)