# Generator Options

## Goal Mode

This determines the seed's win condition. Only one goal can be on at a time.

Modifiers are available:

- **Direct To Credits** causes the seed to be won immediately once the goal is met without needing to defeat Majora. In **Five Fairy Hunt** this is always in effect.
- **Bosses for Early Moon** sets the number of remains to be collected to access the Moon when the Moon Oath song layout is on or a Long Goal is selected. By default, this is 1. 
  - *In Blitz, starting remains don't count toward this number*, unless **Blitz Remains Count** is also checked!
  - If four remains are required for early moon access, Moon Oath won't be a possible song layout.

### Remains on Bosses

All of these keep boss remains on bosses. The player needs all four to access the Moon and fight Majora.

By default, if the Moon Oath song layout is active, Moon access is possible with only one remains.  When Blitz is active and Moon Oath is on, the player will need one **additional** remains for Moon access beyond what they started with.

Be aware that when Blitz-junking is combined with Dungeon Entrance shuffle, post-temple junking is applied to the *new* area of Termina that the temple is in, not the *original* area. For instance, if the top of Snowhead leads to Woodfall Temple, Mountain Village will still enter springtime when Woodfall Temple is cleared--and if Odolwa's Remains were a starting item in that seed, then springtime checks would all be junked.

- **No Blitz**: Start with no remains. *The default goal.*
- **Blitz 1**: Start with one remains, junking its temple and post-temple checks.
- **Blitz 2**: Start with two remains, junking their temple and post-temple checks.
- **Blitz 0 or 1**: Randomly use either No Blitz (85%) or Blitz 1 (15%).
- **Blitz 0, 1, or 2**: Randomly use one of No Blitz (65%), Blitz 1 (25%), or Blitz 2 (10%). This was used in Mystery Season 2.

### Remains Shuffle

This shuffles all four boss remains anywhere. The player needs all four to access the Moon and fight Majora.

By default, if the Moon Oath song layout is active, Moon access is possible with only one remains.

### Five Fairy Hunt

This places the boss remains on Great Fairy Rewards. The player needs any one remains to win immediately, obtaining it by turning in a full set of fairies.

Moon access is not possible in this goal.

- All Stray Fairy checks are always shuffled. Ten fairies from each set are given to the player, and the remaining five from each set are shuffled throughout the game.
- Fairy Fountains hint the regions of their fairies. Use these hints to help you find them!
- No WotHs, no foolishes. Extra backup hints take their place.
- Always start with Epona's Song, Goron Lullaby, and the Great Fairy's Mask.
- Skull Kid Song is junked. Traditional and Songsanity are the only Song Layout options available.
- Dungeon entrances are always shuffled.

### Any Three Remains

This keeps boss remains on bosses. The player needs *any three of their choice* to access the Moon and fight Majora.

By default, if the Moon Oath song layout is active, Moon access is possible with only one remains.

### Long Goals

Most of these change the requirements for fighting Majora. Only one long goal is active at once!

With a long goal active, no WotHs or foolishes are provided. Extra backup hints take their place.

By default, Moon access is possible with only one remains with *any* song layout, not just Moon Oath. Most long goals keep the boss remains on bosses.

- **Full Fairy Hunt**: Boss remains are on Great Fairy Rewards, and the player needs all four for Majora. All Stray Fairies are always shuffled anywhere. Start with Great Fairy's Mask.
- **Mask Hunt**: The player needs all 24 masks for Majora.
- **Skull Tokens**: The player needs all 60 Skulltula tokens for Majora.
- **Hearts**: The player needs all Heart Containers and Pieces of Heart for Majora.

## Setup Modes

These affect the player's starting state, plus song and dungeon structure.

"Default weights" refer to those given in the Category Weights and Hints spreadsheet.

### Song Layout

This determines the Song Layout for the seed. Song Layout is discussed in the Mystery Settings Document. This can be set to **Any**, **Any Non-Moon** (which excludes Moon Oath, giving its weight to Traditional), or a **specific song layout**. *Any* is the default.

- **Any**: The seed randomly selects a song layout per the default weights.
- **Any Non-Moon**: The seed randomly selects any song layout but Moon Oath. Default weights are used, except that Moon Oath's weight is added to Traditional's weight.
- A **specific song layout**: The seed uses the chosen layout.

This option has one modifier:

