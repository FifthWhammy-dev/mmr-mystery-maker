from enum import StrEnum

MYSTERY_MAKER_VERSION = "v6.1.1"
MYSTERY_MAKER_VERSION_FILENAME = "v6_1_1"

class OutputModes(StrEnum):
    WEB = "Web Settings"
    DESKTOP = "Desktop Settings"
    DESKTOPANDSEED = "Desktop Settings and Seed"

class GoalNames(StrEnum):
    REMAINSONBOSSES = "Remains on Bosses"
    REMAINSSHUFFLE = "Remains Shuffle"
    FAIRYHUNT = "Fairy Hunt"
    MASKHUNT = "Mask Hunt"

class DensityNames(StrEnum):
    NORMAL = "Normal"
    SUPER = "Super Mystery"
    TOTAL = "Total Mystery"

class GeneratorOptionNames(StrEnum):
    GOAL = "Goal"
    GOALREMAINS = "Required Remains"
    GOALFAIRYSET = "Fairy Set Size"
    STARTGEAR = "Starting Basic Gear Choice"
    SONGLAYOUT = "Song Layout Choice"
    FREEDUNGEONSONG = "Free Dungeon Song"
    FREEEPONA = "Free Epona's Song"
    RANDOMITEM = "Starting Item Choice"
    FDANYWHERE = "FD Anywhere Choice"
    ERINTERIOR = "Simple Interiors ER Choice"
    ERGROTTO = "Grottos ER Choice"
    ERDUNGEON = "Dungeon ER Choice"
    SMALLKEYS = "Small Keys Choice"
    COWGROTTOFIX = "Junk Shuffled Cow Grottos"
    DENSITYMODE = "Density Mode"
    CATEGORYMINIMUM = "Category Minimum"
    EXCLUDECHECKS = "Exclude Checks"

class CategoryNames(StrEnum):
    BASELINE = "Base"
    SONGLAYOUT = "Song Layout"
    STARTINGITEM = "Starting Item"
    STARTINGITEMPLURAL = "Starting Items"
    STARTINGSONG = "Starting Song"
    FREEDUNGEONSONG = "Extra Dungeon Song"
    STARTINGGEAR = "Starting Basic Gear"
    FDANYWHERE = "Fierce Deity's Mask Anywhere"
    ERINTERIOR = "Entrances: Simple Interiors"
    ERGROTTO = "Entrances: Grottos"
    ERDUNGEON = "Entrances: Dungeons"
    SMALLKEYS = "Small Keys"
    STRAYFAIRIES = "Extra Stray Fairies"
    SHOPCHECKS = "Shops: Checks"
    SHOPPRICES = "Shops: Prices"
    SOILS = "Soft Soils"
    COWS = "Cows"
    HITSPOTS = "Hit Spots"
    TOKENS = "Skulltula Tokens"
    CRATESANDBARRELS = "Crates and Barrels"
    KEATONGRASS = "Keaton Grass"
    PALMTREES = "Palm Trees"
    BUTTERFLYANDWELLFAIRIES = "Butterfly and Well Fairies"
    GOSSIPFAIRIES = "Regional Gossip Fairies"
    LOOSERUPEESOVERWORLD = "Loose Rupees: Overworld"
    LOOSERUPEESTEMPLES = "Loose Rupees: Temples"
    SNOWBALLS = "Snowballs"
    POTS = "Pots"
    MUNDANES = "Photos/Sales/Small Favors"
    NOTEBOOKENTRIES = "Notebook Entries"

