:github_url: hide

> **META**
	:keywords: ragdoll



# PhysicalBone3D

**Inherits:** [PhysicsBody3D<class_PhysicsBody3D>] **<** [CollisionObject3D<class_CollisionObject3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A physics body used to make bones in a [Skeleton3D<class_Skeleton3D>] react to physics.


## Description

The **PhysicalBone3D** node is a physics body that can be used to make bones in a [Skeleton3D<class_Skeleton3D>] react to physics.

\ **Note:** In order to detect physical bones with raycasts, the [SkeletonModifier3D.active<class_SkeletonModifier3D_property_active>] property of the parent [PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>] must be `true` and the [Skeleton3D<class_Skeleton3D>]'s bone must be assigned to **PhysicalBone3D** correctly; it means that [get_bone_id()<class_PhysicalBone3D_method_get_bone_id>] should return a valid id (`>= 0`).


## Tutorials

- [../tutorials/physics/ragdoll_system](Ragdoll System .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`angular_damp<class_PhysicalBone3D_property_angular_damp>`           | ``0.0``                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`DampMode<enum_PhysicalBone3D_DampMode>`   | :ref:`angular_damp_mode<class_PhysicalBone3D_property_angular_damp_mode>` | ``0``                                               |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                   | :ref:`angular_velocity<class_PhysicalBone3D_property_angular_velocity>`   | ``Vector3(0, 0, 0)``                                |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`           | :ref:`body_offset<class_PhysicalBone3D_property_body_offset>`             | ``Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`` |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`bounce<class_PhysicalBone3D_property_bounce>`                       | ``0.0``                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`can_sleep<class_PhysicalBone3D_property_can_sleep>`                 | ``true``                                            |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`custom_integrator<class_PhysicalBone3D_property_custom_integrator>` | ``false``                                           |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`friction<class_PhysicalBone3D_property_friction>`                   | ``1.0``                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`gravity_scale<class_PhysicalBone3D_property_gravity_scale>`         | ``1.0``                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`           | :ref:`joint_offset<class_PhysicalBone3D_property_joint_offset>`           | ``Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`` |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                   | :ref:`joint_rotation<class_PhysicalBone3D_property_joint_rotation>`       | ``Vector3(0, 0, 0)``                                |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`JointType<enum_PhysicalBone3D_JointType>` | :ref:`joint_type<class_PhysicalBone3D_property_joint_type>`               | ``0``                                               |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`linear_damp<class_PhysicalBone3D_property_linear_damp>`             | ``0.0``                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`DampMode<enum_PhysicalBone3D_DampMode>`   | :ref:`linear_damp_mode<class_PhysicalBone3D_property_linear_damp_mode>`   | ``0``                                               |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                   | :ref:`linear_velocity<class_PhysicalBone3D_property_linear_velocity>`     | ``Vector3(0, 0, 0)``                                |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`mass<class_PhysicalBone3D_property_mass>`                           | ``1.0``                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------+-----------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`_integrate_forces<class_PhysicalBone3D_private_method__integrate_forces>`\ (\ state\: :ref:`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`\ ) |virtual|    |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`apply_central_impulse<class_PhysicalBone3D_method_apply_central_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`\ )                                              |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`apply_impulse<class_PhysicalBone3D_method_apply_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ ) |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`get_bone_id<class_PhysicalBone3D_method_get_bone_id>`\ (\ ) |const|                                                                                                   |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`get_simulate_physics<class_PhysicalBone3D_method_get_simulate_physics>`\ (\ )                                                                                         |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_simulating_physics<class_PhysicalBone3D_method_is_simulating_physics>`\ (\ )                                                                                       |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **DampMode**: [🔗<enum_PhysicalBone3D_DampMode>]



[DampMode<enum_PhysicalBone3D_DampMode>] **DAMP_MODE_COMBINE** = `0`

In this mode, the body's damping value is added to any value set in areas or the default value.



[DampMode<enum_PhysicalBone3D_DampMode>] **DAMP_MODE_REPLACE** = `1`

In this mode, the body's damping value replaces any value set in areas or the default value.


----



enum **JointType**: [🔗<enum_PhysicalBone3D_JointType>]



[JointType<enum_PhysicalBone3D_JointType>] **JOINT_TYPE_NONE** = `0`

No joint is applied to the PhysicsBone3D.



[JointType<enum_PhysicalBone3D_JointType>] **JOINT_TYPE_PIN** = `1`

A pin joint is applied to the PhysicsBone3D.



[JointType<enum_PhysicalBone3D_JointType>] **JOINT_TYPE_CONE** = `2`

A cone joint is applied to the PhysicsBone3D.



[JointType<enum_PhysicalBone3D_JointType>] **JOINT_TYPE_HINGE** = `3`

A hinge joint is applied to the PhysicsBone3D.



[JointType<enum_PhysicalBone3D_JointType>] **JOINT_TYPE_SLIDER** = `4`

A slider joint is applied to the PhysicsBone3D.



[JointType<enum_PhysicalBone3D_JointType>] **JOINT_TYPE_6DOF** = `5`

A 6 degrees of freedom joint is applied to the PhysicsBone3D.


----


## Property Descriptions



[float<class_float>] **angular_damp** = `0.0` [🔗<class_PhysicalBone3D_property_angular_damp>]


- |void| **set_angular_damp**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_angular_damp**\ (\ )

Damps the body's rotation. By default, the body will use the [ProjectSettings.physics/3d/default_angular_damp<class_ProjectSettings_property_physics/3d/default_angular_damp>] project setting or any value override set by an [Area3D<class_Area3D>] the body is in. Depending on [angular_damp_mode<class_PhysicalBone3D_property_angular_damp_mode>], you can set [angular_damp<class_PhysicalBone3D_property_angular_damp>] to be added to or to replace the body's damping value.

See [ProjectSettings.physics/3d/default_angular_damp<class_ProjectSettings_property_physics/3d/default_angular_damp>] for more details about damping.


----



[DampMode<enum_PhysicalBone3D_DampMode>] **angular_damp_mode** = `0` [🔗<class_PhysicalBone3D_property_angular_damp_mode>]


- |void| **set_angular_damp_mode**\ (\ value\: [DampMode<enum_PhysicalBone3D_DampMode>]\ )
- [DampMode<enum_PhysicalBone3D_DampMode>] **get_angular_damp_mode**\ (\ )

Defines how [angular_damp<class_PhysicalBone3D_property_angular_damp>] is applied.


----



[Vector3<class_Vector3>] **angular_velocity** = `Vector3(0, 0, 0)` [🔗<class_PhysicalBone3D_property_angular_velocity>]


- |void| **set_angular_velocity**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_angular_velocity**\ (\ )

The PhysicalBone3D's rotational velocity in *radians* per second.


----



[Transform3D<class_Transform3D>] **body_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_PhysicalBone3D_property_body_offset>]


