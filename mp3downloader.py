from pytube import YouTube
import os

def descargar_mp3(enlace, destination_folder):
    try:
        yt = YouTube(enlace)
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path=destination_folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return 'Audio MP3 descargado exitosamente.'
    except Exception as e:
        return f'Error al descargar: {str(e)}'
