# ParallaxLayer in English

# ParallaxLayer

Deprecated:Use theParallax2Dnode instead.
Inherits:Node2D<CanvasItem<Node<Object
A parallax scrolling layer to be used withParallaxBackground.

## Description

A ParallaxLayer must be the child of aParallaxBackgroundnode. Each ParallaxLayer can be set to move at different speeds relative to the camera movement or theParallaxBackground.scroll_offsetvalue.
This node's children will be affected by its scroll offset.
Note:Any changes to this node's position and scale made after it enters the scene will be ignored.

## Properties

| Vector2 | motion_mirroring | Vector2(0,0) |
|---|---|---|
| Vector2 | motion_offset | Vector2(0,0) |
| Vector2 | motion_scale | Vector2(1,1) |
| PhysicsInterpolationMode | physics_interpolation_mode | 2(overridesNode) |

Vector2
motion_mirroring
Vector2(0,0)
Vector2
motion_offset
Vector2(0,0)
Vector2
motion_scale
Vector2(1,1)
PhysicsInterpolationMode
physics_interpolation_mode
2(overridesNode)

## Property Descriptions

Vector2motion_mirroring=Vector2(0,0)🔗

- voidset_mirroring(value:Vector2)
voidset_mirroring(value:Vector2)
- Vector2get_mirroring()
Vector2get_mirroring()
The interval, in pixels, at which theParallaxLayeris drawn repeatedly. Useful for creating an infinitely scrolling background. If an axis is set to0, theParallaxLayerwill be drawn only once along that direction.
Note:If you want the repetition to pixel-perfect match aTexture2Ddisplayed by a child node, you should account for any scale applied to the texture when defining this interval. For example, if you use a childSprite2Dscaled to0.5to display a 600x600 texture, and want this sprite to be repeated continuously horizontally, you should set the mirroring toVector2(300,0).
Note:If the length of the viewport axis is bigger than twice the repeated axis size, it will not repeat infinitely, as the parallax layer only draws 2 instances of the layer at any given time. The visibility window is calculated from the parentParallaxBackground's position, not the layer's own position. So, if you use mirroring,do notchange theParallaxLayerposition relative to its parent. Instead, if you need to adjust the background's position, set theCanvasLayer.offsetproperty in the parentParallaxBackground.
Note:Despite the name, the layer will not be mirrored, it will only be repeated.
Vector2motion_offset=Vector2(0,0)🔗
- voidset_motion_offset(value:Vector2)
voidset_motion_offset(value:Vector2)
- Vector2get_motion_offset()
Vector2get_motion_offset()
The ParallaxLayer's offset relative to the parent ParallaxBackground'sParallaxBackground.scroll_offset.
Vector2motion_scale=Vector2(1,1)🔗
- voidset_motion_scale(value:Vector2)
voidset_motion_scale(value:Vector2)
- Vector2get_motion_scale()
Vector2get_motion_scale()
Multiplies the ParallaxLayer's motion. If an axis is set to0, it will not scroll.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
