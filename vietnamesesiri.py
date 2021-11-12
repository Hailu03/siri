
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
            robot_brain = "Ngân ơi trên đời này mà có ai đẹp bằng Ngân đi nữa thì người đó cũng không xứng làm người yêu Hải"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "quá" in you:
            robot_brain = "Chào Ngân"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "đẹp"in you:
            robot_brain = "Ngân là một cô gái cực kỳ xinh đẹp và dễ thương thật mừng cho cô ấy khi cô ấy đã có một người yêu cũng tốt tính y chang cô ấy"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "thi" in you:
            robot_brain = "Ngân sắp phải thi giữa kỳ rồi cô ấy ôn tập rất chăm chỉ vì vậy tôi hy vọng cô ấy có thể đạt được điểm cao cố lên ngân"
            print("Robot:" + robot_brain)
            speak(robot_brain)
        elif "yêu" in you:
            robot_brain = "Ngân biết hông Hải yêu ngân nhất thế gian này luôn"
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
            robot_brain = "Tạm biệt Ngân"
            print("Robot: " + robot_brain)
            speak(robot_brain)
            
            break
        else:
            robot_brain = " Bạn muốn nói gì với tôi"
            print("Robot: " + robot_brain)
            speak(robot_brain)
        
    