from mysteryutils.Category import Category, Shuffle
from mysteryutils.Definitions import DensityNames, GeneratorOptionNames, CategoryNames, ShuffleNames, shuffleCheckStrings, categoryWeights

def AddCategory(categoryList, categoryName, categoryDescription):
    categoryList[categoryName] = Category(categoryName, categoryDescription)

def AddSimpleCategory(categoryList, categoryName, categoryDescription):
    AddCategory(categoryList, categoryName, categoryDescription)
    AddShuffle(categoryList, categoryName, ShuffleNames.GENERIC_SHUFFLED)

def AddSimpleCategoryWithString(categoryList, categoryName, categoryDescription):
    AddCategory(categoryList, categoryName, categoryDescription)
    AddShuffleWithString(categoryList, categoryName, ShuffleNames.GENERIC_SHUFFLED)

def AddShuffle(categoryList, categoryName, shuffleName):
    categoryList[categoryName].defineShuffle(Shuffle(shuffleName))

def AddShuffleWithString(categoryList, categoryName, shuffleName):
    sh = Shuffle(shuffleName)
    sh.setItemString(shuffleCheckStrings[(categoryName, shuffleName)])
    categoryList[categoryName].defineShuffle(sh)

def HideCategoryByDefault(categoryList, categoryName):
    categoryList[categoryName].setHidden(True)

def CreateSetupCategoryList():
    setupList: dict[str, Category] = {}
    
    AddCategory(setupList, CategoryNames.SONGLAYOUT, "How songs are placed.")
    AddShuffle(setupList, CategoryNames.SONGLAYOUT, ShuffleNames.SL_TRADITIONAL)
    AddShuffle(setupList, CategoryNames.SONGLAYOUT, ShuffleNames.SL_SANITY)
    AddShuffle(setupList, CategoryNames.SONGLAYOUT, ShuffleNames.SL_ALL)

    AddCategory(setupList, CategoryNames.STARTINGITEM, "Which extra item you start with.")
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_DEKU)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_GORON)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_ZORA)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_FD)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_BOW)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_HOOK)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_BOMBS)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_BLAST)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_WALLET)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_BOTTLE)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_BUNNY)
    AddShuffle(setupList, CategoryNames.STARTINGITEM, ShuffleNames.ITEM_GFS)

    AddCategory(setupList, CategoryNames.STARTINGSONG, "Which extra song you start with.")
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_EPONA)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_SONATA)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_LULLABY)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_NEWWAVE)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_ELEGY)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_HEALING)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_STORMS)
    AddShuffle(setupList, CategoryNames.STARTINGSONG, ShuffleNames.SONG_ANYNONEPONA)

    AddCategory(setupList, CategoryNames.FREEDUNGEONSONG, "Which extra dungeon song you start with.")
    AddShuffle(setupList, CategoryNames.FREEDUNGEONSONG, ShuffleNames.SONG_EPONA)
    AddShuffle(setupList, CategoryNames.FREEDUNGEONSONG, ShuffleNames.SONG_SONATA)
    AddShuffle(setupList, CategoryNames.FREEDUNGEONSONG, ShuffleNames.SONG_LULLABY)
    AddShuffle(setupList, CategoryNames.FREEDUNGEONSONG, ShuffleNames.SONG_NEWWAVE)
    AddShuffle(setupList, CategoryNames.FREEDUNGEONSONG, ShuffleNames.SONG_ANYDUNGEON)
    HideCategoryByDefault(setupList, CategoryNames.FREEDUNGEONSONG)

    AddCategory(setupList, CategoryNames.STARTINGGEAR, "Which basic gear you start with.")
    AddShuffle(setupList, CategoryNames.STARTINGGEAR, ShuffleNames.SG_STRONG)
    AddShuffle(setupList, CategoryNames.STARTINGGEAR, ShuffleNames.SG_KOKIRI)
    AddShuffle(setupList, CategoryNames.STARTINGGEAR, ShuffleNames.SG_SWORDLESS)
    AddShuffle(setupList, CategoryNames.STARTINGGEAR, ShuffleNames.SG_FRAGILE)
    HideCategoryByDefault(setupList, CategoryNames.STARTINGGEAR)

    AddCategory(setupList, CategoryNames.FDANYWHERE, "Whether FD Anywhere is on.")
    AddShuffle(setupList, CategoryNames.FDANYWHERE, ShuffleNames.FD_ON)

    AddSimpleCategory(setupList, CategoryNames.ERINTERIOR, "Whether Simple Interior entrances are shuffled.")
    HideCategoryByDefault(setupList, CategoryNames.ERINTERIOR)

    AddSimpleCategory(setupList, CategoryNames.ERGROTTO, "Whether grotto entrances are shuffled.")
                                                      
    AddSimpleCategory(setupList, CategoryNames.ERDUNGEON, "Whether dungeon entrances are shuffled.")

    AddCategory(setupList, CategoryNames.SMALLKEYS, "Whether Small Keys are in play and shuffled.")
    AddShuffle(setupList, CategoryNames.SMALLKEYS, ShuffleNames.SM_KEYS_TEMPLES)

    return setupList

