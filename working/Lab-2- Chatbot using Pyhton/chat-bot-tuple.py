# A simple chatbot for famous landmarks using Tuples

# Tuple storing famous landmarks and their locations
landmarks = (
    ("Eiffel Tower", "Paris, France"),
    ("Great Wall of China", "China"),
    ("Pyramids of Giza", "Giza, Egypt"),
    ("Statue of Liberty", "New York, USA"),
    ("Taj Mahal", "Agra, India"),
    ("Sydney Opera House", "Sydney, Australia"),
    ("Machu Picchu", "Peru"),
    ("Christ the Redeemer", "Rio de Janeiro, Brazil"),
    ("Colosseum", "Rome, Italy"),
    ("Mount Fuji", "Japan")
)

# Function to start the chatbot
def chatbot():
    print("Hello! I'm your landmark chatbot. Ask me about famous landmarks.")
    
    while True:
        user_input = input("\nYou: ").strip().lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        found = False
        for landmark, location in landmarks:
            if user_input in landmark.lower():
                print(f"Chatbot: {landmark} is located in {location}.")
                found = True
                break
        
        if not found:
            print("Chatbot: Sorry, I don't know that landmark. Try asking about another landmark or type 'exit' to quit.")

# Start the chatbot
chatbot()
