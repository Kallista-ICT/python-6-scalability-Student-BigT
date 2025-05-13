def greet(name):
    print(f"Welcome {name}, Are you ready?")

player1 = input("Whats the first player name: ")
player2 = input("Whats the second player name: ")

def main():
    greet(player1)
    greet(player2)

if __name__ == "__main__":
    main()