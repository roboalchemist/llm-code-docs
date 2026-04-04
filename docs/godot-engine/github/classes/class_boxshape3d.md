:github_url: hide



# BoxShape3D

**Inherits:** [Shape3D<class_Shape3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 3D box shape used for physics collision.


## Description

A 3D box shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D<class_CollisionShape3D>].

\ **Performance:** **BoxShape3D** is fast to check collisions against. It is faster than [CapsuleShape3D<class_CapsuleShape3D>] and [CylinderShape3D<class_CylinderShape3D>], but slower than [SphereShape3D<class_SphereShape3D>].


## Tutorials

- [3D Physics Tests Demo ](https://godotengine.org/asset-library/asset/2747)_

- [3D Kinematic Character Demo ](https://godotengine.org/asset-library/asset/2739)_

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`size<class_BoxShape3D_property_size>` | ``Vector3(1, 1, 1)`` |
> +-------------------------------+---------------------------------------------+----------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **size** = `Vector3(1, 1, 1)` [🔗<class_BoxShape3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The box's width, height and depth.

