:github_url: hide



# PhysicsDirectBodyState3D

**Inherits:** [Object<class_Object>]

**Inherited By:** [PhysicsDirectBodyState3DExtension<class_PhysicsDirectBodyState3DExtension>]

Provides direct access to a physics body in the [PhysicsServer3D<class_PhysicsServer3D>].


## Description

Provides direct access to a physics body in the [PhysicsServer3D<class_PhysicsServer3D>], allowing safe changes to physics properties. This object is passed via the direct state callback of [RigidBody3D<class_RigidBody3D>], and is intended for changing the direct state of that body. See [RigidBody3D._integrate_forces()<class_RigidBody3D_private_method__integrate_forces>].


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [../tutorials/physics/ray-casting](Ray-casting .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`angular_velocity<class_PhysicsDirectBodyState3D_property_angular_velocity>`             |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`center_of_mass<class_PhysicsDirectBodyState3D_property_center_of_mass>`                 |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`center_of_mass_local<class_PhysicsDirectBodyState3D_property_center_of_mass_local>`     |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`collision_layer<class_PhysicsDirectBodyState3D_property_collision_layer>`               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`collision_mask<class_PhysicsDirectBodyState3D_property_collision_mask>`                 |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>`               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Basis<class_Basis>`             | :ref:`inverse_inertia_tensor<class_PhysicsDirectBodyState3D_property_inverse_inertia_tensor>` |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`inverse_mass<class_PhysicsDirectBodyState3D_property_inverse_mass>`                     |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`linear_velocity<class_PhysicsDirectBodyState3D_property_linear_velocity>`               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Basis<class_Basis>`             | :ref:`principal_inertia_axes<class_PhysicsDirectBodyState3D_property_principal_inertia_axes>` |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`sleeping<class_PhysicsDirectBodyState3D_property_sleeping>`                             |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`step<class_PhysicsDirectBodyState3D_property_step>`                                     |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`total_angular_damp<class_PhysicsDirectBodyState3D_property_total_angular_damp>`         |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`total_gravity<class_PhysicsDirectBodyState3D_property_total_gravity>`                   |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`total_linear_damp<class_PhysicsDirectBodyState3D_property_total_linear_damp>`           |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`transform<class_PhysicsDirectBodyState3D_property_transform>`                           |
> +---------------------------------------+-----------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`add_constant_central_force<class_PhysicsDirectBodyState3D_method_add_constant_central_force>`\ (\ force\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ )                           |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`add_constant_force<class_PhysicsDirectBodyState3D_method_add_constant_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ ) |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`add_constant_torque<class_PhysicsDirectBodyState3D_method_add_constant_torque>`\ (\ torque\: :ref:`Vector3<class_Vector3>`\ )                                                           |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_central_force<class_PhysicsDirectBodyState3D_method_apply_central_force>`\ (\ force\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ )                                         |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_central_impulse<class_PhysicsDirectBodyState3D_method_apply_central_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ )                                   |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_force<class_PhysicsDirectBodyState3D_method_apply_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ )               |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_impulse<class_PhysicsDirectBodyState3D_method_apply_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>` = Vector3(0, 0, 0)\ )         |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_torque<class_PhysicsDirectBodyState3D_method_apply_torque>`\ (\ torque\: :ref:`Vector3<class_Vector3>`\ )                                                                         |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_torque_impulse<class_PhysicsDirectBodyState3D_method_apply_torque_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`\ )                                                        |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_constant_force<class_PhysicsDirectBodyState3D_method_get_constant_force>`\ (\ ) |const|                                                                                             |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_constant_torque<class_PhysicsDirectBodyState3D_method_get_constant_torque>`\ (\ ) |const|                                                                                           |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`get_contact_collider<class_PhysicsDirectBodyState3D_method_get_contact_collider>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                                    |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_collider_id<class_PhysicsDirectBodyState3D_method_get_contact_collider_id>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                              |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                                       | :ref:`get_contact_collider_object<class_PhysicsDirectBodyState3D_method_get_contact_collider_object>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                      |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_contact_collider_position<class_PhysicsDirectBodyState3D_method_get_contact_collider_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                  |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_collider_shape<class_PhysicsDirectBodyState3D_method_get_contact_collider_shape>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                        |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_contact_collider_velocity_at_position<class_PhysicsDirectBodyState3D_method_get_contact_collider_velocity_at_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|          |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_count<class_PhysicsDirectBodyState3D_method_get_contact_count>`\ (\ ) |const|                                                                                               |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_contact_impulse<class_PhysicsDirectBodyState3D_method_get_contact_impulse>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                                      |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_contact_local_normal<class_PhysicsDirectBodyState3D_method_get_contact_local_normal>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                            |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_contact_local_position<class_PhysicsDirectBodyState3D_method_get_contact_local_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                        |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_local_shape<class_PhysicsDirectBodyState3D_method_get_contact_local_shape>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                              |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_contact_local_velocity_at_position<class_PhysicsDirectBodyState3D_method_get_contact_local_velocity_at_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` | :ref:`get_space_state<class_PhysicsDirectBodyState3D_method_get_space_state>`\ (\ )                                                                                                           |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`get_velocity_at_local_position<class_PhysicsDirectBodyState3D_method_get_velocity_at_local_position>`\ (\ local_position\: :ref:`Vector3<class_Vector3>`\ ) |const|                     |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`integrate_forces<class_PhysicsDirectBodyState3D_method_integrate_forces>`\ (\ )                                                                                                         |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`set_constant_force<class_PhysicsDirectBodyState3D_method_set_constant_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`\ )                                                              |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`set_constant_torque<class_PhysicsDirectBodyState3D_method_set_constant_torque>`\ (\ torque\: :ref:`Vector3<class_Vector3>`\ )                                                           |
> +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **angular_velocity** [🔗<class_PhysicsDirectBodyState3D_property_angular_velocity>]


