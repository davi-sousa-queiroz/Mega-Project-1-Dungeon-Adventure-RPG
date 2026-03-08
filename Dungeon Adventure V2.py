# Dungeon Adventure v2
import random
# ------- GAME VARIABLES ---------
health = 100
gold = 0
inventory = []
#  -------WELCOME AND MENU SYSTEM-------
def welcome():
    print("WELCOME TO DUNGEON ADVENTURE! 🗡️")
    print("Survive as long as you can..")
def main_menu():
    print('1. Explore 🗺️')
    print('2. Show inventory 🎒')
    print('3. Show stats 📈')
    print('4. Use item 🫴')
    print('5. Drop item 🫳')
    print('6. Rest 😴')
    print('7. Shop 💰')
    print('8. Sell 💸')
    print('9. Exit 💨')
def game_over():
    global health, gold, inventory
    if health <= 0 or gold <= 0:
        print('GAME OVER!')
        print('Final stats:')
        print(health)
        print(gold)
        print('Final inventory:')
        print(inventory)
# -------- EXPLORATION SYSTEM ----------
def explore():
    global health, gold, inventory
    event = random.randint(1,3)
    if event == 1:
        print("You found nothing.")
    elif event == 2:
        fight_enemy()
    elif event == 3:
        find_treasure()
    else:
        print('Exploration bug')
# ------- COMBAT SYSTEM AND ENEMIES -------
def fight_enemy():
    global health, gold
    enemy = random.randint(1,7)
    if enemy == 1:
        slime()
    elif enemy == 2:
        spider()
    elif enemy == 3:
        goblin()
    elif enemy == 4:
        baby_dragon()
    elif enemy == 5:
        soldier()
    elif enemy == 6:
        dragon()
    elif enemy == 7:
        samurai()
def slime():
    global health, gold
    print('You have encountered a slime! 🟢 ')
    print('You fight with all your might.')
    print('Health - 5')
    print('Gold + 20')
    health -= 5
    gold += 20
def spider():
    global health, gold
    print('You have encountered a giant spider! 🕷️')
    print('You fight with all your might.')
    print('Health - 7')
    print('Gold + 30')
    health -= 7
    gold += 30
def goblin():
    global health, gold
    print('You have encountered a goblin 🧌')
    print('You fight with all your might.')
    print('Health - 10')
    print('Gold + 40')
    health -= 10
    gold += 40
def baby_dragon():
    global health, gold
    print('You have encountered a baby dragon! 🐉')
    print('You fight with all your might.')
    print('Health - 15')
    print('Gold + 50')
    health -= 15
    gold += 50
def soldier():
    global health, gold
    print('You have encountered a soldier! 💂‍♀️')
    print('You fight with all your might.')
    print('Health - 20')
    print('Gold + 75')
    health -= 20
    gold += 75
def dragon():
    global health, gold
    print('You have encountered a dragon! 🐉')
    print('You fight with all your might.')
    print('Health - 35')
    print('Gold + 90')
    health -= 35
    gold += 90
def samurai():
    global health, gold
    print('YOU HAVE ENCOUNTERED THE MASTER SAMURAI!! 🤺⚔️😱')
    print('You fight with all your might.')
    print('Health - 50')
    print('Gold + 250')
    health -= 50
    gold += 250
# -------- TREASURE SYSTEM ----------
def find_treasure():
    global gold
    treasure = random.randint(1, 10)
    if treasure == 1:
        bandaid()
    elif treasure == 2:
        bandages()
    elif treasure == 3:
        first_aid_kit()
    elif treasure == 4:
        small_health_potion()
    elif treasure == 5:
        large_health_potion()
    elif treasure == 6:
        toy_car()
    elif treasure == 7:
        wooden_sword()
    elif treasure == 8:
        royal_robes()
    elif treasure == 9:
        chest()
    elif treasure == 10:
        diamond()
def bandaid():
    print('You have found a bandaid! 🩹')
    print('Using will heal for 5 hp.')
    inventory.append('bandaid')
def bandages():
    print('You have found a bandages! ❤️‍🩹')
    print('Using will heal for 10 hp.')
    inventory.append('bandages')
def first_aid_kit():
    print('You have found a first aid kit! ⛑️')
    print('Using will heal for 15 hp.')
    inventory.append('first aid kit')
def small_health_potion():
    print('You have found a small health potion! 🧪')
    print('Using will heal for 20 hp.')
    inventory.append('small health potion')
