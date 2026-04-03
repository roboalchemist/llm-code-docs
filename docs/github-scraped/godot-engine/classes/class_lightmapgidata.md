:github_url: hide



# LightmapGIData

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Contains baked lightmap and dynamic object probe data for [LightmapGI<class_LightmapGI>].


## Description

**LightmapGIData** contains baked lightmap and dynamic object probe data for [LightmapGI<class_LightmapGI>]. It is replaced every time lightmaps are baked in [LightmapGI<class_LightmapGI>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------+
> | :ref:`TextureLayered<class_TextureLayered>`                              | :ref:`light_texture<class_LightmapGIData_property_light_texture>`             |        |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`\[:ref:`TextureLayered<class_TextureLayered>`\] | :ref:`lightmap_textures<class_LightmapGIData_property_lightmap_textures>`     | ``[]`` |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`\[:ref:`TextureLayered<class_TextureLayered>`\] | :ref:`shadowmask_textures<class_LightmapGIData_property_shadowmask_textures>` | ``[]`` |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_user<class_LightmapGIData_method_add_user>`\ (\ path\: :ref:`NodePath<class_NodePath>`, uv_scale\: :ref:`Rect2<class_Rect2>`, slice_index\: :ref:`int<class_int>`, sub_instance\: :ref:`int<class_int>`\ ) |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`clear_users<class_LightmapGIData_method_clear_users>`\ (\ )                                                                                                                                                    |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_user_count<class_LightmapGIData_method_get_user_count>`\ (\ ) |const|                                                                                                                                      |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`get_user_path<class_LightmapGIData_method_get_user_path>`\ (\ user_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                      |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`is_using_spherical_harmonics<class_LightmapGIData_method_is_using_spherical_harmonics>`\ (\ ) |const|                                                                                                          |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_uses_spherical_harmonics<class_LightmapGIData_method_set_uses_spherical_harmonics>`\ (\ uses_spherical_harmonics\: :ref:`bool<class_bool>`\ )                                                              |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ShadowmaskMode**: [🔗<enum_LightmapGIData_ShadowmaskMode>]



[ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>] **SHADOWMASK_MODE_NONE** = `0`

Shadowmasking is disabled. No shadowmask texture will be created when baking lightmaps. Existing shadowmask textures will be removed during baking.



[ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>] **SHADOWMASK_MODE_REPLACE** = `1`

Shadowmasking is enabled. Directional shadows that are outside the [DirectionalLight3D.directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>] will be rendered using the shadowmask texture. Shadows that are inside the range will be rendered using real-time shadows exclusively. This mode allows for more precise real-time shadows up close, without the potential "smearing" effect that can occur when using lightmaps with a high texel size. The downside is that when the camera moves fast, the transition between the real-time light and shadowmask can be obvious. Also, objects that only have shadows baked in the shadowmask (and no real-time shadows) won't display any shadows up close.



[ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>] **SHADOWMASK_MODE_OVERLAY** = `2`

Shadowmasking is enabled. Directional shadows will be rendered with real-time shadows overlaid on top of the shadowmask texture. This mode makes for smoother shadow transitions when the camera moves fast, at the cost of a potential smearing effect for directional shadows that are up close (due to the real-time shadow being mixed with a low-resolution shadowmask). Objects that only have shadows baked in the shadowmask (and no real-time shadows) will keep their shadows up close.


----


## Property Descriptions



[TextureLayered<class_TextureLayered>] **light_texture** [🔗<class_LightmapGIData_property_light_texture>]


- |void| **set_light_texture**\ (\ value\: [TextureLayered<class_TextureLayered>]\ )
- [TextureLayered<class_TextureLayered>] **get_light_texture**\ (\ )

**Deprecated:** The lightmap atlas can now contain multiple textures. See [lightmap_textures<class_LightmapGIData_property_lightmap_textures>].

The lightmap atlas texture generated by the lightmapper.


----



[Array<class_Array>]\[[TextureLayered<class_TextureLayered>]\] **lightmap_textures** = `[]` [🔗<class_LightmapGIData_property_lightmap_textures>]


- |void| **set_lightmap_textures**\ (\ value\: [Array<class_Array>]\[[TextureLayered<class_TextureLayered>]\]\ )
- [Array<class_Array>]\[[TextureLayered<class_TextureLayered>]\] **get_lightmap_textures**\ (\ )

The lightmap atlas textures generated by the lightmapper.


----



[Array<class_Array>]\[[TextureLayered<class_TextureLayered>]\] **shadowmask_textures** = `[]` [🔗<class_LightmapGIData_property_shadowmask_textures>]


- |void| **set_shadowmask_textures**\ (\ value\: [Array<class_Array>]\[[TextureLayered<class_TextureLayered>]\]\ )
- [Array<class_Array>]\[[TextureLayered<class_TextureLayered>]\] **get_shadowmask_textures**\ (\ )

The shadowmask atlas textures generated by the lightmapper.


----


## Method Descriptions



|void| **add_user**\ (\ path\: [NodePath<class_NodePath>], uv_scale\: [Rect2<class_Rect2>], slice_index\: [int<class_int>], sub_instance\: [int<class_int>]\ ) [🔗<class_LightmapGIData_method_add_user>]

Adds an object that is considered baked within this **LightmapGIData**.


----



|void| **clear_users**\ (\ ) [🔗<class_LightmapGIData_method_clear_users>]

Clear all objects that are considered baked within this **LightmapGIData**.


----



[int<class_int>] **get_user_count**\ (\ ) |const| [🔗<class_LightmapGIData_method_get_user_count>]

Returns the number of objects that are considered baked within this **LightmapGIData**.


----



[NodePath<class_NodePath>] **get_user_path**\ (\ user_idx\: [int<class_int>]\ ) |const| [🔗<class_LightmapGIData_method_get_user_path>]

Returns the [NodePath<class_NodePath>] of the baked object at index `user_idx`.


----



[bool<class_bool>] **is_using_spherical_harmonics**\ (\ ) |const| [🔗<class_LightmapGIData_method_is_using_spherical_harmonics>]

If `true`, lightmaps were baked with directional information. See also [LightmapGI.directional<class_LightmapGI_property_directional>].


----



|void| **set_uses_spherical_harmonics**\ (\ uses_spherical_harmonics\: [bool<class_bool>]\ ) [🔗<class_LightmapGIData_method_set_uses_spherical_harmonics>]

If `uses_spherical_harmonics` is `true`, tells the engine to treat the lightmap data as if it was baked with directional information.

\ **Note:** Changing this value on already baked lightmaps will not cause them to be baked again. This means the material appearance will look incorrect until lightmaps are baked again, in which case the value set here is discarded as the entire **LightmapGIData** resource is replaced by the lightmapper.

