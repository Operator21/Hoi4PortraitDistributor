import os
from src.mod import Mod
import src.filehelper as FileHelper
import src.input as Input

newMod = Mod(Input.Get("Enter name of your mod: "), Input.Get("Enter targeted version of game (1.11.4): "))
print("Creating mod file")
FileHelper.WriteToFile(f"{newMod.FileName()}.mod", newMod.ModFile(True))
FileHelper.outputFolder += newMod.FileName() + "/"

print("Creating descriptor file")
FileHelper.WriteToFile("descriptor.mod", newMod.ModFile())


while not FileHelper.FolderHasFiles("input"):
    input("Insert your portrait files in the input folder, then press any key ")

imageList = FileHelper.GetFilesOfType('input', 'dds');
print(f"{len(imageList)} dds files detected")


print("Available structures:")
for file in FileHelper.GetFilesOfType("structure", "txt"):
    print(file)

while True:
    selectedStructure = input("Enter desired structure from the list above (default.txt is default value): ")
    if len(selectedStructure) == 0:
        selectedStructure = "default.txt"
    print(selectedStructure + " selected")
    if os.path.exists(FileHelper.structureFolder + selectedStructure):
        break
    print("Invalid input")

fileList = FileHelper.ReadFile(FileHelper.structureFolder + selectedStructure)

max = len(imageList)
pointer = 0

for file in fileList:
    FileHelper.CopyFile(FileHelper.inputFolder + imageList[pointer], FileHelper.leadersFolder() + file)
    print(FileHelper.leadersFolder() + file)
    if(pointer + 1 >= max):
        pointer = 0
    else:
        pointer += 1;