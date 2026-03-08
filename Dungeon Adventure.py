# Dungeon Adventure

import random

health = 100
gold = 0
inventory = []

def welcome():
    print("WELCOME TO DUNGEON ADVENTURE! 🗡️")
    print("Survive as long as you can..")

def main_menu():
    print('1. Explore')
    print('2. Show inventory')
    print('3. Show stats')
    print('4. Exit')
    print('5. Heal')

def explore():

    event = random.randint(1, 3)
    if event == 3:
        print('You found nothing.')
    elif event == 2:
        fight_enemy()
    elif event == 1:
       find_treasure()

def fight_enemy():
    global health, gold
    print('You have encountered an enemy!')
    print('You fought hard.')
    print('-20 health!')
    print('+100 gold!')
    gold += 100
    health -= 20
    if health <= 0:
        game_over()

def find_treasure():
    global gold
    print('You found treasure!')
    roll = random.randint(1, 10)
    if roll == 10:
        print('You found a Sword!')
        inventory.append('Sword')
    elif roll == 9:
        print('You found a Wine Glass!')
        inventory.append('Wine Glass')
    elif roll == 8:
        print('You found Gold!')
        print('+1000 gold 🤩')
        gold += 1000
    elif roll == 7:
        print('You found some old boots!')
        inventory.append('Old boots')
    elif roll == 6:
        print('You found a Crossbow!')
        inventory.append('Crossbow')
    elif roll == 5:
        print('You found a Spear!')
        inventory.append('Spear')
    elif roll == 4:
        print('You found a HEALING POTION!!')
        inventory.append('Healing potion')
    elif roll == 3:
        print('You found an Iron Chestplate!')
        inventory.append('Iron Chestplate')
    elif roll == 2:
        print('You found an old newspaper!')
        inventory.append('Old newspaper')
    elif roll == 1:
        print('You found some yarn!')
        inventory.append('Yarn')

def show_inventory():

    if inventory:
        for item in inventory:
            print(item)

    else:
        print('Inventory is empty!')

def show_stats():

    print("Health points: " + str(health))
    print("Gold points: " + str(gold))

def heal():
    global health
    if 'Healing potion' in inventory:
        inventory.remove('Healing potion')
        print('You have used a healing potion!')
        print('+100 health.')
        health += 100
    else:
        print('You do not have a healing potion!')

def game_over():

    print('GAME OVER! 🪦')
    print('')
    print('Your final stats:')
    print('')
    print('Health points: ' + str(health))
    print('Gold points: ' + str(gold))
    print('Inventory: ' + str(inventory))

def main():
    welcome()
    while health > 0:
        main_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            explore()
        elif choice == '2':
            show_inventory()
        elif choice == '3':
            show_stats()
        elif choice == '4':
            game_over()
            break
        elif choice == '5':
            heal()
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
