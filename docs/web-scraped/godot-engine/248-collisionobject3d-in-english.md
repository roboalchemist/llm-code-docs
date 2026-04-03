# CollisionObject3D in English

# CollisionObject3D

Inherits:Node3D<Node<Object
Inherited By:Area3D,PhysicsBody3D
Abstract base class for 3D physics objects.

## Description

Abstract base class for 3D physics objects.CollisionObject3Dcan hold any number ofShape3Ds for collision. Each shape must be assigned to ashape owner. Shape owners are not nodes and do not appear in the editor, but are accessible through code using theshape_owner_*methods.
Warning:With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

## Properties

| int | collision_layer | 1 |
|---|---|---|
| int | collision_mask | 1 |
| float | collision_priority | 1.0 |
| DisableMode | disable_mode | 0 |
| bool | input_capture_on_drag | false |
| bool | input_ray_pickable | true |

collision_layer
collision_mask
float
collision_priority
DisableMode
disable_mode
bool
input_capture_on_drag
false
bool
input_ray_pickable
true

## Methods

| void | _input_event(camera:Camera3D, event:InputEvent, event_position:Vector3, normal:Vector3, shape_idx:int)virtual |
|---|---|
| void | _mouse_enter()virtual |
| void | _mouse_exit()virtual |
| int | create_shape_owner(owner:Object) |
| bool | get_collision_layer_value(layer_number:int)const |
| bool | get_collision_mask_value(layer_number:int)const |
| RID | get_rid()const |
| PackedInt32Array | get_shape_owners() |
| bool | is_shape_owner_disabled(owner_id:int)const |
| void | remove_shape_owner(owner_id:int) |
| void | set_collision_layer_value(layer_number:int, value:bool) |
| void | set_collision_mask_value(layer_number:int, value:bool) |
| int | shape_find_owner(shape_index:int)const |
| void | shape_owner_add_shape(owner_id:int, shape:Shape3D) |
| void | shape_owner_clear_shapes(owner_id:int) |
| Object | shape_owner_get_owner(owner_id:int)const |
| Shape3D | shape_owner_get_shape(owner_id:int, shape_id:int)const |
| int | shape_owner_get_shape_count(owner_id:int)const |
| int | shape_owner_get_shape_index(owner_id:int, shape_id:int)const |
| Transform3D | shape_owner_get_transform(owner_id:int)const |
| void | shape_owner_remove_shape(owner_id:int, shape_id:int) |
| void | shape_owner_set_disabled(owner_id:int, disabled:bool) |
| void | shape_owner_set_transform(owner_id:int, transform:Transform3D) |

void
_input_event(camera:Camera3D, event:InputEvent, event_position:Vector3, normal:Vector3, shape_idx:int)virtual
void
_mouse_enter()virtual
void
_mouse_exit()virtual
create_shape_owner(owner:Object)
bool
get_collision_layer_value(layer_number:int)const
bool
get_collision_mask_value(layer_number:int)const
get_rid()const
PackedInt32Array
get_shape_owners()
bool
is_shape_owner_disabled(owner_id:int)const
void
remove_shape_owner(owner_id:int)
void
set_collision_layer_value(layer_number:int, value:bool)
void
set_collision_mask_value(layer_number:int, value:bool)
shape_find_owner(shape_index:int)const
void
shape_owner_add_shape(owner_id:int, shape:Shape3D)
void
shape_owner_clear_shapes(owner_id:int)
Object
shape_owner_get_owner(owner_id:int)const
Shape3D
shape_owner_get_shape(owner_id:int, shape_id:int)const
shape_owner_get_shape_count(owner_id:int)const
shape_owner_get_shape_index(owner_id:int, shape_id:int)const
Transform3D
shape_owner_get_transform(owner_id:int)const
void
shape_owner_remove_shape(owner_id:int, shape_id:int)
void
shape_owner_set_disabled(owner_id:int, disabled:bool)
void
shape_owner_set_transform(owner_id:int, transform:Transform3D)

## Signals

input_event(camera:Node, event:InputEvent, event_position:Vector3, normal:Vector3, shape_idx:int)🔗
Emitted when the object receives an unhandledInputEvent.event_positionis the location in world space of the mouse pointer on the surface of the shape with indexshape_idxandnormalis the normal vector of the surface at that point.
mouse_entered()🔗
Emitted when the mouse pointer enters any of this object's shapes. Requiresinput_ray_pickableto betrueand at least onecollision_layerbit to be set.
Note:Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and theCollisionObject3D's area is small. This signal may also not be emitted if anotherCollisionObject3Dis overlapping theCollisionObject3Din question.
mouse_exited()🔗
Emitted when the mouse pointer exits all this object's shapes. Requiresinput_ray_pickableto betrueand at least onecollision_layerbit to be set.
Note:Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and theCollisionObject3D's area is small. This signal may also not be emitted if anotherCollisionObject3Dis overlapping theCollisionObject3Din question.

## Enumerations

enumDisableMode:🔗
DisableModeDISABLE_MODE_REMOVE=0
WhenNode.process_modeis set toNode.PROCESS_MODE_DISABLED, remove from the physics simulation to stop all physics interactions with thisCollisionObject3D.
Automatically re-added to the physics simulation when theNodeis processed again.
DisableModeDISABLE_MODE_MAKE_STATIC=1
WhenNode.process_modeis set toNode.PROCESS_MODE_DISABLED, make the body static. Doesn't affectArea3D.PhysicsBody3Dcan't be affected by forces or other bodies while static.
Automatically setPhysicsBody3Dback to its original mode when theNodeis processed again.
DisableModeDISABLE_MODE_KEEP_ACTIVE=2
WhenNode.process_modeis set toNode.PROCESS_MODE_DISABLED, do not affect the physics simulation.

