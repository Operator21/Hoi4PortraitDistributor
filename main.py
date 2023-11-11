"""
Copyright (C) 2023 Stanislav Zdych

This file is part of the Hoi4PortraitDistributor.

Hoi4PortraitDistributor is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
from src.mod import Mod
import src.filehelper as FileHelper
import src.input as Input

# Get mod details from user
newMod = Mod(Input.Get("Enter name of your mod: "), Input.Get("Enter targeted version of game (1.11.4): "))

# Create mod file
print("Creating mod file")
FileHelper.WriteToFile(f"{newMod.FileName()}.mod", newMod.ModFile(True))
FileHelper.outputFolder += newMod.FileName() + "/"

# Create descriptor file
print("Creating descriptor file")
FileHelper.WriteToFile("descriptor.mod", newMod.ModFile())

# Wait for input files
while not FileHelper.FolderHasFiles("input"):
    input("Insert your portrait files in the input folder, then press any key ")

# Get list of image files
imageList = FileHelper.GetFilesOfType('input', 'png')
print(f"{len(imageList)} dds files detected")

# Display available structures
print("Available structures:")
for file in FileHelper.GetFilesOfType("structure", "txt"):
    print(file)

# Get desired structure from user
while True:
    selectedStructure = input("Enter desired structure from the list above (default.txt is default value): ")
    if len(selectedStructure) == 0:
        selectedStructure = "default.txt"
    print(selectedStructure + " selected")
    if os.path.exists(FileHelper.structureFolder + selectedStructure):
        break
    print("Invalid input")

# Read structure file
fileList = FileHelper.ReadFile(FileHelper.structureFolder + selectedStructure)

# Prepare to distribute images among files
max = len(imageList)
pointer = 0

# Distribute images among files
for file in fileList:
    # Replace file path to sanitize dlc portraits
    newpath = FileHelper.ConvertPath(file)

    FileHelper.CopyFile(FileHelper.inputFolder + imageList[pointer], FileHelper.LeadersFolder() + newpath)
    print(FileHelper.LeadersFolder() + newpath)
    if pointer + 1 >= max:
        pointer = 0
    else:
        pointer += 1
