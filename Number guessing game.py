import random

def start_game():
    print("=" * 40)
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯")
    print("=" * 40)
    print("Computer has chosen a number between 1 and 100.")
    print("Can you guess it? Let's find out!\n")

    # Computer selects a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Taking input from the user
            user_guess = input("Enter your guess (or type 'exit' to quit): ")
            
            # Check if user wants to exit
            if user_guess.lower() == 'exit':
                print(f"👋 Goodbye! The correct number was {secret_number}.")
                break
            
            # Converting input to integer
            user_guess = int(user_guess)
            attempts += 1

            # Validating the range
            if user_guess < 1 or user_guess > 100:
                print("⚠️ Invalid Range! Please guess a number between 1 and 100.")
                continue

            # Core game logic
            if user_guess == secret_number:
                print(f"\n🎉 CONGRATULATIONS! You guessed it right in {attempts} attempts! 🏆")
                break
            elif user_guess < secret_number:
                print("📉 Too Low! Try a higher number.")
            else:
                print("📈 Too High! Try a lower number.")
                
        except ValueError:
            # Handling error if user inputs text instead of a number
            print("❌ Invalid Input! Please enter a valid whole number or 'exit'.")

if __name__ == "__main__":
    start_game()