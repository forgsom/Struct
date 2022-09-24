# Реализовать методы последовательного и бинарного поиска для массива записей следующей структуры: Фамилия, дата_рождения, адрес. Методы реализовать для поля Фамилия.

class Struct:
    def __init__(self, name, date, address):
        self.name = name
        self.date = date
        self.address = address
        self.array_struck = []
        self.array_name = []
    
    def _append(self, name, date, address):
        name, date, address = input("name "), input("date "), input("address ")
        line = list(name + date + address)
        self.array_struck += line
        self.array_name += name

    def search(self, name):
        flag = False
        k = 0
        for i in self.array_name:
            k += 1
            if name in i:
                flag = True
                return flag, k

    def binarySearch(self, name):
        self.array_name = sorted(self.array_name)
        first = 0
        last = len(self.array_name) - 1
        flag = False
        k = 0
        while first <= last and not flag:
            k += 1
            middle = (first + last) // 2
            guess = self.array_name[middle]
            if guess == name:
                flag = True
                return flag, k
            elif guess > name:
                last = middle - 1
            else:
                first = middle + 1
        return flag, k

name, date, address = "", "", ""

s = Struct(name, date, address)

number = int(input("\nSKOKA ZAPISEI? "))
for i in range(number):
    s._append(name, date, address)

print (s.array_struck)
print (s.array_name)

element = input("\nCHTO ISKAT ")
print(s.search(element), "\n\n")

print(s.binarySearch(element))
#a q z