- |void| **set_body_offset**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_body_offset**\ (\ )

Sets the body's transform.


----



[float<class_float>] **bounce** = `0.0` [🔗<class_PhysicalBone3D_property_bounce>]


- |void| **set_bounce**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bounce**\ (\ )

The body's bounciness. Values range from `0` (no bounce) to `1` (full bounciness).

\ **Note:** Even with [bounce<class_PhysicalBone3D_property_bounce>] set to `1.0`, some energy will be lost over time due to linear and angular damping. To have a **PhysicalBone3D** that preserves all its energy over time, set [bounce<class_PhysicalBone3D_property_bounce>] to `1.0`, [linear_damp_mode<class_PhysicalBone3D_property_linear_damp_mode>] to [DAMP_MODE_REPLACE<class_PhysicalBone3D_constant_DAMP_MODE_REPLACE>], [linear_damp<class_PhysicalBone3D_property_linear_damp>] to `0.0`, [angular_damp_mode<class_PhysicalBone3D_property_angular_damp_mode>] to [DAMP_MODE_REPLACE<class_PhysicalBone3D_constant_DAMP_MODE_REPLACE>], and [angular_damp<class_PhysicalBone3D_property_angular_damp>] to `0.0`.


----



[bool<class_bool>] **can_sleep** = `true` [🔗<class_PhysicalBone3D_property_can_sleep>]


- |void| **set_can_sleep**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_able_to_sleep**\ (\ )

If `true`, the body is deactivated when there is no movement, so it will not take part in the simulation until it is awakened by an external force.


----



[bool<class_bool>] **custom_integrator** = `false` [🔗<class_PhysicalBone3D_property_custom_integrator>]


- |void| **set_use_custom_integrator**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_custom_integrator**\ (\ )

If `true`, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the [_integrate_forces()<class_PhysicalBone3D_private_method__integrate_forces>] method, if that virtual method is overridden.

Setting this property will call the method [PhysicsServer3D.body_set_omit_force_integration()<class_PhysicsServer3D_method_body_set_omit_force_integration>] internally.


----



[float<class_float>] **friction** = `1.0` [🔗<class_PhysicalBone3D_property_friction>]


- |void| **set_friction**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_friction**\ (\ )

The body's friction, from `0` (frictionless) to `1` (max friction).


