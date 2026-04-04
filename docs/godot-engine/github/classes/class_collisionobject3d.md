:github_url: hide



# CollisionObject3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [Area3D<class_Area3D>], [PhysicsBody3D<class_PhysicsBody3D>]

Abstract base class for 3D physics objects.


## Description

Abstract base class for 3D physics objects. **CollisionObject3D** can hold any number of [Shape3D<class_Shape3D>]\ s for collision. Each shape must be assigned to a *shape owner*. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the `shape_owner_*` methods.

\ **Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                  | :ref:`collision_layer<class_CollisionObject3D_property_collision_layer>`             | ``1``     |
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                  | :ref:`collision_mask<class_CollisionObject3D_property_collision_mask>`               | ``1``     |
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                              | :ref:`collision_priority<class_CollisionObject3D_property_collision_priority>`       | ``1.0``   |
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
> | :ref:`DisableMode<enum_CollisionObject3D_DisableMode>` | :ref:`disable_mode<class_CollisionObject3D_property_disable_mode>`                   | ``0``     |
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                | :ref:`input_capture_on_drag<class_CollisionObject3D_property_input_capture_on_drag>` | ``false`` |
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                | :ref:`input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>`       | ``true``  |
> +--------------------------------------------------------+--------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_input_event<class_CollisionObject3D_private_method__input_event>`\ (\ camera\: :ref:`Camera3D<class_Camera3D>`, event\: :ref:`InputEvent<class_InputEvent>`, event_position\: :ref:`Vector3<class_Vector3>`, normal\: :ref:`Vector3<class_Vector3>`, shape_idx\: :ref:`int<class_int>`\ ) |virtual| |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_mouse_enter<class_CollisionObject3D_private_method__mouse_enter>`\ (\ ) |virtual|                                                                                                                                                                                                                   |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_mouse_exit<class_CollisionObject3D_private_method__mouse_exit>`\ (\ ) |virtual|                                                                                                                                                                                                                     |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`create_shape_owner<class_CollisionObject3D_method_create_shape_owner>`\ (\ owner\: :ref:`Object<class_Object>`\ )                                                                                                                                                                                    |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`get_collision_layer_value<class_CollisionObject3D_method_get_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                             |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`get_collision_mask_value<class_CollisionObject3D_method_get_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                               |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                           | :ref:`get_rid<class_CollisionObject3D_method_get_rid>`\ (\ ) |const|                                                                                                                                                                                                                                       |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`get_shape_owners<class_CollisionObject3D_method_get_shape_owners>`\ (\ )                                                                                                                                                                                                                             |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_shape_owner_disabled<class_CollisionObject3D_method_is_shape_owner_disabled>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                     |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`remove_shape_owner<class_CollisionObject3D_method_remove_shape_owner>`\ (\ owner_id\: :ref:`int<class_int>`\ )                                                                                                                                                                                       |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`set_collision_layer_value<class_CollisionObject3D_method_set_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )                                                                                                                                    |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`set_collision_mask_value<class_CollisionObject3D_method_set_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )                                                                                                                                      |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`shape_find_owner<class_CollisionObject3D_method_shape_find_owner>`\ (\ shape_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_add_shape<class_CollisionObject3D_method_shape_owner_add_shape>`\ (\ owner_id\: :ref:`int<class_int>`, shape\: :ref:`Shape3D<class_Shape3D>`\ )                                                                                                                                          |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_clear_shapes<class_CollisionObject3D_method_shape_owner_clear_shapes>`\ (\ owner_id\: :ref:`int<class_int>`\ )                                                                                                                                                                           |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                     | :ref:`shape_owner_get_owner<class_CollisionObject3D_method_shape_owner_get_owner>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                         |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Shape3D<class_Shape3D>`                   | :ref:`shape_owner_get_shape<class_CollisionObject3D_method_shape_owner_get_shape>`\ (\ owner_id\: :ref:`int<class_int>`, shape_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                       |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`shape_owner_get_shape_count<class_CollisionObject3D_method_shape_owner_get_shape_count>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                             |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`shape_owner_get_shape_index<class_CollisionObject3D_method_shape_owner_get_shape_index>`\ (\ owner_id\: :ref:`int<class_int>`, shape_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                           |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`           | :ref:`shape_owner_get_transform<class_CollisionObject3D_method_shape_owner_get_transform>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                 |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_remove_shape<class_CollisionObject3D_method_shape_owner_remove_shape>`\ (\ owner_id\: :ref:`int<class_int>`, shape_id\: :ref:`int<class_int>`\ )                                                                                                                                         |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_set_disabled<class_CollisionObject3D_method_shape_owner_set_disabled>`\ (\ owner_id\: :ref:`int<class_int>`, disabled\: :ref:`bool<class_bool>`\ )                                                                                                                                       |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_set_transform<class_CollisionObject3D_method_shape_owner_set_transform>`\ (\ owner_id\: :ref:`int<class_int>`, transform\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                                      |
> +-------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**input_event**\ (\ camera\: [Node<class_Node>], event\: [InputEvent<class_InputEvent>], event_position\: [Vector3<class_Vector3>], normal\: [Vector3<class_Vector3>], shape_idx\: [int<class_int>]\ ) [🔗<class_CollisionObject3D_signal_input_event>]

Emitted when the object receives an unhandled [InputEvent<class_InputEvent>]. `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point.


----



**mouse_entered**\ (\ ) [🔗<class_CollisionObject3D_signal_mouse_entered>]

Emitted when the mouse pointer enters any of this object's shapes. Requires [input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject3D_property_collision_layer>] bit to be set.

\ **Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.


----



**mouse_exited**\ (\ ) [🔗<class_CollisionObject3D_signal_mouse_exited>]

Emitted when the mouse pointer exits all this object's shapes. Requires [input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject3D_property_collision_layer>] bit to be set.

\ **Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.


----


## Enumerations



enum **DisableMode**: [🔗<enum_CollisionObject3D_DisableMode>]



[DisableMode<enum_CollisionObject3D_DisableMode>] **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], remove from the physics simulation to stop all physics interactions with this **CollisionObject3D**.

