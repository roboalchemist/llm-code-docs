:github_url: hide



# OpenXRIPBinding

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Defines a binding between an [OpenXRAction<class_OpenXRAction>] and an XR input or output.


## Description

This binding resource binds an [OpenXRAction<class_OpenXRAction>] to an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+----------------------------------------------------------------------------+--------+
> | :ref:`OpenXRAction<class_OpenXRAction>`           | :ref:`action<class_OpenXRIPBinding_property_action>`                       |        |
> +---------------------------------------------------+----------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`                         | :ref:`binding_modifiers<class_OpenXRIPBinding_property_binding_modifiers>` | ``[]`` |
> +---------------------------------------------------+----------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                       | :ref:`binding_path<class_OpenXRIPBinding_property_binding_path>`           | ``""`` |
> +---------------------------------------------------+----------------------------------------------------------------------------+--------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`paths<class_OpenXRIPBinding_property_paths>`                         |        |
> +---------------------------------------------------+----------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`add_path<class_OpenXRIPBinding_method_add_path>`\ (\ path\: :ref:`String<class_String>`\ )                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>` | :ref:`get_binding_modifier<class_OpenXRIPBinding_method_get_binding_modifier>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_binding_modifier_count<class_OpenXRIPBinding_method_get_binding_modifier_count>`\ (\ ) |const|                    |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_path_count<class_OpenXRIPBinding_method_get_path_count>`\ (\ ) |const|                                            |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`has_path<class_OpenXRIPBinding_method_has_path>`\ (\ path\: :ref:`String<class_String>`\ ) |const|                    |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`remove_path<class_OpenXRIPBinding_method_remove_path>`\ (\ path\: :ref:`String<class_String>`\ )                      |
> +-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[OpenXRAction<class_OpenXRAction>] **action** [🔗<class_OpenXRIPBinding_property_action>]


- |void| **set_action**\ (\ value\: [OpenXRAction<class_OpenXRAction>]\ )
- [OpenXRAction<class_OpenXRAction>] **get_action**\ (\ )

[OpenXRAction<class_OpenXRAction>] that is bound to [binding_path<class_OpenXRIPBinding_property_binding_path>].


----



[Array<class_Array>] **binding_modifiers** = `[]` [🔗<class_OpenXRIPBinding_property_binding_modifiers>]


- |void| **set_binding_modifiers**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_binding_modifiers**\ (\ )

Binding modifiers for this binding.


----



[String<class_String>] **binding_path** = `""` [🔗<class_OpenXRIPBinding_property_binding_path>]


- |void| **set_binding_path**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_binding_path**\ (\ )

Binding path that defines the input or output bound to [action<class_OpenXRIPBinding_property_action>].

\ **Note:** Binding paths are suggestions, an XR runtime may choose to bind the action to a different input or output emulating this input or output.


----



[PackedStringArray<class_PackedStringArray>] **paths** [🔗<class_OpenXRIPBinding_property_paths>]


- |void| **set_paths**\ (\ value\: [PackedStringArray<class_PackedStringArray>]\ )
- [PackedStringArray<class_PackedStringArray>] **get_paths**\ (\ )

**Deprecated:** Use [binding_path<class_OpenXRIPBinding_property_binding_path>] instead.

Paths that define the inputs or outputs bound on the device.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray<class_PackedStringArray>] for more details.


----


## Method Descriptions



|void| **add_path**\ (\ path\: [String<class_String>]\ ) [🔗<class_OpenXRIPBinding_method_add_path>]

**Deprecated:** Binding is for a single path.

Add an input/output path to this binding.


----



[OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>] **get_binding_modifier**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRIPBinding_method_get_binding_modifier>]

Get the [OpenXRBindingModifier<class_OpenXRBindingModifier>] at this index.


----



[int<class_int>] **get_binding_modifier_count**\ (\ ) |const| [🔗<class_OpenXRIPBinding_method_get_binding_modifier_count>]

Get the number of binding modifiers for this binding.


----



[int<class_int>] **get_path_count**\ (\ ) |const| [🔗<class_OpenXRIPBinding_method_get_path_count>]

**Deprecated:** Binding is for a single path.

Get the number of input/output paths in this binding.


----



[bool<class_bool>] **has_path**\ (\ path\: [String<class_String>]\ ) |const| [🔗<class_OpenXRIPBinding_method_has_path>]

**Deprecated:** Binding is for a single path.

Returns `true` if this input/output path is part of this binding.


----



|void| **remove_path**\ (\ path\: [String<class_String>]\ ) [🔗<class_OpenXRIPBinding_method_remove_path>]

**Deprecated:** Binding is for a single path.

Removes this input/output path from this binding.

