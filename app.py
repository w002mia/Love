from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

# Load 1000 facts from the text file
with open("alliance_francaise_facts.txt", "r", encoding="utf-8") as f:
    FACTS = [line.strip() for line in f.readlines()]

@app.route("/")
def index():
    html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>🎓 Alliance Française Bahrain Facts 🎓</title>
    <style>
        body { height:100vh; margin:0; display:flex; justify-content:center; align-items:center;
               font-family:-apple-system, BlinkMacSystemFont, Arial; background:linear-gradient(135deg,#a1c4fd,#c2e9fb);
               text-align:center; padding:20px; }
        .card { background:white; padding:30px; border-radius:18px; font-size:20px;
                box-shadow:0 10px 30px rgba(0,0,0,0.2); transition:opacity 0.4s ease; max-width:90%; }
    </style>
</head>
<body>
    <div class="card" id="fact">Loading facts… 📚</div>

    <script>
        async function loadFact() {
            try {
                const res = await fetch("/fact", { cache: "no-store" });
                const data = await res.json();
                const el = document.getElementById("fact");
                el.style.opacity = 0;
                setTimeout(() => { el.textContent = data.fact; el.style.opacity = 1; }, 200);
            } catch(e){ console.error(e); }
        }
        loadFact();
        setInterval(loadFact, 5000); // change every 5 seconds
    </script>
</body>
</html>
"""
    return render_template_string(html)

@app.route("/fact")
def fact():
    return jsonify({
        "fact": random.choice(FACTS)
    })

if __name__ == "__main__":
    # Fly.io internal port
    app.run(host="0.0.0.0", port=8080)
