:github_url: hide



# AABB

A 3D axis-aligned bounding box.


## Description

The **AABB** built-in [Variant<class_Variant>] type represents an axis-aligned bounding box in a 3D space. It is defined by its [position<class_AABB_property_position>] and [size<class_AABB_property_size>], which are [Vector3<class_Vector3>]. It is frequently used for fast overlap tests (see [intersects()<class_AABB_method_intersects>]). Although **AABB** itself is axis-aligned, it can be combined with [Transform3D<class_Transform3D>] to represent a rotated or skewed bounding box.

It uses floating-point coordinates. The 2D counterpart to **AABB** is [Rect2<class_Rect2>]. There is no version of **AABB** that uses integer coordinates.

\ **Note:** Negative values for [size<class_AABB_property_size>] are not supported. With negative size, most **AABB** methods do not work correctly. Use [abs()<class_AABB_method_abs>] to get an equivalent **AABB** with a non-negative size.

\ **Note:** In a boolean context, an **AABB** evaluates to `false` if both [position<class_AABB_property_position>] and [size<class_AABB_property_size>] are zero (equal to [Vector3.ZERO<class_Vector3_constant_ZERO>]). Otherwise, it always evaluates to `true`.

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
> +-------------------------------+-----------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`end<class_AABB_property_end>`           | ``Vector3(0, 0, 0)`` |
> +-------------------------------+-----------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`position<class_AABB_property_position>` | ``Vector3(0, 0, 0)`` |
> +-------------------------------+-----------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`size<class_AABB_property_size>`         | ``Vector3(0, 0, 0)`` |
> +-------------------------------+-----------------------------------------------+----------------------+
>