- **Moon Oath Adds All Trials** causes Moon Oath to shuffle the Deku, Goron, and Zora Trial Pieces of Heart (in addition to the Link Trial pots, chests, and PoH) when Moon Oath is active. This modifier has no effect when Moon Oath is not the seed's active song layout. Default is off.

### Starting Basic Gear

This determines what sword, shield, and hearts the player starts with, plus related items like Double Defense and Spin Attack Mastery. *Kokiri or Swordless* is the default.

- **Strong**: The player starts with Razor Sword, Hero's Shield, Spin Attack Mastery, and Double Defense.
- **Kokiri**: The player starts with Kokiri Sword and Hero's Shield.
- **Kokiri or Swordless**: The player randomly starts using either the *Kokiri* option or the *Swordless* option, per the default weights.
- **Swordless**: The player starts with no sword or shield. They are instead added to the item pool.
- **Fragile**: The player starts with no sword or shield and with only one heart. The missing starting items, including two Heart Containers, are added to the item pool.

### Starting Random Item

This determines what the player's additional starting non-song item can be. *Any* is the default.

- **Off**: The player does not get an additional starting item.
- **Any**: The player starts with any one of the possible starting items listed in the Category Weights and Hints spreadsheet.
- **Any Transformation Mask**: The player starts with Deku Mask, Goron Mask, Zora Mask, or Fierce Deity's Mask.
- **Any Non-Transformation**: The player starts with any one of the possible starting items that isn't a transformation mask.
- **Any Non-Sword**: The player starts with any one of the possible starting items that isn't the Great Fairy Sword or the Fierce Deity's Mask.

### FD Anywhere

This determines whether Fierce Deity's Mask Anywhere is in effect in the seed. *Sometimes* is the default.

- **Off and Unshuffled**: Not only is FD Anywhere never on, but the Fierce Deity's Mask is not shuffled at all!
- **Off**: FD Anywhere is never on.
- **Only When Starting**: FD Anywhere is only on when starting with the Fierce Deity's Mask.
- **Sometimes**: FD Anywhere is always on when starting with the Fierce Deity's Mask, and is sometimes on otherwise, as specified in the default weights.
- **Always**: FD Anywhere is always on. 

### Dungeon Entrances

This determines whether dungeon entrances--Woodfall Temple, Snowhead Temple, Great Bay Temple, and Inverted Stone Tower Temple--will be shuffled. *Sometimes* is the default.

- **Off**: Dungeon entrance randomization is off.
- **Sometimes**: Dungeon ER is randomly on or off, per the default weights.
- **On**: Dungeon entrance randomization is on.

This option has one modifier:

- **Maps Hint Dungeon ER** causes Dungeon ER to also shuffle the temple Map items in the overworld, enabling them to hint their temple's location when picked up. Default is off.

### Boss Keys

This determines whether and how Boss Keys are shuffled. *Off* is the default.

- **Off**: Boss Keys are off. Boss Doors are unlocked. Boss Key chests are not junked.
- **Sometimes**: Randomly use one of Off (65%), Within Their Temple (20%), or Within Any Temple (15%). This was used in Mystery Season 2.
- **Within Their Temple**: Boss Keys are shuffled anywhere within their own temple.
- **Within Any Temple**: Boss Keys are shuffled anywhere within all temples.
- **Within Their Area**: Boss Keys are shuffled anywhere within their major area of Termina. This includes both overworld and temples. Major areas start with Southern Swamp, Mountain Village, Great Bay Coast, and Ikana Canyon.
- **Anywhere**: Boss Keys are shuffled anywhere.

### Small Keys

This determines whether and how Small Keys are shuffled. *Sometimes* is the default.

- **Off**: Small Keys are off. Small Key Doors are unlocked. Small Key chests are not junked.
- **Sometimes**: Use the default weights.
- **Within Their Temple**: Small Keys are shuffled anywhere within their own temple.
- **Within Any Temple**: Small Keys are shuffled anywhere within all temples.
- **Within Their Area**: Small Keys are shuffled anywhere within their major area of Termina. This includes both overworld and temples. Major areas start with Southern Swamp, Mountain Village, Great Bay Coast, and Ikana Canyon.
- **Anywhere**: Small Keys are shuffled anywhere.

## Density Modes

These affect the frequency and contents of Mystery's categories and shuffles.

"Default weights" refer to those given in the Category Weights and Hints spreadsheet.

### Normal, Light, and Super Mystery

These determine the base weights for each category. *Normal* is the default.

The Category Weights and Hints spreadsheet has a sheet devoted to the weight differences for Light and Super Mystery.

