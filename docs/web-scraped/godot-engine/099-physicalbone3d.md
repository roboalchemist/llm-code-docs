# PhysicalBone3D

# PhysicalBone3D

Inherits:PhysicsBody3D<CollisionObject3D<Node3D<Node<Object
A physics body used to make bones in aSkeleton3Dreact to physics.

## Description

ThePhysicalBone3Dnode is a physics body that can be used to make bones in aSkeleton3Dreact to physics.
Note:In order to detect physical bones with raycasts, theSkeletonModifier3D.activeproperty of the parentPhysicalBoneSimulator3Dmust betrueand theSkeleton3D's bone must be assigned toPhysicalBone3Dcorrectly; it means thatget_bone_id()should return a valid id (>=0).

## Tutorials

- Ragdoll System
Ragdoll System

## Properties

| float | angular_damp | 0.0 |
|---|---|---|
| DampMode | angular_damp_mode | 0 |
| Vector3 | angular_velocity | Vector3(0,0,0) |
| Transform3D | body_offset | Transform3D(1,0,0,0,1,0,0,0,1,0,0,0) |
| float | bounce | 0.0 |
| bool | can_sleep | true |
| bool | custom_integrator | false |
| float | friction | 1.0 |
| float | gravity_scale | 1.0 |
| Transform3D | joint_offset | Transform3D(1,0,0,0,1,0,0,0,1,0,0,0) |
| Vector3 | joint_rotation | Vector3(0,0,0) |
| JointType | joint_type | 0 |
| float | linear_damp | 0.0 |
| DampMode | linear_damp_mode | 0 |
| Vector3 | linear_velocity | Vector3(0,0,0) |
| float | mass | 1.0 |

float
angular_damp
DampMode
angular_damp_mode
Vector3
angular_velocity
Vector3(0,0,0)
Transform3D
body_offset
Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)
float
bounce
bool
can_sleep
true
bool
custom_integrator
false
float
friction
float
gravity_scale
Transform3D
joint_offset
Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)
Vector3
joint_rotation
Vector3(0,0,0)
JointType
joint_type
float
linear_damp
DampMode
linear_damp_mode
Vector3
linear_velocity
Vector3(0,0,0)
float
mass

## Methods

| void | _integrate_forces(state:PhysicsDirectBodyState3D)virtual |
|---|---|
| void | apply_central_impulse(impulse:Vector3) |
| void | apply_impulse(impulse:Vector3, position:Vector3= Vector3(0, 0, 0)) |
| int | get_bone_id()const |
| bool | get_simulate_physics() |
| bool | is_simulating_physics() |

void
_integrate_forces(state:PhysicsDirectBodyState3D)virtual
void
apply_central_impulse(impulse:Vector3)
void
apply_impulse(impulse:Vector3, position:Vector3= Vector3(0, 0, 0))
get_bone_id()const
bool
get_simulate_physics()
bool
is_simulating_physics()

## Enumerations

enumDampMode:🔗
DampModeDAMP_MODE_COMBINE=0
In this mode, the body's damping value is added to any value set in areas or the default value.
DampModeDAMP_MODE_REPLACE=1
In this mode, the body's damping value replaces any value set in areas or the default value.
enumJointType:🔗
JointTypeJOINT_TYPE_NONE=0
No joint is applied to the PhysicsBone3D.
JointTypeJOINT_TYPE_PIN=1
A pin joint is applied to the PhysicsBone3D.
JointTypeJOINT_TYPE_CONE=2
A cone joint is applied to the PhysicsBone3D.
JointTypeJOINT_TYPE_HINGE=3
A hinge joint is applied to the PhysicsBone3D.
JointTypeJOINT_TYPE_SLIDER=4
A slider joint is applied to the PhysicsBone3D.
JointTypeJOINT_TYPE_6DOF=5
A 6 degrees of freedom joint is applied to the PhysicsBone3D.

## Property Descriptions

floatangular_damp=0.0🔗

