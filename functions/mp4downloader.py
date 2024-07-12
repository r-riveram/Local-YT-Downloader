from pytube import YouTube

def descargar_mp4(enlace, destination_folder):
    try:
        yt = YouTube(enlace)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=destination_folder)
        return 'Video MP4 descargado exitosamente.'
    except Exception as e:
        return f'Error al descargar: {str(e)}'
