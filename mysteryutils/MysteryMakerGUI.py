import json
import random
import subprocess
import argparse
import os
import sys
import yaml
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from idlelib.tooltip import Hovertip
from mysteryutils.Definitions import *

def openOptionsGui(version_string: str, show_desktop_options: bool):
    def guiStartRandomize(*args):
        guiWindow.destroy()

    def guiCloseButton(*args):
        windowForceClosed.set("1")
        guiWindow.destroy()

    def guiResetModes(*args):
        goalMode.set(OPTION_DEFAULTS[GeneratorOptionNames.GOAL])
        goalRequiredRemains.set(str(OPTION_DEFAULTS[GeneratorOptionNames.GOALREMAINS]))
        goalFairyHuntSetSize.set(str(OPTION_DEFAULTS[GeneratorOptionNames.GOALFAIRYSET]))
        startDifficultyMode.set(OPTION_DEFAULTS[GeneratorOptionNames.STARTGEAR])
        startSongLayoutMode.set(OPTION_DEFAULTS[GeneratorOptionNames.SONGLAYOUT])
        startFreeOathMode.set("1" if OPTION_DEFAULTS[GeneratorOptionNames.FREEOATH] else "0")
        startFreeEponaMode.set("1" if OPTION_DEFAULTS[GeneratorOptionNames.FREEEPONA] else "0")
        startRandomItemMode.set(OPTION_DEFAULTS[GeneratorOptionNames.RANDOMITEM])
        startFDAnywhereMode.set(OPTION_DEFAULTS[GeneratorOptionNames.FDANYWHERE])
        startInteriorsERMode.set(OPTION_DEFAULTS[GeneratorOptionNames.ERINTERIOR])
        startGrottosERMode.set(OPTION_DEFAULTS[GeneratorOptionNames.ERGROTTO])
        startDungeonERMode.set(OPTION_DEFAULTS[GeneratorOptionNames.ERDUNGEON])
        startSmallKeysMode.set(OPTION_DEFAULTS[GeneratorOptionNames.SMALLKEYS])
        mainDensityMode.set(OPTION_DEFAULTS[GeneratorOptionNames.DENSITYMODE])
        densityCategoryMinimum.set(str(OPTION_DEFAULTS[GeneratorOptionNames.CATEGORYMINIMUM]))
        resetButton.state(["disabled"])

    def guiLoadWeightsFile(*args):
        loadPath = filedialog.askopenfilename(filetypes=[("Mystery Maker weights files", ".yml")])
        
        if loadPath != "":
            with open(loadPath, 'r') as loadedFile:
                weightsFileDict = yaml.safe_load(loadedFile)
                loadSettingsFromDict(weightsFileDict["options"])

    def guiSaveWeightsFile(*args):
        savePath = filedialog.asksaveasfilename(filetypes=[("Mystery Maker weights files", ".yml")])

        if savePath != "":
            weightsFileDict = dict()
            weightsFileDict["mystery_maker_version"] = version_string
            weightsFileDict["options"] = createSettingsDict()

            with open(savePath, "w") as fileToSave:
                yaml.dump(weightsFileDict, fileToSave)

    def browseForBaseSettingsFile(*args):
        baseSettingsFilePath.set(filedialog.askopenfilename())

    def browseForCommandLineExe(*args):
        mmrCommandLineExePath.set(filedialog.askopenfilename())

    def checkDefaults(*args):
        return (goalMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.GOAL] and
                goalRequiredRemains.get() == str(OPTION_DEFAULTS[GeneratorOptionNames.GOALREMAINS]) and
                goalFairyHuntSetSize.get() == str(OPTION_DEFAULTS[GeneratorOptionNames.GOALFAIRYSET]) and
                startDifficultyMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.STARTGEAR] and
                startFreeOathMode.get() == ("1" if OPTION_DEFAULTS[GeneratorOptionNames.FREEOATH] else "0") and
                startFreeEponaMode.get() == ("1" if OPTION_DEFAULTS[GeneratorOptionNames.FREEEPONA] else "0") and
                startRandomItemMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.RANDOMITEM] and
                startSongLayoutMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.SONGLAYOUT] and
                startFDAnywhereMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.FDANYWHERE] and
                startInteriorsERMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.ERINTERIOR] and
                startGrottosERMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.ERGROTTO] and
                startDungeonERMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.ERDUNGEON] and
                startSmallKeysMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.SMALLKEYS] and
                mainDensityMode.get() == OPTION_DEFAULTS[GeneratorOptionNames.DENSITYMODE] and
                densityCategoryMinimum.get() == str(OPTION_DEFAULTS[GeneratorOptionNames.CATEGORYMINIMUM]))
    
    def createSettingsDict(*args):
        cmSettings = dict()
        cmSettings[str(GeneratorOptionNames.GOAL)] = goalMode.get()
        cmSettings[str(GeneratorOptionNames.GOALREMAINS)] = int(goalRequiredRemains.get())
        cmSettings[str(GeneratorOptionNames.GOALFAIRYSET)] = int(goalFairyHuntSetSize.get())
        cmSettings[str(GeneratorOptionNames.STARTGEAR)] = startDifficultyMode.get()
        cmSettings[str(GeneratorOptionNames.SONGLAYOUT)] = startSongLayoutMode.get()
        cmSettings[str(GeneratorOptionNames.FREEOATH)] = (startFreeOathMode.get() == "1")
        cmSettings[str(GeneratorOptionNames.FREEEPONA)] = (startFreeEponaMode.get() == "1")
        cmSettings[str(GeneratorOptionNames.RANDOMITEM)] = startRandomItemMode.get()
        cmSettings[str(GeneratorOptionNames.FDANYWHERE)] = startFDAnywhereMode.get()
        cmSettings[str(GeneratorOptionNames.ERINTERIOR)] = startInteriorsERMode.get()
        cmSettings[str(GeneratorOptionNames.ERGROTTO)] = startGrottosERMode.get()
        cmSettings[str(GeneratorOptionNames.ERDUNGEON)] = startDungeonERMode.get()
        cmSettings[str(GeneratorOptionNames.SMALLKEYS)] = startSmallKeysMode.get()
        cmSettings[str(GeneratorOptionNames.DENSITYMODE)] = mainDensityMode.get()
        cmSettings[str(GeneratorOptionNames.CATEGORYMINIMUM)] = int(densityCategoryMinimum.get())
        
        return cmSettings
    
    def loadSettingsFromDict(modesDict):
        goalMode.set(modesDict[GeneratorOptionNames.GOAL])
        goalRequiredRemains.set(str(modesDict[GeneratorOptionNames.GOALREMAINS]))
        goalFairyHuntSetSize.set(str(modesDict[GeneratorOptionNames.GOALFAIRYSET]))
        startDifficultyMode.set(modesDict[GeneratorOptionNames.STARTGEAR])
        startSongLayoutMode.set(modesDict[GeneratorOptionNames.SONGLAYOUT])
        startFreeOathMode.set("1" if modesDict[GeneratorOptionNames.FREEOATH] else "0")
        startFreeEponaMode.set("1" if modesDict[GeneratorOptionNames.FREEEPONA] else "0")
        startRandomItemMode.set(modesDict[GeneratorOptionNames.RANDOMITEM])
        startFDAnywhereMode.set(modesDict[GeneratorOptionNames.FDANYWHERE])
        startInteriorsERMode.set(modesDict[GeneratorOptionNames.ERINTERIOR])
        startGrottosERMode.set(modesDict[GeneratorOptionNames.ERGROTTO])
        startDungeonERMode.set(modesDict[GeneratorOptionNames.ERDUNGEON])
        startSmallKeysMode.set(modesDict[GeneratorOptionNames.SMALLKEYS])
        mainDensityMode.set(modesDict[GeneratorOptionNames.DENSITYMODE])
        densityCategoryMinimum.set(str(modesDict[GeneratorOptionNames.CATEGORYMINIMUM]))

    def updateModeTabs(*args):                             
        if checkDefaults():
            resetButton.state(["disabled"])
        else:
            resetButton.state(["!disabled"])    

    guiWindow = Tk()
    guiWindow.title("MMR Mystery Maker " + version_string)

    mainframe = ttk.Frame(guiWindow, padding="8 8 4 8")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    guiWindow.columnconfigure(0, weight=1)
    guiWindow.rowconfigure(0, weight=1)

    windowForceClosed = StringVar(value="0")

    outputMode = StringVar(value=OutputModes.WEB)
    if (show_desktop_options):
        ttk.Label(mainframe, text="Output:").grid(column=1, row=2, sticky=E)
        outputMode_combo = ttk.Combobox(mainframe, textvariable=outputMode)
        outputMode_combo["values"] = (OutputModes.WEB, OutputModes.DESKTOP, OutputModes.DESKTOPANDSEED)
        outputMode_combo.grid(column=2, row=2, columnspan=1, sticky=(W, E))
        outputMode_combo.state(["readonly"])
        outputMode_tip = Hovertip(outputMode_combo, "The desired output. This release of Mystery Maker only supports MMR 2.0.")

    baseSettingsFilePath = StringVar(value="Mystery_Settings_base_v6_0_0.json")
    ttk.Label(mainframe, text="Custom base MMR settings file:").grid(column=1, row=3, sticky=E)
    baseSettingsFilePath_entry = ttk.Entry(mainframe, width=70, textvariable=baseSettingsFilePath)
    baseSettingsFilePath_entry.grid(column=2, row=3, columnspan=3, sticky=(W, E))
    baseSettingsFilePath_tip = Hovertip(baseSettingsFilePath_entry, "The MMR settings file that's copied and modified by Mystery Maker to make mystery settings files.\nThis file comes with Mystery Maker.")
    ttk.Button(mainframe, text="Browse...", command=browseForBaseSettingsFile).grid(column=5, row=3, sticky=W)

    mmrCommandLineExePath = StringVar(value="MMR.CLI.exe")
    if (show_desktop_options):
        ttk.Label(mainframe, text="Custom path to MMR.CLI.exe:").grid(column=1, row=4, sticky=E)
        mmrCommandLineExePath_entry = ttk.Entry(mainframe, width=70, textvariable=mmrCommandLineExePath)
        mmrCommandLineExePath_entry.grid(column=2, row=4, columnspan=3, sticky=(W, E))
        mmrCommandLineExePath_tip = Hovertip(mmrCommandLineExePath_entry, "The MMR command-line executable that makes playable seed files.\nChanging this should only be needed if you didn't install Mystery Maker in the same folder as MMR.")
        ttk.Button(mainframe, text="Browse...", command=browseForCommandLineExe).grid(column=5, row=4, sticky=W)

    numberToGenerate = StringVar(value="1")
    ttk.Label(mainframe, text="# of seeds:").grid(column=1, row=5, sticky=E)
    numberToGenerate_spinbox = ttk.Spinbox(mainframe, width=5, from_=1, to=100, textvariable=numberToGenerate)
    numberToGenerate_spinbox.grid(column=2, row=5, sticky=W)
    numberToGenerate_tip = Hovertip(numberToGenerate_spinbox, "Setting this above 1 will create many settings files at once, one at a time.")

    

    loadButton = ttk.Button(mainframe, text="Load Mystery YML...", command=guiLoadWeightsFile)
    loadButton.grid(column=2, row=6, sticky=E)
    loadButton_tip = Hovertip(loadButton, "Load Mystery Maker settings from a .yml file.")
    saveButton = ttk.Button(mainframe, text="Save Mystery YML...", command=guiSaveWeightsFile)
    saveButton.grid(column=3, row=6, sticky=E)
    saveButton_tip = Hovertip(saveButton, "Save Mystery Maker settings to a .yml file.")
    resetButton = ttk.Button(mainframe, text="Reset to Defaults", command=guiResetModes)
    resetButton.grid(column=4, row=6, sticky=E)
    resetButton.state(["disabled"])
    resetButton_tip = Hovertip(resetButton, "Resets all mode settings to default.")
    makeButton = ttk.Button(mainframe, text="Make Mystery", command=guiStartRandomize)
    makeButton.grid(column=5, row=6, sticky=W)
    makeButton_tip = Hovertip(makeButton, text="Generates one or more Mystery settings files and seeds with the specified options,\nplacing them in the 'output' directory.\nMystery Maker will close when finished.")

    #ttk.Label(mainframe, text="Generated settings and seeds will be placed in the 'output' directory.\nHover over options to display a tooltip with more information.", justify="center").grid(column=1, row=0, columnspan=5)

    
    
    

    modeTabs_notebook = ttk.Notebook(mainframe)
    modeTabGoalMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabGoalMode.grid(column=0, row=0, sticky=(N,W,S,E))
    modeTabStartMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabStartMode.grid(column=0, row=0, sticky=(N,W,S,E))    
    modeTabDensityMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabDensityMode.grid(column=0, row=0, sticky=(N,W,S,E)) 
    modeTabs_notebook.add(modeTabGoalMode, text="Goal")
    modeTabs_notebook.add(modeTabStartMode, text="Setup")
    modeTabs_notebook.add(modeTabDensityMode, text="Checks")
    modeTabs_notebook.grid(column=1, row=1, columnspan=5, sticky=(W, E))

    # Goal Mode pane
    goalRequiredRemains = StringVar(value=str(OPTION_DEFAULTS[GeneratorOptionNames.GOALREMAINS]))
    goalMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.GOAL])
    goalFairyHuntSetSize = StringVar(value=str(OPTION_DEFAULTS[GeneratorOptionNames.GOALFAIRYSET]))
    goalRequiredRemains.trace_add("write", updateModeTabs)
    goalMode.trace_add("write", updateModeTabs)
    goalFairyHuntSetSize.trace_add("write", updateModeTabs)

    goalRequiredRemains_label = ttk.Label(modeTabGoalMode, text="Required Remains: ")
    goalRequiredRemains_spinbox = ttk.Spinbox(modeTabGoalMode, width=3, from_=1, to=4, textvariable=goalRequiredRemains)
    goalRemainsOnBosses_radio = ttk.Radiobutton(modeTabGoalMode, text=GoalNames.REMAINSONBOSSES, variable=goalMode, value=GoalNames.REMAINSONBOSSES)
    goalRemainsShuffle_radio = ttk.Radiobutton(modeTabGoalMode, text=GoalNames.REMAINSSHUFFLE, variable=goalMode, value=GoalNames.REMAINSSHUFFLE)
    goalFairyHunt_radio = ttk.Radiobutton(modeTabGoalMode, text=GoalNames.FAIRYHUNT, variable=goalMode, value=GoalNames.FAIRYHUNT)
    goalFairyHuntSetSize_label = ttk.Label(modeTabGoalMode, text="Set Size: ")
    goalFairyHuntSetSize_spinbox = ttk.Spinbox(modeTabGoalMode, width=3, from_=0, to=15, textvariable=goalFairyHuntSetSize)
    goalMaskHunt_radio = ttk.Radiobutton(modeTabGoalMode, text=GoalNames.MASKHUNT, variable=goalMode, value=GoalNames.MASKHUNT)

    goalRequiredRemains_label.grid(column=1, row=1, sticky=(W, E))
    goalRequiredRemains_spinbox.grid(column=2, row=1, sticky=(W, E))
    goalRemainsOnBosses_radio.grid(column=1, row=2, sticky=(W, E))
    goalRemainsShuffle_radio.grid(column=1, row=3, sticky=(W, E))
    goalFairyHunt_radio.grid(column=1, row=4, sticky=(W, E))
    goalFairyHuntSetSize_label.grid(column=2, row=4, sticky=(W, E))
    goalFairyHuntSetSize_spinbox.grid(column=3, row=4, sticky=(W, E))
    goalMaskHunt_radio.grid(column=1, row=5, sticky=(W, E))
    
    goalRequiredRemains_tip = Hovertip(goalRequiredRemains_spinbox, "Remains needed to access the Moon, fight Majora, and receive the Oath hint.")
    goalRemainsOnBosses_tip = Hovertip(goalRemainsOnBosses_radio, "Remains on bosses. The conventional MMR win condition.")
    goalRemainsShuffle_tip = Hovertip(goalRemainsShuffle_radio, "Remains shuffled anywhere. C-Up at the Clock Tower door for region hints.")
    goalFairyHunt_tip = Hovertip(goalFairyHunt_radio, "Remains on Great Fairy Rewards. Visit the Fairy Fountains for region hints.")
    goalFairyHuntSetSize_tip = Hovertip(goalFairyHuntSetSize_spinbox, "Fairies of each color to be shuffled throughout Termina. Link starts with the remainder.")
    goalMaskHunt_tip = Hovertip(goalMaskHunt_radio, "Remains on bosses. To fight Majora, also find all 20 non-transformation masks! Visit the Moon Trial Gossips for mask hints.")

    # Start Modes pane
    startSongLayoutMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.SONGLAYOUT])
    startFreeOathMode = StringVar(value=("1" if OPTION_DEFAULTS[GeneratorOptionNames.FREEOATH] else "0"))
    startFreeEponaMode = StringVar(value=("0" if OPTION_DEFAULTS[GeneratorOptionNames.FREEEPONA] else "0"))
    startDifficultyMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.STARTGEAR])
    startRandomItemMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.RANDOMITEM])
    startFDAnywhereMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.FDANYWHERE])
    startInteriorsERMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.ERINTERIOR])
    startGrottosERMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.ERGROTTO])
    startDungeonERMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.ERDUNGEON])
    startSmallKeysMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.SMALLKEYS])

    startSongLayoutMode.trace_add("write", updateModeTabs)
    startFreeOathMode.trace_add("write", updateModeTabs)
    startFreeEponaMode.trace_add("write", updateModeTabs)
    startDifficultyMode.trace_add("write", updateModeTabs)
    startRandomItemMode.trace_add("write", updateModeTabs)
    startFDAnywhereMode.trace_add("write", updateModeTabs)
    startInteriorsERMode.trace_add("write", updateModeTabs)
    startGrottosERMode.trace_add("write", updateModeTabs)
    startDungeonERMode.trace_add("write", updateModeTabs)
    startSmallKeysMode.trace_add("write", updateModeTabs)
    
    startSongLayout_label = ttk.Label(modeTabStartMode, text="Song Layout:    ")
    startSongLayout_combo = ttk.Combobox(modeTabStartMode, textvariable=startSongLayoutMode)
    startSongLayout_combo["values"] = (ShuffleNames.GENERIC_RANDOM, ShuffleNames.SL_TRADITIONAL, ShuffleNames.SL_SANITY, ShuffleNames.SL_ALL)
    startSongLayout_combo.state(["readonly"])
    
    startFreeOath_check = ttk.Checkbutton(modeTabStartMode, text="Oath Start", variable=startFreeOathMode)
    
    startFreeEpona_check = ttk.Checkbutton(modeTabStartMode, text="Epona Start", variable=startFreeEponaMode)
    
    startDifficulty_label = ttk.Label(modeTabStartMode, text="Starting Basic Gear:    ")
    startDifficulty_combo = ttk.Combobox(modeTabStartMode, textvariable=startDifficultyMode)
    startDifficulty_combo["values"] = (ShuffleNames.SG_STRONG,
                                       ShuffleNames.SG_KOKIRI,
                                       ShuffleNames.SG_SWORDLESS,
                                       ShuffleNames.SG_FRAGILE)
    startDifficulty_combo.state(["readonly"])
    
    startRandomItem_label = ttk.Label(modeTabStartMode, text="Starting Random Item:    ")
    startRandomItem_combo = ttk.Combobox(modeTabStartMode, textvariable=startRandomItemMode, width=25)
    startRandomItem_combo["values"] = (ShuffleNames.GENERIC_OFF,
                                       ShuffleNames.GENERIC_RANDOM,
                                       ShuffleNames.ITEM_DEKU,
                                       ShuffleNames.ITEM_GORON,
                                       ShuffleNames.ITEM_ZORA,
                                       ShuffleNames.ITEM_FD,
                                       ShuffleNames.ITEM_BOW,
                                       ShuffleNames.ITEM_HOOK,
                                       ShuffleNames.ITEM_BOMBS,
                                       ShuffleNames.ITEM_BLAST,
                                       ShuffleNames.ITEM_WALLET,
                                       ShuffleNames.ITEM_BOTTLE,
                                       ShuffleNames.ITEM_BUNNY,
                                       ShuffleNames.ITEM_GFS)
    startRandomItem_combo.state(["readonly"])
    
    startFDAnywhere_label = ttk.Label(modeTabStartMode, text="FD Anywhere:    ")
    startFDAnywhere_combo = ttk.Combobox(modeTabStartMode, textvariable=startFDAnywhereMode, width=25)
    startFDAnywhere_combo["values"] = (ShuffleNames.GENERIC_OFF,
                                       ShuffleNames.FD_STARTING,
                                       ShuffleNames.GENERIC_RANDOM,
                                       ShuffleNames.FD_ON)
    startFDAnywhere_combo.state(["readonly"])
    
    startInteriorsER_combo = ttk.Combobox(modeTabStartMode, textvariable=startInteriorsERMode, width=25)
    startInteriorsER_label = ttk.Label(modeTabStartMode, text="Simple Interiors ER: ")
    startInteriorsER_combo["values"] = (ShuffleNames.GENERIC_OFF,
                                        ShuffleNames.GENERIC_RANDOM,
                                        ShuffleNames.GENERIC_SHUFFLED)
    startInteriorsER_combo.state(["readonly"])
    
    startGrottosER_combo = ttk.Combobox(modeTabStartMode, textvariable=startGrottosERMode, width=25)
    startGrottosER_label = ttk.Label(modeTabStartMode, text="Grottos ER: ")
    startGrottosER_combo["values"] = (ShuffleNames.GENERIC_OFF,
                                      ShuffleNames.GENERIC_RANDOM,
                                      ShuffleNames.GENERIC_SHUFFLED)
    startGrottosER_combo.state(["readonly"])
    
    startDungeonER_label = ttk.Label(modeTabStartMode, text="Dungeon ER: ")
    startDungeonER_combo = ttk.Combobox(modeTabStartMode, textvariable=startDungeonERMode, width=25)
    startDungeonER_combo["values"] = (ShuffleNames.GENERIC_OFF,
                                      ShuffleNames.GENERIC_RANDOM,
                                      ShuffleNames.GENERIC_SHUFFLED)
    startDungeonER_combo.state(["readonly"])

    startSmallKeys_label = ttk.Label(modeTabStartMode, text="Small Keys: ")
    startSmallKeys_combo = ttk.Combobox(modeTabStartMode, textvariable=startSmallKeysMode, width=25)
    startSmallKeys_combo["values"] = (ShuffleNames.GENERIC_OFF,
                                      ShuffleNames.GENERIC_RANDOM,
                                      ShuffleNames.SM_KEYS_TEMPLES)
    startSmallKeys_combo.state(["readonly"])  
    
    startSongLayout_label.grid(column=1, row=1, sticky=(W,E))
    startSongLayout_combo.grid(column=2, row=1, sticky=(W,E))
    startFreeOath_check.grid(column=1, row=2, sticky=(W,E))
    startFreeEpona_check.grid(column=2, row=2, sticky=(W,E))
    startDifficulty_label.grid(column=1, row=3, sticky=(W,E))
    startDifficulty_combo.grid(column=2, row=3, sticky=(W,E))
    startRandomItem_label.grid(column=1, row=4, sticky=(W,E))
    startRandomItem_combo.grid(column=2, row=4, sticky=(W,E))
    startFDAnywhere_label.grid(column=1, row=5, sticky=(W,E))
    startFDAnywhere_combo.grid(column=2, row=5, sticky=(W,E))
    startInteriorsER_label.grid(column=3, row=3, sticky=(W,E))
    startInteriorsER_combo.grid(column=4, row=3, sticky=(W,E))
    startGrottosER_label.grid(column=3, row=4, sticky=(W,E))
    startGrottosER_combo.grid(column=4, row=4, sticky=(W,E))
    startDungeonER_label.grid(column=3, row=5, sticky=(W,E))
    startDungeonER_combo.grid(column=4, row=5, sticky=(W,E))
    startSmallKeys_label.grid(column=1, row=6, sticky=(W,E))
    startSmallKeys_combo.grid(column=2, row=6, sticky=(W,E))
    
    startSongLayout_tip = Hovertip(startSongLayout_combo, "Choose a song layout.")
    startFreeOath_tip = Hovertip(startFreeOath_check, "Also start with Oath to Order. Boss Blue Warp is junked.")
    startFreeEpona_tip = Hovertip(startFreeEpona_check, "Also start with Epona's Song. Romani's Game is junked.")
    startDifficulty_tip = Hovertip(startDifficulty_combo, "Choose how the starting sword, shield, and hearts are handled.")
    startRandomItem_tip = Hovertip(startRandomItem_combo, "Choose a starting item option.")
    startFDAnywhere_tip = Hovertip(startFDAnywhere_combo, "Choose a Fierce Deity's Mask Anywhere option.")
    startInteriorsER_tip = Hovertip(startInteriorsER_combo, "Choose a Simple Interiors ER option.\nAffected entrances include uninverted STT.")
    startGrottosER_tip = Hovertip(startGrottosER_combo, "Choose a Grottos ER option.")
    startDungeonER_tip = Hovertip(startDungeonER_combo, "Choose a Dungeon ER option.\nAffected entrances are WFT, SHT, GBT, and inverted STT.")
    startSmallKeys_tip = Hovertip(startSmallKeys_combo, "Choose a Small Keys option.")

    # Density Modes pane
    mainDensityMode = StringVar(value=OPTION_DEFAULTS[GeneratorOptionNames.DENSITYMODE])
    densityCategoryMinimum = StringVar(value=str(OPTION_DEFAULTS[GeneratorOptionNames.CATEGORYMINIMUM]))
    mainDensityMode.trace_add("write", updateModeTabs)
    densityCategoryMinimum.trace_add("write", updateModeTabs)
    
    densityNormal_radio = ttk.Radiobutton(modeTabDensityMode, text="Normal", variable=mainDensityMode, value=DensityNames.NORMAL)
    densitySuper_radio = ttk.Radiobutton(modeTabDensityMode, text="Super Mystery", variable=mainDensityMode, value=DensityNames.SUPER)
    densityTotal_radio = ttk.Radiobutton(modeTabDensityMode, text="Total Mystery", variable=mainDensityMode, value=DensityNames.TOTAL)
    densityCategoryMinimum_label = ttk.Label(modeTabDensityMode, text="Category Minimum: ")
    densityCategoryMinimum_spinbox = ttk.Spinbox(modeTabDensityMode, width=3, from_=0, to=16, textvariable=densityCategoryMinimum)
    densityCategoryMinimum_spinbox.state(["readonly"])

    densityNormal_radio.grid(column=1, row=1, sticky=(W,E))
    densitySuper_radio.grid(column=2, row=1, sticky=(W,E))
    densityTotal_radio.grid(column=3, row=1, sticky=(W,E))
    densityCategoryMinimum_label.grid(column=1, row=2, sticky=(W,E))
    densityCategoryMinimum_spinbox.grid(column=2, row=2, sticky=(W))

    densityNormal_tip = Hovertip(densityNormal_radio, "Baseline appearance rates for all main categories.")
    densitySuper_tip = Hovertip(densitySuper_radio, "Dramatically increased appearance rates for all main categories.")
    densityTotal_tip = Hovertip(densityTotal_radio, "All main categories are fully in play!")
    densityCategoryMinimum_tip = Hovertip(densityCategoryMinimum_spinbox,"Modifies the minimum number of active categories.\nMystery Maker will reroll until this minimum is met.")

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    baseSettingsFilePath_entry.focus()
    guiWindow.protocol("WM_DELETE_WINDOW", guiCloseButton)
    guiWindow.bind("<Return>", guiStartRandomize)

    guiWindow.mainloop()
    customModesSettings = createSettingsDict()
    
    return [(windowForceClosed.get() == "1"),
            baseSettingsFilePath.get(),
            mmrCommandLineExePath.get(),
            (int)(numberToGenerate.get()),
            outputMode.get(),
            customModesSettings]
