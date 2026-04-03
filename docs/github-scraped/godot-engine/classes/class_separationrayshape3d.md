:github_url: hide



# SeparationRayShape3D

**Inherits:** [Shape3D<class_Shape3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 3D ray shape used for physics collision that tries to separate itself from any collider.


## Description

A 3D ray shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D<class_CollisionShape3D>]. When a **SeparationRayShape3D** collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a **SeparationRayShape3D** next to a character can allow it to instantly move up when touching stairs.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`length<class_SeparationRayShape3D_property_length>`                 | ``1.0``   |
> +---------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`slide_on_slope<class_SeparationRayShape3D_property_slide_on_slope>` | ``false`` |
> +---------------------------+---------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **length** = `1.0` [🔗<class_SeparationRayShape3D_property_length>]


- |void| **set_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_length**\ (\ )

The ray's length.


----



[bool<class_bool>] **slide_on_slope** = `false` [🔗<class_SeparationRayShape3D_property_slide_on_slope>]


- |void| **set_slide_on_slope**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_slide_on_slope**\ (\ )

If `false` (default), the shape always separates and returns a normal along its own direction.

If `true`, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.

