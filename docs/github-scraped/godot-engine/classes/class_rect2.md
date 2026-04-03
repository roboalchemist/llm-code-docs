:github_url: hide



# Rect2

A 2D axis-aligned bounding box using floating-point coordinates.


## Description

The **Rect2** built-in [Variant<class_Variant>] type represents an axis-aligned rectangle in a 2D space. It is defined by its [position<class_Rect2_property_position>] and [size<class_Rect2_property_size>], which are [Vector2<class_Vector2>]. It is frequently used for fast overlap tests (see [intersects()<class_Rect2_method_intersects>]). Although **Rect2** itself is axis-aligned, it can be combined with [Transform2D<class_Transform2D>] to represent a rotated or skewed rectangle.

For integer coordinates, use [Rect2i<class_Rect2i>]. The 3D equivalent to **Rect2** is [AABB<class_AABB>].

\ **Note:** Negative values for [size<class_Rect2_property_size>] are not supported. With negative size, most **Rect2** methods do not work correctly. Use [abs()<class_Rect2_method_abs>] to get an equivalent **Rect2** with a non-negative size.

\ **Note:** In a boolean context, a **Rect2** evaluates to `false` if both [position<class_Rect2_property_position>] and [size<class_Rect2_property_size>] are zero (equal to [Vector2.ZERO<class_Vector2_constant_ZERO>]). Otherwise, it always evaluates to `true`.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Tutorials

- [../tutorials/math/index](Math documentation index .md)

- [../tutorials/math/vector_math](Vector math .md)

