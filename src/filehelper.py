import os, shutil

outputFolder = "output/"
inputFolder = "input/"
structureFolder = "structure/"

def leadersFolder():
    return outputFolder + "gfx/leaders/"

def CreateFolder(folder):
    os.makedirs(os.path.dirname(folder), exist_ok=True)

def WriteToFile(path, content):
    os.makedirs(os.path.dirname(outputFolder + path), exist_ok=True)
    file = open(outputFolder + path, "w")
    file.write(content)
    file.close()

def FolderHasFiles(path):
    if os.listdir(path) == []:
        return False
    return True

def MoveFile(oldPath, newPath):
    os.rename(oldPath, newPath)

def InToOut(oldPath, newPath):
    MoveFile(inputFolder + oldPath, outputFolder + newPath)

def GetFilesOfType(folder, type):
    list = []
    for file in os.listdir(folder):
        if file.endswith("." + type):
            list.append(file)
    return list

def ReadFile(path):
    list = []
    file = open(path)
    for line in file:
        parsed = line.replace("\n", "")
        list.append(parsed)
    return list

def CopyFile(source, destination):
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copyfile(source, destination)

CreateFolder(outputFolder)
CreateFolder(inputFolder)
