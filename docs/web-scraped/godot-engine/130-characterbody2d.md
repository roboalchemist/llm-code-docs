# CharacterBody2D

# CharacterBody2D

Inherits:PhysicsBody2D<CollisionObject2D<Node2D<CanvasItem<Node<Object
A 2D physics body specialized for characters moved by script.

## Description

CharacterBody2Dis a specialized class for physics bodies that are meant to be user-controlled. They are not affected by physics at all, but they affect other physics bodies in their path. They are mainly used to provide high-level API to move objects with wall and slope detection (move_and_slide()method) in addition to the general collision detection provided byPhysicsBody2D.move_and_collide(). This makes it useful for highly configurable physics bodies that must move in specific ways and collide with the world, as is often the case with user-controlled characters.
For game objects that don't require complex movement or collision detection, such as moving platforms,AnimatableBody2Dis simpler to configure.

## Tutorials

- Physics introduction
Physics introduction
- Troubleshooting physics issues
Troubleshooting physics issues
- Kinematic character (2D)
Kinematic character (2D)
- Using CharacterBody2D
Using CharacterBody2D
- 2D Kinematic Character Demo
2D Kinematic Character Demo
- 2D Platformer Demo
2D Platformer Demo

## Properties

| bool | floor_block_on_wall | true |
|---|---|---|
| bool | floor_constant_speed | false |
| float | floor_max_angle | 0.7853982 |
| float | floor_snap_length | 1.0 |
| bool | floor_stop_on_slope | true |
| int | max_slides | 4 |
| MotionMode | motion_mode | 0 |
| int | platform_floor_layers | 4294967295 |
| PlatformOnLeave | platform_on_leave | 0 |
| int | platform_wall_layers | 0 |
| float | safe_margin | 0.08 |
| bool | slide_on_ceiling | true |
| Vector2 | up_direction | Vector2(0,-1) |
| Vector2 | velocity | Vector2(0,0) |
| float | wall_min_slide_angle | 0.2617994 |

bool
floor_block_on_wall
true
bool
floor_constant_speed
false
float
floor_max_angle
0.7853982
float
floor_snap_length
bool
floor_stop_on_slope
true
max_slides
MotionMode
motion_mode
platform_floor_layers
4294967295
PlatformOnLeave
platform_on_leave
platform_wall_layers
float
safe_margin
0.08
bool
slide_on_ceiling
true
Vector2
up_direction
Vector2(0,-1)
Vector2
velocity
Vector2(0,0)
float
wall_min_slide_angle
0.2617994

## Methods

| void | apply_floor_snap() |
|---|---|
| float | get_floor_angle(up_direction:Vector2= Vector2(0, -1))const |
| Vector2 | get_floor_normal()const |
| Vector2 | get_last_motion()const |
| KinematicCollision2D | get_last_slide_collision() |
| Vector2 | get_platform_velocity()const |
| Vector2 | get_position_delta()const |
| Vector2 | get_real_velocity()const |
| KinematicCollision2D | get_slide_collision(slide_idx:int) |
| int | get_slide_collision_count()const |
| Vector2 | get_wall_normal()const |
| bool | is_on_ceiling()const |
| bool | is_on_ceiling_only()const |
| bool | is_on_floor()const |
| bool | is_on_floor_only()const |
| bool | is_on_wall()const |
| bool | is_on_wall_only()const |
| bool | move_and_slide() |

void
apply_floor_snap()
float
get_floor_angle(up_direction:Vector2= Vector2(0, -1))const
Vector2
get_floor_normal()const
Vector2
get_last_motion()const
KinematicCollision2D
get_last_slide_collision()
Vector2
get_platform_velocity()const
Vector2
get_position_delta()const
Vector2
get_real_velocity()const
KinematicCollision2D
get_slide_collision(slide_idx:int)
get_slide_collision_count()const
Vector2
get_wall_normal()const
bool
is_on_ceiling()const
bool
is_on_ceiling_only()const
bool
is_on_floor()const
bool
is_on_floor_only()const
bool
is_on_wall()const
bool
is_on_wall_only()const
bool
move_and_slide()

## Enumerations

