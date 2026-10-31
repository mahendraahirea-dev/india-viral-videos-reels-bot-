from fastapi import FastAPI
import random
from datetime import datetime
app = FastAPI()
TOPICS = {
 "sarkari_yojana": ["PM Silai Machine Yojana 15000", "Ladli Behna Yojana", "PM Awas Yojana 2.5 Lakh"],
 "business": ["Gaon me 20k wala business", "0 se Crore - Raj Shamani Style", "Student 500 roj kamao"],
 "motivation": ["Aaj ka gyan zindagi badal dega", "1% Rule - Roz better bano"],
 "bhakti": ["Hanuman mantra sunte hi kaam banega"]
}
@app.get("/")
def home():
    return {"status": "LIVE - SAFE, Dhan se alag", "time": str(datetime.now())}
@app.get("/create-reel")
def create_reel():
    niche = random.choice(list(TOPICS.keys()))
    topic = random.choice(TOPICS[niche])
    return {"niche": niche, "topic": topic, "script": f"{topic} - Viral hoga! Follow karo.", "format": "9:16"}
@app.get("/.well-known/claude-connector")
def connector():
    return {"name": "India Viral Reels - Safe"}
