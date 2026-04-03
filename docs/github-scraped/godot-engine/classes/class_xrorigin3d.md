:github_url: hide



# XROrigin3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

The origin point in AR/VR.


## Description

This is a special node within the AR/VR system that maps the physical location of the center of our tracking space to the virtual location within our game world.

Multiple origin points can be added to the scene tree, but only one can used at a time. All the [XRCamera3D<class_XRCamera3D>], [XRController3D<class_XRController3D>], and [XRAnchor3D<class_XRAnchor3D>] nodes should be direct children of this node for spatial tracking to work correctly.

It is the position of this node that you update when your character needs to move through your game world while we're not moving in the real world. Movement in the real world is always in relation to this origin point.

For example, if your character is driving a car, the **XROrigin3D** node should be a child node of this car. Or, if you're implementing a teleport system to move your character, you should change the position of this node.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`current<class_XROrigin3D_property_current>`         | ``false`` |
> +---------------------------+-----------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`world_scale<class_XROrigin3D_property_world_scale>` | ``1.0``   |
> +---------------------------+-----------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **current** = `false` [🔗<class_XROrigin3D_property_current>]


- |void| **set_current**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_current**\ (\ )

If `true`, this origin node is currently being used by the [XRServer<class_XRServer>]. Only one origin point can be used at a time.


----



[float<class_float>] **world_scale** = `1.0` [🔗<class_XROrigin3D_property_world_scale>]


- |void| **set_world_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_world_scale**\ (\ )

The scale of the game world compared to the real world. This is the same as [XRServer.world_scale<class_XRServer_property_world_scale>]. By default, most AR/VR platforms assume that 1 game unit corresponds to 1 real world meter.

