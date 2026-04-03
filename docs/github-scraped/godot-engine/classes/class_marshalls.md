:github_url: hide



# Marshalls

**Inherits:** [Object<class_Object>]

Data transformation (marshaling) and encoding helpers.


## Description

Provides data transformation and encoding utility functions.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`base64_to_raw<class_Marshalls_method_base64_to_raw>`\ (\ base64_str\: :ref:`String<class_String>`\ )                                                          |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`base64_to_utf8<class_Marshalls_method_base64_to_utf8>`\ (\ base64_str\: :ref:`String<class_String>`\ )                                                        |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                 | :ref:`base64_to_variant<class_Marshalls_method_base64_to_variant>`\ (\ base64_str\: :ref:`String<class_String>`, allow_objects\: :ref:`bool<class_bool>` = false\ ) |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`raw_to_base64<class_Marshalls_method_raw_to_base64>`\ (\ array\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                                             |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`utf8_to_base64<class_Marshalls_method_utf8_to_base64>`\ (\ utf8_str\: :ref:`String<class_String>`\ )                                                          |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`variant_to_base64<class_Marshalls_method_variant_to_base64>`\ (\ variant\: :ref:`Variant<class_Variant>`, full_objects\: :ref:`bool<class_bool>` = false\ )   |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[PackedByteArray<class_PackedByteArray>] **base64_to_raw**\ (\ base64_str\: [String<class_String>]\ ) [🔗<class_Marshalls_method_base64_to_raw>]

Returns a decoded [PackedByteArray<class_PackedByteArray>] corresponding to the Base64-encoded string `base64_str`.


----



[String<class_String>] **base64_to_utf8**\ (\ base64_str\: [String<class_String>]\ ) [🔗<class_Marshalls_method_base64_to_utf8>]

Returns a decoded string corresponding to the Base64-encoded string `base64_str`.


----



[Variant<class_Variant>] **base64_to_variant**\ (\ base64_str\: [String<class_String>], allow_objects\: [bool<class_bool>] = false\ ) [🔗<class_Marshalls_method_base64_to_variant>]

Returns a decoded [Variant<class_Variant>] corresponding to the Base64-encoded string `base64_str`. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the [@GlobalScope.bytes_to_var()<class_@GlobalScope_method_bytes_to_var>] method.

\ **Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.


----



[String<class_String>] **raw_to_base64**\ (\ array\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_Marshalls_method_raw_to_base64>]

Returns a Base64-encoded string of a given [PackedByteArray<class_PackedByteArray>].


----



[String<class_String>] **utf8_to_base64**\ (\ utf8_str\: [String<class_String>]\ ) [🔗<class_Marshalls_method_utf8_to_base64>]

Returns a Base64-encoded string of the UTF-8 string `utf8_str`.


----



[String<class_String>] **variant_to_base64**\ (\ variant\: [Variant<class_Variant>], full_objects\: [bool<class_bool>] = false\ ) [🔗<class_Marshalls_method_variant_to_base64>]

Returns a Base64-encoded string of the [Variant<class_Variant>] `variant`. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the [@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>] method.

