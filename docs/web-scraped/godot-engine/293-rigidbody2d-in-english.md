# RigidBody2D in English

# RigidBody2D
Inherits:PhysicsBody2D<CollisionObject2D<Node2D<CanvasItem<Node<Object
Inherited By:PhysicalBone2D
A 2D physics body that is moved by a physics simulation.

## Description
RigidBody2Dimplements full 2D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.
The body's behavior can be adjusted vialock_rotation,freeze, andfreeze_mode. By changing various properties of the object, such asmass, you can control how the physics simulation acts on it.
A rigid body will always maintain its shape and size, even when forces are applied to it. It is useful for objects that can be interacted with in an environment, such as a tree that can be knocked over or a stack of crates that can be pushed around.
If you need to directly affect the body, prefer_integrate_forces()as it allows you to directly access the physics state.
If you need to override the default physics behavior, you can write a custom force integration function. Seecustom_integrator.
Note:Changing the 2D transform orlinear_velocityof aRigidBody2Dvery often may lead to some unpredictable behaviors. This also happens when aRigidBody2Dis the descendant of a constantly moving node, like anotherRigidBody2D, as that will cause its global transform to be set whenever its ancestor moves.

## Tutorials
- Physics introduction
Physics introduction
- Troubleshooting physics issues
Troubleshooting physics issues
- 2D Physics Platformer Demo
2D Physics Platformer Demo
- Instancing Demo
Instancing Demo

## Properties

| float | angular_damp | 0.0 |
|---|---|---|
| DampMode | angular_damp_mode | 0 |
| float | angular_velocity | 0.0 |
| bool | can_sleep | true |
| Vector2 | center_of_mass | Vector2(0,0) |
| CenterOfMassMode | center_of_mass_mode | 0 |
| Vector2 | constant_force | Vector2(0,0) |
| float | constant_torque | 0.0 |
| bool | contact_monitor | false |
| CCDMode | continuous_cd | 0 |
| bool | custom_integrator | false |
| bool | freeze | false |
| FreezeMode | freeze_mode | 0 |
| float | gravity_scale | 1.0 |
| float | inertia | 0.0 |
| float | linear_damp | 0.0 |
| DampMode | linear_damp_mode | 0 |
| Vector2 | linear_velocity | Vector2(0,0) |
| bool | lock_rotation | false |
| float | mass | 1.0 |
| int | max_contacts_reported | 0 |
| PhysicsMaterial | physics_material_override |  |
| bool | sleeping | false |

float
angular_damp
DampMode
angular_damp_mode
float
angular_velocity
bool
can_sleep
true
Vector2
center_of_mass
Vector2(0,0)
CenterOfMassMode
center_of_mass_mode
Vector2
constant_force
Vector2(0,0)
float
constant_torque
bool
contact_monitor
false
CCDMode
continuous_cd
bool
custom_integrator
false
bool
freeze
false
FreezeMode
freeze_mode
float
gravity_scale
float
inertia
float
linear_damp
DampMode
linear_damp_mode
Vector2
linear_velocity
Vector2(0,0)
bool
lock_rotation
false
float
mass
max_contacts_reported
PhysicsMaterial
physics_material_override
bool
sleeping
false

## Methods

| void | _integrate_forces(state:PhysicsDirectBodyState2D)virtual |
|---|---|
| void | add_constant_central_force(force:Vector2) |
| void | add_constant_force(force:Vector2, position:Vector2= Vector2(0, 0)) |
| void | add_constant_torque(torque:float) |
| void | apply_central_force(force:Vector2) |
| void | apply_central_impulse(impulse:Vector2= Vector2(0, 0)) |
| void | apply_force(force:Vector2, position:Vector2= Vector2(0, 0)) |
| void | apply_impulse(impulse:Vector2, position:Vector2= Vector2(0, 0)) |
| void | apply_torque(torque:float) |
| void | apply_torque_impulse(torque:float) |
| Array[Node2D] | get_colliding_bodies()const |
| int | get_contact_count()const |
| void | set_axis_velocity(axis_velocity:Vector2) |

