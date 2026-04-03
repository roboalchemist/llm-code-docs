:github_url: hide



# Vector3i

A 3D vector using integer coordinates.


## Description

A 3-element structure that can be used to represent 3D grid coordinates or any other triplet of integers.

It uses integer coordinates and is therefore preferable to [Vector3<class_Vector3>] when exact precision is required. Note that the values are limited to 32 bits, and unlike [Vector3<class_Vector3>] this cannot be configured with an engine build option. Use [int<class_int>] or [PackedInt64Array<class_PackedInt64Array>] if 64-bit values are needed.

\ **Note:** In a boolean context, a Vector3i will evaluate to `false` if it's equal to `Vector3i(0, 0, 0)`. Otherwise, a Vector3i will always evaluate to `true`.


## Tutorials

- [../tutorials/math/index](Math documentation index .md)

- [../tutorials/math/vector_math](Vector math .md)

- [3Blue1Brown Essence of Linear Algebra ](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+-------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`x<class_Vector3i_property_x>` | ``0`` |
> +-----------------------+-------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`y<class_Vector3i_property_y>` | ``0`` |
> +-----------------------+-------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`z<class_Vector3i_property_z>` | ``0`` |
> +-----------------------+-------------------------------------+-------+
>

## Constructors

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`Vector3i<class_Vector3i_constructor_Vector3i>`\ (\ )                                                                                  |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`Vector3i<class_Vector3i_constructor_Vector3i>`\ (\ from\: :ref:`Vector3i<class_Vector3i>`\ )                                          |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`Vector3i<class_Vector3i_constructor_Vector3i>`\ (\ from\: :ref:`Vector3<class_Vector3>`\ )                                            |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`Vector3i<class_Vector3i_constructor_Vector3i>`\ (\ x\: :ref:`int<class_int>`, y\: :ref:`int<class_int>`, z\: :ref:`int<class_int>`\ ) |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`abs<class_Vector3i_method_abs>`\ (\ ) |const|                                                                                   |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`clamp<class_Vector3i_method_clamp>`\ (\ min\: :ref:`Vector3i<class_Vector3i>`, max\: :ref:`Vector3i<class_Vector3i>`\ ) |const| |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`clampi<class_Vector3i_method_clampi>`\ (\ min\: :ref:`int<class_int>`, max\: :ref:`int<class_int>`\ ) |const|                   |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`distance_squared_to<class_Vector3i_method_distance_squared_to>`\ (\ to\: :ref:`Vector3i<class_Vector3i>`\ ) |const|             |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`       | :ref:`distance_to<class_Vector3i_method_distance_to>`\ (\ to\: :ref:`Vector3i<class_Vector3i>`\ ) |const|                             |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`       | :ref:`length<class_Vector3i_method_length>`\ (\ ) |const|                                                                             |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`length_squared<class_Vector3i_method_length_squared>`\ (\ ) |const|                                                             |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`max<class_Vector3i_method_max>`\ (\ with\: :ref:`Vector3i<class_Vector3i>`\ ) |const|                                           |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`max_axis_index<class_Vector3i_method_max_axis_index>`\ (\ ) |const|                                                             |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`maxi<class_Vector3i_method_maxi>`\ (\ with\: :ref:`int<class_int>`\ ) |const|                                                   |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`min<class_Vector3i_method_min>`\ (\ with\: :ref:`Vector3i<class_Vector3i>`\ ) |const|                                           |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`min_axis_index<class_Vector3i_method_min_axis_index>`\ (\ ) |const|                                                             |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`mini<class_Vector3i_method_mini>`\ (\ with\: :ref:`int<class_int>`\ ) |const|                                                   |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`sign<class_Vector3i_method_sign>`\ (\ ) |const|                                                                                 |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`snapped<class_Vector3i_method_snapped>`\ (\ step\: :ref:`Vector3i<class_Vector3i>`\ ) |const|                                   |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`snappedi<class_Vector3i_method_snappedi>`\ (\ step\: :ref:`int<class_int>`\ ) |const|                                           |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`operator !=<class_Vector3i_operator_neq_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )  |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator %<class_Vector3i_operator_mod_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator %<class_Vector3i_operator_mod_int>`\ (\ right\: :ref:`int<class_int>`\ )                  |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator *<class_Vector3i_operator_mul_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`   | :ref:`operator *<class_Vector3i_operator_mul_float>`\ (\ right\: :ref:`float<class_float>`\ )            |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator *<class_Vector3i_operator_mul_int>`\ (\ right\: :ref:`int<class_int>`\ )                  |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator +<class_Vector3i_operator_sum_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator -<class_Vector3i_operator_dif_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator /<class_Vector3i_operator_div_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`   | :ref:`operator /<class_Vector3i_operator_div_float>`\ (\ right\: :ref:`float<class_float>`\ )            |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator /<class_Vector3i_operator_div_int>`\ (\ right\: :ref:`int<class_int>`\ )                  |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`operator \<<class_Vector3i_operator_lt_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`operator \<=<class_Vector3i_operator_lte_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ ) |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`operator ==<class_Vector3i_operator_eq_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )   |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`operator ><class_Vector3i_operator_gt_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )    |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`operator >=<class_Vector3i_operator_gte_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )  |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`operator []<class_Vector3i_operator_idx_int>`\ (\ index\: :ref:`int<class_int>`\ )                 |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator unary+<class_Vector3i_operator_unplus>`\ (\ )                                             |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`operator unary-<class_Vector3i_operator_unminus>`\ (\ )                                            |
> +---------------------------------+----------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Axis**: [🔗<enum_Vector3i_Axis>]



