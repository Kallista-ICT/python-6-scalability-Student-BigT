def create_monster(name,hp,attack):
    print(f"Congrats, You've made {name} with {hp} hp and {attack} atk")

ab = input("For Monster A, What kind of monster is it? ")
bc = int(input("For Monster A, How much health points does it have? "))
cd = int(input("For Monster A, How much attack does it have? "))


de = input("For Monster B, What kind of monster is it? ")
ef = int(input("For Monster B, How much health points does it have? "))
gh = int(input("For Monster B, How much attack does it have? "))

def main():
    create_monster(ab,bc,cd)
    create_monster(de,ef,gh)

if __name__ == "__main__":
    main()



          
