# ==== ДАННЫЕ ИГРОКА ====
PlayerHealthPoint = 25
PlayerEnergyPoint = 20
PlayerInventory = [
    ["Железный меч", 5],
    ["Зелье здоровья", 8],
    ["Зелье здоровья", 8],
    ["Зелье выносливости", 10],
    ["Зелье выносливости", 10]
]

# ==== ДАННЫЕ ПРОТИВНИКОВ ====
EnemyHealthPoint = 0
EnemyComponents = []
EnemyInventory = []
EnemyStrategy = []
EnemyMove = 0
Round = 1
DeleteItem = 0
Move = "Player"


# ==== ФУНКЦИИ ====

def EntityEnemy(Name):
    global EnemyMove, EnemyComponents, EnemyStrategy, EnemyInventory, EnemyHealthPoint
    EnemyMove = 0
    EnemyComponents = []
    EnemyStrategy = []
    EnemyInventory = []

    if Name == "Ложный герой":
        EnemyHealthPoint = 20
        EnemyInventory = [
            ["Железный меч", 5],
            ["Золотой меч", 4],
            ["Зелье здоровья", 10],
            ["Зелье выносливости", 0]
        ]
        EnemyStrategy = [0, 1, 1, 1, 2, 3]
    elif Name == "Покровитель Лоз":
        EnemyHealthPoint = 30
        EnemyInventory = [
            ["Лоза", 2],
            ["Бумеранг", 3],
            ["Зелье здоровья", 14],
            ["Зелье здоровья", 6]
        ]
        EnemyStrategy = [0, 1, 0, 3, 4]
    elif Name == "Богоискатель":
        EnemyHealthPoint = 40
        EnemyInventory = [
            ["Булава", 2],
            ["Горячий осколок", 5],
            ["Зелье выносливости", 0],
            ["Зелье выносливости", 0],
            ["Удар молнии", 1]
        ]
        EnemyStrategy = [0, 1, 2, 3, 4]


def ItemComponents(item):
    # проверка всех предметов
    global EnemyHealthPoint, PlayerHealthPoint, PlayerEnergyPoint, DeleteItem, Move
    Name = item[0]
    Number = item[1]

    # === МЕЧИ ===
    if Name == "Железный меч":
        if Move == "Player":
            if PlayerEnergyPoint < 1:
                print("У вас недостаточно энергии, чтобы использовать Меч!")
            else:
                EnemyHealthPoint -= Number
                PlayerEnergyPoint -= 1
                print("Вы нанесли", Number, "урона противнику при помощи железного меча!")
        else:
            PlayerHealthPoint -= Number
            print("Противник нанес вам", Number, "урона при помощи железного меча!")

    if Name == "Золотой меч":
        if Move == "Player":
            if PlayerEnergyPoint < 1:
                print("У вас недостаточно энергии, чтобы использовать Меч!")
            else:
                EnemyHealthPoint -= 2 * Number
                item[1] -= 1
                if item[1] == 0:
                    DeleteItem = 1
                PlayerEnergyPoint -= 1
                print("Вы нанесли", 2 * Number, "урона противнику при помощи золотого меча!")
        else:
            PlayerHealthPoint -= 2 * Number
            item[1] -= 1
            if item[1] == 0:
                DeleteItem = 1
            print("Противник нанес вам", 2 * Number, "урона при помощи золотого меча!")

    # === БУМЕРАНГ ===
    if Name == "Бумеранг":
        if PlayerEnergyPoint < 1:
            print("У вас недостаточно энергии, чтобы использовать Бумеранг!")
        else:
            if Move == "Player":
                EnemyHealthPoint -= 2 * Number
                PlayerHealthPoint -= Number
                PlayerEnergyPoint -= 1
                print("Вы бросили Бумеранг! Нанесли", 2 * Number, "урона врагу и получили", Number, "урона сами.")
            else:
                PlayerHealthPoint -= 2 * Number
                EnemyHealthPoint -= Number
                print("Противник использовал Бумеранг! Вы получили", 2 * Number, "урона, противник тоже получил",
                      Number, "урона.")

    # === ЗЕЛЬЯ ===
    if Name == "Зелье здоровья":
        if Move == "Player":
            PlayerHealthPoint += Number
            print("Вы выпили Зелье здоровья и восстановили", Number, "здоровья!")
        else:
            EnemyHealthPoint += Number
            print("Противник использовал Зелье здоровья и восстановил", Number, "здоровья!")
        DeleteItem = 1

    if Name == "Зелье выносливости":
        if Move == "Player":
            PlayerEnergyPoint += Number
            print("Вы выпили Зелье выносливости и восстановили", Number, "энергии!")
        else:
            print("Противник использовал Зелье выносливости (эффект на врага не реализован)")
        DeleteItem = 1

    # === ГОРЯЧИЙ ОСКОЛОК ===
    if Name == "Горячий осколок":
        damage = 3 * Number
        if Move == "Player":
            EnemyHealthPoint -= damage
            print("Вы использовали Горячий осколок и нанесли", damage, "урона противнику!")
        else:
            PlayerHealthPoint -= damage
            print("Противник использовал Горячий осколок и нанёс вам", damage, "урона!")
        DeleteItem = 1

    # === БУЛАВА ===
    if Name == "Булава":
        damage = 3 * Number
        if Move == "Player":
            if PlayerEnergyPoint < 4:
                print("У вас недостаточно энергии, чтобы использовать Булаву!")
            else:
                EnemyHealthPoint -= damage
                PlayerEnergyPoint -= 4
                print("Вы использовали Булаву и нанесли", damage, "урона противнику!")
        else:
            PlayerHealthPoint -= damage
            print("Противник использовал Булаву и нанёс вам", damage, "урона!")

    # === УДАР МОЛНИИ ===
    if Name == "Удар молнии":
        required_energy = 999
        if Move == "Player":
            if PlayerEnergyPoint < required_energy:
                print("У вас недостаточно энергии, чтобы использовать Удар молнии!")
            else:
                damage = EnemyHealthPoint - 1
                if damage < 0:
                    damage = 0
                EnemyHealthPoint -= damage
                PlayerEnergyPoint -= required_energy
                print("Вы использовали Удар молнии и нанесли", damage, "урона противнику!")
        else:
            damage = PlayerHealthPoint - 1
            if damage < 0:
                damage = 0
            PlayerHealthPoint -= damage
            print("Противник использовал Удар молнии и нанёс вам", damage, "урона!")

    # === ЛОЗА ===
    if Name == "Лоза":
        if Move == "Player":
            EnemyHealthPoint -= Number
            print("Вы использовали Лозу и нанесли", Number, "урона противнику!")
        else:
            PlayerHealthPoint -= Number
            print("Противник использовал Лозу и нанёс вам", Number, "урона!")
        item[1] += 2


