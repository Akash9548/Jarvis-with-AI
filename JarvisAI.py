#Understood the use cases of following libraries which helped me in achieving the task:
import speech_recognition as sr 
import pyttsx3
import os
import webbrowser
import openai

# --- SETUP ---

# Replace with your actual OpenAI API key
openai.api_key = "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"

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

def speak(text):
    print("Jarvis:", text)
    speaker.say(text)
    speaker.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn't catch that.")
        return ""

# --- CHATGPT API LOGIC ---
def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print(e)
        return "Sorry, I couldn't connect to ChatGPT."

# --- MAIN FUNCTION ---
def run_jarvis():
    speak("Hello Sir! I'm ready to assist you.")
    
    while True:
        command = take_command()

        if "notepad" in command:
            speak("Opening Notepad")
            os.startfile("notepad")

        elif "file explorer" in command:
            speak("Opening File Explorer")
            os.system("explorer")

        elif "chrome" in command:
            speak("Opening Google Chrome")
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "microsoft edge" in command:
            speak("Opening Microsoft Edge")
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edge_path)

        elif "calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        elif "create folder" in command or "make folder" in command:
            speak("What should I name the folder?")
            folder_name = take_command()

            if folder_name:
                base_path = "C:\\Users\\kumar\\Desktop"
                folder_path = os.path.join(base_path, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    speak(f"Folder named {folder_name} has been created.")
                else:
                    speak("A folder with that name already exists.")
            else:
                speak("I didn't get the folder name.")

        elif "ask chat gpt " in command or "question" in command:
            speak("What do you want to ask ChatGPT?")
            user_question = take_command()

            if user_question:
                speak("Thinking...")
                answer = ask_chatgpt(user_question)
                speak(answer)

        elif "exit" in command or "stop" in command or "quit" in command:
            speak("Goodbye Sir! Shutting down.")
            break

        elif command != "":
            speak("Sorry, I don't know that command yet.")

# --- START JARVIS ---
run_jarvis()
