:github_url: hide



# AnimatableBody2D

**Inherits:** [StaticBody2D<class_StaticBody2D>] **<** [PhysicsBody2D<class_PhysicsBody2D>] **<** [CollisionObject2D<class_CollisionObject2D>] **<** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A 2D physics body that can't be moved by external forces. When moved manually, it affects other bodies in its path.


## Description

An animatable 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, [AnimationMixer<class_AnimationMixer>]\ s (with [AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>] set to [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>]), and [RemoteTransform2D<class_RemoteTransform2D>].

When **AnimatableBody2D** is moved, its linear and angular velocity are estimated and used to affect other physics bodies in its path. This makes it useful for moving platforms, doors, and other moving objects.


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [../tutorials/physics/troubleshooting_physics_issues](Troubleshooting physics issues .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>` | :ref:`sync_to_physics<class_AnimatableBody2D_property_sync_to_physics>` | ``true`` |
> +-------------------------+-------------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[bool<class_bool>] **sync_to_physics** = `true` [🔗<class_AnimatableBody2D_property_sync_to_physics>]


- |void| **set_sync_to_physics**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_sync_to_physics_enabled**\ (\ )

If `true`, the body's movement will be synchronized to the physics frame. This is useful when animating movement via [AnimationPlayer<class_AnimationPlayer>], for example on moving platforms. Do **not** use together with [PhysicsBody2D.move_and_collide()<class_PhysicsBody2D_method_move_and_collide>].

