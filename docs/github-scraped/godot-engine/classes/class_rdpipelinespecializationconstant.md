:github_url: hide



# RDPipelineSpecializationConstant

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Pipeline specialization constant (used by [RenderingDevice<class_RenderingDevice>]).


## Description

A *specialization constant* is a way to create additional variants of shaders without actually increasing the number of shader versions that are compiled. This allows improving performance by reducing the number of shader versions and reducing `if` branching, while still allowing shaders to be flexible for different use cases.

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>`         | :ref:`constant_id<class_RDPipelineSpecializationConstant_property_constant_id>` | ``0`` |
> +-------------------------------+---------------------------------------------------------------------------------+-------+
> | :ref:`Variant<class_Variant>` | :ref:`value<class_RDPipelineSpecializationConstant_property_value>`             |       |
> +-------------------------------+---------------------------------------------------------------------------------+-------+
>

----


## Property Descriptions



[int<class_int>] **constant_id** = `0` [🔗<class_RDPipelineSpecializationConstant_property_constant_id>]


- |void| **set_constant_id**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_constant_id**\ (\ )

The identifier of the specialization constant. This is a value starting from `0` and that increments for every different specialization constant for a given shader.


----



[Variant<class_Variant>] **value** [🔗<class_RDPipelineSpecializationConstant_property_value>]


- |void| **set_value**\ (\ value\: [Variant<class_Variant>]\ )
- [Variant<class_Variant>] **get_value**\ (\ )

The specialization constant's value. Only [bool<class_bool>], [int<class_int>] and [float<class_float>] types are valid for specialization constants.

