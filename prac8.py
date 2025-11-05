import os
myFileName = 'MyFile.txt'

base_dir = os.path.dirname(os.path.abspath(__file__))
def MakePath(yourFileName):
    return os.path.join(base_dir, yourFileName)


def NewStudent(number, fileName):
    if (number <= 0):
        print("Невірно вказаний номер студента")
        return
    fileName.write(f"Студент номер {number}\n")
    secName = str(input("Введіть ваше призвіще: "))
    fileName.write(f"Моє прізвище - {secName}\n")

    if (number > 1):
        answer = str(input("Введіть вашу відповідь на запитання: "))
        fileName.write(f"Моя вівдповідь - {answer}\n")
    
    question = str(input("Введіть ваше запитання: "))
    fileName.write(f"Моє запитання - {question}\n")
    fileName.write("----------------------------------------\n")


myFile = open(MakePath(myFileName), 'w')
NewStudent(1, myFile)
myFile.close()
