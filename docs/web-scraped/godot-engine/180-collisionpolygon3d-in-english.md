# CollisionPolygon3D in English

# CollisionPolygon3D

Inherits:Node3D<Node<Object
A node that provides a thickened polygon shape (a prism) to aCollisionObject3Dparent.

## Description

A node that provides a thickened polygon shape (a prism) to aCollisionObject3Dparent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to anArea3Dor turn aPhysicsBody3Dinto a solid object.
Warning:A non-uniformly scaledCollisionShape3Dwill likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.

## Properties

| Color | debug_color | Color(0,0,0,0) |
|---|---|---|
| bool | debug_fill | true |
| float | depth | 1.0 |
| bool | disabled | false |
| float | margin | 0.04 |
| PackedVector2Array | polygon | PackedVector2Array() |

Color
debug_color
Color(0,0,0,0)
bool
debug_fill
true
float
depth
bool
disabled
false
float
margin
0.04
PackedVector2Array
polygon
PackedVector2Array()

## Property Descriptions

Colordebug_color=Color(0,0,0,0)🔗

- voidset_debug_color(value:Color)
voidset_debug_color(value:Color)
- Colorget_debug_color()
Colorget_debug_color()
The collision shape color that is displayed in the editor, or in the running project ifDebug > Visible Collision Shapesis checked at the top of the editor.
Note:The default value isProjectSettings.debug/shapes/collision/shape_color. TheColor(0,0,0,0)value documented here is a placeholder, and not the actual default debug color.
booldebug_fill=true🔗
- voidset_enable_debug_fill(value:bool)
voidset_enable_debug_fill(value:bool)
- boolget_enable_debug_fill()
boolget_enable_debug_fill()
Iftrue, when the shape is displayed, it will show a solid fill color in addition to its wireframe.
floatdepth=1.0🔗
- voidset_depth(value:float)
voidset_depth(value:float)
- floatget_depth()
floatget_depth()
Length that the resulting collision extends in either direction perpendicular to its 2D polygon.
booldisabled=false🔗
- voidset_disabled(value:bool)
voidset_disabled(value:bool)
- boolis_disabled()
boolis_disabled()
Iftrue, no collision will be produced. This property should be changed withObject.set_deferred().
floatmargin=0.04🔗
- voidset_margin(value:float)
voidset_margin(value:float)
- floatget_margin()
floatget_margin()
The collision margin for the generatedShape3D. SeeShape3D.marginfor more details.
PackedVector2Arraypolygon=PackedVector2Array()🔗
- voidset_polygon(value:PackedVector2Array)
voidset_polygon(value:PackedVector2Array)
- PackedVector2Arrayget_polygon()
PackedVector2Arrayget_polygon()
Array of vertices which define the 2D polygon in the local XY plane.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
