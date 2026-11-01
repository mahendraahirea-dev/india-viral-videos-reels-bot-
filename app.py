from flask import Flask
import threading, time, feedparser
from datetime import datetime

app = Flask(__name__)
BLOGGER_RSS = "https://lemonnliveofficial.blogspot.com/feeds/posts/default?alt=rss"

def background_worker():
    print("YT PAISA BOT WORKER STARTED - LIGHT MODE", flush=True)
    while True:
        try:
            feed = feedparser.parse(BLOGGER_RSS)
            title = feed.entries[0].title if feed.entries else "No news"
            print(f"[{datetime.now()}] AUTO CHECK: {title}", flush=True)
            print("VIDEO READY (Test Mode) - FULL AUTO", flush=True)
        except Exception as e:
            print(f"ERROR: {e}", flush=True)
        time.sleep(10800)

threading.Thread(target=background_worker, daemon=True).start()

@app.route('/')
def home():
    return """
    <h1>YT PAISA BOT LIVE ✅</h1>
    <h2>India Viral Videos - FULL AUTO</h2>
    <p>Worker Started: Checking Blogger every 3 hours</p>
    <p>Status: LIVE</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
