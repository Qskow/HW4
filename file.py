# #1

a = [4, 3, 11, 5, 1, 13, 0, 112312]
j = 1
while j < len(a):
    for i in range(0, len(a) - 1):
        if a[i+1] < a[i]:
            b = a[i]
            a[i] = a[i + 1]
            a [i + 1] = b
    j += 1        

print(a)

#2

dict_colors = {}

pink_rgb = (255,192,203)
yellow_rgb = (255,255,0)
blue_rgb = (0, 0, 255)

dict_colors = dict(Pink = None, Yellow = None, Blue= None)
print(dict_colors)

dict_colors['Pink'] = pink_rgb
dict_colors['Yellow'] = yellow_rgb
dict_colors['Blue'] = blue_rgb
print(dict_colors)

#3

import random

s1 = set()
s2 = set()
i = 0
while i < 22:
    s1.add(random.randrange(1, 50))
    s2.add(random.randrange(1, 50))
    i += 1
print('s1:', s1)
print('s2:', s2)

print("Пересечение множеств:", s1.intersection(s2))
print("Уникальные элементы первого множества:", s1.difference(s2))
print("Уникальные элементы второго множества:", s2.difference(s1))
print("Элементы, входящие в первое или во второе, но не в оба из них одновременно",s1.symmetric_difference(s2))

#4

stock = {
    "sleeping bag": 1500,
    "tent": 3000,
    "first aid kit": 500,
    "flashlight": 200,
    "thermos": 300,
    "axe": 2000,
    "cup": 300,
    "tent": 3000,
    "bread": 300,
    "bottle of water": 900,
    "lighter": 50
}

inventory = {
    "bread": 300,
    "bottle of water": 900,
    "lighter": 50
}

while True == True:
    print("""
    1) Добавить предмет в интвентарь.
    2) Удалить предмет из инвентаря.
    3) Список предметов из инвентаря.
    4) Закрыть.
    """)
    weight = 0
    rez = input()
    for key in inventory:
            weight += int(inventory.get(f"{key}"))
    if rez == "1":
        print("Список предметов на выбор: ")
        for key in stock:
            print(key,"-", stock.get(key), "гр")
        print("Вес вашего рюкзака составляет:", weight, "гр")
        print("Свободного места осталось:", 5000 - weight, "гр")
        item = input("Введите название предмета, который хотите добавить: ")
        if item in stock:
            if item in inventory:
                print("Этот предмет уже добавлен в инвентарь")
            if weight + stock.get(item) < 5000:
                solo_weight = int(stock.get(f"{item}"))
                inventory[f"{item}"] = f"{solo_weight}"
            else:
                print("У вас недостаточно места в рюкзаке.")
        else:
            print("Такого предмета на складе нет")
    if rez == "2":
        print("Список предметов на выбор: ")
        for key in inventory:
            print(key,"-", inventory.get(key), "гр")
            
        
        item = input("Введите название предмета, который хотите удалить: ")
        if item in inventory:
            del inventory[item]
        else:
            print("Такого предмета в инвентаре нет")
    if rez == "3":
        for key in inventory:
            print(key,"-", inventory.get(key), "гр")
        print("Вес вашего рюкзака составляет:", weight, "гр")
        print("Свободного места осталось:", 5000 - weight, "гр")    
    if rez == "4":
        break
    