## Property Descriptions

intcollision_layer=1🔗

- voidset_collision_layer(value:int)
voidset_collision_layer(value:int)
- intget_collision_layer()
intget_collision_layer()
The physics layers this CollisionObject3Dis in. Collision objects can exist in one or more of 32 different layers. See alsocollision_mask.
Note:Object A can detect a contact with object B only if object B is in any of the layers that object A scans. SeeCollision layers and masksin the documentation for more information.
intcollision_mask=1🔗
- voidset_collision_mask(value:int)
voidset_collision_mask(value:int)
- intget_collision_mask()
intget_collision_mask()
The physics layers this CollisionObject3Dscans. Collision objects can scan one or more of 32 different layers. See alsocollision_layer.
Note:Object A can detect a contact with object B only if object B is in any of the layers that object A scans. SeeCollision layers and masksin the documentation for more information.
floatcollision_priority=1.0🔗
- voidset_collision_priority(value:float)
voidset_collision_priority(value:float)
- floatget_collision_priority()
floatget_collision_priority()
The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.
DisableModedisable_mode=0🔗
- voidset_disable_mode(value:DisableMode)
voidset_disable_mode(value:DisableMode)
- DisableModeget_disable_mode()
DisableModeget_disable_mode()
Defines the behavior in physics whenNode.process_modeis set toNode.PROCESS_MODE_DISABLED.
boolinput_capture_on_drag=false🔗
- voidset_capture_input_on_drag(value:bool)
voidset_capture_input_on_drag(value:bool)
- boolget_capture_input_on_drag()
boolget_capture_input_on_drag()
Iftrue, theCollisionObject3Dwill continue to receive input events as the mouse is dragged across its shapes.
boolinput_ray_pickable=true🔗
- voidset_ray_pickable(value:bool)
voidset_ray_pickable(value:bool)
- boolis_ray_pickable()
boolis_ray_pickable()
Iftrue, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least onecollision_layerbit to be set.

## Method Descriptions

void_input_event(camera:Camera3D, event:InputEvent, event_position:Vector3, normal:Vector3, shape_idx:int)virtual🔗
Receives unhandledInputEvents.event_positionis the location in world space of the mouse pointer on the surface of the shape with indexshape_idxandnormalis the normal vector of the surface at that point. Connect to theinput_eventsignal to easily pick up these events.
Note:_input_event()requiresinput_ray_pickableto betrueand at least onecollision_layerbit to be set.
void_mouse_enter()virtual🔗
Called when the mouse pointer enters any of this object's shapes. Requiresinput_ray_pickableto betrueand at least onecollision_layerbit to be set. Note that moving between different shapes within a singleCollisionObject3Dwon't cause this function to be called.
void_mouse_exit()virtual🔗
Called when the mouse pointer exits all this object's shapes. Requiresinput_ray_pickableto betrueand at least onecollision_layerbit to be set. Note that moving between different shapes within a singleCollisionObject3Dwon't cause this function to be called.
intcreate_shape_owner(owner:Object)🔗
Creates a new shape owner for the given object. Returnsowner_idof the new owner for future reference.
boolget_collision_layer_value(layer_number:int)const🔗
Returns whether or not the specified layer of thecollision_layeris enabled, given alayer_numberbetween 1 and 32.
boolget_collision_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thecollision_maskis enabled, given alayer_numberbetween 1 and 32.
RIDget_rid()const🔗
Returns the object'sRID.
PackedInt32Arrayget_shape_owners()🔗
Returns anArrayofowner_ididentifiers. You can use these ids in other methods that takeowner_idas an argument.
boolis_shape_owner_disabled(owner_id:int)const🔗
Iftrue, the shape owner and its shapes are disabled.
voidremove_shape_owner(owner_id:int)🔗
Removes the given shape owner.
voidset_collision_layer_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thecollision_layer, given alayer_numberbetween 1 and 32.
voidset_collision_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thecollision_mask, given alayer_numberbetween 1 and 32.
intshape_find_owner(shape_index:int)const🔗
Returns theowner_idof the given shape.
voidshape_owner_add_shape(owner_id:int, shape:Shape3D)🔗
Adds aShape3Dto the shape owner.
voidshape_owner_clear_shapes(owner_id:int)🔗
Removes all shapes from the shape owner.
Objectshape_owner_get_owner(owner_id:int)const🔗
Returns the parent object of the given shape owner.
Shape3Dshape_owner_get_shape(owner_id:int, shape_id:int)const🔗
Returns theShape3Dwith the given ID from the given shape owner.
intshape_owner_get_shape_count(owner_id:int)const🔗
Returns the number of shapes the given shape owner contains.
intshape_owner_get_shape_index(owner_id:int, shape_id:int)const🔗
Returns the child index of theShape3Dwith the given ID from the given shape owner.
Transform3Dshape_owner_get_transform(owner_id:int)const🔗
Returns the shape owner'sTransform3D.
voidshape_owner_remove_shape(owner_id:int, shape_id:int)🔗
Removes a shape from the given shape owner.
voidshape_owner_set_disabled(owner_id:int, disabled:bool)🔗
Iftrue, disables the given shape owner.
voidshape_owner_set_transform(owner_id:int, transform:Transform3D)🔗
Sets theTransform3Dof the given shape owner.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