void
_integrate_forces(state:PhysicsDirectBodyState2D)virtual
void
add_constant_central_force(force:Vector2)
void
add_constant_force(force:Vector2, position:Vector2= Vector2(0, 0))
void
add_constant_torque(torque:float)
void
apply_central_force(force:Vector2)
void
apply_central_impulse(impulse:Vector2= Vector2(0, 0))
void
apply_force(force:Vector2, position:Vector2= Vector2(0, 0))
void
apply_impulse(impulse:Vector2, position:Vector2= Vector2(0, 0))
void
apply_torque(torque:float)
void
apply_torque_impulse(torque:float)
Array[Node2D]
get_colliding_bodies()const
get_contact_count()const
void
set_axis_velocity(axis_velocity:Vector2)

## Signals
body_entered(body:Node)🔗
Emitted when a collision with anotherPhysicsBody2DorTileMapoccurs. Requirescontact_monitorto be set totrueandmax_contacts_reportedto be set high enough to detect all the collisions.TileMaps are detected if theTileSethas CollisionShape2Ds.
bodytheNode, if it exists in the tree, of the otherPhysicsBody2DorTileMap.
body_exited(body:Node)🔗
Emitted when the collision with anotherPhysicsBody2DorTileMapends. Requirescontact_monitorto be set totrueandmax_contacts_reportedto be set high enough to detect all the collisions.TileMaps are detected if theTileSethas CollisionShape2Ds.
bodytheNode, if it exists in the tree, of the otherPhysicsBody2DorTileMap.
body_shape_entered(body_rid:RID, body:Node, body_shape_index:int, local_shape_index:int)🔗
Emitted when one of this RigidBody2D'sShape2Ds collides with anotherPhysicsBody2DorTileMap'sShape2Ds. Requirescontact_monitorto be set totrueandmax_contacts_reportedto be set high enough to detect all the collisions.TileMaps are detected if theTileSethas CollisionShape2Ds.
body_ridtheRIDof the otherPhysicsBody2DorTileSet'sCollisionObject2Dused by thePhysicsServer2D.
bodytheNode, if it exists in the tree, of the otherPhysicsBody2DorTileMap.
body_shape_indexthe index of theShape2Dof the otherPhysicsBody2DorTileMapused by thePhysicsServer2D. Get theCollisionShape2Dnode withbody.shape_owner_get_owner(body.shape_find_owner(body_shape_index)).
local_shape_indexthe index of theShape2Dof this RigidBody2D used by thePhysicsServer2D. Get theCollisionShape2Dnode withself.shape_owner_get_owner(self.shape_find_owner(local_shape_index)).
body_shape_exited(body_rid:RID, body:Node, body_shape_index:int, local_shape_index:int)🔗
Emitted when the collision between one of this RigidBody2D'sShape2Ds and anotherPhysicsBody2DorTileMap'sShape2Ds ends. Requirescontact_monitorto be set totrueandmax_contacts_reportedto be set high enough to detect all the collisions.TileMaps are detected if theTileSethas CollisionShape2Ds.
body_ridtheRIDof the otherPhysicsBody2DorTileSet'sCollisionObject2Dused by thePhysicsServer2D.
bodytheNode, if it exists in the tree, of the otherPhysicsBody2DorTileMap.
body_shape_indexthe index of theShape2Dof the otherPhysicsBody2DorTileMapused by thePhysicsServer2D. Get theCollisionShape2Dnode withbody.shape_owner_get_owner(body.shape_find_owner(body_shape_index)).
local_shape_indexthe index of theShape2Dof this RigidBody2D used by thePhysicsServer2D. Get theCollisionShape2Dnode withself.shape_owner_get_owner(self.shape_find_owner(local_shape_index)).
sleeping_state_changed()🔗
Emitted when the physics engine changes the body's sleeping state.
Note:Changing the valuesleepingwill not trigger this signal. It is only emitted if the sleeping state is changed by the physics engine oremit_signal("sleeping_state_changed")is used.

