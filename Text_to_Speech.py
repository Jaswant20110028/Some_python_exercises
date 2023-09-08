import win32com.client as w

speaker=w.Dispatch("SAPI.SpVoice")

speaker.speak("Jaswant is a hero") 