:github_url: hide



# SoftBody3D

**Inherits:** [MeshInstance3D<class_MeshInstance3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A deformable 3D physics mesh.


## Description

A deformable 3D physics mesh. Used to create elastic or deformable objects such as cloth, rubber, or other flexible materials.

Additionally, **SoftBody3D** is subject to wind forces defined in [Area3D<class_Area3D>] (see [Area3D.wind_source_path<class_Area3D_property_wind_source_path>], [Area3D.wind_force_magnitude<class_Area3D_property_wind_force_magnitude>], and [Area3D.wind_attenuation_factor<class_Area3D_property_wind_attenuation_factor>]).

\ **Note:** It's recommended to use Jolt Physics when using **SoftBody3D** instead of the default GodotPhysics3D, as Jolt Physics' soft body implementation is faster and more reliable. You can switch the physics engine using the [ProjectSettings.physics/3d/physics_engine<class_ProjectSettings_property_physics/3d/physics_engine>] project setting.


## Tutorials

- [../tutorials/physics/soft_body](SoftBody .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`int<class_int>`                           | :ref:`collision_layer<class_SoftBody3D_property_collision_layer>`                 | ``1``            |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`int<class_int>`                           | :ref:`collision_mask<class_SoftBody3D_property_collision_mask>`                   | ``1``            |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`                       | :ref:`damping_coefficient<class_SoftBody3D_property_damping_coefficient>`         | ``0.01``         |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`DisableMode<enum_SoftBody3D_DisableMode>` | :ref:`disable_mode<class_SoftBody3D_property_disable_mode>`                       | ``0``            |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`                       | :ref:`drag_coefficient<class_SoftBody3D_property_drag_coefficient>`               | ``0.0``          |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`                       | :ref:`linear_stiffness<class_SoftBody3D_property_linear_stiffness>`               | ``0.5``          |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>`                 | :ref:`parent_collision_ignore<class_SoftBody3D_property_parent_collision_ignore>` | ``NodePath("")`` |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`                       | :ref:`pressure_coefficient<class_SoftBody3D_property_pressure_coefficient>`       | ``0.0``          |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`                         | :ref:`ray_pickable<class_SoftBody3D_property_ray_pickable>`                       | ``true``         |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`                       | :ref:`shrinking_factor<class_SoftBody3D_property_shrinking_factor>`               | ``0.0``          |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`int<class_int>`                           | :ref:`simulation_precision<class_SoftBody3D_property_simulation_precision>`       | ``5``            |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`                       | :ref:`total_mass<class_SoftBody3D_property_total_mass>`                           | ``1.0``          |
> +-------------------------------------------------+-----------------------------------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`add_collision_exception_with<class_SoftBody3D_method_add_collision_exception_with>`\ (\ body\: :ref:`Node<class_Node>`\ )                                                                                                                          |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`apply_central_force<class_SoftBody3D_method_apply_central_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                                     |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`apply_central_impulse<class_SoftBody3D_method_apply_central_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                               |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`apply_force<class_SoftBody3D_method_apply_force>`\ (\ point_index\: :ref:`int<class_int>`, force\: :ref:`Vector3<class_Vector3>`\ )                                                                                                                |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`apply_impulse<class_SoftBody3D_method_apply_impulse>`\ (\ point_index\: :ref:`int<class_int>`, impulse\: :ref:`Vector3<class_Vector3>`\ )                                                                                                          |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PhysicsBody3D<class_PhysicsBody3D>`\] | :ref:`get_collision_exceptions<class_SoftBody3D_method_get_collision_exceptions>`\ (\ )                                                                                                                                                                  |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                | :ref:`get_collision_layer_value<class_SoftBody3D_method_get_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                                                                                                                  |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                | :ref:`get_collision_mask_value<class_SoftBody3D_method_get_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                                                                                                                    |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                  | :ref:`get_physics_rid<class_SoftBody3D_method_get_physics_rid>`\ (\ ) |const|                                                                                                                                                                            |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                          | :ref:`get_point_transform<class_SoftBody3D_method_get_point_transform>`\ (\ point_index\: :ref:`int<class_int>`\ )                                                                                                                                       |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                | :ref:`is_point_pinned<class_SoftBody3D_method_is_point_pinned>`\ (\ point_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                       |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`remove_collision_exception_with<class_SoftBody3D_method_remove_collision_exception_with>`\ (\ body\: :ref:`Node<class_Node>`\ )                                                                                                                    |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_collision_layer_value<class_SoftBody3D_method_set_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )                                                                                         |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_collision_mask_value<class_SoftBody3D_method_set_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )                                                                                           |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_point_pinned<class_SoftBody3D_method_set_point_pinned>`\ (\ point_index\: :ref:`int<class_int>`, pinned\: :ref:`bool<class_bool>`, attachment_path\: :ref:`NodePath<class_NodePath>` = NodePath(""), insert_at\: :ref:`int<class_int>` = -1\ ) |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **DisableMode**: [🔗<enum_SoftBody3D_DisableMode>]



[DisableMode<enum_SoftBody3D_DisableMode>] **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], remove from the physics simulation to stop all physics interactions with this **SoftBody3D**.

Automatically re-added to the physics simulation when the [Node<class_Node>] is processed again.



[DisableMode<enum_SoftBody3D_DisableMode>] **DISABLE_MODE_KEEP_ACTIVE** = `1`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], do not affect the physics simulation.


