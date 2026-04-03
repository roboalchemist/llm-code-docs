# ResourceImporterDynamicFont in English

# ResourceImporterDynamicFont
Inherits:ResourceImporter<RefCounted<Object
Imports a TTF, TTC, OTF, OTC, WOFF or WOFF2 font file for font rendering that adapts to any size.

## Description
Unlike bitmap fonts, dynamic fonts can be resized to any size and still look crisp. Dynamic fonts also optionally support MSDF font rendering, which allows for run-time scale changes with no re-rasterization cost.
While WOFF and especially WOFF2 tend to result in smaller file sizes, there is no universally "better" font format. In most situations, it's recommended to use the font format that was shipped on the font developer's website.
See alsoResourceImporterBMFontandResourceImporterImageFont.

## Tutorials
- Dynamic fonts - Using fonts
Dynamic fonts - Using fonts

## Properties

| bool | allow_system_fallback | true |
|---|---|---|
| int | antialiasing | 1 |
| bool | compress | true |
| bool | disable_embedded_bitmaps | true |
| Array | fallbacks | [] |
| bool | force_autohinter | false |
| bool | generate_mipmaps | false |
| int | hinting | 1 |
| bool | keep_rounding_remainders | true |
| Dictionary | language_support | {} |
| bool | modulate_color_glyphs | false |
| int | msdf_pixel_range | 8 |
| int | msdf_size | 48 |
| bool | multichannel_signed_distance_field | false |
| Dictionary | opentype_features | {} |
| float | oversampling | 0.0 |
| Array | preload | [] |
| Dictionary | script_support | {} |
| int | subpixel_positioning | 4 |

bool
allow_system_fallback
true
antialiasing
bool
compress
true
bool
disable_embedded_bitmaps
true
Array
fallbacks
bool
force_autohinter
false
bool
generate_mipmaps
false
hinting
bool
keep_rounding_remainders
true
Dictionary
language_support
bool
modulate_color_glyphs
false
msdf_pixel_range
msdf_size
bool
multichannel_signed_distance_field
false
Dictionary
opentype_features
float
oversampling
Array
preload
Dictionary
script_support
subpixel_positioning

