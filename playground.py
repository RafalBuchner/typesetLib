l = """StarScriptType
AstroWaveType
NovaInkType
CosmicType
LunaGlyphType
QuasarType
SolarEdgeType
NebulaType
StellarType
LunarType
AuroraType
GalaxyType
RadiantType
SonicType
OrionType
AstroType
ChromaType
CelestiType
NebulaType
SeraphType
SolarType
StellarType
CosmosType
VelocityType
LumosType
EnigmaType
GravitType
WhisperType
NebulaType
QuirkType
ChromoType
SparkType
RadiType
HaloType
BlazeType
BlazeType
SonicType
GalaxType
QuirkType
CelestiType
NovaType
NebulType
SonicType
SpectraType
SolarType
HyperType
GravityType
OrbitType
LunarType
StarType
StellarType
AstroGlyphType
NebulaInkType
CosmicScriptType
GalaxyEdgeType
CelestialWaveType
LunarSparkType
NovaSerifType
SolarisFoundryType
VelocityType
QuasarLetterType
GravityGraffitiType
ChromaScriptType
WhirlwindType
RadiantAstraType
InterstellarType
WhisperingWeaversType
EnigmaType
SonicScriptType
OrionType
DreamlandLetterType
LuminaryType
StellarEdgeType
NebulaFlareType
NebulaGlyphType
AstroBeamType
AstralAlienType
CosmosFlameType
SolarFlareType
LunarDreamscapeType
RadiantType
StellarHaloType
NebulaEmberType
GravityGlyphType
ChromaticType
VelocityScriptType
AuroraIgnitionType
SonicType
GalaxyType
QuirkitectType
CelestiSparkType
StellarNovaType
NebulaType
EnchantType
CosmicRadianceType
SonicBlastType
SpectraType
SolarType
HypernovaType
GravityType
AstroNova Fonts
StellarEdge Type Foundry
AstroGlow Typography
CosmoSpark Foundry
CelestialFire Fonts
AstroBeam Type
NebulaFlare Foundry
GalacticIgnite Typography
StarburstType
CosmosFlame Foundry
RadiantAstra Fonts
NebulaEmber Type Foundry
CelestiSpark Typography
CosmicRadiance Foundry
AuroraIgnition Type
Stardrift Fonts
Nebuline Type
Lunaris Foundry
AlienGlow
AstroScribe
GalaxaType
CosmoInk
CelestiFont
NebulaGlyph
LunarAlien
Stellara Fonts
AstrixType
AlienScript
AstroBlaze
NovaInk
Stardust Glyphs
Celestial Whispers
Lunar Voyager Fonts
Nebula Syntax
Alien Echo Type Foundry
Interstellar Inkworks
Cosmic Calligraphy
Nebula Serenade
Astral Alien Typography
Lunar Dreamscape Fonts
Stellar Signals
Alien Transmissions
Astral Manuscripts
Galaxy Glyphs
Celestial Scribe Fonts
Silver Snail Type Foundry
Whispering Weavers
Black Francis Fonts
Melodic Mirage
Silent Shout Typography
Enigmatic Echoes
Dreamland Letterforms
Velvety Vowels
Fading Lullabies
Chromatic Serenade
Secret Soundscapes
Sublime Syntax
Ethereal Typeface Studio
Echo Chamber Fonts
Lyrical Whispers
Surfer Rosa Type Foundry
Debaser Fonts
Monkey Gone to Typeface
Doolittle Design
Where Is My Mind? Foundry
Gouge Away Type
Wave of Mutilation Fonts
Bone Machine Type Foundry
Tame Typeface
Here Comes Your Typeface
Caribou Fonts
Gigantic Glyphs
Velouria Type Foundry
Hey Type
Wave of Creation Fonts
SonicType
VelocityScript
WarpFoundry
SwiftGlyph
ExpressoFonts
JetstreamType
HyperFlow Foundry
QuickDraw Fonts
RapidInk
TurboGraphix
ZoomLetter
DynamoType
AccelerateFoundry
SwiftWave Fonts
SpeedyScript
TurboType
OhSnap Fonts
Blastwave Foundry
BlitzType
SonicScript
Explosivio
RapidGlyph
Shockwave Fonts
Velocity Foundry
OhMyType
SonicBlast
Fireworks Fonts
Hypernova Foundry
BlastZone Type
CelestialGlyphs
StellarStrike
NebulaInk
GravityGraffiti
AstralFontWorks
LunarLaunch
CosmicType
Solaris Foundry
AstroMatrix
GalaxyGlyph
OrbitType
CometLetter
NovaFont
InterstellarInk
Astraeus Type Foundry
WildGlyph Foundry
StellarType
VortexFont
ThunderInk
Whirlwind Type
Luminary Fonts
Quirkitect
RumbleType
ChromaScript
GravityGlyph
Nebula Foundry
FluxType
Mirage Fonts
SpectrumLetter
EnigmaType
EnchantedLetter
PixieScript
WhimsyType
EnigmaTales
MagicMuseFonts
MysticGlyphs
FairytaleFoundry
WonderScriptType
EnchantedInk
StorybookType""".split("\n")
l.sort()
newl = []
for n in l:

	if n.replace(" ","") not in newl:
		newl.append(n)
		print(n)
print(len(newl))