----



[float<class_float>] **gravity_scale** = `1.0` [🔗<class_PhysicalBone3D_property_gravity_scale>]


- |void| **set_gravity_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_gravity_scale**\ (\ )

This is multiplied by [ProjectSettings.physics/3d/default_gravity<class_ProjectSettings_property_physics/3d/default_gravity>] to produce this body's gravity. For example, a value of `1.0` will apply normal gravity, `2.0` will apply double the gravity, and `0.5` will apply half the gravity to this body.


----



[Transform3D<class_Transform3D>] **joint_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_PhysicalBone3D_property_joint_offset>]


- |void| **set_joint_offset**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_joint_offset**\ (\ )

Sets the joint's transform.


----



[Vector3<class_Vector3>] **joint_rotation** = `Vector3(0, 0, 0)` [🔗<class_PhysicalBone3D_property_joint_rotation>]


- |void| **set_joint_rotation**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_joint_rotation**\ (\ )

Sets the joint's rotation in radians.


----



[JointType<enum_PhysicalBone3D_JointType>] **joint_type** = `0` [🔗<class_PhysicalBone3D_property_joint_type>]


- |void| **set_joint_type**\ (\ value\: [JointType<enum_PhysicalBone3D_JointType>]\ )
- [JointType<enum_PhysicalBone3D_JointType>] **get_joint_type**\ (\ )

Sets the joint type.


----



[float<class_float>] **linear_damp** = `0.0` [🔗<class_PhysicalBone3D_property_linear_damp>]


- |void| **set_linear_damp**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_linear_damp**\ (\ )

Damps the body's movement. By default, the body will use [ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>] or any value override set by an [Area3D<class_Area3D>] the body is in. Depending on [linear_damp_mode<class_PhysicalBone3D_property_linear_damp_mode>], [linear_damp<class_PhysicalBone3D_property_linear_damp>] may be added to or replace the body's damping value.

See [ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>] for more details about damping.


----



[DampMode<enum_PhysicalBone3D_DampMode>] **linear_damp_mode** = `0` [🔗<class_PhysicalBone3D_property_linear_damp_mode>]


- |void| **set_linear_damp_mode**\ (\ value\: [DampMode<enum_PhysicalBone3D_DampMode>]\ )
- [DampMode<enum_PhysicalBone3D_DampMode>] **get_linear_damp_mode**\ (\ )

Defines how [linear_damp<class_PhysicalBone3D_property_linear_damp>] is applied.


----



[Vector3<class_Vector3>] **linear_velocity** = `Vector3(0, 0, 0)` [🔗<class_PhysicalBone3D_property_linear_velocity>]


- |void| **set_linear_velocity**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_linear_velocity**\ (\ )

The body's linear velocity in units per second. Can be used sporadically, but **don't set this every frame**, because physics may run in another thread and runs at a different granularity. Use [_integrate_forces()<class_PhysicalBone3D_private_method__integrate_forces>] as your process loop for precise control of the body state.


----



[float<class_float>] **mass** = `1.0` [🔗<class_PhysicalBone3D_property_mass>]


- |void| **set_mass**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mass**\ (\ )

The body's mass.


----


## Method Descriptions



|void| **_integrate_forces**\ (\ state\: [PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>]\ ) |virtual| [🔗<class_PhysicalBone3D_private_method__integrate_forces>]

Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but the [custom_integrator<class_PhysicalBone3D_property_custom_integrator>] property allows you to disable the standard force integration and do fully custom force integration for a body.


----



|void| **apply_central_impulse**\ (\ impulse\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicalBone3D_method_apply_central_impulse>]

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).

This is equivalent to using [apply_impulse()<class_PhysicalBone3D_method_apply_impulse>] at the body's center of mass.


----



|void| **apply_impulse**\ (\ impulse\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicalBone3D_method_apply_impulse>]

Applies a positioned impulse to the PhysicsBone3D.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).

\ `position` is the offset from the PhysicsBone3D origin in global coordinates.


----



[int<class_int>] **get_bone_id**\ (\ ) |const| [🔗<class_PhysicalBone3D_method_get_bone_id>]

Returns the unique identifier of the PhysicsBone3D.


----



[bool<class_bool>] **get_simulate_physics**\ (\ ) [🔗<class_PhysicalBone3D_method_get_simulate_physics>]

Returns `true` if the PhysicsBone3D is allowed to simulate physics.


----



[bool<class_bool>] **is_simulating_physics**\ (\ ) [🔗<class_PhysicalBone3D_method_is_simulating_physics>]

Returns `true` if the PhysicsBone3D is currently simulating physics.