enumMotionMode:🔗
MotionModeMOTION_MODE_GROUNDED=0
Apply when notions of walls, ceiling and floor are relevant. In this mode the body motion will react to slopes (acceleration/slowdown). This mode is suitable for sided games like platformers.
MotionModeMOTION_MODE_FLOATING=1
Apply when there is no notion of floor or ceiling. All collisions will be reported ason_wall. In this mode, when you slide, the speed will always be constant. This mode is suitable for top-down games.
enumPlatformOnLeave:🔗
PlatformOnLeavePLATFORM_ON_LEAVE_ADD_VELOCITY=0
Add the last platform velocity to thevelocitywhen you leave a moving platform.
PlatformOnLeavePLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY=1
Add the last platform velocity to thevelocitywhen you leave a moving platform, but any downward motion is ignored. It's useful to keep full jump height even when the platform is moving down.
PlatformOnLeavePLATFORM_ON_LEAVE_DO_NOTHING=2
Do nothing when leaving a platform.

## Property Descriptions

boolfloor_block_on_wall=true🔗

- voidset_floor_block_on_wall_enabled(value:bool)
voidset_floor_block_on_wall_enabled(value:bool)
- boolis_floor_block_on_wall_enabled()
boolis_floor_block_on_wall_enabled()
Iftrue, the body will be able to move on the floor only. This option avoids to be able to walk on walls, it will however allow to slide down along them.
boolfloor_constant_speed=false🔗
- voidset_floor_constant_speed_enabled(value:bool)
voidset_floor_constant_speed_enabled(value:bool)
- boolis_floor_constant_speed_enabled()
boolis_floor_constant_speed_enabled()
Iffalse(by default), the body will move faster on downward slopes and slower on upward slopes.
Iftrue, the body will always move at the same speed on the ground no matter the slope. Note that you need to usefloor_snap_lengthto stick along a downward slope at constant speed.
floatfloor_max_angle=0.7853982🔗
- voidset_floor_max_angle(value:float)
voidset_floor_max_angle(value:float)
- floatget_floor_max_angle()
floatget_floor_max_angle()
Maximum angle (in radians) where a slope is still considered a floor (or a ceiling), rather than a wall, when callingmove_and_slide(). The default value equals 45 degrees.
floatfloor_snap_length=1.0🔗
- voidset_floor_snap_length(value:float)
voidset_floor_snap_length(value:float)
- floatget_floor_snap_length()
floatget_floor_snap_length()
Sets a snapping distance. When set to a value different from0.0, the body is kept attached to slopes when callingmove_and_slide(). The snapping vector is determined by the given distance along the opposite direction of theup_direction.
As long as the snapping vector is in contact with the ground and the body moves againstup_direction, the body will remain attached to the surface. Snapping is not applied if the body moves alongup_direction, meaning it contains vertical rising velocity, so it will be able to detach from the ground when jumping or when the body is pushed up by something. If you want to apply a snap without taking into account the velocity, useapply_floor_snap().
boolfloor_stop_on_slope=true🔗
- voidset_floor_stop_on_slope_enabled(value:bool)
voidset_floor_stop_on_slope_enabled(value:bool)
- boolis_floor_stop_on_slope_enabled()
boolis_floor_stop_on_slope_enabled()
Iftrue, the body will not slide on slopes when callingmove_and_slide()when the body is standing still.
Iffalse, the body will slide on floor's slopes whenvelocityapplies a downward force.
intmax_slides=4🔗
- voidset_max_slides(value:int)
voidset_max_slides(value:int)
- intget_max_slides()
intget_max_slides()
Maximum number of times the body can change direction before it stops when callingmove_and_slide(). Must be greater than zero.
MotionModemotion_mode=0🔗
- voidset_motion_mode(value:MotionMode)
voidset_motion_mode(value:MotionMode)
- MotionModeget_motion_mode()
MotionModeget_motion_mode()
Sets the motion mode which defines the behavior ofmove_and_slide().
intplatform_floor_layers=4294967295🔗
- voidset_platform_floor_layers(value:int)
voidset_platform_floor_layers(value:int)
- intget_platform_floor_layers()
intget_platform_floor_layers()
Collision layers that will be included for detecting floor bodies that will act as moving platforms to be followed by theCharacterBody2D. By default, all floor bodies are detected and propagate their velocity.
PlatformOnLeaveplatform_on_leave=0🔗
- voidset_platform_on_leave(value:PlatformOnLeave)
voidset_platform_on_leave(value:PlatformOnLeave)
- PlatformOnLeaveget_platform_on_leave()
PlatformOnLeaveget_platform_on_leave()
Sets the behavior to apply when you leave a moving platform. By default, to be physically accurate, when you leave the last platform velocity is applied.
intplatform_wall_layers=0🔗
- voidset_platform_wall_layers(value:int)
voidset_platform_wall_layers(value:int)
- intget_platform_wall_layers()
intget_platform_wall_layers()
Collision layers that will be included for detecting wall bodies that will act as moving platforms to be followed by theCharacterBody2D. By default, all wall bodies are ignored.
floatsafe_margin=0.08🔗
- voidset_safe_margin(value:float)
voidset_safe_margin(value:float)
- floatget_safe_margin()
floatget_safe_margin()
Extra margin used for collision recovery when callingmove_and_slide().
If the body is at least this close to another body, it will consider them to be colliding and will be pushed away before performing the actual motion.
A higher value means it's more flexible for detecting collision, which helps with consistently detecting walls and floors.
A lower value forces the collision algorithm to use more exact detection, so it can be used in cases that specifically require precision, e.g at very low scale to avoid visible jittering, or for stability with a stack of character bodies.
boolslide_on_ceiling=true🔗
- voidset_slide_on_ceiling_enabled(value:bool)
voidset_slide_on_ceiling_enabled(value:bool)
- boolis_slide_on_ceiling_enabled()
boolis_slide_on_ceiling_enabled()
Iftrue, during a jump against the ceiling, the body will slide, iffalseit will be stopped and will fall vertically.
Vector2up_direction=Vector2(0,-1)🔗
- voidset_up_direction(value:Vector2)
voidset_up_direction(value:Vector2)
- Vector2get_up_direction()
Vector2get_up_direction()
Vector pointing upwards, used to determine what is a wall and what is a floor (or a ceiling) when callingmove_and_slide(). Defaults toVector2.UP. As the vector will be normalized it can't be equal toVector2.ZERO, if you want all collisions to be reported as walls, consider usingMOTION_MODE_FLOATINGasmotion_mode.
Vector2velocity=Vector2(0,0)🔗
- voidset_velocity(value:Vector2)
voidset_velocity(value:Vector2)
- Vector2get_velocity()
Vector2get_velocity()
Current velocity vector in pixels per second, used and modified during calls tomove_and_slide().
Note:A common mistake is setting this property to the desired velocity multiplied bydelta, which produces a motion vector in pixels.
floatwall_min_slide_angle=0.2617994🔗
- voidset_wall_min_slide_angle(value:float)
voidset_wall_min_slide_angle(value:float)
- floatget_wall_min_slide_angle()
floatget_wall_min_slide_angle()
Minimum angle (in radians) where the body is allowed to slide when it encounters a wall. The default value equals 15 degrees. This property only affects movement whenmotion_modeisMOTION_MODE_FLOATING.

