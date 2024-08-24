import json
import random
import re
import requests
import tkinter as tk
from tkinter import messagebox

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Chatty The ChatBot")

# Load intents from a JSON file that contains patterns and responses for the chatbot
with open('intents.json') as file:
    data = json.load(file)

# Function to match user input with predefined patterns in the intents
def match_intent(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            # Check if the user input matches any pattern in the intent
            if re.search(pattern.lower(), user_input.lower()):
                # Handle user_name intent where the bot recognizes a name
                if intent['tag'] == 'user_name':
                    match = re.search(pattern.lower(), user_input.lower())
                    name = match.group(1)
                    return random.choice(intent['responses']).replace('%1', name), False
                # Handle goodbye intent where the bot may exit
                elif intent['tag'] == 'goodbye':
                    return random.choice(intent['responses']), True
                else:
                    # Return a random response from the matched intent
                    return random.choice(intent['responses']), False
    # If no pattern matches, return a default response
    return "I didn't understand that. Can you please rephrase?", False

# Function to fetch weather data for a specified city using OpenWeatherMap API
def get_weather(city):
    api_key = "cf8e2f1742739dda0553b46f4056fdb2"  # Replace with your actual API key from OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:  # Successful response
        if "main" in data:
            # Convert temperature from Kelvin to Celsius
            temperature = data["main"]["temp"] - 273.15
            return f"The temperature in {city} is {temperature:.2f}°C", False
        else:
            return "Temperature data not available.", False
    elif data["cod"] == "404":  # City not found
        return f"Error: City '{city}' not found.", False
    else:
        # Handle other errors
        return f"Error: {data['message']}" if 'message' in data else "Unknown error.", False

# Function to determine whether to respond with weather data or match an intent
def respond(user_input):
    if "weather in" in user_input.lower():
        # Extract the city name from the user input
        match = re.search(r"weather in (.*)", user_input, re.IGNORECASE)
        if match:
            city = match.group(1)
            return get_weather(city)
        
    return match_intent(user_input)

# Function to handle the chatbot interaction when the user clicks "Send"
def chatbot():
        user_input = user_entry.get()
        user_var.set("")  # Clear the entry field
        if user_input == "":
            # If the user input is empty, prompt them to ask something
            text.config(state=tk.NORMAL)
            text.insert(tk.END, "\nChatty: Please ask something to me")
            text.config(state=tk.DISABLED)
        else:
            # Display the user's input in the chat window
            text.config(state=tk.NORMAL)
            text.insert(tk.END, "\nYou: " + user_input)
            # Generate and display the chatbot's response
            response, should_exit = respond(user_input)
            text.insert(tk.END, "\nChatty: " + response)
            text.config(state=tk.DISABLED)
        
            # Exit the application if the chatbot signals to quit
            if should_exit:
                root.quit()

# Label displaying the chatbot's title
label = tk.Label(root,
                 text="Chatty the ChatBot",
                 anchor=tk.CENTER,
                 bg="wheat",
                 height=2,
                 width=20,
                 bd=3,
                 font=("Times New Roman", 20, "bold", "italic"),
                 cursor="hand2",
                 fg="red",
                 padx=15,
                 pady=15,
                 relief=tk.RAISED
                 )
label.pack(pady=20, anchor=tk.CENTER)

# Text widget to display conversation history
text = tk.Text(root)
text.insert(tk.END, "Chatty: Hi, I'm your chatbot Chatty!")
text.config(state=tk.DISABLED)  # Initially disable text input
text.pack(padx=20, pady=20, anchor=tk.CENTER)

# Entry field for user input
user_var = tk.StringVar()
user_entry = tk.Entry(root, textvariable=user_var, width=70, font=(20))
user_entry.pack(pady=10, padx=10, anchor=tk.CENTER)

# Button to send user input to the chatbot
send_button = tk.Button(root, text="Send", font=(10), bg="lightgreen", command=chatbot)
send_button.pack(pady=10, anchor=tk.CENTER)

# Start the Tkinter main event loop
root.mainloop()
