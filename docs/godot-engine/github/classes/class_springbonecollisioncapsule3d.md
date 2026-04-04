:github_url: hide



# SpringBoneCollisionCapsule3D

**Inherits:** [SpringBoneCollision3D<class_SpringBoneCollision3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A capsule shape collision that interacts with [SpringBoneSimulator3D<class_SpringBoneSimulator3D>].


## Description

A capsule shape collision that interacts with [SpringBoneSimulator3D<class_SpringBoneSimulator3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`height<class_SpringBoneCollisionCapsule3D_property_height>`         | ``0.5``   |
> +---------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`inside<class_SpringBoneCollisionCapsule3D_property_inside>`         | ``false`` |
> +---------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`mid_height<class_SpringBoneCollisionCapsule3D_property_mid_height>` |           |
> +---------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`radius<class_SpringBoneCollisionCapsule3D_property_radius>`         | ``0.1``   |
> +---------------------------+---------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **height** = `0.5` [🔗<class_SpringBoneCollisionCapsule3D_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

The capsule's full height, including the hemispheres.

\ **Note:** The [height<class_SpringBoneCollisionCapsule3D_property_height>] of a capsule must be at least twice its [radius<class_SpringBoneCollisionCapsule3D_property_radius>]. Otherwise, the capsule becomes a sphere. If the [height<class_SpringBoneCollisionCapsule3D_property_height>] is less than twice the [radius<class_SpringBoneCollisionCapsule3D_property_radius>], the properties adjust to a valid value.


----



[bool<class_bool>] **inside** = `false` [🔗<class_SpringBoneCollisionCapsule3D_property_inside>]


- |void| **set_inside**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_inside**\ (\ )

If `true`, the collision acts to trap the joint within the collision.


----



[float<class_float>] **mid_height** [🔗<class_SpringBoneCollisionCapsule3D_property_mid_height>]


- |void| **set_mid_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mid_height**\ (\ )

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for [height<class_SpringBoneCollisionCapsule3D_property_height>].


----



[float<class_float>] **radius** = `0.1` [🔗<class_SpringBoneCollisionCapsule3D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The capsule's radius.

\ **Note:** The [radius<class_SpringBoneCollisionCapsule3D_property_radius>] of a capsule cannot be greater than half of its [height<class_SpringBoneCollisionCapsule3D_property_height>]. Otherwise, the capsule becomes a sphere. If the [radius<class_SpringBoneCollisionCapsule3D_property_radius>] is greater than half of the [height<class_SpringBoneCollisionCapsule3D_property_height>], the properties adjust to a valid value.

