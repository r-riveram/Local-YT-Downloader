from pytube import YouTube

def descargar_mp4(enlace, destination_folder, quality, progress_callback):
    try:
        yt = YouTube(enlace, on_progress_callback=progress_callback)
        if quality == "Highest":
            video = yt.streams.get_highest_resolution()
        else:
            video = yt.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()

        if not video:
            video = yt.streams.get_highest_resolution()
            quality_msg = f"No {quality} stream available. Downloading highest quality."
        else:
            quality_msg = f"Downloading {quality} quality."

        video.download(output_path=destination_folder)
        return f'MP4 video downloaded successfully. {quality_msg}'
    except Exception as e:
        return f'Error: {str(e)}'
