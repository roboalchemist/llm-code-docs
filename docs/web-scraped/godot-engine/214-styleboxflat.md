# StyleBoxFlat

# StyleBoxFlat
Inherits:StyleBox<Resource<RefCounted<Object
A customizableStyleBoxthat doesn't use a texture.

## Description
By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.
Setting corner radius to high values is allowed. As soon as corners overlap, the stylebox will switch to a relative system:
```
height = 30
corner_radius_top_left = 50
corner_radius_bottom_left = 100
```
The relative system now would take the 1:2 ratio of the two left corners to calculate the actual corner width. Both corners added willneverbe more than the height. Result:
```
corner_radius_top_left: 10
corner_radius_bottom_left: 20
```

## Properties

| bool | anti_aliasing | true |
|---|---|---|
| float | anti_aliasing_size | 1.0 |
| Color | bg_color | Color(0.6,0.6,0.6,1) |
| bool | border_blend | false |
| Color | border_color | Color(0.8,0.8,0.8,1) |
| int | border_width_bottom | 0 |
| int | border_width_left | 0 |
| int | border_width_right | 0 |
| int | border_width_top | 0 |
| int | corner_detail | 8 |
| int | corner_radius_bottom_left | 0 |
| int | corner_radius_bottom_right | 0 |
| int | corner_radius_top_left | 0 |
| int | corner_radius_top_right | 0 |
| bool | draw_center | true |
| float | expand_margin_bottom | 0.0 |
| float | expand_margin_left | 0.0 |
| float | expand_margin_right | 0.0 |
| float | expand_margin_top | 0.0 |
| Color | shadow_color | Color(0,0,0,0.6) |
| Vector2 | shadow_offset | Vector2(0,0) |
| int | shadow_size | 0 |
| Vector2 | skew | Vector2(0,0) |

bool
anti_aliasing
true
float
anti_aliasing_size
Color
bg_color
Color(0.6,0.6,0.6,1)
bool
border_blend
false
Color
border_color
Color(0.8,0.8,0.8,1)
border_width_bottom
border_width_left
border_width_right
border_width_top
corner_detail
corner_radius_bottom_left
corner_radius_bottom_right
corner_radius_top_left
corner_radius_top_right
bool
draw_center
true
float
expand_margin_bottom
float
expand_margin_left
float
expand_margin_right
float
expand_margin_top
Color
shadow_color
Color(0,0,0,0.6)
Vector2
shadow_offset
Vector2(0,0)
shadow_size
Vector2
skew
Vector2(0,0)

## Methods

| int | get_border_width(margin:Side)const |
|---|---|
| int | get_border_width_min()const |
| int | get_corner_radius(corner:Corner)const |
| float | get_expand_margin(margin:Side)const |
| void | set_border_width(margin:Side, width:int) |
| void | set_border_width_all(width:int) |
| void | set_corner_radius(corner:Corner, radius:int) |
| void | set_corner_radius_all(radius:int) |
| void | set_expand_margin(margin:Side, size:float) |
| void | set_expand_margin_all(size:float) |

get_border_width(margin:Side)const
get_border_width_min()const
get_corner_radius(corner:Corner)const
float
get_expand_margin(margin:Side)const
void
set_border_width(margin:Side, width:int)
void
set_border_width_all(width:int)
void
set_corner_radius(corner:Corner, radius:int)
void
set_corner_radius_all(radius:int)
void
set_expand_margin(margin:Side, size:float)
void
set_expand_margin_all(size:float)