def large_health_potion():
    print('You have found a LARGE HEALTH POTION!! 🧪😷')
    print('Using will heal for 100 hp.')
    inventory.append('large health potion')
def toy_car():
    print('You have found a small car. 🚗')
    print('It can be sold for 20 gold! 💰')
    inventory.append('small car')
def wooden_sword():
    print('You have found a wooden sword. 🗡️')
    print('It can be sold for 40 gold! 💰')
    inventory.append('wooden sword')
def royal_robes():
    print('You have found some royal robes! 🫅👘')
    print('They can be sold in the shop for 60 gold! 💰')
    inventory.append('royal robes')
def chest():
    print("You have encountered a chest! 🎁 ")
    print('It can be sold in the shop for 100 coins! 💰')
    inventory.append('chest')
def diamond():
    print('You have encountered a DIAMOND!! 💎💍')
    print('It can be sold in the shop for 300 COINS!! 💰')
    inventory.append('diamond')
# ------- INVENTORY AND STATS ----------
def show_inventory():
    if inventory:
        for item in inventory:
            print(item)
    else:
        print('No items in inventory!')
def show_stats():
    print(f'Health : {health}')
    print(f'Gold : {gold}')
def show_only_gold():
    print(gold)
# ----------- ACTIONS -----------
def use_item():
    global health
    show_inventory()
    item = input('Select an item to use: ')
    if item in inventory:
        inventory.remove(item)
        if item == 'bandaid':
            print('Health + 5 ')
            health += 5
        elif item == 'bandages':
            print('Health + 10 ')
            health += 10
        elif item == 'first aid kit':
            print('Health + 15 ')
            health += 15
        elif item == 'small health potion':
            print('Health + 20 ')
            health += 20
        elif item == 'large health potion':
            print('Health + 100 ')
            health += 100
        else:
            print('That item is not usable.')

    else:
        print('That item is not available.')
def sell_item():
    show_inventory()
    global gold
    sellable = input('Select an item to sell: ')
    if sellable in inventory:
        inventory.remove(sellable)
        if sellable == 'toy car':
            print('Gold + 20')
            gold += 20
        elif sellable == 'wooden sword':
            print('Gold + 40')
            gold += 40
        elif sellable == 'royal robes':
            print('Gold + 60')
            gold += 60
        elif sellable == 'chest':
            print('Gold + 100')
            gold += 100
        elif sellable == 'diamond':
            print('Gold + 300')
            gold += 300
        else:
            print('That item is not sellable.')
    else:
        print('That item is not sellable.')
def drop_item():
    show_inventory()
    drop_item = input('Select an item to drop: ')
    if drop_item in inventory:
        inventory.remove(drop_item)
        print(f'You dropped {drop_item}!')
def rest():
    global health
    print('You take a soothing nap.')
    print("Health + 3")
    health += 3
def shop():
    global gold, inventory
    print('ITEMS FOR SALE:')
    for_sale = ['bandaid', 'bandages', 'first aid kit', 'small health potion', 'large health potion', ]
    print(for_sale)
    purchase = input('Select an item to purchase: ')
    if purchase in for_sale:
        if purchase == 'bandaid':
            print(f'{purchase} added to inventory.')
            inventory.append(purchase)
            gold -= 10
        elif purchase == 'bandages':
            print(f'{purchase} added to inventory.')
            inventory.append(purchase)
            gold -= 20
        elif purchase == 'first aid kit':
            print(f'{purchase} added to inventory.')
            inventory.append(purchase)
            gold -= 30
        elif purchase == 'small health potion':
            print(f'{purchase} added to inventory.')
            inventory.append(purchase)
            gold -= 40
        elif purchase == 'large health potion':
            print(f'{purchase} added to inventory.')
            inventory.append(purchase)
            gold -= 300
        else:
            print('That item is not for sale.')
    else:
        print('That item is not for sale.')

# ------------------------------------ DUNGEON ADVENTURE V2 ---------------------------------------

def main():
    global gold, inventory, health
    welcome()
    while health >= 0 and gold >= 0:
        main_menu()
        choice = input('Select an option: ')
        if choice == '1':
            explore()
        elif choice == '2':
            show_inventory()
        elif choice == '3':
            show_stats()
        elif choice == '4':
            use_item()
        elif choice == '5':
            drop_item()
        elif choice == '6':
            rest()
        elif choice == '7':
            shop()
        elif choice == '8':
            sell_item()
        elif choice == '9':
            game_over()
            break
        else:
            print('That option is not available.')
    else:
        game_over()
if __name__ == '__main__':
    main()


