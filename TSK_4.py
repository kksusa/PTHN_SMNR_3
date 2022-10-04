from pickletools import decimalnl_long


def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0 and number <= 100:
                return number
            else: print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def DecimalToBinary(number):
    bin = []
    strbin = ""
    while number >= 1:
        bin.append(number % 2)
        number = number // 2
    for i in range(len(bin) // 2):
        temp = bin[i]
        bin[i] = bin[len(bin) - 1 - i]
        bin[len(bin) - 1 - i] = temp
    for i in bin:
        strbin = strbin + str(i)
    return strbin


data = open('number.txt', 'w')
data.write(str(CheckNumbers("Введите число от 1 до 100:")))
data = open('number.txt', 'r')
decimalNumber = int(data.readline())
data.close
print(f"Двоичное представление числа {decimalNumber} является {DecimalToBinary(decimalNumber)}.")