class ShuffleNames(StrEnum):
    BASE_CHECKS = "Core checks"
    BASE_JUNKED = "Core junked"
    BASE_REMAINS = "Boss remains"
    BASE_DGFREWARDS = "Dungeon Great Fairy Rewards"
    GENERIC_OFF = "Off"
    GENERIC_SHUFFLED = "Shuffled"
    GENERIC_RANDOM = "Random"
    SL_TRADITIONAL = "Traditional"
    SL_SANITY = "Songsanity"
    SL_ALL = "Start with all songs"
    SG_STRONG = "Strong"
    SG_KOKIRI = "Kokiri"
    SG_SWORDLESS = "No sword or shield"
    SG_FRAGILE = "Fragile"
    ITEM_DEKU = "Deku Mask"
    ITEM_GORON = "Goron Mask"
    ITEM_ZORA = "Zora Mask"
    ITEM_FD = "Fierce Deity's Mask"
    ITEM_BOW = "Bow"
    ITEM_HOOK = "Hookshot"
    ITEM_BOMBS = "Bomb Bag"
    ITEM_BLAST = "Blast Mask"
    ITEM_WALLET = "Adult's Wallet"
    ITEM_BOTTLE = "Empty Bottle"
    ITEM_BUNNY = "Bunny Hood"
    ITEM_GFS = "Great Fairy's Sword"
    ITEM_NTM_BINGO = "Mask Bingo"
    ITEM_NTM_R1 = "Mask Bingo -- Row 1"
    ITEM_NTM_R2 = "Mask Bingo -- Row 2"
    ITEM_NTM_R3 = "Mask Bingo -- Row 3"
    ITEM_NTM_R4 = "Mask Bingo -- Row 4"
    ITEM_NTM_C1 = "Mask Bingo -- Column 1"
    ITEM_NTM_C2 = "Mask Bingo -- Column 2"
    ITEM_NTM_C3 = "Mask Bingo -- Column 3"
    ITEM_NTM_C4 = "Mask Bingo -- Column 4"
    ITEM_NTM_C5 = "Mask Bingo -- Column 5"
    SONG_EPONA = "Epona's Song"
    SONG_SONATA = "Sonata of Awakening"
    SONG_LULLABY = "Goron Lullaby"
    SONG_NEWWAVE = "New Wave Bossa Nova"
    SONG_ELEGY = "Elegy of Emptiness"
    SONG_HEALING = "Song of Healing"
    SONG_STORMS = "Song of Storms"
    SONG_ANYNONEPONA = "Any song but Epona"
    SONG_ANYDUNGEON = "Any dungeon song"
    SONG_ALL = "All songs"
    FD_STARTING = "Only when starting"
    FD_ON = "On"
    SM_KEYS_TEMPLES = "Shuffled within any temple"
    STRAYS_BUBBLES = "Just add bubbles"
    STRAYS_FULL = "All Stray Fairies"
    SHOP_C_THREE = "Three-item shops"
    SHOP_C_LATE = "Late shops"
    SHOP_C_FULL = "Almost all purchases"
    SHOP_P_SHUFFLE = "Shuffled prices"
    SHOP_P_RANDOM = "Random prices"
    HITS_SINGLE = "One Rupee per spot"
    TOKENS_ONE = "One Spider House"
    TOKENS_SSH = "Swamp Spider House"
    TOKENS_OSH = "Ocean Spider House"
    TOKENS_BOTH = "Both Spider Houses"
    KEATON_ODD = "Odd grasses only"
    KEATON_FULL = "All Keaton Grass"
    LOOSE_O_R = "Red overworld Rupees"
    LOOSE_O_RB = "Red and Blue overworld Rupees"
    LOOSE_O_RBG = "Red, Blue, and Green overworld Rupees"
    LOOSE_T_R = "Red temple Rupees"
    LOOSE_T_RBG = "Red, Blue, and Green temple Rupees"
    SNOW_SH = "Snowhead regions only"
    SNOW_ANY = "Any-day snowballs"
    POTS_TWED = "Temples and side dungeons"
    NOTE_MEET = "Meetings only"
    NOTE_FULL = "Almost all entries"
    FAIRY_HUNT_FULL_DUNGEON_STRAYS = "Dungeon strays"
    FAIRY_HUNT_INVERTED_STRAYS_CORE = "Dungeon strays other than the core set"
    FAIRY_HUNT_INVERTED_STRAYS_BUBBLES = "Dungeon strays other than the core set and bubbles"
    BUTTERFLYWELL_COWS = "Cow grotto butterflies"

class ItemNames(StrEnum):
    ITEM_DEKU = "Deku Mask"
    ITEM_GORON = "Goron Mask"
    ITEM_ZORA = "Zora Mask"
    ITEM_FD = "Fierce Deity's Mask"
    ITEM_BOW = "Bow"
    ITEM_HOOK = "Hookshot"
    ITEM_BOMBS = "Bomb Bag"
    ITEM_BLAST = "Blast Mask"
    ITEM_WALLET = "Adult's Wallet"
    ITEM_BOTTLE = "Empty Bottle"
    ITEM_BUNNY = "Bunny Hood"
    ITEM_GFS = "Great Fairy's Sword"
    SONG_OATH = "Oath to Order"
    SONG_EPONA = "Epona's Song"
    SONG_SONATA = "Sonata of Awakening"
    SONG_LULLABY = "Goron Lullaby"
    SONG_NEWWAVE = "New Wave Bossa Nove"
    SONG_ELEGY = "Elegy of Emptiness"
    SONG_HEALING = "Song of Healing"
    SONG_STORMS = "Song of Storms"
    SONG_ALL = "All songs"
    ITEM_GFM = "Great Fairy's Mask"
    ITEM_NOTEBOOK = "Bombers' Notebook"
    ITEM_DOUBLEDEF = "Double Defense"
    ITEM_RAZORSWORD = "Razor Sword"
    ITEM_SPINATTACK = "Spin Attack Upgrade"
    ITEM_NTM_R1 = "Non-Transformation Mask Bingo -- Row 1"
    ITEM_NTM_R2 = "Non-Transformation Mask Bingo -- Row 2"
    ITEM_NTM_R3 = "Non-Transformation Mask Bingo -- Row 3"
    ITEM_NTM_R4 = "Non-Transformation Mask Bingo -- Row 4"
    ITEM_NTM_C1 = "Non-Transformation Mask Bingo -- Column 1"
    ITEM_NTM_C2 = "Non-Transformation Mask Bingo -- Column 2"
    ITEM_NTM_C3 = "Non-Transformation Mask Bingo -- Column 3"
    ITEM_NTM_C4 = "Non-Transformation Mask Bingo -- Column 4"
    ITEM_NTM_C5 = "Non-Transformation Mask Bingo -- Column 5"

