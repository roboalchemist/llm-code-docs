# CharFXTransform

# CharFXTransform
Inherits:RefCounted<Object
Controls how an individual character will be displayed in aRichTextEffect.

## Description
By setting various properties on this object, you can control how individual characters will be displayed in aRichTextEffect.

## Tutorials
- BBCode in RichTextLabel
BBCode in RichTextLabel

## Properties

| Color | color | Color(0,0,0,1) |
|---|---|---|
| float | elapsed_time | 0.0 |
| Dictionary | env | {} |
| RID | font | RID() |
| int | glyph_count | 0 |
| int | glyph_flags | 0 |
| int | glyph_index | 0 |
| Vector2 | offset | Vector2(0,0) |
| bool | outline | false |
| Vector2i | range | Vector2i(0,0) |
| int | relative_index | 0 |
| Transform2D | transform | Transform2D(1,0,0,1,0,0) |
| bool | visible | true |

Color
color
Color(0,0,0,1)
float
elapsed_time
Dictionary
font
RID()
glyph_count
glyph_flags
glyph_index
Vector2
offset
Vector2(0,0)
bool
outline
false
Vector2i
range
Vector2i(0,0)
relative_index
Transform2D
transform
Transform2D(1,0,0,1,0,0)
bool
visible
true

## Property Descriptions
Colorcolor=Color(0,0,0,1)🔗
- voidset_color(value:Color)
voidset_color(value:Color)
- Colorget_color()
Colorget_color()
The color the character will be drawn with.
floatelapsed_time=0.0🔗
- voidset_elapsed_time(value:float)
voidset_elapsed_time(value:float)
- floatget_elapsed_time()
floatget_elapsed_time()
The time elapsed since theRichTextLabelwas added to the scene tree (in seconds). Time stops when theRichTextLabelis paused (seeNode.process_mode). Resets when the text in theRichTextLabelis changed.
Note:Time still passes while theRichTextLabelis hidden.
Dictionaryenv={}🔗
- voidset_environment(value:Dictionary)
voidset_environment(value:Dictionary)
- Dictionaryget_environment()
Dictionaryget_environment()
Contains the arguments passed in the opening BBCode tag. By default, arguments are strings; if their contents match a type such asbool,intorfloat, they will be converted automatically. Color codes in the form#rrggbbor#rgbwill be converted to an opaqueColor. String arguments may not contain spaces, even if they're quoted. If present, quotes will also be present in the final string.
For example, the opening BBCode tag[examplefoo=hellobar=truebaz=42color=#ffffff]will map to the followingDictionary:
```
{"foo": "hello", "bar": true, "baz": 42, "color": Color(1, 1, 1, 1)}
```
RIDfont=RID()🔗
- voidset_font(value:RID)
voidset_font(value:RID)
- RIDget_font()
RIDget_font()
TextServerRID of the font used to render glyph, this value can be used withTextServer.font_*methods to retrieve font information.
Note:Read-only. Setting this property won't affect drawing.
intglyph_count=0🔗
- voidset_glyph_count(value:int)
voidset_glyph_count(value:int)
- intget_glyph_count()
intget_glyph_count()
Number of glyphs in the grapheme cluster. This value is set in the first glyph of a cluster.
Note:Read-only. Setting this property won't affect drawing.
intglyph_flags=0🔗
- voidset_glyph_flags(value:int)
voidset_glyph_flags(value:int)
- intget_glyph_flags()
intget_glyph_flags()
Glyph flags. SeeGraphemeFlagfor more info.
Note:Read-only. Setting this property won't affect drawing.
intglyph_index=0🔗
- voidset_glyph_index(value:int)
voidset_glyph_index(value:int)
- intget_glyph_index()
intget_glyph_index()
Glyph index specific to thefont. If you want to replace this glyph, useTextServer.font_get_glyph_index()withfontto get a new glyph index for a single character.
Vector2offset=Vector2(0,0)🔗
- voidset_offset(value:Vector2)
voidset_offset(value:Vector2)
- Vector2get_offset()
Vector2get_offset()
The position offset the character will be drawn with (in pixels).
booloutline=false🔗
- voidset_outline(value:bool)
voidset_outline(value:bool)
- boolis_outline()
boolis_outline()
Iftrue, FX transform is called for outline drawing.
Note:Read-only. Setting this property won't affect drawing.
Vector2irange=Vector2i(0,0)🔗
- voidset_range(value:Vector2i)
voidset_range(value:Vector2i)
- Vector2iget_range()
Vector2iget_range()
Absolute character range in the string, corresponding to the glyph.
Note:Read-only. Setting this property won't affect drawing.
intrelative_index=0🔗
- voidset_relative_index(value:int)
voidset_relative_index(value:int)
- intget_relative_index()
intget_relative_index()
The character offset of the glyph, relative to the currentRichTextEffectcustom block.
Note:Read-only. Setting this property won't affect drawing.
Transform2Dtransform=Transform2D(1,0,0,1,0,0)🔗
- voidset_transform(value:Transform2D)
voidset_transform(value:Transform2D)
- Transform2Dget_transform()
Transform2Dget_transform()
The current transform of the current glyph. It can be overridden (for example, by driving the position and rotation from a curve). You can also alter the existing value to apply transforms on top of other effects.
boolvisible=true🔗
- voidset_visibility(value:bool)
voidset_visibility(value:bool)
- boolis_visible()
boolis_visible()
Iftrue, the character will be drawn. Iffalse, the character will be hidden. Characters around hidden characters will reflow to take the space of hidden characters. If this is not desired, set theircolortoColor(1,1,1,0)instead.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.