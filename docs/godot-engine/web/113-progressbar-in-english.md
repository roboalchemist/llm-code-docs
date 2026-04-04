# ProgressBar in English

# ProgressBar

Inherits:Range<Control<CanvasItem<Node<Object
A control used for visual representation of a percentage.

## Description

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, useTextureProgressBarinstead.

## Properties

| bool | editor_preview_indeterminate |  |
|---|---|---|
| int | fill_mode | 0 |
| bool | indeterminate | false |
| bool | show_percentage | true |

bool
editor_preview_indeterminate
fill_mode
bool
indeterminate
false
bool
show_percentage
true

## Theme Properties

| Color | font_color | Color(0.95,0.95,0.95,1) |
|---|---|---|
| Color | font_outline_color | Color(0,0,0,1) |
| int | outline_size | 0 |
| Font | font |  |
| int | font_size |  |
| StyleBox | background |  |
| StyleBox | fill |  |

Color
font_color
Color(0.95,0.95,0.95,1)
Color
font_outline_color
Color(0,0,0,1)
outline_size
Font
font
font_size
StyleBox
background
StyleBox
fill

## Enumerations

enumFillMode:🔗
FillModeFILL_BEGIN_TO_END=0
The progress bar fills from begin to end horizontally, according to the language direction. IfControl.is_layout_rtl()returnsfalse, it fills from left to right, and if it returnstrue, it fills from right to left.
FillModeFILL_END_TO_BEGIN=1
The progress bar fills from end to begin horizontally, according to the language direction. IfControl.is_layout_rtl()returnsfalse, it fills from right to left, and if it returnstrue, it fills from left to right.
FillModeFILL_TOP_TO_BOTTOM=2
The progress fills from top to bottom.
FillModeFILL_BOTTOM_TO_TOP=3
The progress fills from bottom to top.

## Property Descriptions

booleditor_preview_indeterminate🔗

- voidset_editor_preview_indeterminate(value:bool)
voidset_editor_preview_indeterminate(value:bool)
- boolis_editor_preview_indeterminate_enabled()
boolis_editor_preview_indeterminate_enabled()
Iffalse, theindeterminateanimation will be paused in the editor.
intfill_mode=0🔗
- voidset_fill_mode(value:int)
voidset_fill_mode(value:int)
- intget_fill_mode()
intget_fill_mode()
The fill direction. SeeFillModefor possible values.
boolindeterminate=false🔗
- voidset_indeterminate(value:bool)
voidset_indeterminate(value:bool)
- boolis_indeterminate()
boolis_indeterminate()
When set totrue, the progress bar indicates that something is happening with an animation, but does not show the fill percentage or value.
boolshow_percentage=true🔗
- voidset_show_percentage(value:bool)
voidset_show_percentage(value:bool)
- boolis_percentage_shown()
boolis_percentage_shown()
Iftrue, the fill percentage is displayed on the bar.

## Theme Property Descriptions

Colorfont_color=Color(0.95,0.95,0.95,1)🔗
The color of the text.
Colorfont_outline_color=Color(0,0,0,1)🔗
The tint of text outline of theProgressBar.
intoutline_size=0🔗
The size of the text outline.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
Fontfont🔗
Font used to draw the fill percentage ifshow_percentageistrue.
intfont_size🔗
Font size used to draw the fill percentage ifshow_percentageistrue.
StyleBoxbackground🔗
The style of the background.
StyleBoxfill🔗
The style of the progress (i.e. the part that fills the bar).

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
