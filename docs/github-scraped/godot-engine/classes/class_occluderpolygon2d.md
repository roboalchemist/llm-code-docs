:github_url: hide



# OccluderPolygon2D

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Defines a 2D polygon for LightOccluder2D.


## Description

Editor facility that helps you draw a 2D polygon used as resource for [LightOccluder2D<class_LightOccluder2D>].


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+--------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`closed<class_OccluderPolygon2D_property_closed>`       | ``true``                 |
> +-----------------------------------------------------+--------------------------------------------------------------+--------------------------+
> | :ref:`CullMode<enum_OccluderPolygon2D_CullMode>`    | :ref:`cull_mode<class_OccluderPolygon2D_property_cull_mode>` | ``0``                    |
> +-----------------------------------------------------+--------------------------------------------------------------+--------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`polygon<class_OccluderPolygon2D_property_polygon>`     | ``PackedVector2Array()`` |
> +-----------------------------------------------------+--------------------------------------------------------------+--------------------------+
>

----


## Enumerations



enum **CullMode**: [🔗<enum_OccluderPolygon2D_CullMode>]



[CullMode<enum_OccluderPolygon2D_CullMode>] **CULL_DISABLED** = `0`

Culling is disabled. See [cull_mode<class_OccluderPolygon2D_property_cull_mode>].



[CullMode<enum_OccluderPolygon2D_CullMode>] **CULL_CLOCKWISE** = `1`

Culling is performed in the clockwise direction. See [cull_mode<class_OccluderPolygon2D_property_cull_mode>].



[CullMode<enum_OccluderPolygon2D_CullMode>] **CULL_COUNTER_CLOCKWISE** = `2`

Culling is performed in the counterclockwise direction. See [cull_mode<class_OccluderPolygon2D_property_cull_mode>].


----


## Property Descriptions



[bool<class_bool>] **closed** = `true` [🔗<class_OccluderPolygon2D_property_closed>]


- |void| **set_closed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_closed**\ (\ )

If `true`, closes the polygon. A closed OccluderPolygon2D occludes the light coming from any direction. An opened OccluderPolygon2D occludes the light only at its outline's direction.


----



[CullMode<enum_OccluderPolygon2D_CullMode>] **cull_mode** = `0` [🔗<class_OccluderPolygon2D_property_cull_mode>]


- |void| **set_cull_mode**\ (\ value\: [CullMode<enum_OccluderPolygon2D_CullMode>]\ )
- [CullMode<enum_OccluderPolygon2D_CullMode>] **get_cull_mode**\ (\ )

The culling mode to use.


----



[PackedVector2Array<class_PackedVector2Array>] **polygon** = `PackedVector2Array()` [🔗<class_OccluderPolygon2D_property_polygon>]


- |void| **set_polygon**\ (\ value\: [PackedVector2Array<class_PackedVector2Array>]\ )
- [PackedVector2Array<class_PackedVector2Array>] **get_polygon**\ (\ )

A [Vector2<class_Vector2>] array with the index for polygon's vertices positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array<class_PackedVector2Array>] for more details.

