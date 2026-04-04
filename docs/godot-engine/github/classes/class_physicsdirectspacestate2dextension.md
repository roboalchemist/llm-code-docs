:github_url: hide



# PhysicsDirectSpaceState2DExtension

**Inherits:** [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>] **<** [Object<class_Object>]

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>] implementations.


## Description

This class extends [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>] by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_cast_motion<class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform2D<class_Transform2D>`, motion\: :ref:`Vector2<class_Vector2>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, closest_safe\: ``float*``, closest_unsafe\: ``float*``\ ) |virtual| |required|                                         |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_collide_shape<class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform2D<class_Transform2D>`, motion\: :ref:`Vector2<class_Vector2>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, results\: ``void*``, max_results\: :ref:`int<class_int>`, result_count\: ``int32_t*``\ ) |virtual| |required|      |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`_intersect_point<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point>`\ (\ position\: :ref:`Vector2<class_Vector2>`, canvas_instance_id\: :ref:`int<class_int>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, results\: ``PhysicsServer2DExtensionShapeResult*``, max_results\: :ref:`int<class_int>`\ ) |virtual| |required|                                                                            |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_intersect_ray<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray>`\ (\ from\: :ref:`Vector2<class_Vector2>`, to\: :ref:`Vector2<class_Vector2>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, hit_from_inside\: :ref:`bool<class_bool>`, result\: ``PhysicsServer2DExtensionRayResult*``\ ) |virtual| |required|                                                                                         |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`_intersect_shape<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform2D<class_Transform2D>`, motion\: :ref:`Vector2<class_Vector2>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, result\: ``PhysicsServer2DExtensionShapeResult*``, max_results\: :ref:`int<class_int>`\ ) |virtual| |required| |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_rest_info<class_PhysicsDirectSpaceState2DExtension_private_method__rest_info>`\ (\ shape_rid\: :ref:`RID<class_RID>`, transform\: :ref:`Transform2D<class_Transform2D>`, motion\: :ref:`Vector2<class_Vector2>`, margin\: :ref:`float<class_float>`, collision_mask\: :ref:`int<class_int>`, collide_with_bodies\: :ref:`bool<class_bool>`, collide_with_areas\: :ref:`bool<class_bool>`, rest_info\: ``PhysicsServer2DExtensionShapeRestInfo*``\ ) |virtual| |required|                                             |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_body_excluded_from_query<class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query>`\ (\ body\: :ref:`RID<class_RID>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                 |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **_cast_motion**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform2D<class_Transform2D>], motion\: [Vector2<class_Vector2>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], closest_safe\: `float*`, closest_unsafe\: `float*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_collide_shape**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform2D<class_Transform2D>], motion\: [Vector2<class_Vector2>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], results\: `void*`, max_results\: [int<class_int>], result_count\: `int32_t*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_intersect_point**\ (\ position\: [Vector2<class_Vector2>], canvas_instance_id\: [int<class_int>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], results\: `PhysicsServer2DExtensionShapeResult*`, max_results\: [int<class_int>]\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_intersect_ray**\ (\ from\: [Vector2<class_Vector2>], to\: [Vector2<class_Vector2>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], hit_from_inside\: [bool<class_bool>], result\: `PhysicsServer2DExtensionRayResult*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_intersect_shape**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform2D<class_Transform2D>], motion\: [Vector2<class_Vector2>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], result\: `PhysicsServer2DExtensionShapeResult*`, max_results\: [int<class_int>]\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_rest_info**\ (\ shape_rid\: [RID<class_RID>], transform\: [Transform2D<class_Transform2D>], motion\: [Vector2<class_Vector2>], margin\: [float<class_float>], collision_mask\: [int<class_int>], collide_with_bodies\: [bool<class_bool>], collide_with_areas\: [bool<class_bool>], rest_info\: `PhysicsServer2DExtensionShapeRestInfo*`\ ) |virtual| |required| [🔗<class_PhysicsDirectSpaceState2DExtension_private_method__rest_info>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **is_body_excluded_from_query**\ (\ body\: [RID<class_RID>]\ ) |const| [🔗<class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