class CheckNames(StrEnum):
    BOSSBLUEWARP = "Boss Blue Warp"
    ROMANISGAME = "Romani's Game"

# generator option defaults
OPTION_DEFAULTS = {}
OPTION_DEFAULTS[GeneratorOptionNames.GOAL] = GoalNames.REMAINSONBOSSES
OPTION_DEFAULTS[GeneratorOptionNames.GOALREMAINS] = 4
OPTION_DEFAULTS[GeneratorOptionNames.GOALFAIRYSET] = 5
OPTION_DEFAULTS[GeneratorOptionNames.STARTGEAR] = ShuffleNames.SG_KOKIRI
OPTION_DEFAULTS[GeneratorOptionNames.SONGLAYOUT] = ShuffleNames.GENERIC_RANDOM
OPTION_DEFAULTS[GeneratorOptionNames.FREEDUNGEONSONG] = True
OPTION_DEFAULTS[GeneratorOptionNames.FREEEPONA] = False
OPTION_DEFAULTS[GeneratorOptionNames.RANDOMITEM] = ShuffleNames.GENERIC_RANDOM
OPTION_DEFAULTS[GeneratorOptionNames.FDANYWHERE] = ShuffleNames.FD_ON
OPTION_DEFAULTS[GeneratorOptionNames.ERINTERIOR] = ShuffleNames.GENERIC_OFF
OPTION_DEFAULTS[GeneratorOptionNames.ERGROTTO] = ShuffleNames.GENERIC_RANDOM
OPTION_DEFAULTS[GeneratorOptionNames.ERDUNGEON] = ShuffleNames.GENERIC_RANDOM
OPTION_DEFAULTS[GeneratorOptionNames.SMALLKEYS] = ShuffleNames.GENERIC_RANDOM
OPTION_DEFAULTS[GeneratorOptionNames.COWGROTTOFIX] = True
OPTION_DEFAULTS[GeneratorOptionNames.DENSITYMODE] = DensityNames.NORMAL
OPTION_DEFAULTS[GeneratorOptionNames.CATEGORYMINIMUM] = 6
OPTION_DEFAULTS[GeneratorOptionNames.EXCLUDECHECKS] = "-------------------------------------"

# item strings for main category shuffles
shuffleCheckStrings = {}

shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_CHECKS)] = "1800-------------------------40c-80b003f0-7f003800---3fffff-ffffffff-ffffffff-f0000000-7ffffdfa-7fffffff-ffffffff-ffffffff"
shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_JUNKED)] = "------------------------------3e0000----2-80800000-194f0201-8000f001"
shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_REMAINS)] = "-----f00000--------------------------------"
shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_DGFREWARDS)] = "-------------------------------------f000"

shuffleCheckStrings[(CategoryNames.SONGLAYOUT, ShuffleNames.SL_TRADITIONAL)] = "----------------------------------3f8---"

shuffleCheckStrings[(CategoryNames.STARTINGGEAR, ShuffleNames.SG_SWORDLESS)] = "------------------------------6000000-------"
shuffleCheckStrings[(CategoryNames.STARTINGGEAR, ShuffleNames.SG_FRAGILE)] = "------------------------------1e000000-------"

shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_BUBBLES)] = "--------------------------b003fe-7f363db4----------"
shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_FULL)] = "--------------------------3fffffff-fffffffe----------"
shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.FAIRY_HUNT_FULL_DUNGEON_STRAYS)] = "--------------------------3fffffff-fffffffc----------"
shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.FAIRY_HUNT_INVERTED_STRAYS_BUBBLES)] = "--------------------------3f4ffc01-80c9c248----------"
shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.FAIRY_HUNT_INVERTED_STRAYS_CORE)] = "--------------------------3f4ffc0f-80ffc7fc----------"

shuffleCheckStrings[(CategoryNames.SHOPCHECKS, ShuffleNames.SHOP_C_THREE)] = "---------------------------------3ff80----"
shuffleCheckStrings[(CategoryNames.SHOPCHECKS, ShuffleNames.SHOP_C_LATE)] = "-------------------------3--------3f000----"
shuffleCheckStrings[(CategoryNames.SHOPCHECKS, ShuffleNames.SHOP_C_FULL)] = "-------------------------b03--------3ffff-80000000---"

shuffleCheckStrings[(CategoryNames.SOILS, ShuffleNames.GENERIC_SHUFFLED)] = "-----------7ff-f0000000-------------------------"

shuffleCheckStrings[(CategoryNames.COWS, ShuffleNames.GENERIC_SHUFFLED)] = "-----------------------------1f-e0000000-------"

shuffleCheckStrings[(CategoryNames.HITSPOTS, ShuffleNames.HITS_SINGLE)] = "-------924924-92492492-49240000---8000000-------------------------"

shuffleCheckStrings[(CategoryNames.TOKENS, ShuffleNames.TOKENS_SSH)] = "----------------------------7-ffffffe0--------"
shuffleCheckStrings[(CategoryNames.TOKENS, ShuffleNames.TOKENS_OSH)] = "---------------------------1-fffffff8---------"
shuffleCheckStrings[(CategoryNames.TOKENS, ShuffleNames.TOKENS_BOTH)] = "---------------------------1-ffffffff-ffffffe0--------"

