from flask import Flask, render_template_string
import os

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>เธอร๊ากเค้าม้ายยย</title>

<style>
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background: #ffe6ee;
    font-family: Arial, sans-serif;
}

.container {
    background: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

h1 {
    color: #ff4d94;
    font-size: 2.3rem;
}

.buttons {
    margin-top: 25px;
}

button {
    padding: 15px 35px;
    font-size: 1.2rem;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: 0.4s ease;
}

#yesBtn {
    background: #ff4d94;
    color: white;
}

#noBtn {
    background: #999;
    color: white;
    margin-left: 10px;
}

.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    font-size: 4rem;
    border-radius: 0;
    z-index: 999;
}
</style>
</head>

<body>
<div class="container" id="box">
    <h1 id="question">รักเค้าม๊ายยย❤️</h1>

    <div class="buttons">
        <button id="yesBtn" onclick="yesClick()">Yes</button>
        <button id="noBtn" onclick="noClick()">No</button>
    </div>

    <p id="emoji" style="font-size:2rem;margin-top:15px;"></p>
</div>

<script>
let noCount = 0;

function noClick() {
    noCount++;
    const emoji = document.getElementById("emoji");
    const question = document.getElementById("question");
    const yesBtn = document.getElementById("yesBtn");
    const noBtn = document.getElementById("noBtn");

    if (noCount === 1) {
        emoji.innerText = "🥺💗";
        question.innerText = "แน่ใจนะ…";
    } 
    else if (noCount === 2) {
        emoji.innerText = "😢👉👈";
        question.innerText = "คิดอีกทีได้ไหม";
    } 
    else if (noCount === 3) {
        emoji.innerText = "😭💞";
        question.innerText = "ใจร้ายไปแล้วนะ";
    } 
    else if (noCount === 4) {
        emoji.innerText = "🥹❤️‍🩹";
        question.innerText = "ครั้งสุดท้ายแล้วจริง ๆ";
    } 
    else if (noCount === 5) {
        question.innerText = "เธอรักเค้าไหม ❤️";
        emoji.innerText = "💘💘💘";

        yesBtn.classList.add("fullscreen");
        yesBtn.innerText = "รัก ❤️";

        noBtn.style.display = "none";
    }
}

function yesClick() {
    document.body.innerHTML = `
        <div style="text-align:center;">
            <h1 style="font-size:4rem;color:#ff4d94;">เย้!!! ❤️</h1>
            <p style="font-size:2rem;">เรารักกันน้าน่ารักที่สุด 💖</p>
        </div>
    `;
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)