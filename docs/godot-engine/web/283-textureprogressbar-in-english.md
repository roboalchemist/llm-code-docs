# TextureProgressBar in English

# TextureProgressBar

Inherits:Range<Control<CanvasItem<Node<Object
Texture-based progress bar. Useful for loading screens and life or stamina bars.

## Description

TextureProgressBar works likeProgressBar, but uses up to 3 textures instead of Godot'sThemeresource. It can be used to create horizontal, vertical and radial progress bars.

## Properties

| int | fill_mode | 0 |
|---|---|---|
| MouseFilter | mouse_filter | 1(overridesControl) |
| bool | nine_patch_stretch | false |
| Vector2 | radial_center_offset | Vector2(0,0) |
| float | radial_fill_degrees | 360.0 |
| float | radial_initial_angle | 0.0 |
| BitField[SizeFlags] | size_flags_vertical | 1(overridesControl) |
| float | step | 1.0(overridesRange) |
| int | stretch_margin_bottom | 0 |
| int | stretch_margin_left | 0 |
| int | stretch_margin_right | 0 |
| int | stretch_margin_top | 0 |
| Texture2D | texture_over |  |
| Texture2D | texture_progress |  |
| Vector2 | texture_progress_offset | Vector2(0,0) |
| Texture2D | texture_under |  |
| Color | tint_over | Color(1,1,1,1) |
| Color | tint_progress | Color(1,1,1,1) |
| Color | tint_under | Color(1,1,1,1) |

fill_mode
MouseFilter
mouse_filter
1(overridesControl)
bool
nine_patch_stretch
false
Vector2
radial_center_offset
Vector2(0,0)
float
radial_fill_degrees
360.0
float
radial_initial_angle
BitField[SizeFlags]
size_flags_vertical
1(overridesControl)
float
step
1.0(overridesRange)
stretch_margin_bottom
stretch_margin_left
stretch_margin_right
stretch_margin_top
Texture2D
texture_over
Texture2D
texture_progress
Vector2
texture_progress_offset
Vector2(0,0)
Texture2D
texture_under
Color
tint_over
Color(1,1,1,1)
Color
tint_progress
Color(1,1,1,1)
Color
tint_under
Color(1,1,1,1)

## Methods

| int | get_stretch_margin(margin:Side)const |
|---|---|
| void | set_stretch_margin(margin:Side, value:int) |

get_stretch_margin(margin:Side)const
void
set_stretch_margin(margin:Side, value:int)

## Enumerations

enumFillMode:🔗
FillModeFILL_LEFT_TO_RIGHT=0
Thetexture_progressfills from left to right.
FillModeFILL_RIGHT_TO_LEFT=1
Thetexture_progressfills from right to left.
FillModeFILL_TOP_TO_BOTTOM=2
Thetexture_progressfills from top to bottom.
FillModeFILL_BOTTOM_TO_TOP=3
Thetexture_progressfills from bottom to top.
FillModeFILL_CLOCKWISE=4
Turns the node into a radial bar. Thetexture_progressfills clockwise. Seeradial_center_offset,radial_initial_angleandradial_fill_degreesto control the way the bar fills up.
FillModeFILL_COUNTER_CLOCKWISE=5
Turns the node into a radial bar. Thetexture_progressfills counterclockwise. Seeradial_center_offset,radial_initial_angleandradial_fill_degreesto control the way the bar fills up.
FillModeFILL_BILINEAR_LEFT_AND_RIGHT=6
Thetexture_progressfills from the center, expanding both towards the left and the right.
FillModeFILL_BILINEAR_TOP_AND_BOTTOM=7
Thetexture_progressfills from the center, expanding both towards the top and the bottom.
FillModeFILL_CLOCKWISE_AND_COUNTER_CLOCKWISE=8
Turns the node into a radial bar. Thetexture_progressfills radially from the center, expanding both clockwise and counterclockwise. Seeradial_center_offset,radial_initial_angleandradial_fill_degreesto control the way the bar fills up.

## Property Descriptions

intfill_mode=0🔗

