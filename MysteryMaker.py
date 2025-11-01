import json
import random
import subprocess
import argparse
import os
import sys
from mysteryutils.MysteryMakerGUI import openOptionsGui

MYSTERY_MAKER_VERSION = "v5.0"

MODE_DEFAULTS = {"Goal Mode":"No Blitz",
                 "Long Goal":"None",
                 "Direct to Credits":False,
                 "Start Mode":"Default",
                 "Song Layout":"Any (Default)",
                 "All Moon Trials":False,
                 "Early Moon Access Remains":1,
                 "Blitz Remains Count":False,
                 "Random Item Mode":"Any (Default)",
                 "FD Anywhere Mode":"Sometimes (Default)",
                 "Dungeon Entrances":"Sometimes (Default)",
                 "Boss Keys":"Off (Default)",
                 "Small Keys":"Sometimes (Default)",
                 "Main Density Mode":"Normal",
                 "Category Minimum":6,
                 "No Clock Town":False,
                 "No Post-Temple":False,
                 "Map and Compass Hints":False,
                 "Potsanity":"Default",
                 "Scoopsanity":"Default",
                 "Vanilla Eggs for Baby Zoras":True,
                 "Stubborn Princess":False,
                 "No Iceless FD Logic":False,
                 "No Importance Count":False,
                 "Sun's Song":False}

def CheckForCustom(modeSettings):
    for mode in modeSettings:
        if modeSettings[mode] != MODE_DEFAULTS[mode]:
            return True
    
    return False

def AddEntryToListString(liststring, word, value):
    bitstringWords = liststring.split("-")
    bitstringWords.reverse()
    existingWord = bitstringWords[word]
    if existingWord == '':
        existingWord = '0'
    bitstringWords[word] = hex(int(existingWord,16) | int(value,16))[2:]
    bitstringWords.reverse()
    return "-".join(bitstringWords)

def RemoveEntryFromListString(liststring, word, value):
    bitstringWords = liststring.split("-")
    bitstringWords.reverse()
    existingWord = bitstringWords[word]
    if existingWord == '':
        existingWord = '0'
    if int(existingWord,16) | int(value,16) == int(existingWord,16):
        bitstringWords[word] = hex(int(existingWord,16) - int(value,16))[2:]
    bitstringWords.reverse()
    return "-".join(bitstringWords)

def CheckEntryInListString(liststring, word, value):
    bitstringWords = liststring.split("-")
    bitstringWords.reverse()
    existingWord = bitstringWords[word]
    if existingWord == '':
        existingWord = '0'
    if int(existingWord,16) | int(value,16) == int(existingWord,16):
        return True
    else:
        return False

def AddStringToListString(liststring, newstring):
    liststringWords = liststring.split("-")
    newstringWords = newstring.split("-")
    for i in range(min([len(liststringWords),len(newstringWords)])):
        if (liststringWords[i] != '' or newstringWords[i] != ''):
            if liststringWords[i] == '':
                liststringWords[i] = '0'
            if newstringWords[i] == '':
                newstringWords[i] = '0'
            liststringWords[i] = hex(int(liststringWords[i],16) |
                                     int(newstringWords[i],16))[2:]
            if liststringWords[i] == '0':
                liststringWords[i] = ''
    return "-".join(liststringWords)

def RemoveStringFromListString(liststring, newstring):
    liststringWords = liststring.split("-")
    newstringWords = newstring.split("-")
    for i in range(min([len(liststringWords),len(newstringWords)])):
        if (liststringWords[i] != '' or newstringWords[i] != ''):
            if liststringWords[i] == '':
                liststringWords[i] = '0'
            if newstringWords[i] == '':
                newstringWords[i] = '0'
            liststringWords[i] = hex((int(liststringWords[i],16) ^
                                     int(newstringWords[i],16)) &
                                     int(liststringWords[i],16))[2:]
            if liststringWords[i] == '0':
                liststringWords[i] = ''
    return "-".join(liststringWords)

def CheckStringInListString(liststring, newstring):
    liststringWords = liststring.split("-")
    newstringWords = newstring.split("-")
    for i in range(min([len(liststringWords),len(newstringWords)])):
        if (liststringWords[i] != '' or newstringWords[i] != ''):
            if liststringWords[i] == '':
                liststringWords[i] = '0'
            if newstringWords[i] == '':
                newstringWords[i] = '0'
            if (int(liststringWords[i],16) | int(newstringWords[i],16)) != int(liststringWords[i],16):
                return False
    return True

def FilenameOnly(pathstring):
    filename = pathstring[(pathstring.rfind("/") + 1):]
    filename = filename[(filename.rfind("\\") + 1):]
    return filename
    
