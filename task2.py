import json
import random
import re
import requests
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Chatty The ChatBot")

# Load intents from JSON file
with open('intents.json') as file:
    data = json.load(file)

def match_intent(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if re.search(pattern.lower(), user_input.lower()):
                if intent['tag'] == 'user_name':
                    match = re.search(pattern.lower(), user_input.lower())
                    name = match.group(1)
                    return random.choice(intent['responses']).replace('%1',name),False
                elif intent['tag'] == 'goodbye':
                    return random.choice(intent['responses']),True
                else:
                    return random.choice(intent['responses']), False
    return "I didn't understand that. Can you please rephrase?", False

def get_weather(city):
    api_key = "cf8e2f1742739dda0553b46f4056fdb2"  # Replace with your actual API key from OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:  # Successful response
        if "main" in data:
            temperature = data["main"]["temp"] - 273.15  # Convert temperature to Celsius
            return f"The temperature in {city} is {temperature:.2f}°C", False
        else:
            return "Temperature data not available.", False
    elif data["cod"] == "404":
        return f"Error: City '{city}' not found.", False
    else:
        return f"Error: {data['message']}" if 'message' in data else "Unknown error.", False



def respond(user_input):
    if "weather in" in user_input.lower():
        match = re.search(r"weather in (.*)", user_input, re.IGNORECASE)
        if match:
            city = match.group(1)
            return get_weather(city)
        
    return match_intent(user_input)

def chatbot():
        user_input = user_entry.get()
        user_var.set("")
        if user_input == "":
            text.config(state = tk.NORMAL)
            text.insert(tk.END , "\nChatty: Please ask something to me")
            text.config(state = tk.DISABLED)
        else:
            text.config(state=tk.NORMAL)
            text.insert(tk.END, "\nYou: " + user_input)
            response, should_exit = respond(user_input)
            text.insert(tk.END, "\nChatty: " + response)
            text.config(state=tk.DISABLED)
        
            if should_exit:
                root.quit()
        


label = tk.Label(root,
                 text = "Chatty the ChatBot",
                 anchor=tk.CENTER,
                 bg="wheat",
                 height=2,
                 width=20,
                 bd=3,
                 font=("Times New Roman", 20, "bold", "italic"),
                 cursor = "hand2",
                 fg = "red",
                 padx = 15,
                 pady = 15,
                 relief = tk.RAISED
                 )
label.pack(pady = 20, anchor=tk.CENTER)

text = tk.Text(root)
text.insert(tk.END, "Chatty: Hi, I'm your chatbot Chatty!")
text.config(state = tk.DISABLED)
text.pack(padx=20,pady=20, anchor=tk.CENTER)


user_var = tk.StringVar()
user_entry = tk.Entry(root, textvariable = user_var, width=70, font=(20))
user_entry.pack(pady=10,padx=10, anchor=tk.CENTER)

send_button = tk.Button(root, text="Send", font=(10), bg="lightgreen", command= chatbot)
send_button.pack(pady=10, anchor=tk.CENTER)


root.mainloop()
