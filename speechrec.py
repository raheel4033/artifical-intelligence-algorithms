import speech_recognition as sr

r=sr.Recognizer()

audio='test.wav'

with sr.AudioFile(audio) as source:
    r.adjust_for_ambient_noise(source)
    print('Converting.....')
    audio=r.record(source)

try:
    test=r.recognize_google(audio)
    print(test)
except Exception as e:
    print(e)


