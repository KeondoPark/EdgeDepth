import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=2)
sr.Microphone.list_microphone_names()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    r.recognize_google(audio)