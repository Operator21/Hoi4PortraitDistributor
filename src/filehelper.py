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

import os, shutil
from PIL import Image, ImageOps

outputFolder = "output/"
inputFolder = "input/"
structureFolder = "structure/"

def LeadersFolder():
    """
    Returns the path to the leaders folder in the output directory.
    """
    #return outputFolder + "gfx/leaders/"
    return outputFolder + ""

def CreateFolder(folder):
    """
    Creates a new folder at the specified path if it does not already exist.
    
    :param folder: Path of the folder to be created.
    """
    os.makedirs(os.path.dirname(folder), exist_ok=True)

def WriteToFile(path, content):
    """
    Writes the given content to a file at the specified path.
    
    :param path: Path of the file to write to.
    :param content: Content to write to the file.
    """
    os.makedirs(os.path.dirname(outputFolder + path), exist_ok=True)
    file = open(outputFolder + path, "w")
    file.write(content)
    file.close()

def FolderHasFiles(path):
    """
    Checks if the folder at the specified path has any files.
    
    :param path: Path of the folder to check.
    :return: True if the folder has files, False otherwise.
    """
    if os.listdir(path) == []:
        return False
    return True

def MoveFile(oldPath, newPath):
    """
    Moves a file from oldPath to newPath.
    
    :param oldPath: Current path of the file.
    :param newPath: The new path for the file.
    """
    os.rename(oldPath, newPath)

def InToOut(oldPath, newPath):
    """
    Moves a file from the input folder to the output folder.
    
    :param oldPath: Current path of the file in the input folder.
    :param newPath: The new path for the file in the output folder.
    """
    MoveFile(inputFolder + oldPath, outputFolder + newPath)

def GetFilesOfType(folder, type):
    """
    Retrieves all files of a particular type from a specified folder.
    
    :param folder: The folder to search in.
    :param type: The file type to look for.
    :return: A list of filenames of the specified type.
    """
    list = []
    for file in os.listdir(folder):
        if file.endswith("." + type):
            list.append(file)
    return list

def ReadFile(path):
    """
    Reads a file and returns a list of its lines.
    
    :param path: The path to the file.
    :return: A list of lines from the file.
    """
    list = []
    file = open(path)
    for line in file:
        parsed = line.replace("\n", "")
        list.append(parsed)
    return list

def CopyFile(source, destination):
    """
    Copies a file from source to destination.
    
    :param source: The path to the source file.
    :param destination: The path to the destination file.
    """
    destination_path = os.path.dirname(destination)
    os.makedirs(destination_path, exist_ok=True)
    
    if os.path.exists(destination):
        print("Destination file already exists.")
        return
    
    # Open the image file using PIL
    image = Image.open(source)
    
    # Resize the image to default HOI4 portrait size, stretch to fill
    image = ImageOps.fit(image, (156, 210))

    
    # Save the image in dds format
    dds_destination = os.path.splitext(destination)[0] + ".dds"
    image.save(dds_destination)
    
    print("Image copied and converted to dds format.")

def ConvertPath(path):
    """
    Converts a path to a sanitized path.

    :param path: The path to be sanitized.
    :return: The sanitized path.
    """
    # Split the path into parts
    parts = path.split('/')
    
    # Check if the path starts with 'dlc'
    if parts[0] == 'dlc':
        # Remove the 'dlc' part and the following part
        parts = parts[2:]
    
    # Join the parts back into a path
    return '/'.join(parts)

CreateFolder(outputFolder)
CreateFolder(inputFolder)
