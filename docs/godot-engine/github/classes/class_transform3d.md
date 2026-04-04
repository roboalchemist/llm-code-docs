:github_url: hide



# Transform3D

A 3×4 matrix representing a 3D transformation.


## Description

The **Transform3D** built-in [Variant<class_Variant>] type is a 3×4 matrix representing a transformation in 3D space. It contains a [Basis<class_Basis>], which on its own can represent rotation, scale, and shear. Additionally, combined with its own [origin<class_Transform3D_property_origin>], the transform can also represent a translation.

For a general introduction, see the [../tutorials/math/matrices_and_transforms](Matrices and transforms .md) tutorial.

\ **Note:** Godot uses a [right-handed coordinate system ](https://en.wikipedia.org/wiki/Right-hand_rule)_, which is a common standard. For directions, the convention for built-in types like [Camera3D<class_Camera3D>] is for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the [3D asset direction conventions ](../tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html#d-asset-direction-conventions)_ tutorial.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Tutorials

- [../tutorials/math/index](Math documentation index .md)

- [../tutorials/math/matrices_and_transforms](Matrices and transforms .md)

- [../tutorials/3d/using_transforms](Using 3D transforms .md)

- [Matrix Transform Demo ](https://godotengine.org/asset-library/asset/2787)_

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_

- [2.5D Game Demo ](https://godotengine.org/asset-library/asset/2783)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------+--------------------------------------+
> | :ref:`Basis<class_Basis>`     | :ref:`basis<class_Transform3D_property_basis>`   | ``Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`` |
> +-------------------------------+--------------------------------------------------+--------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`origin<class_Transform3D_property_origin>` | ``Vector3(0, 0, 0)``                 |
> +-------------------------------+--------------------------------------------------+--------------------------------------+
>

## Constructors

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`Transform3D<class_Transform3D_constructor_Transform3D>`\ (\ )                                                                                                                                                                 |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`Transform3D<class_Transform3D_constructor_Transform3D>`\ (\ from\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                                   |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`Transform3D<class_Transform3D_constructor_Transform3D>`\ (\ basis\: :ref:`Basis<class_Basis>`, origin\: :ref:`Vector3<class_Vector3>`\ )                                                                                      |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`Transform3D<class_Transform3D_constructor_Transform3D>`\ (\ from\: :ref:`Projection<class_Projection>`\ )                                                                                                                     |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`Transform3D<class_Transform3D_constructor_Transform3D>`\ (\ x_axis\: :ref:`Vector3<class_Vector3>`, y_axis\: :ref:`Vector3<class_Vector3>`, z_axis\: :ref:`Vector3<class_Vector3>`, origin\: :ref:`Vector3<class_Vector3>`\ ) |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`affine_inverse<class_Transform3D_method_affine_inverse>`\ (\ ) |const|                                                                                                                                           |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`interpolate_with<class_Transform3D_method_interpolate_with>`\ (\ xform\: :ref:`Transform3D<class_Transform3D>`, weight\: :ref:`float<class_float>`\ ) |const|                                                    |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`inverse<class_Transform3D_method_inverse>`\ (\ ) |const|                                                                                                                                                         |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`is_equal_approx<class_Transform3D_method_is_equal_approx>`\ (\ xform\: :ref:`Transform3D<class_Transform3D>`\ ) |const|                                                                                          |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`is_finite<class_Transform3D_method_is_finite>`\ (\ ) |const|                                                                                                                                                     |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`looking_at<class_Transform3D_method_looking_at>`\ (\ target\: :ref:`Vector3<class_Vector3>`, up\: :ref:`Vector3<class_Vector3>` = Vector3(0, 1, 0), use_model_front\: :ref:`bool<class_bool>` = false\ ) |const| |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`orthonormalized<class_Transform3D_method_orthonormalized>`\ (\ ) |const|                                                                                                                                         |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`rotated<class_Transform3D_method_rotated>`\ (\ axis\: :ref:`Vector3<class_Vector3>`, angle\: :ref:`float<class_float>`\ ) |const|                                                                                |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`rotated_local<class_Transform3D_method_rotated_local>`\ (\ axis\: :ref:`Vector3<class_Vector3>`, angle\: :ref:`float<class_float>`\ ) |const|                                                                    |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`scaled<class_Transform3D_method_scaled>`\ (\ scale\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                                                    |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`scaled_local<class_Transform3D_method_scaled_local>`\ (\ scale\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                                        |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`translated<class_Transform3D_method_translated>`\ (\ offset\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                                           |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`translated_local<class_Transform3D_method_translated_local>`\ (\ offset\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                               |
> +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`operator !=<class_Transform3D_operator_neq_Transform3D>`\ (\ right\: :ref:`Transform3D<class_Transform3D>`\ )                     |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`                             | :ref:`operator *<class_Transform3D_operator_mul_AABB>`\ (\ right\: :ref:`AABB<class_AABB>`\ )                                           |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`operator *<class_Transform3D_operator_mul_PackedVector3Array>`\ (\ right\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ ) |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>`                           | :ref:`operator *<class_Transform3D_operator_mul_Plane>`\ (\ right\: :ref:`Plane<class_Plane>`\ )                                        |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`operator *<class_Transform3D_operator_mul_Transform3D>`\ (\ right\: :ref:`Transform3D<class_Transform3D>`\ )                      |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`operator *<class_Transform3D_operator_mul_Vector3>`\ (\ right\: :ref:`Vector3<class_Vector3>`\ )                                  |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`operator *<class_Transform3D_operator_mul_float>`\ (\ right\: :ref:`float<class_float>`\ )                                        |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`operator *<class_Transform3D_operator_mul_int>`\ (\ right\: :ref:`int<class_int>`\ )                                              |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`operator /<class_Transform3D_operator_div_float>`\ (\ right\: :ref:`float<class_float>`\ )                                        |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`operator /<class_Transform3D_operator_div_int>`\ (\ right\: :ref:`int<class_int>`\ )                                              |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`operator ==<class_Transform3D_operator_eq_Transform3D>`\ (\ right\: :ref:`Transform3D<class_Transform3D>`\ )                      |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**IDENTITY** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_Transform3D_constant_IDENTITY>]

The identity **Transform3D**. This is a transform with no translation, no rotation, and a scale of [Vector3.ONE<class_Vector3_constant_ONE>]. Its [basis<class_Transform3D_property_basis>] is equal to [Basis.IDENTITY<class_Basis_constant_IDENTITY>]. This also means that:

- Its [Basis.x<class_Basis_property_x>] points right ([Vector3.RIGHT<class_Vector3_constant_RIGHT>]);

- Its [Basis.y<class_Basis_property_y>] points up ([Vector3.UP<class_Vector3_constant_UP>]);

- Its [Basis.z<class_Basis_property_z>] points back ([Vector3.BACK<class_Vector3_constant_BACK>]).

::

    var transform = Transform3D.IDENTITY
    var basis = transform.basis
    print("| X | Y | Z | Origin")
    print("| %.f | %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x, transform.origin.x])
    print("| %.f | %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y, transform.origin.y])
    print("| %.f | %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z, transform.origin.z])
    # Prints:
    # | X | Y | Z | Origin
    # | 1 | 0 | 0 | 0
    # | 0 | 1 | 0 | 0
    # | 0 | 0 | 1 | 0

If a [Vector3<class_Vector3>], an [AABB<class_AABB>], a [Plane<class_Plane>], a [PackedVector3Array<class_PackedVector3Array>], or another **Transform3D** is transformed (multiplied) by this constant, no transformation occurs.

\ **Note:** In GDScript, this constant is equivalent to creating a [Transform3D<class_Transform3D_constructor_Transform3D>] without any arguments. It can be used to make your code clearer, and for consistency with C#.



**FLIP_X** = `Transform3D(-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_Transform3D_constant_FLIP_X>]

**Transform3D** with mirroring applied perpendicular to the YZ plane. Its [basis<class_Transform3D_property_basis>] is equal to [Basis.FLIP_X<class_Basis_constant_FLIP_X>].



**FLIP_Y** = `Transform3D(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_Transform3D_constant_FLIP_Y>]

**Transform3D** with mirroring applied perpendicular to the XZ plane. Its [basis<class_Transform3D_property_basis>] is equal to [Basis.FLIP_Y<class_Basis_constant_FLIP_Y>].



**FLIP_Z** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0)` [🔗<class_Transform3D_constant_FLIP_Z>]

**Transform3D** with mirroring applied perpendicular to the XY plane. Its [basis<class_Transform3D_property_basis>] is equal to [Basis.FLIP_Z<class_Basis_constant_FLIP_Z>].


----


## Property Descriptions



[Basis<class_Basis>] **basis** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)` [🔗<class_Transform3D_property_basis>]

The [Basis<class_Basis>] of this transform. It is composed by 3 axes ([Basis.x<class_Basis_property_x>], [Basis.y<class_Basis_property_y>], and [Basis.z<class_Basis_property_z>]). Together, these represent the transform's rotation, scale, and shear.


----



[Vector3<class_Vector3>] **origin** = `Vector3(0, 0, 0)` [🔗<class_Transform3D_property_origin>]

The translation offset of this transform. In 3D space, this can be seen as the position.


----


## Constructor Descriptions



[Transform3D<class_Transform3D>] **Transform3D**\ (\ ) [🔗<class_Transform3D_constructor_Transform3D>]

Constructs a **Transform3D** identical to [IDENTITY<class_Transform3D_constant_IDENTITY>].

\ **Note:** In C#, this constructs a **Transform3D** with its [origin<class_Transform3D_property_origin>] and the components of its [basis<class_Transform3D_property_basis>] set to [Vector3.ZERO<class_Vector3_constant_ZERO>].


----


[Transform3D<class_Transform3D>] **Transform3D**\ (\ from\: [Transform3D<class_Transform3D>]\ )

Constructs a **Transform3D** as a copy of the given **Transform3D**.


----


[Transform3D<class_Transform3D>] **Transform3D**\ (\ basis\: [Basis<class_Basis>], origin\: [Vector3<class_Vector3>]\ )

Constructs a **Transform3D** from a [Basis<class_Basis>] and [Vector3<class_Vector3>].


----


[Transform3D<class_Transform3D>] **Transform3D**\ (\ from\: [Projection<class_Projection>]\ )

Constructs a **Transform3D** from a [Projection<class_Projection>]. Because **Transform3D** is a 3×4 matrix and [Projection<class_Projection>] is a 4×4 matrix, this operation trims the last row of the projection matrix (`from.x.w`, `from.y.w`, `from.z.w`, and `from.w.w` are not included in the new transform).


----


[Transform3D<class_Transform3D>] **Transform3D**\ (\ x_axis\: [Vector3<class_Vector3>], y_axis\: [Vector3<class_Vector3>], z_axis\: [Vector3<class_Vector3>], origin\: [Vector3<class_Vector3>]\ )

Constructs a **Transform3D** from four [Vector3<class_Vector3>] values (also called matrix columns).

The first three arguments are the [basis<class_Transform3D_property_basis>]'s axes ([Basis.x<class_Basis_property_x>], [Basis.y<class_Basis_property_y>], and [Basis.z<class_Basis_property_z>]).


----


## Method Descriptions



[Transform3D<class_Transform3D>] **affine_inverse**\ (\ ) |const| [🔗<class_Transform3D_method_affine_inverse>]

Returns the inverted version of this transform. Unlike [inverse()<class_Transform3D_method_inverse>], this method works with almost any [basis<class_Transform3D_property_basis>], including non-uniform ones, but is slower. See also [Basis.inverse()<class_Basis_method_inverse>].

\ **Note:** For this method to return correctly, the transform's [basis<class_Transform3D_property_basis>] needs to have a determinant that is not exactly `0.0` (see [Basis.determinant()<class_Basis_method_determinant>]).


----



[Transform3D<class_Transform3D>] **interpolate_with**\ (\ xform\: [Transform3D<class_Transform3D>], weight\: [float<class_float>]\ ) |const| [🔗<class_Transform3D_method_interpolate_with>]

Returns the result of the linear interpolation between this transform and `xform` by the given `weight`.

The `weight` should be between `0.0` and `1.0` (inclusive). Values outside this range are allowed and can be used to perform *extrapolation* instead.


----



[Transform3D<class_Transform3D>] **inverse**\ (\ ) |const| [🔗<class_Transform3D_method_inverse>]

Returns the [inverted version of this transform ](https://en.wikipedia.org/wiki/Invertible_matrix)_. See also [Basis.inverse()<class_Basis_method_inverse>].

\ **Note:** For this method to return correctly, the transform's [basis<class_Transform3D_property_basis>] needs to be *orthonormal* (see [orthonormalized()<class_Transform3D_method_orthonormalized>]). That means the basis should only represent a rotation. If it does not, use [affine_inverse()<class_Transform3D_method_affine_inverse>] instead.


----



[bool<class_bool>] **is_equal_approx**\ (\ xform\: [Transform3D<class_Transform3D>]\ ) |const| [🔗<class_Transform3D_method_is_equal_approx>]

Returns `true` if this transform and `xform` are approximately equal, by running [@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>] on each component.


----



[bool<class_bool>] **is_finite**\ (\ ) |const| [🔗<class_Transform3D_method_is_finite>]

Returns `true` if this transform is finite, by calling [@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>] on each component.


----



[Transform3D<class_Transform3D>] **looking_at**\ (\ target\: [Vector3<class_Vector3>], up\: [Vector3<class_Vector3>] = Vector3(0, 1, 0), use_model_front\: [bool<class_bool>] = false\ ) |const| [🔗<class_Transform3D_method_looking_at>]

Returns a copy of this transform rotated so that the forward axis (-Z) points towards the `target` position.

The up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the forward axis. The resulting transform is orthonormalized. The existing rotation, scale, and skew information from the original transform is discarded. The `target` and `up` vectors cannot be zero, cannot be parallel to each other, and are defined in global/parent space.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position. By default, the -Z axis (camera forward) is treated as forward (implies +X is right).


----



[Transform3D<class_Transform3D>] **orthonormalized**\ (\ ) |const| [🔗<class_Transform3D_method_orthonormalized>]

Returns a copy of this transform with its [basis<class_Transform3D_property_basis>] orthonormalized. An orthonormal basis is both *orthogonal* (the axes are perpendicular to each other) and *normalized* (the axes have a length of `1.0`), which also means it can only represent a rotation. See also [Basis.orthonormalized()<class_Basis_method_orthonormalized>].


----



[Transform3D<class_Transform3D>] **rotated**\ (\ axis\: [Vector3<class_Vector3>], angle\: [float<class_float>]\ ) |const| [🔗<class_Transform3D_method_rotated>]

Returns a copy of this transform rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector (see [Vector3.normalized()<class_Vector3_method_normalized>]). If `angle` is positive, the basis is rotated counter-clockwise around the axis.

This method is an optimized version of multiplying the given transform `X` with a corresponding rotation transform `R` from the left, i.e., `R * X`.

This can be seen as transforming with respect to the global/parent frame.


----



[Transform3D<class_Transform3D>] **rotated_local**\ (\ axis\: [Vector3<class_Vector3>], angle\: [float<class_float>]\ ) |const| [🔗<class_Transform3D_method_rotated_local>]

Returns a copy of this transform rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector in the transform's local coordinate system. For example, to rotate around the local X-axis, use [Vector3.RIGHT<class_Vector3_constant_RIGHT>].

This method is an optimized version of multiplying the given transform `X` with a corresponding rotation transform `R` from the right, i.e., `X * R`.

This can be seen as transforming with respect to the local frame.


----



[Transform3D<class_Transform3D>] **scaled**\ (\ scale\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Transform3D_method_scaled>]

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform `X` with a corresponding scaling transform `S` from the left, i.e., `S * X`.

This can be seen as transforming with respect to the global/parent frame.


----



[Transform3D<class_Transform3D>] **scaled_local**\ (\ scale\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Transform3D_method_scaled_local>]

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform `X` with a corresponding scaling transform `S` from the right, i.e., `X * S`.

This can be seen as transforming with respect to the local frame.


----



[Transform3D<class_Transform3D>] **translated**\ (\ offset\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Transform3D_method_translated>]

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform `X` with a corresponding translation transform `T` from the left, i.e., `T * X`.

This can be seen as transforming with respect to the global/parent frame.


----



[Transform3D<class_Transform3D>] **translated_local**\ (\ offset\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Transform3D_method_translated_local>]

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform `X` with a corresponding translation transform `T` from the right, i.e., `X * T`.

This can be seen as transforming with respect to the local frame.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Transform3D_operator_neq_Transform3D>]

Returns `true` if the components of both transforms are not equal.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_Transform3D_method_is_equal_approx>] instead, which is more reliable.


----



[AABB<class_AABB>] **operator ***\ (\ right\: [AABB<class_AABB>]\ ) [🔗<class_Transform3D_operator_mul_AABB>]

Transforms (multiplies) the [AABB<class_AABB>] by this transformation matrix.


----



[PackedVector3Array<class_PackedVector3Array>] **operator ***\ (\ right\: [PackedVector3Array<class_PackedVector3Array>]\ ) [🔗<class_Transform3D_operator_mul_PackedVector3Array>]

Transforms (multiplies) every [Vector3<class_Vector3>] element of the given [PackedVector3Array<class_PackedVector3Array>] by this transformation matrix.

On larger arrays, this operation is much faster than transforming each [Vector3<class_Vector3>] individually.


----



[Plane<class_Plane>] **operator ***\ (\ right\: [Plane<class_Plane>]\ ) [🔗<class_Transform3D_operator_mul_Plane>]

Transforms (multiplies) the [Plane<class_Plane>] by this transformation matrix.


----



[Transform3D<class_Transform3D>] **operator ***\ (\ right\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Transform3D_operator_mul_Transform3D>]

Transforms (multiplies) this transform by the `right` transform.

This is the operation performed between parent and child [Node3D<class_Node3D>]\ s.

\ **Note:** If you need to only modify one attribute of this transform, consider using one of the following methods, instead:

- For translation, see [translated()<class_Transform3D_method_translated>] or [translated_local()<class_Transform3D_method_translated_local>].

- For rotation, see [rotated()<class_Transform3D_method_rotated>] or [rotated_local()<class_Transform3D_method_rotated_local>].

- For scale, see [scaled()<class_Transform3D_method_scaled>] or [scaled_local()<class_Transform3D_method_scaled_local>].


----



[Vector3<class_Vector3>] **operator ***\ (\ right\: [Vector3<class_Vector3>]\ ) [🔗<class_Transform3D_operator_mul_Vector3>]

Transforms (multiplies) the [Vector3<class_Vector3>] by this transformation matrix.


----



[Transform3D<class_Transform3D>] **operator ***\ (\ right\: [float<class_float>]\ ) [🔗<class_Transform3D_operator_mul_float>]

Multiplies all components of the **Transform3D** by the given [float<class_float>], including the [origin<class_Transform3D_property_origin>]. This affects the transform's scale uniformly, scaling the [basis<class_Transform3D_property_basis>].


----



[Transform3D<class_Transform3D>] **operator ***\ (\ right\: [int<class_int>]\ ) [🔗<class_Transform3D_operator_mul_int>]

Multiplies all components of the **Transform3D** by the given [int<class_int>], including the [origin<class_Transform3D_property_origin>]. This affects the transform's scale uniformly, scaling the [basis<class_Transform3D_property_basis>].


----



[Transform3D<class_Transform3D>] **operator /**\ (\ right\: [float<class_float>]\ ) [🔗<class_Transform3D_operator_div_float>]

Divides all components of the **Transform3D** by the given [float<class_float>], including the [origin<class_Transform3D_property_origin>]. This affects the transform's scale uniformly, scaling the [basis<class_Transform3D_property_basis>].


----



[Transform3D<class_Transform3D>] **operator /**\ (\ right\: [int<class_int>]\ ) [🔗<class_Transform3D_operator_div_int>]

Divides all components of the **Transform3D** by the given [int<class_int>], including the [origin<class_Transform3D_property_origin>]. This affects the transform's scale uniformly, scaling the [basis<class_Transform3D_property_basis>].


----



[bool<class_bool>] **operator ==**\ (\ right\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Transform3D_operator_eq_Transform3D>]

Returns `true` if the components of both transforms are exactly equal.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_Transform3D_method_is_equal_approx>] instead, which is more reliable.

