from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

LOVE_MESSAGES = [
    "You make the world better just by being here 💖",
    "Someone smiled today because of you 😊",
    "You are deeply appreciated 🌷",
    "You matter more than you think ❤️",
    "Your presence brings warmth ☀️",
    "You’re doing great, even on hard days 🌱",
    "You are enough, exactly as you are ✨",
    "You bring good energy wherever you go 🌈"
]

@app.route("/")
def index():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>💖 Random Love Messages 💖</title>
    <style>
        body {
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: -apple-system, BlinkMacSystemFont, Arial;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            text-align: center;
            padding: 20px;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 18px;
            font-size: 22px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: opacity 0.4s ease;
            max-width: 90%;
        }
    </style>
</head>
<body>
    <div class="card" id="message">Loading love… 💕</div>

    <script>
        async function loadMessage() {
            try {
                const res = await fetch("/message", { cache: "no-store" });
                const data = await res.json();
                const el = document.getElementById("message");
                el.style.opacity = 0;
                setTimeout(() => {
                    el.textContent = data.message;
                    el.style.opacity = 1;
                }, 200);
            } catch (e) {
                console.error(e);
            }
        }

        loadMessage();
        setInterval(loadMessage, 5000); // change every 5 seconds
    </script>
</body>
</html>
"""
    return render_template_string(html)

@app.route("/message")
def message():
    return jsonify({
        "message": random.choice(LOVE_MESSAGES)
    })

if __name__ == "__main__":
    # Fly.io internal port must be 8080
    app.run(host="0.0.0.0", port=8080)