shuffleCheckStrings[(CategoryNames.CRATESANDBARRELS, ShuffleNames.GENERIC_SHUFFLED)] = "---10000------------c0000-2000--3c200--30--1f078-8000008-10000100-20000000------------"

shuffleCheckStrings[(CategoryNames.KEATONGRASS, ShuffleNames.KEATON_ODD)] = "-----15-5aad5400-------------------------------"
shuffleCheckStrings[(CategoryNames.KEATONGRASS, ShuffleNames.KEATON_FULL)] = "-----1f-fffffc00-------------------------------"

shuffleCheckStrings[(CategoryNames.PALMTREES, ShuffleNames.GENERIC_SHUFFLED)] = "1fe00000-------------------------------------"

shuffleCheckStrings[(CategoryNames.BUTTERFLYANDWELLFAIRIES, ShuffleNames.GENERIC_SHUFFLED)] = "1fe000-1fe00000------------------------------------"
shuffleCheckStrings[(CategoryNames.BUTTERFLYANDWELLFAIRIES, ShuffleNames.BUTTERFLYWELL_COWS)] = "-3000000------------------------------------"

shuffleCheckStrings[(CategoryNames.GOSSIPFAIRIES, ShuffleNames.GENERIC_SHUFFLED)] = "-100000-31f7400-----------------------------------"

shuffleCheckStrings[(CategoryNames.LOOSERUPEESOVERWORLD, ShuffleNames.LOOSE_O_R)] = "----------8100--3800000---1000f00----------------------"
shuffleCheckStrings[(CategoryNames.LOOSERUPEESOVERWORLD, ShuffleNames.LOOSE_O_RB)] = "---------8410-8100--3c7c10c---1000f00------40000-300183-c0003e00--------------"
shuffleCheckStrings[(CategoryNames.LOOSERUPEESOVERWORLD, ShuffleNames.LOOSE_O_RBG)] = "---------1ffff-8000fffc--3fffffc---1000f00--7-fffc2000-eff-80000000-40000-300183-c0003e00--------------"

shuffleCheckStrings[(CategoryNames.LOOSERUPEESTEMPLES, ShuffleNames.LOOSE_T_R)] = "---------------6f370f8----------------------"
shuffleCheckStrings[(CategoryNames.LOOSERUPEESTEMPLES, ShuffleNames.LOOSE_T_RBG)] = "---------------6f370f8--1e0-c00---f001fff-ff800000-3000000--------------"

shuffleCheckStrings[(CategoryNames.SNOWBALLS, ShuffleNames.SNOW_SH)] = "-----3c00--------fc0f000---------e00--c00000-------------"
shuffleCheckStrings[(CategoryNames.SNOWBALLS, ShuffleNames.SNOW_ANY)] = "-----1fc00--------fc0ff00-cf800--c0000----180c006--e00-1c0000-c0000c-------------"

shuffleCheckStrings[(CategoryNames.POTS, ShuffleNames.POTS_TWED)] = "--48-a007000----c000000------300000-3c10008-e0000000-20004000----70012001-f0f00000-60004-6-83fde03-dc000000------------"

shuffleCheckStrings[(CategoryNames.MUNDANES, ShuffleNames.GENERIC_SHUFFLED)] = "-----60000--------------------f8c070------------"

shuffleCheckStrings[(CategoryNames.NOTEBOOKENTRIES, ShuffleNames.NOTE_MEET)] = "----1fff-f6000000--------------------------------"
shuffleCheckStrings[(CategoryNames.NOTEBOOKENTRIES, ShuffleNames.NOTE_FULL)] = "---fbb-fa7dffff-f6000000--------------------------------"

# Starting item strings
startItemStrings = {}
startItemStrings[ItemNames.SONG_OATH] = "----2--"
startItemStrings[ItemNames.SONG_EPONA] = "-----8000000-"
startItemStrings[ItemNames.SONG_SONATA] = "-----20000000-"
startItemStrings[ItemNames.SONG_LULLABY] = "-----40000000-"
startItemStrings[ItemNames.SONG_NEWWAVE] = "-----80000000-"
startItemStrings[ItemNames.SONG_ELEGY] = "----1--"
startItemStrings[ItemNames.SONG_HEALING] = "-----2000000-"
startItemStrings[ItemNames.SONG_STORMS] = "-----10000000-"
startItemStrings[ItemNames.SONG_ALL] = "----3-fa000000-"
startItemStrings[ItemNames.ITEM_DEKU] = "------1"
startItemStrings[ItemNames.ITEM_GORON] = "-----200000-"
startItemStrings[ItemNames.ITEM_ZORA] = "-----400000-"
startItemStrings[ItemNames.ITEM_FD] = "----20000--"
startItemStrings[ItemNames.ITEM_BOW] = "------2"
startItemStrings[ItemNames.ITEM_HOOK] = "------400"
startItemStrings[ItemNames.ITEM_BOMBS] = "------20"
startItemStrings[ItemNames.ITEM_BLAST] = "-----8-"
startItemStrings[ItemNames.ITEM_WALLET] = "------40000000"
startItemStrings[ItemNames.ITEM_BOTTLE] = "------100000"
startItemStrings[ItemNames.ITEM_BUNNY] = "-----100-"
startItemStrings[ItemNames.ITEM_GFS] = "------8000"
startItemStrings[ItemNames.ITEM_GFM] = "-----20-"
startItemStrings[ItemNames.ITEM_NOTEBOOK] = "------400000"
startItemStrings[ItemNames.ITEM_DOUBLEDEF] = "------4000"
startItemStrings[ItemNames.ITEM_RAZORSWORD] = "----40000--800000"
startItemStrings[ItemNames.ITEM_SPINATTACK] = "------1000"
startItemStrings[ItemNames.ITEM_NTM_R1] = "-----3e-"
startItemStrings[ItemNames.ITEM_NTM_R2] = "-----7c0-"
startItemStrings[ItemNames.ITEM_NTM_R3] = "-----f800-"
startItemStrings[ItemNames.ITEM_NTM_R4] = "-----1f0000-"
startItemStrings[ItemNames.ITEM_NTM_C1] = "-----10842-"
startItemStrings[ItemNames.ITEM_NTM_C2] = "-----21084-"
startItemStrings[ItemNames.ITEM_NTM_C3] = "-----42108-"
startItemStrings[ItemNames.ITEM_NTM_C4] = "-----84210-"
startItemStrings[ItemNames.ITEM_NTM_C5] = "-----108420-"