----


## Property Descriptions



[int<class_int>] **collision_layer** = `1` [🔗<class_SoftBody3D_property_collision_layer>]


- |void| **set_collision_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_layer**\ (\ )

The physics layers this SoftBody3D **is in**. Collision objects can exist in one or more of 32 different layers. See also [collision_mask<class_SoftBody3D_property_collision_mask>].

\ **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[int<class_int>] **collision_mask** = `1` [🔗<class_SoftBody3D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers this SoftBody3D **scans**. Collision objects can scan one or more of 32 different layers. See also [collision_layer<class_SoftBody3D_property_collision_layer>].

\ **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[float<class_float>] **damping_coefficient** = `0.01` [🔗<class_SoftBody3D_property_damping_coefficient>]


- |void| **set_damping_coefficient**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_damping_coefficient**\ (\ )

The body's damping coefficient. Higher values will slow down the body more noticeably when forces are applied.


----



[DisableMode<enum_SoftBody3D_DisableMode>] **disable_mode** = `0` [🔗<class_SoftBody3D_property_disable_mode>]


- |void| **set_disable_mode**\ (\ value\: [DisableMode<enum_SoftBody3D_DisableMode>]\ )
- [DisableMode<enum_SoftBody3D_DisableMode>] **get_disable_mode**\ (\ )

Defines the behavior in physics when [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>].


----



[float<class_float>] **drag_coefficient** = `0.0` [🔗<class_SoftBody3D_property_drag_coefficient>]


- |void| **set_drag_coefficient**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_drag_coefficient**\ (\ )

The body's drag coefficient. Higher values increase this body's air resistance.

\ **Note:** This value is currently unused by Godot's default physics implementation.


----



[float<class_float>] **linear_stiffness** = `0.5` [🔗<class_SoftBody3D_property_linear_stiffness>]


- |void| **set_linear_stiffness**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_linear_stiffness**\ (\ )

Higher values will result in a stiffer body, while lower values will increase the body's ability to bend. The value can be between `0.0` and `1.0` (inclusive).


----



[NodePath<class_NodePath>] **parent_collision_ignore** = `NodePath("")` [🔗<class_SoftBody3D_property_parent_collision_ignore>]


- |void| **set_parent_collision_ignore**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_parent_collision_ignore**\ (\ )

[NodePath<class_NodePath>] to a [CollisionObject3D<class_CollisionObject3D>] this SoftBody3D should avoid clipping.


----



[float<class_float>] **pressure_coefficient** = `0.0` [🔗<class_SoftBody3D_property_pressure_coefficient>]


- |void| **set_pressure_coefficient**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pressure_coefficient**\ (\ )

The pressure coefficient of this soft body. Simulate pressure build-up from inside this body. Higher values increase the strength of this effect.


----



[bool<class_bool>] **ray_pickable** = `true` [🔗<class_SoftBody3D_property_ray_pickable>]


- |void| **set_ray_pickable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_ray_pickable**\ (\ )

If `true`, the **SoftBody3D** will respond to [RayCast3D<class_RayCast3D>]\ s.


----



[float<class_float>] **shrinking_factor** = `0.0` [🔗<class_SoftBody3D_property_shrinking_factor>]


- |void| **set_shrinking_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_shrinking_factor**\ (\ )

Scales the rest lengths of **SoftBody3D**'s edge constraints. Positive values shrink the mesh, while negative values expand it. For example, a value of `0.1` shortens the edges of the mesh by 10%, while `-0.1` expands the edges by 10%.

\ **Note:** [shrinking_factor<class_SoftBody3D_property_shrinking_factor>] is best used on surface meshes with pinned points.


----



[int<class_int>] **simulation_precision** = `5` [🔗<class_SoftBody3D_property_simulation_precision>]


- |void| **set_simulation_precision**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_simulation_precision**\ (\ )

Increasing this value will improve the resulting simulation, but can affect performance. Use with care.


----



[float<class_float>] **total_mass** = `1.0` [🔗<class_SoftBody3D_property_total_mass>]


- |void| **set_total_mass**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_total_mass**\ (\ )

The SoftBody3D's mass.


----


## Method Descriptions



|void| **add_collision_exception_with**\ (\ body\: [Node<class_Node>]\ ) [🔗<class_SoftBody3D_method_add_collision_exception_with>]

Adds a body to the list of bodies that this body can't collide with.


----



|void| **apply_central_force**\ (\ force\: [Vector3<class_Vector3>]\ ) [🔗<class_SoftBody3D_method_apply_central_force>]

Distributes and applies a force to all points. A force is time dependent and meant to be applied every physics update.


----



|void| **apply_central_impulse**\ (\ impulse\: [Vector3<class_Vector3>]\ ) [🔗<class_SoftBody3D_method_apply_central_impulse>]

Distributes and applies an impulse to all points.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).


