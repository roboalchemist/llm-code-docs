:github_url: hide



# SphereShape3D

**Inherits:** [Shape3D<class_Shape3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 3D sphere shape used for physics collision.


## Description

A 3D sphere shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D<class_CollisionShape3D>].

\ **Performance:** **SphereShape3D** is fast to check collisions against. It is faster than [BoxShape3D<class_BoxShape3D>], [CapsuleShape3D<class_CapsuleShape3D>], and [CylinderShape3D<class_CylinderShape3D>].


## Tutorials

- [3D Physics Tests Demo ](https://godotengine.org/asset-library/asset/2747)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`radius<class_SphereShape3D_property_radius>` | ``0.5`` |
> +---------------------------+----------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **radius** = `0.5` [🔗<class_SphereShape3D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The sphere's radius. The shape's diameter is double the radius.