# Shuffle-to-start-item conversion
shuffleNameToItemName = {}
shuffleNameToItemName[ShuffleNames.SONG_ALL] = ItemNames.SONG_ALL
shuffleNameToItemName[ShuffleNames.SONG_EPONA] = ItemNames.SONG_EPONA
shuffleNameToItemName[ShuffleNames.SONG_SONATA] = ItemNames.SONG_SONATA
shuffleNameToItemName[ShuffleNames.SONG_LULLABY] = ItemNames.SONG_LULLABY
shuffleNameToItemName[ShuffleNames.SONG_NEWWAVE] = ItemNames.SONG_NEWWAVE
shuffleNameToItemName[ShuffleNames.SONG_ELEGY] = ItemNames.SONG_ELEGY
shuffleNameToItemName[ShuffleNames.SONG_HEALING] = ItemNames.SONG_HEALING
shuffleNameToItemName[ShuffleNames.SONG_STORMS] = ItemNames.SONG_STORMS
shuffleNameToItemName[ShuffleNames.ITEM_DEKU] = ItemNames.ITEM_DEKU
shuffleNameToItemName[ShuffleNames.ITEM_GORON] = ItemNames.ITEM_GORON
shuffleNameToItemName[ShuffleNames.ITEM_ZORA] = ItemNames.ITEM_ZORA
shuffleNameToItemName[ShuffleNames.ITEM_FD] = ItemNames.ITEM_FD
shuffleNameToItemName[ShuffleNames.ITEM_BOW] = ItemNames.ITEM_BOW
shuffleNameToItemName[ShuffleNames.ITEM_HOOK] = ItemNames.ITEM_HOOK
shuffleNameToItemName[ShuffleNames.ITEM_BOMBS] = ItemNames.ITEM_BOMBS
shuffleNameToItemName[ShuffleNames.ITEM_BLAST] = ItemNames.ITEM_BLAST
shuffleNameToItemName[ShuffleNames.ITEM_WALLET] = ItemNames.ITEM_WALLET
shuffleNameToItemName[ShuffleNames.ITEM_BOTTLE] = ItemNames.ITEM_BOTTLE
shuffleNameToItemName[ShuffleNames.ITEM_BUNNY] = ItemNames.ITEM_BUNNY
shuffleNameToItemName[ShuffleNames.ITEM_GFS] = ItemNames.ITEM_GFS
shuffleNameToItemName[ShuffleNames.ITEM_NTM_R1] = ItemNames.ITEM_NTM_R1
shuffleNameToItemName[ShuffleNames.ITEM_NTM_R2] = ItemNames.ITEM_NTM_R2
shuffleNameToItemName[ShuffleNames.ITEM_NTM_R3] = ItemNames.ITEM_NTM_R3
shuffleNameToItemName[ShuffleNames.ITEM_NTM_R4] = ItemNames.ITEM_NTM_R4
shuffleNameToItemName[ShuffleNames.ITEM_NTM_C1] = ItemNames.ITEM_NTM_C1
shuffleNameToItemName[ShuffleNames.ITEM_NTM_C2] = ItemNames.ITEM_NTM_C2
shuffleNameToItemName[ShuffleNames.ITEM_NTM_C3] = ItemNames.ITEM_NTM_C3
shuffleNameToItemName[ShuffleNames.ITEM_NTM_C4] = ItemNames.ITEM_NTM_C4
shuffleNameToItemName[ShuffleNames.ITEM_NTM_C5] = ItemNames.ITEM_NTM_C5

# Single check strings
singleCheckStrings = {}
singleCheckStrings[CheckNames.BOSSBLUEWARP] = "----------------------------------200---"
singleCheckStrings[CheckNames.ROMANISGAME] = "----------------------------------8---" 

