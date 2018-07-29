import speech_recognition as sr
import webbrowser as wb

chrome_path = '/usr/bin/google-chrome'
r = sr.Recognizer()

with sr.Microphone() as source:
	print('Say Something!')
	audio = r.listen(source)
	print('Done')

try:
	text = r.recognize_google(audio)
	print('Google thinks you said: \n' + text)
	
	c_text = 'https://www.google.co.in/search?q='+text      
	wb.get(chrome_path).open(c_text)

except Exception as e:
	print(e)
	
