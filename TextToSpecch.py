import pyttsx3 #importing library that converts text to speech
import wikipedia #importing Wikipedia so we can extract info from there

voice = pyttsx3.init()#initialize text to speech engine and create speech engine name voice
while(1):
    In = input("Wiki Search: ") 
    result= wikipedia.summary(In, sentences= 3)
    print(result)
    voice.say(result) #passes the fetched summary to the text-to-speech engine to convert it into speech.
    voice.runAndWait() #executes the speech synthesis, vocalizing the summary retrieved from Wikipedia.
