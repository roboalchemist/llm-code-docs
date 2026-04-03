# Area2D

# Area2D
Inherits:CollisionObject2D<Node2D<CanvasItem<Node<Object
A region of 2D space that detects otherCollisionObject2Ds entering or exiting it.

## Description
Area2Dis a region of 2D space defined by one or multipleCollisionShape2DorCollisionPolygon2Dchild nodes. It detects when otherCollisionObject2Ds enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).
This node can also locally alter or override physics parameters (gravity, damping) and route audio to custom audio buses.
Note:Areas and bodies created withPhysicsServer2Dmight not interact as expected withArea2Ds, and might not emit signals or track objects correctly.

## Tutorials
- Using Area2D
Using Area2D
- 2D Dodge The Creeps Demo
2D Dodge The Creeps Demo
- 2D Pong Demo
2D Pong Demo
- 2D Platformer Demo
2D Platformer Demo

## Properties

| float | angular_damp | 1.0 |
|---|---|---|
| SpaceOverride | angular_damp_space_override | 0 |
| StringName | audio_bus_name | &"Master" |
| bool | audio_bus_override | false |
| float | gravity | 980.0 |
| Vector2 | gravity_direction | Vector2(0,1) |
| bool | gravity_point | false |
| Vector2 | gravity_point_center | Vector2(0,1) |
| float | gravity_point_unit_distance | 0.0 |
| SpaceOverride | gravity_space_override | 0 |
| float | linear_damp | 0.1 |
| SpaceOverride | linear_damp_space_override | 0 |
| bool | monitorable | true |
| bool | monitoring | true |
| int | priority | 0 |

float
angular_damp
SpaceOverride
angular_damp_space_override
StringName
audio_bus_name
&"Master"
bool
audio_bus_override
false
float
gravity
980.0
Vector2
gravity_direction
Vector2(0,1)
bool
gravity_point
false
Vector2
gravity_point_center
Vector2(0,1)
float
gravity_point_unit_distance
SpaceOverride
gravity_space_override
float
linear_damp
SpaceOverride
linear_damp_space_override
bool
monitorable
true
bool
monitoring
true
priority

## Methods

| Array[Area2D] | get_overlapping_areas()const |
|---|---|
| Array[Node2D] | get_overlapping_bodies()const |
| bool | has_overlapping_areas()const |
| bool | has_overlapping_bodies()const |
| bool | overlaps_area(area:Node)const |
| bool | overlaps_body(body:Node)const |

Array[Area2D]
get_overlapping_areas()const
Array[Node2D]
get_overlapping_bodies()const
bool
has_overlapping_areas()const
bool
has_overlapping_bodies()const
bool
overlaps_area(area:Node)const
bool
overlaps_body(body:Node)const

## Signals
area_entered(area:Area2D)🔗
Emitted when the receivedareaenters this area. Requiresmonitoringto be set totrue.
area_exited(area:Area2D)🔗
Emitted when the receivedareaexits this area. Requiresmonitoringto be set totrue.
area_shape_entered(area_rid:RID, area:Area2D, area_shape_index:int, local_shape_index:int)🔗
Emitted when aShape2Dof the receivedareaenters a shape of this area. Requiresmonitoringto be set totrue.
local_shape_indexandarea_shape_indexcontain indices of the interacting shapes from this area and the other area, respectively.area_ridcontains theRIDof the other area. These values can be used with thePhysicsServer2D.
Example:Get theCollisionShape2Dnode from the shape index:
```
var other_shape_owner = area.shape_find_owner(area_shape_index)
var other_shape_node = area.shape_owner_get_owner(other_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```
area_shape_exited(area_rid:RID, area:Area2D, area_shape_index:int, local_shape_index:int)🔗
Emitted when aShape2Dof the receivedareaexits a shape of this area. Requiresmonitoringto be set totrue.
See alsoarea_shape_entered.
body_entered(body:Node2D)🔗
Emitted when the receivedbodyenters this area.bodycan be aPhysicsBody2Dor aTileMap.TileMaps are detected if theirTileSethas collision shapes configured. Requiresmonitoringto be set totrue.
body_exited(body:Node2D)🔗
Emitted when the receivedbodyexits this area.bodycan be aPhysicsBody2Dor aTileMap.TileMaps are detected if theirTileSethas collision shapes configured. Requiresmonitoringto be set totrue.
body_shape_entered(body_rid:RID, body:Node2D, body_shape_index:int, local_shape_index:int)🔗
Emitted when aShape2Dof the receivedbodyenters a shape of this area.bodycan be aPhysicsBody2Dor aTileMap.TileMaps are detected if theirTileSethas collision shapes configured. Requiresmonitoringto be set totrue.
local_shape_indexandbody_shape_indexcontain indices of the interacting shapes from this area and the interacting body, respectively.body_ridcontains theRIDof the body. These values can be used with thePhysicsServer2D.
Example:Get theCollisionShape2Dnode from the shape index:
```
var body_shape_owner = body.shape_find_owner(body_shape_index)
var body_shape_node = body.shape_owner_get_owner(body_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```
body_shape_exited(body_rid:RID, body:Node2D, body_shape_index:int, local_shape_index:int)🔗
Emitted when aShape2Dof the receivedbodyexits a shape of this area.bodycan be aPhysicsBody2Dor aTileMap.TileMaps are detected if theirTileSethas collision shapes configured. Requiresmonitoringto be set totrue.
See alsobody_shape_entered.

