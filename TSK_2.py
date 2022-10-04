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
        array.append(random.randrange(10))
    return array

def PairMultiplication(array):
    arrayMulti = []
    for i in range(math.ceil(len(array)/2)):
        arrayMulti.append(array[i] * array[len(array) - 1 - i])
    return arrayMulti

array1 = GenerateList(CheckNumbers("Введите число элементов в массиве:"))
print(f"Сгенерирован массив: {array1}")
array2 = PairMultiplication(array1)
print(f"Произведение пар чисел в массиве есть массив: {array2}")