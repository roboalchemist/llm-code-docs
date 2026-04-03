:github_url: hide



# RDUniform

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Shader uniform (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------+------------------------------------------------------------+-------+
> | :ref:`int<class_int>`                                | :ref:`binding<class_RDUniform_property_binding>`           | ``0`` |
> +------------------------------------------------------+------------------------------------------------------------+-------+
> | :ref:`UniformType<enum_RenderingDevice_UniformType>` | :ref:`uniform_type<class_RDUniform_property_uniform_type>` | ``3`` |
> +------------------------------------------------------+------------------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+--------------------------------------------------------------------------------+
> | |void|                                             | :ref:`add_id<class_RDUniform_method_add_id>`\ (\ id\: :ref:`RID<class_RID>`\ ) |
> +----------------------------------------------------+--------------------------------------------------------------------------------+
> | |void|                                             | :ref:`clear_ids<class_RDUniform_method_clear_ids>`\ (\ )                       |
> +----------------------------------------------------+--------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\] | :ref:`get_ids<class_RDUniform_method_get_ids>`\ (\ ) |const|                   |
> +----------------------------------------------------+--------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **binding** = `0` [🔗<class_RDUniform_property_binding>]


- |void| **set_binding**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_binding**\ (\ )

The uniform's binding.


----



[UniformType<enum_RenderingDevice_UniformType>] **uniform_type** = `3` [🔗<class_RDUniform_property_uniform_type>]


- |void| **set_uniform_type**\ (\ value\: [UniformType<enum_RenderingDevice_UniformType>]\ )
- [UniformType<enum_RenderingDevice_UniformType>] **get_uniform_type**\ (\ )

The uniform's data type.


----


## Method Descriptions



|void| **add_id**\ (\ id\: [RID<class_RID>]\ ) [🔗<class_RDUniform_method_add_id>]

Binds the given id to the uniform. The data associated with the id is then used when the uniform is passed to a shader.


----



|void| **clear_ids**\ (\ ) [🔗<class_RDUniform_method_clear_ids>]

Unbinds all ids currently bound to the uniform.


----



[Array<class_Array>]\[[RID<class_RID>]\] **get_ids**\ (\ ) |const| [🔗<class_RDUniform_method_get_ids>]

Returns an array of all ids currently bound to the uniform.

