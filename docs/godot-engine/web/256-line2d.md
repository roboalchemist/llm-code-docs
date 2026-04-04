# Line2D

# Line2D
Inherits:Node2D<CanvasItem<Node<Object
A 2D polyline that can optionally be textured.

## Description
This node draws a 2D polyline, i.e. a shape consisting of several points connected by segments.Line2Dis not a mathematical polyline, i.e. the segments are not infinitely thin. It is intended for rendering and it can be colored and optionally textured.
Warning:Certain configurations may be impossible to draw nicely, such as very sharp angles. In these situations, the node uses fallback drawing logic to look decent.
Note:Line2Dis drawn using a 2D mesh.

## Tutorials
- Matrix Transform Demo
Matrix Transform Demo
- 2.5D Game Demo
2.5D Game Demo

## Properties

| bool | antialiased | false |
|---|---|---|
| LineCapMode | begin_cap_mode | 0 |
| bool | closed | false |
| Color | default_color | Color(1,1,1,1) |
| LineCapMode | end_cap_mode | 0 |
| Gradient | gradient |  |
| LineJointMode | joint_mode | 0 |
| PackedVector2Array | points | PackedVector2Array() |
| int | round_precision | 8 |
| float | sharp_limit | 2.0 |
| Texture2D | texture |  |
| LineTextureMode | texture_mode | 0 |
| float | width | 10.0 |
| Curve | width_curve |  |

bool
antialiased
false
LineCapMode
begin_cap_mode
bool
closed
false
Color
default_color
Color(1,1,1,1)
LineCapMode
end_cap_mode
Gradient
gradient
LineJointMode
joint_mode
PackedVector2Array
points
PackedVector2Array()
round_precision
float
sharp_limit
Texture2D
texture
LineTextureMode
texture_mode
float
width
10.0
Curve
width_curve

## Methods

| void | add_point(position:Vector2, index:int= -1) |
|---|---|
| void | clear_points() |
| int | get_point_count()const |
| Vector2 | get_point_position(index:int)const |
| void | remove_point(index:int) |
| void | set_point_position(index:int, position:Vector2) |

void
add_point(position:Vector2, index:int= -1)
void
clear_points()
get_point_count()const
Vector2
get_point_position(index:int)const
void
remove_point(index:int)
void
set_point_position(index:int, position:Vector2)

## Enumerations
enumLineJointMode:🔗
LineJointModeLINE_JOINT_SHARP=0
Makes the polyline's joints pointy, connecting the sides of the two segments by extending them until they intersect. If the rotation of a joint is too big (based onsharp_limit), the joint falls back toLINE_JOINT_BEVELto prevent very long miters.
LineJointModeLINE_JOINT_BEVEL=1
Makes the polyline's joints bevelled/chamfered, connecting the sides of the two segments with a simple line.
LineJointModeLINE_JOINT_ROUND=2
Makes the polyline's joints rounded, connecting the sides of the two segments with an arc. The detail of this arc depends onround_precision.
enumLineCapMode:🔗
LineCapModeLINE_CAP_NONE=0
Draws no line cap.
LineCapModeLINE_CAP_BOX=1
Draws the line cap as a box, slightly extending the first/last segment.
LineCapModeLINE_CAP_ROUND=2
Draws the line cap as a semicircle attached to the first/last segment.
enumLineTextureMode:🔗
LineTextureModeLINE_TEXTURE_NONE=0
Takes the left pixels of the texture and renders them over the whole polyline.
LineTextureModeLINE_TEXTURE_TILE=1
Tiles the texture over the polyline.CanvasItem.texture_repeatof theLine2Dnode must beCanvasItem.TEXTURE_REPEAT_ENABLEDorCanvasItem.TEXTURE_REPEAT_MIRRORfor it to work properly.
LineTextureModeLINE_TEXTURE_STRETCH=2
Stretches the texture across the polyline.CanvasItem.texture_repeatof theLine2Dnode must beCanvasItem.TEXTURE_REPEAT_DISABLEDfor best results.