- voidset_angular_damp(value:float)
voidset_angular_damp(value:float)
- floatget_angular_damp()
floatget_angular_damp()
Damps the body's rotation. By default, the body will use theProjectSettings.physics/3d/default_angular_dampproject setting or any value override set by anArea3Dthe body is in. Depending onangular_damp_mode, you can setangular_dampto be added to or to replace the body's damping value.
SeeProjectSettings.physics/3d/default_angular_dampfor more details about damping.
DampModeangular_damp_mode=0🔗
- voidset_angular_damp_mode(value:DampMode)
voidset_angular_damp_mode(value:DampMode)
- DampModeget_angular_damp_mode()
DampModeget_angular_damp_mode()
Defines howangular_dampis applied.
Vector3angular_velocity=Vector3(0,0,0)🔗
- voidset_angular_velocity(value:Vector3)
voidset_angular_velocity(value:Vector3)
- Vector3get_angular_velocity()
Vector3get_angular_velocity()
The PhysicalBone3D's rotational velocity inradiansper second.
Transform3Dbody_offset=Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)🔗
- voidset_body_offset(value:Transform3D)
voidset_body_offset(value:Transform3D)
- Transform3Dget_body_offset()
Transform3Dget_body_offset()
Sets the body's transform.
floatbounce=0.0🔗
- voidset_bounce(value:float)
voidset_bounce(value:float)
- floatget_bounce()
floatget_bounce()
The body's bounciness. Values range from0(no bounce) to1(full bounciness).
Note:Even withbounceset to1.0, some energy will be lost over time due to linear and angular damping. To have aPhysicalBone3Dthat preserves all its energy over time, setbounceto1.0,linear_damp_modetoDAMP_MODE_REPLACE,linear_dampto0.0,angular_damp_modetoDAMP_MODE_REPLACE, andangular_dampto0.0.
boolcan_sleep=true🔗
- voidset_can_sleep(value:bool)
voidset_can_sleep(value:bool)
- boolis_able_to_sleep()
boolis_able_to_sleep()
Iftrue, the body is deactivated when there is no movement, so it will not take part in the simulation until it is awakened by an external force.
boolcustom_integrator=false🔗
- voidset_use_custom_integrator(value:bool)
voidset_use_custom_integrator(value:bool)
- boolis_using_custom_integrator()
boolis_using_custom_integrator()
Iftrue, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the_integrate_forces()method, if that virtual method is overridden.
Setting this property will call the methodPhysicsServer3D.body_set_omit_force_integration()internally.
floatfriction=1.0🔗
- voidset_friction(value:float)
voidset_friction(value:float)
- floatget_friction()
floatget_friction()
The body's friction, from0(frictionless) to1(max friction).
floatgravity_scale=1.0🔗
- voidset_gravity_scale(value:float)
voidset_gravity_scale(value:float)
- floatget_gravity_scale()
floatget_gravity_scale()
This is multiplied byProjectSettings.physics/3d/default_gravityto produce this body's gravity. For example, a value of1.0will apply normal gravity,2.0will apply double the gravity, and0.5will apply half the gravity to this body.
Transform3Djoint_offset=Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)🔗
- voidset_joint_offset(value:Transform3D)
voidset_joint_offset(value:Transform3D)
- Transform3Dget_joint_offset()
Transform3Dget_joint_offset()
Sets the joint's transform.
Vector3joint_rotation=Vector3(0,0,0)🔗
- voidset_joint_rotation(value:Vector3)
voidset_joint_rotation(value:Vector3)
- Vector3get_joint_rotation()
Vector3get_joint_rotation()
Sets the joint's rotation in radians.
JointTypejoint_type=0🔗
- voidset_joint_type(value:JointType)
voidset_joint_type(value:JointType)
- JointTypeget_joint_type()
JointTypeget_joint_type()
Sets the joint type.
floatlinear_damp=0.0🔗
- voidset_linear_damp(value:float)
voidset_linear_damp(value:float)
- floatget_linear_damp()
floatget_linear_damp()
Damps the body's movement. By default, the body will useProjectSettings.physics/3d/default_linear_dampor any value override set by anArea3Dthe body is in. Depending onlinear_damp_mode,linear_dampmay be added to or replace the body's damping value.
SeeProjectSettings.physics/3d/default_linear_dampfor more details about damping.
DampModelinear_damp_mode=0🔗
- voidset_linear_damp_mode(value:DampMode)
voidset_linear_damp_mode(value:DampMode)
- DampModeget_linear_damp_mode()
DampModeget_linear_damp_mode()
Defines howlinear_dampis applied.
Vector3linear_velocity=Vector3(0,0,0)🔗
- voidset_linear_velocity(value:Vector3)
voidset_linear_velocity(value:Vector3)
- Vector3get_linear_velocity()
Vector3get_linear_velocity()
The body's linear velocity in units per second. Can be used sporadically, butdon't set this every frame, because physics may run in another thread and runs at a different granularity. Use_integrate_forces()as your process loop for precise control of the body state.
floatmass=1.0🔗
- voidset_mass(value:float)
voidset_mass(value:float)
- floatget_mass()
floatget_mass()
The body's mass.

## Method Descriptions

void_integrate_forces(state:PhysicsDirectBodyState3D)virtual🔗
Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but thecustom_integratorproperty allows you to disable the standard force integration and do fully custom force integration for a body.
voidapply_central_impulse(impulse:Vector3)🔗
Applies a directional impulse without affecting rotation.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).
This is equivalent to usingapply_impulse()at the body's center of mass.
voidapply_impulse(impulse:Vector3, position:Vector3= Vector3(0, 0, 0))🔗
Applies a positioned impulse to the PhysicsBone3D.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).
positionis the offset from the PhysicsBone3D origin in global coordinates.
intget_bone_id()const🔗
Returns the unique identifier of the PhysicsBone3D.
boolget_simulate_physics()🔗
Returnstrueif the PhysicsBone3D is allowed to simulate physics.
boolis_simulating_physics()🔗
Returnstrueif the PhysicsBone3D is currently simulating physics.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
