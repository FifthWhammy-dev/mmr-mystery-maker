# MMR Mystery Maker

## About 
MMR Mystery Maker is a Python script (and now standalone .exe, thanks to [PyInstaller](https://pyinstaller.org/en/stable/index.html)) that generates semi-random "Mystery" settings files for [Majora's Mask Randomizer v2.0.0](https://github.com/ZoeyZolotova/mm-rando). 

See the [Mystery Settings Document](https://docs.google.com/document/d/1nmUfmgIVg_QE0gBXbzKHuJvbSApMy80OQ81A-kJuE6Y/edit?usp=sharing) and the [Categories and Hints spreadsheet](https://docs.google.com/spreadsheets/d/1KC0fWYnIos2LB1rBzdjzHxXCn45uNtAR96nkvUDphmU/edit?usp=sharing) to learn more about Mystery settings. See the [changelog.md](https://github.com/FifthWhammy-dev/mmr-mystery-maker/blob/main/changelog.md) file for patch notes on the core settings.

The Mystery Maker script uses hard-coded categories and weights, applying them to an input JSON file to generate a new settings file which can be uploaded to the [MMR 2.0 web generator](mmrandomizer.com).

## How to Use
- Download the latest Mystery Maker release from the Releases section.
- Extract MysteryMaker.exe and the .json files to any folder.
- Run MysteryMaker.exe and an options dialog will open.
- Click "Make Mystery" to generate a settings file! By default, the core settings from the Mystery Settings Document are applied, but options are provided in the GUI if you wish.
- When finished, check the "output" directory for your settings file and Mystery spoiler.
- Use the settings file in the MMR web generator using the Import and Load buttons.

### Command Line Options
Command-line operation is available. Using any command-line option below will bypass the options GUI and go straight to generation.

Current options (and their command-line equivalents):

**Custom Base MMR Settings File (-i FILE, --input FILE)**: use FILE as the base settings file

**Number of Seeds (-n N)**: generate N seeds at a time; -n 5 would generate 5 seeds

**Custom Weights File (-w FILE, --weights-file FILE)**: load a .yml weights file to use different Mystery Maker generator options via the command line

**--version**: command line only--print the current Mystery Maker version number and exit

**--help**: command line only--print these command line options and exit

## Outro
For related info and discussion, and to share feedback, visit the #mystery-discussion channel of the MMR Community Discord: https://discord.gg/7jBRhhJ

And if you wish to package the script into an .exe yourself:

- Install Python (https://www.python.org) and then use Python's pip to install [PyInstaller](https://pyinstaller.org/en/stable/installation.html) and [PyYAML](https://pypi.org/project/PyYAML/).
- Open a PowerShell window or other shell in the same directory as MysteryMaker.py and run:  pyinstaller --onefile .\MysteryMaker.py

Enjoy!

FifthWhammy