## Property Descriptions
boolallow_system_fallback=true🔗
Iftrue, automatically use system fonts as a fallback if a glyph isn't found in this dynamic font. This makes supporting CJK characters or emoji more straightforward, as you don't need to include a CJK/emoji font in your project. See alsofallbacks.
Note:The appearance of system fonts varies across platforms. Loading system fonts is only supported on Windows, macOS, Linux, Android and iOS.
intantialiasing=1🔗
The font antialiasing method to use.
Disabled:Most suited for pixel art fonts, although you do nothaveto change the antialiasing from the defaultGrayscaleif the font file was well-created and the font is used at an integer multiple of its intended size. If pixel art fonts have a bad appearance at their intended size, try settingsubpixel_positioningtoDisabledinstead.
Grayscale:Use grayscale antialiasing. This is the approach used by the operating system on macOS, Android and iOS.
LCD Subpixel:Use antialiasing with subpixel patterns to make fonts sharper on LCD displays. This is the approach used by the operating system on Windows and most Linux distributions. The downside is that this can introduce "fringing" on edges, especially on display technologies that don't use standard RGB subpixels (such as OLED displays). The LCD subpixel layout is globally controlled byProjectSettings.gui/theme/lcd_subpixel_layout, which also allows falling back to grayscale antialiasing.
boolcompress=true🔗
Iftrue, uses lossless compression for the resulting font.
booldisable_embedded_bitmaps=true🔗
If set totrue, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).
Arrayfallbacks=[]🔗
List of font fallbacks to use if a glyph isn't found in this dynamic font. Fonts at the beginning of the array are attempted first, but fallback fonts that don't support the glyph's language and script are attempted last (seelanguage_supportandscript_support). See alsoallow_system_fallback.
boolforce_autohinter=false🔗
Iftrue, forces generation of hinting data for the font usingFreeType's autohinter. This will makehintingeffective with fonts that don't include hinting data.
boolgenerate_mipmaps=false🔗
Iftrue, this font will have mipmaps generated. This prevents text from looking grainy when aControlis scaled down, or when aLabel3Dis viewed from a long distance (ifLabel3D.texture_filteris set to a mode that displays mipmaps).
Enablinggenerate_mipmapsincreases font generation time and memory usage. Only enable this setting if you actually need it.
inthinting=1🔗
The hinting mode to use. This controls how aggressively glyph edges should be snapped to pixels when rasterizing the font. Depending on personal preference, you may prefer using one hinting mode over the other. Hinting modes other thanNoneare only effective if the font contains hinting data (seeforce_autohinter).
None:Smoothest appearance, which can make the font look blurry at small sizes.
Light:Sharp result by snapping glyph edges to pixels on the Y axis only.
Normal:Sharpest by snapping glyph edges to pixels on both X and Y axes.
boolkeep_rounding_remainders=true🔗
If set totrue, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.
Dictionarylanguage_support={}🔗
Override the list of languages supported by this font. If left empty, this is supplied by the font metadata. There is usually no need to change this. See alsoscript_support.
boolmodulate_color_glyphs=false🔗
If set totrue, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.
intmsdf_pixel_range=8🔗
The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines,msdf_pixel_rangemust be set to at leasttwicethe size of the largest font outline. The defaultmsdf_pixel_rangevalue of8allows outline sizes up to4to look correct.
intmsdf_size=48🔗
Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering. Only effective ifmultichannel_signed_distance_fieldistrue.
boolmultichannel_signed_distance_field=false🔗
If set totrue, the font will use multichannel signed distance field (MSDF) for crisp rendering at any size. Since this approach does not rely on rasterizing the font every time its size changes, this allows for resizing the font in real-time without any performance penalty. Text will also not look grainy forControls that are scaled down (or forLabel3Ds viewed from a long distance).
MSDF font rendering can be combined withgenerate_mipmapsto further improve font rendering quality when scaled down.
Dictionaryopentype_features={}🔗
The OpenType features to enable, disable or set a value for this font. This can be used to enable optional features provided by the font, such as ligatures or alternative glyphs. The list of supported OpenType features varies on a per-font basis.
floatoversampling=0.0🔗
If set to a positive value, overrides the oversampling factor of the viewport this font is used in. SeeViewport.oversampling. This value doesn't override theoversamplingparameter ofdraw_*methods.
Arraypreload=[]🔗
The glyph ranges to prerender. This can avoid stuttering during gameplay when new characters need to be rendered, especially ifsubpixel_positioningis enabled. The downside of using preloading is that initial project load times will increase, as well as memory usage.
Dictionaryscript_support={}🔗
Override the list of language scripts supported by this font. If left empty, this is supplied by the font metadata. There is usually no need to change this. See alsolanguage_support.
intsubpixel_positioning=4🔗
Subpixel positioning improves font rendering appearance, especially at smaller font sizes. The downside is that it takes more time to initially render the font, which can cause stuttering during gameplay, especially if used with large font sizes. This should be set toDisabledfor fonts with a pixel art appearance.
Disabled:No subpixel positioning. Lowest quality, fastest rendering.
Auto:Use subpixel positioning at small font sizes (the chosen quality varies depending on font size). Large fonts will not use subpixel positioning. This is a good tradeoff between performance and quality.
One Half of a Pixel:Always perform intermediate subpixel positioning regardless of font size. High quality, slow rendering.
One Quarter of a Pixel:Always perform precise subpixel positioning regardless of font size. Highest quality, slowest rendering.
Auto (Except Pixel Fonts):Disabledfor the pixel style fonts (each glyph contours contain only straight horizontal and vertical lines),Autofor the other fonts.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.