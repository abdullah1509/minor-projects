from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import pyjokes
import requests

# Local speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 = male, 1 = female

### PARAMETERS ###
activationWord = 'computer'

# Configure browser
# Set the path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# Register the browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text, 'txt')
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')

    except Exception as exception:
        print('I did not get that')
        speak('I did not get that')
        print(exception)
        return 'None'

    return query


def search_wikipedia(keyword=''):
    searchResults = wikipedia.search(keyword)
    if not searchResults:
        print('No result found')
        return 'No result found'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary


def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']


# App id obtained by the above steps
app_id = 'KY2A75-6TEG4Q453T'

# Instance of wolframalpha
wolframClient = wolframalpha.Client(app_id)


def search_wolframalpha(keyword=''):
    response = wolframClient.query(keyword)

    # Query not resolved
    if response['@success'] == 'false':
        speak('I could not compute')

    # Query resolved
    else:
        result = ''
        # Question
        pod0 = response['pod'][0]

        # if it's primary or has the title of result or definition, then it's the official result
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or (
                'definition' in pod1['@title'].lower()):
            # Get the result
            result = listOrDict(pod1['subpod'])
            return result.split('(')[0]
        else:
            # Get the interpretation from pod0
            question = listOrDict(pod0['subpod'])
            return (question.split('(')[0])

            speak('Computation failed. Searching wikipedia.')
            return search_wikipedia(question)

# code
def tellTime(keyword=''):
    time = str(datetime.now())
    return time


def tellDay(keyword=''):
    day = datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return day_of_the_week


# Main loop
if __name__ == '__main__':
    speak('Hello!! My name is Computer. How may I assist You?', 120)

    while True:
        # Parse as a list
        # query = 'computer say hello'.split()
        query = parseCommand()

        # Set commands
        if 'hello' in query:
            speak('Greetings to all')

        # Wikipedia
        if 'Wikipedia' in query:
            query = ' '.join(query[1:])
            speak('Checking the wikipedia ')
            result = search_wikipedia(query)
            print(result)
            speak('Do you want me to read that for you?')
            ans = parseCommand()
            if 'yes' in ans:
                speak("According to wikipedia")
                speak(result)

        # Wolfram Alpha
        if 'what' in query:
            query = ' '.join(query[1:])
            try:
                result = search_wolframalpha(query)
                print(result)
                speak(result)
            except:
                print('Unable to compute')
                speak('Unable to compute')

        # Note taking
        if 'notes' in query:
            print('Ready to record your note')
            speak('Ready to record your note')
            newNote = parseCommand().lower()
            now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            with open('note_%s.txt' % now, 'w') as newFile:
                newFile.write(now)
                newFile.write(' ')
                newFile.write(newNote)
            print('Note written')
            speak('Note written')

        if "open" in query:
            if "Geeks" in query:
                speak("Opening GeeksforGeeks ")
                webbrowser.get('chrome').open_new("www.geeksforgeeks.org")
            elif "Google" in query:
                speak("Opening Google ")
                webbrowser.get('chrome').open_new("www.google.com")
            elif "YouTube" in query:
                speak("Opening YouTube ")
                webbrowser.get('chrome').open_new("www.youtube.com")
            elif "stack" in query:
                speak("Opening StackOverFlow. Happy coding ")
                webbrowser.get('chrome').open_new("https://stackoverflow.com/")

        if 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?")

        if 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        if 'joke' in query:
            result = pyjokes.get_joke()
            speak(result)
            print(result)

        if "who I am" in query:
            speak("If you talk then definitely your human.")

        if 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        if "which day it is" in query:
            result = tellDay()
            print(result)
            speak("The day is " + result)

        if "the time" in query:
            result = tellTime(query)
            print(result)
            hour = result[11:13]
            min = result[14:16]
            speak("The time is " + hour + " Hours and " + min + " Minutes ")

        if "tell me your name" in query:
            speak("I am Computer. Your desktop Assistant")

        if "bye" in query or 'exit' in query or 'close' in query:
            print('Goodbye')
            speak('Goodbye')
            break