## Enumerations
enumFreezeMode:🔗
FreezeModeFREEZE_MODE_STATIC=0
Static body freeze mode (default). The body is not affected by gravity and forces. It can be only moved by user code and doesn't collide with other bodies along its path.
FreezeModeFREEZE_MODE_KINEMATIC=1
Kinematic body freeze mode. Similar toFREEZE_MODE_STATIC, but collides with other bodies along its path when moved. Useful for a frozen body that needs to be animated.
enumCenterOfMassMode:🔗
CenterOfMassModeCENTER_OF_MASS_MODE_AUTO=0
In this mode, the body's center of mass is calculated automatically based on its shapes. This assumes that the shapes' origins are also their center of mass.
CenterOfMassModeCENTER_OF_MASS_MODE_CUSTOM=1
In this mode, the body's center of mass is set throughcenter_of_mass. Defaults to the body's origin position.
enumDampMode:🔗
DampModeDAMP_MODE_COMBINE=0
In this mode, the body's damping value is added to any value set in areas or the default value.
DampModeDAMP_MODE_REPLACE=1
In this mode, the body's damping value replaces any value set in areas or the default value.
enumCCDMode:🔗
CCDModeCCD_MODE_DISABLED=0
Continuous collision detection disabled. This is the fastest way to detect body collisions, but can miss small, fast-moving objects.
CCDModeCCD_MODE_CAST_RAY=1
Continuous collision detection enabled using raycasting. This is faster than shapecasting but less precise.
CCDModeCCD_MODE_CAST_SHAPE=2
Continuous collision detection enabled using shapecasting. This is the slowest CCD method and the most precise.

