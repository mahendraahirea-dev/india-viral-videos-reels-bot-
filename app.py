from flask import Flask
import threading, time, feedparser
from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw
import textwrap
from datetime import datetime

app = Flask(__name__)
BLOGGER_RSS = "https://lemonnliveofficial.blogspot.com/feeds/posts/default?alt=rss"

def create_viral_video():
    feed = feedparser.parse(BLOGGER_RSS)
    title = feed.entries[0].title if feed.entries else "Ahilyanagar Breaking"
    print(f"AUTO: {title} -> YT Video", flush=True)
    try:
        tts = gTTS(text=title, lang='mr')
        tts.save("/tmp/voice.mp3")
        audio = AudioFileClip("/tmp/voice.mp3")
        bg = Image.new('RGB', (1080,1920), color=(10,25,60))
        ImageDraw.Draw(bg).text((50,300), textwrap.fill(title, 22), fill=(255,255,255))
        bg.save("/tmp/bg.png")
        clip = ImageClip("/tmp/bg.png").set_duration(audio.duration).set_audio(audio)
        clip.write_videofile(f"/tmp/SHORT_{datetime.now():%Y%m%d_%H%M}.mp4", fps=24, logger=None)
        print("VIDEO READY - PAISA BOT DONE", flush=True)
    except Exception as e:
        print(f"ERROR: {e}", flush=True)

def background_worker():
    print("YT PAISA BOT WORKER STARTED", flush=True)
    while True:
        create_viral_video()
        time.sleep(10800) # dar 3 tas

threading.Thread(target=background_worker, daemon=True).start()

@app.route('/')
def home():
    return "<h1>YT PAISA BOT LIVE ✅</h1><p>Auto every 3 hours</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