- voidset_fill_mode(value:int)
voidset_fill_mode(value:int)
- intget_fill_mode()
intget_fill_mode()
The fill direction. SeeFillModefor possible values.
boolnine_patch_stretch=false🔗
- voidset_nine_patch_stretch(value:bool)
voidset_nine_patch_stretch(value:bool)
- boolget_nine_patch_stretch()
boolget_nine_patch_stretch()
Iftrue, Godot treats the bar's textures like inNinePatchRect. Use thestretch_margin_*properties likestretch_margin_bottomto set up the nine patch's 3×3 grid. When using a radialfill_mode, this setting will only enable stretching fortexture_progress, whiletexture_underandtexture_overwill be treated like inNinePatchRect.
Vector2radial_center_offset=Vector2(0,0)🔗
- voidset_radial_center_offset(value:Vector2)
voidset_radial_center_offset(value:Vector2)
- Vector2get_radial_center_offset()
Vector2get_radial_center_offset()
Offsetstexture_progressiffill_modeisFILL_CLOCKWISE,FILL_COUNTER_CLOCKWISE, orFILL_CLOCKWISE_AND_COUNTER_CLOCKWISE.
Note:The effective radial center always stays within thetexture_progressbounds. If you need to move it outside the texture's bounds, modify thetexture_progressto contain additional empty space where needed.
floatradial_fill_degrees=360.0🔗
- voidset_fill_degrees(value:float)
voidset_fill_degrees(value:float)
- floatget_fill_degrees()
floatget_fill_degrees()
Upper limit for the fill oftexture_progressiffill_modeisFILL_CLOCKWISE,FILL_COUNTER_CLOCKWISE, orFILL_CLOCKWISE_AND_COUNTER_CLOCKWISE. When the node'svalueis equal to itsmax_value, the texture fills up to this angle.
SeeRange.value,Range.max_value.
floatradial_initial_angle=0.0🔗
- voidset_radial_initial_angle(value:float)
voidset_radial_initial_angle(value:float)
- floatget_radial_initial_angle()
floatget_radial_initial_angle()
Starting angle for the fill oftexture_progressiffill_modeisFILL_CLOCKWISE,FILL_COUNTER_CLOCKWISE, orFILL_CLOCKWISE_AND_COUNTER_CLOCKWISE. When the node'svalueis equal to itsmin_value, the texture doesn't show up at all. When thevalueincreases, the texture fills and tends towardsradial_fill_degrees.
Note:radial_initial_angleis wrapped between0and360degrees (inclusive).
intstretch_margin_bottom=0🔗
- voidset_stretch_margin(margin:Side, value:int)
voidset_stretch_margin(margin:Side, value:int)
- intget_stretch_margin(margin:Side)const
intget_stretch_margin(margin:Side)const
The height of the 9-patch's bottom row. A margin of 16 means the 9-slice's bottom corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders. Only effective ifnine_patch_stretchistrue.
intstretch_margin_left=0🔗
- voidset_stretch_margin(margin:Side, value:int)
voidset_stretch_margin(margin:Side, value:int)
- intget_stretch_margin(margin:Side)const
intget_stretch_margin(margin:Side)const
The width of the 9-patch's left column. Only effective ifnine_patch_stretchistrue.
intstretch_margin_right=0🔗
- voidset_stretch_margin(margin:Side, value:int)
voidset_stretch_margin(margin:Side, value:int)
- intget_stretch_margin(margin:Side)const
intget_stretch_margin(margin:Side)const
The width of the 9-patch's right column. Only effective ifnine_patch_stretchistrue.
intstretch_margin_top=0🔗
- voidset_stretch_margin(margin:Side, value:int)
voidset_stretch_margin(margin:Side, value:int)
- intget_stretch_margin(margin:Side)const
intget_stretch_margin(margin:Side)const
The height of the 9-patch's top row. Only effective ifnine_patch_stretchistrue.
Texture2Dtexture_over🔗
- voidset_over_texture(value:Texture2D)
voidset_over_texture(value:Texture2D)
- Texture2Dget_over_texture()
Texture2Dget_over_texture()
Texture2Dthat draws over the progress bar. Use it to add highlights or an upper-frame that hides part oftexture_progress.
Texture2Dtexture_progress🔗
- voidset_progress_texture(value:Texture2D)
voidset_progress_texture(value:Texture2D)
- Texture2Dget_progress_texture()
Texture2Dget_progress_texture()
Texture2Dthat clips based on the node'svalueandfill_mode. Asvalueincreased, the texture fills up. It shows entirely whenvaluereachesmax_value. It doesn't show at all ifvalueis equal tomin_value.
Thevalueproperty comes fromRange. SeeRange.value,Range.min_value,Range.max_value.
Vector2texture_progress_offset=Vector2(0,0)🔗
- voidset_texture_progress_offset(value:Vector2)
voidset_texture_progress_offset(value:Vector2)
- Vector2get_texture_progress_offset()
Vector2get_texture_progress_offset()
The offset oftexture_progress. Useful fortexture_overandtexture_underwith fancy borders, to avoid transparent margins in your progress texture.
Texture2Dtexture_under🔗
- voidset_under_texture(value:Texture2D)
voidset_under_texture(value:Texture2D)
- Texture2Dget_under_texture()
Texture2Dget_under_texture()
Texture2Dthat draws under the progress bar. The bar's background.
Colortint_over=Color(1,1,1,1)🔗
- voidset_tint_over(value:Color)
voidset_tint_over(value:Color)
- Colorget_tint_over()
Colorget_tint_over()
Multiplies the color of the bar'stexture_overtexture. The effect is similar toCanvasItem.modulate, except it only affects this specific texture instead of the entire node.
Colortint_progress=Color(1,1,1,1)🔗
- voidset_tint_progress(value:Color)
voidset_tint_progress(value:Color)
- Colorget_tint_progress()
Colorget_tint_progress()
Multiplies the color of the bar'stexture_progresstexture.
Colortint_under=Color(1,1,1,1)🔗
- voidset_tint_under(value:Color)
voidset_tint_under(value:Color)
- Colorget_tint_under()
Colorget_tint_under()
Multiplies the color of the bar'stexture_undertexture.

## Method Descriptions

intget_stretch_margin(margin:Side)const🔗
Returns the stretch margin with the specified index. Seestretch_margin_bottomand related properties.
voidset_stretch_margin(margin:Side, value:int)🔗
Sets the stretch margin with the specified index. Seestretch_margin_bottomand related properties.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
