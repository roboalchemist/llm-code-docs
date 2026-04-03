:github_url: hide



# Rect2i

A 2D axis-aligned bounding box using integer coordinates.


## Description

The **Rect2i** built-in [Variant<class_Variant>] type represents an axis-aligned rectangle in a 2D space, using integer coordinates. It is defined by its [position<class_Rect2i_property_position>] and [size<class_Rect2i_property_size>], which are [Vector2i<class_Vector2i>]. Because it does not rotate, it is frequently used for fast overlap tests (see [intersects()<class_Rect2i_method_intersects>]).

For floating-point coordinates, see [Rect2<class_Rect2>].

\ **Note:** Negative values for [size<class_Rect2i_property_size>] are not supported. With negative size, most **Rect2i** methods do not work correctly. Use [abs()<class_Rect2i_method_abs>] to get an equivalent **Rect2i** with a non-negative size.

\ **Note:** In a boolean context, a **Rect2i** evaluates to `false` if both [position<class_Rect2i_property_position>] and [size<class_Rect2i_property_size>] are zero (equal to [Vector2i.ZERO<class_Vector2i_constant_ZERO>]). Otherwise, it always evaluates to `true`.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Tutorials

- [../tutorials/math/index](Math documentation index .md)

- [../tutorials/math/vector_math](Vector math .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`end<class_Rect2i_property_end>`           | ``Vector2i(0, 0)`` |
> +---------------------------------+-------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`position<class_Rect2i_property_position>` | ``Vector2i(0, 0)`` |
> +---------------------------------+-------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`size<class_Rect2i_property_size>`         | ``Vector2i(0, 0)`` |
> +---------------------------------+-------------------------------------------------+--------------------+
>

## Constructors

> **TABLE**
> :widths: auto
>
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>` | :ref:`Rect2i<class_Rect2i_constructor_Rect2i>`\ (\ )                                                                                                                      |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>` | :ref:`Rect2i<class_Rect2i_constructor_Rect2i>`\ (\ from\: :ref:`Rect2i<class_Rect2i>`\ )                                                                                  |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>` | :ref:`Rect2i<class_Rect2i_constructor_Rect2i>`\ (\ from\: :ref:`Rect2<class_Rect2>`\ )                                                                                    |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>` | :ref:`Rect2i<class_Rect2i_constructor_Rect2i>`\ (\ position\: :ref:`Vector2i<class_Vector2i>`, size\: :ref:`Vector2i<class_Vector2i>`\ )                                  |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>` | :ref:`Rect2i<class_Rect2i_constructor_Rect2i>`\ (\ x\: :ref:`int<class_int>`, y\: :ref:`int<class_int>`, width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`\ ) |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`abs<class_Rect2i_method_abs>`\ (\ ) |const|                                                                                                                                                   |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`encloses<class_Rect2i_method_encloses>`\ (\ b\: :ref:`Rect2i<class_Rect2i>`\ ) |const|                                                                                                        |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`expand<class_Rect2i_method_expand>`\ (\ to\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                       |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_area<class_Rect2i_method_get_area>`\ (\ ) |const|                                                                                                                                         |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`get_center<class_Rect2i_method_get_center>`\ (\ ) |const|                                                                                                                                     |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`grow<class_Rect2i_method_grow>`\ (\ amount\: :ref:`int<class_int>`\ ) |const|                                                                                                                 |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`grow_individual<class_Rect2i_method_grow_individual>`\ (\ left\: :ref:`int<class_int>`, top\: :ref:`int<class_int>`, right\: :ref:`int<class_int>`, bottom\: :ref:`int<class_int>`\ ) |const| |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`grow_side<class_Rect2i_method_grow_side>`\ (\ side\: :ref:`int<class_int>`, amount\: :ref:`int<class_int>`\ ) |const|                                                                         |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`has_area<class_Rect2i_method_has_area>`\ (\ ) |const|                                                                                                                                         |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`has_point<class_Rect2i_method_has_point>`\ (\ point\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                              |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`intersection<class_Rect2i_method_intersection>`\ (\ b\: :ref:`Rect2i<class_Rect2i>`\ ) |const|                                                                                                |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`intersects<class_Rect2i_method_intersects>`\ (\ b\: :ref:`Rect2i<class_Rect2i>`\ ) |const|                                                                                                    |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`     | :ref:`merge<class_Rect2i_method_merge>`\ (\ b\: :ref:`Rect2i<class_Rect2i>`\ ) |const|                                                                                                              |
> +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator !=<class_Rect2i_operator_neq_Rect2i>`\ (\ right\: :ref:`Rect2i<class_Rect2i>`\ ) |
> +-------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator ==<class_Rect2i_operator_eq_Rect2i>`\ (\ right\: :ref:`Rect2i<class_Rect2i>`\ )  |
> +-------------------------+-------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector2i<class_Vector2i>] **end** = `Vector2i(0, 0)` [🔗<class_Rect2i_property_end>]

