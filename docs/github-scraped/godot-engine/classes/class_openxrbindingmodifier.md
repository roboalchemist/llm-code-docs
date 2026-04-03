:github_url: hide



# OpenXRBindingModifier

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>], [OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>]

Binding modifier base class.


## Description

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`_get_description<class_OpenXRBindingModifier_private_method__get_description>`\ (\ ) |virtual| |required| |const| |
> +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`_get_ip_modification<class_OpenXRBindingModifier_private_method__get_ip_modification>`\ (\ ) |virtual| |required| |
> +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[String<class_String>] **_get_description**\ (\ ) |virtual| |required| |const| [🔗<class_OpenXRBindingModifier_private_method__get_description>]

Return the description of this class that is used for the title bar of the binding modifier editor.


----



[PackedByteArray<class_PackedByteArray>] **_get_ip_modification**\ (\ ) |virtual| |required| [🔗<class_OpenXRBindingModifier_private_method__get_ip_modification>]

Returns the data that is sent to OpenXR when submitting the suggested interacting bindings this modifier is a part of.

\ **Note:** This must be data compatible with an `XrBindingModificationBaseHeaderKHR` structure.

