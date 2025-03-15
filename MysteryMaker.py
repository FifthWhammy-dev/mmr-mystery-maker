import json
import random
import subprocess
import argparse
import os
import sys
from mysteryutils.MysteryMakerGUI import openOptionsGui

MYSTERY_MAKER_VERSION = "v4.1.2"

MODE_DEFAULTS = {"Goal Mode":"Normal",
                 "Long Goal":"None",
                 "Direct to Credits":False,
                 "Start Mode":"Default",
                 "Random Item Mode":"Any (Default)",
                 "FD Anywhere Mode":"Sometimes (Default)",
                 "Main Density Mode":"Normal",
                 "No Clock Town":False,
                 "No Post-Temple":False,
                 "Map and Compass Hints":False,
                 "Boss Keys":"Default",
                 "Potsanity":"Default",
                 "Scoopsanity":"Default",
                 "Vanilla Eggs for Baby Zoras":False}

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
     
    gossipHintsTakenByAlways = 4 + settings["OverrideNumberOfRequiredGossipHints"] + settings["OverrideNumberOfNonRequiredGossipHints"]
    GOSSIP_HINTS_LIMIT = 12  # intentionally two less than the 14 gossip slots available
    if (customModes["No Post-Temple"] == True):
        gossipHintsTakenByAlways -= 3

    nonzeroCategories = 0
    NONZERO_CATEGORIES_MINIMUM = 5

    hardOptions = 0
    HARD_OPTIONS_LIMIT = 2

    if customModes["Main Density Mode"] == "Light":
        HARD_OPTIONS_LIMIT = 0
        settings["OverrideNumberOfRequiredGossipHints"] += 1
        gossipHintsTakenByAlways += 1
    if customModes["Main Density Mode"] == "Super":
        HARD_OPTIONS_LIMIT = 3
        GOSSIP_HINTS_LIMIT = 14
        NONZERO_CATEGORIES_MINIMUM = 8
    
    wgtsStartingBossRemains = [65,25,10,0,0,0,0,0,0]    
    if (customModes["Goal Mode"] == "No Blitz"):
        wgtsStartingBossRemains = [100,0,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Blitz 1"):
        wgtsStartingBossRemains = [0,100,0,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Blitz 2"):
        wgtsStartingBossRemains = [0,0,100,0,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Remains Shuffle"):
        wgtsStartingBossRemains = [0,0,0,100,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Five Fairy Hunt"):
        wgtsStartingBossRemains = [0,0,0,0,100,0,0,0,0]        
    if (customModes["Goal Mode"] == "Normal + Remains Shuffle"):
        wgtsStartingBossRemains = [45,25,10,20,0,0,0,0,0]
    if (customModes["Goal Mode"] == "Grab Bag"):
        wgtsStartingBossRemains = [11,11,11,33,33,0,0,0,0]
    if (customModes["Long Goal"] == "Full Fairy Hunt"):
        wgtsStartingBossRemains = [0,0,0,0,0,100,0,0,0]
    if (customModes["Long Goal"] == "Mask Hunt"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,100,0,0]
    if (customModes["Long Goal"] == "Skull Tokens"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,0,100,0]
    if (customModes["Long Goal"] == "Hearts"):
        wgtsStartingBossRemains = [0,0,0,0,0,0,0,0,100]
    catStartingBossRemains = random.choices(["Normal","Blitz 1","Blitz 2","Remains Shuffle","Five Fairy Hunt","Full Fairy Hunt","Mask Hunt","Skull Tokens","Hearts"], wgtsStartingBossRemains)
    if catStartingBossRemains[0] == "Normal":
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, FourBossRemains"  
    if catStartingBossRemains[0] == "Blitz 1":
        settings["BossRemainsMode"] = "Blitz1"
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, ThreeBossRemains"
    if catStartingBossRemains[0] == "Blitz 2":
        settings["BossRemainsMode"] = "Blitz2"
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, TwoBossRemains"            
    if catStartingBossRemains[0] == "Remains Shuffle":
        itemListString = AddStringToListString(itemListString,
                                               "-----f00000--------------------------------")
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, FourBossRemains"
    if catStartingBossRemains[0] == "Five Fairy Hunt" or catStartingBossRemains[0] == "Full Fairy Hunt":
        gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
        gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        settings["BossRemainsMode"] = "GreatFairyRewards"
        settings["StrayFairyMode"] = "Default"
        junkListString = RemoveStringFromListString(junkListString,
                                                    "-------------------------------------f000")
        itemListString = AddStringToListString(itemListString,
                                               "-----f00000--------------------------------")
        startListString = AddEntryToListString(startListString, 1, "20")
        settings["FairyMaskShimmer"] = True
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        startListString = AddStringToListString(startListString,
                                                "7fe-ffc1ff8-3ff00000--")
        settings["VictoryMode"] = "DirectToCredits, OneBossRemains"
        itemListString = RemoveEntryFromListString(itemListString,3,"1")
    if catStartingBossRemains[0] == "Full Fairy Hunt":
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, FourBossRemains"
    if catStartingBossRemains[0] == "Mask Hunt":
        gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
        gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        settings["RequiredBossRemains"] = 1
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, CantFightMajora, NonTransformationMasks, TransformationMasks"
        else:
            settings["VictoryMode"] = "CantFightMajora, NonTransformationMasks, TransformationMasks"
    if catStartingBossRemains[0] == "Skull Tokens":
        gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
        gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, CantFightMajora, SkullTokens"
        else:
            settings["VictoryMode"] = "CantFightMajora, SkullTokens"
    if catStartingBossRemains[0] == "Hearts":
        gossipHintsTakenByAlways -= settings["OverrideNumberOfRequiredGossipHints"]
        gossipHintsTakenByAlways -= settings["OverrideNumberOfNonRequiredGossipHints"]
        settings["OverrideNumberOfRequiredGossipHints"] = 0
        settings["OverrideNumberOfNonRequiredGossipHints"] = 0
        if (customModes["Direct to Credits"]):
            settings["VictoryMode"] = "DirectToCredits, CantFightMajora, Hearts"
        else:
            settings["VictoryMode"] = "CantFightMajora, Hearts"
                                                    
    wgtsSongsanity = [65,35]
    if customModes["Main Density Mode"] == "Super":
        wgtsSongsanity = [50,50]
    catSongsanity = random.choices(["---","Mix songs with items"],wgtsSongsanity)
    if catSongsanity[0] == "Mix songs with items":
        settings["AddSongs"] = True
        itemListString = RemoveEntryFromListString(itemListString,3,"1")
        settings["OverrideHintPriorities"][2].append("SongEpona")
        settings["OverrideHintPriorities"][2].append("SongElegy")
        if (settings["OverrideNumberOfRequiredGossipHints"] > 0):
            settings["OverrideNumberOfRequiredGossipHints"] += 1
            gossipHintsTakenByAlways += 1
        nonzeroCategories += 1

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
            itemListString = RemoveEntryFromListString(itemListString,7,"200000")
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

    wgtsStartingRandomSong = [0,40,10,10,10,10,10,10,0]
    if catSongsanity[0] != "---":
        wgtsStartingRandomSong[0] = 0
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        wgtsStartingRandomSong = [0,0,0,0,0,100,0,0,0]
    if catStartingBossRemains[0] == "Mask Hunt":
        if customModes["No Clock Town"]:
            wgtsStartingRandomSong = [0,0,0,0,0,0,0,0,100]
        else:
            wgtsStartingRandomSong[8] = 0
            startListString = AddEntryToListString(startListString,2,"2")
            itemListString = RemoveEntryFromListString(itemListString,3,"1")    
    if catStartingBossRemains[0] == "Five Fairy Hunt" or customModes["No Clock Town"] == True:
        wgtsStartingRandomSong[1] = 0
        startListString = AddEntryToListString(startListString,1,"8000000")
        itemListString = RemoveEntryFromListString(itemListString,3,"1")
    catStartingRandomSong = random.choices(["None",
                                            "Epona's Song",
                                            "Song of Healing",
                                            "Song of Storms",
                                            "Sonata of Awakening",
                                            "Goron Lullaby",
                                            "New Wave Bossa Nova",
                                            "Elegy of Emptiness",
                                            "Oath to Order"],
                                           wgtsStartingRandomSong)
    if catStartingRandomSong[0] != "---":
        if catSongsanity[0] == "---":
            itemListString = RemoveEntryFromListString(itemListString,3,"4")        
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

    wgtsFierceDeityAnywhere = [55,45]
    if customModes["FD Anywhere Mode"] == "Only When Starting":
        wgtsFierceDeityAnywhere = [100,0]
    if customModes["FD Anywhere Mode"] == "Always" or catStartingRandomItem[0] == "Fierce Deity's Mask":
        wgtsFierceDeityAnywhere = [0,100]
    if customModes["FD Anywhere Mode"] == "Off" or catStartingSwordShield[0] == "Cruel Start":
        wgtsFierceDeityAnywhere = [100,0]
    catFierceDeityAnywhere = random.choices(["Off","Active"], wgtsFierceDeityAnywhere)
    if catFierceDeityAnywhere[0] == "Active":
        settings["AllowFierceDeityAnywhere"] = True

    wgtsShopsanityChecks = [60,20,20]
    wgtsShopsanityPrices = [65,20,15]
    if customModes["Main Density Mode"] == "Light":
        wgtsShopsanityPrices = [65,35,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsShopsanityChecks = [30,40,30]
        wgtsShopsanityPrices = [30,45,25]
    catShopsanityChecks = random.choices(["---",
                                          "Late Shopsanity",
                                          "Full Shopsanity"],
                                         wgtsShopsanityChecks)
    if catShopsanityChecks[0] == "Late Shopsanity":
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------3--------3f000----")
        if customModes["Main Density Mode"] == "Light":
            wgtsShopsanityPrices = [45,55,0]
        elif customModes["Main Density Mode"] == "Super":
            wgtsShopsanityPrices = [20,50,30]
        else:
            wgtsShopsanityPrices = [45,35,20]
    if catShopsanityChecks[0] == "Full Shopsanity":
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------b03--------3ffff-80000000---")
        if customModes["Main Density Mode"] == "Light":
            wgtsShopsanityPrices = [45,75,0]
        elif customModes["Main Density Mode"] == "Super":
            wgtsShopsanityPrices = [10,55,35]
        else:
            wgtsShopsanityPrices = [25,50,25]

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

    wgtsSoilsanity = [70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsSoilsanity = [40,60]
    catSoilsanity = random.choices(["---","Shuffled"],wgtsSoilsanity)
    if catSoilsanity[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----------7ff-f0000000-------------------------")
        settings["OverrideHintPriorities"][2].append("CollectableRomaniRanchSoftSoil1")
        nonzeroCategories += 1

    wgtsCowsanity = [70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsCowsanity = [40,60]
    catCowsanity = random.choices(["---","Shuffled"],wgtsCowsanity)
    if catCowsanity[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----------------------------1f-e0000000-------")
        settings["OverrideHintPriorities"][1].append("ItemWellCowMilk")
        nonzeroCategories += 1

    wgtsStrayFairies = [0,70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsStrayFairies = [0,40,60]
    if (catStartingBossRemains[0] == "Five Fairy Hunt" or catStartingBossRemains[0] == "Full Fairy Hunt"):
        wgtsStrayFairies = [0,0,100]
    catStrayFairies = random.choices(["---",
                                      "Most chest fairies",
                                      "All stray fairies"],
                                     wgtsStrayFairies)
    if catStrayFairies[0] == "Most chest fairies":
        if (wgtsStrayFairies[0] > 0):
            nonzeroCategories += 1
        itemListString = AddStringToListString(itemListString,
                                                   "--------------------------3fbb83f0-7f003800----------")
    if catStrayFairies[0] == "All stray fairies":
        nonzeroCategories += 1
        settings["OverrideHintPriorities"][2].append("CollectibleStrayFairyStoneTower8")
        settings["OverrideHintPriorities"][2].append("CollectibleStrayFairyStoneTower4")
        itemListString = AddStringToListString(itemListString,
                                               "--------------------------3fffffff-fffffffe----------")
        settings["StrayFairyMode"] = "Default"
        if (catStartingBossRemains[0] != "Five Fairy Hunt" and catStartingBossRemains[0] != "Full Fairy Hunt"):
            startListString = AddStringToListString(startListString,
                                                   "ffff-ffffffff-fff00000--")            

    wgtsEntrancesTemples = [55,45]
    wgtsEntrancesBossRooms = [70,30]
    if customModes["Main Density Mode"] == "Light":
        wgtsEntrancesBossRooms = [100,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsEntrancesTemples = [25,75]
        wgtsEntrancesBossRooms = [40,60]
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        wgtsEntrancesTemples = [0,100]
        wgtsEntrancesBossRooms = [100,0]
    catEntrancesTemples = random.choices(["---","Shuffled"], wgtsEntrancesTemples)
    if catEntrancesTemples[0] == "Shuffled":
        settings["RandomizeDungeonEntrances"] = True
        if customModes["Map and Compass Hints"] or customModes["Main Density Mode"] == "Light":
            startListString = RemoveStringFromListString(startListString,
                                                         "--154--")
    catEntrancesBossRooms = random.choices(["---","Shuffled"], wgtsEntrancesBossRooms)
    if catEntrancesBossRooms[0] == "Shuffled":
        settings["RandomizeBossRooms"] = True
        if customModes["Map and Compass Hints"]:
            startListString = RemoveStringFromListString(startListString,
                                                         "--2a8--")
    if catEntrancesTemples[0] != "---" or catEntrancesBossRooms[0] != "---":
        nonzeroCategories += 1

    wgtsKeysanityBossKeys = [65,20,15,0,0]
    if customModes["Main Density Mode"] == "Light":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsKeysanityBossKeys = [40,30,30,0,0]
    if customModes["Boss Keys"] == "Off":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    if customModes["Boss Keys"] == "Always Active (Either Option)":
        if customModes["Main Density Mode"] != "Light":
            wgtsKeysanityBossKeys[0] = 0
        wgtsKeysanityBossKeys[3] = 0
        wgtsKeysanityBossKeys[4] = 0
    if customModes["Boss Keys"] == "Always Within Their Temple":
        wgtsKeysanityBossKeys = [0,100,0,0,0]
    if customModes["Boss Keys"] == "Always Within Any Temple":
        wgtsKeysanityBossKeys = [0,0,100,0,0]
    if catStartingBossRemains[0] == "Five Fairy Hunt":
        wgtsKeysanityBossKeys = [100,0,0,0,0]
    if hardOptions >= HARD_OPTIONS_LIMIT and customModes["Boss Keys"] == "Default":
        wgtsKeysanityBossKeys[1] += wgtsKeysanityBossKeys[2]
        wgtsKeysanityBossKeys[2] = 0
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
        if customModes["Boss Keys"] == "Default":
            hardOptions += 1
    if catKeysanityBossKeys[0] == "Shuffled within area":
        settings["BossKeyMode"] = "KeepWithinArea, KeepThroughTime"
    if catKeysanityBossKeys[0] == "Shuffled anywhere":
        settings["BossKeyMode"] = "KeepThroughTime"
        settings["OverrideNumberOfRequiredGossipHints"] += 1
        gossipHintsTakenByAlways += 1

    wgtsKeysanitySmallKeys = [65,20,15,0,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsKeysanitySmallKeys = [40,30,30,0,0]
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
        settings["OverrideHintPriorities"][2].remove("ItemIceArrow")
        settings["OverrideHintPriorities"][1].append("ItemIceArrow")
    if catKeysanitySmallKeys[0] == "Shuffled within area":
        settings["SmallKeyMode"] = "KeepWithinArea, KeepThroughTime"
    if catKeysanitySmallKeys[0] == "Shuffled anywhere":
        settings["SmallKeyMode"] = "KeepThroughTime"

    if catKeysanityBossKeys[0] != "---" or catKeysanitySmallKeys[0] != "---":
        nonzeroCategories += 1

    wgtsScoopsanity = [75,25]
    if customModes["Main Density Mode"] == "Light":
        wgtsScoopsanity = [100,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsScoopsanity = [50,50]
    if customModes["Scoopsanity"] == "Off":
        wgtsScoopsanity = [100,0]
    if customModes["Scoopsanity"] == "On":
        wgtsScoopsanity = [0,100]
    catScoopsanity = random.choices(["---","Shuffled with scoops"],
                                       wgtsScoopsanity)
    if catScoopsanity[0] == "Shuffled with scoops":
        itemListString = AddStringToListString(itemListString,
                                               "---------------------------------fdc0000----")
        settings["OverrideHintPriorities"][1].append("BottleCatchBigPoe")
        nonzeroCategories += 1

    wgtsHitSpots = [70,25,5]
    if customModes["Main Density Mode"] == "Light":
        wgtsHitSpots = [70,30,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsHitSpots = [40,45,15]
    catHitSpots = random.choices(["---", "One Rupee each", "All Rupees"], wgtsHitSpots)
    if catHitSpots[0] == "One Rupee each":
        itemListString = AddStringToListString(itemListString,
                                               "-------924924-92492492-49240000---8000000-------------------------")
    if catHitSpots[0] == "All Rupees":
        itemListString = AddStringToListString(itemListString,
                                               "-------1ffffff-ffffffff-fffe0000---8000000-------------------------")
    if catHitSpots[0] != "---":
        nonzeroCategories += 1

    wgtsTokensanity = [80,15,5]
    if customModes["Main Density Mode"] == "Light":
        wgtsTokensanity = [80,20,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsTokensanity = [60,30,10]
    if catStartingBossRemains[0] == "Skull Tokens":
        wgtsTokensanity = [0,0,100]
    catTokensanity = random.choices(["---","One house","Both houses"], wgtsTokensanity)
    catTokensanityHouse = ["---"]
    if catTokensanity[0] == "One house":
        catTokensanityHouse = random.choices(["SSH","OSH"],[1,1])
        if catTokensanityHouse[0] == "SSH":
            itemListString = AddStringToListString(itemListString,
                                               "----------------------------7-ffffffe0--------")
        if catTokensanityHouse[0] == "OSH":
            itemListString = AddStringToListString(itemListString,
                                               "---------------------------1-fffffff8---------")
    if catTokensanity[0] == "Both houses":
        itemListString = AddStringToListString(itemListString,
                                               "---------------------------1-ffffffff-ffffffe0--------")
    if catTokensanity[0] != "---":
        nonzeroCategories += 1

    wgtsCratesAndBarrels = [70,30]
    if customModes["Main Density Mode"] == "Super":
        wgtsCratesAndBarrels = [40,60]
    catCratesAndBarrels = random.choices(["---","Shuffled"], wgtsCratesAndBarrels)
    if catCratesAndBarrels[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "---10000------------c0000-2000--3c200--30--1f078-8000008-10000100-20000000------------")
        nonzeroCategories += 1

    wgtsKeatonGrass = [75,20,5]
    if customModes["Main Density Mode"] == "Light":
        wgtsKeatonGrass = [75,25,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsKeatonGrass = [50,35,15]
    catKeatonGrass = random.choices(["---","Odd checks only","All shuffled"], wgtsKeatonGrass)
    if catKeatonGrass[0] == "Odd checks only":
        itemListString = AddStringToListString(itemListString,
                                               "-----15-5aad5400-------------------------------")
        nonzeroCategories += 1
    if catKeatonGrass[0] == "All shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----1f-fffffc00-------------------------------")
        nonzeroCategories += 1

    wgtsGossipFairies = [75,25,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsGossipFairies = [50,50,0]
    catGossipFairies = random.choices(["---","Regional Gossips","All Termina Gossips"], wgtsGossipFairies)
    if catGossipFairies[0] == "Regional Gossips":
        itemListString = AddStringToListString(itemListString,
                                               "-100000-31f7400-----------------------------------")
        settings["OverrideHintPriorities"][2].append("CollectableSwampSpiderHouseTreeRoomGossipFairy1")
        nonzeroCategories += 1
    if catGossipFairies[0] == "All Termina Gossips":
        itemListString = AddStringToListString(itemListString,
                                               "-100000-ffffff00-----------------------------------")
        nonzeroCategories += 1

    wgtsButterflyAndWellFairies = [75,25]
    if customModes["Main Density Mode"] == "Super":
        wgtsButterflyAndWellFairies = [50,50]
    catButterflyAndWellFairies = random.choices(["---","Shuffled"], wgtsButterflyAndWellFairies)
    if catButterflyAndWellFairies[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "1fe-1fe00000------------------------------------")
        if ("ChestWellLeftPurpleRupee" in settings["OverrideHintPriorities"][2]):
            settings["OverrideHintPriorities"][2].remove("ChestWellLeftPurpleRupee")
        nonzeroCategories += 1

    wgtsLongQuests = [25,20,15,40,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsLongQuests = [0,30,20,50,0]
    if (customModes["No Post-Temple"] == True):
        wgtsLongQuests[0] += wgtsLongQuests[3]
        wgtsLongQuests[3] = 0
        wgtsLongQuests[4] = 0
    if (customModes["No Clock Town"] == True):
        wgtsLongQuests[0] += wgtsLongQuests[1]
        wgtsLongQuests[1] = 0
        wgtsLongQuests[0] += wgtsLongQuests[2]
        wgtsLongQuests[2] = 0
        wgtsLongQuests[4] = 0
    if catStartingBossRemains[0] == "Five Fairy Hunt" or catStartingBossRemains[0] == "Mask Hunt":
        wgtsLongQuests[0] += wgtsLongQuests[2]
        wgtsLongQuests[2] = 0
        wgtsLongQuests[4] = 0
    if hardOptions >= HARD_OPTIONS_LIMIT:
        wgtsLongQuests[4] = 0
    if catSongsanity[0] == "Mix songs with items" and customModes["Main Density Mode"] != "Super":
        wgtsLongQuests = [100,0,0,0,0]
    catLongQuests = random.choices(["---",
                                    "Anju and Kafei",
                                    "Baby Zoras",
                                    "Frog Choir",
                                    "All Long Quests"],
                                   wgtsLongQuests)
    if catLongQuests[0] == "Anju and Kafei" or catLongQuests[0] == "All Long Quests":
        junkListString = RemoveEntryFromListString(junkListString,2,"400000")
        settings["OverrideHintPriorities"][0].append("MaskCouple")
        gossipHintsTakenByAlways += 1
    if catLongQuests[0] == "Baby Zoras" or catLongQuests[0] == "All Long Quests":
        junkListString = RemoveEntryFromListString(junkListString,3,"80")
        settings["OverrideHintPriorities"][0].append("SongNewWaveBossaNova")
        gossipHintsTakenByAlways += 1
        if catSongsanity[0] == "---":
            if catStartingRandomSong[0] == "---":
                itemListString = RemoveEntryFromListString(itemListString,3,"4")
            else:
                itemListString = RemoveEntryFromListString(itemListString,3,"1")
        if catScoopsanity[0] == "Shuffled with scoops" and customModes["Vanilla Eggs for Baby Zoras"]:
            itemListString = RemoveEntryFromListString(itemListString,4,"4000000")
            catScoopsanity[0] = "Shuffled with scoops (unscrambled eggs)"
    if catLongQuests[0] == "Frog Choir" or catLongQuests[0] == "All Long Quests":
        junkListString = RemoveEntryFromListString(junkListString,1,"8000000")
        settings["OverrideHintPriorities"][0].append("HeartPieceChoir")
        gossipHintsTakenByAlways += 1
    if catLongQuests[0] == "All Long Quests":
        hardOptions += 1
    if catLongQuests[0] != "---":
        nonzeroCategories += 1

    wgtsFrogs = [65,35]
    if customModes["Main Density Mode"] == "Super":
        wgtsFrogs = [40,60]
    if hardOptions >= HARD_OPTIONS_LIMIT and (catLongQuests[0] == "Frog Choir" or catLongQuests[0] == "All Long Quests"):
        wgtsFrogs = [100,0]
    catFrogs = random.choices(["---","Shuffled"], wgtsFrogs)
    if catFrogs[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "1-e0000000------------------------------------")
        settings["OverrideHintPriorities"][1].append("FrogGreatBayTemple")
        settings["OverrideHintPriorities"][2].append("FrogWoodfallTemple")
        if catLongQuests[0] == "Frog Choir" or catLongQuests[0] == "All Long Quests":
            hardOptions += 1
        nonzeroCategories += 1
    if (customModes["No Clock Town"] == True and catLongQuests[0] == "Frog Choir" and catFrogs[0] != "Shuffled"):
        junkListString = AddEntryToListString(junkListString,1,"8000000")
        settings["OverrideHintPriorities"][0].remove("HeartPieceChoir")
        nonzeroCategories -= 1
        catLongQuests[0] = "---"

    wgtsLooseRupees = [60,10,10,10,10]
    if customModes["Main Density Mode"] == "Super":
        wgtsLooseRupees = [25,15,15,15,30]
    if hardOptions >= HARD_OPTIONS_LIMIT:
        wgtsLooseRupees[3] += wgtsLooseRupees[4]
        wgtsLooseRupees[4] = 0
    catLooseRupees = random.choices(["---",
                                     "Temple Red only",
                                     "All Red",
                                     "All Red and Blue",
                                     "All Red, Blue, and Green"],
                                    wgtsLooseRupees)
    if catLooseRupees[0] == "Temple Red only":
        itemListString = AddStringToListString(itemListString,
                                               "---------------6f370f8----------------------")
    if catLooseRupees[0] == "All Red":
        itemListString = AddStringToListString(itemListString,
                                               "----------8100-40000000-7800000---7f37ffe----------------------")
    if catLooseRupees[0] == "All Red and Blue":
        itemListString = AddStringToListString(itemListString,
                                               "---------8410-8103-c0000000-7c7c10c---7f37ffe------f041fff-ffb00183-c3003e00--------------")
    if catLooseRupees[0] == "All Red, Blue, and Green":
        itemListString = AddStringToListString(itemListString,
                                               "---------1ffff-8000ffff-fdef7800-7fffffc---7f37ffe--1e7-fffc2cff-fffffeff-80000000-f041fff-ffb00183-c3003e00--------------")
        if (customModes["No Post-Temple"] != True):
            settings["OverrideHintPriorities"][0].remove("MaskScents")
            junkListString = AddEntryToListString(junkListString, 2, "40000")
            gossipHintsTakenByAlways -= 1
        hardOptions += 1
    if catLooseRupees[0] != "---":
        nonzeroCategories += 1

    wgtsSnowsanity = [85,15,0]
    if customModes["Main Density Mode"] == "Super":
        wgtsSnowsanity = [70,30,0]
    if hardOptions >= HARD_OPTIONS_LIMIT:
        wgtsSnowsanity[1] += wgtsSnowsanity[2]
        wgtsSnowsanity[2] = 0
    catSnowsanity = random.choices(["---","Any-day snowballs","All shuffled"], wgtsSnowsanity)
    if catSnowsanity[0] == "Any-day snowballs":
        itemListString = AddStringToListString(itemListString,
                                               "-----1fc00--------fc0ff00-cf800--c0000----180c006--e00-1c0000-c0000c-------------")
    if catSnowsanity[0] == "All shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----1fc00--------fc0ffff-fc3cf800--c0000----180c006--e00-301c0000-c0000c-------------")
        hardOptions += 1
    if catSnowsanity[0] != "---":
        nonzeroCategories += 1

    wgtsPotsanity = [80,10,10]
    if customModes["Main Density Mode"] == "Super":
        wgtsPotsanity = [50,20,30]
    if customModes["Potsanity"] == "Off":
        wgtsPotsanity = [100,0,0]
    if customModes["Potsanity"] == "Always Active (Either Option)":
        wgtsPotsanity[0] = 0
    if customModes["Potsanity"] == "Temples and W/E Dungeons":
        wgtsPotsanity = [0,100,0]
    if customModes["Potsanity"] == "Full Potsanity":
        wgtsPotsanity = [0,0,100]
    if hardOptions >= HARD_OPTIONS_LIMIT and customModes["Potsanity"] == "Default":
        wgtsPotsanity[1] += wgtsPotsanity[2]
        wgtsPotsanity[2] = 0
    catPotsanity = random.choices(["---",
                                   "Temples and west/east dungeons",
                                   "Almost all shuffled"],
                                  wgtsPotsanity)
    if catPotsanity[0] == "Temples and west/east dungeons":
        itemListString = AddStringToListString(itemListString,
                                               "--48-a007000--60--c000000------300000-3c10008-e0000000-20004000----70012001-f0f00000-60004-6-83fde03-dc000000------------")
    if catPotsanity[0] == "Almost all shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "--5d-cb507000--60--c000000-----3-f03f0000-3c107ff-e0000000-20804fff-fffffe18-100--707d2801-f0f3e000-4e0004-e3c186-b3fdef3-dc000000------------")
        junkListString = AddEntryToListString(junkListString, 0, "40000")
        settings["OverrideHintPriorities"][0].remove("ItemBottleGoronRace")
        if (customModes["No Post-Temple"] == False):
            settings["OverrideHintPriorities"][1].append("CollectableDekuShrineGreyBoulderRoomPot1")
            gossipHintsTakenByAlways -= 1
        if customModes["Potsanity"] == "Default":
            hardOptions += 1
    if catPotsanity[0] != "---":
        if ("ChestWellLeftPurpleRupee" in settings["OverrideHintPriorities"][2]):
            settings["OverrideHintPriorities"][2].remove("ChestWellLeftPurpleRupee")
        if ("CollectibleStrayFairyStoneTower7" in settings["OverrideHintPriorities"][2]):
            settings["OverrideHintPriorities"][2].remove("CollectibleStrayFairyStoneTower7")
        nonzeroCategories += 1

    wgtsPhotosSales = [75,25]
    if customModes["Main Density Mode"] == "Super":
        wgtsPhotosSales = [50,50]
    if gossipHintsTakenByAlways >= GOSSIP_HINTS_LIMIT:
        wgtsPhotosSales[0] += wgtsPhotosSales[1]
        wgtsPhotosSales[1] = 0
    catPhotosSales = random.choices(["---", "Shuffled"], wgtsPhotosSales)
    if catPhotosSales[0] == "Shuffled":
        itemListString = AddStringToListString(itemListString,
                                               "-----60000--------------------f8c070------------")
        settings["OverrideHintPriorities"][1].remove("HeartPieceSeaHorse")
        settings["OverrideHintPriorities"][0].append("HeartPieceSeaHorse")
        settings["OverrideHintPriorities"][2].append("MundaneItemKotakeMushroomSaleRedRupee")
        settings["OverrideHintPriorities"][2].append("MundaneItemCuriosityShopPurpleRupee")
        gossipHintsTakenByAlways += 1
        nonzeroCategories += 1

    wgtsMinigames = [100,0,0]
    if hardOptions >= HARD_OPTIONS_LIMIT or (gossipHintsTakenByAlways + 3) > GOSSIP_HINTS_LIMIT:
        wgtsMinigames[1] += wgtsMinigames[2]
        wgtsMinigames[2] = 0
    if gossipHintsTakenByAlways >= GOSSIP_HINTS_LIMIT:
        wgtsMinigames[0] += wgtsMinigames[1]
        wgtsMinigames[1] = 0
    if (customModes["No Clock Town"] == True):
        wgtsMinigames = [100,0,0]
    catMinigames = random.choices(["---",
                                    "Swamp 2 + Full TCG + Extra",
                                    "All shuffled"],
                                   wgtsMinigames)
    catMinigamesExtra = ["---"]
    if catMinigames[0] == "Swamp 2 + Full TCG + Extra":
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------70000-----------1000000-")
        catMinigamesExtra = random.choices(["DPG Three Days", "H&D Three Days", "Town Archery 50"])
    if catMinigamesExtra[0] == "DPG Three Days" or catMinigames[0] == "All shuffled":
        itemListString = AddEntryToListString(itemListString,1,"20000")  
        settings["OverrideHintPriorities"][0].append("MundaneItemDekuPlaygroundPurpleRupee")
        settings["OverrideHintPriorities"][0].append("HeartPieceDekuPlayground")
        gossipHintsTakenByAlways += 1
    if catMinigamesExtra[0] == "H&D Three Days" or catMinigames[0] == "All shuffled":
        itemListString = AddEntryToListString(itemListString,1,"80000")  
        settings["OverrideHintPriorities"][0].append("MundaneItemHoneyAndDarlingPurpleRupee")
        settings["OverrideHintPriorities"][0].append("HeartPieceHoneyAndDarling")
        gossipHintsTakenByAlways += 1
    if catMinigamesExtra[0] == "Town Archery 50" or catMinigames[0] == "All shuffled":
        itemListString = AddEntryToListString(itemListString,1,"40000")  
        settings["OverrideHintPriorities"][0].append("UpgradeBigQuiver")
        settings["OverrideHintPriorities"][0].append("HeartPieceTownArchery")
        gossipHintsTakenByAlways += 1
    if catMinigames[0] == "All shuffled":
        catMinigamesExtra = ["All three"]
        hardOptions += 1
    if catMinigames[0] != "---":
        settings["DoubleArcheryRewards"] = True
        nonzeroCategories += 1
        
    wgtsBombersNotebook = [80,10,10]
    if customModes["Main Density Mode"] == "Super":
        wgtsBombersNotebook = [50,20,30]
    if hardOptions >= HARD_OPTIONS_LIMIT or gossipHintsTakenByAlways >= GOSSIP_HINTS_LIMIT:
        wgtsBombersNotebook[1] += wgtsBombersNotebook[2]
        wgtsBombersNotebook[2] = 0
    if (customModes["No Clock Town"] == True):
        wgtsBombersNotebook = [100,0,0]
    catBombersNotebook = random.choices(["---",
                                         "Meetings only",
                                         "All shuffled"],
                                        wgtsBombersNotebook)
    if catBombersNotebook[0] == "Meetings only":
        startListString = AddEntryToListString(startListString,0,"400000")
        itemListString = AddStringToListString(itemListString,
                                               "----1fff-fe000000--------------------------------")
        settings["OverrideHintPriorities"][1].append("NotebookMeetKafei")
        settings["OverrideHintPriorities"][2].append("NotebookMeetShiro")
    if catBombersNotebook[0] == "All shuffled":
        startListString = AddEntryToListString(startListString,0,"400000")
        itemListString = AddStringToListString(itemListString,
                                               "---f7f-ffffffff-fe000000--------------------------------")
        if catLongQuests[0] == "Anju and Kafei" or catLongQuests[0] == "All Long Quests":
            itemListString = AddEntryToListString(itemListString,34,"80")
            settings["OverrideHintPriorities"][0].append("NotebookUniteAnjuAndKafei")
        settings["OverrideHintPriorities"][0].append("NotebookEscapeFromSakonSHideout")
        settings["OverrideHintPriorities"][2].append("NotebookPostmansFreedom")
        settings["OverrideHintPriorities"][2].append("MaskPostmanHat")
        settings["OverrideHintPriorities"][1].append("NotebookPurchaseCuriosityShopItem")
        settings["OverrideHintPriorities"][1].append("MaskAllNight")
        settings["OverrideHintPriorities"][2].append("NotebookDeliverPendant")
        settings["OverrideHintPriorities"][2].append("NotebookDeliverLetterToMama")
        settings["OverrideHintPriorities"][2].append("NotebookPromiseAnjuDelivery")
        settings["OverrideHintPriorities"][0].append("NotebookSaveTheCows")
        settings["OverrideHintPriorities"][0].append("NotebookProtectMilkDelivery")
        settings["OverrideHintPriorities"][2].append("NotebookGrogsThanks")
        settings["OverrideHintPriorities"][2].append("NotebookMovingGorman")
        settings["OverrideHintPriorities"][2].append("NotebookPromiseKamaro")
        settings["OverrideHintPriorities"][2].append("NotebookSaveInvisibleSoldier")
        settings["OverrideHintPriorities"][2].append("NotebookMeetShiro")
        if catSongsanity[0] == "Mix songs with items":
            settings["OverrideHintPriorities"][2].append("NotebookPromiseRomani")
        gossipHintsTakenByAlways += 1
        hardOptions += 1
    if catBombersNotebook[0] != "---":
        nonzeroCategories += 1

    if (customModes["No Clock Town"] == True):
        itemListString = RemoveStringFromListString(itemListString,
                                                    "1---fff-ffffffff-fe000000-ff80000-1fffc00--1ffff-80000000--8000000--7-700--1e00-200---3e000--8000180--7f008f-c0000000-2---600-fd8000-800-c7f-80000001-70ee04-3fffc4-54600820")
        junkListString = RemoveStringFromListString(junkListString,
                                                    "1---fff-ffffffff-fe000000-ff80000-1fffc00--1ffff-80000000--8000000--7-700--1e00-200---3e000--8000180--7f008f-c0000000-2---600-fd8000-800-c7f-80000001-70ee04-3fffc4-54600820")
        itemListString = AddStringToListString(itemListString,
                                               "-------------------------c-----600-f58000-800---10a804-35fc04-54200820")
        junkListString = AddStringToListString(junkListString,
                                               "-------------------------c-----600-f58000-800---10a804-35fc04-54200820")
        if (catLongQuests[0] == "Frog Choir" and catFrogs[0] == "Shuffled"):
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
        shuffleAndJunkHearts = "------------------------------1e0000------110f0000-"
        if catMinigames[0] == "All shuffled":
            shuffleAndJunkHearts = "------------------------------1e0000------10000-"
        elif catMinigamesExtra[0] == "DPG Three Days":
            shuffleAndJunkHearts = "------------------------------1e0000------d0000-"
        elif catMinigamesExtra[0] == "H&D Three Days":
            shuffleAndJunkHearts = "------------------------------1e0000------70000-"
        elif catMinigamesExtra[0] == "Town Archery 50":
            shuffleAndJunkHearts = "------------------------------1e0000------b0000-"
        itemListString = AddStringToListString(itemListString, shuffleAndJunkHearts)                                               
        junkListString = AddStringToListString(junkListString, shuffleAndJunkHearts)                                                   

    if nonzeroCategories < NONZERO_CATEGORIES_MINIMUM:
        return ''
    
    settings["CustomItemListString"] = itemListString
    settings["CustomStartingItemListString"] = startListString
    settings["CustomJunkLocationsString"] = junkListString

    outputFilename = inputFilename.removesuffix(".json")
    outputFilename = outputFilename.removesuffix("base")
    outputFilename = "output\\" + FilenameOnly(outputFilename) + outputSuffix + ".json" 

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
            if (customModes["Goal Mode"] != "Normal"):
                print("                Goal Mode: ", customModes["Goal Mode"],file=spoiler_file)
            if (customModes["Direct to Credits"] or customModes["Goal Mode"] == "Five Fairy Hunt"):
                print("                            (Direct to Credits is on)", file=spoiler_file)
            if (customModes["Start Mode"] == "Kokiri" or customModes["Start Mode"] == "Swordless"):
                print("    Start Difficulty Mode: ", customModes["Start Mode"],file=spoiler_file)
            if (customModes["Random Item Mode"] != "Any (Default)"):
                print("          Start Item Mode: ", customModes["Random Item Mode"],file=spoiler_file)
            if (customModes["FD Anywhere Mode"] != "Sometimes (Default)"):
                print("         FD Anywhere Mode: ", customModes["FD Anywhere Mode"],file=spoiler_file)
            if (customModes["Main Density Mode"] != "Normal"):
                print("        Main Density Mode: ", customModes["Main Density Mode"],file=spoiler_file)
            if (customModes["No Clock Town"]):
                print("            No Clock Town: ", customModes["No Clock Town"],file=spoiler_file)
            if (customModes["No Post-Temple"]):
                print("           No Post-Temple: ", customModes["No Post-Temple"],file=spoiler_file)
            if (customModes["Map and Compass Hints"]):
                print("    Map and Compass Hints: ", customModes["Map and Compass Hints"],file=spoiler_file)
            if (customModes["Boss Keys"] != "Default"):
                print("                Boss Keys: ", customModes["Boss Keys"],file=spoiler_file)
            if (customModes["Potsanity"] != "Default"):
                print("                Potsanity: ", customModes["Potsanity"],file=spoiler_file)
            if (customModes["Scoopsanity"] != "Default"):
                print("              Scoopsanity: ", customModes["Scoopsanity"],file=spoiler_file)
            if (customModes["Vanilla Eggs for Baby Zoras"]):
                print("Vanilla Eggs + Baby Zoras: ", customModes["Vanilla Eggs for Baby Zoras"],file=spoiler_file)
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
        if (customModes["Start Mode"] == "Default"):
            print("Starting Sword and Shield: ", catStartingSwordShield[0],file=spoiler_file)
        else:
            print("               Start Mode: ", catStartingSwordShield[0],file=spoiler_file)
        if catStartingSwordShield[0] != "Cruel Start":
            print("     Starting Random Item: ", catStartingRandomItem[0],file=spoiler_file)
        if catStartingBossRemains[0] == "Five Fairy Hunt" or (catStartingBossRemains[0] == "Mask Hunt" and customModes["No Clock Town"]):
            print("            Starting Song: ", catStartingRandomSong[0],file=spoiler_file)
        else:
            print("     Starting Random Song: ", catStartingRandomSong[0],file=spoiler_file)
        if customModes["No Clock Town"] == True or catStartingBossRemains[0] == "Five Fairy Hunt" or (catStartingBossRemains[0] == "Mask Hunt" and customModes["No Clock Town"]):
            print("      Extra Starting Song:  Epona's Song", file=spoiler_file)
        if (catStartingBossRemains[0] == "Mask Hunt" and customModes["No Clock Town"] == False):
            print("      Extra Starting Song:  Oath to Order", file=spoiler_file)
        if catStartingSwordShield[0] != "Cruel Start":
            print("    Fierce Deity Anywhere: ", catFierceDeityAnywhere[0],file=spoiler_file)
        print("",file=spoiler_file)
        if (customModes["No Clock Town"] == True or customModes["No Post-Temple"] == True):
            if (customModes["No Clock Town"] == True):
                print(" ***        No Clock Town Checks!        ***",file=spoiler_file)
            if (customModes["No Post-Temple"] == True):
                print(" ***       No Post-Temple Checks!        ***",file=spoiler_file)
            print("",file=spoiler_file)
        print("               Songsanity: ", catSongsanity[0],file=spoiler_file) 
        print("       Shopsanity: Checks: ", catShopsanityChecks[0],file=spoiler_file)
        print("       Shopsanity: Prices: ", catShopsanityPrices[0],file=spoiler_file)
        print("               Soilsanity: ", catSoilsanity[0],file=spoiler_file)
        print("                Cowsanity: ", catCowsanity[0],file=spoiler_file)
        print("            Stray Fairies: ", catStrayFairies[0],file=spoiler_file)
        print("       Entrances: Temples: ", catEntrancesTemples[0],file=spoiler_file)
        if catStartingBossRemains[0] == "Five Fairy Hunt":
            print("    Entrances: Boss Rooms:  Disabled (by Five Fairy Hunt)", file=spoiler_file)
            print("     Keysanity: Boss Keys:  Disabled (by Five Fairy Hunt)", file=spoiler_file)
        else:
            print("    Entrances: Boss Rooms: ", catEntrancesBossRooms[0],file=spoiler_file)
            print("     Keysanity: Boss Keys: ", catKeysanityBossKeys[0],file=spoiler_file)
        print("    Keysanity: Small Keys: ", catKeysanitySmallKeys[0],file=spoiler_file)
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
        print("              Long Quests: ", catLongQuests[0],file=spoiler_file)
        print("                    Frogs: ", catFrogs[0],file=spoiler_file)
        print("             Loose Rupees: ", catLooseRupees[0],file=spoiler_file)
        print("               Snowsanity: ", catSnowsanity[0],file=spoiler_file)
        print("                Potsanity: ", catPotsanity[0],file=spoiler_file)
        print("Photos/Sales/Small Favors: ", catPhotosSales[0],file=spoiler_file)
        if customModes["No Clock Town"] == True:
            print("        Bombers' Notebook:  Disabled (by No Clock Town)", file=spoiler_file)
        else:
            print("        Bombers' Notebook: ", catBombersNotebook[0],file=spoiler_file)
        print("---------------------------------------------",file=spoiler_file)
        print("  Gossip slots for always: ",gossipHintsTakenByAlways,file=spoiler_file)
        print("        Hard options used: ",hardOptions,file=spoiler_file)
        print("       Nonzero categories: ",nonzeroCategories,file=spoiler_file)

    return outputFilename

argParser = argparse.ArgumentParser(description="Randomly generates Mystery settings files for MMR and runs MMR.CLI to roll seeds with them.")
argParser.add_argument("-n", dest="numberOfSettingsFiles",type=int,default=1,
                    help="create multiple settings/seeds at once")
argParser.add_argument("-i", "--input", dest="inputFile",default="Default_Mystery_base.json",
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
    while (resultFilename == ''):
        resultFilename = GenerateMysterySettings(optionSettingsFile,optionCustomModes,(str)(i+1))
    if (optionDontMakeSeed == False):
        mmrcl = optionRandomizerExe + " -outputpatch -spoiler -settings " + resultFilename
        subprocess.call(mmrcl)