# ==== БОЙ ====
def fight(Enemy):
    global EnemyMove, EnemyComponents, EnemyStrategy, EnemyInventory, EnemyHealthPoint
    global Move, DeleteItem, PlayerHealthPoint, PlayerEnergyPoint

    EntityEnemy(Enemy)
    print("\n=== Начало боя с", Enemy, "===")

    while PlayerHealthPoint > 0 and EnemyHealthPoint > 0:
        # --- Ход игрока ---
        Move = "Player"
        print("\nВаш ход")
        print("- Здоровье:", PlayerHealthPoint)
        print("- Энергия:", PlayerEnergyPoint)
        print("- Здоровье противника:", EnemyHealthPoint)
        print("- Использовать предмет:")
        for i in range(len(PlayerInventory)):
            print(i, "-", PlayerInventory[i])

        # Проверка выбора предмета
        try:
            PlayerMove = int(input("Выберите номер: ")) # вот тут я воспользовался ИИ, так как не знал как исправить баг на ошибку после поломки любого предмета
        except ValueError:
            PlayerMove = -1

        if PlayerMove < 0 or PlayerMove >= len(PlayerInventory):
            print("Некорректный выбор! Вы пропустили ход.")
        else:
            ItemComponents(PlayerInventory[PlayerMove])
            if DeleteItem == 1:
                del PlayerInventory[PlayerMove]
                DeleteItem = 0

        # --- Ход противника ---
        if EnemyHealthPoint <= 0:
            break

        Move = "Enemy"
        print("\nХод противника")
        ItemComponents(EnemyInventory[EnemyStrategy[EnemyMove]])
        if DeleteItem == 1:
            delete_index = EnemyStrategy[EnemyMove]
            del EnemyInventory[delete_index]
            del EnemyStrategy[EnemyMove]
            for i in range(len(EnemyStrategy)):
                if EnemyStrategy[i] > delete_index:
                    EnemyStrategy[i] -= 1
            DeleteItem = 0
            if EnemyMove >= len(EnemyStrategy):
                EnemyMove = 0

        if PlayerHealthPoint <= 0:
            print("Вы погибли!")
            return False

        # Следующий ход врага
        if len(EnemyStrategy) > 0:
            EnemyMove = (EnemyMove + 1) % len(EnemyStrategy)

    print("Битва с", Enemy, "закончена!")
    return True


# ==== ИГРОВОЙ ЦИКЛ ====
def gamestart():
    global PlayerInventory
    print("Добро пожаловать в Колизей боли! Ваша задача — победить всех трёх противников и сбежать.")
    input()

    # Раунд 1: Ложный герой
    if not fight("Ложный герой"):
        print("Игра окончена. Колизей удержал вас.")
        return
    # Награды
    PlayerInventory.append(["Золотой меч", 5])
    PlayerInventory.append(["Зелье выносливости", 15])
    print("\nВы получили награды: Золотой меч и Зелье выносливости")
    input()

    # Раунд 2: Покровитель Лоз
    if not fight("Покровитель Лоз"):
        print("Игра окончена. Колизей удержал вас.")
        return
    # Награды
    PlayerInventory.append(["Лоза", 2])
    PlayerInventory.append(["Зелье здоровья", 12])
    print("\nВы получили награды: Лоза и Зелье здоровья")
    input()

    # Раунд 3: Богоискатель
    if not fight("Богоискатель"):
        print("Игра окончена. Колизей удержал вас.")
        return

    # Победа
    print("\nПоздравляем! Вы победили всех противников и сбежали из Колизея!")



gamestart()