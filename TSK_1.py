import random

def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
            else: print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def GenerateList(number):
    array = []
    for i in range(number):
        array.append(random.randrange(10))
    return array

def CountOddPositions(array):
    sum = 0
    for i in range(0, len(array), 2):
        sum += array[i]
    return sum
        
array = GenerateList(CheckNumbers("Введите число элементов в массиве:"))
print(f"Сгенерирован массив: {array}")
print(f"Сумма элементов на нечетных позициях равна: {CountOddPositions(array)}.")