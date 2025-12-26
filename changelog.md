This changelog, covering Mystery Maker releases from Version 5.0 onward, is Markdown-formatted for better readability. Preceding Mystery Maker releases are discussed in the plaintext changelog.txt.

# Mystery Maker release 5.1
This minor Mystery Maker release begins implementing saving and loading of the various options in the Mystery Maker program! For this release, all mode options can be saved or loaded into .yml files this way. Custom weights support for individual categories is planned for Version 6.

Additionally, this release makes core settings changes in response to Version 5 feedback and testing. Overall, Version 5.1 seeks to further increase the amount of Mystery activity in the average seed. Some of the changes are more experimental: in particular, **two Milk Road FD tricks are legal and in logic** in this release!

Version 6 is expected early next year (mid-to-late January 2026). It is slated to include custom weights support and further balance adjustments. It will be the last planned major release of the current development period. 

*This schedule is subject to change if a new version of MMR releases! Supporting new MMR features is a priority for Mystery whenever feasible.*

## Core Settings Changes

### Logic and Tricks
- **FD Jump into Ranch** and **Ranch Tingle as FD** are now ***legal and in logic***! 

These are *special exceptions* to the [MMR Tournament Ruleset Trick List](https://pastebin.com/7nJML4vA), which continues to govern Mystery racing in all *other* respects.

*In light of Iceless FD Logic in v5.0 and the continued increases to category appearance rates in v5.1, the time is right to consider FD as a song item. FD Jump into Ranch is reasonable to execute and offers an alternative to the static-hinted Keg.  Ranch Tingle as FD is a natural pairing.*

### Hints
- **Importance Count** is disabled.

*For the final portion of this testing period, I'd like to examine how seeds play without Importance Count. As we've seen, IC is not without downsides: in other settings some IC hints have proven confusing and frustrating to read by even the most dedicated students of MMR logic, and Mystery's deeper possibilities can exacerbate that difficulty. Spider Houses and the central regions have been particular offenders in Mystery testing.*

*While the decision is not final for Version 6--especially if a new MMR release arrives featuring Zoey's discussed changes to the item importance algorithm--this matter deserves a closer look.*

### Category Organization
- The active category minimum is now **7 out of 17 main categories**, increased from 6 in v5.0.

*Version 5 seeds maintained very reasonable completion times. There's room for a little more in the core settings. Some category weights are also being increased further to match.*

### Song Layout
- **Moon Oath is slightly more likely; Traditional is slightly less likely.** (Moon Oath weight 30 -> 35; Traditional weight 25 -> 20)

*As a significant new addition to Mystery--and to modern competitive MMR as a whole!--Moon Oath gets the privilege of being featured a little more often.*

### Dungeon Setup: Small Keys
- **Whenever Small Keys are shuffled, they are shuffled among all temples.** Small Keys being shuffled is overall slightly more likely.  
  - Small Keys Within Any Temple weight is increased (15 -> 40).
  - Small Keys Within Own Temple is removed from core settings (20 -> 0).

*Small Keys Within Own Temple guarantees that go-moding SHT and STT are more awkward. The Within Any Temple variant is the more interesting shuffle of the two and sticking with only that shuffle also reduces tracking and deduction complexity. Shuffling in the overworld was considered, but Small Keys is one of the few Mystery shuffles that strongly encourages dungeon play and preserving that was preferred.*

### Scoopsanity
- **The Deku Princess is no longer shuffled.**
- Active weight is increased from 30 -> 35.

*Scoopsanity as a category is one of the most criticized, in Mystery and elsewhere. The Deku Princess getting stuck in her bottle is a hassle for Mystery runners. So much so, that runners have been afraid to engage with the category at all during test seeds for fear that they would lose access to their only bottle and be forced to cycle. (As Scoopsanity is not guaranteed, savescumming before scooping is often impractical in a racing context.) And bottle space is indeed a hot commodity in the Mystery early game, thanks to soils, mundanes, and existing standard checks. Version 5's weight increases only heighten that demand.*

*Considering this, as well as the increased rate of Overworld Red Rupees (affecting two checks in Butler Race), the Deku Princess may be better off staying put.*

### Regional Gossip Fairies
- **The Gossip Fairies in Road to Southern Swamp, Path to Mountain Village, and Road to Ikana are back in this shuffle. This reverts the category to its Season 2 form.** Documentation will present this as "all Gossip Fairies in South, North, West, and East Termina, plus any regions connecting them to Termina Field."
- Active weight is increased from 40 -> 45.

*In v5.0 the RtSS, PtMV, and RtI gossip fairies were removed to align Regional Gossip Fairies with the "Central" definition used by new Potsanity (and MMR's area shuffles, incidentally, though those aren't used in Mystery itself). However, this exclusion did diminish both the category itself and those three regions, so it's being reverted here. Hopefully the explanation should alleviate any confusion about the non-perfect overlap with Central Pots.*

### Snowballs
- **Added a new shuffle option: Any-day Large Snowballs.** A total of 16 qualifying snowballs can be found in Goron Village, Path to Snowhead (winter only), and Snowhead. Weight is 15.
- Any-day Snowballs weight is increased (15 -> 20).

*Apart from Shopsanity and North Pots, the northern regions mostly lost out on Version 5's many weight increases. A boost to North's most prominent category may help it hold its own relative to Termina's other areas. As Any-day Snowballs is a large shuffle, introducing a new shuffle of a smaller subset should help the category appear more often as a whole without giving North* too *much at once. Any-day Large Snowballs seems like the most straightforward choice.*

### Potsanity
- **Oceanside Spider House Mask Room Pots 1 and 2 are now considered supply pots, like owl pots. They are no longer shuffled at all in Mystery.**

*One side effect of Mystery's extra shuffles is that the player will have to search for supplies that would have been static in other settings. Some examples include Red and Blue Potions (Shopsanity) and Milk (Cowsanity), but supply drops from pots are perhaps most numerous, so much so that owl pots get a special exemption from shuffling. In exchange, the player is expected to use those owl pots as necessary.*

*However, Ocean Spider House Chest's code input is a special case where the player can come prepared with 30 arrows, but still be especially inconvenienced by a West Pots shuffle if their brute-force attempt takes more than that. Since these are racing settings, guaranteeing the two 10-arrow refills in that room's pots limits the impact of unfortunate RNG for OSH Chest, as even the worst-case OSH Chest attempt can still be completed using 49 arrows.*

- **While still functioning similarly to Version 5, Potsanity is now divided into two separate "Overworld" and "Temple" rolls (like Loose Rupees). Temple Pots can now be shuffled at the same time as two other overworld pot groups and all pots are more likely to appear than they were in Version 5.** Details below:
  - Overworld Pots
    - Off (weight 40)
    - Central (weight 5)
    - South (weight 5)
    - North (weight 5)
    - West (weight 10)
    - East (weight 10)
    - Two of the above (weight 20) -- this picks two different groups from the five above, using their listed weights.
    - Full Potsanity (weight 5) -- all of the above, plus guaranteed Temple Pots
  - Temple Pots -- *always on in Full Potsanity*
    - Off (weight 50)
    - On (weight 50)

*This change allows the "two overworld pot groups" option to be based fully on the familiar Mystery weights system and more clearly presented in the Category Weights and Hints spreadsheet. It also significantly boosts Temple Pots and modestly boosts the overworld groups. Potsanity still counts as only one active category toward the minimum if both Overworld and Temple Pots are in play.*

### Other Main Categories
- **Soilsanity**
  - Active weight is increased from 40 -> 45.
  - Ranch Day 1 Soil is again a backup hint instead of a sometimes hint.
- **Cowsanity**
  - Active weight is increased from 40 -> 45.
- **Stray Fairies**
  - Active weight is increased from 30 -> 45.
- **Tokensanity**
  - One House weight is increased from 20 -> 25.
- **Crates and Barrels**
  - Active weight is increased from 40 -> 45.
- **Keaton Grass**
  - Odd Checks Only weight is increased from 20 -> 25.
- **Butterfly and Well Fairies**
  - Active weight is increased from 35 -> 40.
- **Frogs**
  - Active weight is increased from 20 -> 25.
- **Loose Rupees: Overworld**
  - Overworld Red, Blue, and Green weight is increased from 10 -> 15.
- **Loose Rupees: Temple**
  - Temple Red and Blue is removed (10 -> 0). Its weight is combined into Temple Red, Blue, and Green.
  - Temple Red weight is increased from 30 -> 35.
  - Temple Red, Blue, and Green weight is increased from 10 -> 25.
- **Photos, Sales, and Small Favors (aka Mundane)**
  - Active weight is increased from 35 -> 40.
- Shopsanity, Hit Spots, and Bombers' Notebook are unchanged.

*More weight boosts, to increase activity in every seed and more naturally support higher active category counts. One finding of Version 5 was that dungeons could use some additional help, so the temple-centric categories receive the biggest boosts this release.*

*Notably, with Overworld Greens going from 10 -> 15, every check in Mystery save for Baby Zoras has an effective weight of at least 15. This corresponds to appearing in roughly one in seven seeds, as opposed to Mystery S2's baseline of one in ten.*

## Generator Option Changes
- Modified the Potsanity Density Modes combobox to control **Overworld Pots**. Its "Off" and "Full Potsanity" choices will affect Temple Pots; the others will not.
- Inverted the "Never Shuffles Princess" Density Modes checkbox. It is now **Shuffles Princess**, which causes Scoopsanity to shuffle the Deku Princess. Bottle: Deku Princess will be on the backup hint list.
- New Density Modes checkbox: **No Frog Choir**. Prevents Frogs from replacing Ranch Defense with Frog Choir. (Frog Choir will stay junked.)
- New Density Modes checkbox: **No Shuffling Seahorse**. Prevents Photos, Sales, and Small Favors from shuffling the Seahorse.
- Inverted the "No Importance Count" Extra Modes checkbox. It is now **Importance Count**, which enables Importance Count.
- New Extra Modes checkbox: **No Milk Road FD Logic**. Removes FD Jump into Ranch and Ranch Tingle as FD from the trick list.

.

.

.

.

.

.

.

# Mystery Maker release 5.0
This major Mystery Maker release evolves the core Mystery settings in response to this year's Mystery Season 2 Tournament and to ongoing MMR community feedback. The goal is to present new challenges, address some sore spots in the Version 4 generator, and keep Mystery exciting, enjoyable, and accessible.

Version 5 presents new core settings to enable wider testing in advance of a potential Mystery Season 3 tournament next year. These are *not* planned to be the final Season 3 settings. Further refinements to the core settings and generator options are expected.

Mystery core settings are built from the Modern MMR settings preset's check pool. They are not directly based on the MMR Season 6 settings, though Season 6 and its preseason presets did inspire certain changes.

## Core Settings Changes

### Logic and Tricks
- Following S6's lead, the following **Lens of Truth-related tricks are enabled**:
  - Path to Snowhead Pillar Without Lens of Truth
  - Ikana Castle Invisible Platform Without Lens of Truth
- Using a custom logic file, **FD logic is revised to enable logic for Iceless Ikana** ***and*** **Iceless GBT completion using FD Anywhere**. This "Iceless FD Logic" only takes effect in seeds where FD is in possession and usable anywhere, and can allow for Ice Arrows to be logically non-required in a four-remains seed. Added tricks include:
  - GBT Red Pump as FD *(FD jumping and climbing to the red turnkey near Wart)*
  - GBT Boss Door as FD *(FD jumping to the GBT boss door without needing any green turnkeys)*
  - **[Custom trick!]** GBT Map Chest Room Jumps as FD *(FD jumping in the Map Chest room to reach the nearby red valve room, the seesaw room, and the Map Chest itself)*
  - **[Custom trick!]** Ikana Canyon Iceless as FD *(FD jumping across the river instead of freezing the Octoroks)*
- The FD tricks previously used in Mystery S2 (Straw Roof, Big Octo Skip, Path to Snowhead, Path to Snowhead Pillar, Climb Stone Tower) are all **removed from the trick list**. (Those remain race-legal to execute, of course!)

*Mystery adopts the additional lens tricks used by S6, in part due to the introduction of Importance Count.  More prominently, iceless logic for FD Anywhere--which was partially explored in Mystery Season 1!--expands FD's role in essential progression, making it more than just a coin-flip freebie: with great power comes great logical responsibility. Cutting GBT short with FD has already become fundamental to Mystery racing, and Iceless Ikana is a staple in its many forms, so the execution barrier to entry with these remains low. The FD tricks from Season 2 have been trimmed to keep the trick list focused on the Iceless FD Logic additions and cut down on awkward edge cases during play (e.g. partial SSH clears with just FD) but they're still legal and still useful. Remember that Iceless FD Logic has no effect in seeds without FD Anywhere, keeping Ice Arrow logic for upper Ikana relevant.*

### Item and Check Pool
- All **chest fairies obtained in or requiring entry to uninverted Stone Tower Temple** are no longer included in the initial Mystery check pool. (Stone Tower Updraft Fire Ring requires uninverted STT.) The All Stray Fairies category still adds these checks when active, and the chest fairies obtained in WFT, SHT, GBT, and inverted STT are still in play in non-Blitz Mystery seeds.
- **Fisherman Game is out of the check pool.** It is never shuffled or hinted in the Mystery Version 5 core settings.

*The advent of Iceless FD Logic encourages some tweaks in recognition of the improved logical access to upper Ikana and late GBT. In particular, it would have been possible for Fisherman Game to have Fire Arrows, Ice Arrows, or even the seed's first bow! Considering the detriments of playing the minigame--the impact of the repeated-slash method on ears, thumbs, and controllers, as well as the minigame's random nature--and the tight constraints on hint space, removing Fisherman Game from the pool is considered acceptable. This has the side benefit of preventing the use of a fully rotating always hint set in Mystery.*

*Furthermore, Season 2's chest fairy guarantee heavily favored Stone Tower Temple, where every stray fairy is a chest fairy. With Iceless FD Logic improving access to upper Ikana, the time is ripe to trim the appearance rate of the 10 chest fairies involving uninverted STT (which is unaffected by dungeon ER, remember!). They'll still be in play in All Stray Fairies, although that category is one of the few not to get a weight increase in Version 5.*

### Hints
- **Importance Count** is enabled.  WotH hints will become IC hints.  Mind that Mystery offers more ways for items to become important!  (And that Small Keys and scoops *never* contribute to Importance Count in the core settings.)
- **Hints** are adjusted. Notably, hint tiers have been renamed to "always", "sometimes", and "backup" to better match the terminology of other settings (and the ZSR chatbot!). Further, one gossip hint is always determined by that seed's chosen Song Layout option; see below for more info on Song Layout. For core settings, hints are laid out as follows:
  - 3 ICs and 3 Foolishes
  - Either a 4th IC, Anju and Kafei always hint, or Baby Zoras always hint (depending on the song layout)
  - 5 always hints -- base pool is Ranch Defense, Butler, Boat Archery, Goron Race, Seahorses. **When the Frogs category is active, Frog Choir will replace Ranch Defense** and all Ranch Defense checks will be junked.
  - Sometimes hints -- base pool starts with Gossip Stones and OSH Chest, but many categories will add their own (and OSH Chest won't be hinted if OSH tokens are shuffled). Formerly known as "minor always hints".
  - Backup hints -- base pool is large and intended to fill out the remaining Garos/Gossips. Formerly known as "sometimes hints".

*Importance Count has been a change of great interest throughout S6, and its reception appears to be cautiously positive. It's worth exploring for Version 5. Meanwhile, Seahorses distinguished itself as exceptionally difficult to route throughout Season 2, proving itself deserving of a full-time always hint. The sometimes hint list has also been expanded in Version 5, with OSH Chest joining in most seeds; however, there's only room for two sometimes hints on gossips unless Loose Rupees or Potsanity remove Butler or Goron Race...or if Zora Easter-style light rotation for always hints were to be introduced. Garo hints do remain available in Version 5.*

*Note that Giant's Mask is not given for free in Mystery, as opposed to S6 and SGL.*

### Category Reorganization
- **Boss Room Entrances** remains disabled, due to crash bugs when Gyorg is placed in STT.
- **Boss Keys** is fully disabled (always "Doors Open"/"Boss Keysy").
- **Starting Boss Remains** is now always set to zero in the core settings. Blitz can't occur by default in Version 5, but is still available as a generation option in Mystery Maker.
- **Songsanity** and **Long Quests** are mostly merged into the **Song Layout** category, which has four options. Songsanity itself (and its fourth IC hint) remain part of the category, retaining its weight of 35. Anju and Kafei and Baby Zoras are now included in this category, accompanying the other three song layouts. See details below. (Frog Choir is now governed by the Frogs category.)
- **Loose Rupees** is divided into two separate sets of options: one for overworld, one for temples.
- **Potsanity** is divided into six groups, sorted by general location (Central, South, North, West, East, and Temple). "Central" does include Road to Southern Swamp, Path to Mountain Village, Road to Ikana, and Ikana Graveyard in addition to the customary Clock Town, Termina Field, Milk Road, and Romani Ranch. This matches MMR's own organization of the regions for its "Keep Within Area" option. See further details below.
- **Regional Gossip Fairies** now excludes the Gossip Stones in Road to Southern Swamp, Path to Mountain Village, and Road to Ikana. This change aligns the category with both Potsanity and MMR's "Keep Within Area" shuffle option, which does not consider those regions to be eligible for regional shuffles.
- **Song Layout**, plus the "dungeon setup" categories **Dungeon Entrances** and **Small Keys**, are now considered setup categories, alongside **Starting Boss Remains**, **Starting Sword and Shield**, **Starting Random Item**, **Starting Random Song**, and **Fierce Deity's Mask Anywhere**. As in previous versions, setup categories will not count toward the active category minimum.
- The active category minimum now requires **6 out of 17 main categories** to be active in every Mystery seed. This is a change from v4.1.2 (Season 2--5 out of 21) and v4.2 (Season 2 Finals--8 out of 21). Most category weights are increased to help this occur more naturally.
- The "hard option" designation is no longer used.
- As most categories no longer affect always hints, category rolls are no longer impacted by open Gossip Stone space during generation.

*In Season 2, Boss Keys--especially its Within Any Temple option--had a tendency to drag out seeds that had most or all of their progression before dungeons.  Being forced to full clear or even revisit otherwise go-mode-able or foolish dungeons in search of four additional required items was a major source of complaint from Season 2 players. Removing the category greatly curtails those outcomes while clawing back some time and complexity to be used on the increased quantity and weight of other categories in Version 5 (an effort that the category minimum changes are a part of).*

*Thanks to competitor feedback, Blitz leaves the core Mystery settings for Version 5. As the majority of added Mystery checks are placed in the overworld, Blitz ran counter to the goal of preserving the relevance of dungeons. Blitz 2 in particular was capable of extraordinarily fast seeds that risk being insufficently substantial for a tournament racing format. The Blitz goal modes do remain available as generator options.*

### Song Layout
- Each Mystery seed now uses one of four song layouts, all of which also include a specific hint: either an always hint (and corresponding check) or an extra IC hint.
  - **Traditional** (weight 25) is mostly unchanged from Season 2. Songs are placed on Skull Kid Song, Imprisoned Monkey, Baby Goron, Romani's Game, Day 1 Grave Tablet, Ikana King, and Boss Blue Warp. New to Version 5, **Anju and Kafei** is in play and always hinted.
  - **Songsanity** (weight 35) is unchanged from Season 2. Songs can be placed on any item check, and items can be placed on any song check except the junked Skull Kid Song. A **4th IC hint** is still granted.
  - **Baby Zoras** (weight 10) junks Skull Kid Song and puts **Baby Zoras** in play, which is always hinted. New to Version 5, **Scoopsanity excludes egg scoops when Baby Zoras is on**.
  - **Moon Oath** (weight 30) junks Skull Kid Song, **grants Oath to Order** as an *additional* starting song, and _**puts The Moon into play, shuffling one Piece of Heart, two chests, and four pots from the Link Trial!**_ In this song layout, you can **access The Moon once you collect one remains**! **Anju and Kafei** is also in play and always hinted. Note that Regional Gossip Fairies does not affect The Moon's gossips, and Potsanity does not affect The Moon's pots. The other three trials offer no shuffled checks, but do have Gossip Stones with mask-specific hints.
- Song Layout does not count toward the active category minimum.

*The Moon comes to Mystery! Its trial run in the S6 Moonfall preset got skeptical reviews, which is understandable for main tournament settings. Mystery's approach to moon checks takes advantage of the possibilities offered by the Mystery format: the generator ensures that a moon visit won't be needed in the same seed as a similarly time-consuming eggs run, that Oath to Order is given for free to help players get to the moon (and prevent oath hint cutscenes from popping up), and that runners only need to search one trial for a reasonable return of seven checks. It's a tricky region to handle for a lot of reasons, and moon routing is challenging enough that it shouldn't appear too commonly, but let's give it a try; that's what Mystery is here for.*

*The Song Layout category was born from the fact that Long Quests and Songsanity didn't work well together in Season 2 due to hint space. They also counted toward the category minimum then without shuffling many actual checks, resulting in a few sparse seeds. Combining them into Song Layout and making the new category a fundamental part of seed setup helps solve those problems and leaves room for Anju and Kafei to get more of a chance. As for Baby Zoras, enforcing vanilla eggs guards against outrageously taxing egg scoop placements and advances the philosophy that Baby Zoras' interaction with PFI and PR is what makes the check interesting. One advantage of keeping eggs at 10% is that the check can be presented properly when it does appear without lengthening an excessive amount of seeds.*

### Other Setup Categories
*Unless otherwise stated, any weight increase for an active option is accompanied by an equal decrease to the "off" option. In Mystery core settings, all weights for any given set of options add up to 100.*
- **Starting Boss Remains**
  - Removed in core settings. All core settings seeds will start with zero remains and require all four to fight Majora.
- **Starting Random Song**
  - Epona's Song weight is increased from 40 -> 60.
  - Any Other Non-Oath Song weight is decreased from 60 -> 40, with all six being equally favored. (The generator implementation is changed here slightly to prevent specifying individual fractional weights.)
- **Fierce Deity's Mask Anywhere**
  - Active weight is increased from 45 -> 50.
- **Dungeon Setup: Entrances**
  - Active weight is increased from 45 -> 50.
- **Dungeon Setup: Small Keys**
  - Ice Arrow Chest is now promoted to a sometimes hint by *both* active options, not just Small Keys Within Any Temple.

*In Version 5, Epona's Song is made more likely to promote more early possibilities for progression, as even in Mystery non-Epona starts can occasionally feel constrained. Non-Epona starts will remain, however, as part of Mystery's remit is to explore possibilities that other common settings don't. It's hoped that the increased category weights and minimum will help provide more options in non-Epona.*

### Loose Rupees
- Loose Rupees is split into two related sets of options: **Overworld Loose Rupees** and **Temple Loose Rupees**. Both are rolled independently. Loose Rupees counts as one active category if either or both of Overworld Rupees and Temple Rupees are active. The "progressive Rupee value" principle (e.g. Blues or Greens can't be shuffled without Reds) still applies, but only within each set. Weights for Loose Rupees are overall increased as below:
- **Overworld Loose Rupees** - any loose rupee not in a temple
  - Off: 55 (was 70 for overworld)
  - Overworld Red: 15 (cumulative 30 -> 45 for overworld Red Rupees)
  - Overworld Red and Blue: 20 (cumulative 20 -> 30 for overworld Blue Rupees)
  - Overworld Red, Blue, and Green: 10 (no change from 10 for overworld Green Rupees)
- **Temple Loose Rupees** - includes WFT, SHT, GBT, and STT (both orientations)
  - Off: 50 (was 60 for temples)
  - Temple Red: 30 (cumulative 40 -> 50 for temple Red Rupees)
  - Temple Red and Blue: 10 (no change from 20 for temple Blue Rupees)
  - Temple Red, Blue, and Green: 10 (no change from 10 for temple Green Rupees)
- Butler is still junked when all overworld Green Rupees are shuffled. 

*One problem posed by the loss of Boss Keys and Boss Rooms: how can a sense of discovery be maintained throughout the seed? It's desirable to keep some of the mystery in Mystery unsolved until later, and borrowing from Mystery Season 1 offers something to help: splitting Loose Rupees into overworld and temple shuffles. Both shuffles separately maintain the "sliding scale" system from Season 2--no blues without reds, no greens without blues--cutting down on tracking work.*

### Potsanity
- The many, many pots of **Potsanity** are divided into six groups: Central, South, North, West, East, Temple. Central Pots includes Clock Town, Termina Field, Romani Ranch, Road to Ikana, and Ikana Graveyard. South Pots are from Southern Swamp onward, East Pots are from Ikana Canyon onward, and so on.  Each seed can shuffle no groups, one group, two groups, or very rarely all six (the fabled Full Potsanity!). Not all groups are weighted equally: Temple Pots are most likely (3x), followed by West and East Pots (2x each), then finally Central, South, and North Pots (1x each). Pots by owls are never included, and The Moon's four Link Trial pots are governed by the Moon Oath Song Layout option instead.
  - Off: 40
  - Any one group: 30
  - Any two groups: 25
  - All six groups: 5
- Potsanity's hint-related changes (junking Goron Race, unhinting Stone Tower Wizzrobe, unhinting Well Left Path Chest) are now linked to the shuffling of their specific pot groups (respectively: North Pots, Temple Pots, and East Pots).

*Potsanity was the most difficult category to learn and play in Season 2...absent in 80% of seeds, but an utter wallop in 10%. Full Potsanity comprised 158 checks in 27 different regions, and often mixed with nearby unshuffled pots. The middle 10% option, Temples and West/East Dungeons, mostly worked well, but demanded explanation ("what's a West/East Dungeon again?") These Version 5 changes allow players to encounter the category much more often in more manageable chunks, in the hope that when Full Potsanity does rear its lid, players will be better equipped to challenge it.  This does add some tracking and identification overhead, but should ideally pay off with a better appreciation and utilization of the category.*

*The decision to classify the pots in Ikana Graveyard and Road to Ikana as "Central" pots was made in part to align with how MMR defines north, south, east, and west for its Keep Within Area shuffles. Perhaps more importantly, had the pre-Ikana pots stayed in the East group, the Road to Ikana Pot (with the fairy, by the scarecrow) would have been the lowest-sphere member of East Pots in many seeds, compelling runners to bring a bow or hookshot + Scarecrow Song there early just in case the check was in play. That would've been a particularly awkward way to identify part of a category. Regional Gossip Fairies has been updated accordingly to ensure that Mystery's categories handle this consistently.*

### Other Main Categories
*Unless otherwise stated, any weight increase for an active option is accompanied by an equal decrease to the "off" option. In Mystery, all weights for any given set of options add up to 100.*
- **Shopsanity**
  - Late Shopsanity weight is increased from 20 -> 25.
  - Full Shopsanity weight is increased from 20 -> 25.
  - Random Prices weights are increased by 5 (15 -> 20 base, 20 -> 25 with Late, 25 -> 30 with Full).
- **Soilsanity**
  - Active weight is increased from 30 -> 40.
  - Now adds Ranch Day 1 Soil as a sometimes hint instead of a backup hint.
- **Cowsanity**
  - Active weight is increased from 30 -> 40.
- **Stray Fairies**
  - Still adds all Stray Fairies, including those in uninverted STT and Clock Town, when active.
  - Now adds Snowhead Ceiling Bubble as a sometimes hint.
  - No longer adds Stone Tower Death Armos and Stone Tower Updraft Fire Ring as backup hints.
- **Scoopsanity**
  - Active weight is increased from 25 -> 30.
  - No longer shuffles eggs when Baby Zoras is active.
  - Now adds Bottle: Deku Princess as a backup hint.
- **Hit Spots**
  - One Rupee Each weight is increased from 25 -> 35.
  - All Rupees Shuffled is removed from core settings (5 -> 0).
- **Tokensanity**
  - One House weight is increased from 15 -> 20.
  - Now removes Ocean Spider House Chest from the sometimes hint list when OSH Tokens are shuffled.
- **Crates and Barrels**
  - Active weight is increased from 30 -> 40.
- **Keaton Grass**
  - Unchanged.
- **Butterfly and Well Fairies**
  - Active weight is increased from 25 -> 35.
- **Regional Gossip Fairies**
  - Active weight is increased from 25 -> 40.
  - Now **excludes the Gossip Stones in Road to Southern Swamp, Path to Mountain Village, and Road to Ikana**. The 9 gossips that remain are in Southern Swamp, Swamp Spider House, Mountain Village (spring), Great Bay Coast, Zora Cape, and Ikana Canyon. This change ensures the category is consistent with both MMR's definition of "regional" (as used by Keep Within Area overworld shuffles) and Potsanity's directional groupings.
  - The Moon's gossip fairies are not included.
- **Frogs**
  - Active weight is decreased from 35 -> 20.
  - Now also shuffles Frog Choir, which **when active** will **replace Ranch Defense** in the always hint list and check pool. This causes Ranch Defense and its notebook ribbons to be junked. While Frog Choir with unshuffled frogs is no longer possible in Mystery, Frogs with Choir is actually more likely than in previous versions. 
- **Snowsanity**
  - Unchanged.
- **Photos, Sales, and Small Favors (aka Mundane)**
  - Active weight is increased from 25 -> 35.
  - No longer affects the Seahorses hint, since that check is always hinted in all Version 5 seeds.
- **Bombers' Notebook**
  - Full Notebook weight is increased from 10 -> 15.
  - Full Notebook no longer shuffles the Bombers' Hide and Seek ribbon (aka Notebook: Bombers' Notebook).
  - Full Notebook now won't shuffle the Ranch Defense ribbons when Ranch Defense is junked and replaced by Frog Choir (via the Frogs category).
  - Now adds Escaping from Sakon's Hideout as a sometimes hint instead of an always hint.

*In pursuit of the Version 5 goal of putting more Mystery in every seed, most weights are increased. Ranch Day 1 Soil and Snowhead Ceiling Bubble join the sometimes list.*

*Full Hit Spots included 73 checks, most of which landed often in lower spheres. So much density for so little work, as witnessed in two Season 2 bracket races (one of which was the quickest ever, though Blitz 2 is also to blame there!). Consequently, it leaves the core settings.*

*Frogs was weighted at a premium in Season 2. Season 2 and S6 has shown they're as awkward as they are adorable...four checks, two of which are in temples, of which one demands at least a sometimes hint in Mystery (as the lone guaranteed hard-locked Ice Arrow check, even with FD Anywhere), and you need one specific item to even get started. One lesson of Season 2 is that dungeon revisits seem to annoy players more than overworld shenanigans do, and Frogs is a proven offender in that regard. There's a case for taking Frog Choir off the board, and the check with unshuffled frogs carries a high risk of tedium...but Frogs + Choir is breathtakingly audacious enough to survive the Version 5 testing period at least. Ranch Defense being exchanged for it helps conserve hint space while blanking four of the worst checks to put a required frog on.*

*In rare cases, the Notebook: Bombers and Notebook: Bombers' Notebook entries, when shuffled and placed early, could logically lock the seed's first projectile or Deku Mask in the Hideout or Observatory (the player could open the menu and read the Bombers' Notebook to learn the 5-digit bomber code). The entries would be important or even required in such seeds. As remarkable as that interaction is, it is also very obscure and unintuitive, and could compel runners to scrutinize every shuffled notebook entry they find for Importance Count purposes. Keeping Notebook: Bombers' Notebook unshuffled practically eliminates that burden.*

*Escaping from Sakon's Hideout was the last lingering Season 2 always hint. The hint space crunch and the lack of other category-connected always hints besides Frogs + Choir generate a lot of design pressure to demote Escaping from Sakon's Hideout, and the realization that using Letter to Kafei is already highly encouraged by Full Notebook helps justify the move to sometimes. Doing the check can also get the Termina clock to midnight earlier, which is a unique bit of utility.*

## Generator Option Changes

### Goal Modes
- **No Blitz**, as the new default, is now the first radio button in its row.
- **Blitz 1 and Blitz 2 seeds require one *extra* remains for early moon access** when the Moon Oath song layout is active, preventing immediate moon access in Blitz seeds. (By default, Moon Oath in Blitz 1 sets Remains for Moon Access to 2; Moon Oath in Blitz 2 sets Remains for Moon Access to 3.) This adjustment can be disabled; see below.
- **Normal + Remains Shuffle** now chooses randomly from No Blitz, Blitz 1, or Remains Shuffle with weights 60/20/20 (previously 45/25/10/20, with Blitz 2 possible at 10).
- **Five Fairy Hunt** no longer explicitly removes Boss Keys and Boss Rooms, as that's now redundant with the new core settings. (It still always shuffles dungeon entrances.) Additionally, Five Fairy Hunt never uses the Baby Zoras or Moon Oath song layouts, giving their weights to the Traditional song layout.
- **Mask Hunt** now always uses the Moon Oath song layout.
- **Hearts** now shuffles and junks Fisherman Game. It will no longer shuffle and junk the Moon Trials' Pieces of Heart when Moon Oath already shuffles them.
- New goal mode: **Any Three Remains**. Inspired by SGL 2025, this goal mode requires only three remains to access the moon and defeat Majora.
- New spinbox: **Bosses for Early Moon**. Allows adjustment of the remains needed for moon access when Moon Oath is on. Non-Mask Hunt seeds that would cause 4 remains to be required for "early" moon access cannot roll the Moon Oath song layout, giving its weight to the Traditional song layout instead.
- New checkbox: **Blitz Remains Count** (positioned by Bosses for Early Moon). When checked, Blitz Moon Oath seeds won't require extra remains for moon access.

### Setup Modes
- Renamed from "Start Modes", as not everything here involves starting items anymore.
- New drop-down: **Song Layout**. Allows selecting a specific song layout, or an Any Non-Moon option.
- New checkbox: **Moon Oath Adds All Trials**. Causes Moon Oath to shuffle the Deku, Goron, and Zora Trial Pieces of Heart as well.
- New drop-downs: **Dungeon Entrances** and **Small Keys**. **Maps Hint Dungeon ER** moves to this tab. Small Keys gains Anywhere Within Their Area and Anywhere.
- **Boss Keys** moves to this tab. It loses the Always Active option, but gains Anywhere Within Their Area and Anywhere.

### Density Modes
- **Boss Keys** and **Maps Hint Dungeon ER** (formerly called "Map and Compass Hints") move to Setup Modes, as mentioned above.
- **Light Mystery** now only changes weights. Most weights are decreased slightly, but swordless start, Full Keaton Grass, Double Tokensanity, Full Potsanity, and Full Notebook are set to 0. Light Mystery no longer adds an extra WotH/IC, removes post-temple checks, enforces a category maximum, or makes other adjustments beyond weight changes. Suggested category minimum is 4.
- **Super Mystery** weight changes have been adjusted, remaining greatly elevated above core values. Full Hit Spots is still possible in Super Mystery. Suggested category minimum is 10.
- **No Clock Town** now shuffles and junks the Trading Post Red Potion. All song layouts are now allowed in No Clock Town seeds; when Baby Zoras or Moon Oath is the song layout, No Clock Town will junk Boss Blue Warp (as Skull Kid Song is already junked to give Epona's Song as an extra song).
- **Unscrambled Eggs for Baby Zoras** is renamed to **Always Scrambles Eggs** and inverted. Now, check the box to enable shuffling eggs when Baby Zoras is active, instead of checking the box to disable shuffling required eggs.
- New checkbox: **Never Shuffles Princess**. Prevents Scoopsanity from shuffling the Deku Princess.
- Tooltips for **No Post-Temple** and **No Clock Town** now clarify that the Moon is not post-temple or in Clock Town (after all, we are striving to prevent the latter!).

### Extra Modes
This is a new tab in Version 5.
- New checkbox: **No Iceless FD Logic**. Disables the FD Anywhere tricks allowing for iceless GBT completion and upper Ikana access.
- New checkbox: **No Importance Count**. Disables Importance Count hints, using WotH hints instead.
- New checkbox: **Enable Sun's Song**. Allows use of the Sun's Song (from Ocarina of Time) to rapidly advance the Termina clock.

## Bug fixes
- Disabled Boss Room Entrances in Super Mystery.
- Corrected the default filename for the -i command-line option.