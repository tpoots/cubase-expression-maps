# Custom User Presets and Expression Maps for VSL Synchron Duality Strings

## Why Another Set of Custom Presets?
There are already two (at least) working sets of expression maps available for Duality Strings, so why make another? 
1. The very popular Babylon Waves (Art Conductor) maps available at https://www.babylonwaves.com/ provide maps for Duality. I use their maps for a lot of libraries but in the case of something like Duality, which has a ton of articulations available, the Art Conductor maps end up placing so many articulation lanes in Cubase that I find it difficult to see what I am doing or to click accurately on the lane I want. For example, this is what the Violins 1 Ariculations looks like.
![Alt text](Screenshots/ACDualityArticulationLanes.JPG?raw=true "Title")
2. VSL itself provides Cubase Expression Maps for all of their libraries. I tried to use the Duality ones they provide, however I found that it took SECONDS of time when switching to a Duality track in Cubase 11. This seems to be caused by the very large number of Sound Slots that the VSL Duality expression maps come with (V1 has 675 Sound Slots defined). My system at least cannot handle this complexity, and waiting seconds to switch tracks was too frustrating.

## Custom Duality Expression Maps
* These custom expression maps are all Direction (vs. Attribute) expression maps. They might work for Attribute-based ones too, however I have not tried to adapt them
* They require custom User Presets as well since I have re-organized the factory presets pretty significantly in order to consolidate the cross fade, attack, release, and transition dimensions, in order to reduce the total number of unique possibilities
* I didn't remove any articulations from the default presets, just moved them around, so all the possible sounds are available with these expression maps
* Ignore Runs - I didn't think the Runs necessarily had to be in the same expression map as everything else, so I have ignored them for now.

## Naming Convention
There are two groups Articulation Groups defined in these custom expression maps:
* Group 1 has all the actual articulations (Long, Legatos, Shorts, Pizz, etc.)
* Group 2 is a multidimension selector that allows you to select either
  * Attack (Bold or Agile)
  * Release (Normal, Soft, or Very Soft)
  * Transition (Normal, Legato, Slurred, or Cut)

Only two groups are needed because no samples in Duality use more than one of these (A/R/T) dimensions at once.

The articulations in the expression maps are named in a way that they will tell you what dimensions they use, as well as what other controls can vary the sound/samples. For example: `Long (Vel XF R)` tells you that the "Long" articulation will respond to (1) Velocity, (2) XF (meaning CC 20 cross fade) and (3) "R" or Release dimension from Group 2. The following definitions are used:
* `Vel` - note velocity will affect the patch. For example with the Spicc/Stacc articulation, the velocity selects between Spicc. tight, Spiccato, and Staccato.
* `XF` - CC 20 will cross fade between samples, usually this applies to legato XFades between Espressivo -> Poco Vib. -> Molto Vib. or the Tremolo and Harmonics XFades
* `A` - Attack can be varied using the Group 2 lanes
* `R` - Release can be varied using the Group 2 lanes
* `T` - Transition can be varied using the Group 2 lanes

## Reduce The Number of Lanes
With these expression maps (combined with the user presets), the articulation selection in Cubase becomes somewhat more manageable: 
![Alt text](Screenshots/CustomDualityArticulationLanes.JPG?raw=true "Title")

## Thank Yous
There is not a chance in hell I would have undertaken creating these in the default Cubase Expression Map editor. These maps are made possible by the excellent online Expression Map editor created by Marius Kappes and available here: https://expressionmaps.soundsinabox.de/