Automatically re-added to the physics simulation when the [Node<class_Node>] is processed again.



[DisableMode<enum_CollisionObject3D_DisableMode>] **DISABLE_MODE_MAKE_STATIC** = `1`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], make the body static. Doesn't affect [Area3D<class_Area3D>]. [PhysicsBody3D<class_PhysicsBody3D>] can't be affected by forces or other bodies while static.

Automatically set [PhysicsBody3D<class_PhysicsBody3D>] back to its original mode when the [Node<class_Node>] is processed again.



[DisableMode<enum_CollisionObject3D_DisableMode>] **DISABLE_MODE_KEEP_ACTIVE** = `2`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], do not affect the physics simulation.


----


## Property Descriptions



[int<class_int>] **collision_layer** = `1` [🔗<class_CollisionObject3D_property_collision_layer>]


- |void| **set_collision_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_layer**\ (\ )

The physics layers this CollisionObject3D **is in**. Collision objects can exist in one or more of 32 different layers. See also [collision_mask<class_CollisionObject3D_property_collision_mask>].

\ **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[int<class_int>] **collision_mask** = `1` [🔗<class_CollisionObject3D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers this CollisionObject3D **scans**. Collision objects can scan one or more of 32 different layers. See also [collision_layer<class_CollisionObject3D_property_collision_layer>].

\ **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[float<class_float>] **collision_priority** = `1.0` [🔗<class_CollisionObject3D_property_collision_priority>]


- |void| **set_collision_priority**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_collision_priority**\ (\ )

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.


----



[DisableMode<enum_CollisionObject3D_DisableMode>] **disable_mode** = `0` [🔗<class_CollisionObject3D_property_disable_mode>]


- |void| **set_disable_mode**\ (\ value\: [DisableMode<enum_CollisionObject3D_DisableMode>]\ )
- [DisableMode<enum_CollisionObject3D_DisableMode>] **get_disable_mode**\ (\ )

Defines the behavior in physics when [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>].


----



[bool<class_bool>] **input_capture_on_drag** = `false` [🔗<class_CollisionObject3D_property_input_capture_on_drag>]


- |void| **set_capture_input_on_drag**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_capture_input_on_drag**\ (\ )

If `true`, the **CollisionObject3D** will continue to receive input events as the mouse is dragged across its shapes.


----



[bool<class_bool>] **input_ray_pickable** = `true` [🔗<class_CollisionObject3D_property_input_ray_pickable>]


- |void| **set_ray_pickable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_ray_pickable**\ (\ )

If `true`, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least one [collision_layer<class_CollisionObject3D_property_collision_layer>] bit to be set.


----


## Method Descriptions



|void| **_input_event**\ (\ camera\: [Camera3D<class_Camera3D>], event\: [InputEvent<class_InputEvent>], event_position\: [Vector3<class_Vector3>], normal\: [Vector3<class_Vector3>], shape_idx\: [int<class_int>]\ ) |virtual| [🔗<class_CollisionObject3D_private_method__input_event>]

Receives unhandled [InputEvent<class_InputEvent>]\ s. `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point. Connect to the [input_event<class_CollisionObject3D_signal_input_event>] signal to easily pick up these events.

\ **Note:** [_input_event()<class_CollisionObject3D_private_method__input_event>] requires [input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject3D_property_collision_layer>] bit to be set.


----



|void| **_mouse_enter**\ (\ ) |virtual| [🔗<class_CollisionObject3D_private_method__mouse_enter>]

Called when the mouse pointer enters any of this object's shapes. Requires [input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject3D_property_collision_layer>] bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.


----



|void| **_mouse_exit**\ (\ ) |virtual| [🔗<class_CollisionObject3D_private_method__mouse_exit>]

Called when the mouse pointer exits all this object's shapes. Requires [input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject3D_property_collision_layer>] bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.


----



[int<class_int>] **create_shape_owner**\ (\ owner\: [Object<class_Object>]\ ) [🔗<class_CollisionObject3D_method_create_shape_owner>]

Creates a new shape owner for the given object. Returns `owner_id` of the new owner for future reference.


----



[bool<class_bool>] **get_collision_layer_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_get_collision_layer_value>]

Returns whether or not the specified layer of the [collision_layer<class_CollisionObject3D_property_collision_layer>] is enabled, given a `layer_number` between 1 and 32.


----



[bool<class_bool>] **get_collision_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_get_collision_mask_value>]

Returns whether or not the specified layer of the [collision_mask<class_CollisionObject3D_property_collision_mask>] is enabled, given a `layer_number` between 1 and 32.


----



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_CollisionObject3D_method_get_rid>]

Returns the object's [RID<class_RID>].


----



[PackedInt32Array<class_PackedInt32Array>] **get_shape_owners**\ (\ ) [🔗<class_CollisionObject3D_method_get_shape_owners>]

Returns an [Array<class_Array>] of `owner_id` identifiers. You can use these ids in other methods that take `owner_id` as an argument.


----



[bool<class_bool>] **is_shape_owner_disabled**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_is_shape_owner_disabled>]

If `true`, the shape owner and its shapes are disabled.


----



|void| **remove_shape_owner**\ (\ owner_id\: [int<class_int>]\ ) [🔗<class_CollisionObject3D_method_remove_shape_owner>]

Removes the given shape owner.


----



|void| **set_collision_layer_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_CollisionObject3D_method_set_collision_layer_value>]

Based on `value`, enables or disables the specified layer in the [collision_layer<class_CollisionObject3D_property_collision_layer>], given a `layer_number` between 1 and 32.


----



|void| **set_collision_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_CollisionObject3D_method_set_collision_mask_value>]

Based on `value`, enables or disables the specified layer in the [collision_mask<class_CollisionObject3D_property_collision_mask>], given a `layer_number` between 1 and 32.


----



[int<class_int>] **shape_find_owner**\ (\ shape_index\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_shape_find_owner>]

Returns the `owner_id` of the given shape.


----



|void| **shape_owner_add_shape**\ (\ owner_id\: [int<class_int>], shape\: [Shape3D<class_Shape3D>]\ ) [🔗<class_CollisionObject3D_method_shape_owner_add_shape>]

Adds a [Shape3D<class_Shape3D>] to the shape owner.


----



|void| **shape_owner_clear_shapes**\ (\ owner_id\: [int<class_int>]\ ) [🔗<class_CollisionObject3D_method_shape_owner_clear_shapes>]

Removes all shapes from the shape owner.


----



[Object<class_Object>] **shape_owner_get_owner**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_shape_owner_get_owner>]

Returns the parent object of the given shape owner.


----



[Shape3D<class_Shape3D>] **shape_owner_get_shape**\ (\ owner_id\: [int<class_int>], shape_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_shape_owner_get_shape>]

Returns the [Shape3D<class_Shape3D>] with the given ID from the given shape owner.


----



[int<class_int>] **shape_owner_get_shape_count**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_shape_owner_get_shape_count>]

Returns the number of shapes the given shape owner contains.


----



[int<class_int>] **shape_owner_get_shape_index**\ (\ owner_id\: [int<class_int>], shape_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_shape_owner_get_shape_index>]

Returns the child index of the [Shape3D<class_Shape3D>] with the given ID from the given shape owner.


----



[Transform3D<class_Transform3D>] **shape_owner_get_transform**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject3D_method_shape_owner_get_transform>]

Returns the shape owner's [Transform3D<class_Transform3D>].


----



|void| **shape_owner_remove_shape**\ (\ owner_id\: [int<class_int>], shape_id\: [int<class_int>]\ ) [🔗<class_CollisionObject3D_method_shape_owner_remove_shape>]

Removes a shape from the given shape owner.


----



|void| **shape_owner_set_disabled**\ (\ owner_id\: [int<class_int>], disabled\: [bool<class_bool>]\ ) [🔗<class_CollisionObject3D_method_shape_owner_set_disabled>]

If `true`, disables the given shape owner.


----



|void| **shape_owner_set_transform**\ (\ owner_id\: [int<class_int>], transform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_CollisionObject3D_method_shape_owner_set_transform>]

Sets the [Transform3D<class_Transform3D>] of the given shape owner.

