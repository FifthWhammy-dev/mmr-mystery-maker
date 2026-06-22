import json
import random
import subprocess
import argparse
import os
import sys
import yaml
from datetime import datetime, timezone
from mysteryutils.MysteryMakerGUI import openOptionsGui
from mysteryutils.Definitions import *
from mysteryutils.CategoryListGen import CreateSetupCategoryList, CreateMainCategoryList, ApplyWeights
from mysteryutils.ListStringUtils import *
from mysteryutils.SettingsFile import SettingsFile, DesktopSettingsFile, WebSettingsFile
from mysteryutils.MysterySeed import MysterySeed

argParser = argparse.ArgumentParser(description="Randomly generates Mystery settings files for MMR.")
argParser.add_argument("-n", dest="numberOfSettingsFiles",type=int,default=1,
                    help="create multiple settings/seeds at once")
argParser.add_argument("-i", "--input", dest="inputFile",default="Mystery_Settings_base_v5_1_1.json",
                    help="base MMR settings file")
argParser.add_argument("-r", "--randomizer-exe", dest="randomizerExe",default="MMR.CLI.exe",
                    help="custom MMR command-line executable, used only with --desktop-output")
argParser.add_argument("-w", "--weights-file", dest="weightsFile",default="0",
                    help="custom Mystery Maker weights file")   
argParser.add_argument("-d", "--desktop-output", dest="desktopOutput", action="store_true",
                    help="generate desktop settings instead of web settings, then make a seed with them using a local MMR CLI executable")
argParser.add_argument("--desktop-output-no-seed", dest="desktopOutputNoSeed", action="store_true",
                    help="generate desktop settings instead of web settings, but only make settings files")
argParser.add_argument("--desktop-support-gui", dest="guiDesktopMode", action="store_true",
                    help="open the GUI, but with extra options for desktop MMR")
argParser.add_argument("--version", dest="showVersion", action="store_true",
                    help="print version number and exit")
args = argParser.parse_args()

if (args.showVersion):
    print("MMR Mystery Maker", MYSTERY_MAKER_VERSION)
    sys.exit()

optionSettingsFile = args.inputFile
optionRandomizerExe = args.randomizerExe
optionWeightsFile = args.weightsFile
optionOutputCount = args.numberOfSettingsFiles
optionOutputMode = OutputModes.DESKTOPANDSEED if args.desktopOutput else (OutputModes.DESKTOP if args.desktopOutputNoSeed else OutputModes.WEB)
optionCustomModes = OPTION_DEFAULTS
if optionWeightsFile != "0":
    with open(optionWeightsFile, 'r') as loadedWeightsFile:
        weightsFileDict = yaml.safe_load(loadedWeightsFile)
        optionCustomModes = weightsFileDict["modes"]

if (len(sys.argv) == 1 or (len(sys.argv) == 2 and args.guiDesktopMode)):
    guiResults = openOptionsGui(MYSTERY_MAKER_VERSION, args.guiDesktopMode)
    if (guiResults[0]):
        sys.exit()
    optionSettingsFile = guiResults[1]
    optionRandomizerExe = guiResults[2]
    optionOutputCount = guiResults[3]
    optionOutputMode = guiResults[4]
    optionCustomModes = guiResults[5]

try:
    os.makedirs("output")
except FileExistsError:
    pass

for i in range(optionOutputCount):
    print(i)
    dest = "web" if optionOutputMode == OutputModes.WEB else "desktop"
    d = datetime.now(timezone.utc)
    timestamp = f"{d.year}-{d.month:02}-{d.day:02}T{d.hour:02}-{d.minute:02}-{d.second:02}"
    if optionOutputCount > 1:
        timestamp += f"S{i+1:0{len(str(optionOutputCount))}}"
    outputFilename = "output\\Mystery_" + MYSTERY_MAKER_VERSION_FILENAME + "_" + dest + "_" + timestamp + ".json"
    seedSettings: SettingsFile
    if (optionOutputMode == OutputModes.WEB):
        seedSettings = WebSettingsFile(optionSettingsFile, outputFilename)
    else:
        seedSettings = DesktopSettingsFile(optionSettingsFile, outputFilename)

    seed = MysterySeed(seedSettings, optionCustomModes)
    seed.build()
    seed.write()
    seed.spoil()
    
    if (optionOutputMode == OutputModes.DESKTOPANDSEED):
        mmrcl = optionRandomizerExe + " -outputpatch -spoiler -settings " + outputFilename
        subprocess.call(mmrcl)