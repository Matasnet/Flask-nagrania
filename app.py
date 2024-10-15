import os
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def get_video_list():
    video_dir = 'static/videos'
    videos = []
    for filename in os.listdir(video_dir):
        if filename.endswith('.mp4'):  # Możesz dodać więcej rozszerzeń
            filepath = os.path.join(video_dir, filename)
            mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            videos.append({'name': filename, 'date': mod_time.strftime('%Y-%m-%d %H:%M:%S')})
    videos.sort(key=lambda x: x['date'], reverse=True)  # Sortuj od najnowszego
    return videos

@app.route('/')
def index():
    videos = get_video_list()
    
    # Paginacja
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_videos = len(videos)
    videos = videos[(page - 1) * per_page: page * per_page]
    
    return render_template('index.html', videos=videos, page=page, total_videos=total_videos, per_page=per_page)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
