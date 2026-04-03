:github_url: hide



# CapsuleShape2D

**Inherits:** [Shape2D<class_Shape2D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 2D capsule shape used for physics collision.


## Description

A 2D capsule shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D<class_CollisionShape2D>].

\ **Performance:** **CapsuleShape2D** is fast to check collisions against, but it is slower than [RectangleShape2D<class_RectangleShape2D>] and [CircleShape2D<class_CircleShape2D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`height<class_CapsuleShape2D_property_height>`         | ``30.0`` |
> +---------------------------+-------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`mid_height<class_CapsuleShape2D_property_mid_height>` |          |
> +---------------------------+-------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`radius<class_CapsuleShape2D_property_radius>`         | ``10.0`` |
> +---------------------------+-------------------------------------------------------------+----------+
>

----


## Property Descriptions



[float<class_float>] **height** = `30.0` [🔗<class_CapsuleShape2D_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

The capsule's full height, including the semicircles.

\ **Note:** The [height<class_CapsuleShape2D_property_height>] of a capsule must be at least twice its [radius<class_CapsuleShape2D_property_radius>]. Otherwise, the capsule becomes a circle. If the [height<class_CapsuleShape2D_property_height>] is less than twice the [radius<class_CapsuleShape2D_property_radius>], the properties adjust to a valid value.


----



[float<class_float>] **mid_height** [🔗<class_CapsuleShape2D_property_mid_height>]


- |void| **set_mid_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mid_height**\ (\ )

The capsule's height, excluding the semicircles. This is the height of the central rectangular part in the middle of the capsule, and is the distance between the centers of the two semicircles. This is a wrapper for [height<class_CapsuleShape2D_property_height>].


----



[float<class_float>] **radius** = `10.0` [🔗<class_CapsuleShape2D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The capsule's radius.

\ **Note:** The [radius<class_CapsuleShape2D_property_radius>] of a capsule cannot be greater than half of its [height<class_CapsuleShape2D_property_height>]. Otherwise, the capsule becomes a circle. If the [radius<class_CapsuleShape2D_property_radius>] is greater than half of the [height<class_CapsuleShape2D_property_height>], the properties adjust to a valid value.

