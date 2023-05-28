import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a random response from the Magic 8-Ball
def generate_response():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    response = random.choice(responses)
    response_label.config(text=response)

# Function to handle button click event
def submit_question():
    # Get the user's question from the question entry field
    question = question_entry.get()
    # Check if the user entered a question
    if question:
        # If the user entered a question, generate a response and display it
        generate_response()
    else:
        # If the user did not enter a question, display an error message
        messagebox.showinfo("Error", "Please enter a question.")

# Create the main window
window = tk.Tk()
window.title("Magic 8-Ball")

# Set the size of the window
window.geometry("800x200")

# Create and configure widgets
question_label = tk.Label(window, text="Enter your yes/no question:", font=("Arial", 16))
question_label.pack()

question_entry = tk.Entry(window, width=60, font=("Arial", 16))
question_entry.pack()

submit_button = tk.Button(window, text="Ask", command=submit_question, font=("Arial", 16))
submit_button.pack()

response_label = tk.Label(window, text="", font=("Arial", 16))
response_label.pack()

# Start the main event loop
window.mainloop()