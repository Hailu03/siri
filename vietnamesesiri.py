
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import date
from datetime import datetime
import playsound
import wikipedia

robot_brain =""
r= sr.Recognizer()

def speak(text):
    tts =gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
    with sr.Microphone() as source:
        audio_data = r.record(source, duration =5)
        print("Tôi đang nghe ...")
    
        try:
            you = r.recognize_google(audio_data, language = "vi")
        except:
            you=""
            print(you)

        if you == "":
            robot_brain = "Bạn có thể nói lại không tôi chưa nghe rõ"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "quá" in you:
            robot_brain = "Chào bạn"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "khỏe"in you:
            robot_brain = "Tôi dạo này còn khỏe lắm"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "ngày" in you:
            today = date.today()
            robot_brain = today.strftime("Hôm nay là ngày %d %m %Y")    
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "giờ" in you:
            now = datetime.now()
            robot_brain = now.strftime("%H giờ %M phút %S giây")
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif you:
            wikipedia.set_lang("vi")
            robot_brain=wikipedia.summary(you,sentences =1)
            print("Robot: " + robot_brain)
            speak(robot_brain)
        elif "biệt" in you:
            robot_brain = "Tạm biệt bạn"
            print("Robot: " + robot_brain)
            speak(robot_brain)
            
            break
        else:
            robot_brain = " Bạn muốn nói gì với tôi"
            print("Robot: " + robot_brain)
            speak(robot_brain)
        
    
