:github_url: hide



# CollisionObject2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [Area2D<class_Area2D>], [PhysicsBody2D<class_PhysicsBody2D>]

Abstract base class for 2D physics objects.


## Description

Abstract base class for 2D physics objects. **CollisionObject2D** can hold any number of [Shape2D<class_Shape2D>]\ s for collision. Each shape must be assigned to a *shape owner*. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the `shape_owner_*` methods.

\ **Note:** Only collisions between objects within the same canvas ([Viewport<class_Viewport>] canvas or [CanvasLayer<class_CanvasLayer>]) are supported. The behavior of collisions between objects in different canvases is undefined.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`                                  | :ref:`collision_layer<class_CollisionObject2D_property_collision_layer>`       | ``1``    |
> +--------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`                                  | :ref:`collision_mask<class_CollisionObject2D_property_collision_mask>`         | ``1``    |
> +--------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`                              | :ref:`collision_priority<class_CollisionObject2D_property_collision_priority>` | ``1.0``  |
> +--------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`DisableMode<enum_CollisionObject2D_DisableMode>` | :ref:`disable_mode<class_CollisionObject2D_property_disable_mode>`             | ``0``    |
> +--------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`                                | :ref:`input_pickable<class_CollisionObject2D_property_input_pickable>`         | ``true`` |
> +--------------------------------------------------------+--------------------------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_input_event<class_CollisionObject2D_private_method__input_event>`\ (\ viewport\: :ref:`Viewport<class_Viewport>`, event\: :ref:`InputEvent<class_InputEvent>`, shape_idx\: :ref:`int<class_int>`\ ) |virtual| |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_mouse_enter<class_CollisionObject2D_private_method__mouse_enter>`\ (\ ) |virtual|                                                                                                                             |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_mouse_exit<class_CollisionObject2D_private_method__mouse_exit>`\ (\ ) |virtual|                                                                                                                               |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_mouse_shape_enter<class_CollisionObject2D_private_method__mouse_shape_enter>`\ (\ shape_idx\: :ref:`int<class_int>`\ ) |virtual|                                                                              |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`_mouse_shape_exit<class_CollisionObject2D_private_method__mouse_shape_exit>`\ (\ shape_idx\: :ref:`int<class_int>`\ ) |virtual|                                                                                |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`create_shape_owner<class_CollisionObject2D_method_create_shape_owner>`\ (\ owner\: :ref:`Object<class_Object>`\ )                                                                                              |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`get_collision_layer_value<class_CollisionObject2D_method_get_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                                                                       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`get_collision_mask_value<class_CollisionObject2D_method_get_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                                                                         |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                           | :ref:`get_rid<class_CollisionObject2D_method_get_rid>`\ (\ ) |const|                                                                                                                                                 |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                       | :ref:`get_shape_owner_one_way_collision_margin<class_CollisionObject2D_method_get_shape_owner_one_way_collision_margin>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                             |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`get_shape_owners<class_CollisionObject2D_method_get_shape_owners>`\ (\ )                                                                                                                                       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_shape_owner_disabled<class_CollisionObject2D_method_is_shape_owner_disabled>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_shape_owner_one_way_collision_enabled<class_CollisionObject2D_method_is_shape_owner_one_way_collision_enabled>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                             |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`remove_shape_owner<class_CollisionObject2D_method_remove_shape_owner>`\ (\ owner_id\: :ref:`int<class_int>`\ )                                                                                                 |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`set_collision_layer_value<class_CollisionObject2D_method_set_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )                                              |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`set_collision_mask_value<class_CollisionObject2D_method_set_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )                                                |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`shape_find_owner<class_CollisionObject2D_method_shape_find_owner>`\ (\ shape_index\: :ref:`int<class_int>`\ ) |const|                                                                                          |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_add_shape<class_CollisionObject2D_method_shape_owner_add_shape>`\ (\ owner_id\: :ref:`int<class_int>`, shape\: :ref:`Shape2D<class_Shape2D>`\ )                                                    |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_clear_shapes<class_CollisionObject2D_method_shape_owner_clear_shapes>`\ (\ owner_id\: :ref:`int<class_int>`\ )                                                                                     |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                     | :ref:`shape_owner_get_owner<class_CollisionObject2D_method_shape_owner_get_owner>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                                   |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Shape2D<class_Shape2D>`                   | :ref:`shape_owner_get_shape<class_CollisionObject2D_method_shape_owner_get_shape>`\ (\ owner_id\: :ref:`int<class_int>`, shape_id\: :ref:`int<class_int>`\ ) |const|                                                 |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`shape_owner_get_shape_count<class_CollisionObject2D_method_shape_owner_get_shape_count>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`shape_owner_get_shape_index<class_CollisionObject2D_method_shape_owner_get_shape_index>`\ (\ owner_id\: :ref:`int<class_int>`, shape_id\: :ref:`int<class_int>`\ ) |const|                                     |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform2D<class_Transform2D>`           | :ref:`shape_owner_get_transform<class_CollisionObject2D_method_shape_owner_get_transform>`\ (\ owner_id\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_remove_shape<class_CollisionObject2D_method_shape_owner_remove_shape>`\ (\ owner_id\: :ref:`int<class_int>`, shape_id\: :ref:`int<class_int>`\ )                                                   |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_set_disabled<class_CollisionObject2D_method_shape_owner_set_disabled>`\ (\ owner_id\: :ref:`int<class_int>`, disabled\: :ref:`bool<class_bool>`\ )                                                 |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_set_one_way_collision<class_CollisionObject2D_method_shape_owner_set_one_way_collision>`\ (\ owner_id\: :ref:`int<class_int>`, enable\: :ref:`bool<class_bool>`\ )                                 |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_set_one_way_collision_margin<class_CollisionObject2D_method_shape_owner_set_one_way_collision_margin>`\ (\ owner_id\: :ref:`int<class_int>`, margin\: :ref:`float<class_float>`\ )                 |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`shape_owner_set_transform<class_CollisionObject2D_method_shape_owner_set_transform>`\ (\ owner_id\: :ref:`int<class_int>`, transform\: :ref:`Transform2D<class_Transform2D>`\ )                                |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**input_event**\ (\ viewport\: [Node<class_Node>], event\: [InputEvent<class_InputEvent>], shape_idx\: [int<class_int>]\ ) [🔗<class_CollisionObject2D_signal_input_event>]

Emitted when an input event occurs. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set. See [_input_event()<class_CollisionObject2D_private_method__input_event>] for details.


----



**mouse_entered**\ (\ ) [🔗<class_CollisionObject2D_signal_mouse_entered>]

Emitted when the mouse pointer enters any of this object's shapes. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this signal to be emitted.

\ **Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject2D**'s area is small. This signal may also not be emitted if another **CollisionObject2D** is overlapping the **CollisionObject2D** in question.


----



**mouse_exited**\ (\ ) [🔗<class_CollisionObject2D_signal_mouse_exited>]

Emitted when the mouse pointer exits all this object's shapes. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this signal to be emitted.

\ **Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject2D**'s area is small. This signal may also not be emitted if another **CollisionObject2D** is overlapping the **CollisionObject2D** in question.


----



**mouse_shape_entered**\ (\ shape_idx\: [int<class_int>]\ ) [🔗<class_CollisionObject2D_signal_mouse_shape_entered>]

Emitted when the mouse pointer enters any of this object's shapes or moves from one shape to another. `shape_idx` is the child index of the newly entered [Shape2D<class_Shape2D>]. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set.


----



**mouse_shape_exited**\ (\ shape_idx\: [int<class_int>]\ ) [🔗<class_CollisionObject2D_signal_mouse_shape_exited>]

Emitted when the mouse pointer exits any of this object's shapes. `shape_idx` is the child index of the exited [Shape2D<class_Shape2D>]. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set.


----


## Enumerations



enum **DisableMode**: [🔗<enum_CollisionObject2D_DisableMode>]



[DisableMode<enum_CollisionObject2D_DisableMode>] **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], remove from the physics simulation to stop all physics interactions with this **CollisionObject2D**.

Automatically re-added to the physics simulation when the [Node<class_Node>] is processed again.



[DisableMode<enum_CollisionObject2D_DisableMode>] **DISABLE_MODE_MAKE_STATIC** = `1`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], make the body static. Doesn't affect [Area2D<class_Area2D>]. [PhysicsBody2D<class_PhysicsBody2D>] can't be affected by forces or other bodies while static.

Automatically set [PhysicsBody2D<class_PhysicsBody2D>] back to its original mode when the [Node<class_Node>] is processed again.



[DisableMode<enum_CollisionObject2D_DisableMode>] **DISABLE_MODE_KEEP_ACTIVE** = `2`

When [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>], do not affect the physics simulation.


----


## Property Descriptions



[int<class_int>] **collision_layer** = `1` [🔗<class_CollisionObject2D_property_collision_layer>]


- |void| **set_collision_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_layer**\ (\ )

The physics layers this CollisionObject2D is in. Collision objects can exist in one or more of 32 different layers. See also [collision_mask<class_CollisionObject2D_property_collision_mask>].

\ **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[int<class_int>] **collision_mask** = `1` [🔗<class_CollisionObject2D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers this CollisionObject2D scans. Collision objects can scan one or more of 32 different layers. See also [collision_layer<class_CollisionObject2D_property_collision_layer>].

\ **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[float<class_float>] **collision_priority** = `1.0` [🔗<class_CollisionObject2D_property_collision_priority>]


- |void| **set_collision_priority**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_collision_priority**\ (\ )

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.


----



[DisableMode<enum_CollisionObject2D_DisableMode>] **disable_mode** = `0` [🔗<class_CollisionObject2D_property_disable_mode>]


- |void| **set_disable_mode**\ (\ value\: [DisableMode<enum_CollisionObject2D_DisableMode>]\ )
- [DisableMode<enum_CollisionObject2D_DisableMode>] **get_disable_mode**\ (\ )

Defines the behavior in physics when [Node.process_mode<class_Node_property_process_mode>] is set to [Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>].


----



[bool<class_bool>] **input_pickable** = `true` [🔗<class_CollisionObject2D_property_input_pickable>]


- |void| **set_pickable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pickable**\ (\ )

If `true`, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set.


----


## Method Descriptions



|void| **_input_event**\ (\ viewport\: [Viewport<class_Viewport>], event\: [InputEvent<class_InputEvent>], shape_idx\: [int<class_int>]\ ) |virtual| [🔗<class_CollisionObject2D_private_method__input_event>]

Accepts unhandled [InputEvent<class_InputEvent>]\ s. `shape_idx` is the child index of the clicked [Shape2D<class_Shape2D>]. Connect to [input_event<class_CollisionObject2D_signal_input_event>] to easily pick up these events.

\ **Note:** [_input_event()<class_CollisionObject2D_private_method__input_event>] requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set.


----



|void| **_mouse_enter**\ (\ ) |virtual| [🔗<class_CollisionObject2D_private_method__mouse_enter>]

Called when the mouse pointer enters any of this object's shapes. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this function to be called.


----



|void| **_mouse_exit**\ (\ ) |virtual| [🔗<class_CollisionObject2D_private_method__mouse_exit>]

Called when the mouse pointer exits all this object's shapes. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this function to be called.


----



|void| **_mouse_shape_enter**\ (\ shape_idx\: [int<class_int>]\ ) |virtual| [🔗<class_CollisionObject2D_private_method__mouse_shape_enter>]

Called when the mouse pointer enters any of this object's shapes or moves from one shape to another. `shape_idx` is the child index of the newly entered [Shape2D<class_Shape2D>]. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be called.


----



|void| **_mouse_shape_exit**\ (\ shape_idx\: [int<class_int>]\ ) |virtual| [🔗<class_CollisionObject2D_private_method__mouse_shape_exit>]

Called when the mouse pointer exits any of this object's shapes. `shape_idx` is the child index of the exited [Shape2D<class_Shape2D>]. Requires [input_pickable<class_CollisionObject2D_property_input_pickable>] to be `true` and at least one [collision_layer<class_CollisionObject2D_property_collision_layer>] bit to be called.


----



[int<class_int>] **create_shape_owner**\ (\ owner\: [Object<class_Object>]\ ) [🔗<class_CollisionObject2D_method_create_shape_owner>]

Creates a new shape owner for the given object. Returns `owner_id` of the new owner for future reference.


----



[bool<class_bool>] **get_collision_layer_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_get_collision_layer_value>]

Returns whether or not the specified layer of the [collision_layer<class_CollisionObject2D_property_collision_layer>] is enabled, given a `layer_number` between 1 and 32.


----



[bool<class_bool>] **get_collision_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_get_collision_mask_value>]

Returns whether or not the specified layer of the [collision_mask<class_CollisionObject2D_property_collision_mask>] is enabled, given a `layer_number` between 1 and 32.


----



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_CollisionObject2D_method_get_rid>]

Returns the object's [RID<class_RID>].


----



[float<class_float>] **get_shape_owner_one_way_collision_margin**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_get_shape_owner_one_way_collision_margin>]

Returns the `one_way_collision_margin` of the shape owner identified by given `owner_id`.


----



[PackedInt32Array<class_PackedInt32Array>] **get_shape_owners**\ (\ ) [🔗<class_CollisionObject2D_method_get_shape_owners>]

Returns an [Array<class_Array>] of `owner_id` identifiers. You can use these ids in other methods that take `owner_id` as an argument.


----



[bool<class_bool>] **is_shape_owner_disabled**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_is_shape_owner_disabled>]

If `true`, the shape owner and its shapes are disabled.


----



[bool<class_bool>] **is_shape_owner_one_way_collision_enabled**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_is_shape_owner_one_way_collision_enabled>]

Returns `true` if collisions for the shape owner originating from this **CollisionObject2D** will not be reported to collided with **CollisionObject2D**\ s.


----



|void| **remove_shape_owner**\ (\ owner_id\: [int<class_int>]\ ) [🔗<class_CollisionObject2D_method_remove_shape_owner>]

Removes the given shape owner.


----



|void| **set_collision_layer_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_CollisionObject2D_method_set_collision_layer_value>]

Based on `value`, enables or disables the specified layer in the [collision_layer<class_CollisionObject2D_property_collision_layer>], given a `layer_number` between 1 and 32.


----



|void| **set_collision_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_CollisionObject2D_method_set_collision_mask_value>]

Based on `value`, enables or disables the specified layer in the [collision_mask<class_CollisionObject2D_property_collision_mask>], given a `layer_number` between 1 and 32.


----



[int<class_int>] **shape_find_owner**\ (\ shape_index\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_shape_find_owner>]

Returns the `owner_id` of the given shape.


----



|void| **shape_owner_add_shape**\ (\ owner_id\: [int<class_int>], shape\: [Shape2D<class_Shape2D>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_add_shape>]

Adds a [Shape2D<class_Shape2D>] to the shape owner.


----



|void| **shape_owner_clear_shapes**\ (\ owner_id\: [int<class_int>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_clear_shapes>]

Removes all shapes from the shape owner.


----



[Object<class_Object>] **shape_owner_get_owner**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_shape_owner_get_owner>]

Returns the parent object of the given shape owner.


----



[Shape2D<class_Shape2D>] **shape_owner_get_shape**\ (\ owner_id\: [int<class_int>], shape_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_shape_owner_get_shape>]

Returns the [Shape2D<class_Shape2D>] with the given ID from the given shape owner.


----



[int<class_int>] **shape_owner_get_shape_count**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_shape_owner_get_shape_count>]

Returns the number of shapes the given shape owner contains.


----



[int<class_int>] **shape_owner_get_shape_index**\ (\ owner_id\: [int<class_int>], shape_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_shape_owner_get_shape_index>]

Returns the child index of the [Shape2D<class_Shape2D>] with the given ID from the given shape owner.


----



[Transform2D<class_Transform2D>] **shape_owner_get_transform**\ (\ owner_id\: [int<class_int>]\ ) |const| [🔗<class_CollisionObject2D_method_shape_owner_get_transform>]

Returns the shape owner's [Transform2D<class_Transform2D>].


----



|void| **shape_owner_remove_shape**\ (\ owner_id\: [int<class_int>], shape_id\: [int<class_int>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_remove_shape>]

Removes a shape from the given shape owner.


----



|void| **shape_owner_set_disabled**\ (\ owner_id\: [int<class_int>], disabled\: [bool<class_bool>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_set_disabled>]

If `true`, disables the given shape owner.


----



|void| **shape_owner_set_one_way_collision**\ (\ owner_id\: [int<class_int>], enable\: [bool<class_bool>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_set_one_way_collision>]

If `enable` is `true`, collisions for the shape owner originating from this **CollisionObject2D** will not be reported to collided with **CollisionObject2D**\ s.


----



|void| **shape_owner_set_one_way_collision_margin**\ (\ owner_id\: [int<class_int>], margin\: [float<class_float>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_set_one_way_collision_margin>]

Sets the `one_way_collision_margin` of the shape owner identified by given `owner_id` to `margin` pixels.


----



|void| **shape_owner_set_transform**\ (\ owner_id\: [int<class_int>], transform\: [Transform2D<class_Transform2D>]\ ) [🔗<class_CollisionObject2D_method_shape_owner_set_transform>]

Sets the [Transform2D<class_Transform2D>] of the given shape owner.

