immport os

que = input("do u want to shutdown ur computer?(y/n):")

if que == "n":
    exit()
else:
    os.system("shutdown /s /t 1")