The ending point. This is usually the bottom-right corner of the rectangle, and is equivalent to `position + size`. Setting this point affects the [size<class_Rect2i_property_size>].


----



[Vector2i<class_Vector2i>] **position** = `Vector2i(0, 0)` [🔗<class_Rect2i_property_position>]

The origin point. This is usually the top-left corner of the rectangle.


----



[Vector2i<class_Vector2i>] **size** = `Vector2i(0, 0)` [🔗<class_Rect2i_property_size>]

The rectangle's width and height, starting from [position<class_Rect2i_property_position>]. Setting this value also affects the [end<class_Rect2i_property_end>] point.

\ **Note:** It's recommended setting the width and height to non-negative values, as most methods in Godot assume that the [position<class_Rect2i_property_position>] is the top-left corner, and the [end<class_Rect2i_property_end>] is the bottom-right corner. To get an equivalent rectangle with non-negative size, use [abs()<class_Rect2i_method_abs>].


----


## Constructor Descriptions



[Rect2i<class_Rect2i>] **Rect2i**\ (\ ) [🔗<class_Rect2i_constructor_Rect2i>]

Constructs a **Rect2i** with its [position<class_Rect2i_property_position>] and [size<class_Rect2i_property_size>] set to [Vector2i.ZERO<class_Vector2i_constant_ZERO>].


----


[Rect2i<class_Rect2i>] **Rect2i**\ (\ from\: [Rect2i<class_Rect2i>]\ )

Constructs a **Rect2i** as a copy of the given **Rect2i**.


----


[Rect2i<class_Rect2i>] **Rect2i**\ (\ from\: [Rect2<class_Rect2>]\ )

Constructs a **Rect2i** from a [Rect2<class_Rect2>]. The floating-point coordinates are truncated.


----


[Rect2i<class_Rect2i>] **Rect2i**\ (\ position\: [Vector2i<class_Vector2i>], size\: [Vector2i<class_Vector2i>]\ )

Constructs a **Rect2i** by `position` and `size`.


----


[Rect2i<class_Rect2i>] **Rect2i**\ (\ x\: [int<class_int>], y\: [int<class_int>], width\: [int<class_int>], height\: [int<class_int>]\ )

Constructs a **Rect2i** by setting its [position<class_Rect2i_property_position>] to (`x`, `y`), and its [size<class_Rect2i_property_size>] to (`width`, `height`).


----


## Method Descriptions



[Rect2i<class_Rect2i>] **abs**\ (\ ) |const| [🔗<class_Rect2i_method_abs>]

Returns a **Rect2i** equivalent to this rectangle, with its width and height modified to be non-negative values, and with its [position<class_Rect2i_property_position>] being the top-left corner of the rectangle.


> **TABS**
>

    var rect = Rect2i(25, 25, -100, -50)
    var absolute = rect.abs() # absolute is Rect2i(-75, -25, 100, 50)


    var rect = new Rect2I(25, 25, -100, -50);
    var absolute = rect.Abs(); // absolute is Rect2I(-75, -25, 100, 50)



\ **Note:** It's recommended to use this method when [size<class_Rect2i_property_size>] is negative, as most other methods in Godot assume that the [position<class_Rect2i_property_position>] is the top-left corner, and the [end<class_Rect2i_property_end>] is the bottom-right corner.


----



[bool<class_bool>] **encloses**\ (\ b\: [Rect2i<class_Rect2i>]\ ) |const| [🔗<class_Rect2i_method_encloses>]

Returns `true` if this **Rect2i** completely encloses another one.


----



[Rect2i<class_Rect2i>] **expand**\ (\ to\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_Rect2i_method_expand>]

Returns a copy of this rectangle expanded to align the edges with the given `to` point, if necessary.


> **TABS**
>

    var rect = Rect2i(0, 0, 5, 2)

    rect = rect.expand(Vector2i(10, 0)) # rect is Rect2i(0, 0, 10, 2)
    rect = rect.expand(Vector2i(-5, 5)) # rect is Rect2i(-5, 0, 15, 5)


    var rect = new Rect2I(0, 0, 5, 2);

    rect = rect.Expand(new Vector2I(10, 0)); // rect is Rect2I(0, 0, 10, 2)
    rect = rect.Expand(new Vector2I(-5, 5)); // rect is Rect2I(-5, 0, 15, 5)




----



[int<class_int>] **get_area**\ (\ ) |const| [🔗<class_Rect2i_method_get_area>]

Returns the rectangle's area. This is equivalent to `size.x * size.y`. See also [has_area()<class_Rect2i_method_has_area>].


----



[Vector2i<class_Vector2i>] **get_center**\ (\ ) |const| [🔗<class_Rect2i_method_get_center>]

