# FontVariation in English

# FontVariation

Inherits:Font<Resource<RefCounted<Object
A variation of a font with additional settings.

## Description

Provides OpenType variations, simulated bold / slant, and additional font settings like OpenType features and extra spacing.
To use simulated bold font variant:

```
var fv = FontVariation.new()
fv.base_font = load("res://BarlowCondensed-Regular.ttf")
fv.variation_embolden = 1.2
$Label.add_theme_font_override("font", fv)
$Label.add_theme_font_size_override("font_size", 64)
```

```
var fv = new FontVariation();
fv.SetBaseFont(ResourceLoader.Load<FontFile>("res://BarlowCondensed-Regular.ttf"));
fv.SetVariationEmbolden(1.2);
GetNode("Label").AddThemeFontOverride("font", fv);
GetNode("Label").AddThemeFontSizeOverride("font_size", 64);
```

To set the coordinate of multiple variation axes:

```
var fv = FontVariation.new();
var ts = TextServerManager.get_primary_interface()
fv.base_font = load("res://BarlowCondensed-Regular.ttf")
fv.variation_opentype = { ts.name_to_tag("wght"): 900, ts.name_to_tag("custom_hght"): 900 }
```

## Properties

| Font | base_font |  |
|---|---|---|
| float | baseline_offset | 0.0 |
| Dictionary | opentype_features | {} |
| int | spacing_bottom | 0 |
| int | spacing_glyph | 0 |
| int | spacing_space | 0 |
| int | spacing_top | 0 |
| float | variation_embolden | 0.0 |
| int | variation_face_index | 0 |
| Dictionary | variation_opentype | {} |
| Transform2D | variation_transform | Transform2D(1,0,0,1,0,0) |

Font
base_font
float
baseline_offset
Dictionary
opentype_features
spacing_bottom
spacing_glyph
spacing_space
spacing_top
float
variation_embolden
variation_face_index
Dictionary
variation_opentype
Transform2D
variation_transform
Transform2D(1,0,0,1,0,0)

## Methods

| void | set_spacing(spacing:SpacingType, value:int) |

void
set_spacing(spacing:SpacingType, value:int)

## Property Descriptions

Fontbase_font🔗

- voidset_base_font(value:Font)
voidset_base_font(value:Font)
- Fontget_base_font()
Fontget_base_font()
Base font used to create a variation. If not set, defaultThemefont is used.
floatbaseline_offset=0.0🔗
- voidset_baseline_offset(value:float)
voidset_baseline_offset(value:float)
- floatget_baseline_offset()
floatget_baseline_offset()
Extra baseline offset (as a fraction of font height).
Dictionaryopentype_features={}🔗
- voidset_opentype_features(value:Dictionary)
voidset_opentype_features(value:Dictionary)
- Dictionaryget_opentype_features()
Dictionaryget_opentype_features()
A set of OpenType feature tags. More info:OpenType feature tags.
intspacing_bottom=0🔗
- voidset_spacing(spacing:SpacingType, value:int)
voidset_spacing(spacing:SpacingType, value:int)
- intget_spacing()
intget_spacing()
Extra spacing at the bottom of the line in pixels.
intspacing_glyph=0🔗
- voidset_spacing(spacing:SpacingType, value:int)
voidset_spacing(spacing:SpacingType, value:int)
- intget_spacing()
intget_spacing()
Extra spacing between graphical glyphs.
intspacing_space=0🔗
- voidset_spacing(spacing:SpacingType, value:int)
voidset_spacing(spacing:SpacingType, value:int)
- intget_spacing()
intget_spacing()
Extra width of the space glyphs.
intspacing_top=0🔗
- voidset_spacing(spacing:SpacingType, value:int)
voidset_spacing(spacing:SpacingType, value:int)
- intget_spacing()
intget_spacing()
Extra spacing at the top of the line in pixels.
floatvariation_embolden=0.0🔗
- voidset_variation_embolden(value:float)
voidset_variation_embolden(value:float)
- floatget_variation_embolden()
floatget_variation_embolden()
If is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.
Note:Emboldened fonts might have self-intersecting outlines, which will prevent MSDF fonts andTextMeshfrom working correctly.
intvariation_face_index=0🔗
- voidset_variation_face_index(value:int)
voidset_variation_face_index(value:int)
- intget_variation_face_index()
intget_variation_face_index()
Active face index in the TrueType / OpenType collection file.
Dictionaryvariation_opentype={}🔗
- voidset_variation_opentype(value:Dictionary)
voidset_variation_opentype(value:Dictionary)
- Dictionaryget_variation_opentype()
Dictionaryget_variation_opentype()
Font OpenType variation coordinates. More info:OpenType variation tags.
Note:ThisDictionaryuses OpenType tags as keys. Variation axes can be identified both by tags (int, e.g.0x77678674) and names (String, e.g.wght). Some axes might be accessible by multiple names. For example,wghtrefers to the same axis asweight. Tags on the other hand are unique. To convert between names and tags, useTextServer.name_to_tag()andTextServer.tag_to_name().
Note:To get available variation axes of a font, useFont.get_supported_variation_list().
Transform2Dvariation_transform=Transform2D(1,0,0,1,0,0)🔗
- voidset_variation_transform(value:Transform2D)
voidset_variation_transform(value:Transform2D)
- Transform2Dget_variation_transform()
Transform2Dget_variation_transform()
2D transform, applied to the font outlines, can be used for slanting, flipping and rotating glyphs.
For example, to simulate italic typeface by slanting, apply the following transformTransform2D(1.0,slant,0.0,1.0,0.0,0.0).

## Method Descriptions

voidset_spacing(spacing:SpacingType, value:int)🔗
Sets the spacing forspacingtovaluein pixels (not relative to the font size).

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