## Property Descriptions
boolantialiased=false🔗
- voidset_antialiased(value:bool)
voidset_antialiased(value:bool)
- boolget_antialiased()
boolget_antialiased()
Iftrue, the polyline's border will be anti-aliased.
Note:Line2Dis not accelerated by batching when being anti-aliased.
LineCapModebegin_cap_mode=0🔗
- voidset_begin_cap_mode(value:LineCapMode)
voidset_begin_cap_mode(value:LineCapMode)
- LineCapModeget_begin_cap_mode()
LineCapModeget_begin_cap_mode()
The style of the beginning of the polyline, ifclosedisfalse.
boolclosed=false🔗
- voidset_closed(value:bool)
voidset_closed(value:bool)
- boolis_closed()
boolis_closed()
Iftrueand the polyline has more than 2 points, the last point and the first one will be connected by a segment.
Note:The shape of the closing segment is not guaranteed to be seamless if awidth_curveis provided.
Note:The joint between the closing segment and the first segment is drawn first and it samples thegradientand thewidth_curveat the beginning. This is an implementation detail that might change in a future version.
Colordefault_color=Color(1,1,1,1)🔗
- voidset_default_color(value:Color)
voidset_default_color(value:Color)
- Colorget_default_color()
Colorget_default_color()
The color of the polyline. Will not be used if a gradient is set.
LineCapModeend_cap_mode=0🔗
- voidset_end_cap_mode(value:LineCapMode)
voidset_end_cap_mode(value:LineCapMode)
- LineCapModeget_end_cap_mode()
LineCapModeget_end_cap_mode()
The style of the end of the polyline, ifclosedisfalse.
Gradientgradient🔗
- voidset_gradient(value:Gradient)
voidset_gradient(value:Gradient)
- Gradientget_gradient()
Gradientget_gradient()
The gradient is drawn through the whole line from start to finish. Thedefault_colorwill not be used if this property is set.
LineJointModejoint_mode=0🔗
- voidset_joint_mode(value:LineJointMode)
voidset_joint_mode(value:LineJointMode)
- LineJointModeget_joint_mode()
LineJointModeget_joint_mode()
The style of the connections between segments of the polyline.
PackedVector2Arraypoints=PackedVector2Array()🔗
- voidset_points(value:PackedVector2Array)
voidset_points(value:PackedVector2Array)
- PackedVector2Arrayget_points()
PackedVector2Arrayget_points()
The points of the polyline, interpreted in local 2D coordinates. Segments are drawn between the adjacent points in this array.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.
intround_precision=8🔗
- voidset_round_precision(value:int)
voidset_round_precision(value:int)
- intget_round_precision()
intget_round_precision()
The smoothness used for rounded joints and caps. Higher values result in smoother corners, but are more demanding to render and update.
floatsharp_limit=2.0🔗
- voidset_sharp_limit(value:float)
voidset_sharp_limit(value:float)
- floatget_sharp_limit()
floatget_sharp_limit()
Determines the miter limit of the polyline. Normally, whenjoint_modeis set toLINE_JOINT_SHARP, sharp angles fall back to using the logic ofLINE_JOINT_BEVELjoints to prevent very long miters. Higher values of this property mean that the fallback to a bevel joint will happen at sharper angles.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
The texture used for the polyline. Usestexture_modefor drawing style.
LineTextureModetexture_mode=0🔗
- voidset_texture_mode(value:LineTextureMode)
voidset_texture_mode(value:LineTextureMode)
- LineTextureModeget_texture_mode()
LineTextureModeget_texture_mode()
The style to render thetextureof the polyline.
floatwidth=10.0🔗
- voidset_width(value:float)
voidset_width(value:float)
- floatget_width()
floatget_width()
The polyline's width.
Curvewidth_curve🔗
- voidset_curve(value:Curve)
voidset_curve(value:Curve)
- Curveget_curve()
Curveget_curve()
The polyline's width curve. The width of the polyline over its length will be equivalent to the value of the width curve over its domain. The width curve should be a unitCurve.

## Method Descriptions
voidadd_point(position:Vector2, index:int= -1)🔗
Adds a point with the specifiedpositionrelative to the polyline's own position. If noindexis provided, the new point will be added to the end of the points array.
Ifindexis given, the new point is inserted before the existing point identified by indexindex. The indices of the points after the new point get increased by 1. The providedindexmust not exceed the number of existing points in the polyline. Seeget_point_count().
voidclear_points()🔗
Removes all points from the polyline, making it empty.
intget_point_count()const🔗
Returns the number of points in the polyline.
Vector2get_point_position(index:int)const🔗
Returns the position of the point at indexindex.
voidremove_point(index:int)🔗
Removes the point at indexindexfrom the polyline.
voidset_point_position(index:int, position:Vector2)🔗
Overwrites the position of the point at the givenindexwith the suppliedposition.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.