- [../tutorials/math/vectors_advanced](Advanced vector math .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`end<class_Rect2_property_end>`           | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`position<class_Rect2_property_position>` | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`size<class_Rect2_property_size>`         | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------+-------------------+
>

## Constructors

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`Rect2<class_Rect2_constructor_Rect2>`\ (\ )                                                                                                                                      |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`Rect2<class_Rect2_constructor_Rect2>`\ (\ from\: :ref:`Rect2<class_Rect2>`\ )                                                                                                    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`Rect2<class_Rect2_constructor_Rect2>`\ (\ from\: :ref:`Rect2i<class_Rect2i>`\ )                                                                                                  |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`Rect2<class_Rect2_constructor_Rect2>`\ (\ position\: :ref:`Vector2<class_Vector2>`, size\: :ref:`Vector2<class_Vector2>`\ )                                                      |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`Rect2<class_Rect2_constructor_Rect2>`\ (\ x\: :ref:`float<class_float>`, y\: :ref:`float<class_float>`, width\: :ref:`float<class_float>`, height\: :ref:`float<class_float>`\ ) |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`abs<class_Rect2_method_abs>`\ (\ ) |const|                                                                                                                                                                   |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`encloses<class_Rect2_method_encloses>`\ (\ b\: :ref:`Rect2<class_Rect2>`\ ) |const|                                                                                                                          |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`expand<class_Rect2_method_expand>`\ (\ to\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                                                                                         |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_area<class_Rect2_method_get_area>`\ (\ ) |const|                                                                                                                                                         |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_center<class_Rect2_method_get_center>`\ (\ ) |const|                                                                                                                                                     |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_support<class_Rect2_method_get_support>`\ (\ direction\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                                                                        |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`grow<class_Rect2_method_grow>`\ (\ amount\: :ref:`float<class_float>`\ ) |const|                                                                                                                             |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`grow_individual<class_Rect2_method_grow_individual>`\ (\ left\: :ref:`float<class_float>`, top\: :ref:`float<class_float>`, right\: :ref:`float<class_float>`, bottom\: :ref:`float<class_float>`\ ) |const| |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`grow_side<class_Rect2_method_grow_side>`\ (\ side\: :ref:`int<class_int>`, amount\: :ref:`float<class_float>`\ ) |const|                                                                                     |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_area<class_Rect2_method_has_area>`\ (\ ) |const|                                                                                                                                                         |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_point<class_Rect2_method_has_point>`\ (\ point\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                                                                                |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`intersection<class_Rect2_method_intersection>`\ (\ b\: :ref:`Rect2<class_Rect2>`\ ) |const|                                                                                                                  |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`intersects<class_Rect2_method_intersects>`\ (\ b\: :ref:`Rect2<class_Rect2>`, include_borders\: :ref:`bool<class_bool>` = false\ ) |const|                                                                   |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_equal_approx<class_Rect2_method_is_equal_approx>`\ (\ rect\: :ref:`Rect2<class_Rect2>`\ ) |const|                                                                                                         |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_finite<class_Rect2_method_is_finite>`\ (\ ) |const|                                                                                                                                                       |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`     | :ref:`merge<class_Rect2_method_merge>`\ (\ b\: :ref:`Rect2<class_Rect2>`\ ) |const|                                                                                                                                |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`operator !=<class_Rect2_operator_neq_Rect2>`\ (\ right\: :ref:`Rect2<class_Rect2>`\ )                  |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`operator *<class_Rect2_operator_mul_Transform2D>`\ (\ right\: :ref:`Transform2D<class_Transform2D>`\ ) |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`operator ==<class_Rect2_operator_eq_Rect2>`\ (\ right\: :ref:`Rect2<class_Rect2>`\ )                   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **end** = `Vector2(0, 0)` [🔗<class_Rect2_property_end>]

The ending point. This is usually the bottom-right corner of the rectangle, and is equivalent to `position + size`. Setting this point affects the [size<class_Rect2_property_size>].


----



[Vector2<class_Vector2>] **position** = `Vector2(0, 0)` [🔗<class_Rect2_property_position>]

The origin point. This is usually the top-left corner of the rectangle.


----



[Vector2<class_Vector2>] **size** = `Vector2(0, 0)` [🔗<class_Rect2_property_size>]

The rectangle's width and height, starting from [position<class_Rect2_property_position>]. Setting this value also affects the [end<class_Rect2_property_end>] point.

\ **Note:** It's recommended setting the width and height to non-negative values, as most methods in Godot assume that the [position<class_Rect2_property_position>] is the top-left corner, and the [end<class_Rect2_property_end>] is the bottom-right corner. To get an equivalent rectangle with non-negative size, use [abs()<class_Rect2_method_abs>].


----


## Constructor Descriptions



[Rect2<class_Rect2>] **Rect2**\ (\ ) [🔗<class_Rect2_constructor_Rect2>]

Constructs a **Rect2** with its [position<class_Rect2_property_position>] and [size<class_Rect2_property_size>] set to [Vector2.ZERO<class_Vector2_constant_ZERO>].


----


[Rect2<class_Rect2>] **Rect2**\ (\ from\: [Rect2<class_Rect2>]\ )

Constructs a **Rect2** as a copy of the given **Rect2**.


----


[Rect2<class_Rect2>] **Rect2**\ (\ from\: [Rect2i<class_Rect2i>]\ )

Constructs a **Rect2** from a [Rect2i<class_Rect2i>].


----


[Rect2<class_Rect2>] **Rect2**\ (\ position\: [Vector2<class_Vector2>], size\: [Vector2<class_Vector2>]\ )

Constructs a **Rect2** by `position` and `size`.


----


[Rect2<class_Rect2>] **Rect2**\ (\ x\: [float<class_float>], y\: [float<class_float>], width\: [float<class_float>], height\: [float<class_float>]\ )

Constructs a **Rect2** by setting its [position<class_Rect2_property_position>] to (`x`, `y`), and its [size<class_Rect2_property_size>] to (`width`, `height`).


----


## Method Descriptions



[Rect2<class_Rect2>] **abs**\ (\ ) |const| [🔗<class_Rect2_method_abs>]

Returns a **Rect2** equivalent to this rectangle, with its width and height modified to be non-negative values, and with its [position<class_Rect2_property_position>] being the top-left corner of the rectangle.


> **TABS**
>

    var rect = Rect2(25, 25, -100, -50)
    var absolute = rect.abs() # absolute is Rect2(-75, -25, 100, 50)


    var rect = new Rect2(25, 25, -100, -50);
    var absolute = rect.Abs(); // absolute is Rect2(-75, -25, 100, 50)



\ **Note:** It's recommended to use this method when [size<class_Rect2_property_size>] is negative, as most other methods in Godot assume that the [position<class_Rect2_property_position>] is the top-left corner, and the [end<class_Rect2_property_end>] is the bottom-right corner.


----



[bool<class_bool>] **encloses**\ (\ b\: [Rect2<class_Rect2>]\ ) |const| [🔗<class_Rect2_method_encloses>]

Returns `true` if this rectangle *completely* encloses the `b` rectangle.


----



[Rect2<class_Rect2>] **expand**\ (\ to\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_Rect2_method_expand>]

Returns a copy of this rectangle expanded to align the edges with the given `to` point, if necessary.


> **TABS**
>

    var rect = Rect2(0, 0, 5, 2)

    rect = rect.expand(Vector2(10, 0)) # rect is Rect2(0, 0, 10, 2)
    rect = rect.expand(Vector2(-5, 5)) # rect is Rect2(-5, 0, 15, 5)


    var rect = new Rect2(0, 0, 5, 2);

    rect = rect.Expand(new Vector2(10, 0)); // rect is Rect2(0, 0, 10, 2)
    rect = rect.Expand(new Vector2(-5, 5)); // rect is Rect2(-5, 0, 15, 5)




----



[float<class_float>] **get_area**\ (\ ) |const| [🔗<class_Rect2_method_get_area>]

Returns the rectangle's area. This is equivalent to `size.x * size.y`. See also [has_area()<class_Rect2_method_has_area>].


----



[Vector2<class_Vector2>] **get_center**\ (\ ) |const| [🔗<class_Rect2_method_get_center>]

Returns the center point of the rectangle. This is the same as `position + (size / 2.0)`.


----



[Vector2<class_Vector2>] **get_support**\ (\ direction\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_Rect2_method_get_support>]

Returns the vertex's position of this rect that's the farthest in the given direction. This point is commonly known as the support point in collision detection algorithms.


----



[Rect2<class_Rect2>] **grow**\ (\ amount\: [float<class_float>]\ ) |const| [🔗<class_Rect2_method_grow>]

Returns a copy of this rectangle extended on all sides by the given `amount`. A negative `amount` shrinks the rectangle instead. See also [grow_individual()<class_Rect2_method_grow_individual>] and [grow_side()<class_Rect2_method_grow_side>].


> **TABS**
>

    var a = Rect2(4, 4, 8, 8).grow(4) # a is Rect2(0, 0, 16, 16)
    var b = Rect2(0, 0, 8, 4).grow(2) # b is Rect2(-2, -2, 12, 8)


    var a = new Rect2(4, 4, 8, 8).Grow(4); // a is Rect2(0, 0, 16, 16)
    var b = new Rect2(0, 0, 8, 4).Grow(2); // b is Rect2(-2, -2, 12, 8)




----



[Rect2<class_Rect2>] **grow_individual**\ (\ left\: [float<class_float>], top\: [float<class_float>], right\: [float<class_float>], bottom\: [float<class_float>]\ ) |const| [🔗<class_Rect2_method_grow_individual>]

Returns a copy of this rectangle with its `left`, `top`, `right`, and `bottom` sides extended by the given amounts. Negative values shrink the sides, instead. See also [grow()<class_Rect2_method_grow>] and [grow_side()<class_Rect2_method_grow_side>].


----



[Rect2<class_Rect2>] **grow_side**\ (\ side\: [int<class_int>], amount\: [float<class_float>]\ ) |const| [🔗<class_Rect2_method_grow_side>]

Returns a copy of this rectangle with its `side` extended by the given `amount` (see [Side<enum_@GlobalScope_Side>] constants). A negative `amount` shrinks the rectangle, instead. See also [grow()<class_Rect2_method_grow>] and [grow_individual()<class_Rect2_method_grow_individual>].


----



[bool<class_bool>] **has_area**\ (\ ) |const| [🔗<class_Rect2_method_has_area>]

Returns `true` if this rectangle has positive width and height. See also [get_area()<class_Rect2_method_get_area>].


----



[bool<class_bool>] **has_point**\ (\ point\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_Rect2_method_has_point>]

Returns `true` if the rectangle contains the given `point`. By convention, points on the right and bottom edges are **not** included.

\ **Note:** This method is not reliable for **Rect2** with a *negative* [size<class_Rect2_property_size>]. Use [abs()<class_Rect2_method_abs>] first to get a valid rectangle.


----



[Rect2<class_Rect2>] **intersection**\ (\ b\: [Rect2<class_Rect2>]\ ) |const| [🔗<class_Rect2_method_intersection>]

Returns the intersection between this rectangle and `b`. If the rectangles do not intersect, returns an empty **Rect2**.


> **TABS**
>

    var rect1 = Rect2(0, 0, 5, 10)
    var rect2 = Rect2(2, 0, 8, 4)

    var a = rect1.intersection(rect2) # a is Rect2(2, 0, 3, 4)


    var rect1 = new Rect2(0, 0, 5, 10);
    var rect2 = new Rect2(2, 0, 8, 4);

    var a = rect1.Intersection(rect2); // a is Rect2(2, 0, 3, 4)



\ **Note:** If you only need to know whether two rectangles are overlapping, use [intersects()<class_Rect2_method_intersects>], instead.


----



[bool<class_bool>] **intersects**\ (\ b\: [Rect2<class_Rect2>], include_borders\: [bool<class_bool>] = false\ ) |const| [🔗<class_Rect2_method_intersects>]

Returns `true` if this rectangle overlaps with the `b` rectangle. The edges of both rectangles are excluded, unless `include_borders` is `true`.


----



[bool<class_bool>] **is_equal_approx**\ (\ rect\: [Rect2<class_Rect2>]\ ) |const| [🔗<class_Rect2_method_is_equal_approx>]

Returns `true` if this rectangle and `rect` are approximately equal, by calling [Vector2.is_equal_approx()<class_Vector2_method_is_equal_approx>] on the [position<class_Rect2_property_position>] and the [size<class_Rect2_property_size>].


----



[bool<class_bool>] **is_finite**\ (\ ) |const| [🔗<class_Rect2_method_is_finite>]

Returns `true` if this rectangle's values are finite, by calling [Vector2.is_finite()<class_Vector2_method_is_finite>] on the [position<class_Rect2_property_position>] and the [size<class_Rect2_property_size>].


----



[Rect2<class_Rect2>] **merge**\ (\ b\: [Rect2<class_Rect2>]\ ) |const| [🔗<class_Rect2_method_merge>]

Returns a **Rect2** that encloses both this rectangle and `b` around the edges. See also [encloses()<class_Rect2_method_encloses>].


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [Rect2<class_Rect2>]\ ) [🔗<class_Rect2_operator_neq_Rect2>]

Returns `true` if the [position<class_Rect2_property_position>] or [size<class_Rect2_property_size>] of both rectangles are not equal.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_Rect2_method_is_equal_approx>] instead, which is more reliable.


----



[Rect2<class_Rect2>] **operator ***\ (\ right\: [Transform2D<class_Transform2D>]\ ) [🔗<class_Rect2_operator_mul_Transform2D>]

Inversely transforms (multiplies) the **Rect2** by the given [Transform2D<class_Transform2D>] transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

\ `rect * transform` is equivalent to `transform.inverse() * rect`. See [Transform2D.inverse()<class_Transform2D_method_inverse>].

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * rect` can be used instead. See [Transform2D.affine_inverse()<class_Transform2D_method_affine_inverse>].


----



[bool<class_bool>] **operator ==**\ (\ right\: [Rect2<class_Rect2>]\ ) [🔗<class_Rect2_operator_eq_Rect2>]

Returns `true` if both [position<class_Rect2_property_position>] and [size<class_Rect2_property_size>] of the rectangles are exactly equal, respectively.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_Rect2_method_is_equal_approx>] instead, which is more reliable.

