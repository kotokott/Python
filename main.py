simpleList = [3, 7, 4, 2]
simpleList.append(4)

anotherList = [3, True, 'Vitya', 2.0]

print(simpleList[2])

print(simpleList[-1]) # последний элемент списка

print(simpleList[0:2]) #срез - sublist

print(simpleList[:3]) # срез до индекса 3
print(simpleList[1:]) # с индекса 1

simpleList[1] = 'fish'
print(simpleList)

print(simpleList.index('fish'))
# print(simpleList.index('fish', 3)) поиск, начиная с индекса 3

simpleList.remove('fish')
simpleList.sort()
print(simpleList)
simpleList.sort(reverse=True)
print(simpleList)

names = ["Стив", "Рейчел", "Майкл", "Адам", "Джессика", "Лестер"] # А-Я
names.sort()
print(names)

print(simpleList.pop(3)) # удаление по индексу + return элемента

simpleList.extend([12, 45]) # можно еще с помощью +
print(simpleList)

simpleList.insert(1, 5)
print(simpleList)

