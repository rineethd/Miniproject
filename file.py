import os


def checkcred(uid, pw):
    flag = 0
    file = open('credentials.txt', 'r')
    data = file.readlines()
    for i in data:
        d = i.split()
        if uid == d[0]:
            if pw == d[1]:
                print("Your credentials are valid")
                flag = 1
                return 1
    if flag == 0:
        print("Your credentials are invalid")
        file.close()
        return 0


def menu():
    if r == 1:
        q = input("""a.Show the List of Student
    b.Add New Student
    c.Searching Student
    d.Deleting a Student""")
        if q == 'a':
            for i in range(5):
                file = open("student" + str(i + 1), 'r')
                txt = file.read()
                print(txt)
            file.close()
        if q == 'b':
            file = open("student" + str(6), 'a')
            d = {}
            name = input("Enter student's name: ")
            d['Name'] = name
            d['Age'] = int(input("Enter student's age: "))
            d['Section'] = input("Enter the student's section: ")
            d['Year'] = int(input("Enter the year: "))
            d['Dept'] = input("Enter the department: ")
            file.write(str(d))
            file.close()
        if q == 'c':
            name = input("Enter the name of the student")
            for i in range(5):
                file = open("student" + str(i + 1), 'r')
                txt = file.read()
                if txt.find(name) != -1:
                    print(txt)
            file.close()
        if q == 'd':
            name = input("Enter the name of the student")
            for i in range(6):
                file = open("student" + str(i + 1), 'r')
                txt = file.read()
                if txt.find(name) != -1:
                    os.remove("student" + str(i + 1))
            print("Record deleted")


ch = int(input("""1. Admin
2.Student """))
if ch == 1:
    c = int(input("""1.Sign-up
2.Log-in"""))
    if c == 1:
        ID = input("Enter your username:")
        pw = input("Enter a strong password:")
        file = open('credentials.txt', 'a')
        file.write(ID)
        file.write(" ")
        file.write(pw)
        file.write("\n")
        file.close()
    elif c == 2:
        uid = input("Enter your admin user ID: ")
        pw = input("Enter your password: ")
        r = checkcred(uid, pw)
        menu()


elif ch == 2:
    c = int(input("""1.Sign-up
  2.Log-in"""))
    if c == 1:
        ID = input("Enter your username:")
        pw = input("Enter a strong password:")
        file = open('credentials.txt', 'a')
        file.write(ID)
        file.write(" ")
        file.write(pw)
        file.write("\n")
        file.close()
    elif c == 2:
        uid = input("Enter your student user ID: ")
        pw = input("Enter your password: ")
        r = checkcred(uid, pw)
        menu()