Returns the center point of the rectangle. This is the same as `position + (size / 2)`.

\ **Note:** If the [size<class_Rect2i_property_size>] is odd, the result will be rounded towards [position<class_Rect2i_property_position>].


----



[Rect2i<class_Rect2i>] **grow**\ (\ amount\: [int<class_int>]\ ) |const| [🔗<class_Rect2i_method_grow>]

Returns a copy of this rectangle extended on all sides by the given `amount`. A negative `amount` shrinks the rectangle instead. See also [grow_individual()<class_Rect2i_method_grow_individual>] and [grow_side()<class_Rect2i_method_grow_side>].


> **TABS**
>

    var a = Rect2i(4, 4, 8, 8).grow(4) # a is Rect2i(0, 0, 16, 16)
    var b = Rect2i(0, 0, 8, 4).grow(2) # b is Rect2i(-2, -2, 12, 8)


    var a = new Rect2I(4, 4, 8, 8).Grow(4); // a is Rect2I(0, 0, 16, 16)
    var b = new Rect2I(0, 0, 8, 4).Grow(2); // b is Rect2I(-2, -2, 12, 8)




----



[Rect2i<class_Rect2i>] **grow_individual**\ (\ left\: [int<class_int>], top\: [int<class_int>], right\: [int<class_int>], bottom\: [int<class_int>]\ ) |const| [🔗<class_Rect2i_method_grow_individual>]

Returns a copy of this rectangle with its `left`, `top`, `right`, and `bottom` sides extended by the given amounts. Negative values shrink the sides, instead. See also [grow()<class_Rect2i_method_grow>] and [grow_side()<class_Rect2i_method_grow_side>].


----



[Rect2i<class_Rect2i>] **grow_side**\ (\ side\: [int<class_int>], amount\: [int<class_int>]\ ) |const| [🔗<class_Rect2i_method_grow_side>]

Returns a copy of this rectangle with its `side` extended by the given `amount` (see [Side<enum_@GlobalScope_Side>] constants). A negative `amount` shrinks the rectangle, instead. See also [grow()<class_Rect2i_method_grow>] and [grow_individual()<class_Rect2i_method_grow_individual>].


----



[bool<class_bool>] **has_area**\ (\ ) |const| [🔗<class_Rect2i_method_has_area>]

Returns `true` if this rectangle has positive width and height. See also [get_area()<class_Rect2i_method_get_area>].


----



[bool<class_bool>] **has_point**\ (\ point\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_Rect2i_method_has_point>]

Returns `true` if the rectangle contains the given `point`. By convention, points on the right and bottom edges are **not** included.

\ **Note:** This method is not reliable for **Rect2i** with a *negative* [size<class_Rect2i_property_size>]. Use [abs()<class_Rect2i_method_abs>] first to get a valid rectangle.


----



[Rect2i<class_Rect2i>] **intersection**\ (\ b\: [Rect2i<class_Rect2i>]\ ) |const| [🔗<class_Rect2i_method_intersection>]

Returns the intersection between this rectangle and `b`. If the rectangles do not intersect, returns an empty **Rect2i**.


> **TABS**
>

    var a = Rect2i(0, 0, 5, 10)
    var b = Rect2i(2, 0, 8, 4)

    var c = a.intersection(b) # c is Rect2i(2, 0, 3, 4)


    var a = new Rect2I(0, 0, 5, 10);
    var b = new Rect2I(2, 0, 8, 4);

    var c = rect1.Intersection(rect2); // c is Rect2I(2, 0, 3, 4)



\ **Note:** If you only need to know whether two rectangles are overlapping, use [intersects()<class_Rect2i_method_intersects>], instead.


----



[bool<class_bool>] **intersects**\ (\ b\: [Rect2i<class_Rect2i>]\ ) |const| [🔗<class_Rect2i_method_intersects>]

Returns `true` if this rectangle overlaps with the `b` rectangle. The edges of both rectangles are excluded.


----



[Rect2i<class_Rect2i>] **merge**\ (\ b\: [Rect2i<class_Rect2i>]\ ) |const| [🔗<class_Rect2i_method_merge>]

Returns a **Rect2i** that encloses both this rectangle and `b` around the edges. See also [encloses()<class_Rect2i_method_encloses>].


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [Rect2i<class_Rect2i>]\ ) [🔗<class_Rect2i_operator_neq_Rect2i>]

Returns `true` if the [position<class_Rect2i_property_position>] or [size<class_Rect2i_property_size>] of both rectangles are not equal.


----



[bool<class_bool>] **operator ==**\ (\ right\: [Rect2i<class_Rect2i>]\ ) [🔗<class_Rect2i_operator_eq_Rect2i>]

Returns `true` if both [position<class_Rect2i_property_position>] and [size<class_Rect2i_property_size>] of the rectangles are equal, respectively.

