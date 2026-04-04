:github_url: hide



# PhysicsDirectSpaceState3DExtension

**Inherits:** [PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] **<** [Object<class_Object>]

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] implementations.


## Description

This class extends [PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`_cast_motion<class_PhysicsDirectSpaceState3DExtension_private_method__cast_motion>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform3D<class_Transform3D>`, motion\: :ref:`Vector3<class_Vector3>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, closest_safe\: ``float*``, closest_unsafe\: ``float*``, info\: ``PhysicsServer3DExtensionShapeRestInfo*``\ ) |virtual| |required| |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`_collide_shape<class_PhysicsDirectSpaceState3DExtension_private_method__collide_shape>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform3D<class_Transform3D>`, motion\: :ref:`Vector3<class_Vector3>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, results\: ``void*``, max_results\: :ref:`int<class_int>`, result_count\: ``int32_t*``\ ) |virtual| |required|                 |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`_get_closest_point_to_object_volume<class_PhysicsDirectSpaceState3DExtension_private_method__get_closest_point_to_object_volume>`\ (\ object\: :ref:`RID<class_RID>`, point\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required| |const|                                                                                                                                                                                                                                                                                      |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`_intersect_point<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_point>`\ (\ position\: :ref:`Vector3<class_Vector3>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, results\: ``PhysicsServer3DExtensionShapeResult*``, max_results\: :ref:`int<class_int>`\ ) |virtual| |required|                                                                                                                                   |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`_intersect_ray<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_ray>`\ (\ from\: :ref:`Vector3<class_Vector3>`, to\: :ref:`Vector3<class_Vector3>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, hit_from_inside\: :ref:`bool<class_bool>`, hit_back_faces\: :ref:`bool<class_bool>`, pick_ray\: :ref:`bool<class_bool>`, result\: ``PhysicsServer3DExtensionRayResult*``\ ) |virtual| |required|                      |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`_intersect_shape<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_shape>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform3D<class_Transform3D>`, motion\: :ref:`Vector3<class_Vector3>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, result_count\: ``PhysicsServer3DExtensionShapeResult*``, max_results\: :ref:`int<class_int>`\ ) |virtual| |required|      |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`_rest_info<class_PhysicsDirectSpaceState3DExtension_private_method__rest_info>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform3D<class_Transform3D>`, motion\: :ref:`Vector3<class_Vector3>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, rest_info\: ``PhysicsServer3DExtensionShapeRestInfo*``\ ) |virtual| |required|                                                        |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_body_excluded_from_query<class_PhysicsDirectSpaceState3DExtension_method_is_body_excluded_from_query>`\ (\ body\: :ref:`RID<class_RID>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                            |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **_cast_motion**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform3D<class_Transform3D>], motion\: [Vector3<class_Vector3>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], closest_safe\: `float*`, closest_unsafe\: `float*`, info\: `PhysicsServer3DExtensionShapeRestInfo*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__cast_motion>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_collide_shape**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform3D<class_Transform3D>], motion\: [Vector3<class_Vector3>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], results\: `void*`, max_results\: [int<class_int>], result_count\: `int32_t*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__collide_shape>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_closest_point_to_object_volume**\ (\ object\: [RID<class_RID>], point\: [Vector3<class_Vector3>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__get_closest_point_to_object_volume>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_intersect_point**\ (\ position\: [Vector3<class_Vector3>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], results\: `PhysicsServer3DExtensionShapeResult*`, max_results\: [int<class_int>]\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_point>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_intersect_ray**\ (\ from\: [Vector3<class_Vector3>], to\: [Vector3<class_Vector3>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], hit_from_inside\: [bool<class_bool>], hit_back_faces\: [bool<class_bool>], pick_ray\: [bool<class_bool>], result\: `PhysicsServer3DExtensionRayResult*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_ray>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_intersect_shape**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform3D<class_Transform3D>], motion\: [Vector3<class_Vector3>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], result_count\: `PhysicsServer3DExtensionShapeResult*`, max_results\: [int<class_int>]\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_shape>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_rest_info**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform3D<class_Transform3D>], motion\: [Vector3<class_Vector3>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], rest_info\: `PhysicsServer3DExtensionShapeRestInfo*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState3DExtension_private_method__rest_info>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **is_body_excluded_from_query**\ (\ body\: [RID<class_RID>]\ ) |const| [🔗<class_PhysicsDirectSpaceState3DExtension_method_is_body_excluded_from_query>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

