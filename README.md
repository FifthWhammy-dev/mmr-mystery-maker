# MMR Mystery Maker

## About 
MMR Mystery Maker is a Python script (and now standalone .exe, thanks to [PyInstaller](https://pyinstaller.org/en/stable/index.html)) that generates semi-random "Mystery" settings files for [Majora's Mask Randomizer v1.16.0.12](https://github.com/ZoeyZolotova/mm-rando). 

As of 12/26/2025, Version 5.1 is out! See the [Mystery Settings Document](https://docs.google.com/document/d/1Sty6gbtnH1n4etKx2ejit19MYtsMIVa08kPXt5aJQNY/edit?usp=sharing) and the [Category Weights and Hints spreadsheet](https://docs.google.com/spreadsheets/d/1chR1HI84BfIALG8FryDtHH8DhKTiASyuibOYxcwmvag/edit?usp=sharing) to learn more about of the Mystery settings. See the [changelog.md](https://github.com/FifthWhammy-dev/mmr-mystery-maker/blob/main/changelog.md) file for patch notes on the core settings, plus a listing of new generator options.

The Mystery Maker script uses hard-coded categories and weights, applying them to an input JSON file to generate a new settings file. By default, the script then calls MMR.CLI.exe to generate a new seed using the settings.

## How to Use
- Download the latest Mystery Maker release from the Releases section.
- Extract MysteryMaker.exe and the .json files to the same folder as your MMR install. (You can run Mystery Maker elsewhere, but will have to manually select the base settings file and MMR.CLI.exe.)
- Ensure your desired outputs are on in your MMR settings ("Patch .mmr" is recommended at minimum!), as that's how MMR.CLI.exe decides what to output. MMR will automatically apply your current outputs and cosmetic settings to seeds it generates; there's no need to manually save or create a new settings file.
- Run MysteryMaker.exe and an options dialog will open. If it's in the same directory as MMR, you can just click Randomize in the options dialog to generate the seed.
- When finished, check the "output" directory for your seed and Mystery spoiler.

As of v4.1, many new modes are all selected in Mystery Maker itself! There's only one base settings file now.

### Command Line Options
Command-line operation is available. Using any command-line option will bypass the options GUI and go straight to generation.

New in v5.1: command-line operation can now use custom mode options from the GUI! To do this, save a .yml file from the Mystery Maker GUI with your desired generator options, then specify that file using **-w** on the command line.

Current options (and their command-line equivalents):

**Custom Base MMR Settings File (-i FILE, --input FILE)**: use FILE as the base settings file

**Only Make Settings File (--settings-only)**: only generate a settings JSON and Mystery spoiler; don't make a seed using MMR.CLI.exe afterward

**Number of Seeds (-n N)**: generate N seeds at a time; -n 5 would generate 5 seeds

**Custom Path to MMR.CLI.exe (-r EXE, --randomizer-exe EXE)**: use EXE to create a seed after making the Mystery settings (useful if your MMR.CLI.exe in a different directory)

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
