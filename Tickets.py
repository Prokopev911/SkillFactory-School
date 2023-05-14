# пункт 1
print("Введите количество билетов:")
tickets = int(input())
sum = 0

# пункт 2
for i in range(1, tickets+1):
    print("Введите возраст посетителя № " + str(i) + ":")
    age = int(input())
    if age < 18:
        print("Стоимость: 0руб")
        sum += 0
    elif age >= 18 and age < 25:
        print("Стоимость: 990руб")
        sum += 990
    else:
        print("Стоимость: 1390руб")
        sum += 1390

print("Общая стоимость:" + str(sum))

# пункт 3
if tickets > 3:
    sum *= 0.9

print("Общая стоимость со скидкой:" + str(sum))