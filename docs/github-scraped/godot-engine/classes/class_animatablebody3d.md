:github_url: hide



# AnimatableBody3D

**Inherits:** [StaticBody3D<class_StaticBody3D>] **<** [PhysicsBody3D<class_PhysicsBody3D>] **<** [CollisionObject3D<class_CollisionObject3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A 3D physics body that can't be moved by external forces. When moved manually, it affects other bodies in its path.


## Description

An animatable 3D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, [AnimationMixer<class_AnimationMixer>]\ s (with [AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>] set to [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>]), and [RemoteTransform3D<class_RemoteTransform3D>].

When **AnimatableBody3D** is moved, its linear and angular velocity are estimated and used to affect other physics bodies in its path. This makes it useful for moving platforms, doors, and other moving objects.


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [../tutorials/physics/troubleshooting_physics_issues](Troubleshooting physics issues .md)

- [3D Physics Tests Demo ](https://godotengine.org/asset-library/asset/2747)_

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>` | :ref:`sync_to_physics<class_AnimatableBody3D_property_sync_to_physics>` | ``true`` |
> +-------------------------+-------------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[bool<class_bool>] **sync_to_physics** = `true` [🔗<class_AnimatableBody3D_property_sync_to_physics>]


- |void| **set_sync_to_physics**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_sync_to_physics_enabled**\ (\ )

If `true`, the body's movement will be synchronized to the physics frame. This is useful when animating movement via [AnimationPlayer<class_AnimationPlayer>], for example on moving platforms. Do **not** use together with [PhysicsBody3D.move_and_collide()<class_PhysicsBody3D_method_move_and_collide>].

