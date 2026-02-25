import os
import random

def GameOver():
    print("Вам не удалось призывать покровителя, Чтобы воплатить свои мечты.")

# === Очистка консоли
def clear():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

# === Выбор предмета из всего инвентаря
def Choise(Player_Inventory):
    for i, item in enumerate(Player_Inventory):
        print(i, "-", item)

    try:
        Move = int(input("Выберите номер: "))
    except ValueError:
        Move = "Error"

    if Move == "Error" or Move < 0 or Move >= len(Player_Inventory):
        print("Ошибка системы, использован первый предмет")
        Move = 0
    return Move

# === Выбор активного предмета (Active)
def ActiveChoise(Player_Inventory):
    Active_Player_Inventory = []
    for i, name in enumerate(Player_Inventory):
        if Item(name, 0) == "Active":
            Active_Player_Inventory.append(name)

    for i, item in enumerate(Active_Player_Inventory):
        print(i, "-", item)

    try:
        Move = int(input("Выберите номер: "))
    except ValueError:
        Move = "Error"

    if Move == "Error" or Move < 0 or Move >= len(Active_Player_Inventory):
        print("Ошибка системы, использован первый активный предмет")
        Move = 0

    # Возвращаем индекс в оригинальном инвентаре
    for i, name in enumerate(Player_Inventory):
        if name == Active_Player_Inventory[Move]:
            return i
    return 0

# === Функция предметов
def Item(Name, fight):

    global Damage, Shield, Mana, Mana_max, Heal
    g = 12

    match Name:
        case "Железный меч":
            if fight == 1:
                print("Использован Железный меч, нанесено 5 урона")
                Damage += 5
            else:
                return "Active"

        case "Тяжёлый рывок":
            if fight == 1:
                print("Совершен тяжёлый рывок")
                Heal += -5
                Shield += 5
                Damage += 5

        case "Инферно-жезл":
            if fight == 1:
                print("Использован Инферно-жезл, нанесено", g, "урона")
                Damage += 4
                g += 4
            else:
                return "Active"

        case "Деревянный меч":
            if fight == 1:
                print("Использован Деревянный меч, нанесено 3 урона")
                Damage += 3
            else:
                return "Active"

        case "Огонёк":
            if fight == 1:
                print("Свечка зажигает свой оберегающий огонь, нанесено 2 урона себе, добавлено 5 брони")
                Shield += 3
                Heal -= 2
            else:
                return "Passive"

        case "Деревянный щит":
            if fight == 1:
                print("Использован Деревянный щит, добавлено 5 брони")
                Shield += 5
            else:
                return "Active"
        case "Магическая броня":
            if fight == 1:
                if Mana >= 2:
                    Mana -= 2
                    Shield += 2
                    print("магическая броня активна")
                else:
                    print("Недостаточно силы для магической брони")
            else:
                return "Passive"

# === Персонажи
Player = {
    "hp": 100,
    "hp_max": 100,
    "mp": 100,
    "mp_max": 100,
    "sp": 0,
    "inventory": ["Железный меч", "Деревянный щит",]
}

Candle = {
    "name": "свечка стража",
    "hp": 20,
    "hp_max": 25,
    "sp": 0,
    "inventory": ["Огонёк", "Деревянный меч"]
}

Guard = {
    "name": "страж",
    "hp": 35,
    "hp_max": 25,
    "sp": 0,
    "inventory": ["Тяжёлый рывок", "Инферно-жезл"]
}

Heart = {
"name": "Сердце огня",
    "hp": 35,
    "hp_max": 25,
    "sp": 0,
    "inventory": ["Огонёк", "Инферно-жезл", "Магическая броня"]
}

