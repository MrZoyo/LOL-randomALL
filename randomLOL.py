"""
RandomLOL
Author: MrZoyo
Date: 2024-03-20
----------------
Champions Number: 167
Latest released champion: Smolder
"""

import PySimpleGUI as sg
from PIL import Image
import io
import os
import random

version = 'v0.0.5'
required_folders = ['champions', 'default', 'items', 'positions', 'runes', 'spells']
current_language = "中文"
champions_count = len(os.listdir('champions'))

LANGUAGES = {
    "English": {
        "main_window_title": "Zoyo's LOL Random Generator",
        "random_button": "Random!",
        "player_count": "Player Count: ",
        "help_button": "Help Guide",
        "random_champion": "Random Champion",
        "random_position": "Random Position",
        "random_spells": "Random Spells",
        "random_runes": "Random Runes",
        "random_item": "Random Item",
        "no_jungle": "2-1-2 without Jungle",
        "author": "Author: MrZoyo",
        "version": f"Version: {version}",
        "champion_count": f"Champion Count: {champions_count}",
        "discord_invite": "Join BirdGaming Discord:",
        "discord_link": "https://discord.gg/birdgaming",
        "default_example": "Default Example",
        "close_button": "Close",
        "help_text": """This is a LOL random generator.
Click the Random button to generate random results.
Select the number of players, then click the Random button.
You can choose whether to randomize the champion, position, summoner spells, runes, and the first item.
If random position is selected, you can choose whether to exclude the jungle position (dual top lane).
[Common Uses]
1. Use in vs-Bot game and get the most kills as winner.
2. Use in a five-players team in match/rank game and get the MVP as winner.
For quality gaming, please do not use in match/rank games outside of a five-players team!!!""",
        "folder_error": "Folder {} does not exist or is empty, the files are corrupted.",
        "player": "Player",
        "random_results": "Random Results",
        "default_button": "Default Example",
    },

    "中文": {
        "main_window_title": "Zoyo的LOL随机生成器",
        "random_button": "随机!",
        "player_count": "玩家数量: ",
        "help_button": "帮助指南",
        "random_champion": "随机英雄",
        "random_position": "随机位置",
        "random_spells": "随机召唤师技能",
        "random_runes": "随机符文",
        "random_item": "随机第一件装备",
        "no_jungle": "212分路无打野",
        "author": "作者: MrZoyo",
        "version": f"版本: {version}",
        "champion_count": f"英雄数量: {champions_count}",
        "discord_invite": "加入小鸟游戏Discord:",
        "discord_link": "https://discord.gg/birdgaming",
        "default_example": "默认示例",
        "close_button": "关闭",
        "help_text": """这是一个LOL随机生成器。
点击随机按钮以生成随机结果。
选择玩家数量，然后点击随机按钮。
您可以选择是否随机化英雄、位置、召唤师技能、符文和第一件装备。
如果选择了随机位置，可以选择是否排除打野位置（双上路）。
【常见用途】
1. 在人机游戏中使用，看看谁的击杀更多。
2. 在匹配/排位游戏的五人队伍中使用，看看谁是MVP。
为了质量游戏，请不要在五人队伍外的匹配/排位游戏中使用！！！""",
        "folder_error": "文件夹 {} 不存在或为空，文件已损坏。",
        "player": "玩家",
        "random_results": "随机结果",
        "default_button": "默认示例",
    },

    "Deutsch": {
        "main_window_title": "Zoyos LOL Zufallsgenerator",
        "random_button": "Zufällig Generieren!",
        "player_count": "Spieleranzahl: ",
        "help_button": "Hilfe",
        "random_champion": "Zufälliger Champion",
        "random_position": "Zufällige Position",
        "random_spells": "Zufällige Beschwörerzauber",
        "random_runes": "Zufällige Runen",
        "random_item": "Zufälliger Gegenstand",
        "no_jungle": "2-1-2 ohne Dschungel",
        "author": "Autor: MrZoyo",
        "version": f"Version: {version}",
        "champion_count": f"Championanzahl: {champions_count}",
        "discord_invite": "Trete BirdGaming Discord bei:",
        "discord_link": "https://discord.gg/birdgaming",
        "default_example": "Standardbeispiel",
        "close_button": "Schließen",
        "help_text": """Dies ist ein Zufallsgenerator für LOL.
Klicken Sie auf die Schaltfläche Zufällig, um zufällige Ergebnisse zu generieren.
Wählen Sie die Anzahl der Spieler und klicken Sie dann auf die Schaltfläche Zufällig.
Sie können wählen, ob Sie den Champion, die Position, die Beschwörerzauber, die Runen und den ersten Gegenstand zufällig auswählen.
Wenn eine zufällige Position ausgewählt wird, können Sie wählen, ob die Dschungelposition ausgeschlossen werden soll (Doppel-Top-Lane).
[Verwendungen]
1. Verwenden Sie es im Vs-Bot-Spiel und erzielen Sie die meisten Kills als Gewinner.
2. Verwenden Sie es in einem Fünf-Spieler-Team im Match/Rang-Spiel und holen Sie sich den MVP als Gewinner.
Für Qualitäts-Spiele, bitte nicht in Match/Rang-Spielen außerhalb eines Fünf-Spieler-Teams verwenden!!!""",
        "folder_error": "Ordner {} existiert nicht oder ist leer, die Dateien sind beschädigt.",
        "player": "Spieler",
        "random_results": "Zufällige Ergebnisse",
        "default_button": "Standardbeispiel",
    },

}


