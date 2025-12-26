import json
import random
import subprocess
import argparse
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from idlelib.tooltip import Hovertip

def openOptionsGui(version_string):
    def guiStartRandomize(*args):
        guiWindow.destroy()

    def guiCloseButton(*args):
        windowForceClosed.set("1")
        guiWindow.destroy()

    def guiResetModes(*args):
        goalMode.set("No Blitz")
        goalDirectToCredits.set("0")
        goalEarlyMoonRemains.set("1")
        goalBlitzRemainsCount.set("0")
        startDifficultyMode.set("Default")
        startSongLayoutMode.set("Any (Default)")
        startAllMoonTrialsMode.set("0")
        startRandomItemMode.set("Any (Default)")
        startFDAnywhereMode.set("Sometimes (Default)")
        startDungeonERMode.set("Sometimes (Default)")
        startBossKeysMode.set("Off (Default)")
        startSmallKeysMode.set("Sometimes (Default)")
        mainDensityMode.set("Normal")
        densityCategoryMinimum.set("6")
        densityNoCT.set("0")
        densityNoPT.set("0")
        densityMapCompassMode.set("0")
        densityPotsanityMode.set("Default")
        densityScoopsanityMode.set("Default")
        densityScrambledEggsMode.set("0")
        densityStubbornPrincessMode.set("0")
        extraNoIcelessFDLogicMode.set("0")
        extraICMode.set("0")
        extraSunsSongMode.set("0")
        resetButton.state(["disabled"])

    def browseForBaseSettingsFile(*args):
        baseSettingsFilePath.set(filedialog.askopenfilename())

    def browseForCommandLineExe(*args):
        mmrCommandLineExePath.set(filedialog.askopenfilename())

    def checkDefaults(*args):
        return (goalMode.get() == "No Blitz" and
                goalDirectToCredits.get() == "0" and
                goalEarlyMoonRemains.get() == "1" and
                goalBlitzRemainsCount.get() == "0" and
                startDifficultyMode.get() == "Default" and
                startRandomItemMode.get() == "Any (Default)" and
                startSongLayoutMode.get() == "Any (Default)" and
                startAllMoonTrialsMode.get() == "0" and
                startFDAnywhereMode.get() == "Sometimes (Default)" and
                startDungeonERMode.get() == "Sometimes (Default)" and
                startBossKeysMode.get() == "Off (Default)" and
                startSmallKeysMode.get() == "Sometimes (Default)" and
                mainDensityMode.get() == "Normal" and
                densityCategoryMinimum.get() == "6" and
                densityNoCT.get() == "0" and
                densityNoPT.get() == "0" and
                densityMapCompassMode.get() == "0" and
                densityPotsanityMode.get() == "Default" and
                densityScoopsanityMode.get() == "Default" and
                densityScrambledEggsMode.get() == "0" and
                densityStubbornPrincessMode.get() == "0" and
                extraNoIcelessFDLogicMode.get() == "0" and
                extraICMode.get() == "0" and
                extraSunsSongMode.get() == "0")
    
    def updateModeTabs(*args):
        goalLongGoal_combo.state(["!disabled"] if goalMode.get() == "Long Goal" else ["disabled"])
                      
        if startDifficultyMode.get() == "Cruel":
            startRandomItemMode.set("Off")
            startRandomItem_combo.state(["disabled"])
            startFDAnywhereMode.set("Off")
            startFDAnywhere_combo.state(["disabled"])
        else:
            startRandomItem_combo.state(["!disabled"])
            startFDAnywhere_combo.state(["!disabled"])
        
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

    baseSettingsFilePath = StringVar(value="Mystery_Settings_base_v5.json")
    baseSettingsFilePath_entry = ttk.Entry(mainframe, width=70, textvariable=baseSettingsFilePath)
    baseSettingsFilePath_entry.grid(column=2, row=2, sticky=(W, E))
    baseSettingsFilePath_tip = Hovertip(baseSettingsFilePath_entry, "The MMR settings file that's copied and modified\nby Mystery Maker to make mystery seeds.\nThe Mystery_Settings_base_v5.json file comes with Mystery Maker.")

    mmrCommandLineExePath = StringVar(value="MMR.CLI.exe")
    mmrCommandLineExePath_entry = ttk.Entry(mainframe, width=70, textvariable=mmrCommandLineExePath)
    mmrCommandLineExePath_entry.grid(column=2, row=3, sticky=(W, E))
    mmrCommandLineExePath_tip = Hovertip(mmrCommandLineExePath_entry, "The MMR command-line executable that makes playable seed files.\nChanging this should only be needed if you didn't install\nMystery Maker in the same folder as MMR.")

    numberToGenerate = StringVar(value="1")
    numberToGenerate_spinbox = ttk.Spinbox(mainframe, width=5, from_=1, to=100, textvariable=numberToGenerate)
    numberToGenerate_spinbox.grid(column=2, row=4, sticky=W)
    numberToGenerate_tip = Hovertip(numberToGenerate_spinbox, "Setting this above 1 will create many settings/seeds at once, one at a time.")

    makeSettingsOnly = StringVar(value="0")
    makeSettingsOnly_checkbutton = ttk.Checkbutton(mainframe, text="Only make settings file", variable=makeSettingsOnly)
    makeSettingsOnly_checkbutton.grid(column=1, row=5, sticky=E)
    makeSettingsOnly_tip = Hovertip(makeSettingsOnly_checkbutton, "When checked, Mystery Maker only generates a .json file\nwhich can be loaded manually in MMR to make a playable seed.")

    ttk.Button(mainframe, text="Browse...", command=browseForBaseSettingsFile).grid(column=3, row=2, sticky=W)
    ttk.Button(mainframe, text="Browse...", command=browseForCommandLineExe).grid(column=3, row=3, sticky=W)
    resetButton = ttk.Button(mainframe, text="Reset Modes", command=guiResetModes)
    resetButton.grid(column=2, row=5, sticky=E)
    resetButton.state(["disabled"])
    resetButton_tip = Hovertip(resetButton, "Resets all special goal, start, and density mode settings to default.")
    makeButton = ttk.Button(mainframe, text="Make Mystery", command=guiStartRandomize)
    makeButton.grid(column=3, row=5, sticky=W)
    makeButton_tip = Hovertip(makeButton, text="Generates one or more Mystery settings files and seeds with the specified options,\nplacing them in the 'output' directory.\nMystery Maker will close when finished.")

    ttk.Label(mainframe, text="Generated settings and seeds will be placed in the 'output' directory.\nHover over options to display a tooltip with more information.", justify="center").grid(column=1, row=0, columnspan=3)
    ttk.Label(mainframe, text="Custom base MMR settings file:").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="Custom path to MMR.CLI.exe:").grid(column=1, row=3, sticky=E)
    ttk.Label(mainframe, text="# of seeds:").grid(column=1, row=4, sticky=E)

    modeTabs_notebook = ttk.Notebook(mainframe)
    modeTabGoalMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabGoalMode.grid(column=0, row=0, sticky=(N,W,S,E))
    modeTabStartMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabStartMode.grid(column=0, row=0, sticky=(N,W,S,E))    
    modeTabDensityMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabDensityMode.grid(column=0, row=0, sticky=(N,W,S,E))
    modeTabExtraMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabExtraMode.grid(column=0, row=0, sticky=(N,W,S,E))  
    modeTabs_notebook.add(modeTabGoalMode, text="Goal Mode")
    modeTabs_notebook.add(modeTabStartMode, text="Setup Modes")
    modeTabs_notebook.add(modeTabDensityMode, text="Density Modes")
    modeTabs_notebook.add(modeTabExtraMode, text="Extra Modes")
    modeTabs_notebook.grid(column=1, row=1, columnspan=3, sticky=(W, E))

    # Goal Mode pane
    goalMode = StringVar(value="No Blitz")
    goalLongGoal = StringVar(value="Full Fairy Hunt")
    goalDirectToCredits = StringVar(value="0")
    goalEarlyMoonRemains = StringVar(value="1")
    goalBlitzRemainsCount = StringVar(value="0")
    goalMode.trace_add("write", updateModeTabs)
    goalLongGoal.trace_add("write", updateModeTabs)
    goalDirectToCredits.trace_add("write", updateModeTabs)
    goalEarlyMoonRemains.trace_add("write", updateModeTabs)
    goalBlitzRemainsCount.trace_add("write", updateModeTabs)

    goalNoBlitz_radio = ttk.Radiobutton(modeTabGoalMode, text="No Blitz (default)", variable=goalMode, value="No Blitz")
    goalNoBlitz2_radio = ttk.Radiobutton(modeTabGoalMode, text="No Blitz 2", variable=goalMode, value="No Blitz 2")
    goalBlitz1_radio = ttk.Radiobutton(modeTabGoalMode, text="Blitz 1", width=15, variable=goalMode, value="Blitz 1")
    goalBlitz2_radio = ttk.Radiobutton(modeTabGoalMode, text="Blitz 2", width=15, variable=goalMode, value="Blitz 2")
    goalSeason2_radio = ttk.Radiobutton(modeTabGoalMode, text="Two to Four Remains", variable=goalMode, value="Two to Four Remains")
    goalAnyThree_radio = ttk.Radiobutton(modeTabGoalMode, text="Any Three Remains", variable=goalMode, value="Any Three Remains")
    goalRS_radio = ttk.Radiobutton(modeTabGoalMode, text="Remains Shuffle", variable=goalMode, value="Remains Shuffle")
    goalNPRS_radio = ttk.Radiobutton(modeTabGoalMode, text="Normal + Remains Shuffle", variable=goalMode, value="Normal + Remains Shuffle")
    goalFFH_radio = ttk.Radiobutton(modeTabGoalMode, text="Five Fairy Hunt", variable=goalMode, value="Five Fairy Hunt")
    goalGB_radio = ttk.Radiobutton(modeTabGoalMode, text="Grab Bag", variable=goalMode, value="Grab Bag")
    goalLongGoal_radio = ttk.Radiobutton(modeTabGoalMode, text="Long Goal:", variable=goalMode, value="Long Goal")    
    goalLongGoal_combo = ttk.Combobox(modeTabGoalMode, textvariable=goalLongGoal)
    goalLongGoal_combo["values"] = ("Full Fairy Hunt", "Mask Hunt", "Skull Tokens", "Hearts")
    goalLongGoal_combo.state(["readonly"])
    goalLongGoal_combo.state(["disabled"])
    goalDirectToCredits_check = ttk.Checkbutton(modeTabGoalMode, text="Direct To Credits", variable=goalDirectToCredits)
    goalEarlyMoonRemains_label = ttk.Label(modeTabGoalMode, text="Bosses for Early Moon: ")
    goalEarlyMoonRemains_spinbox = ttk.Spinbox(modeTabGoalMode, width=3, from_=0, to=4, textvariable=goalEarlyMoonRemains)
    goalEarlyMoonRemains_spinbox.state(["readonly"])
    goalBlitzRemainsCount_check = ttk.Checkbutton(modeTabGoalMode, text="Blitz Remains Count", variable=goalBlitzRemainsCount)

    goalNoBlitz_radio.grid(column=1, row=1, sticky=(W, E))
    goalNoBlitz2_radio.grid(column=2, row=1, sticky=(W, E))
    goalBlitz1_radio.grid(column=3, row=1, sticky=(W, E))
    goalBlitz2_radio.grid(column=4, row=1, sticky=(W, E))
    goalSeason2_radio.grid(column=5, row=1, sticky=(W, E))
    goalAnyThree_radio.grid(column=1, row=2, sticky=(W, E))
    goalRS_radio.grid(column=1, row=3, sticky=(W, E))
    goalNPRS_radio.grid(column=2, row=3, sticky=(W, E))
    goalFFH_radio.grid(column=1, row=4, sticky=(W, E))
    goalGB_radio.grid(column=2, row=4, sticky=(W, E))
    goalLongGoal_radio.grid(column=1, row=5, sticky=(W, E))
    goalLongGoal_combo.grid(column=2, row=5, sticky=(W, E))
    goalDirectToCredits_check.grid(column=1, row=6, sticky=(W, E))
    goalEarlyMoonRemains_label.grid(column=1, row=7, sticky=(W,E))
    goalEarlyMoonRemains_spinbox.grid(column=2, row=7, sticky=(W))
    goalBlitzRemainsCount_check.grid(column=3, row=7, sticky=(W,E))
    
    goalNoBlitz_tip = Hovertip(goalNoBlitz_radio, "Remains on bosses. Always start without any remains.")
    goalNoBlitz2_tip = Hovertip(goalNoBlitz2_radio, "Remains on bosses. May start with one remains,\nwith its corresponding temple and post-temple junked.\nDefault weights are 85/15 for 0/1 starting remains.")
    goalBlitz1_tip = Hovertip(goalBlitz1_radio, "Remains on bosses. Always start with one remains;\nits temple and post-temple checks are junked.")
    goalBlitz2_tip = Hovertip(goalBlitz2_radio, "Remains on bosses. Always start with two remains;\ntheir temple and post-temple checks are junked.")
    goalSeason2_tip = Hovertip(goalSeason2_radio, "Remains on bosses. May start with one or two remains,\nwith corresponding temples and post-temples junked.\nDefault weights are 65/25/10 for 0/1/2 starting remains.\nThis was used in Mystery Season 2.")
    goalAnyThree_tip = Hovertip(goalAnyThree_radio, "Remains on bosses. Majora may be accessed and fought with three remains instead of four. MMR's item importance algorithm will take this into account!")
    goalRS_tip = Hovertip(goalRS_radio, "Remains shuffled anywhere. C-Up at clock tower door for region hints.")
    goalNPRS_tip = Hovertip(goalNPRS_radio, "Choose from No Blitz, Blitz 1, or Remains Shuffle (60/20/20).")
    goalFFH_tip = Hovertip(goalFFH_radio, "Remains on Great Fairy Rewards.\nAll Stray Fairies shuffled and five Stray Fairies of each color are placed:\nfind and turn in one set to win immediately!\nAlways start with Epona, Lullaby, Great Fairy's Mask, and the other 40 fairies.\nSkull Kid Song is junked; only Traditional and Songsanity song layouts are possible.\nTemple locations always shuffled.\nFairy Fountains hint fairy regions. No WotHs, no foolishes.")
    goalGB_tip = Hovertip(goalGB_radio, "Choose one of Remains on Bosses, Remains Shuffle, or Five Fairy Hunt (equal weights).\nFor Remains on Bosses, No Blitz, Blitz 1, and Blitz 2 are all equally likely.")
    goalLongGoal_tip = Hovertip(goalLongGoal_radio, "Choose a long victory mode from the drop-down box.\nComplete the chosen win condition before fighting Majora.\n(Hover over the drop-down box for specifics.)\nEvery long victory mode gives no WotH or foolish hints.")
    goalLongGoalCombo_tip = Hovertip(goalLongGoal_combo, "Full Fairy Hunt: Find all four boss remains on Great Fairy Rewards. All Stray Fairies are shuffled.\nMask Hunt: Find all shuffled masks. Always uses Moon Oath song layout.\nSkull Tokens: Find all 60 shuffled skull tokens.\nHearts: Find all shuffled Heart Containers and Pieces of Heart.")
    goalDirectToCredits_tip = Hovertip(goalDirectToCredits_check, "Win immediately upon collecting all required remains or\nwin condition items without needing to use Oath and fight Majora.\n(This is always on in Five Fairy Hunt.)")
    goalEarlyMoonRemains_tip = Hovertip(goalEarlyMoonRemains_spinbox, "Modifies the number of remains from unjunked bosses to be collected during the seed\nfor moon access when Moon Oath is the song layout.\n(By default, Mystery adjusts MMR's 'Remains for Moon Access' value automatically in Blitz seeds;\nMystery seeds will require two remains in Link's inventory for moon access in a Blitz 1 Moon Oath seed.)\nDefault is 1.\nMoon Oath will not be rolled in non-Mask Hunt seeds where this value would cause four remains to be required for moon access.")
    goalBlitzRemainsCount_tip = Hovertip(goalBlitzRemainsCount_check, "If checked, free starting remains from Blitz-junked bosses count toward moon access in relevant seeds\n(i.e. Remains for Moon Access is constant regardless of Blitz).")

    # Start Modes pane
    startSongLayoutMode = StringVar(value="Any (Default)")
    startDifficultyMode = StringVar(value="Default")
    startRandomItemMode = StringVar(value="Any (Default)")
    startFDAnywhereMode = StringVar(value="Sometimes (Default)")
    startDungeonERMode = StringVar(value="Sometimes (Default)")
    startBossKeysMode = StringVar(value="Off (Default)")
    startSmallKeysMode = StringVar(value="Sometimes (Default)")
    startAllMoonTrialsMode = StringVar(value="0")
    startSongLayoutMode.trace_add("write", updateModeTabs)
    startDifficultyMode.trace_add("write", updateModeTabs)
    startRandomItemMode.trace_add("write", updateModeTabs)
    startFDAnywhereMode.trace_add("write", updateModeTabs)
    startDungeonERMode.trace_add("write", updateModeTabs)
    startBossKeysMode.trace_add("write", updateModeTabs)
    startSmallKeysMode.trace_add("write", updateModeTabs)
    startAllMoonTrialsMode.trace_add("write", updateModeTabs)
    
    startSongLayout_label = ttk.Label(modeTabStartMode, text="Song Layout:    ")
    startSongLayout_combo = ttk.Combobox(modeTabStartMode, textvariable=startSongLayoutMode)
    startSongLayout_combo["values"] = ("Any (Default)", "Any Non-Moon", "Traditional", "Songsanity", "Baby Zoras", "Moon Oath")
    startSongLayout_combo.state(["readonly"])
    startDifficulty_label = ttk.Label(modeTabStartMode, text="Start Difficulty:    ")
    startDifficulty_combo = ttk.Combobox(modeTabStartMode, textvariable=startDifficultyMode)
    startDifficulty_combo["values"] = ("Strong", "Kokiri", "Default", "Swordless", "Fragile", "Cruel")
    startDifficulty_combo.state(["readonly"])
    startRandomItem_label = ttk.Label(modeTabStartMode, text="Starting Random Item:    ")
    startRandomItem_combo = ttk.Combobox(modeTabStartMode, textvariable=startRandomItemMode, width=25)
    startRandomItem_combo["values"] = ("Off",
                                       "Any (Default)",
                                       "Any Transformation Mask",
                                       "Any Non-Transformation",
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
    startFDAnywhere_combo["values"] = ("Off", "Only When Starting", "Sometimes (Default)", "Always")
    startFDAnywhere_combo.state(["readonly"])
    startDungeonER_label = ttk.Label(modeTabStartMode, text="Dungeon Entrances: ")
    startDungeonER_combo = ttk.Combobox(modeTabStartMode, textvariable=startDungeonERMode, width=25)
    startDungeonER_combo["values"] = ("Off", "Sometimes (Default)", "Always")
    startDungeonER_combo.state(["readonly"])
    startBossKeys_label = ttk.Label(modeTabStartMode, text="Boss Keys:    ")
    startBossKeys_combo = ttk.Combobox(modeTabStartMode, textvariable=startBossKeysMode, width=25)
    startBossKeys_combo["values"] = ("Off (Default)", "Sometimes", "Always Within Their Temple", "Always Within Any Temple", "Anywhere Within Their Area", "Anywhere")
    startBossKeys_combo.state(["readonly"])
    startSmallKeys_label = ttk.Label(modeTabStartMode, text="Small Keys:    ")
    startSmallKeys_combo = ttk.Combobox(modeTabStartMode, textvariable=startSmallKeysMode, width=25)
    startSmallKeys_combo["values"] = ("Off", "Sometimes (Default)", "Always Within Their Temple", "Always Within Any Temple", "Anywhere Within Their Area", "Anywhere")
    startSmallKeys_combo.state(["readonly"])
    startAllMoonTrials_check = ttk.Checkbutton(modeTabStartMode, text="Moon Oath Adds All Trials", variable=startAllMoonTrialsMode)

    
    startSongLayout_label.grid(column=1, row=1, sticky=(W,E))
    startSongLayout_combo.grid(column=2, row=1, sticky=(W,E))
    startDifficulty_label.grid(column=1, row=2, sticky=(W,E))
    startDifficulty_combo.grid(column=2, row=2, sticky=(W,E))
    startRandomItem_label.grid(column=1, row=3, sticky=(W,E))
    startRandomItem_combo.grid(column=2, row=3, sticky=(W,E))
    startFDAnywhere_label.grid(column=1, row=4, sticky=(W,E))
    startFDAnywhere_combo.grid(column=2, row=4, sticky=(W,E))
    startDungeonER_label.grid(column=1, row=5, sticky=(W,E))
    startDungeonER_combo.grid(column=2, row=5, sticky=(W,E))
    startBossKeys_label.grid(column=1, row=6, sticky=(W,E))
    startBossKeys_combo.grid(column=2, row=6, sticky=(W,E))
    startSmallKeys_label.grid(column=1, row=7, sticky=(W,E))
    startSmallKeys_combo.grid(column=2, row=7, sticky=(W,E))
    startAllMoonTrials_check.grid(column=3, row=1, sticky=(W,E))
    startSongLayout_tip = Hovertip(startSongLayout_combo, "Choose a song layout.\nSong checks include Skull Kid Song, Imprisoned Monkey, Baby Goron, Romani's Game, Day 1 Grave Tablet, Ikana King, and Boss Blue Warp.\nAny: Use the default Mystery category roll.\nAny Non-Moon: Use a random roll, excluding Moon Oath. (Its weight is added to Traditional.)\nTraditional: Songs on song checks, including Skull Kid Song. Adds and hints Anju and Kafei.\nSongsanity: Songs anywhere. Traditional song checks (except Skull Kid Song) can get items. Adds a 4th WotH hint.\nBaby Zoras: Songs on song checks. Baby Zoras replaces Skull Kid's Song and is always hinted. By default, Scoopsanity can't shuffle eggs.\nMoon Oath: Songs on song checks, except Skull Kid's Song. Oath to Order is given as an additional starting song.\n          Link Trial's PoH, chests, and pots are shuffled! Moon access is available with fewer remains. Adds and hints Anju and Kafei.")
    startDifficulty_tip = Hovertip(startDifficulty_combo, "Choose a starting difficulty mode.\nHigher difficulties change more than just starting items!\nStrong: Razor Sword, Hero's Shield, Spin Attack Mastery, and Double Defense.\nKokiri: Kokiri Sword and Hero's Shield.\nDefault: 75% chance of Kokiri Sword and Hero's Shield (always, in Light Mystery).\nSwordless: No Kokiri Sword or Hero's Shield.\nFragile: No sword (or FD or GFS, by default), no shield, one heart. No Crit Wiggle.\nCruel: No sword, no shield, one heart. No starting random item. Fierce Deity's Mask is not shuffled. Link takes double damage!")
    startRandomItem_tip = Hovertip(startRandomItem_combo, "Choose a starting random item mode, or guarantee a specific starting item.\n(When randomized, Bomb Bag, Blast Mask, Bunny Hood, and Great Fairy's Sword each\nhave half the weight of other items.)\nOff: Do not give a starting random item.\nAny: Randomly choose any item on the list.\nAny Transformation Mask: Randomly choose any transformation mask, including Fierce Deity's Mask.\nAny Non-Transformation: Randomly choose anything but Deku, Goron, Zora, or Fierce Deity.")
    startFDAnywhere_tip = Hovertip(startFDAnywhere_combo, "Choose a Fierce Deity's Mask Anywhere mode.\n(Remember that FD can be required in logic when FD Anywhere is active!\nConsult the Mystery Settings Document or base .json for added tricks.)\nOff: FD Anywhere is never on.\nOnly When Starting: FD Anywhere is only on when starting with Fierce Deity's Mask.\nSometimes: FD Anywhere is always on when starting with FD, and sometimes on otherwise (50%, by default).\nAlways: FD Anywhere is always on.")
    startDungeonER_tip = Hovertip(startDungeonER_combo, "Choose a Dungeon Entrances option.\nAffected entrances are WFT, SHT, GBT, and inverted STT.\nOff: Dungeon entrances are never shuffled.\nSometimes: Use the default Mystery category roll.\nAlways: Dungeon entrances are always shuffled.")
    startBossKeys_tip = Hovertip(startBossKeys_combo, "Choose a Boss Keys option.\nRemember that WotH/Foolish hints ignore Boss Keys when shuffled within temples!\nOff: Boss Keys don't appear. Boss doors are always open and Boss Key chests can have items.\nSometimes: Use a random roll with Season 2 weights (65/20/15 for off/own temple/any temple).\nAlways Within Their Temple: Boss Keys are on any check in their own temple.\nAlways Within Any Temple: Boss Keys are on any check in any temple.\nAnywhere Within Their Area: Boss Keys are on any check in their temple or temple's region.\nAnywhere: Boss Keys are anywhere.")
    startSmallKeys_tip = Hovertip(startSmallKeys_combo, "Choose a Small Keys option.\nRemember that WotH/Foolish hints ignore Small Keys when shuffled within temples!\nOff: Small Keys don't appear. Small key doors are always open.\nSometimes: Use the default Mystery category roll.\nAlways Within Their Temple: Small Keys are on any check in their own temple.\nAlways Within Any Temple: Small Keys are on any check in any temple.\nAnywhere Within Their Area: Small Keys are on any check in their temple or temple's region.\nAnywhere: Small Keys are anywhere.")
    startAllMoonTrials_tip = Hovertip(startAllMoonTrials_check, "Adds the Deku Trial, Goron Trial, and Zora Trial Pieces of Heart to the Moon Oath shuffle.")

    # Density Modes pane
    mainDensityMode = StringVar(value="Normal")
    densityCategoryMinimum = StringVar(value="7")
    densityNoCT = StringVar(value="0")
    densityNoPT = StringVar(value="0")
    densityMapCompassMode = StringVar(value="0")
    densityPotsanityMode = StringVar(value="Default")
    densityScoopsanityMode = StringVar(value="Default")
    densityScrambledEggsMode = StringVar(value="0")
    densityStubbornPrincessMode = StringVar(value="0")
    densityNoFrogChoirMode = StringVar(value="0")
    densityStubbornSeahorseMode = StringVar(value="0")
    mainDensityMode.trace_add("write", updateModeTabs)
    densityCategoryMinimum.trace_add("write", updateModeTabs)
    densityNoCT.trace_add("write", updateModeTabs)
    densityNoPT.trace_add("write", updateModeTabs)
    densityMapCompassMode.trace_add("write", updateModeTabs)
    densityPotsanityMode.trace_add("write", updateModeTabs)
    densityScoopsanityMode.trace_add("write", updateModeTabs)
    densityScrambledEggsMode.trace_add("write", updateModeTabs)
    densityStubbornPrincessMode.trace_add("write", updateModeTabs)
    densityNoFrogChoirMode.trace_add("write", updateModeTabs)
    densityStubbornSeahorseMode.trace_add("write", updateModeTabs)
    
    densityNormal_radio = ttk.Radiobutton(modeTabDensityMode, text="Normal (default)", variable=mainDensityMode, value="Normal")
    densityLight_radio = ttk.Radiobutton(modeTabDensityMode, text="Light Mystery", variable=mainDensityMode, value="Light")
    densitySuper_radio = ttk.Radiobutton(modeTabDensityMode, text="Super Mystery", variable=mainDensityMode, value="Super")
    densityCategoryMinimum_label = ttk.Label(modeTabDensityMode, text="Category Minimum: ")
    densityCategoryMinimum_spinbox = ttk.Spinbox(modeTabDensityMode, width=3, from_=0, to=14, textvariable=densityCategoryMinimum)
    densityCategoryMinimum_spinbox.state(["readonly"])
    densityNoCT_check = ttk.Checkbutton(modeTabDensityMode, text="No Clock Town", variable=densityNoCT)
    densityNoPT_check = ttk.Checkbutton(modeTabDensityMode, text="No Post-Temple", variable=densityNoPT)
    densityMapCompass_check = ttk.Checkbutton(modeTabStartMode, text="Maps Hint Dungeon ER", variable=densityMapCompassMode)
    densityPotsanity_label = ttk.Label(modeTabDensityMode, text="Overworld Pots: ")
    densityScoopsanity_label = ttk.Label(modeTabDensityMode, text="Scoopsanity:  ")
    densityPotsanity_combo = ttk.Combobox(modeTabDensityMode, textvariable=densityPotsanityMode, width=25)
    densityPotsanity_combo["values"] = ("Off", "Default", "Central Pots", "South Pots", "North Pots", "West Pots", "East Pots", "Any One Group", "Any Two Groups", "Full Potsanity")
    densityPotsanity_combo.state(["readonly"])
    densityScoopsanity_combo = ttk.Combobox(modeTabDensityMode, textvariable=densityScoopsanityMode, width=25)
    densityScoopsanity_combo["values"] = ("Off", "Default", "On")
    densityScoopsanity_combo.state(["readonly"])
    densityScrambledEggs_check = ttk.Checkbutton(modeTabDensityMode, text="Always Scrambles Eggs", variable=densityScrambledEggsMode)
    densityStubbornPrincess_check = ttk.Checkbutton(modeTabDensityMode, text="Shuffles Princess", variable=densityStubbornPrincessMode)
    densityNoFrogChoir_check = ttk.Checkbutton(modeTabDensityMode, text="No Frog Choir", variable=densityNoFrogChoirMode)
    densityStubbornSeahorse_check = ttk.Checkbutton(modeTabDensityMode, text="Never Shuffle Seahorse", variable=densityStubbornSeahorseMode)

    densityMapCompass_check.grid(column=3, row=5, sticky=(W,E))   # should be moved up alongside other setup modes

    densityNormal_radio.grid(column=1, row=1, sticky=(W,E))
    densityLight_radio.grid(column=2, row=1, sticky=(W,E))
    densitySuper_radio.grid(column=3, row=1, sticky=(W,E))
    densityCategoryMinimum_label.grid(column=1, row=2, sticky=(W,E))
    densityCategoryMinimum_spinbox.grid(column=2, row=2, sticky=(W))
    densityNoCT_check.grid(column=1, row=3, sticky=(W,E))
    densityNoPT_check.grid(column=2, row=3, sticky=(W,E))
    densityPotsanity_label.grid(column=1, row=4, sticky=(W,E))
    densityPotsanity_combo.grid(column=2, row=4, sticky=(W,E))
    densityScoopsanity_label.grid(column=1, row=5, sticky=(W,E))
    densityScoopsanity_combo.grid(column=2, row=5, sticky=(W,E))
    densityScrambledEggs_check.grid(column=3, row=5, sticky=(W,E))
    densityStubbornPrincess_check.grid(column=4, row=5, sticky=(W,E))
    densityNoFrogChoir_check.grid(column=1, row=6, sticky=(W,E))
    densityStubbornSeahorse_check.grid(column=1, row=7, sticky=(W,E))

    densityNormal_tip = Hovertip(densityNormal_radio, "Baseline appearance rates for all categories. See the Category Weights Table for specifics.\nSuggested category minimum is 7.")
    densityLight_tip = Hovertip(densityLight_radio, "Excludes certain mystery options with harder or high-quantity checks\nand decreases other weights slightly.\nNo full Keaton Grass, full Tokensanity, or full Notebook.\nNo swordless start or full Potsanity (by default).\nSuggested category minimum is 5.")
    densitySuper_tip = Hovertip(densitySuper_radio,"Dramatically increased appearance rates for all categories!\nFull Hit Spots is possible.\nSuggested category minimum is 9.")
    densityCategoryMinimum_tip = Hovertip(densityCategoryMinimum_spinbox,"Modifies the minimum number of active categories.\nMystery Maker will reroll until this minimum is met.")
    densityNoCT_tip = Hovertip(densityNoCT_check, "All non-scoop checks in Clock Town regions, including those added by Mystery categories,\nare junked or unshuffled as appropriate.\nThe Bombers' Notebook category is disabled.\nEpona's Song is granted as an additional starting song; Skull Kid Song is always junked.\nWhen the song layout is Baby Zoras or Moon Oath, Boss Blue Warp is junked too.\nThe Moon is not in Clock Town.")
    densityNoPT_tip = Hovertip(densityNoPT_check, "All post-temple checks, including those added by Mystery categories,\nare junked or unshuffled as appropriate.\nBottle: Deku Princess is never shuffled; other scoops are not affected.\nFrog Choir is disabled.\nMoon checks are not considered post-temple.")
    densityMapCompass_tip = Hovertip(densityMapCompass_check, "Whenever temple entrances are shuffled, temples' Maps are shuffled and placed exclusively in the overworld,\nrevealing their corresponding entrance shuffle when found.")
    densityPotsanity_tip = Hovertip(densityPotsanity_combo, "Choose an Overworld Pots option instead of using the customary random roll.\n'Central' is Clock Town, Termina Field, Romani Ranch, Road to Ikana, and Ikana Graveyard.\nOwl pots are excluded.\nOff: Pot contents won't be shuffled. Also prevents Temple Pots.\nDefault: Use the default Mystery roll.\nSpecific Group: Shuffle all pots in that group.\nAny One Group: Shuffle one group, chosen randomly (by group weights).\nAny Two Groups: Shuffle two different groups, chosen randomly (by group weights)\nFull Potsanity: Shuffle all groups! Guarantees Temple Pots too.")
    densityScoopsanity_tip = Hovertip(densityScoopsanity_combo, "Choose a Scoopsanity option instead of using the customary random roll for the category.\nOff: Scoops won't be shuffled.\nDefault: Use the default Mystery category roll.\nOn: Scoops, except for bugs, are shuffled.")
    densityUnscrambledEggs_tip = Hovertip(densityScrambledEggs_check, "Allows Scoopsanity to shuffle Zora Eggs even when Baby Zoras is active.")
    densityStubbornPrincess_tip = Hovertip(densityStubbornPrincess_check, "Includes the Deku Princess in Scoopsanity.\nBottle: Deku Princess will be on the backup hint list.")
    densityNoFrogChoir_tip = Hovertip(densityNoFrogChoir_check, "Prevents the Frogs category from replacing Ranch Defense with Frog Choir.\n(Ranch Defense will remain in play and be always hinted; Frog Choir will stay junked.)")
    densityStubbornSeahorse_tip = Hovertip(densityStubbornSeahorse_check, "Excludes the Fisherman Pictograph check from the Photos, Sales, and Small Favors category.\nThis keeps the Seahorse in its vanilla location and model.")
    
    # Extra Modes pane
    extraNoIcelessFDLogicMode = StringVar(value="0")
    extraNoMilkRoadFDLogicMode = StringVar(value="0")
    extraICMode = StringVar(value="0")
    extraSunsSongMode = StringVar(value="0")
    extraNoIcelessFDLogicMode.trace_add("write", updateModeTabs)
    extraNoMilkRoadFDLogicMode.trace_add("write", updateModeTabs)
    extraICMode.trace_add("write", updateModeTabs)
    extraSunsSongMode.trace_add("write", updateModeTabs)

    extraNoIcelessFDLogic_check = ttk.Checkbutton(modeTabExtraMode, text="No Iceless FD Logic", variable=extraNoIcelessFDLogicMode)
    extraNoMilkRoadFDLogic_check = ttk.Checkbutton(modeTabExtraMode, text="No Milk Road FD Logic", variable=extraNoMilkRoadFDLogicMode)
    extraNoIC_check = ttk.Checkbutton(modeTabExtraMode, text="Importance Count", variable=extraICMode)
    extraSunsSong_check = ttk.Checkbutton(modeTabExtraMode, text="Enable Sun's Song", variable=extraSunsSongMode)

    extraNoIcelessFDLogic_check.grid(column=1, row=1, sticky=(W,E))
    extraNoMilkRoadFDLogic_check.grid(column=1, row=2, sticky=(W,E))
    extraNoIC_check.grid(column=1, row=3, sticky=(W,E))
    extraSunsSong_check.grid(column=1, row=4, sticky=(W,E))

    extraNoIcelessFDLogic_tip = Hovertip(extraNoIcelessFDLogic_check, "Disable Iceless FD logic. Removes the 'as FD' GBT Red Pump/GBT Boss Door/Ikana Canyon Iceless/GBT Map Chest Jumps tricks.")
    extraNoMilkRoadFDLogic_tip = Hovertip(extraNoMilkRoadFDLogic_check, "Disable Milk Road FD logic. Removes the FD Jump into Ranch and Ranch Tingle as FD tricks.")
    extraNoIC_tip = Hovertip(extraNoIC_check, "Enable Importance Count. WotH hints will become IC hints instead.")
    extraSunsSong_tip = Hovertip(extraSunsSong_check, "Allow the use of Sun's Song (C-Right, C-Down, C-Up, C-Right, C-Down, C-Up) to speed up the clock.\nSun's Song will be available from the start of the seed.")


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    baseSettingsFilePath_entry.focus()
    guiWindow.protocol("WM_DELETE_WINDOW", guiCloseButton)
    guiWindow.bind("<Return>", guiStartRandomize)

    guiWindow.mainloop()
    customModesSettings = dict()
    customModesSettings["Goal Mode"] = goalMode.get()
    if goalMode.get() == "Long Goal":
        customModesSettings["Long Goal"] = goalLongGoal.get()
    else:
        customModesSettings["Long Goal"] = "None"
    customModesSettings["Direct to Credits"] = (goalDirectToCredits.get() == "1")
    customModesSettings["Start Mode"] = startDifficultyMode.get()
    customModesSettings["Song Layout"] = startSongLayoutMode.get()
    customModesSettings["All Moon Trials"] = (startAllMoonTrialsMode.get() == "1")
    customModesSettings["Early Moon Access Remains"] = int(goalEarlyMoonRemains.get())
    customModesSettings["Blitz Remains Count"] = (goalBlitzRemainsCount.get() == "1")
    customModesSettings["Random Item Mode"] = startRandomItemMode.get()
    customModesSettings["FD Anywhere Mode"] = startFDAnywhereMode.get()
    customModesSettings["Dungeon Entrances"] = startDungeonERMode.get()
    customModesSettings["Boss Keys"] = startBossKeysMode.get()
    customModesSettings["Small Keys"] = startSmallKeysMode.get()
    customModesSettings["Main Density Mode"] = mainDensityMode.get()
    customModesSettings["Category Minimum"] = int(densityCategoryMinimum.get())
    customModesSettings["No Clock Town"] = (densityNoCT.get() == "1")
    customModesSettings["No Post-Temple"] = (densityNoPT.get() == "1")
    customModesSettings["Map and Compass Hints"] = (densityMapCompassMode.get() == "1")
    customModesSettings["Potsanity"] = densityPotsanityMode.get()
    customModesSettings["Scoopsanity"] = densityScoopsanityMode.get()
    customModesSettings["Vanilla Eggs for Baby Zoras"] = (densityScrambledEggsMode.get() == "0") # careful here!
    customModesSettings["Stubborn Princess"] = (densityStubbornPrincessMode.get() == "0")
    customModesSettings["No Frog Choir"] = (densityNoFrogChoirMode.get () == "1")
    customModesSettings["Stubborn Seahorse"] = (densityStubbornSeahorseMode.get() == "1")
    customModesSettings["No Iceless FD Logic"] = (extraNoIcelessFDLogicMode.get() == "1")
    customModesSettings["No Milk Road FD Logic"] = (extraNoMilkRoadFDLogicMode.get() == "1")
    customModesSettings["Importance Count"] = (extraICMode.get() == "1")
    customModesSettings["Sun's Song"] = (extraSunsSongMode.get() == "1")

    return [(windowForceClosed.get() == "1"),
            baseSettingsFilePath.get(),
            mmrCommandLineExePath.get(),
            (int)(numberToGenerate.get()),
            (makeSettingsOnly.get() == "1"),
            customModesSettings]
