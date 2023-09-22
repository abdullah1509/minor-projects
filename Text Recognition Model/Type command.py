
import pyttsx3
import datetime
import webbrowser
import time
import subprocess
import tkinter as tk
from tkinter import Scrollbar, Entry, Button

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak("Hello,Good Morning, How can i help you")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon,How can i help you")
    else:
        speak("Hello,Good Evening,How can i help you")

greetings = ["hello","hi","Hi","Hey","Howdy","Good morning","Good afternoon""Good evening""Hi there","What's up?",
           "How's it going?","Greetings","Salutations","How are you?","How's everything?","Sup?","Yo"]


root = tk.Tk()
root.title("Myassist")

# Create a frame for the chat display
chat_frame = tk.Frame(root)
chat_frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a Text widget to display chat messages
chat_display = tk.Text(chat_frame, wrap=tk.WORD, font=("Arial", 12))
chat_display.grid(row=0, column=0, sticky="nsew")
chat_display.config(state=tk.DISABLED)
chat_canvas = tk.Canvas(chat_frame, borderwidth=0, highlightthickness=0)
chat_canvas.grid(row=0, column=0, sticky="nsew")
scrollbar = Scrollbar(chat_frame, command=chat_canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
chat_canvas.config(yscrollcommand=scrollbar.set)
y_position = 10


# Function to add a chat bubble to the chat display
def add_chat_bubble(sender, message, alignment):
    global y_position
    x1, y1, x2, y2 = 10, y_position, 300, y_position + 30
    color = "lightblue" if sender == "Myassist" else "lightgreen"

    if sender == "Myassist":
        x1, y1, x2, y2 = 10, y_position, 300, y_position + 30
    else:
        x1, y1, x2, y2 = 400, y_position, 690, y_position + 30
    chat_canvas.create_oval(x1, y1, x2, y2, fill=color)

    # Create text inside the chat bubble
    chat_canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=message, fill="black", font=("Arial", 12))

    y_position += 40
    # Scroll the canvas to the end of the chat
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
    chat_display.config(state=tk.NORMAL)

    # Set text color and alignment based on sender
    text_color = "green" if sender == "Myassist" else "blue"

    # Add the chat bubble with proper formatting
    chat_display.insert(tk.END, f"\n{message}\n", ("message",), "\n")

    # Configure tag styles for sender name and message
    if sender == "Myassist":
        chat_display.tag_configure("message", foreground="Blue", justify="left")
    else:
        chat_display.tag_configure("message", foreground=text_color, justify="left")

    # Scroll to the end of the chat display
    chat_display.see(tk.END)

    chat_display.config(state=tk.DISABLED)


# Create a Scrollbar for the Text widget
scrollbar = Scrollbar(chat_frame, command=chat_display.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
chat_display.config(yscrollcommand=scrollbar.set)
# Create an Entry widget for user input
user_input = Entry(root, font=("Arial", 12))
user_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
wishMe()


# Function to handle user input
def handle_user_input():
    global y_position
    statement = user_input.get()
    add_chat_bubble("You", statement, "left")

    # Clear the user input field

    if statement in greetings:
        speak("Hi, How can I help you")
        add_chat_bubble("Myassist", "Hi, How can I help you", "left")

    elif "good bye" in statement or "ok bye" in statement or "stop" in statement:
        response = 'Your assistant is shutting down. Goodbye!'
        speak(response)
        add_chat_bubble("Myassist", response, "left")
        root.after(2000, root.destroy)

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        add_chat_bubble("Myassist", "Youtube is open now", "left")
        speak("youtube is open now")
        time.sleep(5)

    # Rest of your code...

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        add_chat_bubble("Myassist", "Google chrome is open now", "right")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        add_chat_bubble("Myassist", "Google Mail is open now", "left")
        speak("Google Mail open now")
        time.sleep(5)

    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        add_chat_bubble("Myassist", strTime, "left")
        speak(f"the time is {strTime}")

    elif 'search' in statement:
        statement = statement.replace("search", "")
        speak("the results displayed")
        add_chat_bubble("Myassist", "The results displayed", "left")
        webbrowser.open_new_tab(statement)
        time.sleep(5)

    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am your personal assistant. I can help you'
              'open youtube,google chrome, gmail,predict time and search something')
        add_chat_bubble("Myassist", 'I am your personal assistant.', "left")

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Abdullah")
        add_chat_bubble("Myassist", "I was built by Abdullah", "left")
        print("I was built by Abdullah")

    elif "shut down" in statement or "sign out" in statement:
        speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        add_chat_bubble("Myassist", "Shutting down", "left")
        subprocess.call(["shutdown", "/l"])
    else:
        speak("Sorry, Unable to answer this query")
        add_chat_bubble("Myassist", "Sorry, unable to answer this query", "left")


# Create a button to send the user's message
send_button = Button(root, text="Ask", command=handle_user_input, bg="blue", fg="white", font=("Calibri", 12), relief="sunken")
send_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# Start the GUI event loop
root.mainloop()