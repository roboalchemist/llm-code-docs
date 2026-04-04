:github_url: hide



# Plane

A plane in Hessian normal form.


## Description

Represents a normalized plane equation. [normal<class_Plane_property_normal>] is the normal of the plane (a, b, c normalized), and [d<class_Plane_property_d>] is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.


## Tutorials

- [../tutorials/math/index](Math documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------+----------------------+
> | :ref:`float<class_float>`     | :ref:`d<class_Plane_property_d>`           | ``0.0``              |
> +-------------------------------+--------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`normal<class_Plane_property_normal>` | ``Vector3(0, 0, 0)`` |
> +-------------------------------+--------------------------------------------+----------------------+
> | :ref:`float<class_float>`     | :ref:`x<class_Plane_property_x>`           | ``0.0``              |
> +-------------------------------+--------------------------------------------+----------------------+
> | :ref:`float<class_float>`     | :ref:`y<class_Plane_property_y>`           | ``0.0``              |
> +-------------------------------+--------------------------------------------+----------------------+
> | :ref:`float<class_float>`     | :ref:`z<class_Plane_property_z>`           | ``0.0``              |
> +-------------------------------+--------------------------------------------+----------------------+
>

## Constructors

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ )                                                                                                                             |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ from\: :ref:`Plane<class_Plane>`\ )                                                                                           |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ a\: :ref:`float<class_float>`, b\: :ref:`float<class_float>`, c\: :ref:`float<class_float>`, d\: :ref:`float<class_float>`\ ) |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ normal\: :ref:`Vector3<class_Vector3>`\ )                                                                                     |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ normal\: :ref:`Vector3<class_Vector3>`, d\: :ref:`float<class_float>`\ )                                                      |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ normal\: :ref:`Vector3<class_Vector3>`, point\: :ref:`Vector3<class_Vector3>`\ )                                              |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`Plane<class_Plane_constructor_Plane>`\ (\ point1\: :ref:`Vector3<class_Vector3>`, point2\: :ref:`Vector3<class_Vector3>`, point3\: :ref:`Vector3<class_Vector3>`\ )     |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`distance_to<class_Plane_method_distance_to>`\ (\ point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                  |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_center<class_Plane_method_get_center>`\ (\ ) |const|                                                                                           |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_point<class_Plane_method_has_point>`\ (\ point\: :ref:`Vector3<class_Vector3>`, tolerance\: :ref:`float<class_float>` = 1e-05\ ) |const|       |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`intersect_3<class_Plane_method_intersect_3>`\ (\ b\: :ref:`Plane<class_Plane>`, c\: :ref:`Plane<class_Plane>`\ ) |const|                           |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`intersects_ray<class_Plane_method_intersects_ray>`\ (\ from\: :ref:`Vector3<class_Vector3>`, dir\: :ref:`Vector3<class_Vector3>`\ ) |const|        |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`intersects_segment<class_Plane_method_intersects_segment>`\ (\ from\: :ref:`Vector3<class_Vector3>`, to\: :ref:`Vector3<class_Vector3>`\ ) |const| |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_equal_approx<class_Plane_method_is_equal_approx>`\ (\ to_plane\: :ref:`Plane<class_Plane>`\ ) |const|                                           |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_finite<class_Plane_method_is_finite>`\ (\ ) |const|                                                                                             |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_point_over<class_Plane_method_is_point_over>`\ (\ point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                              |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>`     | :ref:`normalized<class_Plane_method_normalized>`\ (\ ) |const|                                                                                           |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`project<class_Plane_method_project>`\ (\ point\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                          |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`operator !=<class_Plane_operator_neq_Plane>`\ (\ right\: :ref:`Plane<class_Plane>`\ )                  |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`operator *<class_Plane_operator_mul_Transform3D>`\ (\ right\: :ref:`Transform3D<class_Transform3D>`\ ) |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`operator ==<class_Plane_operator_eq_Plane>`\ (\ right\: :ref:`Plane<class_Plane>`\ )                   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`operator unary+<class_Plane_operator_unplus>`\ (\ )                                                    |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>` | :ref:`operator unary-<class_Plane_operator_unminus>`\ (\ )                                                   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**PLANE_YZ** = `Plane(1, 0, 0, 0)` [🔗<class_Plane_constant_PLANE_YZ>]

A plane that extends in the Y and Z axes (normal vector points +X).



**PLANE_XZ** = `Plane(0, 1, 0, 0)` [🔗<class_Plane_constant_PLANE_XZ>]

A plane that extends in the X and Z axes (normal vector points +Y).



**PLANE_XY** = `Plane(0, 0, 1, 0)` [🔗<class_Plane_constant_PLANE_XY>]

A plane that extends in the X and Y axes (normal vector points +Z).


----


## Property Descriptions



[float<class_float>] **d** = `0.0` [🔗<class_Plane_property_d>]

The distance from the origin to the plane, expressed in terms of [normal<class_Plane_property_normal>] (according to its direction and magnitude). Actual absolute distance from the origin to the plane can be calculated as `abs(d) / normal.length()` (if [normal<class_Plane_property_normal>] has zero length then this **Plane** does not represent a valid plane).

In the scalar equation of the plane `ax + by + cz = d`, this is `d`, while the `(a, b, c)` coordinates are represented by the [normal<class_Plane_property_normal>] property.


----



[Vector3<class_Vector3>] **normal** = `Vector3(0, 0, 0)` [🔗<class_Plane_property_normal>]

The normal of the plane, typically a unit vector. Shouldn't be a zero vector as **Plane** with such [normal<class_Plane_property_normal>] does not represent a valid plane.

In the scalar equation of the plane `ax + by + cz = d`, this is the vector `(a, b, c)`, where `d` is the [d<class_Plane_property_d>] property.


----



[float<class_float>] **x** = `0.0` [🔗<class_Plane_property_x>]

The X component of the plane's [normal<class_Plane_property_normal>] vector.


----



[float<class_float>] **y** = `0.0` [🔗<class_Plane_property_y>]

The Y component of the plane's [normal<class_Plane_property_normal>] vector.


----



[float<class_float>] **z** = `0.0` [🔗<class_Plane_property_z>]

The Z component of the plane's [normal<class_Plane_property_normal>] vector.


----


## Constructor Descriptions



[Plane<class_Plane>] **Plane**\ (\ ) [🔗<class_Plane_constructor_Plane>]

Constructs a default-initialized **Plane** with all components set to `0`.


----


[Plane<class_Plane>] **Plane**\ (\ from\: [Plane<class_Plane>]\ )

Constructs a **Plane** as a copy of the given **Plane**.


----


[Plane<class_Plane>] **Plane**\ (\ a\: [float<class_float>], b\: [float<class_float>], c\: [float<class_float>], d\: [float<class_float>]\ )

Creates a plane from the four parameters. The three components of the resulting plane's [normal<class_Plane_property_normal>] are `a`, `b` and `c`, and the plane has a distance of `d` from the origin.


----


[Plane<class_Plane>] **Plane**\ (\ normal\: [Vector3<class_Vector3>]\ )

Creates a plane from the normal vector. The plane will intersect the origin.

The `normal` of the plane must be a unit vector.


----


[Plane<class_Plane>] **Plane**\ (\ normal\: [Vector3<class_Vector3>], d\: [float<class_float>]\ )

Creates a plane from the normal vector and the plane's distance from the origin.

The `normal` of the plane must be a unit vector.


----


[Plane<class_Plane>] **Plane**\ (\ normal\: [Vector3<class_Vector3>], point\: [Vector3<class_Vector3>]\ )

Creates a plane from the normal vector and a point on the plane.

The `normal` of the plane must be a unit vector.


----


[Plane<class_Plane>] **Plane**\ (\ point1\: [Vector3<class_Vector3>], point2\: [Vector3<class_Vector3>], point3\: [Vector3<class_Vector3>]\ )

Creates a plane from the three points, given in clockwise order.


----


## Method Descriptions



[float<class_float>] **distance_to**\ (\ point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Plane_method_distance_to>]

Returns the shortest distance from the plane to the position `point`. If the point is above the plane, the distance will be positive. If below, the distance will be negative.


----



[Vector3<class_Vector3>] **get_center**\ (\ ) |const| [🔗<class_Plane_method_get_center>]

Returns the center of the plane.


----



[bool<class_bool>] **has_point**\ (\ point\: [Vector3<class_Vector3>], tolerance\: [float<class_float>] = 1e-05\ ) |const| [🔗<class_Plane_method_has_point>]

Returns `true` if `point` is inside the plane. Comparison uses a custom minimum `tolerance` threshold.


----



[Variant<class_Variant>] **intersect_3**\ (\ b\: [Plane<class_Plane>], c\: [Plane<class_Plane>]\ ) |const| [🔗<class_Plane_method_intersect_3>]

Returns the intersection point of the three planes `b`, `c` and this plane. If no intersection is found, `null` is returned.


----



[Variant<class_Variant>] **intersects_ray**\ (\ from\: [Vector3<class_Vector3>], dir\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Plane_method_intersects_ray>]

Returns the intersection point of a ray consisting of the position `from` and the direction normal `dir` with this plane. If no intersection is found, `null` is returned.


----



[Variant<class_Variant>] **intersects_segment**\ (\ from\: [Vector3<class_Vector3>], to\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Plane_method_intersects_segment>]

Returns the intersection point of a segment from position `from` to position `to` with this plane. If no intersection is found, `null` is returned.


----



[bool<class_bool>] **is_equal_approx**\ (\ to_plane\: [Plane<class_Plane>]\ ) |const| [🔗<class_Plane_method_is_equal_approx>]

Returns `true` if this plane and `to_plane` are approximately equal, by running [@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>] on each component.


----



[bool<class_bool>] **is_finite**\ (\ ) |const| [🔗<class_Plane_method_is_finite>]

Returns `true` if this plane is finite, by calling [@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>] on each component.


----



[bool<class_bool>] **is_point_over**\ (\ point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Plane_method_is_point_over>]

Returns `true` if `point` is located above the plane.


----



[Plane<class_Plane>] **normalized**\ (\ ) |const| [🔗<class_Plane_method_normalized>]

Returns a copy of the plane, with normalized [normal<class_Plane_property_normal>] (so it's a unit vector). Returns `Plane(0, 0, 0, 0)` if [normal<class_Plane_property_normal>] can't be normalized (it has zero length).


----



[Vector3<class_Vector3>] **project**\ (\ point\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Plane_method_project>]

Returns the orthogonal projection of `point` into a point in the plane.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [Plane<class_Plane>]\ ) [🔗<class_Plane_operator_neq_Plane>]

Returns `true` if the planes are not equal.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_Plane_method_is_equal_approx>] instead, which is more reliable.


----



[Plane<class_Plane>] **operator ***\ (\ right\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Plane_operator_mul_Transform3D>]

Inversely transforms (multiplies) the **Plane** by the given [Transform3D<class_Transform3D>] transformation matrix.

\ `plane * transform` is equivalent to `transform.affine_inverse() * plane`. See [Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>].


----



[bool<class_bool>] **operator ==**\ (\ right\: [Plane<class_Plane>]\ ) [🔗<class_Plane_operator_eq_Plane>]

Returns `true` if the planes are exactly equal.

\ **Note:** Due to floating-point precision errors, consider using [is_equal_approx()<class_Plane_method_is_equal_approx>] instead, which is more reliable.


----



[Plane<class_Plane>] **operator unary+**\ (\ ) [🔗<class_Plane_operator_unplus>]

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.


----



[Plane<class_Plane>] **operator unary-**\ (\ ) [🔗<class_Plane_operator_unminus>]

Returns the negative value of the **Plane**. This is the same as writing `Plane(-p.normal, -p.d)`. This operation flips the direction of the normal vector and also flips the distance value, resulting in a Plane that is in the same place, but facing the opposite direction.