# === Механика боя
def battle(Enemy):
    print("\n=== Начало боя с", Enemy["name"])

    global Damage, Shield, Mana, Mana_max, Heal

    while Player["hp"] > 0 and Enemy["hp"] > 0:
        Damage = 0
        Shield = 0
        Heal = 0
        Player["sp"] //= 2
        Mana = Player["mp"]
        Mana_max = Player["mp_max"]

        input()
        clear()

        # --- Ход игрока ---
        print("\n* Ваш ход")
        print(f"Вы [\033[31m{Player['hp']}/{Player['hp_max']}♥\033[0m "
              f"\033[35m{Mana}/{Mana_max}★\033[0m "
              f"\033[32m{Player['sp']}⛨\033[0m]")
        print(f"{Enemy['name']} [\033[31m{Enemy['hp']}/{Enemy['hp_max']}♥\033[0m "
              f"\033[32m{Enemy['sp']}⛨\033[0m]")
        print(" ")

        # Активируем пассивные предметы игрока
        for name in Player["inventory"]:
            if Item(name, 0) == "Passive":
                Item(name, 1)

        print("Выберите активный предмет для атаки/защиты:")
        active_index = ActiveChoise(Player["inventory"])
        Item(Player["inventory"][active_index], 1)

        # Лечение себя
        Player["hp"] += Heal
        Heal = 0

        # Нанесение урона врагу
        if Enemy["sp"] >= Damage:
            Enemy["sp"] -= Damage
        else:
            Damage -= Enemy["sp"]
            Enemy["sp"] = 0
            Enemy["hp"] -= Damage
        Damage = 0

        # Добавление брони игроку
        Player["sp"] += Shield
        Shield = 0

        if Enemy["hp"] <= 0:
            print("Вы победили!")
            Player["mp"] = Mana
            Player["hp_max"] = Mana_max
            return True

        input()
        clear()

        # --- Ход врага ---
        Player["mp"] = Mana
        Player["hp_max"] = Mana_max
        Mana = 999999
        Mana_max = 999999
        Enemy["sp"] //= 2
        Damage = 0
        Shield = 0
        print("\n* Ход противника")
        print(f"Вы [\033[31m{Player['hp']}/{Player['hp_max']}♥\033[0m "
              f"\033[35m{Player['mp']}/{Player['mp_max']}★\033[0m "
              f"\033[32m{Player['sp']}⛨\033[0m]")
        print(f"{Enemy['name']} [\033[31m{Enemy['hp']}/{Enemy['hp_max']}♥\033[0m "
              f"\033[32m{Enemy['sp']}⛨\033[0m]")

        # пассивные предметы врага
        for name in Enemy["inventory"]:
            if Item(name, 0) == "Passive":
                Item(name, 1)

        # Враг случайно выбирает активный предмет
        Active_Enemy_Inventory = [name for name in Enemy["inventory"] if Item(name, 0) == "Active"]
        if Active_Enemy_Inventory:
            chosen_item = random.choice(Active_Enemy_Inventory)
            Item(chosen_item, 1)

        # Лечение противника
        Enemy["hp"] += Heal
        Heal = 0

        # Нанесение урона игроку
        if Player["sp"] >= Damage:
            Player["sp"] -= Damage
        else:
            Damage -= Player["sp"]
            Player["sp"] = 0
            Player["hp"] -= Damage
        Damage = 0

        # Добавление брони врагу
        Enemy["sp"] += Shield
        Shield = 0

        if Player["hp"] <= 0:
            print("Вы проиграли...")
            return False

# === Игра
def Game():
    print()
    print("Вы авантюрист, ваша задача призвать покровителя для заполучения вечного богатства и бессмертия")
    print("Вам нужно открыть врата древнего храма для освобождения покровителя")
    print(f"У вас есть \033[31mздоровье ♥\033[0m, если оно упадёт до нуля - вы проиграете")
    print(f"Вы обладаете \033[35mспиритической силой ★\033[0m, ваш основный способ борьбы с противниками покровителя") # времени не осталось, чтобы реализовать механику :(
    print(f"Вы можете создавать \033[32mзащиту ⛨\033[0m, чтобы избежать потерели \033[31mздоровья ♥\033[0m")

    input()
    clear()

    print("Вы идёте в лес и наблюдаете странный огонёк")
    a = input("Потушите ли вы огонь, чтобы избежать лесного пожара? (ответ y/n):")
    match a:
        case "y":
            print("Вы попытались потушить огонь, но оно обратило взор на вас!")
            if (battle(Candle) == False):
                GameOver()
                return
        case "n":
            print("Вы не обращая внимание на огонь пошли дальше, но вот огонь обратил на вас внимание.")
            if (battle(Candle) == False):
                GameOver()
                return
        case _:
            print("Вы падайте прямо на этот огонь, получая 10 урона")
            Player["hp"] -= 10
            if Player["hp"] <= 0:
                print("Этого было достаточно, чтобы так глупо потерпеть поражение")
                GameOver()
            if (battle(Candle) == False):
                GameOver()
                return
    print("Перед вами 2 пути, один введет к загадочному алтарю, другой к реке.")
    a = input("Какой вы путь выберете? (Ответ 1/2):")
    match a:
        case "1":
            print("Вы наткнулись на алтарь древнего стража, что держит врата храма закрытыми")
            b = input("Вы возмёте странный красный огонёк на алтаре? (Ответ y/n):")
            match b:
                case "y":
                    print("Вы получили странный огонёк")
                    Player["inventory"].append("Огонёк")
                case _:
                    print("Вы обошли алтарь строной")
        case "2":
            print("Вы отдохнули у реки и восстановили свои силы")
            Player["hp_max"] += 20
            Player["hp"] = Player["hp_max"]
        case _:
            print("Вы решаетесь продолжить прямой путь к храму")
    print("Вы подходите к вратам и вы видите стража")
    a = input("Попытаетесь его обойти? (Ответ y/n):")
    match a:
        case "n":
            print("Вы пошли напролом стражу.")
            if (battle(Guard) == False):
                GameOver()
                return
        case _:
            print("Вы спотыкаетесь об камень ипадайте на землю, вас замечает страж")
            Player["hp"] -= 10
            if (battle(Guard) == False):
                GameOver()
                return
    print("Вы подходите к вратам...")
    print("Вы открываете их и с ужасом осознаёте, что вся история про покровителя явлалась ложью с целью сохранить сердце огня в тайне.")
    a = input("Желаете стразиться с сердцем огня? (Ответ y/n):")
    match a:
        case "y":
            if (battle(Heart) == False):
                print("Вы потерпели поражение и не смогли себе доказать, что вы способны на большее.")
                return
            else:
                print("Вы доказали себе, что готовы пройти через любые препятствия, пусть даже есть те которые таковыми не являются.")
                return
        case "n":
            print("Вы покинули храм, зная что верить никому не стоит.")
            return
        case _:
            print("Вы не смогли ничего придумать более осмысленного, вы просто покинули храм.")

Game()