# Stray Fairy starting item strings for Fairy Hunt
strayFairyStartItemStrings = {}

strayFairyStartItemStrings[0] = "------"
strayFairyStartItemStrings[1] = "-20004000-80010000----"
strayFairyStartItemStrings[2] = "-6000c001-80030000----"
strayFairyStartItemStrings[3] = "-e001c003-80070000----"
strayFairyStartItemStrings[4] = "1-e003c007-800f0000----"
strayFairyStartItemStrings[5] = "3-e007c00f-801f0000----"
strayFairyStartItemStrings[6] = "7-e00fc01f-803f0000----"
strayFairyStartItemStrings[7] = "f-e01fc03f-807f0000----"
strayFairyStartItemStrings[8] = "1f-e03fc07f-80ff0000----"
strayFairyStartItemStrings[9] = "3f-e07fc0ff-81ff0000----"
strayFairyStartItemStrings[10] = "7f-e0ffc1ff-83ff0000----"
strayFairyStartItemStrings[11] = "ff-e1ffc3ff-87ff0000----"
strayFairyStartItemStrings[12] = "1ff-e3ffc7ff-8fff0000----"
strayFairyStartItemStrings[13] = "3ff-e7ffcfff-9fff0000----"
strayFairyStartItemStrings[14] = "7ff-efffdfff-bfff0000----"
strayFairyStartItemStrings[15] = "fff-ffffffff-ffff0000----"

# category weights
categoryWeights = {}
categoryWeights[DensityNames.NORMAL] = {}
categoryWeights[DensityNames.NORMAL][CategoryNames.SONGLAYOUT] = {ShuffleNames.SL_TRADITIONAL: 65,
                                                                  ShuffleNames.SL_SANITY: 35}
categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGITEM] = {ShuffleNames.ITEM_DEKU: 10,
                                                                    ShuffleNames.ITEM_GORON: 10,
                                                                    ShuffleNames.ITEM_ZORA: 10,
                                                                    ShuffleNames.ITEM_FD: 10,
                                                                    ShuffleNames.ITEM_BOW: 10,
                                                                    ShuffleNames.ITEM_HOOK: 10,
                                                                    ShuffleNames.ITEM_BOMBS: 5,
                                                                    ShuffleNames.ITEM_BLAST: 0,
                                                                    ShuffleNames.ITEM_WALLET: 5,
                                                                    ShuffleNames.ITEM_BOTTLE: 5,
                                                                    ShuffleNames.ITEM_BUNNY: 0,
                                                                    ShuffleNames.ITEM_GFS: 0,
                                                                    ShuffleNames.ITEM_NTM_BINGO: 25}
categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGSONG] = {ShuffleNames.SONG_EPONA: 90,
                                                                    ShuffleNames.SONG_ANYNONEPONA: 10}
categoryWeights[DensityNames.NORMAL][CategoryNames.FREEDUNGEONSONG] = {ShuffleNames.SONG_ANYDUNGEON: 0}
categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGGEAR] = {ShuffleNames.SG_STRONG: 0,
                                                                    ShuffleNames.SG_KOKIRI: 100,
                                                                    ShuffleNames.SG_SWORDLESS: 0,
                                                                    ShuffleNames.SG_FRAGILE: 0}
categoryWeights[DensityNames.NORMAL][CategoryNames.FDANYWHERE] = {ShuffleNames.FD_ON: 100}
categoryWeights[DensityNames.NORMAL][CategoryNames.ERINTERIOR] = {ShuffleNames.GENERIC_SHUFFLED: 0}
categoryWeights[DensityNames.NORMAL][CategoryNames.ERGROTTO] = {ShuffleNames.GENERIC_SHUFFLED: 60}
categoryWeights[DensityNames.NORMAL][CategoryNames.ERDUNGEON] = {ShuffleNames.GENERIC_SHUFFLED: 60}
categoryWeights[DensityNames.NORMAL][CategoryNames.SMALLKEYS] = {ShuffleNames.SM_KEYS_TEMPLES: 35}
categoryWeights[DensityNames.NORMAL][CategoryNames.STRAYFAIRIES] = {ShuffleNames.STRAYS_FULL: 40}
categoryWeights[DensityNames.NORMAL][CategoryNames.SHOPCHECKS] = {ShuffleNames.SHOP_C_LATE: 30,
                                                                  ShuffleNames.SHOP_C_FULL: 25}
categoryWeights[DensityNames.NORMAL][CategoryNames.SHOPPRICES] = {ShuffleNames.SHOP_P_SHUFFLE: 20,
                                                                  ShuffleNames.SHOP_P_RANDOM: 20}
categoryWeights[DensityNames.NORMAL][CategoryNames.SOILS] = {ShuffleNames.GENERIC_SHUFFLED: 35}
categoryWeights[DensityNames.NORMAL][CategoryNames.COWS] = {ShuffleNames.GENERIC_SHUFFLED: 45}
categoryWeights[DensityNames.NORMAL][CategoryNames.HITSPOTS] = {ShuffleNames.HITS_SINGLE: 40}
categoryWeights[DensityNames.NORMAL][CategoryNames.TOKENS] = {ShuffleNames.TOKENS_ONE: 30,
                                                              ShuffleNames.TOKENS_BOTH: 5}
