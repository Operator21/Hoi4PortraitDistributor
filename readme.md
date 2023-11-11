## Hearts of Iron IV Portrait Distributor
### What is this?
This program allows you to simply create portrait replacer mods for Hears of Iron IV.

### How it works?
By providing any number (atleast 1) of png images to input folder and running main.py script. Script will guide you through mod creation process, you just enter name of the mod, targeted version and structure which you want to use. 

#### Activating created mod
Whole mod structure will be created in output folder, copying .mod file and folder from output to your Hearts of Iron IV mod folder and activating it in launcher is all you need to do to get it working.

### Structure
Is simple text (.txt) file which tells the script which images you want to replace. This file should be located in structure folder. Make sure that you follow pattern in given example.

#### example.txt
```txt
gfx/leaders/GXC/Portrait_Guanxi_Clique_Li_Zongren.dds
gfx/leaders/ger_leader1.dds
dlc/dlc028_la_resistance/gfx/leaders/POR/portrait_por_bento_goncalves.dds
```

### Requirements
Project was created using **Python 3.11.2** but older versions may work. Do no forget to install requirements.txt with pip.

```txt
pip install -r requirements.txt
```

### License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