- |void| **set_angular_velocity**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_angular_velocity**\ (\ )

The body's rotational velocity in *radians* per second.


----



[Vector3<class_Vector3>] **center_of_mass** [🔗<class_PhysicsDirectBodyState3D_property_center_of_mass>]


- [Vector3<class_Vector3>] **get_center_of_mass**\ (\ )

The body's center of mass position relative to the body's center in the global coordinate system.


----



[Vector3<class_Vector3>] **center_of_mass_local** [🔗<class_PhysicsDirectBodyState3D_property_center_of_mass_local>]


- [Vector3<class_Vector3>] **get_center_of_mass_local**\ (\ )

The body's center of mass position in the body's local coordinate system.


----



[int<class_int>] **collision_layer** [🔗<class_PhysicsDirectBodyState3D_property_collision_layer>]


- |void| **set_collision_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_layer**\ (\ )

The body's collision layer.


----



[int<class_int>] **collision_mask** [🔗<class_PhysicsDirectBodyState3D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The body's collision mask.


----



[Vector3<class_Vector3>] **inverse_inertia** [🔗<class_PhysicsDirectBodyState3D_property_inverse_inertia>]


- [Vector3<class_Vector3>] **get_inverse_inertia**\ (\ )

The inverse of the inertia of the body.


----



[Basis<class_Basis>] **inverse_inertia_tensor** [🔗<class_PhysicsDirectBodyState3D_property_inverse_inertia_tensor>]


- [Basis<class_Basis>] **get_inverse_inertia_tensor**\ (\ )

The inverse of the inertia tensor of the body.


----



[float<class_float>] **inverse_mass** [🔗<class_PhysicsDirectBodyState3D_property_inverse_mass>]


- [float<class_float>] **get_inverse_mass**\ (\ )

The inverse of the mass of the body.


----



[Vector3<class_Vector3>] **linear_velocity** [🔗<class_PhysicsDirectBodyState3D_property_linear_velocity>]


- |void| **set_linear_velocity**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_linear_velocity**\ (\ )

The body's linear velocity in units per second.


----



[Basis<class_Basis>] **principal_inertia_axes** [🔗<class_PhysicsDirectBodyState3D_property_principal_inertia_axes>]


- [Basis<class_Basis>] **get_principal_inertia_axes**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **sleeping** [🔗<class_PhysicsDirectBodyState3D_property_sleeping>]


- |void| **set_sleep_state**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_sleeping**\ (\ )

If `true`, this body is currently sleeping (not active).


----



[float<class_float>] **step** [🔗<class_PhysicsDirectBodyState3D_property_step>]


- [float<class_float>] **get_step**\ (\ )

The timestep (delta) used for the simulation.


----



[float<class_float>] **total_angular_damp** [🔗<class_PhysicsDirectBodyState3D_property_total_angular_damp>]


- [float<class_float>] **get_total_angular_damp**\ (\ )

The rate at which the body stops rotating, if there are not any other forces moving it.


----



[Vector3<class_Vector3>] **total_gravity** [🔗<class_PhysicsDirectBodyState3D_property_total_gravity>]


- [Vector3<class_Vector3>] **get_total_gravity**\ (\ )

The total gravity vector being currently applied to this body.


----



[float<class_float>] **total_linear_damp** [🔗<class_PhysicsDirectBodyState3D_property_total_linear_damp>]


- [float<class_float>] **get_total_linear_damp**\ (\ )

The rate at which the body stops moving, if there are not any other forces moving it.


----



[Transform3D<class_Transform3D>] **transform** [🔗<class_PhysicsDirectBodyState3D_property_transform>]


- |void| **set_transform**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_transform**\ (\ )

The body's transformation matrix.


----


## Method Descriptions



|void| **add_constant_central_force**\ (\ force\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicsDirectBodyState3D_method_add_constant_central_force>]

Adds a constant directional force without affecting rotation that keeps being applied over time until cleared with `constant_force = Vector3(0, 0, 0)`.

This is equivalent to using [add_constant_force()<class_PhysicsDirectBodyState3D_method_add_constant_force>] at the body's center of mass.


----



|void| **add_constant_force**\ (\ force\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicsDirectBodyState3D_method_add_constant_force>]

Adds a constant positioned force to the body that keeps being applied over time until cleared with `constant_force = Vector3(0, 0, 0)`.

\ `position` is the offset from the body origin in global coordinates.


----



|void| **add_constant_torque**\ (\ torque\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsDirectBodyState3D_method_add_constant_torque>]

Adds a constant rotational force without affecting position that keeps being applied over time until cleared with `constant_torque = Vector3(0, 0, 0)`.


----



|void| **apply_central_force**\ (\ force\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicsDirectBodyState3D_method_apply_central_force>]

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using [apply_force()<class_PhysicsDirectBodyState3D_method_apply_force>] at the body's center of mass.


----



|void| **apply_central_impulse**\ (\ impulse\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicsDirectBodyState3D_method_apply_central_impulse>]

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using [apply_impulse()<class_PhysicsDirectBodyState3D_method_apply_impulse>] at the body's center of mass.


----



|void| **apply_force**\ (\ force\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicsDirectBodyState3D_method_apply_force>]

Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.

\ `position` is the offset from the body origin in global coordinates.


----



|void| **apply_impulse**\ (\ impulse\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>] = Vector3(0, 0, 0)\ ) [🔗<class_PhysicsDirectBodyState3D_method_apply_impulse>]

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