def check_folders(language):
    for folder in required_folders:
        if not os.path.exists(folder) or not os.listdir(folder):
            sg.popup_error(LANGUAGES[language]["folder_error"].format(folder))
            exit()


def load_image(path, size=(100, 100)):
    """Adjust the image size and return the image data as bytes"""
    image = Image.open(path)
    image = image.resize(size, Image.Resampling.LANCZOS)
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    return bio.getvalue()


def create_random_results_window(language, num_results, values):
    previous_positions = []
    popup_layout = \
    [
        [sg.Text(LANGUAGES[language]["discord_invite"]),
         sg.InputText(LANGUAGES[language]["discord_link"], key='-READONLY-', readonly=True, enable_events=True)],
    ]
    for i in range(num_results):
        paths, previous_positions = random_selection(values, previous_positions)
        images_data = [load_image(path) for path in paths]
        popup_layout.extend([
            [sg.Text(f"{LANGUAGES[language]['player']} {i + 1}:")],
            [sg.Image(data=img) for img in images_data],
            [sg.HorizontalSeparator()]
        ])

    # Add a close button
    popup_layout.append([sg.Button(LANGUAGES[language]["close_button"], key='-CLOSE-')])
    return sg.Window(LANGUAGES[language]["random_results"].format(num_results), popup_layout)


def random_selection(values, previous_positions, default=False):
    paths = []
    if default:
        # Default random selection
        paths = [
            os.path.join('default', 'Zoyo.png'),
            os.path.join('default', 'sup.png'),
            os.path.join('default', 'PoroRecall.png'),
            os.path.join('default', 'PoroThrow.png'),
            os.path.join('default', 'Omnistone.png'),
            os.path.join('default', 'gold.png')
        ]
    else:
        # Handle "NO JUNGLE" logic
        if values['NO_JUNGLE']:
            available_positions = [pos for pos in os.listdir('positions') if
                                   pos != 'jng.png' and pos not in previous_positions]
        else:
            available_positions = [pos for pos in os.listdir('positions') if pos not in previous_positions]

        if values['RANDOM_POSITION']:
            position_filename = random.choice(available_positions) if available_positions else 'top.png'
        else:
            position_filename = 'default/nopos.png'

        # Other random logic (hero, rune, item)
        hero = random.choice(os.listdir('champions')) if values['RANDOM_CHAMPION'] else 'default/Zoyo.png'
        rune = random.choice(os.listdir('runes')) if values['RANDOM_RUNES'] else 'default/Omnistone.png'
        item = random.choice(os.listdir('items')) if values['RANDOM_ITEM'] else 'default/gold.png'

        spells = ['default/PoroRecall.png', 'default/PoroThrow.png']  # 默认召唤师技能
        if values['RANDOM_SPELLS']:
            spells = random.sample(os.listdir('spells'), 2)
            if position_filename == 'jng.png' and 'Smite.png' not in spells:
                spells[0] = 'Smite.png'

        previous_positions.append(position_filename)

        paths = [
            os.path.join('champions', hero),
            os.path.join('positions', position_filename),
            os.path.join('spells', spells[0]),
            os.path.join('spells', spells[1]),
            os.path.join('runes', rune),
            os.path.join('items', item)
        ]

    return paths, previous_positions


