import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")
        
    x = random.randrange(1,10)
    guess = None
        
    while x != guess:
            
        guess = int(input("Pick a number between 1 to 10: "))
            
        if x == guess:
            print("you genius!")
        elif x > guess:
            print("Try a bigger number.")
        elif x < guess:
            print("Try a smaller number.")

main()