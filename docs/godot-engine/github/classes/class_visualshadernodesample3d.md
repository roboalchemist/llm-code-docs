:github_url: hide



# VisualShaderNodeSample3D

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeTexture2DArray<class_VisualShaderNodeTexture2DArray>], [VisualShaderNodeTexture3D<class_VisualShaderNodeTexture3D>]

A base node for nodes which samples 3D textures in the visual shader graph.


## Description

A virtual class, use the descendants instead.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------+-------+
> | :ref:`Source<enum_VisualShaderNodeSample3D_Source>` | :ref:`source<class_VisualShaderNodeSample3D_property_source>` | ``0`` |
> +-----------------------------------------------------+---------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Source**: [🔗<enum_VisualShaderNodeSample3D_Source>]



[Source<enum_VisualShaderNodeSample3D_Source>] **SOURCE_TEXTURE** = `0`

Creates internal uniform and provides a way to assign it within node.



[Source<enum_VisualShaderNodeSample3D_Source>] **SOURCE_PORT** = `1`

Use the uniform texture from sampler port.



[Source<enum_VisualShaderNodeSample3D_Source>] **SOURCE_MAX** = `2`

Represents the size of the [Source<enum_VisualShaderNodeSample3D_Source>] enum.


----


## Property Descriptions



[Source<enum_VisualShaderNodeSample3D_Source>] **source** = `0` [🔗<class_VisualShaderNodeSample3D_property_source>]


- |void| **set_source**\ (\ value\: [Source<enum_VisualShaderNodeSample3D_Source>]\ )
- [Source<enum_VisualShaderNodeSample3D_Source>] **get_source**\ (\ )

An input source type.

