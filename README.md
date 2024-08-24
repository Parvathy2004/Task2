# Task2
Building a Chatbot Using Python
## Documentation: Chatty the ChatBot

### Overview
This is a simple chatbot application built using Python's Tkinter library for the graphical user interface (GUI). The chatbot, named "Chatty," interacts with users based on predefined intents stored in a JSON file. It also has the capability to fetch current weather information for a specified city using the OpenWeatherMap API.

### Key Components

1. **Intents and Pattern Matching**:
   - **Intents JSON File**: The chatbot's responses are based on patterns defined in a JSON file (`intents.json`). Each intent contains patterns (user input examples) and corresponding responses.
   - **match_intent Function**: This function takes user input, searches for matching patterns in the intents, and returns an appropriate response. It handles special cases like extracting and using a user’s name (`user_name` intent) and exiting the chat on a goodbye intent (`goodbye`).

2. **Weather Functionality**:
   - **get_weather Function**: If the user asks about the weather in a specific city, this function is called. It sends a request to the OpenWeatherMap API and returns the current temperature in Celsius. Error handling is included for cases like invalid city names or API request failures.

3. **Responding to User Input**:
   - **respond Function**: This function decides whether to call `get_weather` or `match_intent` based on the user’s input. It returns the chatbot’s response and whether the application should exit.

4. **Graphical User Interface (GUI)**:
   - **Main Window**: The application window is created using Tkinter, with a title "Chatty The ChatBot".
   - **Label**: Displays the chatbot's name ("Chatty the ChatBot") in a stylized manner.
   - **Text Widget**: Used to display the conversation between the user and Chatty. It starts with an initial greeting and is updated as the conversation progresses.
   - **Entry Widget**: Where the user types their input. The input is passed to the chatbot for processing when the user presses the "Send" button.
   - **Button Widget**: The "Send" button triggers the chatbot to process the user's input and display the response.

5. **User Interaction Flow**:
   - The user enters text into the entry field.
   - Upon clicking the "Send" button, the chatbot processes the input.
   - The conversation is displayed in the text widget, with both user input and Chatty's responses.

### Design Choices

- **Tkinter for GUI**: Tkinter was chosen for its simplicity and ease of use in creating basic GUI applications in Python.
- **Pattern Matching with Regular Expressions**: Regular expressions (`re` module) are used to match user input against patterns in the intents file, providing flexibility in recognizing various ways users might phrase their queries.
- **Weather API Integration**: The integration of the OpenWeatherMap API adds dynamic functionality to the chatbot, allowing it to provide real-time information rather than relying solely on predefined responses.

### Challenges Faced

- **Pattern Matching Accuracy**: Ensuring that the chatbot accurately identifies and matches user input to the correct intent was crucial. Regular expressions were used to handle variations in user input.
- **API Error Handling**: Handling different types of errors from the weather API, such as incorrect city names or network issues, was necessary to maintain a smooth user experience.

### Conclusion

This chatbot application is a basic implementation of a conversational agent with simple intent recognition and weather querying capabilities. It serves as a foundation for more complex chatbot projects, where additional features, intents, and external data sources can be incorporated.



### Chatbot Questions Documentation

The chatbot "Chatty" is designed to recognize and respond to the following user questions or statements:

#### 1. **Greeting Questions**
- "hi"
- "hello"
- "hey"
- "greetings"

#### 2. **Casual Conversation Questions**
- "how are you"
- "how do you feel"
- "are you ok"

#### 3. **Goodbye Questions**
- "bye"
- "see you later"
- "goodbye"

#### 4. **Name Inquiry Questions**
- "what is your name?"
- "who are you?"

#### 5. **Thank You Questions**
- "thanks"
- "thank you"
- "thanku"

#### 6. **Weather Inquiry Questions**
- "what is the weather in (city name)"
- "weather in (city name)"

#### 7. **User Name Identification Questions**
- "my name is (your name)"
- "i am (your name)"
- "everyone calls me (your name)"
