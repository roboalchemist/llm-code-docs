# ResourceImporterBMFont

# ResourceImporterBMFont
Inherits:ResourceImporter<RefCounted<Object
Imports a bitmap font in the BMFont (.fnt) format.

## Description
The BMFont format is a format created by theBMFontprogram. Many BMFont-compatible programs also exist, likeBMGlyph.
Compared toResourceImporterImageFont,ResourceImporterBMFontsupports bitmap fonts with varying glyph widths/heights.
See alsoResourceImporterDynamicFont.

## Tutorials
- Bitmap fonts - Using fonts
Bitmap fonts - Using fonts

## Properties

| bool | compress | true |
|---|---|---|
| Array | fallbacks | [] |
| int | scaling_mode | 2 |

bool
compress
true
Array
fallbacks
scaling_mode

## Property Descriptions
boolcompress=true🔗
Iftrue, uses lossless compression for the resulting font.
Arrayfallbacks=[]🔗
List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.
intscaling_mode=2🔗
Font scaling mode.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.