[Axis<enum_Vector3i_Axis>] **AXIS_X** = `0`

Enumerated value for the X axis. Returned by [max_axis_index()<class_Vector3i_method_max_axis_index>] and [min_axis_index()<class_Vector3i_method_min_axis_index>].



[Axis<enum_Vector3i_Axis>] **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by [max_axis_index()<class_Vector3i_method_max_axis_index>] and [min_axis_index()<class_Vector3i_method_min_axis_index>].



[Axis<enum_Vector3i_Axis>] **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by [max_axis_index()<class_Vector3i_method_max_axis_index>] and [min_axis_index()<class_Vector3i_method_min_axis_index>].


----


## Constants



**ZERO** = `Vector3i(0, 0, 0)` [🔗<class_Vector3i_constant_ZERO>]

Zero vector, a vector with all components set to `0`.



**ONE** = `Vector3i(1, 1, 1)` [🔗<class_Vector3i_constant_ONE>]

One vector, a vector with all components set to `1`.



**MIN** = `Vector3i(-2147483648, -2147483648, -2147483648)` [🔗<class_Vector3i_constant_MIN>]

Min vector, a vector with all components equal to `INT32_MIN`. Can be used as a negative integer equivalent of [Vector3.INF<class_Vector3_constant_INF>].



**MAX** = `Vector3i(2147483647, 2147483647, 2147483647)` [🔗<class_Vector3i_constant_MAX>]

Max vector, a vector with all components equal to `INT32_MAX`. Can be used as an integer equivalent of [Vector3.INF<class_Vector3_constant_INF>].



**LEFT** = `Vector3i(-1, 0, 0)` [🔗<class_Vector3i_constant_LEFT>]

Left unit vector. Represents the local direction of left, and the global direction of west.



**RIGHT** = `Vector3i(1, 0, 0)` [🔗<class_Vector3i_constant_RIGHT>]

Right unit vector. Represents the local direction of right, and the global direction of east.



**UP** = `Vector3i(0, 1, 0)` [🔗<class_Vector3i_constant_UP>]

Up unit vector.



**DOWN** = `Vector3i(0, -1, 0)` [🔗<class_Vector3i_constant_DOWN>]

Down unit vector.



**FORWARD** = `Vector3i(0, 0, -1)` [🔗<class_Vector3i_constant_FORWARD>]

Forward unit vector. Represents the local direction of forward, and the global direction of north.



**BACK** = `Vector3i(0, 0, 1)` [🔗<class_Vector3i_constant_BACK>]

Back unit vector. Represents the local direction of back, and the global direction of south.


----


## Property Descriptions



[int<class_int>] **x** = `0` [🔗<class_Vector3i_property_x>]

The vector's X component. Also accessible by using the index position `[0]`.


----



[int<class_int>] **y** = `0` [🔗<class_Vector3i_property_y>]

The vector's Y component. Also accessible by using the index position `[1]`.


----



[int<class_int>] **z** = `0` [🔗<class_Vector3i_property_z>]

The vector's Z component. Also accessible by using the index position `[2]`.


----


## Constructor Descriptions



[Vector3i<class_Vector3i>] **Vector3i**\ (\ ) [🔗<class_Vector3i_constructor_Vector3i>]

Constructs a default-initialized **Vector3i** with all components set to `0`.


----


[Vector3i<class_Vector3i>] **Vector3i**\ (\ from\: [Vector3i<class_Vector3i>]\ )

Constructs a **Vector3i** as a copy of the given **Vector3i**.


----


[Vector3i<class_Vector3i>] **Vector3i**\ (\ from\: [Vector3<class_Vector3>]\ )

Constructs a new **Vector3i** from the given [Vector3<class_Vector3>] by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result of [Vector3.ceil()<class_Vector3_method_ceil>], [Vector3.floor()<class_Vector3_method_floor>] or [Vector3.round()<class_Vector3_method_round>] to this constructor instead.


