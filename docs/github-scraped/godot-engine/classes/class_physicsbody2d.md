:github_url: hide



# PhysicsBody2D

**Inherits:** [CollisionObject2D<class_CollisionObject2D>] **<** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [CharacterBody2D<class_CharacterBody2D>], [RigidBody2D<class_RigidBody2D>], [StaticBody2D<class_StaticBody2D>]

Abstract base class for 2D game objects affected by physics.


## Description

**PhysicsBody2D** is an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [../tutorials/physics/troubleshooting_physics_issues](Troubleshooting physics issues .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | input_pickable | ``false`` (overrides :ref:`CollisionObject2D<class_CollisionObject2D_property_input_pickable>`) |
> +-------------------------+----------------+-------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`add_collision_exception_with<class_PhysicsBody2D_method_add_collision_exception_with>`\ (\ body\: :ref:`Node<class_Node>`\ )                                                                                                                                                                                                      |
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PhysicsBody2D<class_PhysicsBody2D>`\] | :ref:`get_collision_exceptions<class_PhysicsBody2D_method_get_collision_exceptions>`\ (\ )                                                                                                                                                                                                                                              |
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                          | :ref:`get_gravity<class_PhysicsBody2D_method_get_gravity>`\ (\ ) |const|                                                                                                                                                                                                                                                                |
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`KinematicCollision2D<class_KinematicCollision2D>`                | :ref:`move_and_collide<class_PhysicsBody2D_method_move_and_collide>`\ (\ motion\: :ref:`Vector2<class_Vector2>`, test_only\: :ref:`bool<class_bool>` = false, safe_margin\: :ref:`float<class_float>` = 0.08, recovery_as_collision\: :ref:`bool<class_bool>` = false\ )                                                                |
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`remove_collision_exception_with<class_PhysicsBody2D_method_remove_collision_exception_with>`\ (\ body\: :ref:`Node<class_Node>`\ )                                                                                                                                                                                                |
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                | :ref:`test_move<class_PhysicsBody2D_method_test_move>`\ (\ from\: :ref:`Transform2D<class_Transform2D>`, motion\: :ref:`Vector2<class_Vector2>`, collision\: :ref:`KinematicCollision2D<class_KinematicCollision2D>` = null, safe_margin\: :ref:`float<class_float>` = 0.08, recovery_as_collision\: :ref:`bool<class_bool>` = false\ ) |
> +------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_collision_exception_with**\ (\ body\: [Node<class_Node>]\ ) [🔗<class_PhysicsBody2D_method_add_collision_exception_with>]

Adds a body to the list of bodies that this body can't collide with.


----



[Array<class_Array>]\[[PhysicsBody2D<class_PhysicsBody2D>]\] **get_collision_exceptions**\ (\ ) [🔗<class_PhysicsBody2D_method_get_collision_exceptions>]

Returns an array of nodes that were added as collision exceptions for this body.


----



[Vector2<class_Vector2>] **get_gravity**\ (\ ) |const| [🔗<class_PhysicsBody2D_method_get_gravity>]

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from [Area2D<class_Area2D>] nodes and the global world gravity.


----



[KinematicCollision2D<class_KinematicCollision2D>] **move_and_collide**\ (\ motion\: [Vector2<class_Vector2>], test_only\: [bool<class_bool>] = false, safe_margin\: [float<class_float>] = 0.08, recovery_as_collision\: [bool<class_bool>] = false\ ) [🔗<class_PhysicsBody2D_method_move_and_collide>]

Moves the body along the vector `motion`. In order to be frame rate independent in [Node._physics_process()<class_Node_private_method__physics_process>] or [Node._process()<class_Node_private_method__process>], `motion` should be computed using `delta`.

Returns a [KinematicCollision2D<class_KinematicCollision2D>], which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

\ `safe_margin` is the extra margin used for collision recovery (see [CharacterBody2D.safe_margin<class_CharacterBody2D_property_safe_margin>] for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by [CharacterBody2D<class_CharacterBody2D>] for improving floor detection during floor snapping.


----



|void| **remove_collision_exception_with**\ (\ body\: [Node<class_Node>]\ ) [🔗<class_PhysicsBody2D_method_remove_collision_exception_with>]

Removes a body from the list of bodies that this body can't collide with.


----



[bool<class_bool>] **test_move**\ (\ from\: [Transform2D<class_Transform2D>], motion\: [Vector2<class_Vector2>], collision\: [KinematicCollision2D<class_KinematicCollision2D>] = null, safe_margin\: [float<class_float>] = 0.08, recovery_as_collision\: [bool<class_bool>] = false\ ) [🔗<class_PhysicsBody2D_method_test_move>]

Checks for collisions without moving the body. In order to be frame rate independent in [Node._physics_process()<class_Node_private_method__physics_process>] or [Node._process()<class_Node_private_method__process>], `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given [Transform2D<class_Transform2D>], then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

\ `collision` is an optional object of type [KinematicCollision2D<class_KinematicCollision2D>], which contains additional information about the collision when stopped, or when touching another body along the motion.

\ `safe_margin` is the extra margin used for collision recovery (see [CharacterBody2D.safe_margin<class_CharacterBody2D_property_safe_margin>] for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.