Mystery Maker does not automatically adjust the category minimum for Light or Super Mystery.

- **Normal** uses default weights.
- **Light Mystery** uses decreased weights and excludes certain more difficult shuffles.
- **Super Mystery** uses increased weights and adds exclusive shuffles.

### Category Minimum

This determines how many main categories must be active in the seed. Mystery Maker will reroll until the category minimum is met. *7* is the default.

See the Mystery Settings Document for an overview of the 17 main categories.

### No Clock Town

This causes all non-scoop checks in all Clock Town regions, including those affected by Mystery categories, to be junked or unshuffled. This is *off* by default.

Specifically, when No Clock Town is active:
- Every non-scoop check located fully or partially in a Clock Town region is junked or unshuffled. This includes Tingle, Keaton Quiz, and the Observatory pots. It does *not* include Termina Field checks connected to the Telescope.
- Default Clock Town checks with useful unique items, Pieces of Heart, Purple Rupees, and Silver Rupees are shuffled and junked. All other default Clock Town checks are unshuffled. *(Unique items are not useful if they only lock Clock Town checks.)*
- The Frog in the Laundry Pool is shuffled and junked only if Frog Choir is active. Otherwise, it is unshuffled. All other possible Mystery Clock Town checks are always unshuffled, even if their categories are active. 
- The Notebook Entries category is disabled entirely.
- Because Skull Kid Song is always junked, Epona's Song is given as an *additional* starting song. When the song layout is Baby Zoras or Moon Oath, Boss Blue Warp is junked also.
- The player may still need to purchase a Powder Keg or Red Potion, set up the Scarecrow's Song, or access The Moon. *(The Moon is not in Clock Town. Preventing that is the goal of the game, after all!)*

### No Post-Temple

This causes all post-temple checks, including those affected by Mystery categories, to be junked or unshuffled. This is *off* by default.

This does keep the Deku Princess from being shuffled (overriding Scoopsanity's Shuffles Princess modifier), but does not affect other scoops.

### Overworld Pots

This determines how overworld pots are shuffled, as described in the Mystery Settings Document. *Sometimes* is the default.

- **Off**: Overworld pots are not shuffled.
- **Sometimes**: Use the default weights.
- A **specific group**: Shuffle the chosen group or number of groups.

### Scoopsanity

This determines how scoops are shuffled, as described in the Mystery Settings Document. *Sometimes* is the default.

- **Off**: Scoops are not shuffled.
- **Sometimes**: Use the default weights.
- **On**: Scoops are shuffled.

This option has two modifiers:

- **Always Scrambles Eggs** allows Scoopsanity to shuffle Zora Eggs even when Baby Zoras is active. (Normally, Baby Zoras prevents eggs from being shuffled.) Default is off.
- **Shuffles Princess** adds the Deku Princess to the Scoopsanity shuffle. Default is off.

### No Frog Choir

This prevents the Frogs category from enabling the Frog Choir check when active. *On* is the default.

Whenever Frog Choir is active in a seed, it will replace Ranch Defense in the always hint list and all Ranch Defense checks will be junked.

### Never Shuffle Seahorse

This prevents the Photos, Sales, and Small Favors category from shuffling the Seahorse on the Fisherman Pictograph check. *Off* is the default.

## Extra Modes

These affect logic and other MMR features not covered by the other tabs.

### No Iceless FD Logic

This removes Ice Arrow-related FD tricks from the trick list, returning the Ice Arrows to their usual logical role. *Off* is the default.

Tricks removed by this option:
- **GBT Red Pump as FD**
- **GBT Boss Door as FD**
- **Ikana Canyon Iceless as FD**
- **GBT Map Chest Room Jumps as FD**

### No Milk Road FD Logic

This removes Milk Road-related FD tricks from the trick list which are illegal in most racing rulesets. *Off* is the default.

Tricks removed by this option:
- **FD Jump into Ranch**
- **Ranch Tingle as FD**

### Importance Count

This causes WotH hints to become Importance Count hints instead. *Off* is the default.

### Enable Sun's Song

This allows use of the Sun's Song from Ocarina of Time *(C-Right, C-Down, C-Up, C-Right, C-Down, C-Up)* to quickly advance the Termina clock. *Off* is the default.

When enabled, Sun's Song is available for free from the start of the seed. *(Similar to the Inverted Song of Time and Double Song of Time, the Sun's Song is not an item.)*