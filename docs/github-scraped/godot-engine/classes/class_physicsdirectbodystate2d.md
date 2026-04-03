:github_url: hide



# PhysicsDirectBodyState2D

**Inherits:** [Object<class_Object>]

**Inherited By:** [PhysicsDirectBodyState2DExtension<class_PhysicsDirectBodyState2DExtension>]

Provides direct access to a physics body in the [PhysicsServer2D<class_PhysicsServer2D>].


## Description

Provides direct access to a physics body in the [PhysicsServer2D<class_PhysicsServer2D>], allowing safe changes to physics properties. This object is passed via the direct state callback of [RigidBody2D<class_RigidBody2D>], and is intended for changing the direct state of that body. See [RigidBody2D._integrate_forces()<class_RigidBody2D_private_method__integrate_forces>].


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [../tutorials/physics/ray-casting](Ray-casting .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`angular_velocity<class_PhysicsDirectBodyState2D_property_angular_velocity>`         |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`         | :ref:`center_of_mass<class_PhysicsDirectBodyState2D_property_center_of_mass>`             |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`         | :ref:`center_of_mass_local<class_PhysicsDirectBodyState2D_property_center_of_mass_local>` |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`collision_layer<class_PhysicsDirectBodyState2D_property_collision_layer>`           |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`collision_mask<class_PhysicsDirectBodyState2D_property_collision_mask>`             |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>`           |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`inverse_mass<class_PhysicsDirectBodyState2D_property_inverse_mass>`                 |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`         | :ref:`linear_velocity<class_PhysicsDirectBodyState2D_property_linear_velocity>`           |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`sleeping<class_PhysicsDirectBodyState2D_property_sleeping>`                         |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`step<class_PhysicsDirectBodyState2D_property_step>`                                 |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`total_angular_damp<class_PhysicsDirectBodyState2D_property_total_angular_damp>`     |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`         | :ref:`total_gravity<class_PhysicsDirectBodyState2D_property_total_gravity>`               |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`total_linear_damp<class_PhysicsDirectBodyState2D_property_total_linear_damp>`       |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
> | :ref:`Transform2D<class_Transform2D>` | :ref:`transform<class_PhysicsDirectBodyState2D_property_transform>`                       |
> +---------------------------------------+-------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`add_constant_central_force<class_PhysicsDirectBodyState2D_method_add_constant_central_force>`\ (\ force\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ )                           |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`add_constant_force<class_PhysicsDirectBodyState2D_method_add_constant_force>`\ (\ force\: :ref:`Vector2<class_Vector2>`, position\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ ) |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`add_constant_torque<class_PhysicsDirectBodyState2D_method_add_constant_torque>`\ (\ torque\: :ref:`float<class_float>`\ )                                                            |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_central_force<class_PhysicsDirectBodyState2D_method_apply_central_force>`\ (\ force\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ )                                         |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_central_impulse<class_PhysicsDirectBodyState2D_method_apply_central_impulse>`\ (\ impulse\: :ref:`Vector2<class_Vector2>`\ )                                                   |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_force<class_PhysicsDirectBodyState2D_method_apply_force>`\ (\ force\: :ref:`Vector2<class_Vector2>`, position\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ )               |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_impulse<class_PhysicsDirectBodyState2D_method_apply_impulse>`\ (\ impulse\: :ref:`Vector2<class_Vector2>`, position\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ )         |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_torque<class_PhysicsDirectBodyState2D_method_apply_torque>`\ (\ torque\: :ref:`float<class_float>`\ )                                                                          |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`apply_torque_impulse<class_PhysicsDirectBodyState2D_method_apply_torque_impulse>`\ (\ impulse\: :ref:`float<class_float>`\ )                                                         |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_constant_force<class_PhysicsDirectBodyState2D_method_get_constant_force>`\ (\ ) |const|                                                                                          |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                         | :ref:`get_constant_torque<class_PhysicsDirectBodyState2D_method_get_constant_torque>`\ (\ ) |const|                                                                                        |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`get_contact_collider<class_PhysicsDirectBodyState2D_method_get_contact_collider>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                                 |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_collider_id<class_PhysicsDirectBodyState2D_method_get_contact_collider_id>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                           |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                                       | :ref:`get_contact_collider_object<class_PhysicsDirectBodyState2D_method_get_contact_collider_object>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                   |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_contact_collider_position<class_PhysicsDirectBodyState2D_method_get_contact_collider_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                               |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_collider_shape<class_PhysicsDirectBodyState2D_method_get_contact_collider_shape>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                     |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_contact_collider_velocity_at_position<class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|       |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_count<class_PhysicsDirectBodyState2D_method_get_contact_count>`\ (\ ) |const|                                                                                            |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_contact_impulse<class_PhysicsDirectBodyState2D_method_get_contact_impulse>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                                   |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_contact_local_normal<class_PhysicsDirectBodyState2D_method_get_contact_local_normal>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                         |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_contact_local_position<class_PhysicsDirectBodyState2D_method_get_contact_local_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                     |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_contact_local_shape<class_PhysicsDirectBodyState2D_method_get_contact_local_shape>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|                                           |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_contact_local_velocity_at_position<class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |const|             |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>` | :ref:`get_space_state<class_PhysicsDirectBodyState2D_method_get_space_state>`\ (\ )                                                                                                        |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                     | :ref:`get_velocity_at_local_position<class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position>`\ (\ local_position\: :ref:`Vector2<class_Vector2>`\ ) |const|                  |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`integrate_forces<class_PhysicsDirectBodyState2D_method_integrate_forces>`\ (\ )                                                                                                      |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`set_constant_force<class_PhysicsDirectBodyState2D_method_set_constant_force>`\ (\ force\: :ref:`Vector2<class_Vector2>`\ )                                                           |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`set_constant_torque<class_PhysicsDirectBodyState2D_method_set_constant_torque>`\ (\ torque\: :ref:`float<class_float>`\ )                                                            |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **angular_velocity** [🔗<class_PhysicsDirectBodyState2D_property_angular_velocity>]


- |void| **set_angular_velocity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_angular_velocity**\ (\ )

The body's rotational velocity in *radians* per second.


----



[Vector2<class_Vector2>] **center_of_mass** [🔗<class_PhysicsDirectBodyState2D_property_center_of_mass>]


- [Vector2<class_Vector2>] **get_center_of_mass**\ (\ )

The body's center of mass position relative to the body's center in the global coordinate system.


----



[Vector2<class_Vector2>] **center_of_mass_local** [🔗<class_PhysicsDirectBodyState2D_property_center_of_mass_local>]


- [Vector2<class_Vector2>] **get_center_of_mass_local**\ (\ )

The body's center of mass position in the body's local coordinate system.


----



[int<class_int>] **collision_layer** [🔗<class_PhysicsDirectBodyState2D_property_collision_layer>]


- |void| **set_collision_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_layer**\ (\ )

The body's collision layer.


----



[int<class_int>] **collision_mask** [🔗<class_PhysicsDirectBodyState2D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The body's collision mask.


----



[float<class_float>] **inverse_inertia** [🔗<class_PhysicsDirectBodyState2D_property_inverse_inertia>]


- [float<class_float>] **get_inverse_inertia**\ (\ )

The inverse of the inertia of the body.


----



[float<class_float>] **inverse_mass** [🔗<class_PhysicsDirectBodyState2D_property_inverse_mass>]


- [float<class_float>] **get_inverse_mass**\ (\ )

The inverse of the mass of the body.


----



[Vector2<class_Vector2>] **linear_velocity** [🔗<class_PhysicsDirectBodyState2D_property_linear_velocity>]


- |void| **set_linear_velocity**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_linear_velocity**\ (\ )

The body's linear velocity in pixels per second.


----



[bool<class_bool>] **sleeping** [🔗<class_PhysicsDirectBodyState2D_property_sleeping>]


- |void| **set_sleep_state**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_sleeping**\ (\ )

If `true`, this body is currently sleeping (not active).


----



[float<class_float>] **step** [🔗<class_PhysicsDirectBodyState2D_property_step>]


- [float<class_float>] **get_step**\ (\ )

The timestep (delta) used for the simulation.


----



[float<class_float>] **total_angular_damp** [🔗<class_PhysicsDirectBodyState2D_property_total_angular_damp>]


- [float<class_float>] **get_total_angular_damp**\ (\ )

The rate at which the body stops rotating, if there are not any other forces moving it.


----



[Vector2<class_Vector2>] **total_gravity** [🔗<class_PhysicsDirectBodyState2D_property_total_gravity>]


- [Vector2<class_Vector2>] **get_total_gravity**\ (\ )

The total gravity vector being currently applied to this body.


----



[float<class_float>] **total_linear_damp** [🔗<class_PhysicsDirectBodyState2D_property_total_linear_damp>]


- [float<class_float>] **get_total_linear_damp**\ (\ )

The rate at which the body stops moving, if there are not any other forces moving it.


----



[Transform2D<class_Transform2D>] **transform** [🔗<class_PhysicsDirectBodyState2D_property_transform>]


- |void| **set_transform**\ (\ value\: [Transform2D<class_Transform2D>]\ )
- [Transform2D<class_Transform2D>] **get_transform**\ (\ )

The body's transformation matrix.


----


## Method Descriptions



|void| **add_constant_central_force**\ (\ force\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_PhysicsDirectBodyState2D_method_add_constant_central_force>]

Adds a constant directional force without affecting rotation that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

This is equivalent to using [add_constant_force()<class_PhysicsDirectBodyState2D_method_add_constant_force>] at the body's center of mass.


----



|void| **add_constant_force**\ (\ force\: [Vector2<class_Vector2>], position\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_PhysicsDirectBodyState2D_method_add_constant_force>]

Adds a constant positioned force to the body that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

\ `position` is the offset from the body origin in global coordinates.


----



|void| **add_constant_torque**\ (\ torque\: [float<class_float>]\ ) [🔗<class_PhysicsDirectBodyState2D_method_add_constant_torque>]

Adds a constant rotational force without affecting position that keeps being applied over time until cleared with `constant_torque = 0`.


----



|void| **apply_central_force**\ (\ force\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_PhysicsDirectBodyState2D_method_apply_central_force>]

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using [apply_force()<class_PhysicsDirectBodyState2D_method_apply_force>] at the body's center of mass.


----



|void| **apply_central_impulse**\ (\ impulse\: [Vector2<class_Vector2>]\ ) [🔗<class_PhysicsDirectBodyState2D_method_apply_central_impulse>]

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using [apply_impulse()<class_PhysicsDirectBodyState2D_method_apply_impulse>] at the body's center of mass.


----



|void| **apply_force**\ (\ force\: [Vector2<class_Vector2>], position\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_PhysicsDirectBodyState2D_method_apply_force>]

Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.

\ `position` is the offset from the body origin in global coordinates.


----



|void| **apply_impulse**\ (\ impulse\: [Vector2<class_Vector2>], position\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_PhysicsDirectBodyState2D_method_apply_impulse>]

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

\ `position` is the offset from the body origin in global coordinates.


----



|void| **apply_torque**\ (\ torque\: [float<class_float>]\ ) [🔗<class_PhysicsDirectBodyState2D_method_apply_torque>]

Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.

\ **Note:** [inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>] is required for this to work. To have [inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>], an active [CollisionShape2D<class_CollisionShape2D>] must be a child of the node, or you can manually set [inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>].


----



|void| **apply_torque_impulse**\ (\ impulse\: [float<class_float>]\ ) [🔗<class_PhysicsDirectBodyState2D_method_apply_torque_impulse>]

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

\ **Note:** [inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>] is required for this to work. To have [inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>], an active [CollisionShape2D<class_CollisionShape2D>] must be a child of the node, or you can manually set [inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>].


----



[Vector2<class_Vector2>] **get_constant_force**\ (\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_constant_force>]

Returns the body's total constant positional forces applied during each physics update.

See [add_constant_force()<class_PhysicsDirectBodyState2D_method_add_constant_force>] and [add_constant_central_force()<class_PhysicsDirectBodyState2D_method_add_constant_central_force>].


----



[float<class_float>] **get_constant_torque**\ (\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_constant_torque>]

Returns the body's total constant rotational forces applied during each physics update.

See [add_constant_torque()<class_PhysicsDirectBodyState2D_method_add_constant_torque>].


----



[RID<class_RID>] **get_contact_collider**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_collider>]

Returns the collider's [RID<class_RID>].


----



[int<class_int>] **get_contact_collider_id**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_collider_id>]

Returns the collider's object id.


----



[Object<class_Object>] **get_contact_collider_object**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_collider_object>]

Returns the collider object. This depends on how it was created (will return a scene node if such was used to create it).


----



[Vector2<class_Vector2>] **get_contact_collider_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_collider_position>]

Returns the position of the contact point on the collider in the global coordinate system.


----



[int<class_int>] **get_contact_collider_shape**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_collider_shape>]

Returns the collider's shape index.


----



[Vector2<class_Vector2>] **get_contact_collider_velocity_at_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position>]

Returns the velocity vector at the collider's contact point.


----



[int<class_int>] **get_contact_count**\ (\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_count>]

Returns the number of contacts this body has with other bodies.

\ **Note:** By default, this returns 0 unless bodies are configured to monitor contacts. See [RigidBody2D.contact_monitor<class_RigidBody2D_property_contact_monitor>].


----



[Vector2<class_Vector2>] **get_contact_impulse**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_impulse>]

Returns the impulse created by the contact.


----



[Vector2<class_Vector2>] **get_contact_local_normal**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_local_normal>]

Returns the local normal at the contact point.


----



[Vector2<class_Vector2>] **get_contact_local_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_local_position>]

Returns the position of the contact point on the body in the global coordinate system.


----



[int<class_int>] **get_contact_local_shape**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_local_shape>]

Returns the local shape index of the collision.


----



[Vector2<class_Vector2>] **get_contact_local_velocity_at_position**\ (\ contact_idx\: [int<class_int>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position>]

Returns the velocity vector at the body's contact point.


----



[PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>] **get_space_state**\ (\ ) [🔗<class_PhysicsDirectBodyState2D_method_get_space_state>]

Returns the current state of the space, useful for queries.


----



[Vector2<class_Vector2>] **get_velocity_at_local_position**\ (\ local_position\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position>]

Returns the body's velocity at the given relative position, including both translation and rotation.


----



|void| **integrate_forces**\ (\ ) [🔗<class_PhysicsDirectBodyState2D_method_integrate_forces>]

Updates the body's linear and angular velocity by applying gravity and damping for the equivalent of one physics tick.


----



|void| **set_constant_force**\ (\ force\: [Vector2<class_Vector2>]\ ) [🔗<class_PhysicsDirectBodyState2D_method_set_constant_force>]

Sets the body's total constant positional forces applied during each physics update.

See [add_constant_force()<class_PhysicsDirectBodyState2D_method_add_constant_force>] and [add_constant_central_force()<class_PhysicsDirectBodyState2D_method_add_constant_central_force>].


----



|void| **set_constant_torque**\ (\ torque\: [float<class_float>]\ ) [🔗<class_PhysicsDirectBodyState2D_method_set_constant_torque>]

Sets the body's total constant rotational forces applied during each physics update.

See [add_constant_torque()<class_PhysicsDirectBodyState2D_method_add_constant_torque>].