def create_window(language):
    layout = [
        [
            sg.Button(LANGUAGES[language]["random_button"], key="-Random-", size=(20, 2), font=("Helvetica", 30)),
            sg.Text(LANGUAGES[language]["player_count"]),
            sg.Combo([1, 2, 3, 4, 5], default_value=1, key='NUM_RESULTS'),
            sg.Button(LANGUAGES[language]["help_button"], key="-HELP-", size=(8, 1), font=("Helvetica", 10)),
        ],
        [
            sg.Checkbox(LANGUAGES[language]["random_champion"], default=True, key='RANDOM_CHAMPION'),
            sg.Checkbox(LANGUAGES[language]["random_position"], default=True, key='RANDOM_POSITION'),
            sg.Checkbox(LANGUAGES[language]["random_spells"], default=True, key='RANDOM_SPELLS'),
            sg.Checkbox(LANGUAGES[language]["random_runes"], default=True, key='RANDOM_RUNES'),
            sg.Checkbox(LANGUAGES[language]["random_item"], default=True, key='RANDOM_ITEM'),
            sg.Checkbox(LANGUAGES[language]["no_jungle"], default=False, key='NO_JUNGLE'),
        ],
        [
            sg.Image(data=load_image('./default/LANG.png', size=(30, 30))),
            sg.Combo(list(LANGUAGES.keys()), default_value=language, key="-LANGUAGE-", enable_events=True),
            sg.Text(LANGUAGES[language]["author"]), sg.Text(LANGUAGES[language]["version"]),
            sg.Text(LANGUAGES[language]["champion_count"].format(champions_count))
        ],
        [sg.Text(LANGUAGES[language]["discord_invite"]),
         sg.InputText(LANGUAGES[language]["discord_link"], key='-READONLY-', readonly=True, enable_events=True)]
    ]

    # Load and display default data
    default_paths, _ = random_selection(None, None, default=True)
    default_images = [load_image(path) for path in default_paths]
    layout.extend([
        [sg.Text(LANGUAGES[language]["default_button"]), *[sg.Image(data=img_data) for img_data in default_images]],
        [sg.HorizontalSeparator()]
    ])

    return sg.Window(LANGUAGES[language]["main_window_title"], layout)


def main():
    global current_language
    check_folders(current_language)
    window = create_window(current_language)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "-LANGUAGE-":
            current_language = values["-LANGUAGE-"]
            window.close()
            window = create_window(current_language)  # recreate the window with the new language

        elif event == "-HELP-":
            sg.popup(LANGUAGES[current_language]["help_text"], title=LANGUAGES[current_language]["help_button"])

        elif event == "-Random-":
            num_results = values['NUM_RESULTS']
            random_results_window = create_random_results_window(current_language, num_results, values)
            while True:
                event, values = random_results_window.read()
                if event in (sg.WIN_CLOSED, '-CLOSE-'):
                    break
            random_results_window.close()
        elif event == "-HELP-":
            sg.popup(LANGUAGES[current_language]["help_text"], title=LANGUAGES[current_language]["help_button"])

    window.close()


if __name__ == "__main__":
    main()
