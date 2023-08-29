import io
import vlc
import tempfile
from youtubesearchpython import VideosSearch
from pytube import YouTube
class MusicPlayer:
    def main(self, sentence):
        sentence = sentence.lower()
        if "play" in sentence:
            song_name = sentence.split("play ")[-1]
            self.play_music(song_name)

    def play_music(self, song_name):
        search = VideosSearch(song_name, limit=1)
        video_url = search.result()['result'][0]['link']
        
        youtube = YouTube(video_url)
        stream = youtube.streams.filter(only_audio=True).first()

        audio_data = io.BytesIO()
        stream.stream_to_buffer(audio_data)
        audio_data.seek(0)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_file.write(audio_data.read())
        temp_file.close()

        audio_instance = vlc.Instance()
        player = audio_instance.media_player_new()
        media = audio_instance.media_new_path(temp_file.name)
        player.set_media(media)
        player.play()

        while player.get_state() != vlc.State.Ended:
            pass

        player.release()
        temp_file.close()
        temp_file.unlink()
        
    def stop(self):
        audio_instance = vlc.Instance()
        player = audio_instance.media_player_new()
        player.stop()
        player.release()
        return

musicplayer = MusicPlayer()

if __name__ == "__main__":
    song_name = input("Enter the name of the song: ")
    musicplayer = MusicPlayer()
    musicplayer.play_music(song_name)
