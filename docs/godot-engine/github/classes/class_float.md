:github_url: hide



# float

A built-in type for floating-point numbers.


## Description

The **float** built-in type is a 64-bit double-precision floating-point number, equivalent to `double` in C++. This type has 14 reliable decimal digits of precision. The maximum value of **float** is approximately `1.79769e308`, and the minimum is approximately `-1.79769e308`.

Many methods and properties in the engine use 32-bit single-precision floating-point numbers instead, equivalent to `float` in C++, which have 6 reliable decimal digits of precision. For data structures such as [Vector2<class_Vector2>] and [Vector3<class_Vector3>], Godot uses 32-bit floating-point numbers by default, but it can be changed to use 64-bit doubles if Godot is compiled with the `precision=double` option.

Math done using the **float** type is not guaranteed to be exact and will often result in small errors. You should usually use the [@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>] and [@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>] methods instead of `==` to compare **float** values for equality.


## Tutorials

- [Wikipedia: Double-precision floating-point format ](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)_

- [Wikipedia: Single-precision floating-point format ](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)_


## Constructors

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`float<class_float_constructor_float>`\ (\ )                                     |
> +---------------------------+---------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`float<class_float_constructor_float>`\ (\ from\: :ref:`float<class_float>`\ )   |
> +---------------------------+---------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`float<class_float_constructor_float>`\ (\ from\: :ref:`String<class_String>`\ ) |
> +---------------------------+---------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`float<class_float_constructor_float>`\ (\ from\: :ref:`bool<class_bool>`\ )     |
> +---------------------------+---------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`float<class_float_constructor_float>`\ (\ from\: :ref:`int<class_int>`\ )       |
> +---------------------------+---------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator !=<class_float_operator_neq_float>`\ (\ right\: :ref:`float<class_float>`\ )               |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator !=<class_float_operator_neq_int>`\ (\ right\: :ref:`int<class_int>`\ )                     |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`           | :ref:`operator *<class_float_operator_mul_Color>`\ (\ right\: :ref:`Color<class_Color>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>` | :ref:`operator *<class_float_operator_mul_Quaternion>`\ (\ right\: :ref:`Quaternion<class_Quaternion>`\ ) |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`       | :ref:`operator *<class_float_operator_mul_Vector2>`\ (\ right\: :ref:`Vector2<class_Vector2>`\ )          |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`       | :ref:`operator *<class_float_operator_mul_Vector2i>`\ (\ right\: :ref:`Vector2i<class_Vector2i>`\ )       |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`       | :ref:`operator *<class_float_operator_mul_Vector3>`\ (\ right\: :ref:`Vector3<class_Vector3>`\ )          |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`       | :ref:`operator *<class_float_operator_mul_Vector3i>`\ (\ right\: :ref:`Vector3i<class_Vector3i>`\ )       |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector4<class_Vector4>`       | :ref:`operator *<class_float_operator_mul_Vector4>`\ (\ right\: :ref:`Vector4<class_Vector4>`\ )          |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`Vector4<class_Vector4>`       | :ref:`operator *<class_float_operator_mul_Vector4i>`\ (\ right\: :ref:`Vector4i<class_Vector4i>`\ )       |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator *<class_float_operator_mul_float>`\ (\ right\: :ref:`float<class_float>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator *<class_float_operator_mul_int>`\ (\ right\: :ref:`int<class_int>`\ )                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator **<class_float_operator_pow_float>`\ (\ right\: :ref:`float<class_float>`\ )               |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator **<class_float_operator_pow_int>`\ (\ right\: :ref:`int<class_int>`\ )                     |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator +<class_float_operator_sum_float>`\ (\ right\: :ref:`float<class_float>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator +<class_float_operator_sum_int>`\ (\ right\: :ref:`int<class_int>`\ )                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator -<class_float_operator_dif_float>`\ (\ right\: :ref:`float<class_float>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator -<class_float_operator_dif_int>`\ (\ right\: :ref:`int<class_int>`\ )                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator /<class_float_operator_div_float>`\ (\ right\: :ref:`float<class_float>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator /<class_float_operator_div_int>`\ (\ right\: :ref:`int<class_int>`\ )                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator \<<class_float_operator_lt_float>`\ (\ right\: :ref:`float<class_float>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator \<<class_float_operator_lt_int>`\ (\ right\: :ref:`int<class_int>`\ )                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator \<=<class_float_operator_lte_float>`\ (\ right\: :ref:`float<class_float>`\ )              |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator \<=<class_float_operator_lte_int>`\ (\ right\: :ref:`int<class_int>`\ )                    |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator ==<class_float_operator_eq_float>`\ (\ right\: :ref:`float<class_float>`\ )                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator ==<class_float_operator_eq_int>`\ (\ right\: :ref:`int<class_int>`\ )                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator ><class_float_operator_gt_float>`\ (\ right\: :ref:`float<class_float>`\ )                 |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator ><class_float_operator_gt_int>`\ (\ right\: :ref:`int<class_int>`\ )                       |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator >=<class_float_operator_gte_float>`\ (\ right\: :ref:`float<class_float>`\ )               |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`operator >=<class_float_operator_gte_int>`\ (\ right\: :ref:`int<class_int>`\ )                     |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator unary+<class_float_operator_unplus>`\ (\ )                                                 |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`operator unary-<class_float_operator_unminus>`\ (\ )                                                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[float<class_float>] **float**\ (\ ) [🔗<class_float_constructor_float>]

Constructs a default-initialized **float** set to `0.0`.


----


[float<class_float>] **float**\ (\ from\: [float<class_float>]\ )

Constructs a **float** as a copy of the given **float**.


----


[float<class_float>] **float**\ (\ from\: [String<class_String>]\ )

Converts a [String<class_String>] to a **float**, following the same rules as [String.to_float()<class_String_method_to_float>].


----


[float<class_float>] **float**\ (\ from\: [bool<class_bool>]\ )

Cast a [bool<class_bool>] value to a floating-point value, `float(true)` will be equal to 1.0 and `float(false)` will be equal to 0.0.


----


[float<class_float>] **float**\ (\ from\: [int<class_int>]\ )

Cast an [int<class_int>] value to a floating-point value, `float(1)` will be equal to `1.0`.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_neq_float>]

Returns `true` if two floats are different from each other.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.


----



[bool<class_bool>] **operator !=**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_neq_int>]

Returns `true` if the integer has different value than the float.


----



[Color<class_Color>] **operator ***\ (\ right\: [Color<class_Color>]\ ) [🔗<class_float_operator_mul_Color>]

Multiplies each component of the [Color<class_Color>], including the alpha, by the given **float**.

::

    print(1.5 * Color(0.5, 0.5, 0.5)) # Prints (0.75, 0.75, 0.75, 1.5)


----



[Quaternion<class_Quaternion>] **operator ***\ (\ right\: [Quaternion<class_Quaternion>]\ ) [🔗<class_float_operator_mul_Quaternion>]

Multiplies each component of the [Quaternion<class_Quaternion>] by the given **float**. This operation is not meaningful on its own, but it can be used as a part of a larger expression.


----



[Vector2<class_Vector2>] **operator ***\ (\ right\: [Vector2<class_Vector2>]\ ) [🔗<class_float_operator_mul_Vector2>]

Multiplies each component of the [Vector2<class_Vector2>] by the given **float**.

::

    print(2.5 * Vector2(1, 3)) # Prints (2.5, 7.5)


----



[Vector2<class_Vector2>] **operator ***\ (\ right\: [Vector2i<class_Vector2i>]\ ) [🔗<class_float_operator_mul_Vector2i>]

Multiplies each component of the [Vector2i<class_Vector2i>] by the given **float**. Returns a [Vector2<class_Vector2>].

::

    print(0.9 * Vector2i(10, 15)) # Prints (9.0, 13.5)


----



[Vector3<class_Vector3>] **operator ***\ (\ right\: [Vector3<class_Vector3>]\ ) [🔗<class_float_operator_mul_Vector3>]

Multiplies each component of the [Vector3<class_Vector3>] by the given **float**.


----



[Vector3<class_Vector3>] **operator ***\ (\ right\: [Vector3i<class_Vector3i>]\ ) [🔗<class_float_operator_mul_Vector3i>]

Multiplies each component of the [Vector3i<class_Vector3i>] by the given **float**. Returns a [Vector3<class_Vector3>].

::

    print(0.9 * Vector3i(10, 15, 20)) # Prints (9.0, 13.5, 18.0)


----



[Vector4<class_Vector4>] **operator ***\ (\ right\: [Vector4<class_Vector4>]\ ) [🔗<class_float_operator_mul_Vector4>]

Multiplies each component of the [Vector4<class_Vector4>] by the given **float**.


----



[Vector4<class_Vector4>] **operator ***\ (\ right\: [Vector4i<class_Vector4i>]\ ) [🔗<class_float_operator_mul_Vector4i>]

Multiplies each component of the [Vector4i<class_Vector4i>] by the given **float**. Returns a [Vector4<class_Vector4>].

::

    print(0.9 * Vector4i(10, 15, 20, -10)) # Prints (9.0, 13.5, 18.0, -9.0)


----



[float<class_float>] **operator ***\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_mul_float>]

Multiplies two **float**\ s.


----



[float<class_float>] **operator ***\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_mul_int>]

Multiplies a **float** and an [int<class_int>]. The result is a **float**.


----



[float<class_float>] **operator ****\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_pow_float>]

Raises a **float** to a power of a **float**.

::

    print(39.0625**0.25) # 2.5


----



[float<class_float>] **operator ****\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_pow_int>]

Raises a **float** to a power of an [int<class_int>]. The result is a **float**.

::

    print(0.9**3) # 0.729


----



[float<class_float>] **operator +**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_sum_float>]

Adds two floats.


----



[float<class_float>] **operator +**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_sum_int>]

Adds a **float** and an [int<class_int>]. The result is a **float**.


----



[float<class_float>] **operator -**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_dif_float>]

Subtracts a float from a float.


----



[float<class_float>] **operator -**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_dif_int>]

Subtracts an [int<class_int>] from a **float**. The result is a **float**.


----



[float<class_float>] **operator /**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_div_float>]

Divides two floats.


----



[float<class_float>] **operator /**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_div_int>]

Divides a **float** by an [int<class_int>]. The result is a **float**.


----



[bool<class_bool>] **operator <**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_lt_float>]

Returns `true` if the left float is less than the right one.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.


----



[bool<class_bool>] **operator <**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_lt_int>]

Returns `true` if this **float** is less than the given [int<class_int>].


----



[bool<class_bool>] **operator <=**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_lte_float>]

Returns `true` if the left float is less than or equal to the right one.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.


----



[bool<class_bool>] **operator <=**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_lte_int>]

Returns `true` if this **float** is less than or equal to the given [int<class_int>].


----



[bool<class_bool>] **operator ==**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_eq_float>]

Returns `true` if both floats are exactly equal.

\ **Note:** Due to floating-point precision errors, consider using [@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>] or [@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>] instead, which are more reliable.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.


----



[bool<class_bool>] **operator ==**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_eq_int>]

Returns `true` if the **float** and the given [int<class_int>] are equal.


----



[bool<class_bool>] **operator >**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_gt_float>]

Returns `true` if the left float is greater than the right one.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.


----



[bool<class_bool>] **operator >**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_gt_int>]

Returns `true` if this **float** is greater than the given [int<class_int>].


----



[bool<class_bool>] **operator >=**\ (\ right\: [float<class_float>]\ ) [🔗<class_float_operator_gte_float>]

Returns `true` if the left float is greater than or equal to the right one.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.


----



[bool<class_bool>] **operator >=**\ (\ right\: [int<class_int>]\ ) [🔗<class_float_operator_gte_int>]

Returns `true` if this **float** is greater than or equal to the given [int<class_int>].


----



[float<class_float>] **operator unary+**\ (\ ) [🔗<class_float_operator_unplus>]

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.


----



[float<class_float>] **operator unary-**\ (\ ) [🔗<class_float_operator_unminus>]

Returns the negative value of the **float**. If positive, turns the number negative. If negative, turns the number positive. With floats, the number zero can be either positive or negative.