\ `position` is the offset from the body origin in global coordinates.


----



|void| **apply_torque**\ (\ torque\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsDirectBodyState3D_method_apply_torque>]

Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.

\ **Note:** [inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>] is required for this to work. To have [inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>], an active [CollisionShape3D<class_CollisionShape3D>] must be a child of the node, or you can manually set [inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>].


----



|void| **apply_torque_impulse**\ (\ impulse\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsDirectBodyState3D_method_apply_torque_impulse>]

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

\ **Note:** [inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>] is required for this to work. To have [inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>], an active [CollisionShape3D<class_CollisionShape3D>] must be a child of the node, or you can manually set [inverse_inertia<class_PhysicsDirectBodyState3D_property_inverse_inertia>].


----



[Vector3<class_Vector3>] **get_constant_force**\ (\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_constant_force>]

Returns the body's total constant positional forces applied during each physics update.

See [add_constant_force()<class_PhysicsDirectBodyState3D_method_add_constant_force>] and [add_constant_central_force()<class_PhysicsDirectBodyState3D_method_add_constant_central_force>].


----



[Vector3<class_Vector3>] **get_constant_torque**\ (\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_constant_torque>]

Returns the body's total constant rotational forces applied during each physics update.

See [add_constant_torque()<class_PhysicsDirectBodyState3D_method_add_constant_torque>].


