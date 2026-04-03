# CSGShape3D

# CSGShape3D

Inherits:GeometryInstance3D<VisualInstance3D<Node3D<Node<Object
Inherited By:CSGCombiner3D,CSGPrimitive3D
The CSG base class.

## Description

This is the CSG base class that provides CSG operation support to the various CSG nodes in Godot.
Performance:CSG nodes are only intended for prototyping as they have a significant CPU performance cost. Consider baking final CSG operation results into static geometry that replaces the CSG nodes.
Individual CSG root node results can be baked to nodes with static resources with the editor menu that appears when a CSG root node is selected.
Individual CSG root nodes can also be baked to static resources with scripts by callingbake_static_mesh()for the visual mesh orbake_collision_shape()for the physics collision.
Entire scenes of CSG nodes can be baked to static geometry and exported with the editor glTF scene exporter:Scene > Export As... > glTF 2.0 Scene...

## Tutorials

- Prototyping levels with CSG
Prototyping levels with CSG

## Properties

| bool | calculate_tangents | true |
|---|---|---|
| int | collision_layer | 1 |
| int | collision_mask | 1 |
| float | collision_priority | 1.0 |
| Operation | operation | 0 |
| float | snap |  |
| bool | use_collision | false |

bool
calculate_tangents
true
collision_layer
collision_mask
float
collision_priority
Operation
operation
float
snap
bool
use_collision
false

## Methods

| ConcavePolygonShape3D | bake_collision_shape() |
|---|---|
| ArrayMesh | bake_static_mesh() |
| bool | get_collision_layer_value(layer_number:int)const |
| bool | get_collision_mask_value(layer_number:int)const |
| Array | get_meshes()const |
| bool | is_root_shape()const |
| void | set_collision_layer_value(layer_number:int, value:bool) |
| void | set_collision_mask_value(layer_number:int, value:bool) |

ConcavePolygonShape3D
bake_collision_shape()
ArrayMesh
bake_static_mesh()
bool
get_collision_layer_value(layer_number:int)const
bool
get_collision_mask_value(layer_number:int)const
Array
get_meshes()const
bool
is_root_shape()const
void
set_collision_layer_value(layer_number:int, value:bool)
void
set_collision_mask_value(layer_number:int, value:bool)

## Enumerations

enumOperation:🔗
OperationOPERATION_UNION=0
Geometry of both primitives is merged, intersecting geometry is removed.
OperationOPERATION_INTERSECTION=1
Only intersecting geometry remains, the rest is removed.
OperationOPERATION_SUBTRACTION=2
The second shape is subtracted from the first, leaving a dent with its shape.

## Property Descriptions

boolcalculate_tangents=true🔗

- voidset_calculate_tangents(value:bool)
voidset_calculate_tangents(value:bool)
- boolis_calculating_tangents()
boolis_calculating_tangents()
Calculate tangents for the CSG shape which allows the use of normal and height maps. This is only applied on the root shape, this setting is ignored on any child. Setting this tofalsecan speed up shape generation slightly.
intcollision_layer=1🔗
- voidset_collision_layer(value:int)
voidset_collision_layer(value:int)
- intget_collision_layer()
intget_collision_layer()
The physics layers this area is in.
Collidable objects can exist in any of 32 different layers. These layers work like a tagging system, and are not visual. A collidable can use these layers to select with which objects it can collide, using the collision_mask property.
A contact is detected if object A is in any of the layers that object B scans, or object B is in any layer scanned by object A. SeeCollision layers and masksin the documentation for more information.
intcollision_mask=1🔗
- voidset_collision_mask(value:int)
voidset_collision_mask(value:int)
- intget_collision_mask()
intget_collision_mask()
The physics layers this CSG shape scans for collisions. Only effective ifuse_collisionistrue. SeeCollision layers and masksin the documentation for more information.
floatcollision_priority=1.0🔗
- voidset_collision_priority(value:float)
voidset_collision_priority(value:float)
- floatget_collision_priority()
floatget_collision_priority()
The priority used to solve colliding when occurring penetration. Only effective ifuse_collisionistrue. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.
Operationoperation=0🔗
- voidset_operation(value:Operation)
voidset_operation(value:Operation)
- Operationget_operation()
Operationget_operation()
The operation that is performed on this shape. This is ignored for the first CSG child node as the operation is between this node and the previous child of this nodes parent.
floatsnap🔗
- voidset_snap(value:float)
voidset_snap(value:float)
- floatget_snap()
floatget_snap()
Deprecated:The CSG library no longer uses snapping.
This property does nothing.
booluse_collision=false🔗
- voidset_use_collision(value:bool)
voidset_use_collision(value:bool)
- boolis_using_collision()
boolis_using_collision()
Adds a collision shape to the physics engine for our CSG shape. This will always act like a static body. Note that the collision shape is still active even if the CSG shape itself is hidden. See alsocollision_maskandcollision_priority.

## Method Descriptions

ConcavePolygonShape3Dbake_collision_shape()🔗
Returns a baked physicsConcavePolygonShape3Dof this node's CSG operation result. Returns an empty shape if the node is not a CSG root node or has no valid geometry.
Performance:If the CSG operation results in a very detailed geometry with many faces physics performance will be very slow. Concave shapes should in general only be used for static level geometry and not with dynamic objects that are moving.
Note:CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to callawaitget_tree().process_framebefore usingbake_collision_shape()inNode._ready()or after changing properties on theCSGShape3D.
ArrayMeshbake_static_mesh()🔗
Returns a baked staticArrayMeshof this node's CSG operation result. Materials from involved CSG nodes are added as extra mesh surfaces. Returns an empty mesh if the node is not a CSG root node or has no valid geometry.
Note:CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty mesh or outdated mesh data, make sure to callawaitget_tree().process_framebefore usingbake_static_mesh()inNode._ready()or after changing properties on theCSGShape3D.
boolget_collision_layer_value(layer_number:int)const🔗
Returns whether or not the specified layer of thecollision_layeris enabled, given alayer_numberbetween 1 and 32.
boolget_collision_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thecollision_maskis enabled, given alayer_numberbetween 1 and 32.
Arrayget_meshes()const🔗
Returns anArraywith two elements, the first is theTransform3Dof this node and the second is the rootMeshof this node. Only works when this node is the root shape.
Note:CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to callawaitget_tree().process_framebefore usingget_meshes()inNode._ready()or after changing properties on theCSGShape3D.
boolis_root_shape()const🔗
Returnstrueif this is a root shape and is thus the object that is rendered.
voidset_collision_layer_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thecollision_layer, given alayer_numberbetween 1 and 32.
voidset_collision_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thecollision_mask, given alayer_numberbetween 1 and 32.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
