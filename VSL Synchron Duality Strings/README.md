# Custom User Presets and Expression Maps for VSL Synchron Duality Strings (incl. Sordinos)

This is a set of expression maps and custom user presets that work together (in Cubase) to reduce the total number of articulation lanes when using Direction-style expression maps with VSL's Synchron Duality Strings. They are based on the `VelXF + Velocity` presets, which utilize CC1 for dynamics in both short and long articulations. In these presets, Velocity tends to be a dimension that controls attack, instead of dynamic layer. However, I have modified the defaults to *restore* Velocity control for the short articulations, I feel it is more intuitive to control shorts with Velocity over CC1. This means that these maps mix and match how dynamics are controlled. For staccato, spiccato, pizzicato, and detache Velocity controls the dynamics. All other articulations are controlled by CC1. I have left the Velocity-as-selection-control alone for Glissandos and Trills. I also utilize a naming convention that presents additional information along with the name of the articulation. The name convention is explained below, but the purpose is to show which controls (velocity, CC20) and which groups (Group 2 and Group 3 direction lanes) apply to which articulations.

## How to Use
Download and copy the user presets to wherever you keep your Synchron Player user presets, and they'll be available to load within your player. I have re-organized the dimension tree and changed quite a few of the Controllers used for selecting or cross fading between slots, however no pathces have been removed from the factory presets. It's all still there.

## Custom Duality Expression Maps
* Shorts (staccato, spiccato, pizzicato, and detache) use Velocity to control the dynamics
* Everything else (longs, legatos, trills, trems, glissandos, etc.) use CC1 to control the dynamics
* These custom expression maps are all Direction (vs. Attribute) expression maps. They might work for Attribute-based ones too, however I have not tried to adapt them
* They require custom User Presets as well since I have re-organized the factory presets somewhat in order to consolidate the cross fade, attack, release, and transition dimensions, in order to reduce the total number of unique possibilities
* I didn't remove any articulations from the default presets, just moved them around, so all the possible sounds are available with these expression maps
* No Runs - I didn't think the Runs necessarily had to be in the same expression map as everything else, so I have ignored them for now. When I need them, I put the Runs on a totally separate track.

## Naming Convention
There are three "Articulation Groups" defined in these custom expression maps:
* `Group 1` has all the actual articulations (Long, Legatos, Shorts, Pizz, etc.)
* `Group 2` is the `E` group, it is the "Expression" selector that applies to ONLY the Longs and Legatos (Poco vib., Molto vib., Vibrato XF, Espressivo)
* `Group 3` is a multidimension selector that allows you to select either
  * Attack (Bold or Agile)
  * Release (Normal, Soft, or Very Soft)
  * Transition (Normal, Legato, Slurred, or Cut)

Only three groups are needed because no samples in Duality use more than three of these selections simultaneously.

The articulations in the expression maps are named in a way that they will tell you what dimensions they use, as well as what other controls can vary the sound/samples. For example: `Long (Vel E R)` tells you that the "Long" articulation will change patches in responds (1) Velocity, (2) "E" (meaning you must choose an Expression from Group 2) and (3) "R" or Release dimension from Group 3. The following definitions are used:
* `Vel` - note velocity will affect the patch. For example Longs and Legatos the velocity will select the "Attack" of the note
* `E` - Expression, this applies only to Longs and Legatos and selects between Poco vib., Molto vib., Vibrato XF, and Espressivo
* `XF` - means that CC 20 will cross fade between samples, usually this applies to legato XFades between Poco Vib. -> Molto Vib. in the "Vibrato XF" patches, or the Tremolo and Harmonics XFades, or selecting the style of shorts ala staccatto or detache
* `A` - Attack can be varied using the Group 3 lanes
* `R` - Release can be varied using the Group 3 lanes
* `T` - Transition can be varied using the Group 3 lanes

## Thank Yous
There is not a chance in hell I would have undertaken creating these in the default Cubase Expression Map editor. These maps are made possible by the excellent online Expression Map editor created by Marius Kappes and available here: https://expressionmaps.soundsinabox.de/

--------------
## Appendix A: Why Another Set of Custom Presets?
There are already two (at least) working sets of expression maps available for Duality Strings, so why make another? 
1. The very popular Babylon Waves (Art Conductor) maps available at https://www.babylonwaves.com/ provide maps for Duality. I use their maps for a lot of libraries but in the case of something like Duality, which has a ton of articulations available, the Art Conductor maps end up placing so many articulation lanes in Cubase that I find it difficult to see what I am doing or to click accurately on the lane I want. If you use the drop-down selector for Attribute style maps, this is probably not a problem for you, but I like to use the Direction-style.
   
2. VSL itself provides Cubase Expression Maps for all of their libraries. I tried to use the Duality ones they provide, however I find them to be rather complex. You really have to know the library inside and out to understand which combinations make sense, and which ones are impossible. I wanted to have expression maps that made it painfully obvious what was available and which control apply to which articulations.

## Appendix B: Differences between the factory "VelXF + Velocity" presets, and these custom presets
The differences between the out-of-the-box Factory "VelXF + Velocity" presets and these custom presets are the following:
* Velocity is used to control dynamics for Shorts, CC1 for longs
* Attack is remapped to the same set of keyswitches as Transition and Release
* Tight Spiccato is added to the possible XFades for the Staccato/Spiccato combo patch
* All XFades are mapped to CC20
* CC20 selects beteen the Shorts (Tight Spiccato, Spiccato, and Staccato)
* CC20 selects between the detaches (Soft, Normal, Marcato)
* Pizzicato uses CC20 to select between Pizz, Col Legno, and Snap Pizz is added as a "top layer" to that Dim A combo
  
