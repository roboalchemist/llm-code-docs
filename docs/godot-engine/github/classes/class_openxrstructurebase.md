:github_url: hide



# OpenXRStructureBase

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRSpatialContextPersistenceConfig<class_OpenXRSpatialContextPersistenceConfig>]

Object for storing OpenXR structure data.


## Description

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+------------------------------------------------------+
> | :ref:`OpenXRStructureBase<class_OpenXRStructureBase>` | :ref:`next<class_OpenXRStructureBase_property_next>` |
> +-------------------------------------------------------+------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`_get_header<class_OpenXRStructureBase_private_method__get_header>`\ (\ next\: :ref:`int<class_int>`\ ) |virtual| |
> +-----------------------+------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`get_structure_type<class_OpenXRStructureBase_method_get_structure_type>`\ (\ )                                   |
> +-----------------------+------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[OpenXRStructureBase<class_OpenXRStructureBase>] **next** [🔗<class_OpenXRStructureBase_property_next>]


- |void| **set_next**\ (\ value\: [OpenXRStructureBase<class_OpenXRStructureBase>]\ )
- [OpenXRStructureBase<class_OpenXRStructureBase>] **get_next**\ (\ )

Setting another structure object here chains these structures together to extend the API functionality. Consult the OpenXR documentation for which structures can be used with a given API call.


----


## Method Descriptions



[int<class_int>] **_get_header**\ (\ next\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRStructureBase_private_method__get_header>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **get_structure_type**\ (\ ) [🔗<class_OpenXRStructureBase_method_get_structure_type>]

Returns the structure type (OpenXR `XrStructureType`) used for this structure.

