import os
myFileName = 'MyFile.txt'

base_dir = os.path.dirname(os.path.abspath(__file__))
def MakePath(yourFileName):
    return os.path.join(base_dir, yourFileName)

try:
    myFile = open(MakePath(myFileName), 'w')
    myFile.write("Студент номер 1\n")
    myFile.write("Моє прізвище - Бачиш\n")
    myFile.write("Моє запитання - Що таке словник в Python?\n")
    myFile.write("----------------------------------------\n")
    myFile.close()
except:
    print("Error 1")

try:
    with open(MakePath(myFileName), 'a') as file:
        file.write("Студент номер 2\n")
        file.write("Моє прізвище - Сагайдак\n")
        file.write("Моя відповідь - структура даних, що зберігає дані у вигляді ключ-значення\n")
        file.write("Моє запитання - Які основні типи даних в Python?\n")
        file.write("----------------------------------------\n")
except:
    print("Error 2")

try:
    with open(MakePath(myFileName), 'r') as file:
        file.seek(0)
        text = file.read()
        print(text)
except:
    print("Error 3")
