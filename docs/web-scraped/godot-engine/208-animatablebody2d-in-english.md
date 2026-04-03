# AnimatableBody2D in English

# AnimatableBody2D

Inherits:StaticBody2D<PhysicsBody2D<CollisionObject2D<Node2D<CanvasItem<Node<Object
A 2D physics body that can't be moved by external forces. When moved manually, it affects other bodies in its path.

## Description

An animatable 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code,AnimationMixers (withAnimationMixer.callback_mode_processset toAnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS), andRemoteTransform2D.
WhenAnimatableBody2Dis moved, its linear and angular velocity are estimated and used to affect other physics bodies in its path. This makes it useful for moving platforms, doors, and other moving objects.

## Tutorials

- Physics introduction
Physics introduction
- Troubleshooting physics issues
Troubleshooting physics issues

## Properties

| bool | sync_to_physics | true |

bool
sync_to_physics
true

## Property Descriptions

boolsync_to_physics=true🔗

- voidset_sync_to_physics(value:bool)
voidset_sync_to_physics(value:bool)
- boolis_sync_to_physics_enabled()
boolis_sync_to_physics_enabled()
Iftrue, the body's movement will be synchronized to the physics frame. This is useful when animating movement viaAnimationPlayer, for example on moving platforms. Donotuse together withPhysicsBody2D.move_and_collide().

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