def GenerateMysterySettings(inputFilename, customModes, outputSuffix="output"):
    random.seed()

    with open(inputFilename, "r") as read_file:
        data = json.load(read_file)

    settings = data["GameplaySettings"]
    itemListString = settings["CustomItemListString"]
    startListString = settings["CustomStartingItemListString"]
    junkListString = settings["CustomJunkLocationsString"]
     
    # gossipHintsTakenByAlways = 4 + settings["OverrideNumberOfRequiredGossipHints"] + settings["OverrideNumberOfNonRequiredGossipHints"]
    # GOSSIP_HINTS_LIMIT = 12  # intentionally two less than the 14 gossip slots available
    # if (customModes["No Post-Temple"] == True):
    #    gossipHintsTakenByAlways -= 3

    nonzeroCategories = 0
    NONZERO_CATEGORIES_MINIMUM = customModes["Category Minimum"]

    moonAccessRemainsRequirement = customModes["Early Moon Access Remains"]

    #hardOptions = 0
    #HARD_OPTIONS_LIMIT = 2

    if customModes["Main Density Mode"] == "Light":
    #    HARD_OPTIONS_LIMIT = 0
        settings["OverrideNumberOfRequiredGossipHints"] += 1
    #    gossipHintsTakenByAlways += 1
        if NONZERO_CATEGORIES_MINIMUM > 8:
            NONZERO_CATEGORIES_MINIMUM = 8
    #if customModes["Main Density Mode"] == "Super":
    #    HARD_OPTIONS_LIMIT = 3
    #    GOSSIP_HINTS_LIMIT = 14
    
    wgtsStartingBossRemains = [100,0,0,0,0,0,0,0,0,0]    
    if (customModes["Goal Mode"] == "No Blitz"):
        wgtsStartingBossRemains = [100,0,0,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Blitz 1"):
        wgtsStartingBossRemains = [0,100,0,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Blitz 2"):
        wgtsStartingBossRemains = [0,0,100,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Remains Shuffle"):
        wgtsStartingBossRemains = [0,0,0,100,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Five Fairy Hunt"):
        wgtsStartingBossRemains = [0,0,0,0,100,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Any Three Remains"):
        wgtsStartingBossRemains = [0,0,0,0,0,100,0,0,0,0]
    if (customModes["Goal Mode"] == "No Blitz 2"):
        wgtsStartingBossRemains = [85,15,0,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Two to Four Remains"):
        wgtsStartingBossRemains = [65,25,10,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Normal + Remains Shuffle"):
        wgtsStartingBossRemains = [45,25,10,20,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Grab Bag"):
        wgtsStartingBossRemains = [11,11,11,33,33,0,0,0,0,0]
    if (customModes["Long Goal"] == "Full Fairy Hunt"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,100,0,0,0]
    if (customModes["Long Goal"] == "Mask Hunt"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,0,100,0,0]
    if (customModes["Long Goal"] == "Skull Tokens"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,0,0,100,0]
    if (customModes["Long Goal"] == "Hearts"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,0,0,0,100]
    catStartingBossRemains = random.choices(["Normal","Blitz 1","Blitz 2","Remains Shuffle","Five Fairy Hunt","Any Three Remains","Full Fairy Hunt","Mask Hunt","Skull Tokens","Hearts"], wgtsStartingBossRemains)
    if catStartingBossRemains[0] == "Normal":
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, FourBossRemains"
        else:
            settings["VictoryMode"] = "CantFightMajora, FourBossRemains"  
    if catStartingBossRemains[0] == "Blitz 1":
        settings["BossRemainsMode"] = "Blitz1"
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, ThreeBossRemains"
        else:
            settings["VictoryMode"] = "CantFightMajora, ThreeBossRemains"
        if (customModes["Blitz Remains Count"] == False):
            moonAccessRemainsRequirement = min(4, moonAccessRemainsRequirement + 1)
    if catStartingBossRemains[0] == "Blitz 2":
        settings["BossRemainsMode"] = "Blitz2"
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, TwoBossRemains"            
        else:
            settings["VictoryMode"] = "CantFightMajora, TwoBossRemains"
        if (customModes["Blitz Remains Count"] == False):
            moonAccessRemainsRequirement = min(4, moonAccessRemainsRequirement + 2)
    if catStartingBossRemains[0] == "Any Three Remains":
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, ThreeBossRemains"
        else:
            settings["VictoryMode"] = "CantFightMajora, ThreeBossRemains"
        settings["RequiredBossRemains"] = 3
        if moonAccessRemainsRequirement > 3:
            moonAccessRemainsRequirement = 3
    if catStartingBossRemains[0] == "Remains Shuffle":
        itemListString = AddStringToListString(itemListString,
                                               "-----f00000--------------------------------")       # shuffle Boss Remains
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, FourBossRemains"
        else:
            settings["VictoryMode"] = "CantFightMajora, FourBossRemains"
    if catStartingBossRemains[0] == "Five Fairy Hunt" or catStartingBossRemains[0] == "Full Fairy Hunt":
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        settings["BossRemainsMode"] = "GreatFairyRewards"
        settings["StrayFairyMode"] = "Default"
        junkListString = RemoveStringFromListString(junkListString,
                                                    "-------------------------------------f000")    # unjunk temple Great Fairies
        itemListString = AddStringToListString(itemListString,
                                               "-----f00000--------------------------------")       # shuffle Boss Remains
        startListString = AddEntryToListString(startListString, 1, "20")                            # start with Great Fairy's Mask
        settings["FairyMaskShimmer"] = True
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        startListString = AddStringToListString(startListString,
                                                "7fe-ffc1ff8-3ff00000--")                           # start with 10 stray fairies from each set
        settings["VictoryMode"] = "DirectToCredits, OneBossRemains"
        itemListString = RemoveEntryFromListString(itemListString,3,"1")                            # junk Skull Kid Song
    if catStartingBossRemains[0] == "Full Fairy Hunt":
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, FourBossRemains"
        else:
            settings["VictoryMode"] = "CantFightMajora, FourBossRemains"
    if catStartingBossRemains[0] == "Mask Hunt":
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        settings["RequiredBossRemains"] = moonAccessRemainsRequirement
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, CantFightMajora, NonTransformationMasks, TransformationMasks"
        else:
            settings["VictoryMode"] = "CantFightMajora, NonTransformationMasks, TransformationMasks"
    if catStartingBossRemains[0] == "Skull Tokens":
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, CantFightMajora, SkullTokens"
        else:
            settings["VictoryMode"] = "CantFightMajora, SkullTokens"
    if catStartingBossRemains[0] == "Hearts":
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
    #    gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, CantFightMajora, Hearts"
        else:
            settings["VictoryMode"] = "CantFightMajora, Hearts"
                                                    
    wgtsSongLayout = [25,35,10,30]
    if customModes["Song Layout"] == "Traditional":
        wgtsSongLayout = [100,0,0,0]
    elif customModes["Song Layout"] == "Songsanity":
        wgtsSongLayout = [0,100,0,0]
    elif customModes["Song Layout"] == "Baby Zoras":
        wgtsSongLayout = [0,0,100,0]
    elif customModes["Song Layout"] == "Moon Oath":
        wgtsSongLayout = [0,0,0,100]
    elif customModes["Song Layout"] == "Any Non-Moon":
        wgtsSongLayout = [55,35,10,0]
    if (moonAccessRemainsRequirement >= 4) or (moonAccessRemainsRequirement == 3 and catStartingBossRemains[0] == "Any Three Remains") or (catStartingBossRemains[0] == "Five Fairy Hunt"):
        wgtsSongLayout[0] += wgtsSongLayout[3]
        wgtsSongLayout[3] = 0
    if (catStartingBossRemains[0] == "Five Fairy Hunt"):
        wgtsSongLayout[0] += wgtsSongLayout[2]
        wgtsSongLayout[2] = 0
    if catStartingBossRemains[0] == "Mask Hunt":
        wgtsSongLayout = [0,0,0,100]
    catSongLayout = random.choices(["Traditional","Songsanity","Baby Zoras","Moon Oath"],wgtsSongLayout)
    if catSongLayout[0] == "Traditional":
        junkListString = RemoveEntryFromListString(junkListString,2,"400000")                                       # unjunk Anju and Kafei
        #settings["OverrideHintPriorities"][0].append("MaskCouple")                                                 # always hint A&K (redundant)
    elif catSongLayout[0] == "Songsanity":
        settings["AddSongs"] = True
        itemListString = RemoveEntryFromListString(itemListString,3,"1")                                            # unshuffle Skull Kid Song
        settings["OverrideHintPriorities"][3].append("SongEpona")                                                   # backup hint Romani's Game
        settings["OverrideHintPriorities"][3].append("SongElegy")                                                   # backup hint Ikana King
        if (settings["OverrideNumberOfRequiredGossipHints"] > 0):
            settings["OverrideNumberOfRequiredGossipHints"] += 1                                                    # IC +1 (unless in an IC-less goal mode)
    elif catSongLayout[0] == "Baby Zoras":
        itemListString = RemoveEntryFromListString(itemListString,3,"1")                                            # unshuffle Skull Kid Song
        junkListString = RemoveEntryFromListString(junkListString,3,"80")                                           # unjunk Baby Zoras
        #settings["OverrideHintPriorities"][0].append("SongNewWaveBossaNova")                                       # always hint BZ (redundant)        
    elif catSongLayout[0] == "Moon Oath":
        startListString = AddEntryToListString(startListString,2,"2")                                               # start with Oath to Order
        itemListString = RemoveEntryFromListString(itemListString,3,"1")                                            # unshuffle Skull Kid Song
        junkListString = RemoveEntryFromListString(junkListString,2,"400000")                                       # Anju and Kafei
        #settings["OverrideHintPriorities"][0].append("MaskCouple")                                                 # always hint A&K (redundant)
        settings["RequiredBossRemains"] = moonAccessRemainsRequirement                                              # set Remains for Moon Access (default 1 + blitz)
        if (customModes["All Moon Trials"]):
            itemListString = AddStringToListString(itemListString,"----------------f000000--------------de0000-------") # Moon Trial PoHs, chests, and pots [10, 1r]
        else:
            itemListString = AddStringToListString(itemListString,"----------------f000000--------------d00000-------") # Just the Link Trial PoH, chests, and pots [7, 1r]


    wgtsStartingSwordShield = [75,25,0,0,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsStartingSwordShield = [100,0,0,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsStartingSwordShield = [50,50,0,0,0]
    if (customModes["Start Mode"] == "Kokiri"):
        wgtsStartingSwordShield = [100,0,0,0,0]
    if (customModes["Start Mode"] == "Swordless"):
        wgtsStartingSwordShield = [0,100,0,0,0]
    if (customModes["Start Mode"] == "Strong"):
        wgtsStartingSwordShield = [0,0,100,0,0]
    if (customModes["Start Mode"] == "Fragile"):
        wgtsStartingSwordShield = [0,0,0,100,0]
    if (customModes["Start Mode"] == "Cruel"):
        wgtsStartingSwordShield = [0,0,0,0,100]
    catStartingSwordShield = random.choices(["Normal","No sword or shield","Strong Start","Fragile Start","Cruel Start"],wgtsStartingSwordShield)
    if catStartingSwordShield[0] == "No sword or shield":
        itemListString = AddEntryToListString(itemListString,7,"4000000")
        itemListString = AddEntryToListString(itemListString,7,"2000000")
    if catStartingSwordShield[0] == "Strong Start":
        startListString = AddStringToListString(startListString,"--40000--805000")
    if catStartingSwordShield[0] == "Fragile Start":
        itemListString = AddStringToListString(itemListString,"------------------------------1e000000-------")
        settings["CritWiggleDisable"] = True
    if catStartingSwordShield[0] == "Cruel Start":
        itemListString = AddStringToListString(itemListString,"------------------------------1e000000-------")
        if catStartingBossRemains[0] != "Mask Hunt":
            itemListString = RemoveEntryFromListString(itemListString,7,"200000")   # unshuffle FD
        if (settings["DamageMode"] == "Default"):
            settings["DamageMode"] = "Double"

    catStartingRandomItem = 0
    wgtsStartingRandomItem = [0,10,10,10,10,10,10,5,5,10,10,5,5,0]
    if customModes["Random Item Mode"] == "Any Transformation Mask":
        wgtsStartingRandomItem = [0,10,10,10,10,0,0,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Any Non-Transformation":
        wgtsStartingRandomItem = [0,0,0,0,0,10,10,5,5,10,10,5,5,0]
    if catStartingSwordShield[0] == "Fragile Start":
        wgtsStartingRandomItem[4] = 0
        wgtsStartingRandomItem[12] = 0
    if customModes["Random Item Mode"] == "Deku Mask":
        wgtsStartingRandomItem = [0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Goron Mask":
        wgtsStartingRandomItem = [0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Zora Mask":
        wgtsStartingRandomItem = [0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Fierce Deity's Mask":
        wgtsStartingRandomItem = [0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Bow":
        wgtsStartingRandomItem = [0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Hookshot":
        wgtsStartingRandomItem = [0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Bomb Bag":
        wgtsStartingRandomItem = [0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Blast Mask":
        wgtsStartingRandomItem = [0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    if customModes["Random Item Mode"] == "Adult's Wallet":
        wgtsStartingRandomItem = [0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    if customModes["Random Item Mode"] == "Empty Bottle (Dampe's)":
        wgtsStartingRandomItem = [0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    if customModes["Random Item Mode"] == "Bunny Hood":
        wgtsStartingRandomItem = [0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    if customModes["Random Item Mode"] == "Great Fairy's Sword":
        wgtsStartingRandomItem = [0,0,0,0,0,0,0,0,0,0,0,0,1,0]    
    if catStartingSwordShield[0] == "Cruel Start" or customModes["Random Item Mode"] == "Off":
        wgtsStartingRandomItem = [100,0,0,0,0,0,0,0,0,0,0,0,0,0]
    catStartingRandomItem = random.choices(["None",
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
                                            "Great Fairy's Sword",
                                            "Magic"],
                                            wgtsStartingRandomItem)  
    if catStartingRandomItem[0] == "Deku Mask":
        startListString = AddEntryToListString(startListString,0,"1")
    if catStartingRandomItem[0] == "Goron Mask":
        startListString = AddEntryToListString(startListString,1,"200000")
    if catStartingRandomItem[0] == "Zora Mask":
        startListString = AddEntryToListString(startListString,1,"400000")
    if catStartingRandomItem[0] == "Fierce Deity's Mask":
        startListString = AddEntryToListString(startListString,2,"20000")
    if catStartingRandomItem[0] == "Bow":
        startListString = AddEntryToListString(startListString,0,"2")
    if catStartingRandomItem[0] == "Hookshot":
        startListString = AddEntryToListString(startListString,0,"400")
    if catStartingRandomItem[0] == "Magic":
        startListString = AddEntryToListString(startListString,0,"800")
    if catStartingRandomItem[0] == "Bomb Bag":
        startListString = AddEntryToListString(startListString,0,"20")
    if catStartingRandomItem[0] == "Blast Mask":
        startListString = AddEntryToListString(startListString,1,"8")
    if catStartingRandomItem[0] == "Empty Bottle (Dampe's)":
        startListString = AddEntryToListString(startListString,0,"100000")
    if catStartingRandomItem[0] == "Great Fairy's Sword":
        startListString = AddEntryToListString(startListString,0,"8000")
    if catStartingRandomItem[0] == "Adult's Wallet":
        startListString = AddEntryToListString(startListString,0,"40000000")
    if catStartingRandomItem[0] == "Bunny Hood":
        startListString = AddEntryToListString(startListString,1,"100")

    wgtsStartingRandomSong = [0,60,0,0,0,0,0,0,0,40]
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        wgtsStartingRandomSong = [0,0,0,0,0,100,0,0,0,0]   
    if catStartingBossRemains[0] == "Five Fairy Hunt" or (customModes["No Clock Town"]):
        wgtsStartingRandomSong[1] = 0
        startListString = AddEntryToListString(startListString,1,"8000000")     # add Epona's Song
        itemListString = RemoveEntryFromListString(itemListString,3,"1")        # unshuffle Skull Kid Song
    if (customModes["No Clock Town"]) and (catSongLayout[0] == "Baby Zoras" or catSongLayout[0] == "Moon Oath"):
        junkListString = AddEntryToListString(junkListString,3,"300")           # junk Boss Blue Warp (to make room for either the Baby Zoras check or the free Oath)

    catStartingRandomSong = random.choices(["None",
                                            "Epona's Song",
                                            "Song of Healing",
                                            "Song of Storms",
                                            "Sonata of Awakening",
                                            "Goron Lullaby",
                                            "New Wave Bossa Nova",
                                            "Elegy of Emptiness",
                                            "Oath to Order",
                                            "Not Epona or Oath"],
                                           wgtsStartingRandomSong)
    if catStartingRandomSong[0] == "Not Epona or Oath":
        catStartingRandomSong = random.choices(["Song of Healing",
                                                "Song of Storms",
                                                "Sonata of Awakening",
                                                "Goron Lullaby",
                                                "New Wave Bossa Nova",
                                                "Elegy of Emptiness"],
                                                [1,1,1,1,1,1])     
    if catStartingRandomSong[0] == "Epona's Song":
        startListString = AddEntryToListString(startListString,1,"8000000")
    if catStartingRandomSong[0] == "Song of Healing":
        startListString = AddEntryToListString(startListString,1,"2000000")
    if catStartingRandomSong[0] == "Song of Storms":
        startListString = AddEntryToListString(startListString,1,"10000000")
    if catStartingRandomSong[0] == "Sonata of Awakening":
        startListString = AddEntryToListString(startListString,1,"20000000")
    if catStartingRandomSong[0] == "Goron Lullaby":
        startListString = AddEntryToListString(startListString,1,"40000000")
    if catStartingRandomSong[0] == "New Wave Bossa Nova":
        startListString = AddEntryToListString(startListString,1,"80000000")
    if catStartingRandomSong[0] == "Elegy of Emptiness":
        startListString = AddEntryToListString(startListString,2,"1")
    if catStartingRandomSong[0] == "Oath to Order":
        startListString = AddEntryToListString(startListString,2,"2")

    wgtsFierceDeityAnywhere = [50,50]
    if customModes["FD Anywhere Mode"] == "Only When Starting":
        wgtsFierceDeityAnywhere = [100,0]
    if customModes["FD Anywhere Mode"] == "Always" or catStartingRandomItem[0] == "Fierce Deity's Mask":
        wgtsFierceDeityAnywhere = [0,100]
    if customModes["FD Anywhere Mode"] == "Off" or catStartingSwordShield[0] == "Cruel Start":
        wgtsFierceDeityAnywhere = [100,0]
    catFierceDeityAnywhere = random.choices(["Off","Active"], wgtsFierceDeityAnywhere)
    if catFierceDeityAnywhere[0] == "Active":
        settings["AllowFierceDeityAnywhere"] = True

    wgtsEntrancesTemples = [50,50]
    if customModes["Dungeon Entrances"] == "Off":
        wgtsEntrancesTemples = [100,0]
    if customModes["Dungeon Entrances"] == "Sometimes (Default)":
        wgtsEntrancesTemples = [50,50]
    if customModes["Dungeon Entrances"] == "Always":
        wgtsEntrancesTemples = [0,100]
    wgtsEntrancesBossRooms = [100,0]
    # wgtsEntrancesBossRooms = [70,30]
    if customModes["Main Density Mode"] == "Light":
        wgtsEntrancesBossRooms = [100,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsEntrancesTemples = [100,0]
        #wgtsEntrancesBossRooms = [40,60]
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        wgtsEntrancesTemples = [0,100]
        wgtsEntrancesBossRooms = [100,0]
    catEntrancesTemples = random.choices(["---","Shuffled"], wgtsEntrancesTemples)
    if catEntrancesTemples[0] == "Shuffled":
        settings["RandomizeDungeonEntrances"] = True
        if customModes["Map and Compass Hints"]:
            startListString = RemoveStringFromListString(startListString,
                                                         "--154--")         # don't start with temple maps; shuffle them instead
    catEntrancesBossRooms = random.choices(["---","Shuffled"], wgtsEntrancesBossRooms)
    if catEntrancesBossRooms[0] == "Shuffled":
        settings["RandomizeBossRooms"] = True
        if customModes["Map and Compass Hints"]:
            startListString = RemoveStringFromListString(startListString,
                                                         "--2a8--")         # don't start with temple compasses; shuffle them instead

    wgtsKeysanityBossKeys = [100,0,0,0,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    if customModes["Boss Keys"] == "Off (Default)":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    if customModes["Boss Keys"] == "Sometimes":
        wgtsKeysanityBossKeys = [65,20,15,0,0]
    if customModes["Boss Keys"] == "Always Within Their Temple":
        wgtsKeysanityBossKeys = [0,100,0,0,0]
    if customModes["Boss Keys"] == "Always Within Any Temple":
        wgtsKeysanityBossKeys = [0,0,100,0,0]
    if customModes["Boss Keys"] == "Anywhere Within Their Area":
        wgtsKeysanityBossKeys = [0,0,0,100,0]
    if customModes["Boss Keys"] == "Anywhere":
        wgtsKeysanityBossKeys = [0,0,0,0,100]
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    #if hardOptions >= HARD_OPTIONS_LIMIT and customModes["Boss Keys"] == "Default":
    #    wgtsKeysanityBossKeys[1] += wgtsKeysanityBossKeys[2]
    #    wgtsKeysanityBossKeys[2] = 0
    catKeysanityBossKeys = random.choices(["---",
                                           "Shuffled within their temple",
                                           "Shuffled within any temple",
                                           "Shuffled within area",
                                           "Shuffled anywhere"],
                                          wgtsKeysanityBossKeys)
    if catKeysanityBossKeys[0] == "Shuffled within their temple":
        settings["BossKeyMode"] = "KeepWithinArea, KeepWithinTemples, KeepThroughTime"
    if catKeysanityBossKeys[0] == "Shuffled within any temple":
        settings["BossKeyMode"] = "KeepWithinTemples, KeepThroughTime"
    #    if customModes["Boss Keys"] == "Default":
    #        hardOptions += 1
    if catKeysanityBossKeys[0] == "Shuffled within area":
        settings["BossKeyMode"] = "KeepWithinArea, KeepThroughTime"
    if catKeysanityBossKeys[0] == "Shuffled anywhere":
        settings["BossKeyMode"] = "KeepThroughTime"

    wgtsKeysanitySmallKeys = [65,20,15,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsKeysanitySmallKeys = [40,30,30,0,0]
    if customModes["Small Keys"] == "Off":
        wgtsKeysanitySmallKeys = [100,0,0,0,0]
    if customModes["Small Keys"] == "Sometimes (Default)":
        wgtsKeysanitySmallKeys = [65,20,15,0,0]
    if customModes["Small Keys"] == "Always Within Their Temple":
        wgtsKeysanitySmallKeys = [0,100,0,0,0]
    if customModes["Small Keys"] == "Always Within Any Temple":
        wgtsKeysanitySmallKeys = [0,0,100,0,0]
    if customModes["Small Keys"] == "Anywhere Within Their Area":
        wgtsKeysanitySmallKeys = [0,0,0,100,0]
    if customModes["Small Keys"] == "Anywhere":
        wgtsKeysanitySmallKeys = [0,0,0,0,100]
    catKeysanitySmallKeys = random.choices(["---",
                                            "Shuffled within their temple",
                                            "Shuffled within any temple",
                                            "Shuffled within area",
                                            "Shuffled anywhere"],
                                           wgtsKeysanitySmallKeys)
    if catKeysanitySmallKeys[0] == "Shuffled within their temple":
        settings["SmallKeyMode"] = "KeepWithinArea, KeepWithinTemples, KeepThroughTime"
    if catKeysanitySmallKeys[0] == "Shuffled within any temple":
        settings["SmallKeyMode"] = "KeepWithinTemples, KeepThroughTime"
    if catKeysanitySmallKeys[0] == "Shuffled within area":
        settings["SmallKeyMode"] = "KeepWithinArea, KeepThroughTime"
    if catKeysanitySmallKeys[0] == "Shuffled anywhere":
        settings["SmallKeyMode"] = "KeepThroughTime"
    if catKeysanitySmallKeys[0] != "---":
        settings["OverrideHintPriorities"][3].remove("ItemIceArrow")
        settings["OverrideHintPriorities"][2].append("ItemIceArrow")        # Ice Arrow Chest: backup hint -> sometimes hint

    wgtsShopsanityChecks = [50,25,25]
    wgtsShopsanityPrices = [60,20,20]
    if customModes["Main Density Mode"] == "Light":
        wgtsShopsanityChecks = [60,20,20]
        wgtsShopsanityPrices = [65,20,15]
    if customModes["Main Density Mode"] == "Super":
        wgtsShopsanityChecks = [30,35,35]
        wgtsShopsanityPrices = [30,35,35]
    catShopsanityChecks = random.choices(["---",
                                          "Late Shopsanity",
                                          "Full Shopsanity"],
                                         wgtsShopsanityChecks)
    if catShopsanityChecks[0] == "Late Shopsanity":
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------3--------3f000----")               # Goron + Zora + Milk Bar [8, 3r]
        if customModes["Main Density Mode"] == "Light":
            wgtsShopsanityPrices = [45,35,20]
        elif customModes["Main Density Mode"] == "Super":
            wgtsShopsanityPrices = [20,40,40]
        else:
            wgtsShopsanityPrices = [40,35,25]
    if catShopsanityChecks[0] == "Full Shopsanity":
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------b03--------3ffff-80000000---")     # All purchases minus Swamp Scrub [24, 7r] 
        if customModes["Main Density Mode"] == "Light":
            wgtsShopsanityPrices = [25,50,25]
        elif customModes["Main Density Mode"] == "Super":
            wgtsShopsanityPrices = [10,45,45]
        else:
            wgtsShopsanityPrices = [20,50,30]

    catShopsanityPrices = random.choices(["---",
                                          "Shuffle purchase prices",
                                          "Randomize purchase prices"],
                                         wgtsShopsanityPrices)
    if catShopsanityPrices[0] == "Shuffle purchase prices":
        settings["PriceMode"] = "Purchases, ShuffleOnly"
        itemListString = AddEntryToListString(itemListString,1,"1")
    if catShopsanityPrices[0] == "Randomize purchase prices":
        settings["PriceMode"] = "Purchases"
        itemListString = AddEntryToListString(itemListString,1,"1")
        settings["FillWallet"] = True

    if catShopsanityChecks[0] != "---" or catShopsanityPrices[0] != "---":
        nonzeroCategories += 1

    wgtsSoilsanity = [60,40]
    if customModes["Main Density Mode"] == "Light":
        wgtsSoilsanity = [70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsSoilsanity = [35,65]
    catSoilsanity = random.choices(["---","Shuffled"],wgtsSoilsanity)
    if catSoilsanity[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----------7ff-f0000000-------------------------")  # Soft soils [15, 7r] 
        # settings["OverrideHintPriorities"][2].append("CollectableRomaniRanchSoftSoil1")           # sometimes hint Ranch Day 1 Soil (redundant)
        nonzeroCategories += 1

    wgtsCowsanity = [60,40]
    if customModes["Main Density Mode"] == "Light":
        wgtsCowsanity = [70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsCowsanity = [35,65]
    catCowsanity = random.choices(["---","Shuffled"],wgtsCowsanity)
    if catCowsanity[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----------------------------1f-e0000000-------")   # Cows [8, 4r]
        # settings["OverrideHintPriorities"][2].append("ItemWellCowMilk")                           # sometimes hint Cow Beneath the Well (redundant)
        nonzeroCategories += 1

    wgtsStrayFairies = [0,70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsStrayFairies = [0,40,60]
    if (catStartingBossRemains[0] == "Five Fairy Hunt" or catStartingBossRemains[0] == "Full Fairy Hunt"):
        wgtsStrayFairies = [0,0,100]
    catStrayFairies = random.choices(["---",
                                      "Chest fairies except normal STT",
                                      "All stray fairies"],
                                     wgtsStrayFairies)
    if catStrayFairies[0] == "Chest fairies except normal STT":
        if (wgtsStrayFairies[0] > 0):
            nonzeroCategories += 1
        else:
            catStrayFairies[0] = "--- (chest fairies except normal STT)"
        itemListString = AddStringToListString(itemListString,
                                                   "--------------------------b003f0-7f003800----------")   # Non nSTT chest fairies [19, 4r]
    if catStrayFairies[0] == "All stray fairies":
        nonzeroCategories += 1
        itemListString = AddStringToListString(itemListString,
                                               "--------------------------3fffffff-fffffffe----------")     # All stray fairies, plus Clock Town [61, 4r]
        settings["StrayFairyMode"] = "Default"
        if (catStartingBossRemains[0] != "Five Fairy Hunt" and catStartingBossRemains[0] != "Full Fairy Hunt"):
            startListString = AddStringToListString(startListString,
                                                   "ffff-ffffffff-fff00000--")            

    wgtsScoopsanity = [70,30]
    if customModes["Main Density Mode"] == "Light":
        wgtsScoopsanity = [75,25]
    if customModes["Main Density Mode"] == "Super":
        wgtsScoopsanity = [40,60]
    if customModes["Scoopsanity"] == "Off":
        wgtsScoopsanity = [100,0]
    if customModes["Scoopsanity"] == "On":
        wgtsScoopsanity = [0,100]
    catScoopsanity = random.choices(["---","Shuffled"],
                                       wgtsScoopsanity)
    if catScoopsanity[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "---------------------------------fdc0000----")  # All scoops except bugs [9, ?r]
        #settings["OverrideHintPriorities"][2].append("BottleCatchBigPoe")                      # Sometimes hint Big Poe scoop (redundant)
        if customModes["Vanilla Eggs for Baby Zoras"] and catSongLayout[0] == "Baby Zoras":
            itemListString = RemoveEntryFromListString(itemListString,4,"4000000")              # Unshuffle Zora Egg scoop
            catScoopsanity[0] = "Shuffled (no eggs)"
        if customModes["Stubborn Princess"]:
            itemListString = RemoveEntryFromListString(itemListString,4,"80000")                # Unshuffle Deku Princess
            catScoopsanity[0] = catScoopsanity[0] + " (no Princess)"
        nonzeroCategories += 1

    wgtsHitSpots = [65,35,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsHitSpots = [70,30,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsHitSpots = [35,50,15]
    catHitSpots = random.choices(["---", "One Rupee each", "All Rupees"], wgtsHitSpots)
    if catHitSpots[0] == "One Rupee each":
        itemListString = AddStringToListString(itemListString,
                                               "-------924924-92492492-49240000---8000000-------------------------")    # 1 per Hit Spot (plus school gong) [25,10r]
    if catHitSpots[0] == "All Rupees":
        itemListString = AddStringToListString(itemListString,
                                               "-------1ffffff-ffffffff-fffe0000---8000000-------------------------")   # All per Hit Spot (plus gong) [73,10r]
    if catHitSpots[0] != "---":
        nonzeroCategories += 1

    wgtsTokensanity = [75,20,5]
    if customModes["Main Density Mode"] == "Light":
        wgtsTokensanity = [85,15,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsTokensanity = [55,35,10]
    if catStartingBossRemains[0] == "Skull Tokens":
        wgtsTokensanity = [0,0,100]
    catTokensanity = random.choices(["---","One house","Both houses"], wgtsTokensanity)
    catTokensanityHouse = ["---"]
    if catTokensanity[0] == "One house":
        catTokensanityHouse = random.choices(["SSH","OSH"],[1,1])
        if catTokensanityHouse[0] == "SSH":
            itemListString = AddStringToListString(itemListString,
                                               "----------------------------7-ffffffe0--------")    # SSH tokens [30, 1r]
        if catTokensanityHouse[0] == "OSH":
            itemListString = AddStringToListString(itemListString,
                                               "---------------------------1-fffffff8---------")    # OSH tokens [30, 1r]
            if ("HeartPieceOceanSpiderHouse" in settings["OverrideHintPriorities"][2]):
                settings["OverrideHintPriorities"][2].remove("HeartPieceOceanSpiderHouse")    # unhint OSH Chest
    if catTokensanity[0] == "Both houses":
        itemListString = AddStringToListString(itemListString,
                                               "---------------------------1-ffffffff-ffffffe0--------")    # All tokens [60, 2r]
        if ("HeartPieceOceanSpiderHouse" in settings["OverrideHintPriorities"][2]):
            settings["OverrideHintPriorities"][2].remove("HeartPieceOceanSpiderHouse")        # unhint OSH Chest
    if catTokensanity[0] != "---":
        nonzeroCategories += 1

    wgtsCratesAndBarrels = [60,40]
    if customModes["Main Density Mode"] == "Light":
        wgtsCratesAndBarrels = [70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsCratesAndBarrels = [40,60]
    catCratesAndBarrels = random.choices(["---","Shuffled"], wgtsCratesAndBarrels)
    if catCratesAndBarrels[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "---10000------------c0000-2000--3c200--30--1f078-8000008-10000100-20000000------------") # Crates and barrels [25, 7r]
        nonzeroCategories += 1

    wgtsKeatonGrass = [75,20,5]
    if customModes["Main Density Mode"] == "Light":
        wgtsKeatonGrass = [75,25,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsKeatonGrass = [50,35,15]
    catKeatonGrass = random.choices(["---","Odd checks only","All shuffled"], wgtsKeatonGrass)
    if catKeatonGrass[0] == "Odd checks only":
        itemListString = AddStringToListString(itemListString,
                                               "-----15-5aad5400-------------------------------")   # Odd Keaton Grass [15, 3r]
        nonzeroCategories += 1
    if catKeatonGrass[0] == "All shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----1f-fffffc00-------------------------------")   # All Keaton Grass [27, 3r]
        nonzeroCategories += 1

    wgtsButterflyAndWellFairies = [65,35]
    if customModes["Main Density Mode"] == "Light":
        wgtsButterflyAndWellFairies = [75,25]
    if customModes["Main Density Mode"] == "Super":
        wgtsButterflyAndWellFairies = [35,65]
    catButterflyAndWellFairies = random.choices(["---","Shuffled"], wgtsButterflyAndWellFairies)
    if catButterflyAndWellFairies[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "1fe-1fe00000------------------------------------")  # Butterfly and Well Fairies [16, 5r]
        if ("ChestWellLeftPurpleRupee" in settings["OverrideHintPriorities"][3]):                   
            settings["OverrideHintPriorities"][3].remove("ChestWellLeftPurpleRupee")                # unhint Well Left Side Chest
        nonzeroCategories += 1

    wgtsGossipFairies = [60,40,0,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsGossipFairies = [75,25,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsGossipFairies = [35,65,0,0]
    catGossipFairies = random.choices(["---","Regional Gossips","Regional Gossips S2","All Termina Gossips"], wgtsGossipFairies)
    if catGossipFairies[0] == "Regional Gossips":
        itemListString = AddStringToListString(itemListString,
                                               "-100000-3037400-----------------------------------")        # Regional Gossips [9, 6r]
        nonzeroCategories += 1
    if catGossipFairies[0] == "Regional Gossips S2":
        itemListString = AddStringToListString(itemListString,
                                               "-100000-31f7400-----------------------------------")        # Regional Gossips S2 (including Road/Path/Road) [12, 9r]
        #settings["OverrideHintPriorities"][3].append("CollectableSwampSpiderHouseTreeRoomGossipFairy1")    # Backup hint SSH Gossip Fairy (redundant)
        nonzeroCategories += 1
    if catGossipFairies[0] == "All Termina Gossips":
        itemListString = AddStringToListString(itemListString,
                                               "-100000-ffffff00-----------------------------------")       # All Gossips [25, 12r]
        nonzeroCategories += 1

    wgtsFrogs = [80,20]
    if customModes["Main Density Mode"] == "Super":
        wgtsFrogs = [50,50]
    #if hardOptions >= HARD_OPTIONS_LIMIT and (catLongQuests[0] == "Frog Choir" or catLongQuests[0] == "All Long Quests"):
    #    wgtsFrogs = [100,0]
    catFrogs = random.choices(["---","Shuffled"], wgtsFrogs)
    if catFrogs[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "1-e0000000------------------------------------")    # Frogs [4, 4r]
        #settings["OverrideHintPriorities"][2].append("FrogGreatBayTemple")                         # sometimes hint GBT Frog (redundant)
        #settings["OverrideHintPriorities"][3].append("FrogWoodfallTemple")                         # backup hint WFT Frog (redundant)
        junkListString = RemoveEntryFromListString(junkListString,1,"8000000")                      # unjunk Frog Choir
        settings["OverrideHintPriorities"][1].append("HeartPieceChoir")                             # always hint Frog Choir
        junkListString = AddStringToListString(junkListString,
                                               "-----------------------------------80000--20000") # junk Ranch Defense checks (not ribbons yet)
        nonzeroCategories += 1

    wgtsLooseRupeesOverworld = [55,15,20,10]
    if customModes["Main Density Mode"] == "Light":
        wgtsLooseRupeesOverworld = [70,10,10,10]
    if customModes["Main Density Mode"] == "Super":
        wgtsLooseRupeesOverworld = [30,20,20,30]
    catLooseRupeesOverworld = random.choices(["---",                                     
                                     "Overworld Red",
                                     "Overworld Red and Blue",
                                     "Overworld Red, Blue, and Green"],
                                    wgtsLooseRupeesOverworld)
    if catLooseRupeesOverworld[0] == "Overworld Red":
        itemListString = AddStringToListString(itemListString,
                                               "----------8100-40000000-7800000---1000f06----------------------") # Overworld Red (incl. guays) [14, 7r] 
    if catLooseRupeesOverworld[0] == "Overworld Red and Blue":
        itemListString = AddStringToListString(itemListString,
                                               "---------8410-8103-c0000000-7c7c10c---1000f06------40000-300183-c0003e00--------------") # Overworld Red + Blue [43, 12r]
    if catLooseRupeesOverworld[0] == "Overworld Red, Blue, and Green":
        itemListString = AddStringToListString(itemListString,
                                               "---------1ffff-8000ffff-fdef7800-7fffffc---1000f06--7-fffc20ff-fffffeff-80000000-40000-300183-c0003e00--------------") # Overworld R+B+G [156, 13r]
        if (customModes["No Post-Temple"] != True):                                                 # If No Post-Temple didn't already do it...
            settings["OverrideHintPriorities"][1].remove("MaskScents")                              # unhint Butler
            junkListString = AddEntryToListString(junkListString, 2, "40000")                       # junk Butler
    
    wgtsLooseRupeesTemple = [50,30,10,10]
    if customModes["Main Density Mode"] == "Light":
        wgtsLooseRupeesTemple = [60,20,10,10]
    if customModes["Main Density Mode"] == "Super":
        wgtsLooseRupeesTemple = [25,30,15,30]
    catLooseRupeesTemple = random.choices(["---",                                     
                                     "Temple Red",
                                     "Temple Red and Blue",
                                     "Temple Red, Blue, and Green"],
                                    wgtsLooseRupeesTemple)
    if catLooseRupeesTemple[0] == "Temple Red":
        itemListString = AddStringToListString(itemListString,
                                               "---------------6f370f8----------------------")                          # Temple Red [16, 4r]
    if catLooseRupeesTemple[0] == "Temple Red and Blue":
        itemListString = AddStringToListString(itemListString,
                                               "---------------6f370f8------f001fff-ff800000-3000000--------------")    # Temple Red + Blue [44, 4r]
    if catLooseRupeesTemple[0] == "Temple Red, Blue, and Green":
        itemListString = AddStringToListString(itemListString,
                                               "---------------6f370f8--1e0-c00---f001fff-ff800000-3000000--------------")  # Temple R+B+G [50, 4r]
    
    if catLooseRupeesOverworld[0] != "---" or catLooseRupeesTemple[0] != "---":
        nonzeroCategories += 1

    wgtsSnowsanity = [85,0,15,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsSnowsanity = [90,0,10,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsSnowsanity = [70,0,30,0]
    #if hardOptions >= HARD_OPTIONS_LIMIT:
    #    wgtsSnowsanity[1] += wgtsSnowsanity[2]
    #    wgtsSnowsanity[2] = 0
    catSnowsanity = random.choices(["---","Any-day large snowballs","Any-day snowballs","All shuffled"], wgtsSnowsanity)
    if catSnowsanity[0] == "Any-day large snowballs":
        itemListString = AddStringToListString(itemListString,
                                               "-------------fc0f000-3800---------1c0000--------------")                                # Large snowballs in GV, PTSH, SH [16, 3r]
    if catSnowsanity[0] == "Any-day snowballs":
        itemListString = AddStringToListString(itemListString,
                                               "-----1fc00--------fc0ff00-cf800--c0000----180c006--e00-1c0000-c0000c-------------")     # Non-owl any-day snowballs [46, 6r]
    if catSnowsanity[0] == "All shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----1fc00--------fc0ffff-fc3cf800--c0000----180c006--e00-301c0000-c0000c-------------") # Non-owl snowballs [64, 6r]
    #    hardOptions += 1
    if catSnowsanity[0] != "---":
        nonzeroCategories += 1

    #                         0  1  2  A C S N W E T
    wgtsPotsanityOverworld = [40,30,25,5,0,0,0,0,0,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsPotsanityOverworld = [50,40,10,0,0,0,0,0,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsPotsanityOverworld = [20,20,40,20,0,0,0,0,0,0]
    if customModes["Potsanity"] == "Off":
        wgtsPotsanityOverworld = [100,0,0,0,0,0,0,0,0,0]
    if customModes["Potsanity"] == "Central Pots":
        wgtsPotsanityOverworld = [0,0,0,0,100,0,0,0,0,0]
    if customModes["Potsanity"] == "South Pots":
        wgtsPotsanityOverworld = [0,0,0,0,0,100,0,0,0,0]
    if customModes["Potsanity"] == "North Pots":
        wgtsPotsanityOverworld = [0,0,0,0,0,0,100,0,0,0]
    if customModes["Potsanity"] == "West Pots":
        wgtsPotsanityOverworld = [0,0,0,0,0,0,0,100,0,0]
    if customModes["Potsanity"] == "East Pots":
        wgtsPotsanityOverworld = [0,0,0,0,0,0,0,0,100,0]
    if customModes["Potsanity"] == "Temple Pots":
        wgtsPotsanityOverworld = [0,0,0,0,0,0,0,0,0,100]
    if customModes["Potsanity"] == "Any One Group":
        wgtsPotsanityOverworld = [0,100,0,0,0,0,0,0,0,0]
    if customModes["Potsanity"] == "Any Two Groups":
        wgtsPotsanityOverworld = [0,0,100,0,0,0,0,0,0,0]
    if customModes["Potsanity"] == "Full Potsanity":
        wgtsPotsanityOverworld = [0,0,0,100,0,0,0,0,0,0]
    catPotsanity = random.choices(["---",
                                            "One group",
                                            "Two groups",
                                            "All groups",
                                            "Central pots",
                                            "South pots",
                                            "North pots",
                                            "West pots",
                                            "East pots",
                                            "Temple pots"],
                                            wgtsPotsanityOverworld)
    wgtsPODirectionRoll = [1,1,1,2,2,3]
    PODirectionsToRoll = 0
    POEligibleDirections = ["Central","South","North","West","East","Temple"]
    PORolledDirections = []
    if catPotsanity[0] == "All groups":
        PORolledDirections = POEligibleDirections                                                                                                               # Total [146, 23r]!
    elif catPotsanity[0].endswith(" pots"):
        PORolledDirections = [catPotsanity[0].removesuffix(" pots")]
    elif catPotsanity[0] != "---":
        if catPotsanity[0] == "One group":
            PODirectionsToRoll = 1
        if catPotsanity[0] == "Two groups":
            PODirectionsToRoll = 2
        for roll in range(PODirectionsToRoll):
            rolledDirection = random.choices(POEligibleDirections, wgtsPODirectionRoll)[0]
            wgtsPODirectionRoll[POEligibleDirections.index(rolledDirection)] = 0
            PORolledDirections.append(rolledDirection)
    if "Central" in PORolledDirections:
        itemListString = AddStringToListString(itemListString,
                                               "--10-1000000-----------f--20000000-1e00---70000000-3e000--3c180-3-dc000000------------")                        # Central [32, 7r]
    if "South" in PORolledDirections:
        itemListString = AddStringToListString(itemListString,
                                               "--------------30---18-100----480000---------------")                                                            # South [7, 3r]
        #if (customModes["No Post-Temple"] == False):
        #    settings["OverrideHintPriorities"][2].append("CollectableDekuShrineGreyBoulderRoomPot1")   # sometimes hint Butler Race Dual Pot (redundant)
    if "North" in PORolledDirections:
        itemListString = AddStringToListString(itemListString,
                                               "---500000-----------7c0--fff-ffffe000---7c0000-----------------")                                               # North [43, 3r]
        junkListString = AddEntryToListString(junkListString, 0, "40000")       # junk Goron Race
        settings["OverrideHintPriorities"][1].remove("ItemBottleGoronRace")     # unhint Goron Race
    if "West" in PORolledDirections:
        itemListString = AddStringToListString(itemListString,
                                               "-----60--c000000-----2-f0000-3c00000------10000--4-e00006-fc0f0-------------")                                  # West [30, 6r]
    if "East" in PORolledDirections:
        itemListString = AddStringToListString(itemListString,
                                               "--5-c2007000---------1-f0300000-10000-e0000000-804000----2801-f0000000---3301e00-------------")                 # East [36, 4r]
        if ("ChestWellLeftPurpleRupee" in settings["OverrideHintPriorities"][3]):
            settings["OverrideHintPriorities"][3].remove("ChestWellLeftPurpleRupee")    # unhint Well Left Path Chest
    if "Temple" in PORolledDirections:
        itemListString = AddStringToListString(itemListString,
                                               "--48-8000000------------------f00000-60000--8000000-------------")                                              # Temple pots [10, 4r]
        if ("CollectibleStrayFairyStoneTower7" in settings["OverrideHintPriorities"][3]):
            settings["OverrideHintPriorities"][3].remove("CollectibleStrayFairyStoneTower7")    # unhint Stone Tower Wizzrobe

    if catPotsanity[0] != "---":
        nonzeroCategories += 1

    wgtsPhotosSales = [65,35]
    if customModes["Main Density Mode"] == "Light":
        wgtsPhotosSales = [75,25]
    if customModes["Main Density Mode"] == "Super":
        wgtsPhotosSales = [35,65]
    #if gossipHintsTakenByAlways >= GOSSIP_HINTS_LIMIT:
    #    wgtsPhotosSales[0] += wgtsPhotosSales[1]
    #    wgtsPhotosSales[1] = 0
    catPhotosSales = random.choices(["---", "Shuffled"], wgtsPhotosSales)
    if catPhotosSales[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----60000--------------------f8c070------------") # Curio sales, Mushroom sale, Photos, Zora Jar Game, Dampe D2 bats [12, 6r]
        #settings["OverrideHintPriorities"][3].append("MundaneItemKotakeMushroomSaleRedRupee")   # backup hint Kotake Mushroom Sale (redundant)
        #settings["OverrideHintPriorities"][3].append("MundaneItemCuriosityShopPurpleRupee")     # backup hint Curiosity Shop Purple Rupee (redundant)
    #    gossipHintsTakenByAlways += 1
        nonzeroCategories += 1
       
    wgtsBombersNotebook = [80,10,15]
    if customModes["Main Density Mode"] == "Light":
        wgtsBombersNotebook = [80,20,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsBombersNotebook = [50,20,30]
    #if hardOptions >= HARD_OPTIONS_LIMIT or gossipHintsTakenByAlways >= GOSSIP_HINTS_LIMIT:
    #    wgtsBombersNotebook[1] += wgtsBombersNotebook[2]
    #    wgtsBombersNotebook[2] = 0
    if (customModes["No Clock Town"] == True):
        wgtsBombersNotebook = [100,0,0]
    catBombersNotebook = random.choices(["---",
                                         "Meetings only",
                                         "All shuffled"],
                                        wgtsBombersNotebook)
    if catBombersNotebook[0] == "Meetings only":
        startListString = AddEntryToListString(startListString,0,"400000")
        itemListString = AddStringToListString(itemListString,
                                               "----1fff-fe000000--------------------------------") # [20, 9r]
        settings["OverrideHintPriorities"][2].append("NotebookMeetKafei")
        #settings["OverrideHintPriorities"][3].append("NotebookMeetShiro")
    if catBombersNotebook[0] == "All shuffled":
        startListString = AddEntryToListString(startListString,0,"400000")
        itemListString = AddStringToListString(itemListString,
                                               "---f7f-fbffffff-fe000000--------------------------------") # [49, 10r] (no Hide and Seek ribbon)
        if catSongLayout[0] == "Traditional" or catSongLayout[0] == "Moon Oath":
            itemListString = AddEntryToListString(itemListString,34,"80")                       # shuffle Anju and Kafei ribbon
            #settings["OverrideHintPriorities"][0].append("NotebookUniteAnjuAndKafei")
        #settings["OverrideHintPriorities"][2].append("NotebookEscapeFromSakonSHideout")
        settings["OverrideHintPriorities"][3].append("NotebookPostmansFreedom")
        settings["OverrideHintPriorities"][3].append("MaskPostmanHat")
        settings["OverrideHintPriorities"][2].append("NotebookPurchaseCuriosityShopItem")
        settings["OverrideHintPriorities"][2].append("MaskAllNight")
        #settings["OverrideHintPriorities"][2].append("NotebookDeliverPendant")
        #settings["OverrideHintPriorities"][2].append("NotebookDeliverLetterToMama")
        #settings["OverrideHintPriorities"][2].append("NotebookPromiseAnjuDelivery")
        #settings["OverrideHintPriorities"][0].append("NotebookSaveTheCows")
        #settings["OverrideHintPriorities"][0].append("NotebookProtectMilkDelivery")
        #settings["OverrideHintPriorities"][2].append("NotebookGrogsThanks")
        #settings["OverrideHintPriorities"][2].append("NotebookMovingGorman")
        #settings["OverrideHintPriorities"][2].append("NotebookPromiseKamaro")
        #settings["OverrideHintPriorities"][2].append("NotebookSaveInvisibleSoldier")
        #settings["OverrideHintPriorities"][2].append("NotebookMeetShiro")
        #if catSongsanity[0] == "Mix songs with items":
        #    settings["OverrideHintPriorities"][2].append("NotebookPromiseRomani")
        #    gossipHintsTakenByAlways += 1
        #    hardOptions += 1
        
        if catFrogs[0] == "Shuffled":
            junkListString = AddStringToListString(junkListString,
                                                   "----600000---------------------------------") # junk Ranch Defense ribbons if Frogs is on
    if catBombersNotebook[0] != "---":
        nonzeroCategories += 1

    if (customModes["No Clock Town"] == True):
        itemListString = RemoveStringFromListString(itemListString,
                                                    "1---fff-ffffffff-fe000000-ff80000-1fffc00--1ffff-80000000--8000000--7-700--1e00-200---3e000--8000180--7f008f-c0000000-2---600-fd8000-800-c7f-80000001-70ee04-3fffc4-54600820")
        junkListString = RemoveStringFromListString(junkListString,
                                                    "1---fff-ffffffff-fe000000-ff80000-1fffc00--1ffff-80000000--8000000--7-700--1e00-200---3e000--8000180--7f008f-c0000000-2---600-fd8000-800-c7f-80000001-70ee04-3fffc4-54600820")
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------c-----600-f58000-800--80000000-10a804-35fc04-54200820")
        junkListString = AddStringToListString(junkListString,
                                               "-------------------------c-----600-f58000-800--80000000-10a804-35fc04-54200820")
        if (catFrogs[0] == "Shuffled"):
            itemListString = AddStringToListString(itemListString,"1-------------------------------------")
            junkListString = AddStringToListString(junkListString,"1-------------------------------------")
        if catStartingBossRemains[0] == "Mask Hunt":
            itemListString = AddStringToListString(itemListString,"-----------------------------------604600--")
            junkListString = AddStringToListString(junkListString,"-----------------------------------604600--")

    if (customModes["No Post-Temple"] == True):
        itemListString = RemoveStringFromListString(itemListString,
                                                    "-c000000-30000-100000--1fc1f-f0000000---------806--8-1ff-fffff000---80003-c0000000--------206--80000--40040-4c000000-40000")
        junkListString = RemoveStringFromListString(junkListString,
                                                    "-c000000-30000-100000--1fc1f-f0000000---------806--8-1ff-fffff000---80003-c0000000--------206--80000--40040-4c000000-40000")
        itemListString = AddStringToListString(itemListString,
                                               "-----------------------------------40040-4c000000-40000")
        junkListString = AddStringToListString(junkListString,
                                               "-----------------------------------40040-4c000000-40000")

    if catStartingBossRemains[0] == "Hearts":
        shuffleAndJunkHearts = "------------------------------1e0000------510f0000-"    # Beaver Race 2, Swamp Arch 2, Town Arch 50, DPG Three Days, H&D Three Days, Fisherman Game, Keaton Quiz, Moon Trial PoHs
        #if catMinigames[0] == "All shuffled":
        #    shuffleAndJunkHearts = "------------------------------1e0000------10000-"
        #elif catMinigamesExtra[0] == "DPG Three Days":
        #    shuffleAndJunkHearts = "------------------------------1e0000------d0000-"
        #elif catMinigamesExtra[0] == "H&D Three Days":
        #    shuffleAndJunkHearts = "------------------------------1e0000------70000-"
        #elif catMinigamesExtra[0] == "Town Archery 50":
        #    shuffleAndJunkHearts = "------------------------------1e0000------b0000-"
        itemListString = AddStringToListString(itemListString, shuffleAndJunkHearts)                                               
        junkListString = AddStringToListString(junkListString, shuffleAndJunkHearts)
        if catSongLayout[0] == "Moon Oath":
            if (customModes["All Moon Trials"]):
                junkListString = RemoveStringFromListString(junkListString, "------------------------------1e0000-------")  # don't junk Moon Trial PoHs when the checks are in play
            else:
                junkListString = RemoveStringFromListString(junkListString, "------------------------------100000-------")  # don't junk Link Trial PoH when it's in play

    if nonzeroCategories < NONZERO_CATEGORIES_MINIMUM:
        return ''
    
    if (customModes["No Iceless FD Logic"]):
        settings["EnabledTricks"].remove("GBT Red Pump as FD")
        settings["EnabledTricks"].remove("GBT Boss Door as FD")
        settings["EnabledTricks"].remove("GBT Map Chest Room Jumps as FD")
        settings["EnabledTricks"].remove("Ikana Canyon Iceless as FD")
    
    if (customModes["No Importance Count"]):
        settings["ImportanceCount"] = False
    
    if (customModes["Sun's Song"]):
        settings["EnableSunsSong"] = True

    settings["CustomItemListString"] = itemListString
    settings["CustomStartingItemListString"] = startListString
    settings["CustomJunkLocationsString"] = junkListString

    outputFilename = inputFilename.removesuffix(".json")
    outputFilename = outputFilename.removesuffix("base")
    outputFilename = "output\\" + FilenameOnly(outputFilename) + "_" + outputSuffix + ".json"

    try:
        os.makedirs("output")
    except FileExistsError:
        pass

    with open(outputFilename, "w") as write_file:
        json.dump(data,write_file,indent=4)

    spoilerlogFilename = outputFilename.removesuffix(".json")
    spoilerlogFilename = spoilerlogFilename + "_MysterySpoiler.txt"

    with open(spoilerlogFilename, "w") as spoiler_file:
        print("MMR Mystery Maker", MYSTERY_MAKER_VERSION,"-- Mystery Spoiler Log",file=spoiler_file)
        print("Base settings: ", FilenameOnly(inputFilename),file=spoiler_file)
        print("  Output file: ", outputFilename,file=spoiler_file)
        if (CheckForCustom(customModes)):
            print(" ***       ALTERNATE MODES ACTIVE!       *** ",file=spoiler_file)
            if (customModes["Goal Mode"] != "No Blitz"):
                print("                Goal Mode: ", customModes["Goal Mode"],file=spoiler_file)
            if (customModes["Direct to Credits"] or customModes["Goal Mode"] == "Five Fairy Hunt"):
                print("                            (Direct to Credits is on)", file=spoiler_file)
            if (customModes["Start Mode"] == "Kokiri" or customModes["Start Mode"] == "Swordless"):
                print("    Start Difficulty Mode: ", customModes["Start Mode"],file=spoiler_file)
            if (customModes["Song Layout"] != "Any (Default)"):
                print("         Song Layout Mode: ", customModes["Song Layout"],file=spoiler_file)
            if (customModes["All Moon Trials"]):
                print("                                (Moon Oath Adds All Trials)", file=spoiler_file)
            if (customModes["Early Moon Access Remains"] != 1 or customModes["Blitz Remains Count"]):
                print("Early Moon Access Remains: ", customModes["Early Moon Access Remains"],file=spoiler_file)
            if (customModes["Blitz Remains Count"]):
                print("                                (Blitz Remains count)", file=spoiler_file)
            if (customModes["Random Item Mode"] != "Any (Default)"):
                print("          Start Item Mode: ", customModes["Random Item Mode"],file=spoiler_file)
            if (customModes["FD Anywhere Mode"] != "Sometimes (Default)"):
                print("         FD Anywhere Mode: ", customModes["FD Anywhere Mode"],file=spoiler_file)
            if (customModes["Dungeon Entrances"] != "Sometimes (Default)"):
                print("   Dungeon Entrances Mode: ", customModes["Dungeon Entrances"],file=spoiler_file)
            if (customModes["Boss Keys"] != "Off (Default)"):
                print("           Boss Keys Mode: ", customModes["Boss Keys"],file=spoiler_file)
            if (customModes["Small Keys"] != "Sometimes (Default)"):
                print("          Small Keys Mode: ", customModes["Small Keys"],file=spoiler_file)
            if (customModes["Main Density Mode"] != "Normal"):
                print("        Main Density Mode: ", customModes["Main Density Mode"],file=spoiler_file)
            if (NONZERO_CATEGORIES_MINIMUM != 6):
                print("         Category Minimum: ", NONZERO_CATEGORIES_MINIMUM,file=spoiler_file)
            if (customModes["No Clock Town"]):
                print("            No Clock Town: ", customModes["No Clock Town"],file=spoiler_file)
            if (customModes["No Post-Temple"]):
                print("           No Post-Temple: ", customModes["No Post-Temple"],file=spoiler_file)
            if (customModes["Map and Compass Hints"]):
                print("    Map and Compass Hints: ", customModes["Map and Compass Hints"],file=spoiler_file)
            if (customModes["Potsanity"] != "Default"):
                print("           Potsanity Mode: ", customModes["Potsanity"],file=spoiler_file)
            if (customModes["Scoopsanity"] != "Default"):
                print("         Scoopsanity Mode: ", customModes["Scoopsanity"],file=spoiler_file)
            if (customModes["Vanilla Eggs for Baby Zoras"] != True):
                print("Vanilla Eggs + Baby Zoras: ", customModes["Vanilla Eggs for Baby Zoras"],file=spoiler_file)
            if (customModes["Stubborn Princess"]):
                print("        Stubborn Princess: ", customModes["Stubborn Princess"],file=spoiler_file)
            if (customModes["No Iceless FD Logic"]):
                print("      No Iceless FD Logic: ", customModes["No Iceless FD Logic"],file=spoiler_file)
            if (customModes["No Importance Count"]):
                print("      No Importance Count: ", customModes["No Importance Count"],file=spoiler_file)
            if (customModes["Sun's Song"]):
                print("               Sun's Song: ", customModes["Sun's Song"],file=spoiler_file)
        print("=============================================",file=spoiler_file)
        if customModes["Main Density Mode"] == "Light":
            print(" ***        Light Mystery Active!        ***",file=spoiler_file)
            print("",file=spoiler_file)      
        if customModes["Main Density Mode"] == "Super":
            print(" ***        Super Mystery Active!        ***",file=spoiler_file)
            print("",file=spoiler_file)
        print("                Goal Mode: ", catStartingBossRemains[0],file=spoiler_file)
        if (customModes["Direct to Credits"] or customModes["Goal Mode"] == "Five Fairy Hunt"):
            print("                            (Direct to Credits)", file=spoiler_file)
        print("",file=spoiler_file)
        if catSongLayout[0] == "Moon Oath":
            if (customModes["All Moon Trials"]):
                catSongLayout[0] = "Full Moon Oath"
            print("              Song Layout: ", catSongLayout[0], "--", moonAccessRemainsRequirement, "remains for moon access", file=spoiler_file)
        else:
            print("              Song Layout: ", catSongLayout[0],file=spoiler_file) 
        print("",file=spoiler_file)
        if (customModes["Start Mode"] == "Default"):
            print("Starting Sword and Shield: ", catStartingSwordShield[0],file=spoiler_file)
        else:
            print("               Start Mode: ", catStartingSwordShield[0],file=spoiler_file)
        if catStartingSwordShield[0] != "Cruel Start":
            print("     Starting Random Item: ", catStartingRandomItem[0],file=spoiler_file)
        if catStartingBossRemains[0] == "Five Fairy Hunt":
            print("            Starting Song: ", catStartingRandomSong[0],file=spoiler_file)
        else:
            print("     Starting Random Song: ", catStartingRandomSong[0],file=spoiler_file)
        if customModes["No Clock Town"] == True or catStartingBossRemains[0] == "Five Fairy Hunt":
            print("      Extra Starting Song:  Epona's Song", file=spoiler_file)
        if catSongLayout[0] == "Moon Oath" or catSongLayout[0] == "Full Moon Oath":
            print("      Extra Starting Song:  Oath to Order", file=spoiler_file)
        if catStartingSwordShield[0] != "Cruel Start":
            print("    Fierce Deity Anywhere: ", catFierceDeityAnywhere[0],file=spoiler_file)
        print("        Dungeon Entrances: ", catEntrancesTemples[0],file=spoiler_file)
        if catKeysanityBossKeys[0] != "---":
            print("                Boss Keys: ", catKeysanityBossKeys[0],file=spoiler_file)
        print("               Small Keys: ", catKeysanitySmallKeys[0],file=spoiler_file)        
        print("",file=spoiler_file)
        if (customModes["No Clock Town"] == True or customModes["No Post-Temple"] == True):
            if (customModes["No Clock Town"] == True):
                print(" ***        No Clock Town Checks!        ***",file=spoiler_file)
            if (customModes["No Post-Temple"] == True):
                print(" ***       No Post-Temple Checks!        ***",file=spoiler_file)
            print("",file=spoiler_file)
        print("       Shopsanity: Checks: ", catShopsanityChecks[0],file=spoiler_file)
        print("       Shopsanity: Prices: ", catShopsanityPrices[0],file=spoiler_file)
        print("               Soilsanity: ", catSoilsanity[0],file=spoiler_file)
        print("                Cowsanity: ", catCowsanity[0],file=spoiler_file)
        print("            Stray Fairies: ", catStrayFairies[0],file=spoiler_file)

        print("              Scoopsanity: ", catScoopsanity[0],file=spoiler_file)
        print("                Hit Spots: ", catHitSpots[0],file=spoiler_file)
        if catTokensanity[0] == "One house":
            print("              Tokensanity: ", catTokensanity[0], "--", catTokensanityHouse[0],file=spoiler_file)
        else:
            print("              Tokensanity: ", catTokensanity[0],file=spoiler_file)
        print("       Crates and Barrels: ", catCratesAndBarrels[0],file=spoiler_file)
        print("             Keaton Grass: ", catKeatonGrass[0],file=spoiler_file)
        print("           Gossip Fairies: ", catGossipFairies[0],file=spoiler_file)
        print("   Butterfly/Well Fairies: ", catButterflyAndWellFairies[0],file=spoiler_file)
        print("          Frogs and Choir: ", catFrogs[0],file=spoiler_file)
        print("  Loose Rupees: Overworld: ", catLooseRupeesOverworld[0],file=spoiler_file)
        print("    Loose Rupees: Temples: ", catLooseRupeesTemple[0],file=spoiler_file)
        print("               Snowsanity: ", catSnowsanity[0],file=spoiler_file)
        if catPotsanity[0] == "---" or catPotsanity[0] == "All groups":
            print("                Potsanity: ", catPotsanity[0],file=spoiler_file)
        else:
            print("                Potsanity: ", catPotsanity[0], "--", PORolledDirections,file=spoiler_file)
        print("Photos/Sales/Small Favors: ", catPhotosSales[0],file=spoiler_file)
        if customModes["No Clock Town"] == True:
            print("        Bombers' Notebook:  --- (disabled by No Clock Town)", file=spoiler_file)
        else:
            print("        Bombers' Notebook: ", catBombersNotebook[0],file=spoiler_file)
        print("---------------------------------------------",file=spoiler_file)
    #    print("  Gossip slots for always: ",gossipHintsTakenByAlways,file=spoiler_file)
    #    print("        Hard options used: ",hardOptions,file=spoiler_file)
        print("        Active categories: ",nonzeroCategories,file=spoiler_file)

    return outputFilename

argParser = argparse.ArgumentParser(description="Randomly generates Mystery settings files for MMR and runs MMR.CLI to roll seeds with them.")
argParser.add_argument("-n", dest="numberOfSettingsFiles",type=int,default=1,
                    help="create multiple settings/seeds at once")
argParser.add_argument("-i", "--input", dest="inputFile",default="Mystery_Settings_base_v5.json",
                    help="base MMR settings file")
argParser.add_argument("-r", "--randomizer-exe", dest="randomizerExe",default="MMR.CLI.exe",
                    help="MMR command-line executable")   
argParser.add_argument("--settings-only", dest="settingsOnly", action="store_true",
                    help="only generate settings; don't roll any seeds")
argParser.add_argument("--version", dest="showVersion", action="store_true",
                    help="print version number and exit")
args = argParser.parse_args()

if (args.showVersion):
    print("MMR Mystery Maker", MYSTERY_MAKER_VERSION)
    sys.exit()

optionSettingsFile = args.inputFile
optionRandomizerExe = args.randomizerExe
optionOutputCount = args.numberOfSettingsFiles
optionDontMakeSeed = args.settingsOnly
optionCustomModes = MODE_DEFAULTS

if (len(sys.argv) == 1):
    guiResults = openOptionsGui(MYSTERY_MAKER_VERSION)
    if (guiResults[0]):
        sys.exit()
    optionSettingsFile = guiResults[1]
    optionRandomizerExe = guiResults[2]
    optionOutputCount = guiResults[3]
    optionDontMakeSeed = guiResults[4]
    optionCustomModes = guiResults[5]

for i in range(optionOutputCount):
    resultFilename = ''
    consecutiveFailures = 0
    while (resultFilename == ''):
        resultFilename = GenerateMysterySettings(optionSettingsFile,optionCustomModes,(str)(i+1))
        if (resultFilename == ''):
            consecutiveFailures += 1
            if (consecutiveFailures >= 10000):
                print ("Exiting, couldn't meet category minimum after 10000 attempts")
                sys.exit()
    if (optionDontMakeSeed == False):
        mmrcl = optionRandomizerExe + " -outputpatch -spoiler -settings " + resultFilename
        subprocess.call(mmrcl)