## Enumerations
enumSpaceOverride:🔗
SpaceOverrideSPACE_OVERRIDE_DISABLED=0
This area does not affect gravity/damping.
SpaceOverrideSPACE_OVERRIDE_COMBINE=1
This area adds its gravity/damping values to whatever has been calculated so far (inpriorityorder).
SpaceOverrideSPACE_OVERRIDE_COMBINE_REPLACE=2
This area adds its gravity/damping values to whatever has been calculated so far (inpriorityorder), ignoring any lower priority areas.
SpaceOverrideSPACE_OVERRIDE_REPLACE=3
This area replaces any gravity/damping, even the defaults, ignoring any lower priority areas.
SpaceOverrideSPACE_OVERRIDE_REPLACE_COMBINE=4
This area replaces any gravity/damping calculated so far (inpriorityorder), but keeps calculating the rest of the areas.

## Property Descriptions
floatangular_damp=1.0🔗
- voidset_angular_damp(value:float)
voidset_angular_damp(value:float)
- floatget_angular_damp()
floatget_angular_damp()
The rate at which objects stop spinning in this area. Represents the angular velocity lost per second.
SeeProjectSettings.physics/2d/default_angular_dampfor more details about damping.
SpaceOverrideangular_damp_space_override=0🔗
- voidset_angular_damp_space_override_mode(value:SpaceOverride)
voidset_angular_damp_space_override_mode(value:SpaceOverride)
- SpaceOverrideget_angular_damp_space_override_mode()
SpaceOverrideget_angular_damp_space_override_mode()
Override mode for angular damping calculations within this area.
StringNameaudio_bus_name=&"Master"🔗
- voidset_audio_bus_name(value:StringName)
voidset_audio_bus_name(value:StringName)
- StringNameget_audio_bus_name()
StringNameget_audio_bus_name()
The name of the area's audio bus.
boolaudio_bus_override=false🔗
- voidset_audio_bus_override(value:bool)
voidset_audio_bus_override(value:bool)
- boolis_overriding_audio_bus()
boolis_overriding_audio_bus()
Iftrue, the area's audio bus overrides the default audio bus.
floatgravity=980.0🔗
- voidset_gravity(value:float)
voidset_gravity(value:float)
- floatget_gravity()
floatget_gravity()
The area's gravity intensity (in pixels per second squared). This value multiplies the gravity direction. This is useful to alter the force of gravity without altering its direction.
Vector2gravity_direction=Vector2(0,1)🔗
- voidset_gravity_direction(value:Vector2)
voidset_gravity_direction(value:Vector2)
- Vector2get_gravity_direction()
Vector2get_gravity_direction()
The area's gravity vector (not normalized).
boolgravity_point=false🔗
- voidset_gravity_is_point(value:bool)
voidset_gravity_is_point(value:bool)
- boolis_gravity_a_point()
boolis_gravity_a_point()
Iftrue, gravity is calculated from a point (set viagravity_point_center). See alsogravity_space_override.
Vector2gravity_point_center=Vector2(0,1)🔗
- voidset_gravity_point_center(value:Vector2)
voidset_gravity_point_center(value:Vector2)
- Vector2get_gravity_point_center()
Vector2get_gravity_point_center()
If gravity is a point (seegravity_point), this will be the point of attraction.
floatgravity_point_unit_distance=0.0🔗
- voidset_gravity_point_unit_distance(value:float)
voidset_gravity_point_unit_distance(value:float)
- floatget_gravity_point_unit_distance()
floatget_gravity_point_unit_distance()
The distance at which the gravity strength is equal togravity. For example, on a planet 100 pixels in radius with a surface gravity of 4.0 px/s², set thegravityto 4.0 and the unit distance to 100.0. The gravity will have falloff according to the inverse square law, so in the example, at 200 pixels from the center the gravity will be 1.0 px/s² (twice the distance, 1/4th the gravity), at 50 pixels it will be 16.0 px/s² (half the distance, 4x the gravity), and so on.
The above is true only when the unit distance is a positive number. When this is set to 0.0, the gravity will be constant regardless of distance.
SpaceOverridegravity_space_override=0🔗
- voidset_gravity_space_override_mode(value:SpaceOverride)
voidset_gravity_space_override_mode(value:SpaceOverride)
- SpaceOverrideget_gravity_space_override_mode()
SpaceOverrideget_gravity_space_override_mode()
Override mode for gravity calculations within this area.
floatlinear_damp=0.1🔗
- voidset_linear_damp(value:float)
voidset_linear_damp(value:float)
- floatget_linear_damp()
floatget_linear_damp()
The rate at which objects stop moving in this area. Represents the linear velocity lost per second.
SeeProjectSettings.physics/2d/default_linear_dampfor more details about damping.
SpaceOverridelinear_damp_space_override=0🔗
- voidset_linear_damp_space_override_mode(value:SpaceOverride)
voidset_linear_damp_space_override_mode(value:SpaceOverride)
- SpaceOverrideget_linear_damp_space_override_mode()
SpaceOverrideget_linear_damp_space_override_mode()
Override mode for linear damping calculations within this area.
boolmonitorable=true🔗
- voidset_monitorable(value:bool)
voidset_monitorable(value:bool)
- boolis_monitorable()
boolis_monitorable()
Iftrue, other monitoring areas can detect this area.
boolmonitoring=true🔗
- voidset_monitoring(value:bool)
voidset_monitoring(value:bool)
- boolis_monitoring()
boolis_monitoring()
Iftrue, the area detects bodies or areas entering and exiting it.
intpriority=0🔗
- voidset_priority(value:int)
voidset_priority(value:int)
- intget_priority()
intget_priority()
The area's priority. Higher priority areas are processed first. TheWorld2D's physics is always processed last, after all areas.

