from flask import *
from flask_compress import Compress
import os
import youtube_dl
from multiprocessing.pool import ThreadPool
import ssl

compress = Compress()
app = Flask(__name__)
app.secret_key = os.urandom(12)

def downloading(form):
    if form.get("type") == "영상 (mp4)":
        ty = "mp4"
        options = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]', 
            'noplaylist': True,
            'outtmpl': 'static/downloads/%(title)s.%(ext)s',
            'continuedl': True
        }
    else:
        ty = "mp3"
        options = {
            'format': 'bestaudio/best', 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],      
            'noplaylist': True,
            'outtmpl': 'static/downloads/%(title)s.%(ext)s',
            'continuedl': True         
        }
    with youtube_dl.YoutubeDL(options) as ydl:
        info = ydl.extract_info(form.get("link"), download=True)
    return info, ty


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/download_finish', methods=["POST", "GET"])
def download_page():
    if request.method == 'POST':
        try:
            form = request.form
                # ydl.download([form.get("link")] )
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(downloading, (form,))
            info = async_result.get()
            info, ty = info 
            return render_template("download_finish.html",title=info["title"], uploader=info["uploader"], ext=ty, thumbnail=info["thumbnail"])
        except:
            return redirect(url_for('main'))
    else:
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.debug = True
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='certfile.crt', keyfile='private.key', password='password')
    app.run(host="0.0.0.0", threaded=True, port=443, ssl_context=ssl_context)