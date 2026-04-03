# CollisionShape2D in English

# CollisionShape2D
Inherits:Node2D<CanvasItem<Node<Object
A node that provides aShape2Dto aCollisionObject2Dparent.

## Description
A node that provides aShape2Dto aCollisionObject2Dparent and allows it to be edited. This can give a detection shape to anArea2Dor turn aPhysicsBody2Dinto a solid object.

## Tutorials
- Physics introduction
Physics introduction
- 2D Dodge The Creeps Demo
2D Dodge The Creeps Demo
- 2D Pong Demo
2D Pong Demo
- 2D Kinematic Character Demo
2D Kinematic Character Demo

## Properties

| Color | debug_color | Color(0,0,0,0) |
|---|---|---|
| bool | disabled | false |
| bool | one_way_collision | false |
| float | one_way_collision_margin | 1.0 |
| Shape2D | shape |  |

Color
debug_color
Color(0,0,0,0)
bool
disabled
false
bool
one_way_collision
false
float
one_way_collision_margin
Shape2D
shape

## Property Descriptions
Colordebug_color=Color(0,0,0,0)🔗
- voidset_debug_color(value:Color)
voidset_debug_color(value:Color)
- Colorget_debug_color()
Colorget_debug_color()
The collision shape color that is displayed in the editor, or in the running project ifDebug > Visible Collision Shapesis checked at the top of the editor.
Note:The default value isProjectSettings.debug/shapes/collision/shape_color. TheColor(0,0,0,0)value documented here is a placeholder, and not the actual default debug color.
booldisabled=false🔗
- voidset_disabled(value:bool)
voidset_disabled(value:bool)
- boolis_disabled()
boolis_disabled()
A disabled collision shape has no effect in the world. This property should be changed withObject.set_deferred().
boolone_way_collision=false🔗
- voidset_one_way_collision(value:bool)
voidset_one_way_collision(value:bool)
- boolis_one_way_collision_enabled()
boolis_one_way_collision_enabled()
Sets whether this collision shape should only detect collision on one side (top or bottom).
Note:This property has no effect if thisCollisionShape2Dis a child of anArea2Dnode.
floatone_way_collision_margin=1.0🔗
- voidset_one_way_collision_margin(value:float)
voidset_one_way_collision_margin(value:float)
- floatget_one_way_collision_margin()
floatget_one_way_collision_margin()
The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the shape at a high velocity.
Shape2Dshape🔗
- voidset_shape(value:Shape2D)
voidset_shape(value:Shape2D)
- Shape2Dget_shape()
Shape2Dget_shape()
The actual shape owned by this collision shape.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.