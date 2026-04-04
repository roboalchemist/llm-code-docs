# AnimationNodeBlendSpace2D in English

# AnimationNodeBlendSpace2D

Inherits:AnimationRootNode<AnimationNode<Resource<RefCounted<Object
A set ofAnimationRootNodes placed on 2D coordinates, crossfading between the three adjacent ones. Used byAnimationTree.

## Description

A resource used byAnimationNodeBlendTree.
AnimationNodeBlendSpace2Drepresents a virtual 2D space on whichAnimationRootNodes are placed. Outputs the linear blend of the three adjacent animations using aVector2weight. Adjacent in this context means the threeAnimationRootNodes making up the triangle that contains the current value.
You can add vertices to the blend space withadd_blend_point()and automatically triangulate it by settingauto_trianglestotrue. Otherwise, useadd_triangle()andremove_triangle()to triangulate the blend space by hand.

## Tutorials

- Using AnimationTree
Using AnimationTree
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| bool | auto_triangles | true |
|---|---|---|
| BlendMode | blend_mode | 0 |
| Vector2 | max_space | Vector2(1,1) |
| Vector2 | min_space | Vector2(-1,-1) |
| Vector2 | snap | Vector2(0.1,0.1) |
| bool | sync | false |
| String | x_label | "x" |
| String | y_label | "y" |

bool
auto_triangles
true
BlendMode
blend_mode
Vector2
max_space
Vector2(1,1)
Vector2
min_space
Vector2(-1,-1)
Vector2
snap
Vector2(0.1,0.1)
bool
sync
false
String
x_label
String
y_label

## Methods

| void | add_blend_point(node:AnimationRootNode, pos:Vector2, at_index:int= -1) |
|---|---|
| void | add_triangle(x:int, y:int, z:int, at_index:int= -1) |
| int | get_blend_point_count()const |
| AnimationRootNode | get_blend_point_node(point:int)const |
| Vector2 | get_blend_point_position(point:int)const |
| int | get_triangle_count()const |
| int | get_triangle_point(triangle:int, point:int) |
| void | remove_blend_point(point:int) |
| void | remove_triangle(triangle:int) |
| void | set_blend_point_node(point:int, node:AnimationRootNode) |
| void | set_blend_point_position(point:int, pos:Vector2) |

void
add_blend_point(node:AnimationRootNode, pos:Vector2, at_index:int= -1)
void
add_triangle(x:int, y:int, z:int, at_index:int= -1)
get_blend_point_count()const
AnimationRootNode
get_blend_point_node(point:int)const
Vector2
get_blend_point_position(point:int)const
get_triangle_count()const
get_triangle_point(triangle:int, point:int)
void
remove_blend_point(point:int)
void
remove_triangle(triangle:int)
void
set_blend_point_node(point:int, node:AnimationRootNode)
void
set_blend_point_position(point:int, pos:Vector2)

## Signals

triangles_updated()🔗
Emitted every time the blend space's triangles are created, removed, or when one of their vertices changes position.

## Enumerations

enumBlendMode:🔗
BlendModeBLEND_MODE_INTERPOLATED=0
The interpolation between animations is linear.
BlendModeBLEND_MODE_DISCRETE=1
The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.
BlendModeBLEND_MODE_DISCRETE_CARRY=2
Similar toBLEND_MODE_DISCRETE, but starts the new animation at the last animation's playback position.

## Property Descriptions

boolauto_triangles=true🔗

- voidset_auto_triangles(value:bool)
voidset_auto_triangles(value:bool)
- boolget_auto_triangles()
boolget_auto_triangles()
Iftrue, the blend space is triangulated automatically. The mesh updates every time you add or remove points withadd_blend_point()andremove_blend_point().
BlendModeblend_mode=0🔗
- voidset_blend_mode(value:BlendMode)
voidset_blend_mode(value:BlendMode)
- BlendModeget_blend_mode()
BlendModeget_blend_mode()
Controls the interpolation between animations.
Vector2max_space=Vector2(1,1)🔗
- voidset_max_space(value:Vector2)
voidset_max_space(value:Vector2)
- Vector2get_max_space()
Vector2get_max_space()
The blend space's X and Y axes' upper limit for the points' position. Seeadd_blend_point().
Vector2min_space=Vector2(-1,-1)🔗
- voidset_min_space(value:Vector2)
voidset_min_space(value:Vector2)
- Vector2get_min_space()
Vector2get_min_space()
The blend space's X and Y axes' lower limit for the points' position. Seeadd_blend_point().
Vector2snap=Vector2(0.1,0.1)🔗
- voidset_snap(value:Vector2)
voidset_snap(value:Vector2)
- Vector2get_snap()
Vector2get_snap()
Position increment to snap to when moving a point.
boolsync=false🔗
- voidset_use_sync(value:bool)
voidset_use_sync(value:bool)
- boolis_using_sync()
boolis_using_sync()
Iffalse, the blended animations' frame are stopped when the blend value is0.
Iftrue, forcing the blended animations to advance frame.
Stringx_label="x"🔗
- voidset_x_label(value:String)
voidset_x_label(value:String)
- Stringget_x_label()
Stringget_x_label()
Name of the blend space's X axis.
Stringy_label="y"🔗
- voidset_y_label(value:String)
voidset_y_label(value:String)
- Stringget_y_label()
Stringget_y_label()
Name of the blend space's Y axis.

## Method Descriptions

voidadd_blend_point(node:AnimationRootNode, pos:Vector2, at_index:int= -1)🔗
Adds a new point that represents anodeat the position set bypos. You can insert it at a specific index using theat_indexargument. If you use the default value forat_index, the point is inserted at the end of the blend points array.
voidadd_triangle(x:int, y:int, z:int, at_index:int= -1)🔗
Creates a new triangle using three pointsx,y, andz. Triangles can overlap. You can insert the triangle at a specific index using theat_indexargument. If you use the default value forat_index, the point is inserted at the end of the blend points array.
intget_blend_point_count()const🔗
Returns the number of points in the blend space.
AnimationRootNodeget_blend_point_node(point:int)const🔗
Returns theAnimationRootNodereferenced by the point at indexpoint.
Vector2get_blend_point_position(point:int)const🔗
Returns the position of the point at indexpoint.
intget_triangle_count()const🔗
Returns the number of triangles in the blend space.
intget_triangle_point(triangle:int, point:int)🔗
Returns the position of the point at indexpointin the triangle of indextriangle.
voidremove_blend_point(point:int)🔗
Removes the point at indexpointfrom the blend space.
voidremove_triangle(triangle:int)🔗
Removes the triangle at indextrianglefrom the blend space.
voidset_blend_point_node(point:int, node:AnimationRootNode)🔗
Changes theAnimationNodereferenced by the point at indexpoint.
voidset_blend_point_position(point:int, pos:Vector2)🔗
Updates the position of the point at indexpointin the blend space.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
