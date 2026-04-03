:github_url: hide



# RegExMatch

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Contains the results of a [RegEx<class_RegEx>] search.


## Description

Contains the results of a single [RegEx<class_RegEx>] match returned by [RegEx.search()<class_RegEx_method_search>] and [RegEx.search_all()<class_RegEx_method_search_all>]. It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+---------------------------------------------------+-------------------------+
> | :ref:`Dictionary<class_Dictionary>`               | :ref:`names<class_RegExMatch_property_names>`     | ``{}``                  |
> +---------------------------------------------------+---------------------------------------------------+-------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`strings<class_RegExMatch_property_strings>` | ``PackedStringArray()`` |
> +---------------------------------------------------+---------------------------------------------------+-------------------------+
> | :ref:`String<class_String>`                       | :ref:`subject<class_RegExMatch_property_subject>` | ``""``                  |
> +---------------------------------------------------+---------------------------------------------------+-------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+---------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_end<class_RegExMatch_method_get_end>`\ (\ name\: :ref:`Variant<class_Variant>` = 0\ ) |const|       |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_group_count<class_RegExMatch_method_get_group_count>`\ (\ ) |const|                                 |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_start<class_RegExMatch_method_get_start>`\ (\ name\: :ref:`Variant<class_Variant>` = 0\ ) |const|   |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_string<class_RegExMatch_method_get_string>`\ (\ name\: :ref:`Variant<class_Variant>` = 0\ ) |const| |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Dictionary<class_Dictionary>] **names** = `{}` [🔗<class_RegExMatch_property_names>]


- [Dictionary<class_Dictionary>] **get_names**\ (\ )

A dictionary of named groups and its corresponding group number. Only groups that were matched are included. If multiple groups have the same name, that name would refer to the first matching one.


----



[PackedStringArray<class_PackedStringArray>] **strings** = `PackedStringArray()` [🔗<class_RegExMatch_property_strings>]


- [PackedStringArray<class_PackedStringArray>] **get_strings**\ (\ )

An [Array<class_Array>] of the match and its capturing groups.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray<class_PackedStringArray>] for more details.


----



[String<class_String>] **subject** = `""` [🔗<class_RegExMatch_property_subject>]


- [String<class_String>] **get_subject**\ (\ )

The source string used with the search pattern to find this matching result.


----


## Method Descriptions



[int<class_int>] **get_end**\ (\ name\: [Variant<class_Variant>] = 0\ ) |const| [🔗<class_RegExMatch_method_get_end>]

Returns the end position of the match within the source string. The end position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.


----



[int<class_int>] **get_group_count**\ (\ ) |const| [🔗<class_RegExMatch_method_get_group_count>]

Returns the number of capturing groups.


----



[int<class_int>] **get_start**\ (\ name\: [Variant<class_Variant>] = 0\ ) |const| [🔗<class_RegExMatch_method_get_start>]

Returns the starting position of the match within the source string. The starting position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.


----



[String<class_String>] **get_string**\ (\ name\: [Variant<class_Variant>] = 0\ ) |const| [🔗<class_RegExMatch_method_get_string>]

Returns the substring of the match from the source string. Capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns an empty string if the group did not match or doesn't exist.

