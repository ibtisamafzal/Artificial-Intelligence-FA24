#create chat-bot using dictionary, tuple, sets
#read-file
#write-file
#history.com
#forensic-focus-youtube
#Google-Deep-mind
#hugging-face-daily-pages


# A simple chatbot for computer terminologies

terminologies = {
    "CPU": "Central Processing Unit, the brain of the computer where most calculations take place.",
    "RAM": "Random Access Memory, a form of computer memory that stores data temporarily.",
    "HDD": "Hard Disk Drive, a data storage device that uses magnetic storage to store and retrieve digital information.",
    "SSD": "Solid State Drive, a data storage device that uses integrated circuits to store data.",
    "Motherboard": "The main printed circuit board in a computer that connects all components together.",
    "GPU": "Graphics Processing Unit, a specialized processor designed to accelerate graphics rendering.",
    "Operating System": "System software that manages computer hardware and software resources.",
    "Python": "A high-level, interpreted programming language known for its ease of learning and readability.",
    "Algorithm": "A set of instructions designed to perform a specific task or solve a problem.",
    "Binary": "The basic language of computers, consisting of only 0s and 1s."
}

# Function to start the chatbot
def chatbot():
    print("Hello! I'm your computer terminologies chatbot. Ask me about computer terms.")
    
    while True:
        user_input = input("\n Enter Term: ").strip().lower()
        
        found = False
        for term, definition in terminologies.items():
            if user_input in term.lower():
                print(f"{term} - {definition}")
                found = True
                break
        
        if not found:
            print("Chatbot: Sorry, I don't know that term. Try asking about another computer term or type 'exit' to quit.")

# Start the chatbot
chatbot()