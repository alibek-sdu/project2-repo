import pyttsx3

engine = pyttsx3.init("nsss") #Тичер, это для Мака, для других ОС сам поменяйте драйвер чтобы запустить Список: espeak, sapi5
text = "Hello, how are you today?"
audio_file_path = "output.mp3"
engine.save_to_file(text, audio_file_path)
engine.runAndWait()