def CreateMainCategoryList():
    mainList: dict[str, Category] = {}

    AddCategory(mainList, CategoryNames.STRAYFAIRIES, "Stray Fairies beyond the core set.")
    AddShuffleWithString(mainList, CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_BUBBLES)
    AddShuffleWithString(mainList, CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_FULL)

    AddCategory(mainList, CategoryNames.SHOPCHECKS, "Items for sale in shops and by merchants.")
    AddShuffleWithString(mainList, CategoryNames.SHOPCHECKS, ShuffleNames.SHOP_C_THREE)
    AddShuffleWithString(mainList, CategoryNames.SHOPCHECKS, ShuffleNames.SHOP_C_FULL)

    AddCategory(mainList, CategoryNames.SHOPPRICES, "Prices of items for sale.")
    AddShuffle(mainList, CategoryNames.SHOPPRICES, ShuffleNames.SHOP_P_SHUFFLE)
    AddShuffle(mainList, CategoryNames.SHOPPRICES, ShuffleNames.SHOP_P_RANDOM)

    AddSimpleCategoryWithString(mainList, CategoryNames.SOILS, "Items from placing bugs in soft soils.")
    
    AddSimpleCategoryWithString(mainList, CategoryNames.COWS, "Milk from cows.")
    
    AddCategory(mainList, CategoryNames.HITSPOTS, "Rupees from striking certain locations.")
    AddShuffleWithString(mainList, CategoryNames.HITSPOTS, ShuffleNames.HITS_SINGLE)

    AddCategory(mainList, CategoryNames.TOKENS, "Gold Skulltula tokens from Spider Houses.")
    AddShuffle(mainList, CategoryNames.TOKENS, ShuffleNames.TOKENS_ONE)
    AddShuffleWithString(mainList, CategoryNames.TOKENS, ShuffleNames.TOKENS_SSH)
    AddShuffleWithString(mainList, CategoryNames.TOKENS, ShuffleNames.TOKENS_OSH)
    AddShuffleWithString(mainList, CategoryNames.TOKENS, ShuffleNames.TOKENS_BOTH)

    AddSimpleCategoryWithString(mainList, CategoryNames.CRATESANDBARRELS, "Items in crates and barrels.")

    AddCategory(mainList, CategoryNames.KEATONGRASS, "Rupees from spin-attacking Keaton Grass in quick succession.")
    AddShuffleWithString(mainList, CategoryNames.KEATONGRASS, ShuffleNames.KEATON_ODD)
    AddShuffleWithString(mainList, CategoryNames.KEATONGRASS, ShuffleNames.KEATON_FULL)

    AddSimpleCategoryWithString(mainList, CategoryNames.PALMTREES, "Deku Nuts from palm trees.")

    AddSimpleCategoryWithString(mainList, CategoryNames.BUTTERFLYANDWELLFAIRIES, "Fairies from butterflies and Beneath the Well.")

    AddSimpleCategoryWithString(mainList, CategoryNames.GOSSIPFAIRIES, "Fairies from Gossip Stones not originally in central Termina.")

    AddCategory(mainList, CategoryNames.LOOSERUPEESOVERWORLD, "Freestanding and invisible Rupees in the overworld.")
    AddShuffleWithString(mainList, CategoryNames.LOOSERUPEESOVERWORLD, ShuffleNames.LOOSE_O_R)
    AddShuffleWithString(mainList, CategoryNames.LOOSERUPEESOVERWORLD, ShuffleNames.LOOSE_O_RB)
    AddShuffleWithString(mainList, CategoryNames.LOOSERUPEESOVERWORLD, ShuffleNames.LOOSE_O_RBG)

    AddCategory(mainList, CategoryNames.LOOSERUPEESTEMPLES, "Freestanding and invisible Rupees in temples.")
    AddShuffleWithString(mainList, CategoryNames.LOOSERUPEESTEMPLES, ShuffleNames.LOOSE_T_R)
    AddShuffleWithString(mainList, CategoryNames.LOOSERUPEESTEMPLES, ShuffleNames.LOOSE_T_RBG)

    AddCategory(mainList, CategoryNames.SNOWBALLS, "Items in snowballs.")
    AddShuffleWithString(mainList, CategoryNames.SNOWBALLS, ShuffleNames.SNOW_SH)
    AddShuffleWithString(mainList, CategoryNames.SNOWBALLS, ShuffleNames.SNOW_ANY)

    AddCategory(mainList, CategoryNames.POTS, "Items in pots.")
    AddShuffleWithString(mainList, CategoryNames.POTS, ShuffleNames.POTS_TWED)

    AddSimpleCategoryWithString(mainList, CategoryNames.MUNDANES, "Items from taking photos, selling bottle contents, and doing small favors.")

    AddCategory(mainList, CategoryNames.NOTEBOOKENTRIES, "Entries in the Bombers' Notebook.")
    AddShuffleWithString(mainList, CategoryNames.NOTEBOOKENTRIES, ShuffleNames.NOTE_MEET)
    AddShuffleWithString(mainList, CategoryNames.NOTEBOOKENTRIES, ShuffleNames.NOTE_FULL)

    return mainList

