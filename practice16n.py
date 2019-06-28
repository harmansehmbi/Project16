import os

print(os.getcwd())
print(os.name)

print(os.getlogin())
print(os.getppid())


pathToDir = "\This PC\HARMANPREET\Downloads"                      # path to directory
pathToFile= "\This PC\HARMANPREET\Downloads\practice12a.csv"      # path to file

print("Is Downloads available:", os.path.exists(pathToDir))
print("Is practice12a.csv available:", os.path.exists(pathToFile))

files = os.walk("\This PC\HARMANPREET\Downloads")
print("files:", files)

allFiles = list(files)
for file in allFiles:
    print(file)