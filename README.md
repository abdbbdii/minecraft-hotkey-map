# MINECRAFT HOTKEY CHART GENERATOR

## Video Demo:

##### [Watch on YouTube](https://www.youtube.com/watch?v=SlrZR0yFiYM)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/SlrZR0yFiYM/0.jpg)](https://www.youtube.com/watch?v=SlrZR0yFiYM "Watch on youtube")

## Requirements:

1. Make sure you have downloaded the code to your own Windows computer.
2. Make sure you have Minecraft game installed on your Windows computer.
3. Make sure you have an active internet connection.

## Program Description:

### Overview:
This Program generates a customized Minecraft hotkey chart in either SVG or PNG format. It does so by parsing an SVG template, extracting keybindings and modifiers from the Minecraft game configuration, and then updating the SVG template with the customized keybindings.

### Here's a detailed breakdown of the code:
#### 1. Importing Libraries:
   - `requests` for making HTTP requests to download the SVG template.
   - `xml.etree.ElementTree` as `ET` for parsing and manipulating SVG data.
   - `re` for regular expression operations.
   - `os` for working with the file system.
   - `sys` for system-related operations.
   - `cairosvg` for converting SVG to PNG.
   - `colr` for color manipulation in CLI.


#### 3. Defining Parameters:
- Various parameters such as `output_file_name`, `input_SVG_link`, `input_file_name`, `mod_colors`, and `key_list` are defined. These parameters determine the output file name, source SVG link, mod colors, and a list of Minecraft keys.


#### 4. Reading Minecraft Keystrokes:
- The program attempts to open the Minecraft options file (`options.txt`) to extract keystrokes and their associated actions. If the file is not found, it exits with an error message.


#### 5. Extracting Keystrokes:
- The program parses each line of the options.txt file of the game using regular expressions to extract keybindings and associated actions. It categorizes them into modded or vanilla actions.


#### 6. Customizing Color Scheme:
- The program allows the user to customize the color scheme for the hotkey chart interactively. It prompts the user to choose colors for various elements such as:
    - Background
    - Header Text
    - Custom Keys Frame
    - Mouse Frame
    - Keyboard Frame
    - Mods Section Frame
    - Keyboard Key
    - Default Text

#### 7. Choosing Output Format:
- The user is prompted to choose between generating an SVG or PNG file. If PNG is selected, the user can specify a scale factor for the image.


#### 8. Applying Color Scheme:
- The program applies the chosen color scheme to the SVG file by modifying the relevant attributes in the SVG XML data.


#### 9. Matching Keybindings:
- The program matches the extracted keybindings with their corresponding text representations in the SVG file and updates them.


#### 10. Writing Output File:
- Depending on the chosen output format (SVG or PNG), the program either writes the modified SVG file or converts it to PNG using CairoSVG. Temporary SVG files are created during this process and cleaned up afterward.


#### 11. Functions:
- `cleanup()` A utility function to remove duplicates from a list of modnames.
- `combine()` A utility function to combine two lists into a dictionarywhere elements from the first list are keys and elements from the secondlist are values.
- `getUserPath()` A function that returns the path to the Minecraftoptions file in the user's APPDATA directory.
- `change_color()` A function that allows the user to input a colorvalue in hexadecimal format (#RRGGBB) and validates it. It returns theselected color.


### Summary:
This program not only takes Minecraft keybindings but also the mods used to modify the base game, from the game's configuration file and combines them with an SVG template, customizes the appearance of the hotkey chart and outputs it in the user's preferred format (SVG or PNG). It offers a way for Minecraft players to create visual hotkey charts for reference while playing the game.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/abdbbdii)

![Made with Python](https://img.shields.io/badge/Made_with_Python-3776AB?style=for-the-badge&logo=python&logoColor=white)<br>
![BSD Licensed](https://img.shields.io/badge/BSD_Licensed-AB2B28?style=for-the-badge&logo=bsd&logoColor=white)
