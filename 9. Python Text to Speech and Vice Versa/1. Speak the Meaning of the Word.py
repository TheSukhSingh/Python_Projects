import pyttsx3
from PyDictionary import PyDictionary

def speak(audio):

	# Having the initial constructor of pyttsx3 
	# and having the sapi5 in it as a parameter
	engine = pyttsx3.init('sapi5')
	
	# Calling the getter and setter of pyttsx3
	voices = engine.getProperty('voices')
	
	# Method for the speaking of the assistant
	engine.setProperty('voice', voices[0].id)
	engine.say(audio)
	engine.runAndWait()

def Dictionary(wordmean):
	dic = PyDictionary()
	
	# Taking the string input
	
	word = dic.meaning(wordmean)
	return word

speak("Which word do u want to find the meaning sir")
query = str(input())
meaning = Dictionary(query)

for state in meaning:
		print(meaning[state])
		speak("the meaning is")
		speak(str(meaning[state]))