## Constructors

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`AABB<class_AABB_constructor_AABB>`\ (\ )                                                                                 |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`AABB<class_AABB_constructor_AABB>`\ (\ from\: :ref:`AABB<class_AABB>`\ )                                                 |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`AABB<class_AABB_constructor_AABB>`\ (\ position\: :ref:`Vector3<class_Vector3>`, size\: :ref:`Vector3<class_Vector3>`\ ) |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`       | :ref:`abs<class_AABB_method_abs>`\ (\ ) |const|                                                                                                         |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`encloses<class_AABB_method_encloses>`\ (\ with\: :ref:`AABB<class_AABB>`\ ) |const|                                                               |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`       | :ref:`expand<class_AABB_method_expand>`\ (\ to_point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                         |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_center<class_AABB_method_get_center>`\ (\ ) |const|                                                                                           |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_endpoint<class_AABB_method_get_endpoint>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                          |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_longest_axis<class_AABB_method_get_longest_axis>`\ (\ ) |const|                                                                               |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_longest_axis_index<class_AABB_method_get_longest_axis_index>`\ (\ ) |const|                                                                   |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_longest_axis_size<class_AABB_method_get_longest_axis_size>`\ (\ ) |const|                                                                     |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_shortest_axis<class_AABB_method_get_shortest_axis>`\ (\ ) |const|                                                                             |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_shortest_axis_index<class_AABB_method_get_shortest_axis_index>`\ (\ ) |const|                                                                 |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_shortest_axis_size<class_AABB_method_get_shortest_axis_size>`\ (\ ) |const|                                                                   |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_support<class_AABB_method_get_support>`\ (\ direction\: :ref:`Vector3<class_Vector3>`\ ) |const|                                              |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_volume<class_AABB_method_get_volume>`\ (\ ) |const|                                                                                           |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`       | :ref:`grow<class_AABB_method_grow>`\ (\ by\: :ref:`float<class_float>`\ ) |const|                                                                       |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_point<class_AABB_method_has_point>`\ (\ point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                      |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_surface<class_AABB_method_has_surface>`\ (\ ) |const|                                                                                         |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_volume<class_AABB_method_has_volume>`\ (\ ) |const|                                                                                           |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`       | :ref:`intersection<class_AABB_method_intersection>`\ (\ with\: :ref:`AABB<class_AABB>`\ ) |const|                                                       |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`intersects<class_AABB_method_intersects>`\ (\ with\: :ref:`AABB<class_AABB>`\ ) |const|                                                           |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`intersects_plane<class_AABB_method_intersects_plane>`\ (\ plane\: :ref:`Plane<class_Plane>`\ ) |const|                                            |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`intersects_ray<class_AABB_method_intersects_ray>`\ (\ from\: :ref:`Vector3<class_Vector3>`, dir\: :ref:`Vector3<class_Vector3>`\ ) |const|        |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`intersects_segment<class_AABB_method_intersects_segment>`\ (\ from\: :ref:`Vector3<class_Vector3>`, to\: :ref:`Vector3<class_Vector3>`\ ) |const| |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_equal_approx<class_AABB_method_is_equal_approx>`\ (\ aabb\: :ref:`AABB<class_AABB>`\ ) |const|                                                 |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_finite<class_AABB_method_is_finite>`\ (\ ) |const|                                                                                             |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`       | :ref:`merge<class_AABB_method_merge>`\ (\ with\: :ref:`AABB<class_AABB>`\ ) |const|                                                                     |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator !=<class_AABB_operator_neq_AABB>`\ (\ right\: :ref:`AABB<class_AABB>`\ )                     |
> +-------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`operator *<class_AABB_operator_mul_Transform3D>`\ (\ right\: :ref:`Transform3D<class_Transform3D>`\ ) |
> +-------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator ==<class_AABB_operator_eq_AABB>`\ (\ right\: :ref:`AABB<class_AABB>`\ )                      |
> +-------------------------+-------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **end** = `Vector3(0, 0, 0)` [🔗<class_AABB_property_end>]

The ending point. This is usually the corner on the top-right and back of the bounding box, and is equivalent to `position + size`. Setting this point affects the [size<class_AABB_property_size>].


----



[Vector3<class_Vector3>] **position** = `Vector3(0, 0, 0)` [🔗<class_AABB_property_position>]

The origin point. This is usually the corner on the bottom-left and forward of the bounding box.


----



[Vector3<class_Vector3>] **size** = `Vector3(0, 0, 0)` [🔗<class_AABB_property_size>]

The bounding box's width, height, and depth starting from [position<class_AABB_property_position>]. Setting this value also affects the [end<class_AABB_property_end>] point.

\ **Note:** It's recommended setting the width, height, and depth to non-negative values. This is because most methods in Godot assume that the [position<class_AABB_property_position>] is the bottom-left-forward corner, and the [end<class_AABB_property_end>] is the top-right-back corner. To get an equivalent bounding box with non-negative size, use [abs()<class_AABB_method_abs>].


----


## Constructor Descriptions



[AABB<class_AABB>] **AABB**\ (\ ) [🔗<class_AABB_constructor_AABB>]

Constructs an **AABB** with its [position<class_AABB_property_position>] and [size<class_AABB_property_size>] set to [Vector3.ZERO<class_Vector3_constant_ZERO>].


----


[AABB<class_AABB>] **AABB**\ (\ from\: [AABB<class_AABB>]\ )

Constructs an **AABB** as a copy of the given **AABB**.


----


[AABB<class_AABB>] **AABB**\ (\ position\: [Vector3<class_Vector3>], size\: [Vector3<class_Vector3>]\ )

Constructs an **AABB** by `position` and `size`.


----


## Method Descriptions



[AABB<class_AABB>] **abs**\ (\ ) |const| [🔗<class_AABB_method_abs>]

Returns an **AABB** equivalent to this bounding box, with its width, height, and depth modified to be non-negative values.


> **TABS**
>

    var box = AABB(Vector3(5, 0, 5), Vector3(-20, -10, -5))
    var absolute = box.abs()
    print(absolute.position) # Prints (-15.0, -10.0, 0.0)
    print(absolute.size)     # Prints (20.0, 10.0, 5.0)


    var box = new Aabb(new Vector3(5, 0, 5), new Vector3(-20, -10, -5));
    var absolute = box.Abs();
    GD.Print(absolute.Position); // Prints (-15, -10, 0)
    GD.Print(absolute.Size);     // Prints (20, 10, 5)



\ **Note:** It's recommended to use this method when [size<class_AABB_property_size>] is negative, as most other methods in Godot assume that the [size<class_AABB_property_size>]'s components are greater than `0`.


----



[bool<class_bool>] **encloses**\ (\ with\: [AABB<class_AABB>]\ ) |const| [🔗<class_AABB_method_encloses>]

Returns `true` if this bounding box *completely* encloses the `with` box. The edges of both boxes are included.


> **TABS**
>

    var a = AABB(Vector3(0, 0, 0), Vector3(4, 4, 4))
    var b = AABB(Vector3(1, 1, 1), Vector3(3, 3, 3))
    var c = AABB(Vector3(2, 2, 2), Vector3(8, 8, 8))

    print(a.encloses(a)) # Prints true
    print(a.encloses(b)) # Prints true
    print(a.encloses(c)) # Prints false


    var a = new Aabb(new Vector3(0, 0, 0), new Vector3(4, 4, 4));
    var b = new Aabb(new Vector3(1, 1, 1), new Vector3(3, 3, 3));
    var c = new Aabb(new Vector3(2, 2, 2), new Vector3(8, 8, 8));

    GD.Print(a.Encloses(a)); // Prints True
    GD.Print(a.Encloses(b)); // Prints True
    GD.Print(a.Encloses(c)); // Prints False




----



[AABB<class_AABB>] **expand**\ (\ to_point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_AABB_method_expand>]

Returns a copy of this bounding box expanded to align the edges with the given `to_point`, if necessary.


> **TABS**
>

    var box = AABB(Vector3(0, 0, 0), Vector3(5, 2, 5))

    box = box.expand(Vector3(10, 0, 0))
    print(box.position) # Prints (0.0, 0.0, 0.0)
    print(box.size)     # Prints (10.0, 2.0, 5.0)

    box = box.expand(Vector3(-5, 0, 5))
    print(box.position) # Prints (-5.0, 0.0, 0.0)
    print(box.size)     # Prints (15.0, 2.0, 5.0)


    var box = new Aabb(new Vector3(0, 0, 0), new Vector3(5, 2, 5));

    box = box.Expand(new Vector3(10, 0, 0));
    GD.Print(box.Position); // Prints (0, 0, 0)
    GD.Print(box.Size);     // Prints (10, 2, 5)

    box = box.Expand(new Vector3(-5, 0, 5));
    GD.Print(box.Position); // Prints (-5, 0, 0)
    GD.Print(box.Size);     // Prints (15, 2, 5)




----



[Vector3<class_Vector3>] **get_center**\ (\ ) |const| [🔗<class_AABB_method_get_center>]

Returns the center point of the bounding box. This is the same as `position + (size / 2.0)`.


----



[Vector3<class_Vector3>] **get_endpoint**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_AABB_method_get_endpoint>]

Returns the position of one of the 8 vertices that compose this bounding box. With an `idx` of `0` this is the same as [position<class_AABB_property_position>], and an `idx` of `7` is the same as [end<class_AABB_property_end>].


----



[Vector3<class_Vector3>] **get_longest_axis**\ (\ ) |const| [🔗<class_AABB_method_get_longest_axis>]

Returns the longest normalized axis of this bounding box's [size<class_AABB_property_size>], as a [Vector3<class_Vector3>] ([Vector3.RIGHT<class_Vector3_constant_RIGHT>], [Vector3.UP<class_Vector3_constant_UP>], or [Vector3.BACK<class_Vector3_constant_BACK>]).


> **TABS**
>

    var box = AABB(Vector3(0, 0, 0), Vector3(2, 4, 8))

    print(box.get_longest_axis())       # Prints (0.0, 0.0, 1.0)
    print(box.get_longest_axis_index()) # Prints 2
    print(box.get_longest_axis_size())  # Prints 8.0


    var box = new Aabb(new Vector3(0, 0, 0), new Vector3(2, 4, 8));

    GD.Print(box.GetLongestAxis());      // Prints (0, 0, 1)
    GD.Print(box.GetLongestAxisIndex()); // Prints Z
    GD.Print(box.GetLongestAxisSize());  // Prints 8



See also [get_longest_axis_index()<class_AABB_method_get_longest_axis_index>] and [get_longest_axis_size()<class_AABB_method_get_longest_axis_size>].


----



[int<class_int>] **get_longest_axis_index**\ (\ ) |const| [🔗<class_AABB_method_get_longest_axis_index>]

Returns the index to the longest axis of this bounding box's [size<class_AABB_property_size>] (see [Vector3.AXIS_X<class_Vector3_constant_AXIS_X>], [Vector3.AXIS_Y<class_Vector3_constant_AXIS_Y>], and [Vector3.AXIS_Z<class_Vector3_constant_AXIS_Z>]).

For an example, see [get_longest_axis()<class_AABB_method_get_longest_axis>].


----



[float<class_float>] **get_longest_axis_size**\ (\ ) |const| [🔗<class_AABB_method_get_longest_axis_size>]

Returns the longest dimension of this bounding box's [size<class_AABB_property_size>].

For an example, see [get_longest_axis()<class_AABB_method_get_longest_axis>].


----



[Vector3<class_Vector3>] **get_shortest_axis**\ (\ ) |const| [🔗<class_AABB_method_get_shortest_axis>]

Returns the shortest normalized axis of this bounding box's [size<class_AABB_property_size>], as a [Vector3<class_Vector3>] ([Vector3.RIGHT<class_Vector3_constant_RIGHT>], [Vector3.UP<class_Vector3_constant_UP>], or [Vector3.BACK<class_Vector3_constant_BACK>]).


> **TABS**
>

    var box = AABB(Vector3(0, 0, 0), Vector3(2, 4, 8))

    print(box.get_shortest_axis())       # Prints (1.0, 0.0, 0.0)
    print(box.get_shortest_axis_index()) # Prints 0
    print(box.get_shortest_axis_size())  # Prints 2.0


    var box = new Aabb(new Vector3(0, 0, 0), new Vector3(2, 4, 8));

    GD.Print(box.GetShortestAxis());      // Prints (1, 0, 0)
    GD.Print(box.GetShortestAxisIndex()); // Prints X
    GD.Print(box.GetShortestAxisSize());  // Prints 2



See also [get_shortest_axis_index()<class_AABB_method_get_shortest_axis_index>] and [get_shortest_axis_size()<class_AABB_method_get_shortest_axis_size>].


----



[int<class_int>] **get_shortest_axis_index**\ (\ ) |const| [🔗<class_AABB_method_get_shortest_axis_index>]

Returns the index to the shortest axis of this bounding box's [size<class_AABB_property_size>] (see [Vector3.AXIS_X<class_Vector3_constant_AXIS_X>], [Vector3.AXIS_Y<class_Vector3_constant_AXIS_Y>], and [Vector3.AXIS_Z<class_Vector3_constant_AXIS_Z>]).

For an example, see [get_shortest_axis()<class_AABB_method_get_shortest_axis>].


----



[float<class_float>] **get_shortest_axis_size**\ (\ ) |const| [🔗<class_AABB_method_get_shortest_axis_size>]

Returns the shortest dimension of this bounding box's [size<class_AABB_property_size>].

For an example, see [get_shortest_axis()<class_AABB_method_get_shortest_axis>].


----



[Vector3<class_Vector3>] **get_support**\ (\ direction\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_AABB_method_get_support>]

Returns the vertex's position of this bounding box that's the farthest in the given direction. This point is commonly known as the support point in collision detection algorithms.


----



[float<class_float>] **get_volume**\ (\ ) |const| [🔗<class_AABB_method_get_volume>]

Returns the bounding box's volume. This is equivalent to `size.x * size.y * size.z`. See also [has_volume()<class_AABB_method_has_volume>].


----



[AABB<class_AABB>] **grow**\ (\ by\: [float<class_float>]\ ) |const| [🔗<class_AABB_method_grow>]

Returns a copy of this bounding box extended on all sides by the given amount `by`. A negative amount shrinks the box instead.


> **TABS**
>

    var a = AABB(Vector3(4, 4, 4), Vector3(8, 8, 8)).grow(4)
    print(a.position) # Prints (0.0, 0.0, 0.0)
    print(a.size)     # Prints (16.0, 16.0, 16.0)

    var b = AABB(Vector3(0, 0, 0), Vector3(8, 4, 2)).grow(2)
    print(b.position) # Prints (-2.0, -2.0, -2.0)
    print(b.size)     # Prints (12.0, 8.0, 6.0)


    var a = new Aabb(new Vector3(4, 4, 4), new Vector3(8, 8, 8)).Grow(4);
    GD.Print(a.Position); // Prints (0, 0, 0)
    GD.Print(a.Size);     // Prints (16, 16, 16)

    var b = new Aabb(new Vector3(0, 0, 0), new Vector3(8, 4, 2)).Grow(2);
    GD.Print(b.Position); // Prints (-2, -2, -2)
    GD.Print(b.Size);     // Prints (12, 8, 6)




----



[bool<class_bool>] **has_point**\ (\ point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_AABB_method_has_point>]

Returns `true` if the bounding box contains the given `point`. By convention, points exactly on the right, top, and front sides are **not** included.

\ **Note:** This method is not reliable for **AABB** with a *negative* [size<class_AABB_property_size>]. Use [abs()<class_AABB_method_abs>] first to get a valid bounding box.


----



[bool<class_bool>] **has_surface**\ (\ ) |const| [🔗<class_AABB_method_has_surface>]

Returns `true` if this bounding box has a surface or a length, that is, at least one component of [size<class_AABB_property_size>] is greater than `0`. Otherwise, returns `false`.


----



[bool<class_bool>] **has_volume**\ (\ ) |const| [🔗<class_AABB_method_has_volume>]

Returns `true` if this bounding box's width, height, and depth are all positive. See also [get_volume()<class_AABB_method_get_volume>].


----



[AABB<class_AABB>] **intersection**\ (\ with\: [AABB<class_AABB>]\ ) |const| [🔗<class_AABB_method_intersection>]

Returns the intersection between this bounding box and `with`. If the boxes do not intersect, returns an empty **AABB**. If the boxes intersect at the edge, returns a flat **AABB** with no volume (see [has_surface()<class_AABB_method_has_surface>] and [has_volume()<class_AABB_method_has_volume>]).


> **TABS**
>

    var box1 = AABB(Vector3(0, 0, 0), Vector3(5, 2, 8))
    var box2 = AABB(Vector3(2, 0, 2), Vector3(8, 4, 4))

    var intersection = box1.intersection(box2)
    print(intersection.position) # Prints (2.0, 0.0, 2.0)
    print(intersection.size)     # Prints (3.0, 2.0, 4.0)


    var box1 = new Aabb(new Vector3(0, 0, 0), new Vector3(5, 2, 8));
    var box2 = new Aabb(new Vector3(2, 0, 2), new Vector3(8, 4, 4));

    var intersection = box1.Intersection(box2);
    GD.Print(intersection.Position); // Prints (2, 0, 2)
    GD.Print(intersection.Size);     // Prints (3, 2, 4)



\ **Note:** If you only need to know whether two bounding boxes are intersecting, use [intersects()<class_AABB_method_intersects>], instead.


----



[bool<class_bool>] **intersects**\ (\ with\: [AABB<class_AABB>]\ ) |const| [🔗<class_AABB_method_intersects>]

Returns `true` if this bounding box overlaps with the box `with`. The edges of both boxes are *always* excluded.


----



[bool<class_bool>] **intersects_plane**\ (\ plane\: [Plane<class_Plane>]\ ) |const| [🔗<class_AABB_method_intersects_plane>]

Returns `true` if this bounding box is on both sides of the given `plane`.


----



[Variant<class_Variant>] **intersects_ray**\ (\ from\: [Vector3<class_Vector3>], dir\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_AABB_method_intersects_ray>]

Returns the first point where this bounding box and the given ray intersect, as a [Vector3<class_Vector3>]. If no intersection occurs, returns `null`.

The ray begin at `from`, faces `dir` and extends towards infinity.


----



[Variant<class_Variant>] **intersects_segment**\ (\ from\: [Vector3<class_Vector3>], to\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_AABB_method_intersects_segment>]

Returns the first point where this bounding box and the given segment intersect, as a [Vector3<class_Vector3>]. If no intersection occurs, returns `null`.

The segment begins at `from` and ends at `to`.


----



[bool<class_bool>] **is_equal_approx**\ (\ aabb\: [AABB<class_AABB>]\ ) |const| [🔗<class_AABB_method_is_equal_approx>]

Returns `true` if this bounding box and `aabb` are approximately equal, by calling [Vector3.is_equal_approx()<class_Vector3_method_is_equal_approx>] on the [position<class_AABB_property_position>] and the [size<class_AABB_property_size>].


----



[bool<class_bool>] **is_finite**\ (\ ) |const| [🔗<class_AABB_method_is_finite>]

Returns `true` if this bounding box's values are finite, by calling [Vector3.is_finite()<class_Vector3_method_is_finite>] on the [position<class_AABB_property_position>] and the [size<class_AABB_property_size>].


----



[AABB<class_AABB>] **merge**\ (\ with\: [AABB<class_AABB>]\ ) |const| [🔗<class_AABB_method_merge>]

Returns an **AABB** that encloses both this bounding box and `with` around the edges. See also [encloses()<class_AABB_method_encloses>].


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [AABB<class_AABB>]\ ) [🔗<class_AABB_operator_neq_AABB>]

Returns `true` if the [position<class_AABB_property_position>] or [size<class_AABB_property_size>] of both bounding boxes are not equal.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_AABB_method_is_equal_approx>] instead, which is more reliable.


----



[AABB<class_AABB>] **operator ***\ (\ right\: [Transform3D<class_Transform3D>]\ ) [🔗<class_AABB_operator_mul_Transform3D>]

Inversely transforms (multiplies) the **AABB** by the given [Transform3D<class_Transform3D>] transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

\ `aabb * transform` is equivalent to `transform.inverse() * aabb`. See [Transform3D.inverse()<class_Transform3D_method_inverse>].

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * aabb` can be used instead. See [Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>].


----



[bool<class_bool>] **operator ==**\ (\ right\: [AABB<class_AABB>]\ ) [🔗<class_AABB_operator_eq_AABB>]

Returns `true` if both [position<class_AABB_property_position>] and [size<class_AABB_property_size>] of the bounding boxes are exactly equal, respectively.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_AABB_method_is_equal_approx>] instead, which is more reliable.

