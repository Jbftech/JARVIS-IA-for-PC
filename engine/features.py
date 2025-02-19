from playsound import playsound
import eel

# Play assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\Boot.mp3"
    playsound(music_dir)