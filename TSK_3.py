import random
import math

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
        array.append(round(random.random() * 2 - 1, 2) + random.randint(-9, 9))
    return array

def Difference(array):
    max = min = abs(round(math.fmod(array[0], 1), 2))
    for i in range(1, len(array)):
        fracPart = abs(round(math.fmod(array[i], 1), 2))
        if fracPart > max: max = fracPart
        elif fracPart < min: min = fracPart
    diff = round(max - min, 2)
    return diff

array = GenerateList(CheckNumbers("Введите число элементов в массиве:"))
print(f"Сгенерирован массив: {array}")
print(f"Разница между максимальным и минимальным значением дробной части: {Difference(array)}")