from mysteryutils.SettingsFile import *
from mysteryutils.Definitions import *
from mysteryutils.Category import Category, Shuffle
from mysteryutils.CategoryListGen import CreateSetupCategoryList, CreateMainCategoryList, ApplyWeights
from mysteryutils.ListStringUtils import *
import random

def FilenameOnly(pathstring):
    filename = pathstring[(pathstring.rfind("/") + 1):]
    filename = filename[(filename.rfind("\\") + 1):]
    return filename

class MysterySeed:
    def __init__(self, seed: SettingsFile, options: dict):
        self.seed = seed
        self.options = options
        
        self.setupCategories: dict[str, Category] = {}
        self.mainCategories: dict[str, Category] = {}

    def build(self):
        # build category lists
        self.setupCategories = CreateSetupCategoryList()
        self.mainCategories = CreateMainCategoryList()
        ApplyWeights(self.setupCategories, self.mainCategories, self.options)

        # extract MMR item strings from settings files
        startList = self.seed.getBasicSetting("CustomStartingItemListString")
        checkPool = self.seed.getBasicSetting("CustomItemListString")
        junkList = self.seed.getBasicSetting("CustomJunkLocationsString")

        # Goal Remains option
        if self.options[GeneratorOptionNames.GOALREMAINS] < 1:
            self.options[GeneratorOptionNames.GOALREMAINS] = 1
        if self.options[GeneratorOptionNames.GOALREMAINS] > 4:
            self.options[GeneratorOptionNames.GOALREMAINS] = 4
        match self.options[GeneratorOptionNames.GOALREMAINS]:
            case 1:
                self.seed.setBasicSetting("VictoryMode","CantFightMajora, OneBossRemains")
            case 2:
                self.seed.setBasicSetting("VictoryMode","CantFightMajora, TwoBossRemains")
            case 3:
                self.seed.setBasicSetting("VictoryMode","CantFightMajora, ThreeBossRemains")
            case 4:
                self.seed.setBasicSetting("VictoryMode","CantFightMajora, FourBossRemains")
        self.seed.setBasicSetting("RequiredBossRemains", self.options[GeneratorOptionNames.GOALREMAINS])

        # Goal Mode option
        match self.options[GeneratorOptionNames.GOAL]:
            case GoalNames.REMAINSONBOSSES:
                pass
            case GoalNames.REMAINSSHUFFLE:
                checkPool = AddStringToListString(checkPool, shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_REMAINS)])
            case GoalNames.FAIRYHUNT:
                if self.options[GeneratorOptionNames.GOALFAIRYSET] < 0:
                    self.options[GeneratorOptionNames.GOALREMAINS] = 0
                if self.options[GeneratorOptionNames.GOALREMAINS] > 15:
                    self.options[GeneratorOptionNames.GOALREMAINS] = 15
                startList = RemoveStringFromListString(startList, strayFairyStartItemStrings[15])
                startList = AddStringToListString(startList, strayFairyStartItemStrings[self.options[GeneratorOptionNames.GOALFAIRYSET]])
                startList = AddStringToListString(startList, startItemStrings[ItemNames.ITEM_GFM])
                checkPool = AddStringToListString(checkPool, shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_REMAINS)])
                junkList = RemoveStringFromListString(junkList, shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_DGFREWARDS)])
                self.seed.setBasicSetting("BossRemainsMode", "GreatFairyRewards")
            case GoalNames.MASKHUNT:
                self.seed.setBasicSetting("VictoryMode", self.seed.getBasicSetting("VictoryMode") + ", NonTransformationMasks")

        # Free Oath option
        if self.options[GeneratorOptionNames.FREEOATH] and self.options[GeneratorOptionNames.SONGLAYOUT] != ShuffleNames.SL_ALL:
            startList = AddStringToListString(startList, startItemStrings[ItemNames.SONG_OATH])
            checkPool = RemoveStringFromListString(checkPool, singleCheckStrings[CheckNames.BOSSBLUEWARP])
        
        # Free Epona option
        if self.options[GeneratorOptionNames.FREEEPONA] and self.options[GeneratorOptionNames.SONGLAYOUT] != ShuffleNames.SL_ALL:
            startList = AddStringToListString(startList, startItemStrings[ItemNames.SONG_EPONA])
            checkPool = RemoveStringFromListString(checkPool, singleCheckStrings[CheckNames.ROMANISGAME])
            self.setupCategories[CategoryNames.STARTINGSONG].guaranteeShuffle(ShuffleNames.SONG_ANYNONEPONA)

        # roll setup categories in order               
        for curName, curCategory in self.setupCategories.items():
            curCategory.roll()

            # modify Epona chance for Songsanity seeds
            if curName == CategoryNames.SONGLAYOUT and curCategory.getActiveShuffle() == ShuffleNames.SL_SANITY:
                self.setupCategories[CategoryNames.STARTINGSONG].modifyWeight(ShuffleNames.SONG_EPONA, -30)
                self.setupCategories[CategoryNames.STARTINGSONG].modifyWeight(ShuffleNames.SONG_ANYNONEPONA, 30)

        # resolve separate roll for non-Epona starting song
        if self.setupCategories[CategoryNames.STARTINGSONG].getActiveShuffle() == ShuffleNames.SONG_ANYNONEPONA:
            songCandidates = [ShuffleNames.SONG_SONATA,
                              ShuffleNames.SONG_LULLABY,
                              ShuffleNames.SONG_NEWWAVE,
                              ShuffleNames.SONG_ELEGY,
                              ShuffleNames.SONG_HEALING,
                              ShuffleNames.SONG_STORMS]
            selectedSong = random.choice(songCandidates)
            self.setupCategories[CategoryNames.STARTINGSONG].setActiveShuffle(selectedSong)
        
        # resolve FD Anywhere guarantee for a starting FD (if not prevented by option)
        if (self.setupCategories[CategoryNames.STARTINGITEM].getActiveShuffle() == ShuffleNames.ITEM_FD and
              self.options[GeneratorOptionNames.FDANYWHERE] != ShuffleNames.GENERIC_OFF):
            self.setupCategories[CategoryNames.FDANYWHERE].setActiveShuffle(ShuffleNames.FD_ON)

        # resolve "new ER guarantee" if needed (and not prevented by options)
        if (not self.setupCategories[CategoryNames.ERINTERIOR].isActive() and not self.setupCategories[CategoryNames.ERGROTTO].isActive() and
              self.options[GeneratorOptionNames.ERINTERIOR] == ShuffleNames.GENERIC_RANDOM and self.options[GeneratorOptionNames.ERGROTTO] == ShuffleNames.GENERIC_RANDOM):
            guaranteedERCandidates = [CategoryNames.ERINTERIOR, CategoryNames.ERGROTTO]
            guaranteedERWeights = [self.setupCategories[CategoryNames.ERINTERIOR].getWeight(ShuffleNames.GENERIC_SHUFFLED),
                                   self.setupCategories[CategoryNames.ERGROTTO].getWeight(ShuffleNames.GENERIC_SHUFFLED)]
            self.setupCategories[random.choices(guaranteedERCandidates, guaranteedERWeights)[0]].setActiveShuffle(ShuffleNames.GENERIC_SHUFFLED)
        
        # apply setup categories
        match self.setupCategories[CategoryNames.SONGLAYOUT].getActiveShuffle():
            case ShuffleNames.SL_SANITY:
                self.seed.setBasicSetting("AddSongs", True)
                checkPool = RemoveStringFromListString(checkPool, shuffleCheckStrings[(CategoryNames.SONGLAYOUT, ShuffleNames.SL_TRADITIONAL)])
                self.seed.setBasicSetting("OverrideNumberOfRequiredGossipHints", self.seed.getBasicSetting("OverrideNumberOfRequiredGossipHints") + 1)
                self.seed.setHintTierSize(0, self.seed.getHintTierSize(0) - 1)
            case ShuffleNames.SL_ALL:
                self.setupCategories[CategoryNames.STARTINGSONG].setActiveShuffle(ShuffleNames.SONG_ALL)
                checkPool = RemoveStringFromListString(checkPool, shuffleCheckStrings[(CategoryNames.SONGLAYOUT, ShuffleNames.SL_TRADITIONAL)])
        
        if self.setupCategories[CategoryNames.STARTINGITEM].getActiveShuffle() != ShuffleNames.GENERIC_OFF:
            itemToAdd = shuffleNameToItemName[self.setupCategories[CategoryNames.STARTINGITEM].getActiveShuffle()]
            startList = AddStringToListString(startList, startItemStrings[itemToAdd])
        
        songToAdd = shuffleNameToItemName[self.setupCategories[CategoryNames.STARTINGSONG].getActiveShuffle()]
        startList = AddStringToListString(startList, startItemStrings[songToAdd])

        if self.setupCategories[CategoryNames.FDANYWHERE].isActive():
            self.seed.setBasicSetting("AllowFierceDeityAnywhere", True)

        enabledERs = []        
        if self.setupCategories[CategoryNames.ERINTERIOR].isActive():
            enabledERs.append("SimpleInteriors")
        if self.setupCategories[CategoryNames.ERGROTTO].isActive():
            enabledERs.append("Grottos")
        if self.setupCategories[CategoryNames.ERDUNGEON].isActive():
            enabledERs.append("DungeonEntrances")
        if len(enabledERs) > 0:
            self.seed.setBasicSetting("EntranceMode", ", ".join(enabledERs))
        
        if self.setupCategories[CategoryNames.SMALLKEYS].getActiveShuffle() == ShuffleNames.SM_KEYS_TEMPLES:
            self.seed.setBasicSetting("SmallKeyMode", "DoorsOpen, KeepWithinTemples, KeepThroughTime")
            self.seed.removeHintFromTier("ItemIceArrow", 2)
            self.seed.addHintToTier("ItemIceArrow", 1)
        
        # prepare active categories for rolling
        mainCategoryMinimum = self.options[GeneratorOptionNames.CATEGORYMINIMUM]
        if mainCategoryMinimum < 0:
            mainCategoryMinimum = 0
        if mainCategoryMinimum > 16:
            mainCategoryMinimum = 16
        rerollBatchSize = max((16 - mainCategoryMinimum) // 2, 1)
        categoriesToRoll = [CategoryNames.STRAYFAIRIES,
                            CategoryNames.SHOPCHECKS,
                            CategoryNames.SOILS,
                            CategoryNames.COWS,
                            CategoryNames.HITSPOTS,
                            CategoryNames.TOKENS,
                            CategoryNames.CRATESANDBARRELS,
                            CategoryNames.KEATONGRASS,
                            CategoryNames.PALMTREES,
                            CategoryNames.BUTTERFLYANDWELLFAIRIES,
                            CategoryNames.GOSSIPFAIRIES,
                            CategoryNames.LOOSERUPEESOVERWORLD,
                            CategoryNames.SNOWBALLS,
                            CategoryNames.POTS,
                            CategoryNames.MUNDANES,
                            CategoryNames.NOTEBOOKENTRIES]
        inactiveCategories = []
        activeCategories = []

        # roll active categories until the minimum is met, rerolling in batches as needed
        while (len(categoriesToRoll) > 0):
            curCategory = categoriesToRoll[0]
            self.mainCategories[curCategory].roll()
            curCategoryIsActive = self.mainCategories[curCategory].isActive()

            # special handling for the categories with two sets of shuffles -- Shopsanity and Loose Rupees 
            if curCategory == CategoryNames.SHOPCHECKS:                
                if self.options[GeneratorOptionNames.DENSITYMODE] != DensityNames.TOTAL:
                    match self.mainCategories[curCategory].getActiveShuffle():
                        case ShuffleNames.SHOP_C_THREE:
                            self.mainCategories[CategoryNames.SHOPPRICES].modifyWeight(ShuffleNames.SHOP_P_SHUFFLE, 15)
                            self.mainCategories[CategoryNames.SHOPPRICES].modifyWeight(ShuffleNames.SHOP_P_RANDOM, 5)
                        case ShuffleNames.SHOP_C_FULL:
                            self.mainCategories[CategoryNames.SHOPPRICES].modifyWeight(ShuffleNames.SHOP_P_SHUFFLE, 30)
                            self.mainCategories[CategoryNames.SHOPPRICES].modifyWeight(ShuffleNames.SHOP_P_RANDOM, 10)
                self.mainCategories[CategoryNames.SHOPPRICES].roll()
                curCategoryIsActive = curCategoryIsActive or self.mainCategories[CategoryNames.SHOPPRICES].isActive()

            if curCategory == CategoryNames.LOOSERUPEESOVERWORLD:
                self.mainCategories[CategoryNames.LOOSERUPEESTEMPLES].roll()
                curCategoryIsActive = curCategoryIsActive or self.mainCategories[CategoryNames.LOOSERUPEESTEMPLES].isActive()
            
            categoriesToRoll.remove(curCategory)
            if curCategoryIsActive:
                activeCategories.append(curCategory)
            else:
                inactiveCategories.append(curCategory)
            
            if len(categoriesToRoll) == 0 and len(activeCategories) < mainCategoryMinimum:
                random.shuffle(inactiveCategories)
                for n in range(rerollBatchSize):
                    categoriesToRoll.append(inactiveCategories[0])
                    inactiveCategories.remove(0)
        
        # resolve separate roll for Single-House Tokens' spider house
        if self.mainCategories[CategoryNames.TOKENS].getActiveShuffle() == ShuffleNames.TOKENS_ONE:
            houseCandidates = [ShuffleNames.TOKENS_SSH,
                               ShuffleNames.TOKENS_OSH]
            selectedHouse = random.choice(houseCandidates)
            self.mainCategories[CategoryNames.TOKENS].setActiveShuffle(selectedHouse)

        # apply active categories
        for curName, curCategory in self.mainCategories.items():
            if curCategory.isActive() and curName != CategoryNames.SHOPPRICES:
                checkPool = AddStringToListString(checkPool, shuffleCheckStrings[(curName, curCategory.getActiveShuffle())])
        
        if self.mainCategories[CategoryNames.STRAYFAIRIES].isActive():
            self.seed.setBasicSetting("StrayFairyMode", "Default")

        # special handling of Stray Fairies for Fairy Hunt: always shuffle dungeon strays, but junk inactive checks
        if self.options[GeneratorOptionNames.GOAL] == GoalNames.FAIRYHUNT:
            self.seed.setBasicSetting("StrayFairyMode", "Default")
            checkPool = AddStringToListString(checkPool, shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.FAIRY_HUNT_FULL_DUNGEON_STRAYS)])
            match self.mainCategories[CategoryNames.STRAYFAIRIES]:
                case ShuffleNames.STRAYS_BUBBLES:
                    junkList = AddStringToListString(junkList, shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.FAIRY_HUNT_INVERTED_STRAYS_BUBBLES)])
                case ShuffleNames.GENERIC_OFF:
                    junkList = AddStringToListString(junkList, shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.FAIRY_HUNT_INVERTED_STRAYS_CORE)])

        match self.mainCategories[CategoryNames.SHOPPRICES].getActiveShuffle():
            case ShuffleNames.SHOP_P_SHUFFLE:
                self.seed.setBasicSetting("PriceMode", "Purchases, ShuffleOnly")
            case ShuffleNames.SHOP_P_RANDOM:
                self.seed.setBasicSetting("PriceMode", "Purchases")
                self.seed.setBasicSetting("FillWallet", True)
        
        if (self.mainCategories[CategoryNames.TOKENS].getActiveShuffle() == ShuffleNames.TOKENS_OSH or
              self.mainCategories[CategoryNames.TOKENS].getActiveShuffle() == ShuffleNames.TOKENS_BOTH):
            self.seed.removeHintFromTier("HeartPieceOceanSpiderHouse", 1)
        
        if self.mainCategories[CategoryNames.BUTTERFLYANDWELLFAIRIES].isActive() or self.mainCategories[CategoryNames.POTS].isActive():
            self.seed.removeHintFromTier("ChestWellLeftPurpleRupee", 2)
        
        if self.mainCategories[CategoryNames.POTS].isActive():
            self.seed.removeHintFromTier("CollectibleStrayFairyStoneTower7", 2)  # Inverted Stone Tower Temple Wizzrobe
        
        if self.mainCategories[CategoryNames.NOTEBOOKENTRIES].isActive():
            startList = AddStringToListString(startList, startItemStrings[ItemNames.ITEM_NOTEBOOK])

        # apply the Excluded Checks string (junk Excluded Checks that are in the core check list, unshuffle Excluded Checks that aren't in the core check list)
        baselineStringOverlap = GetListStringOverlap(shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_CHECKS)], self.options[GeneratorOptionNames.EXCLUDECHECKS])
        excludeMinusBaselineStringOverlap = RemoveStringFromListString(self.options[GeneratorOptionNames.EXCLUDECHECKS], baselineStringOverlap)
        junkList = AddStringToListString(junkList, baselineStringOverlap)
        checkPool = RemoveStringFromListString(checkPool, excludeMinusBaselineStringOverlap)

        # restore item strings to settings files
        self.seed.setBasicSetting("CustomStartingItemListString", startList)
        self.seed.setBasicSetting("CustomItemListString", checkPool)
        self.seed.setBasicSetting("CustomJunkLocationsString", junkList)

    def write(self):
        self.seed.write()

    def spoil(self):
        usingCustomOptions = False
        customOptions = []

        for option in self.options:
            if self.options[option] != OPTION_DEFAULTS[option]:
                usingCustomOptions = True
                customOptions.append(option)
        
        spoilerLogFilename = self.seed.getOutputFilePath().removesuffix(".json") + "_MysterySpoiler.txt"
        
        with open(spoilerLogFilename, "w") as spoiler_file:
            print("MMR Mystery Maker", MYSTERY_MAKER_VERSION,"-- Mystery Spoiler Log",file=spoiler_file)
            print("Base settings: ", FilenameOnly(self.seed.getBaseFilePath()),file=spoiler_file)
            print("  Output file: ", FilenameOnly(self.seed.getOutputFilePath()),file=spoiler_file)
            if (usingCustomOptions):
                print(" ***        CUSTOM OPTIONS ACTIVE!       *** ",file=spoiler_file)
                for option in customOptions:
                    print(f"{option:>28}:  {self.options[option]}",file=spoiler_file)
            print("=============================================",file=spoiler_file)
            for s, sc in self.setupCategories.items():
                print(sc.spoil(), file=spoiler_file)
            print("", file=spoiler_file)
            for m, mc in self.mainCategories.items():
                print(mc.spoil(), file=spoiler_file)
            



    

    
            
        


            






                    




        