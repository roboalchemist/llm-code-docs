:github_url: hide



# OpenXRInteractionProfile

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Suggested bindings object for OpenXR.


## Description

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

For more information see the [interaction profiles info in the OpenXR specification ](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles)_.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`   | :ref:`binding_modifiers<class_OpenXRInteractionProfile_property_binding_modifiers>`               | ``[]`` |
> +-----------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`   | :ref:`bindings<class_OpenXRInteractionProfile_property_bindings>`                                 | ``[]`` |
> +-----------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`interaction_profile_path<class_OpenXRInteractionProfile_property_interaction_profile_path>` | ``""`` |
> +-----------------------------+---------------------------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRIPBinding<class_OpenXRIPBinding>`                 | :ref:`get_binding<class_OpenXRInteractionProfile_method_get_binding>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                   |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                         | :ref:`get_binding_count<class_OpenXRInteractionProfile_method_get_binding_count>`\ (\ ) |const|                                      |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>` | :ref:`get_binding_modifier<class_OpenXRInteractionProfile_method_get_binding_modifier>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                         | :ref:`get_binding_modifier_count<class_OpenXRInteractionProfile_method_get_binding_modifier_count>`\ (\ ) |const|                    |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Array<class_Array>] **binding_modifiers** = `[]` [🔗<class_OpenXRInteractionProfile_property_binding_modifiers>]


- |void| **set_binding_modifiers**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_binding_modifiers**\ (\ )

Binding modifiers for this interaction profile.


----



[Array<class_Array>] **bindings** = `[]` [🔗<class_OpenXRInteractionProfile_property_bindings>]


- |void| **set_bindings**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_bindings**\ (\ )

Action bindings for this interaction profile.


----



[String<class_String>] **interaction_profile_path** = `""` [🔗<class_OpenXRInteractionProfile_property_interaction_profile_path>]


- |void| **set_interaction_profile_path**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_interaction_profile_path**\ (\ )

The interaction profile path identifying the XR device.


----


## Method Descriptions



[OpenXRIPBinding<class_OpenXRIPBinding>] **get_binding**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRInteractionProfile_method_get_binding>]

Retrieve the binding at this index.


----



[int<class_int>] **get_binding_count**\ (\ ) |const| [🔗<class_OpenXRInteractionProfile_method_get_binding_count>]

Get the number of bindings in this interaction profile.


----



[OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>] **get_binding_modifier**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRInteractionProfile_method_get_binding_modifier>]

Get the [OpenXRBindingModifier<class_OpenXRBindingModifier>] at this index.


----



[int<class_int>] **get_binding_modifier_count**\ (\ ) |const| [🔗<class_OpenXRInteractionProfile_method_get_binding_modifier_count>]

Get the number of binding modifiers in this interaction profile.

