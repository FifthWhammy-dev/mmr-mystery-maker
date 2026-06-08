from enum import StrEnum

class CategoryNames(StrEnum):
    BASELINE = "Base"
    SONGLAYOUT = "Song Layout"
    STARTINGITEM = "Starting Item"
    STARTINGSONG = "Starting Song"
    FDANYWHERE = "Fierce Deity's Mask Anywhere"
    ERINTERIOR = "Entrances: Simple Interiors"
    ERGROTTO = "Entrances: Grottos"
    ERDUNGEON = "Entrances: Dungeons"
    SMALLKEYS = "Small Keys"
    STRAYFAIRIES = "Stray Fairies"
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
    GENERIC_OFF = "---"
    GENERIC_SHUFFLED = "Shuffled"
    SL_TRADITIONAL = "Songs on song checks"
    SL_SANITY = "Songs anywhere"
    ITEM_DEKU = "Deku Mask"
    ITEM_GORON = "Goron Mask"
    ITEM_ZORA = "Zora Mask"
    ITEM_FD = "Fierce Deity Mask"
    ITEM_BOW = "Bow"
    ITEM_HOOK = "Hookshot"
    ITEM_BOMBS = "Bomb Bag"
    ITEM_BLAST = "Blast Mask"
    ITEM_WALLET = "Adult's Wallet"
    ITEM_BOTTLE = "Empty Bottle"
    ITEM_BUNNY = "Bunny Hood"
    ITEM_GFS = "Great Fairy's Sword"
    SONG_EPONA = "Epona's Song"
    SONG_OTHER = "Any non-Epona song but Oath"
    FD_ON = "On"
    KEYS_TEMPLES = "Shuffled within any temple"
    STRAYS_BASE = "Dungeon ER chests"
    STRAYS_BUBBLES = "Bubbles plus Dungeon ER chests"
    STRAYS_FULL = "All Stray Fairies"
    SHOP_C_THREE = "Three-Item Shops"
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
    LOOSE_O_R = "Red Overworld Rupees"
    LOOSE_O_RB = "Red and Blue Overworld Rupees"
    LOOSE_O_RBG = "Red, Blue, and Green Overworld Rupees"
    LOOSE_T_R = "Red Temple Rupees"
    LOOSE_T_RBG = "Red, Blue, and Green Temple Rupees"
    SNOW_SH = "Snowhead regions only"
    SNOW_ANY = "Any-day snowballs"
    POTS_TWED = "Temples and West/East Dungeons"
    NOTE_MEET = "Meetings only"
    NOTE_FULL = "Almost all entries"

# item strings for main category shuffles
shuffleCheckStrings = {}

shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_CHECKS)] = "1800-------------------------40c-80b003f0-7f003800---3fffff-ffffffff-ffffffff-f0000000-7ffffffa-7fffffff-ffffffff-ffffffff"
shuffleCheckStrings[(CategoryNames.BASELINE, ShuffleNames.BASE_JUNKED)] = "------------------------------3e0000----2-80c00000-194f0201-8000f001"

shuffleCheckStrings[(CategoryNames.SONGLAYOUT, ShuffleNames.SL_TRADITIONAL)] = "----------------------------------3f8---"

shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_BASE)] = "--------------------------b003f0-7f003800----------"
shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_BUBBLES)] = "--------------------------b003fe-7f363db4----------"
shuffleCheckStrings[(CategoryNames.STRAYFAIRIES, ShuffleNames.STRAYS_FULL)] = "--------------------------3fffffff-fffffffe----------"

shuffleCheckStrings[(CategoryNames.SHOPCHECKS, ShuffleNames.SHOP_C_THREE)] = "---------------------------------3ff80----"
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

shuffleCheckStrings[(CategoryNames.NOTEBOOKENTRIES, ShuffleNames.GENERIC_SHUFFLED)] = "----1fff-f6000000--------------------------------"
shuffleCheckStrings[(CategoryNames.NOTEBOOKENTRIES, ShuffleNames.GENERIC_SHUFFLED)] = "---fbb-fa7dffff-f6000000--------------------------------"

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