## Property Descriptions
boolanti_aliasing=true🔗
- voidset_anti_aliased(value:bool)
voidset_anti_aliased(value:bool)
- boolis_anti_aliased()
boolis_anti_aliased()
Antialiasing draws a small ring around the edges, which fades to transparency. As a result, edges look much smoother. This is only noticeable when using rounded corners orskew.
Note:When using beveled corners with 45-degree angles (corner_detail= 1), it is recommended to setanti_aliasingtofalseto ensure crisp visuals and avoid possible visual glitches.
floatanti_aliasing_size=1.0🔗
- voidset_aa_size(value:float)
voidset_aa_size(value:float)
- floatget_aa_size()
floatget_aa_size()
This changes the size of the antialiasing effect.1.0is recommended for an optimal result at 100% scale, identical to how rounded rectangles are rendered in web browsers and most vector drawing software.
Note:Higher values may produce a blur effect but can also create undesired artifacts on small boxes with large-radius corners.
Colorbg_color=Color(0.6,0.6,0.6,1)🔗
- voidset_bg_color(value:Color)
voidset_bg_color(value:Color)
- Colorget_bg_color()
Colorget_bg_color()
The background color of the stylebox.
boolborder_blend=false🔗
- voidset_border_blend(value:bool)
voidset_border_blend(value:bool)
- boolget_border_blend()
boolget_border_blend()
Iftrue, the border will fade into the background color.
Colorborder_color=Color(0.8,0.8,0.8,1)🔗
- voidset_border_color(value:Color)
voidset_border_color(value:Color)
- Colorget_border_color()
Colorget_border_color()
Sets the color of the border.
intborder_width_bottom=0🔗
- voidset_border_width(margin:Side, width:int)
voidset_border_width(margin:Side, width:int)
- intget_border_width(margin:Side)const
intget_border_width(margin:Side)const
Border width for the bottom border.
intborder_width_left=0🔗
- voidset_border_width(margin:Side, width:int)
voidset_border_width(margin:Side, width:int)
- intget_border_width(margin:Side)const
intget_border_width(margin:Side)const
Border width for the left border.
intborder_width_right=0🔗
- voidset_border_width(margin:Side, width:int)
voidset_border_width(margin:Side, width:int)
- intget_border_width(margin:Side)const
intget_border_width(margin:Side)const
Border width for the right border.
intborder_width_top=0🔗
- voidset_border_width(margin:Side, width:int)
voidset_border_width(margin:Side, width:int)
- intget_border_width(margin:Side)const
intget_border_width(margin:Side)const
Border width for the top border.
intcorner_detail=8🔗
- voidset_corner_detail(value:int)
voidset_corner_detail(value:int)
- intget_corner_detail()
intget_corner_detail()
This sets the number of vertices used for each corner. Higher values result in rounder corners but take more processing power to compute. When choosing a value, you should take the corner radius (set_corner_radius_all()) into account.
For corner radii less than 10,4or5should be enough. For corner radii less than 30, values between8and12should be enough.
A corner detail of1will result in chamfered corners instead of rounded corners, which is useful for some artistic effects.
intcorner_radius_bottom_left=0🔗
- voidset_corner_radius(corner:Corner, radius:int)
voidset_corner_radius(corner:Corner, radius:int)
- intget_corner_radius(corner:Corner)const
intget_corner_radius(corner:Corner)const
The bottom-left corner's radius. If0, the corner is not rounded.
intcorner_radius_bottom_right=0🔗
- voidset_corner_radius(corner:Corner, radius:int)
voidset_corner_radius(corner:Corner, radius:int)
- intget_corner_radius(corner:Corner)const
intget_corner_radius(corner:Corner)const
The bottom-right corner's radius. If0, the corner is not rounded.
intcorner_radius_top_left=0🔗
- voidset_corner_radius(corner:Corner, radius:int)
voidset_corner_radius(corner:Corner, radius:int)
- intget_corner_radius(corner:Corner)const
intget_corner_radius(corner:Corner)const
The top-left corner's radius. If0, the corner is not rounded.
intcorner_radius_top_right=0🔗
- voidset_corner_radius(corner:Corner, radius:int)
voidset_corner_radius(corner:Corner, radius:int)
- intget_corner_radius(corner:Corner)const
intget_corner_radius(corner:Corner)const
The top-right corner's radius. If0, the corner is not rounded.
booldraw_center=true🔗
- voidset_draw_center(value:bool)
voidset_draw_center(value:bool)
- boolis_draw_center_enabled()
boolis_draw_center_enabled()
Toggles drawing of the inner part of the stylebox.
floatexpand_margin_bottom=0.0🔗
- voidset_expand_margin(margin:Side, size:float)
voidset_expand_margin(margin:Side, size:float)
- floatget_expand_margin(margin:Side)const
floatget_expand_margin(margin:Side)const
Expands the stylebox outside of the control rect on the bottom edge. Useful in combination withborder_width_bottomto draw a border outside the control rect.
Note:UnlikeStyleBox.content_margin_bottom,expand_margin_bottomdoesnotaffect the size of the clickable area forControls. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.
floatexpand_margin_left=0.0🔗
- voidset_expand_margin(margin:Side, size:float)
voidset_expand_margin(margin:Side, size:float)
- floatget_expand_margin(margin:Side)const
floatget_expand_margin(margin:Side)const
Expands the stylebox outside of the control rect on the left edge. Useful in combination withborder_width_leftto draw a border outside the control rect.
Note:UnlikeStyleBox.content_margin_left,expand_margin_leftdoesnotaffect the size of the clickable area forControls. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.
floatexpand_margin_right=0.0🔗
- voidset_expand_margin(margin:Side, size:float)
voidset_expand_margin(margin:Side, size:float)
- floatget_expand_margin(margin:Side)const
floatget_expand_margin(margin:Side)const
Expands the stylebox outside of the control rect on the right edge. Useful in combination withborder_width_rightto draw a border outside the control rect.
Note:UnlikeStyleBox.content_margin_right,expand_margin_rightdoesnotaffect the size of the clickable area forControls. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.
floatexpand_margin_top=0.0🔗
- voidset_expand_margin(margin:Side, size:float)
voidset_expand_margin(margin:Side, size:float)
- floatget_expand_margin(margin:Side)const
floatget_expand_margin(margin:Side)const
Expands the stylebox outside of the control rect on the top edge. Useful in combination withborder_width_topto draw a border outside the control rect.
Note:UnlikeStyleBox.content_margin_top,expand_margin_topdoesnotaffect the size of the clickable area forControls. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.
Colorshadow_color=Color(0,0,0,0.6)🔗
- voidset_shadow_color(value:Color)
voidset_shadow_color(value:Color)
- Colorget_shadow_color()
Colorget_shadow_color()
The color of the shadow. This has no effect ifshadow_sizeis lower than 1.
Vector2shadow_offset=Vector2(0,0)🔗
- voidset_shadow_offset(value:Vector2)
voidset_shadow_offset(value:Vector2)
- Vector2get_shadow_offset()
Vector2get_shadow_offset()
The shadow offset in pixels. Adjusts the position of the shadow relatively to the stylebox.
intshadow_size=0🔗
- voidset_shadow_size(value:int)
voidset_shadow_size(value:int)
- intget_shadow_size()
intget_shadow_size()
The shadow size in pixels.
Vector2skew=Vector2(0,0)🔗
- voidset_skew(value:Vector2)
voidset_skew(value:Vector2)
- Vector2get_skew()
Vector2get_skew()
If set to a non-zero value on either axis,skewdistorts the StyleBox horizontally and/or vertically. This can be used for "futuristic"-style UIs. Positive values skew the StyleBox towards the right (X axis) and upwards (Y axis), while negative values skew the StyleBox towards the left (X axis) and downwards (Y axis).
Note:To ensure text does not touch the StyleBox's edges, consider increasing theStyleBox's content margin (seeStyleBox.content_margin_bottom). It is preferable to increase the content margin instead of the expand margin (seeexpand_margin_bottom), as increasing the expand margin does not increase the size of the clickable area forControls.

## Method Descriptions
intget_border_width(margin:Side)const🔗
Returns the specifiedSide's border width.
intget_border_width_min()const🔗
Returns the smallest border width out of all four borders.
intget_corner_radius(corner:Corner)const🔗
Returns the givencorner's radius.
floatget_expand_margin(margin:Side)const🔗
Returns the size of the specifiedSide's expand margin.
voidset_border_width(margin:Side, width:int)🔗
Sets the specifiedSide's border width towidthpixels.
voidset_border_width_all(width:int)🔗
Sets the border width towidthpixels for all sides.
voidset_corner_radius(corner:Corner, radius:int)🔗
Sets the corner radius toradiuspixels for the givencorner.
voidset_corner_radius_all(radius:int)🔗
Sets the corner radius toradiuspixels for all corners.
voidset_expand_margin(margin:Side, size:float)🔗
Sets the expand margin tosizepixels for the specifiedSide.
voidset_expand_margin_all(size:float)🔗
Sets the expand margin tosizepixels for all sides.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.