----


[Vector3i<class_Vector3i>] **Vector3i**\ (\ x\: [int<class_int>], y\: [int<class_int>], z\: [int<class_int>]\ )

Returns a **Vector3i** with the given components.


----


## Method Descriptions



[Vector3i<class_Vector3i>] **abs**\ (\ ) |const| [🔗<class_Vector3i_method_abs>]

Returns a new vector with all components in absolute values (i.e. positive).


----



[Vector3i<class_Vector3i>] **clamp**\ (\ min\: [Vector3i<class_Vector3i>], max\: [Vector3i<class_Vector3i>]\ ) |const| [🔗<class_Vector3i_method_clamp>]

Returns a new vector with all components clamped between the components of `min` and `max`, by running [@GlobalScope.clamp()<class_@GlobalScope_method_clamp>] on each component.


----



[Vector3i<class_Vector3i>] **clampi**\ (\ min\: [int<class_int>], max\: [int<class_int>]\ ) |const| [🔗<class_Vector3i_method_clampi>]

Returns a new vector with all components clamped between `min` and `max`, by running [@GlobalScope.clamp()<class_@GlobalScope_method_clamp>] on each component.


----



[int<class_int>] **distance_squared_to**\ (\ to\: [Vector3i<class_Vector3i>]\ ) |const| [🔗<class_Vector3i_method_distance_squared_to>]

Returns the squared distance between this vector and `to`.

This method runs faster than [distance_to()<class_Vector3i_method_distance_to>], so prefer it if you need to compare vectors or need the squared distance for some formula.


----



[float<class_float>] **distance_to**\ (\ to\: [Vector3i<class_Vector3i>]\ ) |const| [🔗<class_Vector3i_method_distance_to>]

Returns the distance between this vector and `to`.


----



[float<class_float>] **length**\ (\ ) |const| [🔗<class_Vector3i_method_length>]

Returns the length (magnitude) of this vector.


----



[int<class_int>] **length_squared**\ (\ ) |const| [🔗<class_Vector3i_method_length_squared>]

Returns the squared length (squared magnitude) of this vector.

This method runs faster than [length()<class_Vector3i_method_length>], so prefer it if you need to compare vectors or need the squared distance for some formula.


----



[Vector3i<class_Vector3i>] **max**\ (\ with\: [Vector3i<class_Vector3i>]\ ) |const| [🔗<class_Vector3i_method_max>]

Returns the component-wise maximum of this and `with`, equivalent to `Vector3i(maxi(x, with.x), maxi(y, with.y), maxi(z, with.z))`.


----



[int<class_int>] **max_axis_index**\ (\ ) |const| [🔗<class_Vector3i_method_max_axis_index>]

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_X<class_Vector3i_constant_AXIS_X>].


----



[Vector3i<class_Vector3i>] **maxi**\ (\ with\: [int<class_int>]\ ) |const| [🔗<class_Vector3i_method_maxi>]

Returns the component-wise maximum of this and `with`, equivalent to `Vector3i(maxi(x, with), maxi(y, with), maxi(z, with))`.


----



[Vector3i<class_Vector3i>] **min**\ (\ with\: [Vector3i<class_Vector3i>]\ ) |const| [🔗<class_Vector3i_method_min>]

Returns the component-wise minimum of this and `with`, equivalent to `Vector3i(mini(x, with.x), mini(y, with.y), mini(z, with.z))`.


----



[int<class_int>] **min_axis_index**\ (\ ) |const| [🔗<class_Vector3i_method_min_axis_index>]

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_Z<class_Vector3i_constant_AXIS_Z>].


----



[Vector3i<class_Vector3i>] **mini**\ (\ with\: [int<class_int>]\ ) |const| [🔗<class_Vector3i_method_mini>]

Returns the component-wise minimum of this and `with`, equivalent to `Vector3i(mini(x, with), mini(y, with), mini(z, with))`.


----



[Vector3i<class_Vector3i>] **sign**\ (\ ) |const| [🔗<class_Vector3i_method_sign>]

Returns a new vector with each component set to `1` if it's positive, `-1` if it's negative, and `0` if it's zero. The result is identical to calling [@GlobalScope.sign()<class_@GlobalScope_method_sign>] on each component.


----



[Vector3i<class_Vector3i>] **snapped**\ (\ step\: [Vector3i<class_Vector3i>]\ ) |const| [🔗<class_Vector3i_method_snapped>]

Returns a new vector with each component snapped to the closest multiple of the corresponding component in `step`.


----



[Vector3i<class_Vector3i>] **snappedi**\ (\ step\: [int<class_int>]\ ) |const| [🔗<class_Vector3i_method_snappedi>]

