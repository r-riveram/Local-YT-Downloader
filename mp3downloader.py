from pytube import YouTube
import os

def descargar_mp3(enlace, destination_folder, progress_callback):
    try:
        yt = YouTube(enlace, on_progress_callback=progress_callback)
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path=destination_folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return 'MP3 Audio downloaded successfully.'
    except Exception as e:
        return f'Error: {str(e)}'
