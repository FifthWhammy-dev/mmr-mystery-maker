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

    def browseForBaseSettingsFile(*args):
        baseSettingsFilePath.set(filedialog.askopenfilename())

    def browseForCommandLineExe(*args):
        mmrCommandLineExePath.set(filedialog.askopenfilename())

    guiWindow = Tk()
    guiWindow.title("MMR Mystery Maker " + version_string)

    mainframe = ttk.Frame(guiWindow, padding="8 8 4 8")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    guiWindow.columnconfigure(0, weight=1)
    guiWindow.rowconfigure(0, weight=1)

    windowForceClosed = StringVar(value="0")

    baseSettingsFilePath = StringVar(value="Mystery_Settings_base.json")
    baseSettingsFilePath_entry = ttk.Entry(mainframe, width=70, textvariable=baseSettingsFilePath)
    baseSettingsFilePath_entry.grid(column=2, row=1, sticky=(W, E))
    baseSettingsFilePath_tip = Hovertip(baseSettingsFilePath_entry, "The MMR settings file that's copied and modified\nby Mystery Maker to make mystery seeds.\nThe Mystery_Settings_base.json file comes with Mystery Maker.")

    mmrCommandLineExePath = StringVar(value="MMR.CLI.exe")
    mmrCommandLineExePath_entry = ttk.Entry(mainframe, width=70, textvariable=mmrCommandLineExePath)
    mmrCommandLineExePath_entry.grid(column=2, row=2, sticky=(W, E))
    mmrCommandLineExePath_tip = Hovertip(mmrCommandLineExePath_entry, "The MMR command-line executable that makes playable seed files.\nChanging this should only be needed if you didn't install\nMystery Maker in the same folder as MMR.")

    numberToGenerate = StringVar(value="1")
    numberToGenerate_spinbox = ttk.Spinbox(mainframe, width=5, from_=1, to=100,textvariable=numberToGenerate)
    numberToGenerate_spinbox.grid(column=2, row=3, sticky=W)
    numberToGenerate_tip = Hovertip(numberToGenerate_spinbox, "Setting this above 1 will create many settings/seeds at once, one at a time.")

    makeSettingsOnly = StringVar(value="0")
    makeSettingsOnly_checkbutton = ttk.Checkbutton(mainframe, text="Only make settings file", variable=makeSettingsOnly)
    makeSettingsOnly_checkbutton.grid(column=1, row=4, sticky=E)
    makeSettingsOnly_tip = Hovertip(makeSettingsOnly_checkbutton, "When checked, Mystery Maker only generates a .json file\nwhich can be loaded manually in MMR to make a playable seed.")

    ttk.Button(mainframe, text="Browse...", command=browseForBaseSettingsFile).grid(column=3, row=1, sticky=W)
    ttk.Button(mainframe, text="Browse...", command=browseForCommandLineExe).grid(column=3, row=2, sticky=W)
    ttk.Button(mainframe, text="Randomize", command=guiStartRandomize).grid(column=3, row=4, sticky=W)

    ttk.Label(mainframe, text="Custom base MMR settings file:").grid(column=1, row=1, sticky=E)
    ttk.Label(mainframe, text="Custom path to MMR.CLI.exe:").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="# of seeds:").grid(column=1, row=3, sticky=E)

    modeTabs_notebook = ttk.Notebook(mainframe)
    modeTabGoalMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabGoalMode.grid(column=0, row=0, sticky=(N,W,S,E))
    modeTabStartMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabStartMode.grid(column=0, row=0, sticky=(N,W,S,E))    
    modeTabDensityMode = ttk.Frame(modeTabs_notebook, padding="4 4 4 4")
    modeTabs_notebook.add(modeTabGoalMode, text="Goal Mode")
    modeTabs_notebook.add(modeTabStartMode, text="Start Mode")
    modeTabs_notebook.add(modeTabDensityMode, text="Density Modes")
    modeTabs_notebook.grid(column=1, row=0, columnspan=3, sticky=(W, E))

    goalMode = StringVar(value="Normal")
    goalNormal_radio = ttk.Radiobutton(modeTabGoalMode, text="Normal (default)", variable=goalMode, value="Normal")
    goalNoBlitz_radio = ttk.Radiobutton(modeTabGoalMode, text="No Blitz", variable=goalMode, value="No Blitz")
    goalBlitz1_radio = ttk.Radiobutton(modeTabGoalMode, text="Blitz 1", width=20, variable=goalMode, value="Blitz 1")
    goalBlitz2_radio = ttk.Radiobutton(modeTabGoalMode, text="Blitz 2", variable=goalMode, value="Blitz 2")
    goalRS_radio = ttk.Radiobutton(modeTabGoalMode, text="Remains Shuffle", variable=goalMode, value="Remains Shuffle")
    goalNPRS_radio = ttk.Radiobutton(modeTabGoalMode, text="Normal + Remains Shuffle", variable=goalMode, value="Normal + Remains Shuffle")
    goalTFH_radio = ttk.Radiobutton(modeTabGoalMode, text="Five Fairy Hunt", variable=goalMode, value="Five Fairy Hunt")
    goalFFH_radio = ttk.Radiobutton(modeTabGoalMode, text="Full Fairy Hunt", variable=goalMode, value="Full Fairy Hunt")
    goalNormal_radio.grid(column=1, row=1, sticky=(W, E))
    goalNoBlitz_radio.grid(column=2, row=1, sticky=(W, E))
    goalBlitz1_radio.grid(column=3, row=1, sticky=(W, E))
    goalBlitz2_radio.grid(column=4, row=1, sticky=(W, E))
    goalRS_radio.grid(column=1, row=2, sticky=(W, E))
    goalNPRS_radio.grid(column=2, row=2, sticky=(W, E))
    goalTFH_radio.grid(column=1, row=3, sticky=(W, E))
    goalFFH_radio.grid(column=1, row=4, sticky=(W, E))
    goalNormal_tip = Hovertip(goalNormal_radio, "Remains on bosses. May start with one or two remains,\nwith corresponding temples and post-temples junked.\nDefault weights are 65/25/10 for 0/1/2 starting remains.")
    goalNoBlitz_tip = Hovertip(goalNoBlitz_radio, "Remains on bosses. Always start without any remains.")
    goalBlitz1_tip = Hovertip(goalBlitz1_radio, "Remains on bosses. Always start with one remains;\nits temple and post-temple checks are junked.")
    goalBlitz2_tip = Hovertip(goalBlitz2_radio, "Remains on bosses. Always start with two remains;\ntheir temple and post-temple checks are junked.")
    goalRS_tip = Hovertip(goalRS_radio, "Remains shuffled anywhere. C-Up at clock tower door for region hints.")
    goalNPRS_tip = Hovertip(goalNPRS_radio, "Choose any normal goal mode (wgt 45/25/10)\nor Remains Shuffle (wgt 20).")
    goalTFH_tip = Hovertip(goalTFH_radio, "Remains on Great Fairy Rewards.\nAll Stray Fairies shuffled and five Stray Fairies of each color are placed:\nfind and turn in one set to win immediately!\nAlways start with Epona, Lullaby, and the other 40 fairies.\nSkull Kid Song is junked, and Baby Zoras are disabled.\nTemple locations always shuffled. Boss Keys and Boss Rooms never shuffled.\nFairy Fountains hint fairy regions. No WotHs, no foolishes.")
    goalFFH_tip = Hovertip(goalFFH_radio, "Remains on Great Fairy Rewards.\nAll Stray Fairies always shuffled: find and turn in all 60, then beat Majora!\nFairy Fountains hint fairy regions. No WotHs, no foolishes.")

    startMode = StringVar(value="Default")
    startDefault_radio = ttk.Radiobutton(modeTabStartMode, text="Default Start", variable=startMode, value="Default")
    startGenerous_radio = ttk.Radiobutton(modeTabStartMode, text="Generous Start", variable=startMode, value="Generous")
    startStandard_radio = ttk.Radiobutton(modeTabStartMode, text="Standard Start", variable=startMode, value="Standard")
    startSwordless_radio = ttk.Radiobutton(modeTabStartMode, text="Swordless Start", variable=startMode, value="Swordless")
    startFragile_radio = ttk.Radiobutton(modeTabStartMode, text="Fragile Start", variable=startMode, value="Fragile")
    startCruel_radio = ttk.Radiobutton(modeTabStartMode, text="Cruel Start", variable=startMode, value="Cruel")
    startDefault_radio.grid(column=1, row=1, sticky=(W,E))
    startGenerous_radio.grid(column=1, row=2, sticky=(W,E))
    startStandard_radio.grid(column=2, row=2, sticky=(W,E))
    startSwordless_radio.grid(column=1, row=3, sticky=(W,E))
    startFragile_radio.grid(column=2, row=3, sticky=(W,E))
    startCruel_radio.grid(column=3, row=3, sticky=(W,E))
    startDefault_tip = Hovertip(startDefault_radio, "Occasionally start without Kokiri Sword or Hero's Shield (25%, by default).")
    startGenerous_tip = Hovertip(startGenerous_radio, "Always start with Razor Sword and Hero's Shield,\nplus Spin Attack Mastery and Double Defense.")
    startStandard_tip = Hovertip(startStandard_radio, "Always start with Kokiri Sword and Hero's Shield.")
    startSwordless_tip = Hovertip(startSwordless_radio, "Always start without Kokiri Sword and Hero's Shield.")
    startFragile_tip = Hovertip(startFragile_radio, "Always start without Kokiri Sword and Hero's Shield, and with only one heart.\nFierce Deity's Mask and Great Fairy's Sword are removed from the Starting Random Item pool.\nCrit Wiggle is disabled.")
    startCruel_tip = Hovertip(startCruel_radio, "Always start without Kokiri Sword and Hero's Shield, and with only one heart.\nStarting Random Item is disabled.\nFierce Deity's Mask is not shuffled.\nLink takes double damage!")

    densityNoCT = StringVar(value="0")
    densityNoPT = StringVar(value="0")
    mainDensityMode = StringVar(value="Normal")
    densityNormal_radio = ttk.Radiobutton(modeTabDensityMode, text="Normal (default)", variable=mainDensityMode, value="Normal")
    densityLight_radio = ttk.Radiobutton(modeTabDensityMode, text="Light", variable=mainDensityMode, value="Light")
    densitySuper_radio = ttk.Radiobutton(modeTabDensityMode, text="Super", variable=mainDensityMode, value="Super")
    densityNoCT_checkbutton = ttk.Checkbutton(modeTabDensityMode, text="No Clock Town", variable=densityNoCT)
    densityNoPT_checkbutton = ttk.Checkbutton(modeTabDensityMode, text="No Post-Temple", variable=densityNoPT)
    densityNormal_radio.grid(column=1, row=1, sticky=(W,E))
    densityLight_radio.grid(column=2, row=1, sticky=(W,E))
    densitySuper_radio.grid(column=3, row=1, sticky=(W,E))
    densityNoCT_checkbutton.grid(column=1, row=2, sticky=(W,E))
    densityNoPT_checkbutton.grid(column=1, row=3, sticky=(W,E))
    densityNoCT_tip = Hovertip(densityNoCT_checkbutton, "All non-scoop checks in Clock Town regions, including those added by Mystery categories,\nare junked or unshuffled as appropriate.\nThe Bombers' Notebook category is disabled.\nEpona's Song is granted as an additional starting item; Skull Kid Song is always junked.\nBaby Zoras is disabled. Frog Choir can only be active if Frogs are shuffled.")
    densityNoPT_tip = Hovertip(densityNoPT_checkbutton, "All post-temple checks, including those added by Mystery categories,\nare junked or unshuffled as appropriate.\nBottle: Deku Princess is never shuffled; other scoops are not affected.\nFrog Choir is disabled.")

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    baseSettingsFilePath_entry.focus()
    guiWindow.protocol("WM_DELETE_WINDOW", guiCloseButton)
    guiWindow.bind("<Return>", guiStartRandomize)

    guiWindow.mainloop()
    customModesSettings = dict()
    customModesSettings["Goal Mode"] = goalMode.get()
    customModesSettings["Start Mode"] = startMode.get()
    customModesSettings["Main Density Mode"] = mainDensityMode.get()
    customModesSettings["No Clock Town"] = (densityNoCT.get() == "1")
    customModesSettings["No Post-Temple"] = (densityNoPT.get() == "1")
    
    return [(windowForceClosed.get() == "1"),
            baseSettingsFilePath.get(),
            mmrCommandLineExePath.get(),
            (int)(numberToGenerate.get()),
            (makeSettingsOnly.get() == "1"),
            customModesSettings]
