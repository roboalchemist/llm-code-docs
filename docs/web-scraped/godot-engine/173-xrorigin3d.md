# XROrigin3D

# XROrigin3D
Inherits:Node3D<Node<Object
The origin point in AR/VR.

## Description
This is a special node within the AR/VR system that maps the physical location of the center of our tracking space to the virtual location within our game world.
Multiple origin points can be added to the scene tree, but only one can used at a time. All theXRCamera3D,XRController3D, andXRAnchor3Dnodes should be direct children of this node for spatial tracking to work correctly.
It is the position of this node that you update when your character needs to move through your game world while we're not moving in the real world. Movement in the real world is always in relation to this origin point.
For example, if your character is driving a car, theXROrigin3Dnode should be a child node of this car. Or, if you're implementing a teleport system to move your character, you should change the position of this node.

## Tutorials
- XR documentation index
XR documentation index

## Properties

| bool | current | false |
|---|---|---|
| float | world_scale | 1.0 |

bool
current
false
float
world_scale

## Property Descriptions
boolcurrent=false🔗
- voidset_current(value:bool)
voidset_current(value:bool)
- boolis_current()
boolis_current()
Iftrue, this origin node is currently being used by theXRServer. Only one origin point can be used at a time.
floatworld_scale=1.0🔗
- voidset_world_scale(value:float)
voidset_world_scale(value:float)
- floatget_world_scale()
floatget_world_scale()
The scale of the game world compared to the real world. This is the same asXRServer.world_scale. By default, most AR/VR platforms assume that 1 game unit corresponds to 1 real world meter.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.