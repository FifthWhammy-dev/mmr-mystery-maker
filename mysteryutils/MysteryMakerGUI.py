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
        goalMode.set("Normal")
        goalDirectToCredits.set("0")
        startDifficultyMode.set("Default")
        startRandomItemMode.set("Any (Default)")
        startFDAnywhereMode.set("Sometimes (Default)")
        mainDensityMode.set("Normal")
        densityNoCT.set("0")
        densityNoPT.set("0")
        densityMapCompassMode.set("0")
        densityBossKeysMode.set("Default")
        resetButton.state(["disabled"])

    def browseForBaseSettingsFile(*args):
        baseSettingsFilePath.set(filedialog.askopenfilename())

    def browseForCommandLineExe(*args):
        mmrCommandLineExePath.set(filedialog.askopenfilename())

    def checkDefaults(*args):
        return (goalMode.get() == "Normal" and
                goalDirectToCredits.get() == "0" and
                startDifficultyMode.get() == "Default" and
                startRandomItemMode.get() == "Any (Default)" and
                startFDAnywhereMode.get() == "Sometimes (Default)" and
                mainDensityMode.get() == "Normal" and
                densityNoCT.get() == "0" and
                densityNoPT.get() == "0" and
                densityMapCompassMode.get() == "0" and
                densityBossKeysMode.get() == "Default")
    
    def updateModeTabs(*args):
        goalLongGoal_combo.state(["!disabled"] if goalMode.get() == "Long Goal" else ["disabled"])
        
        if goalMode.get() == "Five Fairy Hunt":
            densityBossKeysMode.set("Off")
            densityBossKeys_combo.state(["disabled"])
        else:
            if mainDensityMode.get() != "Light":
                densityBossKeys_combo.state(["!disabled"])        
        
        if mainDensityMode.get() == "Light":
            densityBossKeysMode.set("Off")
            densityBossKeys_combo.state(["disabled"])
            densityNoPT.set("1")
            densityNoPT_check.state(["disabled"])
            densityMapCompassMode.set("1")
            densityMapCompass_check.state(["disabled"])
        else:
            if goalMode.get() != "Five Fairy Hunt":
                densityBossKeys_combo.state(["!disabled"])
            densityNoPT_check.state(["!disabled"])
            densityMapCompass_check.state(["!disabled"])
        
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

    baseSettingsFilePath = StringVar(value="Mystery_Settings_base.json")
    baseSettingsFilePath_entry = ttk.Entry(mainframe, width=70, textvariable=baseSettingsFilePath)
    baseSettingsFilePath_entry.grid(column=2, row=2, sticky=(W, E))
    baseSettingsFilePath_tip = Hovertip(baseSettingsFilePath_entry, "The MMR settings file that's copied and modified\nby Mystery Maker to make mystery seeds.\nThe Mystery_Settings_base.json file comes with Mystery Maker.")

    mmrCommandLineExePath = StringVar(value="MMR.CLI.exe")
    mmrCommandLineExePath_entry = ttk.Entry(mainframe, width=70, textvariable=mmrCommandLineExePath)
    mmrCommandLineExePath_entry.grid(column=2, row=3, sticky=(W, E))
    mmrCommandLineExePath_tip = Hovertip(mmrCommandLineExePath_entry, "The MMR command-line executable that makes playable seed files.\nChanging this should only be needed if you didn't install\nMystery Maker in the same folder as MMR.")

    numberToGenerate = StringVar(value="1")
    numberToGenerate_spinbox = ttk.Spinbox(mainframe, width=5, from_=1, to=100,textvariable=numberToGenerate)
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
    modeTabs_notebook.add(modeTabGoalMode, text="Goal Mode")
    modeTabs_notebook.add(modeTabStartMode, text="Start Modes")
    modeTabs_notebook.add(modeTabDensityMode, text="Density Modes")
    modeTabs_notebook.grid(column=1, row=1, columnspan=3, sticky=(W, E))

    # Goal Mode pane
    goalMode = StringVar(value="Normal")
    goalLongGoal = StringVar(value="Full Fairy Hunt")
    goalDirectToCredits = StringVar(value="0")
    goalMode.trace_add("write", updateModeTabs)
    goalLongGoal.trace_add("write", updateModeTabs)
    goalDirectToCredits.trace_add("write", updateModeTabs)

    goalNormal_radio = ttk.Radiobutton(modeTabGoalMode, text="Normal (default)", variable=goalMode, value="Normal")
    goalNoBlitz_radio = ttk.Radiobutton(modeTabGoalMode, text="No Blitz", variable=goalMode, value="No Blitz")
    goalBlitz1_radio = ttk.Radiobutton(modeTabGoalMode, text="Blitz 1", width=20, variable=goalMode, value="Blitz 1")
    goalBlitz2_radio = ttk.Radiobutton(modeTabGoalMode, text="Blitz 2", variable=goalMode, value="Blitz 2")
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

    goalNormal_radio.grid(column=1, row=1, sticky=(W, E))
    goalNoBlitz_radio.grid(column=2, row=1, sticky=(W, E))
    goalBlitz1_radio.grid(column=3, row=1, sticky=(W, E))
    goalBlitz2_radio.grid(column=4, row=1, sticky=(W, E))
    goalRS_radio.grid(column=1, row=2, sticky=(W, E))
    goalNPRS_radio.grid(column=2, row=2, sticky=(W, E))
    goalFFH_radio.grid(column=1, row=3, sticky=(W, E))
    goalGB_radio.grid(column=2, row=3, sticky=(W, E))
    goalLongGoal_radio.grid(column=1, row=4, sticky=(W, E))
    goalLongGoal_combo.grid(column=2, row=4, sticky=(W, E))
    goalDirectToCredits_check.grid(column=1, row=5, sticky=(W, E))
    
    goalNormal_tip = Hovertip(goalNormal_radio, "Remains on bosses. May start with one or two remains,\nwith corresponding temples and post-temples junked.\nDefault weights are 65/25/10 for 0/1/2 starting remains.")
    goalNoBlitz_tip = Hovertip(goalNoBlitz_radio, "Remains on bosses. Always start without any remains.")
    goalBlitz1_tip = Hovertip(goalBlitz1_radio, "Remains on bosses. Always start with one remains;\nits temple and post-temple checks are junked.")
    goalBlitz2_tip = Hovertip(goalBlitz2_radio, "Remains on bosses. Always start with two remains;\ntheir temple and post-temple checks are junked.")
    goalRS_tip = Hovertip(goalRS_radio, "Remains shuffled anywhere. C-Up at clock tower door for region hints.")
    goalNPRS_tip = Hovertip(goalNPRS_radio, "Choose any normal Remains on Bosses goal mode (45/25/10)\nor Remains Shuffle (20).")
    goalFFH_tip = Hovertip(goalFFH_radio, "Remains on Great Fairy Rewards.\nAll Stray Fairies shuffled and five Stray Fairies of each color are placed:\nfind and turn in one set to win immediately!\nAlways start with Epona, Lullaby, Great Fairy's Mask, and the other 40 fairies.\nSkull Kid Song is junked, and Baby Zoras are disabled.\nTemple locations always shuffled. Boss Keys and Boss Rooms never shuffled.\nFairy Fountains hint fairy regions. No WotHs, no foolishes.")
    goalGB_tip = Hovertip(goalGB_radio, "Choose one of Remains on Bosses, Remains Shuffle, or Five Fairy Hunt (equal weights).\nFor Remains on Bosses, No Blitz, Blitz 1, and Blitz 2 are all equally likely.")
    goalLongGoal_tip = Hovertip(goalLongGoal_radio, "Choose a long victory mode from the drop-down box.\nComplete the chosen win condition before fighting Majora.\n(Hover over the drop-down box for specifics.)\nEvery long victory mode gives no WotH or foolish hints.")
    goalLongGoalCombo_tip = Hovertip(goalLongGoal_combo, "Full Fairy Hunt: Find all four boss remains on Great Fairy Rewards. All Stray Fairies are shuffled.\nMask Hunt: Find all shuffled masks. Moon access only requires one remains. Start with Oath also; Skull Kid's Song is junked.\nSkull Tokens: Find all 60 shuffled skull tokens.\nHearts: Find all shuffled Heart Containers and Pieces of Heart.")
    goalDirectToCredits_tip = Hovertip(goalDirectToCredits_check, "Win immediately upon collecting all required remains or\nwin condition items without needing to use Oath and fight Majora.\n(This is always on in Five Fairy Hunt.)")

    # Start Modes pane
    startDifficultyMode = StringVar(value="Default")
    startRandomItemMode = StringVar(value="Any (Default)")
    startFDAnywhereMode = StringVar(value="Sometimes (Default)")
    startDifficultyMode.trace_add("write", updateModeTabs)
    startRandomItemMode.trace_add("write", updateModeTabs)
    startFDAnywhereMode.trace_add("write", updateModeTabs)
    
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
    
    startDifficulty_label.grid(column=1, row=1, sticky=(W,E))
    startDifficulty_combo.grid(column=2, row=1, sticky=(W,E))
    startRandomItem_label.grid(column=1, row=2, sticky=(W,E))
    startRandomItem_combo.grid(column=2, row=2, sticky=(W,E))
    startFDAnywhere_label.grid(column=1, row=3, sticky=(W,E))
    startFDAnywhere_combo.grid(column=2, row=3, sticky=(W,E))
    startDifficulty_tip = Hovertip(startDifficulty_combo, "Choose a starting difficulty mode.\nHigher difficulties change more than just starting items!\nStrong: Razor Sword, Hero's Shield, Spin Attack Mastery, and Double Defense.\nKokiri: Kokiri Sword and Hero's Shield.\nDefault: 75% chance of Kokiri Sword and Hero's Shield (always, in Light Mystery).\nSwordless: No Kokiri Sword or Hero's Shield.\nFragile: No sword (or FD or GFS, by default), no shield, one heart. No Crit Wiggle.\nCruel: No sword, no shield, one heart. No starting random item. Fierce Deity's Mask is not shuffled. Link takes double damage!")
    startRandomItem_tip = Hovertip(startRandomItem_combo, "Choose a starting random item mode, or guarantee a specific starting item.\n(When randomized, Bomb Bag, Blast Mask, Bunny Hood, and Great Fairy's Sword each\nhave half the weight of other items.)\nOff: Do not give a starting random item.\nAny: Randomly choose any item on the list.\nAny Transformation Mask: Randomly choose any transformation mask, including Fierce Deity's Mask.\nAny Non-Transformation: Randomly choose anything but Deku, Goron, Zora, or Fierce Deity.")
    startFDAnywhere_tip = Hovertip(startFDAnywhere_combo, "Choose a Fierce Deity's Mask Anywhere mode.\n(Remember that FD can be required in logic when FD Anywhere is active!\nConsult the Mystery Settings Document or base .json for added tricks.)\nOff: FD Anywhere is never on.\nOnly When Starting: FD Anywhere is only on when starting with Fierce Deity's Mask.\nSometimes: FD Anywhere is always on when starting with FD, and sometimes on otherwise (45%, by default).\nAlways: FD Anywhere is always on.")
  
    # Density Modes pane
    mainDensityMode = StringVar(value="Normal")
    densityNoCT = StringVar(value="0")
    densityNoPT = StringVar(value="0")
    densityMapCompassMode = StringVar(value="0")
    densityBossKeysMode = StringVar(value="Default")
    mainDensityMode.trace_add("write", updateModeTabs)
    
    densityNormal_radio = ttk.Radiobutton(modeTabDensityMode, text="Normal (default)", variable=mainDensityMode, value="Normal")
    densityLight_radio = ttk.Radiobutton(modeTabDensityMode, text="Light Mystery", variable=mainDensityMode, value="Light")
    densitySuper_radio = ttk.Radiobutton(modeTabDensityMode, text="Super Mystery", variable=mainDensityMode, value="Super")
    densityNoCT_check = ttk.Checkbutton(modeTabDensityMode, text="No Clock Town", variable=densityNoCT)
    densityNoPT_check = ttk.Checkbutton(modeTabDensityMode, text="No Post-Temple", variable=densityNoPT)
    densityMapCompass_check = ttk.Checkbutton(modeTabDensityMode, text="Map and Compass Hints", variable=densityMapCompassMode)
    densityBossKeys_label = ttk.Label(modeTabDensityMode, text="Boss Keys:    ")
    densityBossKeys_combo = ttk.Combobox(modeTabDensityMode, textvariable=densityBossKeysMode, width=25)
    densityBossKeys_combo["values"] = ("Off", "Default", "Always Active (Either Option)", "Always Within Their Temple", "Always Within Any Temple")
    densityBossKeys_combo.state(["readonly"])

    densityNormal_radio.grid(column=1, row=1, sticky=(W,E))
    densityLight_radio.grid(column=2, row=1, sticky=(W,E))
    densitySuper_radio.grid(column=3, row=1, sticky=(W,E))
    densityNoCT_check.grid(column=1, row=2, sticky=(W,E))
    densityNoPT_check.grid(column=1, row=3, sticky=(W,E))
    densityMapCompass_check.grid(column=1, row=4, sticky=(W,E))
    densityBossKeys_label.grid(column=1, row=5, sticky=(W,E))
    densityBossKeys_combo.grid(column=2, row=5, sticky=(W,E))
    densityNormal_tip = Hovertip(densityNormal_radio, "Baseline appearance rates for all categories. See the Category Weights Table for specifics.\nGossip major hint limit (WotHs + foolishes + major always hints) is 12.\nHard option limit is 2.\nActive category minimum is 5.\n(Hard options are Boss Keys Within Any Temple, Frogs with Frog Choir,\nAll Loose Rupees, Full Potsanity, and Full Bombers' Notebook.)")
    densityLight_tip = Hovertip(densityLight_radio, "Excludes certain mystery options with harder or high-quantity checks.\nNo hard options.\nNo Boss Keys, Boss Rooms, Scoopsanity, Shopsanity price randomization,\nfull Hit Spots, full Keaton Grass, or full Tokensanity.\nNo post-temple checks. 1 extra WotH hint.\nMap and Compass Hints is on. No swordless start (by default).")
    densitySuper_tip = Hovertip(densitySuper_radio,"Dramatically increased appearance rates for all categories!\nSongsanity and Long Quests can both be active.\nGossip major hint limit (WotHs + foolishes + major always hints) increased to 14.\nHard option limit increased to 3.\nActive category minimum increased to 8.")
    densityNoCT_tip = Hovertip(densityNoCT_check, "All non-scoop checks in Clock Town regions, including those added by Mystery categories,\nare junked or unshuffled as appropriate.\nThe Bombers' Notebook category is disabled.\nEpona's Song is granted as an additional starting song; Skull Kid Song is always junked.\nBaby Zoras is disabled. Frog Choir can only be active if Frogs are shuffled.")
    densityNoPT_tip = Hovertip(densityNoPT_check, "All post-temple checks, including those added by Mystery categories,\nare junked or unshuffled as appropriate.\nBottle: Deku Princess is never shuffled; other scoops are not affected.\nFrog Choir is disabled.")
    densityMapCompass_tip = Hovertip(densityMapCompass_check, "The Entrances category also shuffles temples' Maps and Compasses\nalongside temple and boss room entrances (respectively).\nThey are placed exclusively in the overworld and will reveal\ntheir corresponding temple or boss entrance shuffle when found.")
    densityBossKeys_tip = Hovertip(densityBossKeys_combo, "Choose a Boss Keys option instead of using the customary Keysanity: Boss Keys roll.\nIf anything but Default is used, Always Within Any Temple won't count against the hard option limit.\nRemember that WotH/Foolish hints ignore Boss Keys in Mystery!\nOff: Boss Keys don't appear. Boss doors are always open.\nDefault: Any other option, at random (65/20/15).\nAlways Active (Either Option): Either active option (20/15).\nAlways Within Their Temple: Boss Keys are on any check in their own temple.\nAlways Within Any Temple: Boss Keys are on any check in any temple.")

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
    customModesSettings["Random Item Mode"] = startRandomItemMode.get()
    customModesSettings["FD Anywhere Mode"] = startFDAnywhereMode.get()
    customModesSettings["Main Density Mode"] = mainDensityMode.get()
    customModesSettings["No Clock Town"] = (densityNoCT.get() == "1")
    customModesSettings["No Post-Temple"] = (densityNoPT.get() == "1")
    customModesSettings["Map and Compass Hints"] = (densityMapCompassMode.get() == "1")
    customModesSettings["Boss Keys"] = densityBossKeysMode.get()

    
    return [(windowForceClosed.get() == "1"),
            baseSettingsFilePath.get(),
            mmrCommandLineExePath.get(),
            (int)(numberToGenerate.get()),
            (makeSettingsOnly.get() == "1"),
            customModesSettings]
