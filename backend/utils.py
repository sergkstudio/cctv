import os
import subprocess
from datetime import datetime

def record_rtsp_stream(rtsp_url, output_dir, duration=60):
    """Записывает RTSP поток в файл"""
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = os.path.join(output_dir, f"video_{now}.mp4")
    command = [
        'ffmpeg', '-i', rtsp_url, '-t', str(duration),
        '-c:v', 'copy', '-c:a', 'aac', output_path
    ]
    subprocess.run(command)
    return output_path