## Property Descriptions
floatangular_damp=0.0🔗
- voidset_angular_damp(value:float)
voidset_angular_damp(value:float)
- floatget_angular_damp()
floatget_angular_damp()
Damps the body's rotation. By default, the body will use theProjectSettings.physics/2d/default_angular_dampsetting or any value override set by anArea2Dthe body is in. Depending onangular_damp_mode, you can setangular_dampto be added to or to replace the body's damping value.
SeeProjectSettings.physics/2d/default_angular_dampfor more details about damping.
DampModeangular_damp_mode=0🔗
- voidset_angular_damp_mode(value:DampMode)
voidset_angular_damp_mode(value:DampMode)
- DampModeget_angular_damp_mode()
DampModeget_angular_damp_mode()
Defines howangular_dampis applied.
floatangular_velocity=0.0🔗
- voidset_angular_velocity(value:float)
voidset_angular_velocity(value:float)
- floatget_angular_velocity()
floatget_angular_velocity()
The body's rotational velocity inradiansper second.
boolcan_sleep=true🔗
- voidset_can_sleep(value:bool)
voidset_can_sleep(value:bool)
- boolis_able_to_sleep()
boolis_able_to_sleep()
Iftrue, the body can enter sleep mode when there is no movement. Seesleeping.
Vector2center_of_mass=Vector2(0,0)🔗
- voidset_center_of_mass(value:Vector2)
voidset_center_of_mass(value:Vector2)
- Vector2get_center_of_mass()
Vector2get_center_of_mass()
The body's custom center of mass, relative to the body's origin position, whencenter_of_mass_modeis set toCENTER_OF_MASS_MODE_CUSTOM. This is the balanced point of the body, where applied forces only cause linear acceleration. Applying forces outside of the center of mass causes angular acceleration.
Whencenter_of_mass_modeis set toCENTER_OF_MASS_MODE_AUTO(default value), the center of mass is automatically determined, but this does not update the value ofcenter_of_mass.
CenterOfMassModecenter_of_mass_mode=0🔗
- voidset_center_of_mass_mode(value:CenterOfMassMode)
voidset_center_of_mass_mode(value:CenterOfMassMode)
- CenterOfMassModeget_center_of_mass_mode()
CenterOfMassModeget_center_of_mass_mode()
Defines the way the body's center of mass is set.
Vector2constant_force=Vector2(0,0)🔗
- voidset_constant_force(value:Vector2)
voidset_constant_force(value:Vector2)
- Vector2get_constant_force()
Vector2get_constant_force()
The body's total constant positional forces applied during each physics update.
Seeadd_constant_force()andadd_constant_central_force().
floatconstant_torque=0.0🔗
- voidset_constant_torque(value:float)
voidset_constant_torque(value:float)
- floatget_constant_torque()
floatget_constant_torque()
The body's total constant rotational forces applied during each physics update.
Seeadd_constant_torque().
boolcontact_monitor=false🔗
- voidset_contact_monitor(value:bool)
voidset_contact_monitor(value:bool)
- boolis_contact_monitor_enabled()
boolis_contact_monitor_enabled()
Iftrue, the RigidBody2D will emit signals when it collides with another body.
Note:By default the maximum contacts reported is set to 0, meaning nothing will be recorded, seemax_contacts_reported.
CCDModecontinuous_cd=0🔗
- voidset_continuous_collision_detection_mode(value:CCDMode)
voidset_continuous_collision_detection_mode(value:CCDMode)
- CCDModeget_continuous_collision_detection_mode()
CCDModeget_continuous_collision_detection_mode()
Continuous collision detection mode.
Continuous collision detection tries to predict where a moving body will collide instead of moving it and correcting its movement after collision. Continuous collision detection is slower, but more precise and misses fewer collisions with small, fast-moving objects. Raycasting and shapecasting methods are available.
boolcustom_integrator=false🔗
- voidset_use_custom_integrator(value:bool)
voidset_use_custom_integrator(value:bool)
- boolis_using_custom_integrator()
boolis_using_custom_integrator()
Iftrue, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the_integrate_forces()method, if that virtual method is overridden.
Setting this property will call the methodPhysicsServer2D.body_set_omit_force_integration()internally.
boolfreeze=false🔗
- voidset_freeze_enabled(value:bool)
voidset_freeze_enabled(value:bool)
- boolis_freeze_enabled()
boolis_freeze_enabled()
Iftrue, the body is frozen. Gravity and forces are not applied anymore.
Seefreeze_modeto set the body's behavior when frozen.
Note:For a body that is always frozen, useStaticBody2DorAnimatableBody2Dinstead.
FreezeModefreeze_mode=0🔗
- voidset_freeze_mode(value:FreezeMode)
voidset_freeze_mode(value:FreezeMode)
- FreezeModeget_freeze_mode()
FreezeModeget_freeze_mode()
The body's freeze mode. Determines the body's behavior whenfreezeistrue.
Note:For a body that is always frozen, useStaticBody2DorAnimatableBody2Dinstead.
floatgravity_scale=1.0🔗
- voidset_gravity_scale(value:float)
voidset_gravity_scale(value:float)
- floatget_gravity_scale()
floatget_gravity_scale()
Multiplies the gravity applied to the body. The body's gravity is calculated from theProjectSettings.physics/2d/default_gravityproject setting and/or any additional gravity vector applied byArea2Ds.
floatinertia=0.0🔗
- voidset_inertia(value:float)
voidset_inertia(value:float)
- floatget_inertia()
floatget_inertia()
The body's moment of inertia. This is like mass, but for rotation: it determines how much torque it takes to rotate the body. The moment of inertia is usually computed automatically from the mass and the shapes, but this property allows you to set a custom value.
If set to0, inertia is automatically computed (default value).
Note:This value does not change when inertia is automatically computed. UsePhysicsServer2Dto get the computed inertia.
```
@onready var ball = $Ball

func get_ball_inertia():
    return 1.0 / PhysicsServer2D.body_get_direct_state(ball.get_rid()).inverse_inertia
```
```
private RigidBody2D _ball;

public override void _Ready()
{
    _ball = GetNode<RigidBody2D>("Ball");
}

private float GetBallInertia()
{
    return 1.0f / PhysicsServer2D.BodyGetDirectState(_ball.GetRid()).InverseInertia;
}
```
floatlinear_damp=0.0🔗
- voidset_linear_damp(value:float)
voidset_linear_damp(value:float)
- floatget_linear_damp()
floatget_linear_damp()
Damps the body's movement. By default, the body will use theProjectSettings.physics/2d/default_linear_dampsetting or any value override set by anArea2Dthe body is in. Depending onlinear_damp_mode, you can setlinear_dampto be added to or to replace the body's damping value.
SeeProjectSettings.physics/2d/default_linear_dampfor more details about damping.
DampModelinear_damp_mode=0🔗
- voidset_linear_damp_mode(value:DampMode)
voidset_linear_damp_mode(value:DampMode)
- DampModeget_linear_damp_mode()
DampModeget_linear_damp_mode()
Defines howlinear_dampis applied.
Vector2linear_velocity=Vector2(0,0)🔗
- voidset_linear_velocity(value:Vector2)
voidset_linear_velocity(value:Vector2)
- Vector2get_linear_velocity()
Vector2get_linear_velocity()
The body's linear velocity in pixels per second. Can be used sporadically, butdon't set this every frame, because physics may run in another thread and runs at a different granularity. Use_integrate_forces()as your process loop for precise control of the body state.
boollock_rotation=false🔗
- voidset_lock_rotation_enabled(value:bool)
voidset_lock_rotation_enabled(value:bool)
- boolis_lock_rotation_enabled()
boolis_lock_rotation_enabled()
Iftrue, the body cannot rotate. Gravity and forces only apply linear movement.
floatmass=1.0🔗
- voidset_mass(value:float)
voidset_mass(value:float)
- floatget_mass()
floatget_mass()
The body's mass.
intmax_contacts_reported=0🔗
- voidset_max_contacts_reported(value:int)
voidset_max_contacts_reported(value:int)
- intget_max_contacts_reported()
intget_max_contacts_reported()
The maximum number of contacts that will be recorded. Requires a value greater than 0 andcontact_monitorto be set totrueto start to register contacts. Useget_contact_count()to retrieve the count orget_colliding_bodies()to retrieve bodies that have been collided with.
Note:The number of contacts is different from the number of collisions. Collisions between parallel edges will result in two contacts (one at each end), and collisions between parallel faces will result in four contacts (one at each corner).
PhysicsMaterialphysics_material_override🔗
- voidset_physics_material_override(value:PhysicsMaterial)
voidset_physics_material_override(value:PhysicsMaterial)
- PhysicsMaterialget_physics_material_override()
PhysicsMaterialget_physics_material_override()
The physics material override for the body.
If a material is assigned to this property, it will be used instead of any other physics material, such as an inherited one.
boolsleeping=false🔗
- voidset_sleeping(value:bool)
voidset_sleeping(value:bool)
- boolis_sleeping()
boolis_sleeping()
Iftrue, the body will not move and will not calculate forces until woken up by another body through, for example, a collision, or by using theapply_impulse()orapply_force()methods.

