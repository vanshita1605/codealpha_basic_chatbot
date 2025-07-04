import random
import re
from datetime import datetime

class BasicChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.conversation_history = []
        
        # Predefined responses organized by categories
        self.responses = {
            'greetings': {
                'patterns': [
                    r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b',
                    r'\b(what\'s up|whats up|sup)\b'
                ],
                'replies': [
                    "Hi! How can I help you today?",
                    "Hello! Nice to meet you!",
                    "Hey there! What's on your mind?",
                    "Greetings! How are you doing?",
                    "Hi! I'm here to chat with you!"
                ]
            },
            'how_are_you': {
                'patterns': [
                    r'\b(how are you|how do you do|how\'s it going|hows it going)\b',
                    r'\b(are you okay|are you well|how are things)\b'
                ],
                'replies': [
                    "I'm fine, thanks! How about you?",
                    "I'm doing great! Thanks for asking!",
                    "I'm wonderful! How are you today?",
                    "All good here! How can I assist you?",
                    "I'm excellent! What brings you here?"
                ]
            },
            'goodbye': {
                'patterns': [
                    r'\b(bye|goodbye|see you|farewell|take care)\b',
                    r'\b(gotta go|have to go|talk later|catch you later)\b'
                ],
                'replies': [
                    "Goodbye! Have a great day!",
                    "See you later! Take care!",
                    "Bye! It was nice chatting with you!",
                    "Farewell! Come back anytime!",
                    "Take care! Hope to see you again soon!"
                ]
            },
            'name': {
                'patterns': [
                    r'\b(what is your name|what\'s your name|whats your name)\b',
                    r'\b(who are you|tell me about yourself)\b'
                ],
                'replies': [
                    f"I'm {self.name}, your friendly chatbot!",
                    f"My name is {self.name}. I'm here to chat!",
                    f"I'm {self.name}, a simple rule-based chatbot!",
                    f"You can call me {self.name}. Nice to meet you!"
                ]
            },
            'age': {
                'patterns': [
                    r'\b(how old are you|what is your age|whats your age)\b',
                    r'\b(when were you born|your birthday)\b'
                ],
                'replies': [
                    "I'm timeless! I exist in the digital realm.",
                    "Age is just a number for AI like me!",
                    "I was born when this program started running!",
                    "I don't age like humans do. I'm always young at heart!"
                ]
            },
            'help': {
                'patterns': [
                    r'\b(help|assist|support|what can you do)\b',
                    r'\b(commands|options|features)\b'
                ],
                'replies': [
                    "I can chat with you! Try saying hello, asking how I am, or saying goodbye.",
                    "I'm a simple chatbot. I can respond to greetings, questions about myself, and farewells!",
                    "You can talk to me about basic things. I understand greetings, questions, and goodbyes!",
                    "I'm here to have a friendly conversation with you!"
                ]
            },
            'weather': {
                'patterns': [
                    r'\b(weather|temperature|rain|sunny|cloudy)\b',
                    r'\b(hot|cold|warm|cool outside)\b'
                ],
                'replies': [
                    "I wish I could check the weather for you, but I don't have access to weather data!",
                    "I can't see outside, but I hope it's nice weather where you are!",
                    "Weather talk is great! Unfortunately, I can't provide weather updates.",
                    "I'd love to chat about weather, but I don't have real-time weather info!"
                ]
            },
            'time': {
                'patterns': [
                    r'\b(what time|current time|time is it)\b',
                    r'\b(date|today|day)\b'
                ],
                'replies': [
                    f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                    f"Today is {datetime.now().strftime('%A, %B %d, %Y')}",
                    f"Right now it's {datetime.now().strftime('%I:%M %p on %B %d, %Y')}",
                ]
            },
            'compliments': {
                'patterns': [
                    r'\b(you are nice|you\'re nice|youre nice|good job|well done)\b',
                    r'\b(thank you|thanks|appreciate)\b'
                ],
                'replies': [
                    "Thank you! That's very kind of you to say!",
                    "You're welcome! I'm glad I could help!",
                    "Thanks! I appreciate your kind words!",
                    "That means a lot to me! Thank you!",
                    "You're too kind! Happy to chat with you!"
                ]
            },
            'default': {
                'patterns': [],
                'replies': [
                    "I'm not sure I understand. Can you try rephrasing that?",
                    "That's interesting! Tell me more.",
                    "I'm still learning. Could you ask me something else?",
                    "Hmm, I don't have a good response for that. What else would you like to talk about?",
                    "I'm a simple chatbot, so I might not understand everything. Try asking me about myself!",
                    "Can you try asking me something different? I'm better with greetings and simple questions!"
                ]
            }
        }
    
    def clean_input(self, user_input):
        """Clean and normalize user input"""
        # Convert to lowercase and strip whitespace
        cleaned = user_input.lower().strip()
        # Remove extra spaces
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned
    
    def find_response_category(self, user_input):
        """Find the appropriate response category based on user input"""
        cleaned_input = self.clean_input(user_input)
        
        # Check each category except 'default'
        for category, data in self.responses.items():
            if category == 'default':
                continue
            
            for pattern in data['patterns']:
                if re.search(pattern, cleaned_input, re.IGNORECASE):
                    return category
        
        return 'default'
    
    def get_response(self, user_input):
        """Generate a response based on user input"""
        category = self.find_response_category(user_input)
        replies = self.responses[category]['replies']
        
        # Select a random reply from the category
        response = random.choice(replies)
        
        # Store conversation in history
        self.conversation_history.append({
            'user': user_input,
            'bot': response,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
        
        return response
    
    def display_conversation_history(self):
        """Display the conversation history"""
        if not self.conversation_history:
            print("No conversation history yet!")
            return
        
        print("\n=== CONVERSATION HISTORY ===")
        for i, exchange in enumerate(self.conversation_history, 1):
            print(f"{i}. [{exchange['timestamp']}]")
            print(f"   You: {exchange['user']}")
            print(f"   Bot: {exchange['bot']}")
            print()
    
    def display_help(self):
        """Display help information about the chatbot"""
        print("\n=== CHATBOT HELP ===")
        print("I'm a simple rule-based chatbot. Here's what I can understand:")
        print("• Greetings: hello, hi, hey, good morning")
        print("• How are you: how are you, how's it going")
        print("• About me: what's your name, how old are you")
        print("• Time/Date: what time is it, what's the date")
        print("• Weather: weather, temperature (limited responses)")
        print("• Compliments: thank you, good job, you're nice")
        print("• Goodbye: bye, goodbye, see you later")
        print("• Help: help, what can you do")
        print("\nSpecial commands:")
        print("• 'history' - View conversation history")
        print("• 'clear' - Clear conversation history")
        print("• 'quit' or 'exit' - End the conversation")
        print()
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history.clear()
        print("Conversation history cleared!")
    
    def chat(self):
        """Main chat loop"""
        print(f"Hello! I'm {self.name}, your friendly chatbot!")
        print("Type 'help' for commands, or just start chatting!")
        print("Type 'quit' or 'exit' to end our conversation.")
        print("-" * 50)
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Check for empty input
                if not user_input:
                    print("Please say something!")
                    continue
                
                # Check for special commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print(f"\n{self.name}: {random.choice(self.responses['goodbye']['replies'])}")
                    break
                
                elif user_input.lower() == 'help':
                    self.display_help()
                    continue
                
                elif user_input.lower() == 'history':
                    self.display_conversation_history()
                    continue
                
                elif user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                
                # Generate and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Let's continue our conversation!")

def main():
    """Main function to start the chatbot"""
    try:
        chatbot = BasicChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"Failed to start chatbot: {e}")

if __name__ == "__main__":
    main()