def ApplyWeights(setupList, mainList, customOptions):
    weightDict = categoryWeights[customOptions[GeneratorOptionNames.DENSITYMODE]]

    # Start with the base weights for the given density mode
    for c in setupList:
        setupList[c].setWeights(weightDict[c])

    for c in mainList:
        mainList[c].setWeights(weightDict[c])

    # Song layout changes from option
    if (customOptions[GeneratorOptionNames.SONGLAYOUT] != ShuffleNames.GENERIC_RANDOM):
        setupList[CategoryNames.SONGLAYOUT].guaranteeShuffle(customOptions[GeneratorOptionNames.SONGLAYOUT])
     
    # Starting item changes from option
    if (customOptions[GeneratorOptionNames.RANDOMITEM] == ShuffleNames.GENERIC_OFF):
        setupList[CategoryNames.STARTINGITEM].zeroAllShuffles()
    elif (customOptions[GeneratorOptionNames.RANDOMITEM] != ShuffleNames.GENERIC_RANDOM):
        setupList[CategoryNames.STARTINGITEM].guaranteeShuffle(customOptions[GeneratorOptionNames.RANDOMITEM])

    # Extra dungeon song changes from option
    if (customOptions[GeneratorOptionNames.FREEDUNGEONSONG]):
        setupList[CategoryNames.FREEDUNGEONSONG].guaranteeShuffle(ShuffleNames.SONG_ANYDUNGEON)
        setupList[CategoryNames.FREEDUNGEONSONG].setHidden(False)

    # Starting gear changes from option
    if (customOptions[GeneratorOptionNames.STARTGEAR] != ShuffleNames.SG_KOKIRI):
        setupList[CategoryNames.STARTINGGEAR].guaranteeShuffle(customOptions[GeneratorOptionNames.STARTGEAR])
        setupList[CategoryNames.STARTINGGEAR].setHidden(False)

    # FD Anywhere changes from option
    if (customOptions[GeneratorOptionNames.FDANYWHERE] == ShuffleNames.GENERIC_OFF):
        setupList[CategoryNames.FDANYWHERE].zeroAllShuffles()
    elif (customOptions[GeneratorOptionNames.FDANYWHERE] == ShuffleNames.FD_STARTING):
        setupList[CategoryNames.FDANYWHERE].zeroAllShuffles()
    elif (customOptions[GeneratorOptionNames.FDANYWHERE] == ShuffleNames.FD_ON):
        setupList[CategoryNames.FDANYWHERE].guaranteeShuffle(ShuffleNames.FD_ON)
    
    # ER changes from options
    if (customOptions[GeneratorOptionNames.ERINTERIOR] != ShuffleNames.GENERIC_OFF):
        setupList[CategoryNames.ERINTERIOR].guaranteeShuffle(customOptions[GeneratorOptionNames.ERINTERIOR])
        setupList[CategoryNames.ERINTERIOR].setHidden(False)

    if (customOptions[GeneratorOptionNames.ERGROTTO] != ShuffleNames.GENERIC_RANDOM):
        setupList[CategoryNames.ERGROTTO].guaranteeShuffle(customOptions[GeneratorOptionNames.ERGROTTO])
    
    if (customOptions[GeneratorOptionNames.ERDUNGEON] != ShuffleNames.GENERIC_RANDOM):
        setupList[CategoryNames.ERDUNGEON].guaranteeShuffle(customOptions[GeneratorOptionNames.ERDUNGEON])
    
    # Small Keys change from option
    if (customOptions[GeneratorOptionNames.SMALLKEYS] != ShuffleNames.GENERIC_RANDOM):
        setupList[CategoryNames.SMALLKEYS].guaranteeShuffle(customOptions[GeneratorOptionNames.SMALLKEYS])
