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

def ListCreate(number):
    array = []
    for i in range(m * n):
        array.append(random.randint(1, 9))
    return array

def ListShuffle(arrayIn):
    chosenIndexArray = []
    for i in range(len(arrayIn) // 2):
        while True:
            tempIndex1 = random.randrange(len(arrayIn))
            tempIndex2 = random.randrange(len(arrayIn))
            if tempIndex1 not in chosenIndexArray and tempIndex2 not in chosenIndexArray and tempIndex1 != tempIndex2:
                temp = arrayIn[tempIndex1]
                arrayIn[tempIndex1] = arrayIn[tempIndex2]
                arrayIn[tempIndex2] = temp
                chosenIndexArray.append(tempIndex1)
                chosenIndexArray.append(tempIndex2)
                break
    return arrayIn

def PrintArray(array, param):
    for i in range(len(array)):
        print(f"{array[i]}", end = " ")
        if (i + 1) % param == 0: print()    

while True:
    m = CheckNumbers("Введите число строк в массиве:")
    n = CheckNumbers("Введите число столбцов в массиве:")
    result = m * n
    if (result) % 2 == 0:
        break
    else: print(f"Произведение чисел {m} и {n} нечётное. Пожалуйста, повторите ввод.")

array1 = ListCreate(result)
PrintArray(array1, m)
print()
array2 = ListShuffle(array1)
PrintArray(array2, m)