## Method Descriptions

voidapply_floor_snap()🔗
Allows to manually apply a snap to the floor regardless of the body's velocity. This function does nothing whenis_on_floor()returnstrue.
floatget_floor_angle(up_direction:Vector2= Vector2(0, -1))const🔗
Returns the floor's collision angle at the last collision point according toup_direction, which isVector2.UPby default. This value is always positive and only valid after callingmove_and_slide()and whenis_on_floor()returnstrue.
Vector2get_floor_normal()const🔗
Returns the collision normal of the floor at the last collision point. Only valid after callingmove_and_slide()and whenis_on_floor()returnstrue.
Warning:The collision normal is not always the same as the surface normal.
Vector2get_last_motion()const🔗
Returns the last motion applied to theCharacterBody2Dduring the last call tomove_and_slide(). The movement can be split into multiple motions when sliding occurs, and this method return the last one, which is useful to retrieve the current direction of the movement.
KinematicCollision2Dget_last_slide_collision()🔗
Returns aKinematicCollision2Dif a collision occurred. The returned value contains information about the latest collision that occurred during the last call tomove_and_slide(). Returnsnullif no collision occurred. See alsoget_slide_collision().
Vector2get_platform_velocity()const🔗
Returns the linear velocity of the platform at the last collision point. Only valid after callingmove_and_slide().
Vector2get_position_delta()const🔗
Returns the travel (position delta) that occurred during the last call tomove_and_slide().
Vector2get_real_velocity()const🔗
Returns the current real velocity since the last call tomove_and_slide(). For example, when you climb a slope, you will move diagonally even though the velocity is horizontal. This method returns the diagonal movement, as opposed tovelocitywhich returns the requested velocity.
KinematicCollision2Dget_slide_collision(slide_idx:int)🔗
Returns aKinematicCollision2D, which contains information about a collision that occurred during the last call tomove_and_slide(). Since the body can collide several times in a single call tomove_and_slide(), you must specify the index of the collision in the range 0 to (get_slide_collision_count()- 1). See alsoget_last_slide_collision().
Example:Iterate through the collisions with aforloop:

