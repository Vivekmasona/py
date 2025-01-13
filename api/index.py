from flask import Flask, request, Response
import yt_dlp

app = Flask(__name__)

@app.route('/stream', methods=['GET'])
def stream_audio():
    url = request.args.get('url')
    if not url:
        return "Please provide a YouTube URL as 'url' query parameter", 400
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            return Response(audio_url, mimetype='audio/mp3')
    except Exception as e:
        return str(e), 500

# Vercel automatically uses the app instance
