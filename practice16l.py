import os

print(os.getcwd())
print(os.name)

print(os.getlogin())
print(os.getppid())


pathToDir = "\This PC\HARMANPREET\Downloads"                      # path to directory
pathToFile= "\This PC\HARMANPREET\Downloads\practice12a.csv"      # path to file

print("Is Downloads available:", os.path.exists(pathToDir))
print("Is practice12a.csv available:", os.path.exists(pathToFile))

# path = "\This PC\HARMANPREET\Downloads\MyPythonPrograms"
# os.mkdir(path)

print(os.getcwd())
os.chdir("\This PC\HARMANPREET\Downloads\MyPythonPrograms")
print(os.getcwd())