Returns a new vector with each component snapped to the closest multiple of `step`.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_neq_Vector3i>]

Returns `true` if the vectors are not equal.


----



[Vector3i<class_Vector3i>] **operator %**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_mod_Vector3i>]

Gets the remainder of each component of the **Vector3i** with the components of the given **Vector3i**. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using [@GlobalScope.posmod()<class_@GlobalScope_method_posmod>] instead if you want to handle negative numbers.

::

    print(Vector3i(10, -20, 30) % Vector3i(7, 8, 9)) # Prints (3, -4, 3)


----



[Vector3i<class_Vector3i>] **operator %**\ (\ right\: [int<class_int>]\ ) [🔗<class_Vector3i_operator_mod_int>]

Gets the remainder of each component of the **Vector3i** with the given [int<class_int>]. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using [@GlobalScope.posmod()<class_@GlobalScope_method_posmod>] instead if you want to handle negative numbers.

::

    print(Vector3i(10, -20, 30) % 7) # Prints (3, -6, 2)


----



[Vector3i<class_Vector3i>] **operator ***\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_mul_Vector3i>]

Multiplies each component of the **Vector3i** by the components of the given **Vector3i**.

::

    print(Vector3i(10, 20, 30) * Vector3i(3, 4, 5)) # Prints (30, 80, 150)


----



[Vector3<class_Vector3>] **operator ***\ (\ right\: [float<class_float>]\ ) [🔗<class_Vector3i_operator_mul_float>]

Multiplies each component of the **Vector3i** by the given [float<class_float>]. Returns a [Vector3<class_Vector3>].

::

    print(Vector3i(10, 15, 20) * 0.9) # Prints (9.0, 13.5, 18.0)


----



[Vector3i<class_Vector3i>] **operator ***\ (\ right\: [int<class_int>]\ ) [🔗<class_Vector3i_operator_mul_int>]

Multiplies each component of the **Vector3i** by the given [int<class_int>].


----



[Vector3i<class_Vector3i>] **operator +**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_sum_Vector3i>]

Adds each component of the **Vector3i** by the components of the given **Vector3i**.

::

    print(Vector3i(10, 20, 30) + Vector3i(3, 4, 5)) # Prints (13, 24, 35)


----



[Vector3i<class_Vector3i>] **operator -**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_dif_Vector3i>]

Subtracts each component of the **Vector3i** by the components of the given **Vector3i**.

::

    print(Vector3i(10, 20, 30) - Vector3i(3, 4, 5)) # Prints (7, 16, 25)


----



[Vector3i<class_Vector3i>] **operator /**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_div_Vector3i>]

Divides each component of the **Vector3i** by the components of the given **Vector3i**.

::

    print(Vector3i(10, 20, 30) / Vector3i(2, 5, 3)) # Prints (5, 4, 10)


----



[Vector3<class_Vector3>] **operator /**\ (\ right\: [float<class_float>]\ ) [🔗<class_Vector3i_operator_div_float>]

Divides each component of the **Vector3i** by the given [float<class_float>]. Returns a [Vector3<class_Vector3>].

::

    print(Vector3i(1, 2, 3) / 2.5) # Prints (0.4, 0.8, 1.2)


----



[Vector3i<class_Vector3i>] **operator /**\ (\ right\: [int<class_int>]\ ) [🔗<class_Vector3i_operator_div_int>]

Divides each component of the **Vector3i** by the given [int<class_int>].


----



[bool<class_bool>] **operator <**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_lt_Vector3i>]

Compares two **Vector3i** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.


----



[bool<class_bool>] **operator <=**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_lte_Vector3i>]

Compares two **Vector3i** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.


----



[bool<class_bool>] **operator ==**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_eq_Vector3i>]

Returns `true` if the vectors are equal.


----



[bool<class_bool>] **operator >**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_gt_Vector3i>]

Compares two **Vector3i** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.


----



[bool<class_bool>] **operator >=**\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_Vector3i_operator_gte_Vector3i>]

Compares two **Vector3i** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.


----



[int<class_int>] **operator []**\ (\ index\: [int<class_int>]\ ) [🔗<class_Vector3i_operator_idx_int>]

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, `v[1]` is equivalent to `v.y`, and `v[2]` is equivalent to `v.z`.


----



[Vector3i<class_Vector3i>] **operator unary+**\ (\ ) [🔗<class_Vector3i_operator_unplus>]

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.


----



[Vector3i<class_Vector3i>] **operator unary-**\ (\ ) [🔗<class_Vector3i_operator_unminus>]

Returns the negative value of the **Vector3i**. This is the same as writing `Vector3i(-v.x, -v.y, -v.z)`. This operation flips the direction of the vector while keeping the same magnitude.

