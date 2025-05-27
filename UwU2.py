def create_monsters():
    print("Welcome to the Monster Creator!")

    try:
        count = int(input("How many monsters do you want to create? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    monsters = []

    for i in range(count):
        print(f"\nCreating monster #{i + 1}")
        name = input("What's the monster's name? ")
        try:
            hp = int(input("How much HP does it have? "))
            atk = int(input("How much ATK does it have? "))
        except ValueError:
            print("HP and ATK must be numbers. Skipping this monster ;-;.")
            continue

        monster = {
            "name": name,
            "hp": hp,
            "atk": atk
        }

        monsters.append(monster)

    print("\nGenerating your monsters...\n")
    
    if monsters:
        print("You've created the following monsters:")
        for i, m in enumerate(monsters):
            print(f"{i + 1}. {m['name']} with {m['hp']} HP and {m['atk']} ATK")
    else:
        print("No monsters were created.")

create_monsters()