----



|void| **apply_force**\ (\ point_index\: [int<class_int>], force\: [Vector3<class_Vector3>]\ ) [🔗<class_SoftBody3D_method_apply_force>]

Applies a force to a point. A force is time dependent and meant to be applied every physics update.


----



|void| **apply_impulse**\ (\ point_index\: [int<class_int>], impulse\: [Vector3<class_Vector3>]\ ) [🔗<class_SoftBody3D_method_apply_impulse>]

Applies an impulse to a point.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).


----



[Array<class_Array>]\[[PhysicsBody3D<class_PhysicsBody3D>]\] **get_collision_exceptions**\ (\ ) [🔗<class_SoftBody3D_method_get_collision_exceptions>]

Returns an array of nodes that were added as collision exceptions for this body.


----



[bool<class_bool>] **get_collision_layer_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_SoftBody3D_method_get_collision_layer_value>]

Returns whether or not the specified layer of the [collision_layer<class_SoftBody3D_property_collision_layer>] is enabled, given a `layer_number` between 1 and 32.


----



[bool<class_bool>] **get_collision_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_SoftBody3D_method_get_collision_mask_value>]

Returns whether or not the specified layer of the [collision_mask<class_SoftBody3D_property_collision_mask>] is enabled, given a `layer_number` between 1 and 32.


----



[RID<class_RID>] **get_physics_rid**\ (\ ) |const| [🔗<class_SoftBody3D_method_get_physics_rid>]

Returns the internal [RID<class_RID>] used by the [PhysicsServer3D<class_PhysicsServer3D>] for this body.


----



[Vector3<class_Vector3>] **get_point_transform**\ (\ point_index\: [int<class_int>]\ ) [🔗<class_SoftBody3D_method_get_point_transform>]

Returns local translation of a vertex in the surface array.


----



[bool<class_bool>] **is_point_pinned**\ (\ point_index\: [int<class_int>]\ ) |const| [🔗<class_SoftBody3D_method_is_point_pinned>]

Returns `true` if vertex is set to pinned.


----



|void| **remove_collision_exception_with**\ (\ body\: [Node<class_Node>]\ ) [🔗<class_SoftBody3D_method_remove_collision_exception_with>]

Removes a body from the list of bodies that this body can't collide with.


----



|void| **set_collision_layer_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_SoftBody3D_method_set_collision_layer_value>]

Based on `value`, enables or disables the specified layer in the [collision_layer<class_SoftBody3D_property_collision_layer>], given a `layer_number` between 1 and 32.


----



|void| **set_collision_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_SoftBody3D_method_set_collision_mask_value>]

Based on `value`, enables or disables the specified layer in the [collision_mask<class_SoftBody3D_property_collision_mask>], given a `layer_number` between 1 and 32.


----



|void| **set_point_pinned**\ (\ point_index\: [int<class_int>], pinned\: [bool<class_bool>], attachment_path\: [NodePath<class_NodePath>] = NodePath(""), insert_at\: [int<class_int>] = -1\ ) [🔗<class_SoftBody3D_method_set_point_pinned>]

Sets the pinned state of a surface vertex. When set to `true`, the optional `attachment_path` can define a [Node3D<class_Node3D>] the pinned vertex will be attached to.