categoryWeights[DensityNames.NORMAL][CategoryNames.CRATESANDBARRELS] = {ShuffleNames.GENERIC_SHUFFLED: 45}
categoryWeights[DensityNames.NORMAL][CategoryNames.KEATONGRASS] = {ShuffleNames.KEATON_ODD: 30,
                                                                   ShuffleNames.KEATON_FULL: 5}
categoryWeights[DensityNames.NORMAL][CategoryNames.PALMTREES] = {ShuffleNames.GENERIC_SHUFFLED: 60}
categoryWeights[DensityNames.NORMAL][CategoryNames.BUTTERFLYANDWELLFAIRIES] = {ShuffleNames.GENERIC_SHUFFLED: 40}
categoryWeights[DensityNames.NORMAL][CategoryNames.GOSSIPFAIRIES] = {ShuffleNames.GENERIC_SHUFFLED: 45}
categoryWeights[DensityNames.NORMAL][CategoryNames.LOOSERUPEESOVERWORLD] = {ShuffleNames.LOOSE_O_R: 15,
                                                                            ShuffleNames.LOOSE_O_RB: 20,
                                                                            ShuffleNames.LOOSE_O_RBG: 15}
categoryWeights[DensityNames.NORMAL][CategoryNames.LOOSERUPEESTEMPLES] = {ShuffleNames.LOOSE_T_R: 40,
                                                                          ShuffleNames.LOOSE_T_RBG: 25}
categoryWeights[DensityNames.NORMAL][CategoryNames.SNOWBALLS] = {ShuffleNames.SNOW_SH: 20,
                                                                 ShuffleNames.SNOW_ANY: 15}
categoryWeights[DensityNames.NORMAL][CategoryNames.POTS] = {ShuffleNames.POTS_TWED: 35}
categoryWeights[DensityNames.NORMAL][CategoryNames.MUNDANES] = {ShuffleNames.GENERIC_SHUFFLED: 35}
categoryWeights[DensityNames.NORMAL][CategoryNames.NOTEBOOKENTRIES] = {ShuffleNames.NOTE_MEET: 15,
                                                                       ShuffleNames.NOTE_FULL: 15}

categoryWeights[DensityNames.SUPER] = {}
categoryWeights[DensityNames.SUPER][CategoryNames.SONGLAYOUT] = categoryWeights[DensityNames.NORMAL][CategoryNames.SONGLAYOUT]
categoryWeights[DensityNames.SUPER][CategoryNames.STARTINGITEM] = categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGITEM]
categoryWeights[DensityNames.SUPER][CategoryNames.STARTINGSONG] = categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGSONG]
categoryWeights[DensityNames.SUPER][CategoryNames.FREEDUNGEONSONG] = categoryWeights[DensityNames.NORMAL][CategoryNames.FREEDUNGEONSONG]
categoryWeights[DensityNames.SUPER][CategoryNames.STARTINGGEAR] = categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGGEAR]
categoryWeights[DensityNames.SUPER][CategoryNames.FDANYWHERE] = categoryWeights[DensityNames.NORMAL][CategoryNames.FDANYWHERE]
categoryWeights[DensityNames.SUPER][CategoryNames.ERINTERIOR] = categoryWeights[DensityNames.NORMAL][CategoryNames.ERINTERIOR]
categoryWeights[DensityNames.SUPER][CategoryNames.ERGROTTO] = categoryWeights[DensityNames.NORMAL][CategoryNames.ERGROTTO]
categoryWeights[DensityNames.SUPER][CategoryNames.ERDUNGEON] = categoryWeights[DensityNames.NORMAL][CategoryNames.ERDUNGEON]
categoryWeights[DensityNames.SUPER][CategoryNames.SMALLKEYS] = categoryWeights[DensityNames.NORMAL][CategoryNames.SMALLKEYS]
categoryWeights[DensityNames.SUPER][CategoryNames.STRAYFAIRIES] = {ShuffleNames.STRAYS_FULL: 70}
categoryWeights[DensityNames.SUPER][CategoryNames.SHOPCHECKS] = {ShuffleNames.SHOP_C_LATE: 45,
                                                                  ShuffleNames.SHOP_C_FULL: 40}
categoryWeights[DensityNames.SUPER][CategoryNames.SHOPPRICES] = {ShuffleNames.SHOP_P_SHUFFLE: 30,
                                                                  ShuffleNames.SHOP_P_RANDOM: 25}
categoryWeights[DensityNames.SUPER][CategoryNames.SOILS] = {ShuffleNames.GENERIC_SHUFFLED: 70}
categoryWeights[DensityNames.SUPER][CategoryNames.COWS] = {ShuffleNames.GENERIC_SHUFFLED: 70}
categoryWeights[DensityNames.SUPER][CategoryNames.HITSPOTS] = {ShuffleNames.HITS_SINGLE: 70}
categoryWeights[DensityNames.SUPER][CategoryNames.TOKENS] = {ShuffleNames.TOKENS_ONE: 35,
                                                              ShuffleNames.TOKENS_BOTH: 25}
