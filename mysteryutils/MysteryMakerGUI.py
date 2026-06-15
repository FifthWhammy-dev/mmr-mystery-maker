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
from mysteryutils.Definitions import OutputModes

def openOptionsGui(version_string: str, show_desktop_options: bool):
    def guiStartRandomize(*args):
        guiWindow.destroy()

    def guiCloseButton(*args):
        windowForceClosed.set("1")
        guiWindow.destroy()

    def guiResetModes(*args):
        goalMode.set("Remains on Bosses")
        startDifficultyMode.set("Kokiri or Swordless")
        startSongLayoutMode.set("Any")
        startFreeOathMode.set("1")
        startFreeEponaMode.set("0")
        startRandomItemMode.set("Any")
        startFDAnywhereMode.set("Sometimes")
        startInteriorsERMode.set("Sometimes")
        startGrottosERMode.set("Sometimes")
        startDungeonERMode.set("Sometimes")
        mainDensityMode.set("Normal")
        densityCategoryMinimum.set("7")
        resetButton.state(["disabled"])

    def guiLoadWeightsFile(*args):
        loadPath = filedialog.askopenfilename(filetypes=[("Mystery Maker weights files", ".yml")])
        
        if loadPath != "":
            with open(loadPath, 'r') as loadedFile:
                weightsFileDict = yaml.safe_load(loadedFile)
                loadSettingsFromDict(weightsFileDict["modes"])

    def guiSaveWeightsFile(*args):
        savePath = filedialog.asksaveasfilename(filetypes=[("Mystery Maker weights files", ".yml")])

        if savePath != "":
            weightsFileDict = dict()
            weightsFileDict["mystery_maker_version"] = version_string
            weightsFileDict["modes"] = createSettingsDict()

            with open(savePath, "w") as fileToSave:
                yaml.dump(weightsFileDict, fileToSave)

    def browseForBaseSettingsFile(*args):
        baseSettingsFilePath.set(filedialog.askopenfilename())

    def browseForCommandLineExe(*args):
        mmrCommandLineExePath.set(filedialog.askopenfilename())

    def checkDefaults(*args):
        return (goalMode.get() == "Remains on Bosses" and
                startDifficultyMode.get() == "Kokiri or Swordless" and
                startFreeOathMode.get() == "1" and
                startFreeEponaMode.get() == "0" and
                startRandomItemMode.get() == "Any" and
                startSongLayoutMode.get() == "Random" and
                startFDAnywhereMode.get() == "Sometimes" and
                startInteriorsERMode.get() == "Sometimes" and
                startGrottosERMode.get() == "Sometimes" and
                startDungeonERMode.get() == "Sometimes" and
                mainDensityMode.get() == "Normal" and
                densityCategoryMinimum.get() == "7")
    
    def createSettingsDict(*args):
        cmSettings = dict()
        cmSettings["Goal Mode"] = goalMode.get()
        cmSettings["Start Mode"] = startDifficultyMode.get()
        cmSettings["Song Layout"] = startSongLayoutMode.get()
        cmSettings["Free Oath"] = startFreeOathMode.get()
        cmSettings["Free Epona"] = startFreeEponaMode.get()
        cmSettings["Random Item Mode"] = startRandomItemMode.get()
        cmSettings["FD Anywhere Mode"] = startFDAnywhereMode.get()
        cmSettings["Simple Interiors ER"] = startInteriorsERMode.get()
        cmSettings["Grottos ER"] = startGrottosERMode.get()
        cmSettings["Dungeon ER"] = startDungeonERMode.get()
        cmSettings["Main Density Mode"] = mainDensityMode.get()
        cmSettings["Category Minimum"] = int(densityCategoryMinimum.get())
        
        return cmSettings
    
    def loadSettingsFromDict(modesDict):
        goalMode.set(modesDict["Goal Mode"])
        startDifficultyMode.set(modesDict["Start Mode"])
        startSongLayoutMode.set(modesDict["Song Layout"])
        startFreeOathMode.set(modesDict["Free Oath"])
        startFreeEponaMode.set(modesDict["Free Epona"])
        startRandomItemMode.set(modesDict["Random Item Mode"])
        startFDAnywhereMode.set(modesDict["FD Anywhere Mode"])
        startInteriorsERMode.set(modesDict["Simple Interiors ER"])
        startGrottosERMode.set(modesDict["Grottos ER"])
        startDungeonERMode.set(modesDict["Dungeon ER"])
        mainDensityMode.set(modesDict["Main Density Mode"])
        densityCategoryMinimum.set(str(modesDict["Category Minimum"]))

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
    baseSettingsFilePath_tip = Hovertip(baseSettingsFilePath_entry, "The MMR settings file that's copied and modified by Mystery Maker to make mystery seeds.\nThis file comes with Mystery Maker.")
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
    numberToGenerate_tip = Hovertip(numberToGenerate_spinbox, "Setting this above 1 will create many settings/seeds at once, one at a time.")

    

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
    goalRequiredRemains = StringVar(value="4")
    goalMode = StringVar(value="Remains on Bosses")
    goalFairyHuntSetSize = StringVar(value="5")
    goalRequiredRemains.trace_add("write", updateModeTabs)
    goalMode.trace_add("write", updateModeTabs)
    goalFairyHuntSetSize.trace_add("write", updateModeTabs)

    goalRequiredRemains_label = ttk.Label(modeTabGoalMode, text="Required Remains: ")
    goalRequiredRemains_spinbox = ttk.Spinbox(modeTabGoalMode, width=3, from_=1, to=4, textvariable=goalRequiredRemains)
    goalRemainsOnBosses_radio = ttk.Radiobutton(modeTabGoalMode, text="Remains on Bosses", variable=goalMode, value="Remains on Bosses")
    goalRemainsShuffle_radio = ttk.Radiobutton(modeTabGoalMode, text="Remains Shuffle", variable=goalMode, value="Remains Shuffle")
    goalFairyHunt_radio = ttk.Radiobutton(modeTabGoalMode, text="Fairy Hunt", variable=goalMode, value="Fairy Hunt")
    goalFairyHuntSetSize_label = ttk.Label(modeTabGoalMode, text="Set Size: ")
    goalFairyHuntSetSize_spinbox = ttk.Spinbox(modeTabGoalMode, width=3, from_=0, to=15, textvariable=goalFairyHuntSetSize)
    goalMaskHunt_radio = ttk.Radiobutton(modeTabGoalMode, text="Mask Hunt", variable=goalMode, value="Mask Hunt")

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
    startSongLayoutMode = StringVar(value="Random")
    startFreeOathMode = StringVar(value="1")
    startFreeEponaMode = StringVar(value="0")
    startDifficultyMode = StringVar(value="Kokiri or Swordless")
    startRandomItemMode = StringVar(value="Any")
    startFDAnywhereMode = StringVar(value="Sometimes")
    startInteriorsERMode = StringVar(value="Sometimes")
    startGrottosERMode = StringVar(value="Sometimes")
    startDungeonERMode = StringVar(value="Sometimes")
    startSongLayoutMode.trace_add("write", updateModeTabs)
    startFreeOathMode.trace_add("write", updateModeTabs)
    startFreeEponaMode.trace_add("write", updateModeTabs)
    startDifficultyMode.trace_add("write", updateModeTabs)
    startRandomItemMode.trace_add("write", updateModeTabs)
    startFDAnywhereMode.trace_add("write", updateModeTabs)
    startInteriorsERMode.trace_add("write", updateModeTabs)
    startGrottosERMode.trace_add("write", updateModeTabs)
    startDungeonERMode.trace_add("write", updateModeTabs)
    startSongLayout_label = ttk.Label(modeTabStartMode, text="Song Layout:    ")
    startSongLayout_combo = ttk.Combobox(modeTabStartMode, textvariable=startSongLayoutMode)
    startSongLayout_combo["values"] = ("Random", "Traditional", "Songsanity", "Start with All")
    startSongLayout_combo.state(["readonly"])
    startFreeOath_check = ttk.Checkbutton(modeTabStartMode, text="Oath Start", variable=startFreeOathMode)
    startFreeEpona_check = ttk.Checkbutton(modeTabStartMode, text="Epona Start", variable=startFreeEponaMode)
    startDifficulty_label = ttk.Label(modeTabStartMode, text="Starting Basic Gear:    ")
    startDifficulty_combo = ttk.Combobox(modeTabStartMode, textvariable=startDifficultyMode)
    startDifficulty_combo["values"] = ("Strong", "Kokiri", "Kokiri or Swordless", "Swordless", "Fragile")
    startDifficulty_combo.state(["readonly"])
    startRandomItem_label = ttk.Label(modeTabStartMode, text="Starting Random Item:    ")
    startRandomItem_combo = ttk.Combobox(modeTabStartMode, textvariable=startRandomItemMode, width=25)
    startRandomItem_combo["values"] = ("Off",
                                       "Any",
                                       "Any Transformation Mask",
                                       "Any Non-Transformation",
                                       "Any Non-Sword",
                                       "Deku Mask",
                                       "Goron Mask",
                                       "Zora Mask",
                                       "Fierce Deity's Mask",
                                       "Bow",
                                       "Hookshot",
                                       "Bomb Bag",
                                       "Blast Mask",
                                       "Adult's Wallet",
                                       "Empty Bottle (Dampe's)",
                                       "Bunny Hood",
                                       "Great Fairy's Sword")
    startRandomItem_combo.state(["readonly"])
    startFDAnywhere_label = ttk.Label(modeTabStartMode, text="FD Anywhere:    ")
    startFDAnywhere_combo = ttk.Combobox(modeTabStartMode, textvariable=startFDAnywhereMode, width=25)
    startFDAnywhere_combo["values"] = ("Off and Unshuffled", "Off", "Only When Starting", "Sometimes", "Always")
    startFDAnywhere_combo.state(["readonly"])
    startInteriorsER_combo = ttk.Combobox(modeTabStartMode, textvariable=startInteriorsERMode, width=25)
    startInteriorsER_label = ttk.Label(modeTabStartMode, text="Simple Interiors ER: ")
    startInteriorsER_combo["values"] = ("Off", "Sometimes", "Always")
    startInteriorsER_combo.state(["readonly"])
    startGrottosER_combo = ttk.Combobox(modeTabStartMode, textvariable=startGrottosERMode, width=25)
    startGrottosER_label = ttk.Label(modeTabStartMode, text="Grottos ER: ")
    startGrottosER_combo["values"] = ("Off", "Sometimes", "Always")
    startGrottosER_combo.state(["readonly"])
    startDungeonER_label = ttk.Label(modeTabStartMode, text="Dungeon ER: ")
    startDungeonER_combo = ttk.Combobox(modeTabStartMode, textvariable=startDungeonERMode, width=25)
    startDungeonER_combo["values"] = ("Off", "Sometimes", "Always")
    startDungeonER_combo.state(["readonly"])    
    
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
    startSongLayout_tip = Hovertip(startSongLayout_combo, "Choose a song layout.")
    startFreeOath_tip = Hovertip(startFreeOath_check, "Also start with Oath to Order. Boss Blue Warp is junked.")
    startFreeEpona_tip = Hovertip(startFreeEpona_check, "Also start with Epona's Song. Romani's Game is junked.")
    startDifficulty_tip = Hovertip(startDifficulty_combo, "Choose how the starting sword, shield, and hearts are handled.")
    startRandomItem_tip = Hovertip(startRandomItem_combo, "Choose a starting random item mode, or guarantee a specific starting item.")
    startFDAnywhere_tip = Hovertip(startFDAnywhere_combo, "Choose a Fierce Deity's Mask Anywhere mode.")
    startInteriorsER_tip = Hovertip(startDungeonER_combo, "Choose a Simple Interiors ER option.\nAffected entrances include uninverted STT.")
    startGrottosER_tip = Hovertip(startDungeonER_combo, "Choose a Grottos ER option.")
    startDungeonER_tip = Hovertip(startDungeonER_combo, "Choose a Dungeon ER option.\nAffected entrances are WFT, SHT, GBT, and inverted STT.")

    # Density Modes pane
    mainDensityMode = StringVar(value="Normal")
    densityCategoryMinimum = StringVar(value="7")
    mainDensityMode.trace_add("write", updateModeTabs)
    densityCategoryMinimum.trace_add("write", updateModeTabs)
    
    densityNormal_radio = ttk.Radiobutton(modeTabDensityMode, text="Normal", variable=mainDensityMode, value="Normal")
    densitySuper_radio = ttk.Radiobutton(modeTabDensityMode, text="Super Mystery", variable=mainDensityMode, value="Super")
    densityCategoryMinimum_label = ttk.Label(modeTabDensityMode, text="Category Minimum: ")
    densityCategoryMinimum_spinbox = ttk.Spinbox(modeTabDensityMode, width=3, from_=0, to=14, textvariable=densityCategoryMinimum)
    densityCategoryMinimum_spinbox.state(["readonly"])

    densityNormal_radio.grid(column=1, row=1, sticky=(W,E))
    densitySuper_radio.grid(column=2, row=1, sticky=(W,E))
    densityCategoryMinimum_label.grid(column=1, row=2, sticky=(W,E))
    densityCategoryMinimum_spinbox.grid(column=2, row=2, sticky=(W))

    densityNormal_tip = Hovertip(densityNormal_radio, "Baseline appearance rates for all categories.")
    densitySuper_tip = Hovertip(densitySuper_radio,"Dramatically increased appearance rates for all categories!")
    densityCategoryMinimum_tip = Hovertip(densityCategoryMinimum_spinbox,"Modifies the minimum number of active categories.\nMystery Maker will reroll until this minimum is met.")
    
    # Extra Modes pane

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
