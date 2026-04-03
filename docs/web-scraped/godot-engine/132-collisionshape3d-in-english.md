# CollisionShape3D in English

# CollisionShape3D

Inherits:Node3D<Node<Object
A node that provides aShape3Dto aCollisionObject3Dparent.

## Description

A node that provides aShape3Dto aCollisionObject3Dparent and allows it to be edited. This can give a detection shape to anArea3Dor turn aPhysicsBody3Dinto a solid object.
Warning:A non-uniformly scaledCollisionShape3Dwill likely not behave as expected. Make sure to keep its scale the same on all axes and adjust itsshaperesource instead.

## Tutorials

- Physics introduction
Physics introduction
- 3D Kinematic Character Demo
3D Kinematic Character Demo
- 3D Platformer Demo
3D Platformer Demo
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| Color | debug_color | Color(0,0,0,0) |
|---|---|---|
| bool | debug_fill | true |
| bool | disabled | false |
| Shape3D | shape |  |

Color
debug_color
Color(0,0,0,0)
bool
debug_fill
true
bool
disabled
false
Shape3D
shape

## Methods

| void | make_convex_from_siblings() |
|---|---|
| void | resource_changed(resource:Resource) |

void
make_convex_from_siblings()
void
resource_changed(resource:Resource)

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
booldisabled=false🔗
- voidset_disabled(value:bool)
voidset_disabled(value:bool)
- boolis_disabled()
boolis_disabled()
A disabled collision shape has no effect in the world. This property should be changed withObject.set_deferred().
Shape3Dshape🔗
- voidset_shape(value:Shape3D)
voidset_shape(value:Shape3D)
- Shape3Dget_shape()
Shape3Dget_shape()
The actual shape owned by this collision shape.

## Method Descriptions

voidmake_convex_from_siblings()🔗
Sets the collision shape's shape to the addition of all its convexedMeshInstance3Dsiblings geometry.
voidresource_changed(resource:Resource)🔗
Deprecated:UseResource.changedinstead.
This method does nothing.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