## Method Descriptions
Array[Area2D]get_overlapping_areas()const🔗
Returns a list of intersectingArea2Ds. The overlapping area'sCollisionObject2D.collision_layermust be part of this area'sCollisionObject2D.collision_maskin order to be detected.
For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.
Array[Node2D]get_overlapping_bodies()const🔗
Returns a list of intersectingPhysicsBody2Ds andTileMaps. The overlapping body'sCollisionObject2D.collision_layermust be part of this area'sCollisionObject2D.collision_maskin order to be detected.
For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.
boolhas_overlapping_areas()const🔗
Returnstrueif intersecting anyArea2Ds, otherwise returnsfalse. The overlapping area'sCollisionObject2D.collision_layermust be part of this area'sCollisionObject2D.collision_maskin order to be detected.
For performance reasons (collisions are all processed at the same time) the list of overlapping areas is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.
boolhas_overlapping_bodies()const🔗
Returnstrueif intersecting anyPhysicsBody2Ds orTileMaps, otherwise returnsfalse. The overlapping body'sCollisionObject2D.collision_layermust be part of this area'sCollisionObject2D.collision_maskin order to be detected.
For performance reasons (collisions are all processed at the same time) the list of overlapping bodies is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.
booloverlaps_area(area:Node)const🔗
Returnstrueif the givenArea2Dintersects or overlaps thisArea2D,falseotherwise.
Note:The result of this test is not immediate after moving objects. For performance, the list of overlaps is updated once per frame and before the physics step. Consider using signals instead.
booloverlaps_body(body:Node)const🔗
Returnstrueif the given physics body intersects or overlaps thisArea2D,falseotherwise.
Note:The result of this test is not immediate after moving objects. For performance, list of overlaps is updated once per frame and before the physics step. Consider using signals instead.
Thebodyargument can either be aPhysicsBody2Dor aTileMapinstance. While TileMaps are not physics bodies themselves, they register their tiles with collision shapes as a virtual physics body.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.