----



[RID<class_RID>] **get_contact_collider**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider>]

Returns the collider's [RID<class_RID>].


----



[int<class_int>] **get_contact_collider_id**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_id>]

Returns the collider's object id.


----



[Object<class_Object>] **get_contact_collider_object**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_object>]

Returns the collider object.


----



[Vector3<class_Vector3>] **get_contact_collider_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_position>]

Returns the position of the contact point on the collider in the global coordinate system.


----



[int<class_int>] **get_contact_collider_shape**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_shape>]

Returns the collider's shape index.


----



[Vector3<class_Vector3>] **get_contact_collider_velocity_at_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_collider_velocity_at_position>]

Returns the linear velocity vector at the collider's contact point.


----



[int<class_int>] **get_contact_count**\ (\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_count>]

Returns the number of contacts this body has with other bodies.

\ **Note:** By default, this returns 0 unless bodies are configured to monitor contacts. See [RigidBody3D.contact_monitor<class_RigidBody3D_property_contact_monitor>].


----



[Vector3<class_Vector3>] **get_contact_impulse**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_impulse>]

Impulse created by the contact.


----



[Vector3<class_Vector3>] **get_contact_local_normal**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_normal>]

Returns the local normal at the contact point.


----



[Vector3<class_Vector3>] **get_contact_local_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_position>]

Returns the position of the contact point on the body in the global coordinate system.


----



[int<class_int>] **get_contact_local_shape**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_shape>]

Returns the local shape index of the collision.


----



[Vector3<class_Vector3>] **get_contact_local_velocity_at_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_contact_local_velocity_at_position>]

Returns the linear velocity vector at the body's contact point.


----



[PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] **get_space_state**\ (\ ) [🔗<class_PhysicsDirectBodyState3D_method_get_space_state>]

Returns the current state of the space, useful for queries.


----



[Vector3<class_Vector3>] **get_velocity_at_local_position**\ (\ local_position\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_PhysicsDirectBodyState3D_method_get_velocity_at_local_position>]

Returns the body's velocity at the given relative position, including both translation and rotation.


----



|void| **integrate_forces**\ (\ ) [🔗<class_PhysicsDirectBodyState3D_method_integrate_forces>]

Updates the body's linear and angular velocity by applying gravity and damping for the equivalent of one physics tick.


----



|void| **set_constant_force**\ (\ force\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsDirectBodyState3D_method_set_constant_force>]

Sets the body's total constant positional forces applied during each physics update.

See [add_constant_force()<class_PhysicsDirectBodyState3D_method_add_constant_force>] and [add_constant_central_force()<class_PhysicsDirectBodyState3D_method_add_constant_central_force>].


----



|void| **set_constant_torque**\ (\ torque\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsDirectBodyState3D_method_set_constant_torque>]

Sets the body's total constant rotational forces applied during each physics update.

See [add_constant_torque()<class_PhysicsDirectBodyState3D_method_add_constant_torque>].

