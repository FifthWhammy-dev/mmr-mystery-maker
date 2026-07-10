# Generator Options

## Goal

This tab contains options that alter the seed's win condition. Only one goal can be on at a time.

The **Required Remains** spinbox applies to all win conditions and specifies how many remains are needed for access to the Moon and Majora.

### Remains on Bosses

Remains are vanilla. The default win condition.

### Remains Shuffle

This shuffles all four boss remains anywhere. The player needs all four to access the Moon and fight Majora.

Tatl will hint the regions of the boss remains at the Clock Tower door (press C-Up).

### Fairy Hunt

This places the boss remains on Great Fairy Rewards and scatters the dungeon Stray Fairies throughout Termina. Turn in a full set of fairies to get a remains!

Fairy Fountains hint the regions of their fairies. Additionally, you start with the Great Fairy Mask, which will shimmer when near a check containing a fairy.

The **Set Size** spinbox determines how many fairies of each color get shuffled throughout Termina. The remainder are added to the starting inventory.

In this win condition, all dungeon Stray Fairies are shuffled, but the non-core Stray Fairies (i.e. everything beyond the chest fairies in WFT/SHT/GBT/ISTT) are not automatically put into play; they become junked by default. The Extra Stray Fairies category can unjunk these fairies, just as it would add them to the pool in non-Fairy Hunt seeds.

## Setup

This tab affects the player's starting state and allows specifying the possible results of all setup categories.

### Song Layout

This determines the Song Layout for the seed. Song Layout is discussed in the Mystery Settings Document. This can be set to **Random**, **Traditional**, **Songsanity**, or **Start with all songs**, the last of which is exclusively available as a generator option. True to its name, it grants all songs and unshuffles all song checks.

Toggles for **Free Dungeon Song** and **Free Epona** are also available. Free Dungeon Song junks Boss Blue Warp and grants a random dungeon song; Free Epona unshuffles Romani's Game respectively and grants Epona's song. This is in addition to the starting random song, which will not duplicate any bonus song granted this way. These toggles have no effect if **Start with all songs** is being used.

### Starting Basic Gear

This determines what sword, shield, and hearts the player starts with, plus related items like Double Defense and Spin Attack Mastery. *Kokiri* is the default.

- **Strong**: The player starts with Razor Sword, Hero's Shield, Spin Attack Mastery, and Double Defense.
- **Kokiri**: The player starts with Kokiri Sword and Hero's Shield.
- **No sword or shield**: The player starts with no sword or shield. They are instead added to the item pool.
- **Fragile**: The player starts with no sword or shield and with only one heart. The missing starting items, including two Heart Containers, are added to the item pool.

### Starting Random Item

This determines what the player's additional starting non-song item(s) can be. This can be set to **Random**, **Off**, or any of the possible items from this setup category, including all possible **Mask Bingo** options and retired items from previous Mystery releases.

### FD Anywhere

This determines whether Fierce Deity's Mask Anywhere is in effect in the seed. **On** is the default.

- **Off**: FD Anywhere is never on.
- **Only When Starting**: FD Anywhere is only on when starting with the Fierce Deity's Mask.
- **On**: FD Anywhere is always on. 

### Entrance Randomization and Small Keys

These determine how each of Simple Interiors ER, Grotto ER, Dungeon ER, or Small Keys can be used in the seed. Options are **Off**, **Random**, and **Shuffled**, but Simple Interiors uses only Off or Shuffled and Small Keys uses **Shuffled within any temple** instead of Shuffled.

- **Off**: This category is guaranteed to be off.
- **Random**: This category is randomly off or active, per the default weights.
- **Shuffled**: This category is guaranteed to be active.

**Disable Shuffled Cow Grottos** is on by default in order to avoid problems with Twin Islands Ice cow grottos. This toggle disables the Cows category and junks cow grotto butterfly fairies when Grotto ER is on (but makes Cows more likely when Grotto ER is off).

## Checks 

This tab contains options that affect Mystery's main categories.

### Normal, Super, and Total Mystery

These determine the base weights for each category. *Normal* is the default.

In Version 6, these density modes only impact main categories; they no longer add exclusive shuffles or alter setup categories.

- **Normal** uses default weights for main categories.
- **Super Mystery** uses significantly increased weights for main categories! The Category Weights and Hints spreadsheet has a sheet listing Super Mystery weights.
- **Total Mystery** guarantees that *every main category will be active to its fullest extent!*

### Category Minimum

This determines how many main categories must be active in the seed. When building settings files, Mystery Maker will reroll categories as needed until the category minimum is met. *6* is the default.

See the Mystery Settings Document for an overview of the 16 main categories.

### Exclude Checks

This can remove checks from play by specifying an MMR item string. Checks in this string will be always junked if they are in the core check list and always unshuffled otherwise.