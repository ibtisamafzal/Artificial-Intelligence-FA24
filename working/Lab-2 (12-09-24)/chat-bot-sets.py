

# A simple chatbot for laptop companies using Sets

# Set storing the names of laptop companies
laptop_companies = {
    "dell", 
    "hp", 
    "lenovo", 
    "apple", 
    "asus", 
    "acer", 
    "microsoft", 
    "razer", 
    "msi", 
    "samsung"
}

# Function to start the chatbot
def chatbot():
    print("Hello! I'm your laptop companies chatbot. Ask me about laptop brands.")
    
    while True:
        user_input = input("\nYou: ").strip().lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Check if the user input is in the set of laptop companies
        if user_input in laptop_companies:
            print(f"Chatbot: Yes, {user_input.capitalize()} is a well-known laptop company.")
        else:
            print("Chatbot: Sorry, I'm not familiar with that brand. Try asking about another company or type 'exit' to quit.")

# Start the chatbot
chatbot()
