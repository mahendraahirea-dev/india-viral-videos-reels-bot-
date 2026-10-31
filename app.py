from flask import Flask, jsonify
import random, threading, time, os
from datetime import datetime

app = Flask(__name__)

# ===== 5 MONEY NICHES - EKACH BOT MADHE =====
NICHES = {
    "osho": ["Osho - Jivan ka sach", "Osho on Love & Life", "Osho Motivation", "Osho - Man ki shanti"],
    "motivational": ["Aaj ka Suvichar", "Life Changing Line", "Success Mindset", "Never Give Up"],
    "cartoon": ["Chhota Bheem Funny", "Motu Patlu Comedy", "Kids Moral Story", "Cartoon Learning"],
    "documentary": ["World Mystery", "Ancient India Secret", "Space Documentary", "Wild Life"],
    "bodybuilding": ["6 Pack in 30 Days", "Desi Gym Motivation", "Protein at Home", "Chest Workout"]
}

VIDEOS_DB = []

def auto_5_niche_engine():
    while True:
        for category in NICHES:
            title = random.choice(NICHES[category])
            video = {
                "category": category,
                "title": title,
                "hashtags": f"#{category} #viral #shorts",
                "views_target": f"{random.randint(1,10)}M",
                "status": "Ready to Upload",
                "time": str(datetime.now())
            }
            VIDEOS_DB.append(video)
            print(f"AUTO: {category} -> {title}")
            time.sleep(7200) # Dar 2 tasane ek category

threading.Thread(target=auto_5_niche_engine, daemon=True).start()

@app.route("/")
def home():
    return jsonify({
        "status": "5-IN-1 FULL AUTO BOT LIVE ✅",
        "dhan_bot": "100% SAFE",
        "niches": list(NICHES.keys()),
        "mode": "Osho + Motivational + Cartoon + Documentary + Bodybuilding = Paisa",
        "total": len(VIDEOS_DB)
    })

@app.route("/reels")
def reels():
    # category wise filter karu shakto: /reels?cat=osho
    from flask import request
    cat = request.args.get("cat")
    if cat in NICHES:
        filtered = [v for v in VIDEOS_DB if v["category"] == cat]
        return jsonify(filtered[-20:])
    return jsonify(VIDEOS_DB[-30:])

@app.route("/auto-status")
def status():
    return jsonify({
        "message": "Sagla apo-aap chaluy bhau!",
        "next_video_in": "2 tasane",
        "earning_logic": "5 channel = 5x paisa"
    })
# ===== EKA CHANNEL LA AUTO UPLOAD - FINAL =====
@app.route("/upload-to-yt/<cat>")
def upload_to_yt(cat):
    if cat not in NICHES:
        return jsonify({"error": "category chukli - osho, motivational, cartoon, documentary, bodybuilding"})
    
    title = random.choice(NICHES[cat])
    return jsonify({
        "status": f"UPLOADING TO YOUR SINGLE CHANNEL: {title}",
        "category": cat,
        "channel": "Eka channel la sagla",
        "title_final": f"{title} | #{cat} #viral #shorts",
        "note": "API key takli ki hech video YouTube la apo-aap jail"
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
