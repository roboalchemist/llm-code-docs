# Node2D in English

# Node2D
Inherits:CanvasItem<Node<Object
Inherited By:AnimatedSprite2D,AudioListener2D,AudioStreamPlayer2D,BackBufferCopy,Bone2D,Camera2D,CanvasGroup,CanvasModulate,CollisionObject2D,CollisionPolygon2D,CollisionShape2D,CPUParticles2D,GPUParticles2D,Joint2D,Light2D,LightOccluder2D,Line2D,Marker2D,MeshInstance2D,MultiMeshInstance2D,NavigationLink2D,NavigationObstacle2D,NavigationRegion2D,Parallax2D,ParallaxLayer,Path2D,PathFollow2D,Polygon2D,RayCast2D,RemoteTransform2D,ShapeCast2D,Skeleton2D,Sprite2D,TileMap,TileMapLayer,TouchScreenButton,VisibleOnScreenNotifier2D
A 2D game object, inherited by all 2D-related nodes. Has a position, rotation, scale, and skew.

## Description
A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.
Note:Since bothNode2DandControlinherit fromCanvasItem, they share several concepts from the class such as theCanvasItem.z_indexandCanvasItem.visibleproperties.

## Tutorials
- Custom drawing in 2D
Custom drawing in 2D
- All 2D Demos
All 2D Demos

## Properties

| Vector2 | global_position |  |
|---|---|---|
| float | global_rotation |  |
| float | global_rotation_degrees |  |
| Vector2 | global_scale |  |
| float | global_skew |  |
| Transform2D | global_transform |  |
| Vector2 | position | Vector2(0,0) |
| float | rotation | 0.0 |
| float | rotation_degrees |  |
| Vector2 | scale | Vector2(1,1) |
| float | skew | 0.0 |
| Transform2D | transform |  |

Vector2
global_position
float
global_rotation
float
global_rotation_degrees
Vector2
global_scale
float
global_skew
Transform2D
global_transform
Vector2
position
Vector2(0,0)
float
rotation
float
rotation_degrees
Vector2
scale
Vector2(1,1)
float
skew
Transform2D
transform

## Methods

| void | apply_scale(ratio:Vector2) |
|---|---|
| float | get_angle_to(point:Vector2)const |
| Transform2D | get_relative_transform_to_parent(parent:Node)const |
| void | global_translate(offset:Vector2) |
| void | look_at(point:Vector2) |
| void | move_local_x(delta:float, scaled:bool= false) |
| void | move_local_y(delta:float, scaled:bool= false) |
| void | rotate(radians:float) |
| Vector2 | to_global(local_point:Vector2)const |
| Vector2 | to_local(global_point:Vector2)const |
| void | translate(offset:Vector2) |

void
apply_scale(ratio:Vector2)
float
get_angle_to(point:Vector2)const
Transform2D
get_relative_transform_to_parent(parent:Node)const
void
global_translate(offset:Vector2)
void
look_at(point:Vector2)
void
move_local_x(delta:float, scaled:bool= false)
void
move_local_y(delta:float, scaled:bool= false)
void
rotate(radians:float)
Vector2
to_global(local_point:Vector2)const
Vector2
to_local(global_point:Vector2)const
void
translate(offset:Vector2)