```
for i in get_slide_collision_count():
    var collision = get_slide_collision(i)
    print("Collided with: ", collision.get_collider().name)
```

```
for (int i = 0; i < GetSlideCollisionCount(); i++)
{
    KinematicCollision2D collision = GetSlideCollision(i);
    GD.Print("Collided with: ", (collision.GetCollider() as Node).Name);
}
```

intget_slide_collision_count()const🔗
Returns the number of times the body collided and changed direction during the last call tomove_and_slide().
Vector2get_wall_normal()const🔗
Returns the collision normal of the wall at the last collision point. Only valid after callingmove_and_slide()and whenis_on_wall()returnstrue.
Warning:The collision normal is not always the same as the surface normal.
boolis_on_ceiling()const🔗
Returnstrueif the body collided with the ceiling on the last call ofmove_and_slide(). Otherwise, returnsfalse. Theup_directionandfloor_max_angleare used to determine whether a surface is "ceiling" or not.
boolis_on_ceiling_only()const🔗
Returnstrueif the body collided only with the ceiling on the last call ofmove_and_slide(). Otherwise, returnsfalse. Theup_directionandfloor_max_angleare used to determine whether a surface is "ceiling" or not.
boolis_on_floor()const🔗
Returnstrueif the body collided with the floor on the last call ofmove_and_slide(). Otherwise, returnsfalse. Theup_directionandfloor_max_angleare used to determine whether a surface is "floor" or not.
boolis_on_floor_only()const🔗
Returnstrueif the body collided only with the floor on the last call ofmove_and_slide(). Otherwise, returnsfalse. Theup_directionandfloor_max_angleare used to determine whether a surface is "floor" or not.
boolis_on_wall()const🔗
Returnstrueif the body collided with a wall on the last call ofmove_and_slide(). Otherwise, returnsfalse. Theup_directionandfloor_max_angleare used to determine whether a surface is "wall" or not.
boolis_on_wall_only()const🔗
Returnstrueif the body collided only with a wall on the last call ofmove_and_slide(). Otherwise, returnsfalse. Theup_directionandfloor_max_angleare used to determine whether a surface is "wall" or not.
boolmove_and_slide()🔗
Moves the body based onvelocity. If the body collides with another, it will slide along the other body (by default only on floor) rather than stop immediately. If the other body is aCharacterBody2DorRigidBody2D, it will also be affected by the motion of the other body. You can use this to make moving and rotating platforms, or to make nodes push other nodes.
This method should be used inNode._physics_process()(or in a method called byNode._physics_process()), as it uses the physics step'sdeltavalue automatically in calculations. Otherwise, the simulation will run at an incorrect speed.
Modifiesvelocityif a slide collision occurred. To get the latest collision callget_last_slide_collision(), for detailed information about collisions that occurred, useget_slide_collision().
When the body touches a moving platform, the platform's velocity is automatically added to the body motion. If a collision occurs due to the platform's motion, it will always be first in the slide collisions.
The general behavior and available properties change according to themotion_mode.
Returnstrueif the body collided, otherwise, returnsfalse.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
