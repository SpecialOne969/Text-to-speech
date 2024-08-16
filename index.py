import tkinter as tk
from tkinter import messagebox
import pyttsx3

def text_to_speech():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Input Error", "Please enter some text to convert to speech.")

def clear_text():
    text_input.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Text to Speech Application")
root.geometry("400x300")
root.resizable(False, False)

# Create a text input widget
text_input = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), height=10, width=40)
text_input.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons with appropriate styling
speak_button = tk.Button(button_frame, text="Speak", command=text_to_speech, width=10)
speak_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, width=10)
clear_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
