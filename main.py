import os
from src.mod import Mod
import src.filehelper as FileHelper
import src.input as Input

newMod = Mod(Input.Get("Enter name of your mod: "), Input.Get("Enter targeted version of game (1.11.4): "))

print("Creating .mod file")
#print(newMod.ModFile())
FileHelper.WriteToFile(f"{newMod.FileName()}.mod", newMod.ModFile())
FileHelper.outputFolder += newMod.FileName() + "/"


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

for file in fileList:
    FileHelper.CopyFile(FileHelper.inputFolder + imageList[0], FileHelper.leadersFolder() + file)
    print(FileHelper.leadersFolder() + file)