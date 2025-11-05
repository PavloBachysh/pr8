import os
myFileName = 'MyFile.txt'

base_dir = os.path.dirname(os.path.abspath(__file__))
def MakePath(yourFileName):
    return os.path.join(base_dir, yourFileName)


myFile = open(MakePath(myFileName), 'w')
myFile.write("Студент номер 1\n")
myFile.write("Моє прізвище - Бачиш\n")
myFile.write("Моє запитання - Що таке словник в Python?\n")
myFile.write("----------------------------------------\n")
myFile.close()