## Property Descriptions
Vector2global_position🔗
- voidset_global_position(value:Vector2)
voidset_global_position(value:Vector2)
- Vector2get_global_position()
Vector2get_global_position()
Global position. See alsoposition.
floatglobal_rotation🔗
- voidset_global_rotation(value:float)
voidset_global_rotation(value:float)
- floatget_global_rotation()
floatget_global_rotation()
Global rotation in radians. See alsorotation.
floatglobal_rotation_degrees🔗
- voidset_global_rotation_degrees(value:float)
voidset_global_rotation_degrees(value:float)
- floatget_global_rotation_degrees()
floatget_global_rotation_degrees()
Helper property to accessglobal_rotationin degrees instead of radians. See alsorotation_degrees.
Vector2global_scale🔗
- voidset_global_scale(value:Vector2)
voidset_global_scale(value:Vector2)
- Vector2get_global_scale()
Vector2get_global_scale()
Global scale. See alsoscale.
floatglobal_skew🔗
- voidset_global_skew(value:float)
voidset_global_skew(value:float)
- floatget_global_skew()
floatget_global_skew()
Global skew in radians. See alsoskew.
Transform2Dglobal_transform🔗
- voidset_global_transform(value:Transform2D)
voidset_global_transform(value:Transform2D)
- Transform2Dget_global_transform()
Transform2Dget_global_transform()
GlobalTransform2D. See alsotransform.
Vector2position=Vector2(0,0)🔗
- voidset_position(value:Vector2)
voidset_position(value:Vector2)
- Vector2get_position()
Vector2get_position()
Position, relative to the node's parent. See alsoglobal_position.
floatrotation=0.0🔗
- voidset_rotation(value:float)
voidset_rotation(value:float)
- floatget_rotation()
floatget_rotation()
Rotation in radians, relative to the node's parent. See alsoglobal_rotation.
Note:This property is edited in the inspector in degrees. If you want to use degrees in a script, userotation_degrees.
floatrotation_degrees🔗
- voidset_rotation_degrees(value:float)
voidset_rotation_degrees(value:float)
- floatget_rotation_degrees()
floatget_rotation_degrees()
Helper property to accessrotationin degrees instead of radians. See alsoglobal_rotation_degrees.
Vector2scale=Vector2(1,1)🔗
- voidset_scale(value:Vector2)
voidset_scale(value:Vector2)
- Vector2get_scale()
Vector2get_scale()
The node's scale, relative to the node's parent. Unscaled value:(1,1). See alsoglobal_scale.
Note:Negative X scales in 2D are not decomposable from the transformation matrix. Due to the way scale is represented with transformation matrices in Godot, negative scales on the X axis will be changed to negative scales on the Y axis and a rotation of 180 degrees when decomposed.
floatskew=0.0🔗
- voidset_skew(value:float)
voidset_skew(value:float)
- floatget_skew()
floatget_skew()
If set to a non-zero value, slants the node in one direction or another. This can be used for pseudo-3D effects. See alsoglobal_skew.
Note:Skew is performed on the X axis only, andbetweenrotation and scaling.
Note:This property is edited in the inspector in degrees. If you want to use degrees in a script, useskew=deg_to_rad(value_in_degrees).
Transform2Dtransform🔗
- voidset_transform(value:Transform2D)
voidset_transform(value:Transform2D)
- Transform2Dget_transform()
Transform2Dget_transform()
The node'sTransform2D, relative to the node's parent. See alsoglobal_transform.

## Method Descriptions
voidapply_scale(ratio:Vector2)🔗
Multiplies the current scale by theratiovector.
floatget_angle_to(point:Vector2)const🔗
Returns the angle between the node and thepointin radians. See alsolook_at().
Illustration of the returned angle.
Transform2Dget_relative_transform_to_parent(parent:Node)const🔗
Returns theTransform2Drelative to this node's parent.
voidglobal_translate(offset:Vector2)🔗
Adds theoffsetvector to the node's global position.
voidlook_at(point:Vector2)🔗
Rotates the node so that its local +X axis points towards thepoint, which is expected to use global coordinates. This method is a combination of bothrotate()andget_angle_to().
pointshould not be the same as the node's position, otherwise the node always looks to the right.
voidmove_local_x(delta:float, scaled:bool= false)🔗
Applies a local translation on the node's X axis with the amount specified indelta. Ifscaledisfalse, normalizes the movement to occur independently of the node'sscale.
voidmove_local_y(delta:float, scaled:bool= false)🔗
Applies a local translation on the node's Y axis with the amount specified indelta. Ifscaledisfalse, normalizes the movement to occur independently of the node'sscale.
voidrotate(radians:float)🔗
Applies a rotation to the node, in radians, starting from its current rotation. This is equivalent torotation+=radians.
Vector2to_global(local_point:Vector2)const🔗
Transforms the provided local position into a position in global coordinate space. The input is expected to be local relative to theNode2Dit is called on. e.g. Applying this method to the positions of child nodes will correctly transform their positions into the global coordinate space, but applying it to a node's own position will give an incorrect result, as it will incorporate the node's own transformation into its global position.
Vector2to_local(global_point:Vector2)const🔗
Transforms the provided global position into a position in local coordinate space. The output will be local relative to theNode2Dit is called on. e.g. It is appropriate for determining the positions of child nodes, but it is not appropriate for determining its own position relative to its parent.
voidtranslate(offset:Vector2)🔗
Translates the node by the givenoffsetin local coordinates. This is equivalent toposition+=offset.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.