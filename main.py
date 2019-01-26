import speech_recognition as sr
import files_folders_open as ffo
import music
import utilities
import google_surf
import run_executables
import wave
import pyaudio

r = sr.Recognizer()
r.energy_threshold=2500
r.operation_timeout = 2
fil_name = "nothisdfdfs"

def play_sound(music_name):
    chunk = 1024  
    f = wave.open(r"{}".format(music_name),"rb")  
    p = pyaudio.PyAudio()  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    data = f.readframes(chunk)  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
    stream.stop_stream()  
    stream.close()  
    p.terminate() 

while True:
    with sr.Microphone() as source :
        print("Say something!")
        audio = r.listen( source )
    
    try:
        str = r.recognize_google(audio)
        str = str.lower()
        print(str)
        li = []
        def get_words(str):
            li = str.split()
            return li
             
        li = get_words(str)

        if "open" in li or "Open" in li or "close" in li or "back" in li or "organise" in li:
            ffo.opening(li)
        elif ("play" in li or "Play" in li) and ("music" in li or "Music" in li):
            music.play_music(li[1])
        elif "switch" in li:
            utilities.tabs_switching_operation()
        elif "search" in li and "google" in li:
            google_surf.search()
        elif "run" in li:
            run_executables.run_executable(" ".join(li[1:]))
        elif "bye" in li:
            break
    except sr.UnknownValueError:
    	play_sound('sorry.wav')
        #print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
