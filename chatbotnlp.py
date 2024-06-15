import tkinter as tk
from tkinter import scrolledtext
import random

# Define a large set of intents and responses
intents = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Greetings! How can I be of service?"],
    "well_being_animals": ["All animals deserve care and love. How can I help with your questions about animals?", 
                           "Animals are wonderful creatures. What would you like to know about them?", 
                           "I'm happy to talk about animals. What's your question?"],
    "gadgets": ["Gadgets are amazing, aren't they? Do you have any specific gadget in mind?", 
                "Technology is fascinating. Let's talk about gadgets! What interests you?", 
                "I can provide information on various gadgets. What would you like to know?"],
    "science": ["Science is the key to understanding our world. What aspect of science are you curious about?", 
                "From physics to biology, science explains so much. What would you like to discuss?", 
                "Science is a vast field. What specific topic are you interested in?"],
    "computers": ["Computers are essential in today's world. What do you want to know about computers?", 
                  "From hardware to software, computers are fascinating. What's your question about them?", 
                  "I can help you with information about computers. What would you like to know?"],
    "weather": ["The weather is a common topic. How can I assist with your weather-related query?", 
                "Weather can be unpredictable. Do you have a specific question about the weather?", 
                "I can provide information on weather. What would you like to know?"],
    "health": ["Health is important. What aspect of health are you concerned about?", 
               "I can offer advice on various health topics. What do you need help with?", 
               "Let's talk about health. What specific topic are you interested in?"],
    "fitness": ["Fitness is crucial for a healthy life. What would you like to know about fitness?", 
                "I can provide tips and advice on fitness. What are you looking to improve?", 
                "Fitness questions are welcome. How can I help you stay fit?"],
    "nutrition": ["Nutrition is key to good health. Do you have a specific nutrition question?", 
                  "I can help with information on nutrition. What would you like to know?", 
                  "Let's talk about nutrition. What specific aspect are you interested in?"],
    "cooking": ["Cooking is a great skill. What would you like to cook or learn about?", 
                "I can provide recipes and cooking tips. What are you planning to cook?", 
                "Let's discuss cooking. Do you need a recipe or cooking advice?"],
    "movies": ["Movies are a great form of entertainment. Do you have a specific movie in mind?", 
               "I can suggest movies or provide information about them. What are you interested in?", 
               "Let's talk about movies. What genre or movie are you interested in?"],
    "music": ["Music can be very relaxing. What kind of music do you like?", 
              "I can recommend songs or artists. What are you in the mood for?", 
              "Let's discuss music. Do you have a favorite genre or artist?"],
    "books": ["Books are a great way to gain knowledge. What book or genre do you like?", 
              "I can suggest books or discuss them with you. What are you reading?", 
              "Let's talk about books. Do you need a recommendation or have a question about a book?"],
    "travel": ["Traveling can be exciting. Do you have a destination in mind?", 
               "I can provide travel tips or information. Where are you planning to go?", 
               "Let's discuss travel. What information or advice do you need?"],
    "sports": ["Sports are a great way to stay active. What sport are you interested in?", 
               "I can provide information on various sports. What would you like to discuss?", 
               "Let's talk about sports. Do you have a favorite sport or team?"],
    "technology": ["Technology is constantly evolving. What tech topic are you interested in?", 
                   "I can help with various technology-related queries. What do you need to know?", 
                   "Let's discuss technology. Do you have a specific question or topic in mind?"],
    "history": ["History is full of fascinating stories. What historical event or period interests you?", 
                "I can provide information on history. What would you like to learn about?", 
                "Let's talk about history. Do you have a specific question or topic in mind?"],
    "news": ["Keeping up with news is important. Do you have a specific news topic you're interested in?", 
             "I can discuss recent news or provide information. What news are you following?", 
             "Let's talk about the news. What would you like to discuss or know more about?"],
    "relationships": ["Relationships are complex. Do you have a specific question or concern?", 
                      "I can offer advice on relationships. What would you like to discuss?", 
                      "Let's talk about relationships. How can I assist you?"],
    "finance": ["Finance is crucial for stability. Do you have a specific financial question?", 
                "I can provide information on finance. What would you like to know?", 
                "Let's discuss finance. What aspect are you interested in?"],
    "education": ["Education is important for growth. Do you have a specific educational query?", 
                  "I can help with various educational topics. What do you need assistance with?", 
                  "Let's talk about education. What would you like to learn or know more about?"],
    "career": ["Career development is vital. Do you have a specific career-related question?", 
               "I can offer advice on careers. What are you looking to achieve?", 
               "Let's discuss your career. How can I help you progress?"],
    "default": ["I'm not sure how to respond to that. Can you please ask something else?", 
                "I'm here to help with your queries. Can you please rephrase your question?", 
                "I'm not sure I understand. Could you ask your question in a different way?"]
}

