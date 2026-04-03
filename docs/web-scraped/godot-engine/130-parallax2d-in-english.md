# Parallax2D in English

# Parallax2D
Inherits:Node2D<CanvasItem<Node<Object
A node used to create a parallax scrolling background.

## Description
AParallax2Dis used to create a parallax effect. It can move at a different speed relative to the camera movement usingscroll_scale. This creates an illusion of depth in a 2D game. If manual scrolling is desired, theCamera2Dposition can be ignored withignore_camera_scroll.
Note:Any changes to this node's position made after it enters the scene tree will be overridden ifignore_camera_scrollisfalseorscreen_offsetis modified.

## Tutorials
- 2D Parallax
2D Parallax

## Properties

| Vector2 | autoscroll | Vector2(0,0) |
|---|---|---|
| bool | follow_viewport | true |
| bool | ignore_camera_scroll | false |
| Vector2 | limit_begin | Vector2(-10000000,-10000000) |
| Vector2 | limit_end | Vector2(10000000,10000000) |
| PhysicsInterpolationMode | physics_interpolation_mode | 2(overridesNode) |
| Vector2 | repeat_size | Vector2(0,0) |
| int | repeat_times | 1 |
| Vector2 | screen_offset | Vector2(0,0) |
| Vector2 | scroll_offset | Vector2(0,0) |
| Vector2 | scroll_scale | Vector2(1,1) |

Vector2
autoscroll
Vector2(0,0)
bool
follow_viewport
true
bool
ignore_camera_scroll
false
Vector2
limit_begin
Vector2(-10000000,-10000000)
Vector2
limit_end
Vector2(10000000,10000000)
PhysicsInterpolationMode
physics_interpolation_mode
2(overridesNode)
Vector2
repeat_size
Vector2(0,0)
repeat_times
Vector2
screen_offset
Vector2(0,0)
Vector2
scroll_offset
Vector2(0,0)
Vector2
scroll_scale
Vector2(1,1)

## Property Descriptions
Vector2autoscroll=Vector2(0,0)🔗
- voidset_autoscroll(value:Vector2)
voidset_autoscroll(value:Vector2)
- Vector2get_autoscroll()
Vector2get_autoscroll()
Velocity at which the offset scrolls automatically, in pixels per second.
boolfollow_viewport=true🔗
- voidset_follow_viewport(value:bool)
voidset_follow_viewport(value:bool)
- boolget_follow_viewport()
boolget_follow_viewport()
Iftrue, thisParallax2Dis offset by the current camera's position. If theParallax2Dis in aCanvasLayerseparate from the current camera, it may be desired to match the value withCanvasLayer.follow_viewport_enabled.
boolignore_camera_scroll=false🔗
- voidset_ignore_camera_scroll(value:bool)
voidset_ignore_camera_scroll(value:bool)
- boolis_ignore_camera_scroll()
boolis_ignore_camera_scroll()
Iftrue,Parallax2D's position is not affected by the position of the camera.
Vector2limit_begin=Vector2(-10000000,-10000000)🔗
- voidset_limit_begin(value:Vector2)
voidset_limit_begin(value:Vector2)
- Vector2get_limit_begin()
Vector2get_limit_begin()
Top-left limits for scrolling to begin. If the camera is outside of this limit, theParallax2Dstops scrolling. Must be lower thanlimit_endminus the viewport size to work.
Vector2limit_end=Vector2(10000000,10000000)🔗
- voidset_limit_end(value:Vector2)
voidset_limit_end(value:Vector2)
- Vector2get_limit_end()
Vector2get_limit_end()
Bottom-right limits for scrolling to end. If the camera is outside of this limit, theParallax2Dwill stop scrolling. Must be higher thanlimit_beginand the viewport size combined to work.
Vector2repeat_size=Vector2(0,0)🔗
- voidset_repeat_size(value:Vector2)
voidset_repeat_size(value:Vector2)
- Vector2get_repeat_size()
Vector2get_repeat_size()
Repeats theTexture2Dof each of this node's children and offsets them by this value. When scrolling, the node's position loops, giving the illusion of an infinite scrolling background if the values are larger than the screen size. If an axis is set to0, theTexture2Dwill not be repeated.
intrepeat_times=1🔗
- voidset_repeat_times(value:int)
voidset_repeat_times(value:int)
- intget_repeat_times()
intget_repeat_times()
Overrides the amount of times the texture repeats. Each texture copy spreads evenly from the original byrepeat_size. Useful for when zooming out with a camera.
Vector2screen_offset=Vector2(0,0)🔗
- voidset_screen_offset(value:Vector2)
voidset_screen_offset(value:Vector2)
- Vector2get_screen_offset()
Vector2get_screen_offset()
Offset used to scroll thisParallax2D. This value is updated automatically unlessignore_camera_scrollistrue.
Vector2scroll_offset=Vector2(0,0)🔗
- voidset_scroll_offset(value:Vector2)
voidset_scroll_offset(value:Vector2)
- Vector2get_scroll_offset()
Vector2get_scroll_offset()
TheParallax2D's offset. Similar toscreen_offsetandNode2D.position, but will not be overridden.
Note:Values will loop ifrepeat_sizeis set higher than0.
Vector2scroll_scale=Vector2(1,1)🔗
- voidset_scroll_scale(value:Vector2)
voidset_scroll_scale(value:Vector2)
- Vector2get_scroll_scale()
Vector2get_scroll_scale()
Multiplier to the finalParallax2D's offset. Can be used to simulate distance from the camera.
For example, a value of1scrolls at the same speed as the camera. A value greater than1scrolls faster, making objects appear closer. Less than1scrolls slower, making objects appear further, and a value of0stops the objects completely.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.