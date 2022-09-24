class Student:
    def __init__(self, name, date, curs, group):
        self.name = name
        self.date = date
        self.curs = curs
        self.group = group
        self.stack = []


    def append(self, name, date, curs, group):
        file = open("text.txt", "a")
        line = str(self.name) + " " + str(self.date) + " " + str(self.curs) + " " + str(self.group)
        file.writelines(line+"\n")
        file.close()

    def delete(self, name, date, curs, group):
        file1 = open("text.txt", "r")
        file2 = open("text2.txt", "w")
        element = str(self.name) + " " + str(self.date) + " " + str(self.curs) + " " + str(self.group)
        for line in file1:
            if element not in line:
                file2.write(line)
        file1.close()
        file2.close()
        
        file1 = open("text.txt", "w")
        file2 = open("text2.txt", "r")
        for line in file2:
            file1.write(line)
        file1.close()
        file2.close()

    def check(self, name, date, curs, group):
        file = open("text.txt", "r")
        line = str(self.name) + " " + str(self.date) + " " + str(self.curs) + " " + str(self.group)
        index = 0
        for i in file:
            if line in i:
                print("\n"+str(index)+" "+line)
            index+=1
        file.close()

    def show(self):
        file = open("text.txt", "r")
        print(file.readlines())
        file.close()


name, date, curs, group = "","","",""

#menu
while True:
    print("\n1. append element")
    print("2. delete element")
    print("3. check element")
    print("4. show all element")
    print("0. quit")
    cmd = input("\nSelect: ")
    print()
    
    if cmd == "1":
        name, date, curs, group = input("name "), input("date "), input("curs "), int(input("group "))
        student = Student(name, date, curs, group)
        student.append(name, date, curs, group)

    elif cmd == "2":
        name, date, curs, group = input("name "), input("date "), input("curs "), int(input("group "))
        student = Student(name, date, curs, group)
        student.delete(name, date, curs, group)

    elif cmd == "3":
        name, date, curs, group = input("name "), input("date "), input("curs "), int(input("group "))
        student = Student(name, date, curs, group)
        student.check(name, date, curs, group)

    elif cmd == "4":
        student = Student(name, date, curs, group)
        student.show()

    elif cmd == "0":
        break

    else:
        print("Wrong command\n")