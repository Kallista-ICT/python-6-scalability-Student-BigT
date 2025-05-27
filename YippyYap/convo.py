
import greetings

def choose_greeting():
    name = input("What's your name? ")

    print("\nChoose a greeting type:")
    print("1. Hello")
    print("2. Good Morning")
    print("3. Good Afternoon")
    print("4. Good Evening")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        greetings.hello(name)
    elif choice == "2":
        greetings.good_morning(name)
    elif choice == "3":
        greetings.good_afternoon(name)
    elif choice == "4":
        greetings.good_evening(name)
    else:
        print("Invalid choice. Please select 1-4.")

def main():
    print("Welcome to the Conversation Program!")
    choose_greeting()

if __name__ == "__main__":
    main()