:github_url: hide



# VisualShaderNodeCubemap

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [Cubemap<class_Cubemap>] sampling node to be used within the visual shader graph.


## Description

Translated to `texture(cubemap, vec3)` in the shader language. Returns a color vector and alpha channel as scalar.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-------+
> | :ref:`TextureLayered<class_TextureLayered>`                  | :ref:`cube_map<class_VisualShaderNodeCubemap_property_cube_map>`         |       |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-------+
> | :ref:`Source<enum_VisualShaderNodeCubemap_Source>`           | :ref:`source<class_VisualShaderNodeCubemap_property_source>`             | ``0`` |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-------+
> | :ref:`TextureType<enum_VisualShaderNodeCubemap_TextureType>` | :ref:`texture_type<class_VisualShaderNodeCubemap_property_texture_type>` | ``0`` |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Source**: [🔗<enum_VisualShaderNodeCubemap_Source>]



[Source<enum_VisualShaderNodeCubemap_Source>] **SOURCE_TEXTURE** = `0`

Use the [Cubemap<class_Cubemap>] set via [cube_map<class_VisualShaderNodeCubemap_property_cube_map>]. If this is set to [source<class_VisualShaderNodeCubemap_property_source>], the `samplerCube` port is ignored.



[Source<enum_VisualShaderNodeCubemap_Source>] **SOURCE_PORT** = `1`

Use the [Cubemap<class_Cubemap>] sampler reference passed via the `samplerCube` port. If this is set to [source<class_VisualShaderNodeCubemap_property_source>], the [cube_map<class_VisualShaderNodeCubemap_property_cube_map>] texture is ignored.



[Source<enum_VisualShaderNodeCubemap_Source>] **SOURCE_MAX** = `2`

Represents the size of the [Source<enum_VisualShaderNodeCubemap_Source>] enum.


----



enum **TextureType**: [🔗<enum_VisualShaderNodeCubemap_TextureType>]



[TextureType<enum_VisualShaderNodeCubemap_TextureType>] **TYPE_DATA** = `0`

No hints are added to the uniform declaration.



[TextureType<enum_VisualShaderNodeCubemap_TextureType>] **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.



[TextureType<enum_VisualShaderNodeCubemap_TextureType>] **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.



[TextureType<enum_VisualShaderNodeCubemap_TextureType>] **TYPE_MAX** = `3`

Represents the size of the [TextureType<enum_VisualShaderNodeCubemap_TextureType>] enum.


----


## Property Descriptions



[TextureLayered<class_TextureLayered>] **cube_map** [🔗<class_VisualShaderNodeCubemap_property_cube_map>]


- |void| **set_cube_map**\ (\ value\: [TextureLayered<class_TextureLayered>]\ )
- [TextureLayered<class_TextureLayered>] **get_cube_map**\ (\ )

The [Cubemap<class_Cubemap>] texture to sample when using [SOURCE_TEXTURE<class_VisualShaderNodeCubemap_constant_SOURCE_TEXTURE>] as [source<class_VisualShaderNodeCubemap_property_source>].


----



[Source<enum_VisualShaderNodeCubemap_Source>] **source** = `0` [🔗<class_VisualShaderNodeCubemap_property_source>]


- |void| **set_source**\ (\ value\: [Source<enum_VisualShaderNodeCubemap_Source>]\ )
- [Source<enum_VisualShaderNodeCubemap_Source>] **get_source**\ (\ )

Defines which source should be used for the sampling.


----



[TextureType<enum_VisualShaderNodeCubemap_TextureType>] **texture_type** = `0` [🔗<class_VisualShaderNodeCubemap_property_texture_type>]


- |void| **set_texture_type**\ (\ value\: [TextureType<enum_VisualShaderNodeCubemap_TextureType>]\ )
- [TextureType<enum_VisualShaderNodeCubemap_TextureType>] **get_texture_type**\ (\ )

Defines the type of data provided by the source texture.

