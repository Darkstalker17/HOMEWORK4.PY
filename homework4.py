# Extended Chatbot Project

def chatbot():
    print("Hello! I'm your friendly chatbot 🤖")
    
    while True:
        # Ask how the user feels
        emotion = input("How are you feeling today? (happy/sad/angry/other): ").lower()
        
        if emotion == "happy":
            print("Yay! I'm glad you're feeling happy 😄")
        elif emotion == "sad":
            print("Oh no! I hope things get better soon. 😢")
        elif emotion == "angry":
            print("Take a deep breath. Anger can be tough to deal with 😤")
        else:
            print("Thanks for sharing! I hope your day goes well 😊")
        
        # Choose a conversation topic
        print("\nLet's talk about something!")
        print("1. Hobbies")
        print("2. School")
        print("3. Games")
        print("4. Movies")
        
        topic = input("Pick a topic (1-4): ")
        
        if topic == "1":
            hobby = input("What's your favorite hobby? ")
            print(f"Wow! {hobby} sounds super fun!")
        elif topic == "2":
            subject = input("Which subject do you like the most at school? ")
            print(f"{subject} is really interesting! Keep up the great work!")
        elif topic == "3":
            game = input("What's your favorite game? ")
            print(f"{game} is awesome! I wish I could play it too 🎮")
        elif topic == "4":
            movie = input("What's your favorite movie? ")
            print(f"{movie} is a classic! I'll add it to my watchlist 🍿")
        else:
            print("Hmm, I don't know about that topic, but we can chat about something else!")
        
        # Option to continue or end the chat
        repeat = input("\nDo you want to continue chatting? (yes/no): ").lower()
        if repeat != "yes":
            print("It was nice talking to you! Bye 👋")
            break
        print("\n--- Let's chat again! ---\n")

# Run the chatbot
chatbot()