# Function to get chatbot response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return random.choice(intents["greeting"])
    elif "animal" in user_input or "pet" in user_input:
        return random.choice(intents["well_being_animals"])
    elif "gadget" in user_input or "device" in user_input:
        return random.choice(intents["gadgets"])
    elif "science" in user_input or "physics" in user_input or "biology" in user_input:
        return random.choice(intents["science"])
    elif "computer" in user_input or "laptop" in user_input or "pc" in user_input:
        return random.choice(intents["computers"])
    elif "weather" in user_input:
        return random.choice(intents["weather"])
    elif "health" in user_input:
        return random.choice(intents["health"])
    elif "fitness" in user_input:
        return random.choice(intents["fitness"])
    elif "nutrition" in user_input:
        return random.choice(intents["nutrition"])
    elif "cooking" in user_input:
        return random.choice(intents["cooking"])
    elif "movie" in user_input or "film" in user_input:
        return random.choice(intents["movies"])
    elif "music" in user_input or "song" in user_input:
        return random.choice(intents["music"])
    elif "book" in user_input or "novel" in user_input:
        return random.choice(intents["books"])
    elif "travel" in user_input or "trip" in user_input:
        return random.choice(intents["travel"])
    elif "sport" in user_input or "game" in user_input:
        return random.choice(intents["sports"])
    elif "technology" in user_input or "tech" in user_input:
        return random.choice(intents["technology"])
    elif "history" in user_input or "historic" in user_input:
        return random.choice(intents["history"])
    elif "news" in user_input or "headline" in user_input:
        return random.choice(intents["news"])
    elif "relationship" in user_input or "love" in user_input or "friend" in user_input:
        return random.choice(intents["relationships"])
    elif "finance" in user_input or "money" in user_input:
        return random.choice(intents["finance"])
    elif "education" in user_input or "school" in user_input or "college" in user_input:
        return random.choice(intents["education"])
    elif "career" in user_input or "job" in user_input or "work" in user_input:
        return random.choice(intents["career"])
    else:
        return random.choice(intents["default"])

# Function to handle sending messages
def send_message(event=None):
    user_input = entry_box.get("1.0", tk.END).strip()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        entry_box.delete("1.0", tk.END)
        
        response = get_response(user_input)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n")
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)
    return "break"  # Prevent default behavior of the Enter key

# Create the main window
window = tk.Tk()
window.title("Chatbot")
window.geometry("500x600")

# Create the chat window
chat_log = scrolledtext.ScrolledText(window, state='disabled', wrap='word', bg="white", width=60, height=25, font=("Arial", 12))
chat_log.config(state=tk.DISABLED)

# Create the entry box for typing messages
entry_box = tk.Text(window, bd=0, bg="white", width=45, height=2, font=("Arial", 12), wrap='word')
entry_box.bind("<Return>", send_message)

# Create the send button
send_button = tk.Button(window, font=("Arial", 12, 'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                        command=send_message)

# Place all the components on the window
chat_log.place(x=6, y=6, height=486, width=488)
entry_box.place(x=6, y=501, height=90, width=360)
send_button.place(x=376, y=501, height=90, width=105)

# Run the Tkinter event loop
window.mainloop()