categoryWeights[DensityNames.SUPER][CategoryNames.CRATESANDBARRELS] = {ShuffleNames.GENERIC_SHUFFLED: 75}
categoryWeights[DensityNames.SUPER][CategoryNames.KEATONGRASS] = {ShuffleNames.KEATON_ODD: 35,
                                                                   ShuffleNames.KEATON_FULL: 30}
categoryWeights[DensityNames.SUPER][CategoryNames.PALMTREES] = {ShuffleNames.GENERIC_SHUFFLED: 75}
categoryWeights[DensityNames.SUPER][CategoryNames.BUTTERFLYANDWELLFAIRIES] = {ShuffleNames.GENERIC_SHUFFLED: 70}
categoryWeights[DensityNames.SUPER][CategoryNames.GOSSIPFAIRIES] = {ShuffleNames.GENERIC_SHUFFLED: 75}
categoryWeights[DensityNames.SUPER][CategoryNames.LOOSERUPEESOVERWORLD] = {ShuffleNames.LOOSE_O_R: 20,
                                                                            ShuffleNames.LOOSE_O_RB: 25,
                                                                            ShuffleNames.LOOSE_O_RBG: 35}
categoryWeights[DensityNames.SUPER][CategoryNames.LOOSERUPEESTEMPLES] = {ShuffleNames.LOOSE_T_R: 45,
                                                                          ShuffleNames.LOOSE_T_RBG: 35}
categoryWeights[DensityNames.SUPER][CategoryNames.SNOWBALLS] = {ShuffleNames.SNOW_SH: 35,
                                                                 ShuffleNames.SNOW_ANY: 25}
categoryWeights[DensityNames.SUPER][CategoryNames.POTS] = {ShuffleNames.POTS_TWED: 60}
categoryWeights[DensityNames.SUPER][CategoryNames.MUNDANES] = {ShuffleNames.GENERIC_SHUFFLED: 65}
categoryWeights[DensityNames.SUPER][CategoryNames.NOTEBOOKENTRIES] = {ShuffleNames.NOTE_MEET: 25,
                                                                       ShuffleNames.NOTE_FULL: 30}

categoryWeights[DensityNames.TOTAL] = {}
categoryWeights[DensityNames.TOTAL][CategoryNames.SONGLAYOUT] = categoryWeights[DensityNames.NORMAL][CategoryNames.SONGLAYOUT]
categoryWeights[DensityNames.TOTAL][CategoryNames.STARTINGITEM] = categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGITEM]
categoryWeights[DensityNames.TOTAL][CategoryNames.STARTINGSONG] = categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGSONG]
categoryWeights[DensityNames.TOTAL][CategoryNames.FREEDUNGEONSONG] = categoryWeights[DensityNames.NORMAL][CategoryNames.FREEDUNGEONSONG]
categoryWeights[DensityNames.TOTAL][CategoryNames.STARTINGGEAR] = categoryWeights[DensityNames.NORMAL][CategoryNames.STARTINGGEAR]
categoryWeights[DensityNames.TOTAL][CategoryNames.FDANYWHERE] = categoryWeights[DensityNames.NORMAL][CategoryNames.FDANYWHERE]
categoryWeights[DensityNames.TOTAL][CategoryNames.ERINTERIOR] = categoryWeights[DensityNames.NORMAL][CategoryNames.ERINTERIOR]
categoryWeights[DensityNames.TOTAL][CategoryNames.ERGROTTO] = categoryWeights[DensityNames.NORMAL][CategoryNames.ERGROTTO]
categoryWeights[DensityNames.TOTAL][CategoryNames.ERDUNGEON] = categoryWeights[DensityNames.NORMAL][CategoryNames.ERDUNGEON]
categoryWeights[DensityNames.TOTAL][CategoryNames.SMALLKEYS] = categoryWeights[DensityNames.NORMAL][CategoryNames.SMALLKEYS]
categoryWeights[DensityNames.TOTAL][CategoryNames.STRAYFAIRIES] = {ShuffleNames.STRAYS_FULL: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.SHOPCHECKS] = {ShuffleNames.SHOP_C_FULL: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.SHOPPRICES] = {ShuffleNames.SHOP_P_RANDOM: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.SOILS] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.COWS] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.HITSPOTS] = {ShuffleNames.HITS_SINGLE: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.TOKENS] = {ShuffleNames.TOKENS_BOTH: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.CRATESANDBARRELS] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.KEATONGRASS] = {ShuffleNames.KEATON_FULL: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.PALMTREES] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.BUTTERFLYANDWELLFAIRIES] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.GOSSIPFAIRIES] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.LOOSERUPEESOVERWORLD] = {ShuffleNames.LOOSE_O_RBG: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.LOOSERUPEESTEMPLES] = {ShuffleNames.LOOSE_T_RBG: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.SNOWBALLS] = {ShuffleNames.SNOW_ANY: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.POTS] = {ShuffleNames.POTS_TWED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.MUNDANES] = {ShuffleNames.GENERIC_SHUFFLED: 100}
categoryWeights[DensityNames.TOTAL][CategoryNames.NOTEBOOKENTRIES] = {ShuffleNames.NOTE_FULL: 100}
