:github_url: hide



# CylinderShape3D

**Inherits:** [Shape3D<class_Shape3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 3D cylinder shape used for physics collision.


## Description

A 3D cylinder shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D<class_CollisionShape3D>].

\ **Note:** There are several known bugs with cylinder collision shapes. Using [CapsuleShape3D<class_CapsuleShape3D>] or [BoxShape3D<class_BoxShape3D>] instead is recommended.

\ **Performance:** **CylinderShape3D** is fast to check collisions against, but it is slower than [CapsuleShape3D<class_CapsuleShape3D>], [BoxShape3D<class_BoxShape3D>], and [SphereShape3D<class_SphereShape3D>].


## Tutorials

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_

- [3D Physics Tests Demo ](https://godotengine.org/asset-library/asset/2747)_

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`height<class_CylinderShape3D_property_height>` | ``2.0`` |
> +---------------------------+------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`radius<class_CylinderShape3D_property_radius>` | ``0.5`` |
> +---------------------------+------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **height** = `2.0` [🔗<class_CylinderShape3D_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

The cylinder's height.


----



[float<class_float>] **radius** = `0.5` [🔗<class_CylinderShape3D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The cylinder's radius.

