# PhysicsBody2D in English

# PhysicsBody2D

Inherits:CollisionObject2D<Node2D<CanvasItem<Node<Object
Inherited By:CharacterBody2D,RigidBody2D,StaticBody2D
Abstract base class for 2D game objects affected by physics.

## Description

PhysicsBody2Dis an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.

## Tutorials

- Physics introduction
Physics introduction
- Troubleshooting physics issues
Troubleshooting physics issues

## Properties

| bool | input_pickable | false(overridesCollisionObject2D) |

bool
input_pickable
false(overridesCollisionObject2D)

## Methods

| void | add_collision_exception_with(body:Node) |
|---|---|
| Array[PhysicsBody2D] | get_collision_exceptions() |
| Vector2 | get_gravity()const |
| KinematicCollision2D | move_and_collide(motion:Vector2, test_only:bool= false, safe_margin:float= 0.08, recovery_as_collision:bool= false) |
| void | remove_collision_exception_with(body:Node) |
| bool | test_move(from:Transform2D, motion:Vector2, collision:KinematicCollision2D= null, safe_margin:float= 0.08, recovery_as_collision:bool= false) |

void
add_collision_exception_with(body:Node)
Array[PhysicsBody2D]
get_collision_exceptions()
Vector2
get_gravity()const
KinematicCollision2D
move_and_collide(motion:Vector2, test_only:bool= false, safe_margin:float= 0.08, recovery_as_collision:bool= false)
void
remove_collision_exception_with(body:Node)
bool
test_move(from:Transform2D, motion:Vector2, collision:KinematicCollision2D= null, safe_margin:float= 0.08, recovery_as_collision:bool= false)

## Method Descriptions

voidadd_collision_exception_with(body:Node)🔗
Adds a body to the list of bodies that this body can't collide with.
Array[PhysicsBody2D]get_collision_exceptions()🔗
Returns an array of nodes that were added as collision exceptions for this body.
Vector2get_gravity()const🔗
Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides fromArea2Dnodes and the global world gravity.
KinematicCollision2Dmove_and_collide(motion:Vector2, test_only:bool= false, safe_margin:float= 0.08, recovery_as_collision:bool= false)🔗
Moves the body along the vectormotion. In order to be frame rate independent inNode._physics_process()orNode._process(),motionshould be computed usingdelta.
Returns aKinematicCollision2D, which contains information about the collision when stopped, or when touching another body along the motion.
Iftest_onlyistrue, the body does not move but the would-be collision information is given.
safe_marginis the extra margin used for collision recovery (seeCharacterBody2D.safe_marginfor more details).
Ifrecovery_as_collisionistrue, any depenetration from the recovery phase is also reported as a collision; this is used e.g. byCharacterBody2Dfor improving floor detection during floor snapping.
voidremove_collision_exception_with(body:Node)🔗
Removes a body from the list of bodies that this body can't collide with.
booltest_move(from:Transform2D, motion:Vector2, collision:KinematicCollision2D= null, safe_margin:float= 0.08, recovery_as_collision:bool= false)🔗
Checks for collisions without moving the body. In order to be frame rate independent inNode._physics_process()orNode._process(),motionshould be computed usingdelta.
Virtually sets the node's position, scale and rotation to that of the givenTransform2D, then tries to move the body along the vectormotion. Returnstrueif a collision would stop the body from moving along the whole path.
collisionis an optional object of typeKinematicCollision2D, which contains additional information about the collision when stopped, or when touching another body along the motion.
safe_marginis the extra margin used for collision recovery (seeCharacterBody2D.safe_marginfor more details).
Ifrecovery_as_collisionistrue, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body wouldtouchany other bodies.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