## Method Descriptions
void_integrate_forces(state:PhysicsDirectBodyState2D)virtual🔗
Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but thecustom_integratorproperty allows you to disable the standard force integration and do fully custom force integration for a body.
voidadd_constant_central_force(force:Vector2)🔗
Adds a constant directional force without affecting rotation that keeps being applied over time until cleared withconstant_force=Vector2(0,0).
This is equivalent to usingadd_constant_force()at the body's center of mass.
voidadd_constant_force(force:Vector2, position:Vector2= Vector2(0, 0))🔗
Adds a constant positioned force to the body that keeps being applied over time until cleared withconstant_force=Vector2(0,0).
positionis the offset from the body origin in global coordinates.
voidadd_constant_torque(torque:float)🔗
Adds a constant rotational force without affecting position that keeps being applied over time until cleared withconstant_torque=0.
voidapply_central_force(force:Vector2)🔗
Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.
This is equivalent to usingapply_force()at the body's center of mass.
voidapply_central_impulse(impulse:Vector2= Vector2(0, 0))🔗
Applies a directional impulse without affecting rotation.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
This is equivalent to usingapply_impulse()at the body's center of mass.
voidapply_force(force:Vector2, position:Vector2= Vector2(0, 0))🔗
Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.
positionis the offset from the body origin in global coordinates.
voidapply_impulse(impulse:Vector2, position:Vector2= Vector2(0, 0))🔗
Applies a positioned impulse to the body.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
positionis the offset from the body origin in global coordinates.
voidapply_torque(torque:float)🔗
Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.
Note:inertiais required for this to work. To haveinertia, an activeCollisionShape2Dmust be a child of the node, or you can manually setinertia.
voidapply_torque_impulse(torque:float)🔗
Applies a rotational impulse to the body without affecting the position.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
Note:inertiais required for this to work. To haveinertia, an activeCollisionShape2Dmust be a child of the node, or you can manually setinertia.
Array[Node2D]get_colliding_bodies()const🔗
Returns a list of the bodies colliding with this one. Requirescontact_monitorto be set totrueandmax_contacts_reportedto be set high enough to detect all the collisions.
Note:The result of this test is not immediate after moving objects. For performance, list of collisions is updated once per frame and before the physics step. Consider using signals instead.
intget_contact_count()const🔗
Returns the number of contacts this body has with other bodies. By default, this returns 0 unless bodies are configured to monitor contacts (seecontact_monitor).
Note:To retrieve the colliding bodies, useget_colliding_bodies().
voidset_axis_velocity(axis_velocity:Vector2)🔗
Sets the body's velocity on the given axis. The velocity in the given vector axis will be set as the given vector length. This is useful for jumping behavior.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.