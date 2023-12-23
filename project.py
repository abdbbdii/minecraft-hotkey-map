import requests
import xml.etree.ElementTree as ET
import re
import os
import sys
import cairosvg
from colr import color


def main():
    # Defining all changable parameters

    output_file_name = "Minecraft_hotkey_chart"
    input_SVG_link = "https://svgshare.com/i/xdy.svg"
    input_file_name = "input_SVG_file.svg"

    mod_colors = [
        "#FFF680",
        "#6EC167",
        "#F1693F",
        "#6699FF",
        "#FF6666",
        "#EA9F21",
        "#1B7639",
        "#8E67AD",
        "#FF99CC",
        "#05A485",
        "#F58E68",
        "#669999",
        "#FF9999",
        "#0F75BC",
        "#A76D35",
        "#A52A2A",
        "#336666",
        "#996666",
        "#CC9966",
        "#00BFFF",
        "#F064A5",
        "#CCFF00",
    ]

    # Defining all keys

    key_list = [
        "mouse.left",
        "mouse.right",
        "mouse.middle",
        "mouse.scroll",
        "mouse.4",
        "mouse.5",
        "mouse.6",
        "mouse.7",
        "mouse.8",
        "mouse.9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "grave.accent",
        "equal",
        "minus",
        "right.bracket",
        "left.bracket",
        "backslash",
        "semicolon",
        "apostrophe",
        "comma",
        "period",
        "slash",
        "enter",
        "space",
        "escape",
        "tab",
        "backspace",
        "caps.lock",
        "left.shift",
        "left.control",
        "left.alt",
        "left.win",
        "right.shift",
        "right.control",
        "right.alt",
        "right.win",
        "menu",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "up",
        "down",
        "left",
        "right",
        "insert",
        "home",
        "page.up",
        "delete",
        "end",
        "page.down",
        "scroll.lock",
        "print.screen",
        "pause",
        "keypad.num.lock",
        "keypad.0",
        "keypad.1",
        "keypad.2",
        "keypad.3",
        "keypad.4",
        "keypad.5",
        "keypad.6",
        "keypad.7",
        "keypad.8",
        "keypad.9",
        "keypad.divide",
        "keypad.multiply",
        "keypad.subtract",
        "keypad.add",
        "keypad.enter",
        "keypad.decimal",
    ]

    # Importing keystrokes from the minecraft folder

    text_id_incomplete = {}
    line_color_incomplete = {}
    mods = []

    file_path = getUserPath(".minecraft\options.txt")
    try:
        keyFile = open(file_path, "r")
    except FileNotFoundError:
        sys.exit("FileNotFoundError:\nMake sure your Minecraft is installed correctly.\n")

    # Extracting keystrokes from minecraft options file

    for line in keyFile:
        if pattern := re.match("^key_(.+):(.+)$", line):
            key_sroke = pattern.group(2)
            line = pattern.group(1).removeprefix("key.").replace(".key.", ".")

            # Setting mod value for all the vanila keystrokes to Minecraft
            if line.count(".") == 0:
                mod_name = "Minecraft"
                key_description = line.title()

            # If any line starts with key_gui instead of key_key, then the mod information is given before the underscore
            elif pattern := re.match("^gui.([a-z]+)_(.+)$", line):
                mod_name = pattern.group(1).title()
                key_description = pattern.group(2).replace("_", " ").title()

            # If any line starts with key_key instead of key_gui, then the mod information is given before the period
            elif pattern := re.match("^([a-z]+).(.+)$", line):
                if pattern.group(1) == "hotbar":
                    mod_name = "Minecraft"
                    key_description = line.replace(".", " ").title()
                else:
                    mod_name = pattern.group(1).title()
                    key_description = pattern.group(2).replace("_", " ").title()
            else:
                raise ValueError(line + "can't be converted")
            key_sroke = key_sroke.removeprefix("key.").removeprefix("keyboard.")

            # Making all imported keystrokes according to the text represented by lines inside key group in svg
            n = 1
            while f"{key_sroke}{n}" in text_id_incomplete:
                n += 1
            text_id_incomplete.update({f"{key_sroke}{n}": key_description})
            line_color_incomplete.update({f"{key_sroke}{n}": mod_name})
            mods.append(mod_name)
    mods = cleanup(mods)
    mod_color_dict = combine(mods, mod_colors)

    # Getting the Default layout

    namespace = "http://www.w3.org/2000/svg"
    encoding = "utf-8"
    try:
        response = requests.get(input_SVG_link)
    except:
        sys.exit("ConnectionError:\nAn error occured while downloading required SVG file. Make sure you have an active internet connection.\n")
    with open(input_file_name, "wb") as file:
        file.write(response.content)
    root = ET.parse(input_file_name).getroot()
    ET.register_namespace("", namespace)

    # Customizing the color scheme

    default_bg_color = "#363639"
    default_header_text_color = "#BCBEC0"
    default_customkeys_frame_color = "#1D191C"
    default_mouse_frame_color = "#1D191C"
    default_keyboard_frame_color = "#1D191C"
    default_mod_frame_color = "#221E22"
    default_key_color = "#221E22"
    default_line_color = "#BCBEC0"

    while True:
        print(
            f"""
This Chart follows this color scheme (Open https://en.wikipedia.org/wiki/Web_colors for help):

    [1]: {color('■',default_bg_color)} {default_bg_color}: Background
    [2]: {color('■',default_header_text_color)} {default_header_text_color}: Header Text
    [3]: {color('■',default_customkeys_frame_color)} {default_customkeys_frame_color}: Custom Keys Frame
    [4]: {color('■',default_mouse_frame_color)} {default_mouse_frame_color}: Mouse Frame
    [5]: {color('■',default_keyboard_frame_color)} {default_keyboard_frame_color}: Keyboard Frame
    [6]: {color('■',default_mod_frame_color)} {default_mod_frame_color}: Mods Section Frame
    [7]: {color('■',default_key_color)} {default_key_color}: Keyboard Key
    [8]: {color('■',default_line_color)} {default_line_color}: Default Text

If you want to customize it, Press a number corresponding to the Hex Code.
When you are happy just press [Enter] to go with it.
"""
        )
        match input("Enter your choice: "):
            case "1":
                default_bg_color = change_color(default_bg_color)
                continue
            case "2":
                default_header_text_color = change_color(default_header_text_color)
                continue
            case "3":
                default_customkeys_frame_color = change_color(default_customkeys_frame_color)
                continue
            case "4":
                default_mouse_frame_color = change_color(default_mouse_frame_color)
                continue
            case "5":
                default_keyboard_frame_color = change_color(default_keyboard_frame_color)
                continue
            case "6":
                default_mod_frame_color = change_color(default_mod_frame_color)
                continue
            case "7":
                default_key_color = change_color(default_key_color)
                continue
            case "8":
                default_line_color = change_color(default_line_color)
                continue
            case "":
                while True:
                    user_input = input(
                        """
Do you want this color scheme to be your final?
    [Enter]: Sure
    [0]: No, go back.

Enter your choice: """
                    )
                    match user_input:
                        case "":
                            break
                        case "0":
                            break
                        case _:
                            print("Invalid Input")
                            continue
                if user_input == "0":
                    continue
                break
            case _:
                print("Invalid Input, try again.")
                continue

    # Option to choose between SVG and PNG file

    while True:
        SVGorPNG = input("\nType 'png' or 'svg' to choose the format of the output file: ").lower()
        if SVGorPNG == "png":
            while True:
                scale_factor = input("Enter the value of Scale Factor and please don't enter too high number or press [Enter] to set the default value of 50.0: ")
                if scale_factor == "":
                    scale_factor = 50.0
                    break
                elif scale_factor.isdecimal():
                    break
                else:
                    continue
            scale_factor = float(scale_factor)
            break
        elif SVGorPNG == "svg":
            break
        else:
            print("Invalid Input")
            continue

    # Applying the color scheme

    root[0][0].attrib["fill"] = default_bg_color  # Setting bg color
    root[0][2][0].attrib["fill"] = default_mod_frame_color  # Setting mod frame color
    for rect_element in root[0][2].iter(f"{{{namespace}}}rect"):
        rect_element.attrib["fill"] = default_mod_frame_color  # Setting empty mod color
    root[0][4][0].attrib["fill"] = default_customkeys_frame_color  # Setting customkeys frame color
    root[0][5][0].attrib["fill"] = default_keyboard_frame_color  # Setting keyboard frame color
    for path_element in root[0][3][0].iter(f"{{{namespace}}}path"):
        if "(Stroke)" in path_element.attrib["id"]:
            path_element.attrib["fill"] = default_line_color  # Setting mouse stroke color
        else:
            path_element.attrib["fill"] = default_mouse_frame_color  # Setting mouse frame color
    for path_element in root[0][5].iter(f"{{{namespace}}}path"):
        path_element.attrib["fill"] = default_line_color  # Setting keyboard icons color
    for rect_element in root[0][4][1].iter(f"{{{namespace}}}rect"):
        rect_element.attrib["fill"] = default_key_color  # Setting key color in customkeys
    for rect_element in root[0][5][1].iter(f"{{{namespace}}}rect"):
        rect_element.attrib["fill"] = default_key_color  # Setting key color in keyboard
    for text_element in root[0][2].iter(f"{{{namespace}}}text"):
        text_element.attrib["fill"] = default_line_color  # Setting line color in mods section
    for text_element in root[0][3].iter(f"{{{namespace}}}text"):
        text_element.attrib["fill"] = default_line_color  # Setting line color in mouse
    for text_element in root[0][4].iter(f"{{{namespace}}}text"):
        text_element.attrib["fill"] = default_line_color  # Setting line color in customkeys
    for text_element in root[0][5].iter(f"{{{namespace}}}text"):
        text_element.attrib["fill"] = default_line_color  # Setting line color in keyboard
    for text_element in root[0][1].iter(f"{{{namespace}}}text"):
        text_element.attrib["fill"] = default_header_text_color  # Setting header text color in header

    # Finding and replacing the matched id of every line in svg with the keystroke values

    all_key_dict = {}
    all_mod_dict = {}
    modname_dict = {}
    n = 1
    for mod in mods:
        modname_dict.update({f"modname{n}": mod})
        n += 1
    for text_element in root.iter(f"{{{namespace}}}text"):
        text_id = text_element.get("id")
        if text_id[:-1] in key_list:
            all_key_dict.update({text_id: None})
            all_key_dict.update(text_id_incomplete)
            all_mod_dict.update({text_id: None})
            all_mod_dict.update(line_color_incomplete)

            if all_mod_dict[text_id] is not None:
                text_element.attrib["fill"] = mod_color_dict[all_mod_dict[text_id]]  # Returns the value of the mod
            text_element[0].text = all_key_dict[text_element.attrib["id"]]
        try:
            if text_id[:-1] == "modname" or text_id[:-2] == "modname":
                text_element[0].text = modname_dict[text_id]
        except:
            pass
    for text_element in root.iter(f"{{{namespace}}}text"):
        try:
            if (text_element.attrib["id"][:-1] == "modname" and text_element[0].text[:-1] == "modname") or (text_element.attrib["id"][:-2] == "modname" and text_element[0].text[:-2] == "modname"):
                text_element[0].text = None
        except:
            pass
    for rect_element in root.iter(f"{{{namespace}}}rect"):
        try:
            if rect_element.attrib["id"][:-1] == "modcolor" or rect_element.attrib["id"][:-2] == "modcolor":
                rect_element.attrib["fill"] = mod_color_dict[modname_dict[rect_element.attrib["id"].replace("modcolor", "modname")]]
        except:
            pass

    # Writing the modified svg file
    if SVGorPNG == "svg":
        with open(f"{output_file_name}.svg", "w", encoding=encoding) as file:
            file.write(ET.tostring(root, encoding="unicode"))
        os.remove(input_file_name)

    elif SVGorPNG == "png":
        with open(f"_{output_file_name}.svg", "w", encoding=encoding) as file:
            file.write(ET.tostring(root, encoding="unicode"))
        input_svg_file = f"_{output_file_name}.svg"
        output_png_file = f"{output_file_name}.png"
        cairosvg.svg2png(url=input_svg_file, write_to=output_png_file, output_width=scale_factor * cairosvg.svg2png(url=input_svg_file)[0], output_height=scale_factor * cairosvg.svg2png(url=input_svg_file)[1])
        os.remove(f"_{output_file_name}.svg")
        os.remove(input_file_name)


def cleanup(list):
    mods_ = []
    for mod in list:
        if mod not in mods_:
            mods_.append(mod)
    return mods_


def combine(list_1, list_2):
    combined_dict = {}
    for element1, element2 in zip(list_1, list_2):
        combined_dict[element1] = element2
    return combined_dict


def getUserPath(postPath):
    try:
        appdata_path = os.getenv("APPDATA")
        return os.path.join(appdata_path, postPath)
    except TypeError:
        sys.exit("Make sure this program runs on a Local Windows Computer.\nExiting the Program.")


def change_color(colorvar):
    while True:
        newcolorvar = input("Enter a color value in a format (#RRGGBB)\nOpen https://www.google.com/search?q=color+picker to generate one\nOr press [Enter] to go back: ").upper()
        if not newcolorvar:
            return colorvar
        try:
            color("■", newcolorvar)
            if not newcolorvar.startswith("#"):
                newcolorvar = f"#{newcolorvar}"
            return newcolorvar
        except ValueError:
            print("Invalid value, try again.")
            continue


if __name__ == "__main__":
    main()
