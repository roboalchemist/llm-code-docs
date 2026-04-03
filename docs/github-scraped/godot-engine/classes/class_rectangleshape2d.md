:github_url: hide



# RectangleShape2D

**Inherits:** [Shape2D<class_Shape2D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 2D rectangle shape used for physics collision.


## Description

A 2D rectangle shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D<class_CollisionShape2D>].

\ **Performance:** **RectangleShape2D** is fast to check collisions against. It is faster than [CapsuleShape2D<class_CapsuleShape2D>], but slower than [CircleShape2D<class_CircleShape2D>].


## Tutorials

- [2D Pong Demo ](https://godotengine.org/asset-library/asset/2728)_

- [2D Kinematic Character Demo ](https://godotengine.org/asset-library/asset/2719)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------+---------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`size<class_RectangleShape2D_property_size>` | ``Vector2(20, 20)`` |
> +-------------------------------+---------------------------------------------------+---------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **size** = `Vector2(20, 20)` [🔗<class_RectangleShape2D_property_size>]


- |void| **set_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_size**\ (\ )

The rectangle's width and height.

