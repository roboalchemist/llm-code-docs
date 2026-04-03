:github_url: hide



# VisualShaderNodeTexture3D

**Inherits:** [VisualShaderNodeSample3D<class_VisualShaderNodeSample3D>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Performs a 3D texture lookup within the visual shader graph.


## Description

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------+
> | :ref:`Texture3D<class_Texture3D>` | :ref:`texture<class_VisualShaderNodeTexture3D_property_texture>` |
> +-----------------------------------+------------------------------------------------------------------+
>

----


## Property Descriptions



[Texture3D<class_Texture3D>] **texture** [🔗<class_VisualShaderNodeTexture3D_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture3D<class_Texture3D>]\ )
- [Texture3D<class_Texture3D>] **get_texture**\ (\ )

A source texture. Used if [VisualShaderNodeSample3D.source<class_VisualShaderNodeSample3D_property_source>] is set to [VisualShaderNodeSample3D.SOURCE_TEXTURE<class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE>].

