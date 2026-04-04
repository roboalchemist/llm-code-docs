:github_url: hide



# ClassDB

**Inherits:** [Object<class_Object>]

A class information repository.


## Description

Provides access to metadata stored for every available engine class.

\ **Note:** Script-defined classes with `class_name` are not part of **ClassDB**, so they will not return reflection data such as a method or property list. However, [GDExtension<class_GDExtension>]-defined classes *are* part of **ClassDB**, so they will return reflection data.


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`can_instantiate<class_ClassDB_method_can_instantiate>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`class_call_static<class_ClassDB_method_class_call_static>`\ (\ class\: :ref:`StringName<class_StringName>`, method\: :ref:`StringName<class_StringName>`, ...\ ) |vararg|                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`class_exists<class_ClassDB_method_class_exists>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`APIType<enum_ClassDB_APIType>`                             | :ref:`class_get_api_type<class_ClassDB_method_class_get_api_type>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`class_get_enum_constants<class_ClassDB_method_class_get_enum_constants>`\ (\ class\: :ref:`StringName<class_StringName>`, enum\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`class_get_enum_list<class_ClassDB_method_class_get_enum_list>`\ (\ class\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`class_get_integer_constant<class_ClassDB_method_class_get_integer_constant>`\ (\ class\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`\ ) |const|                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`class_get_integer_constant_enum<class_ClassDB_method_class_get_integer_constant_enum>`\ (\ class\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`class_get_integer_constant_list<class_ClassDB_method_class_get_integer_constant_list>`\ (\ class\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`class_get_method_argument_count<class_ClassDB_method_class_get_method_argument_count>`\ (\ class\: :ref:`StringName<class_StringName>`, method\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const| |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`class_get_method_list<class_ClassDB_method_class_get_method_list>`\ (\ class\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`class_get_property<class_ClassDB_method_class_get_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                  |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`class_get_property_default_value<class_ClassDB_method_class_get_property_default_value>`\ (\ class\: :ref:`StringName<class_StringName>`, property\: :ref:`StringName<class_StringName>`\ ) |const|                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`class_get_property_getter<class_ClassDB_method_class_get_property_getter>`\ (\ class\: :ref:`StringName<class_StringName>`, property\: :ref:`StringName<class_StringName>`\ )                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`class_get_property_list<class_ClassDB_method_class_get_property_list>`\ (\ class\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`class_get_property_setter<class_ClassDB_method_class_get_property_setter>`\ (\ class\: :ref:`StringName<class_StringName>`, property\: :ref:`StringName<class_StringName>`\ )                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`class_get_signal<class_ClassDB_method_class_get_signal>`\ (\ class\: :ref:`StringName<class_StringName>`, signal\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`class_get_signal_list<class_ClassDB_method_class_get_signal_list>`\ (\ class\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`class_has_enum<class_ClassDB_method_class_has_enum>`\ (\ class\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`class_has_integer_constant<class_ClassDB_method_class_has_integer_constant>`\ (\ class\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`\ ) |const|                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`class_has_method<class_ClassDB_method_class_has_method>`\ (\ class\: :ref:`StringName<class_StringName>`, method\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`class_has_signal<class_ClassDB_method_class_has_signal>`\ (\ class\: :ref:`StringName<class_StringName>`, signal\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                            | :ref:`class_set_property<class_ClassDB_method_class_set_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ ) |const|                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`get_class_list<class_ClassDB_method_get_class_list>`\ (\ ) |const|                                                                                                                                                                                |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`get_inheriters_from_class<class_ClassDB_method_get_inheriters_from_class>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`get_parent_class<class_ClassDB_method_get_parent_class>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`instantiate<class_ClassDB_method_instantiate>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_class_enabled<class_ClassDB_method_is_class_enabled>`\ (\ class\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_class_enum_bitfield<class_ClassDB_method_is_class_enum_bitfield>`\ (\ class\: :ref:`StringName<class_StringName>`, enum\: :ref:`StringName<class_StringName>`, no_inheritance\: :ref:`bool<class_bool>` = false\ ) |const|                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_parent_class<class_ClassDB_method_is_parent_class>`\ (\ class\: :ref:`StringName<class_StringName>`, inherits\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **APIType**: [🔗<enum_ClassDB_APIType>]



[APIType<enum_ClassDB_APIType>] **API_CORE** = `0`

Native Core class type.



[APIType<enum_ClassDB_APIType>] **API_EDITOR** = `1`

Native Editor class type.



[APIType<enum_ClassDB_APIType>] **API_EXTENSION** = `2`

GDExtension class type.



[APIType<enum_ClassDB_APIType>] **API_EDITOR_EXTENSION** = `3`

GDExtension Editor class type.



[APIType<enum_ClassDB_APIType>] **API_NONE** = `4`

Unknown class type.


----


## Method Descriptions



[bool<class_bool>] **can_instantiate**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_can_instantiate>]

Returns `true` if objects can be instantiated from the specified `class`, otherwise returns `false`.


----



[Variant<class_Variant>] **class_call_static**\ (\ class\: [StringName<class_StringName>], method\: [StringName<class_StringName>], ...\ ) |vararg| [🔗<class_ClassDB_method_class_call_static>]

Calls a static method on a class.


----



[bool<class_bool>] **class_exists**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_exists>]

Returns whether the specified `class` is available or not.


----



[APIType<enum_ClassDB_APIType>] **class_get_api_type**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_get_api_type>]

Returns the API type of the specified `class`.


----



[PackedStringArray<class_PackedStringArray>] **class_get_enum_constants**\ (\ class\: [StringName<class_StringName>], enum\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_enum_constants>]

Returns an array with all the keys in `enum` of `class` or its ancestry.


----



[PackedStringArray<class_PackedStringArray>] **class_get_enum_list**\ (\ class\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_enum_list>]

Returns an array with all the enums of `class` or its ancestry.


----



[int<class_int>] **class_get_integer_constant**\ (\ class\: [StringName<class_StringName>], name\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_get_integer_constant>]

Returns the value of the integer constant `name` of `class` or its ancestry. Always returns 0 when the constant could not be found.


----



[StringName<class_StringName>] **class_get_integer_constant_enum**\ (\ class\: [StringName<class_StringName>], name\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_integer_constant_enum>]

Returns which enum the integer constant `name` of `class` or its ancestry belongs to.


----



[PackedStringArray<class_PackedStringArray>] **class_get_integer_constant_list**\ (\ class\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_integer_constant_list>]

Returns an array with the names all the integer constants of `class` or its ancestry.


----



[int<class_int>] **class_get_method_argument_count**\ (\ class\: [StringName<class_StringName>], method\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_method_argument_count>]

Returns the number of arguments of the method `method` of `class` or its ancestry if `no_inheritance` is `false`.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **class_get_method_list**\ (\ class\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_method_list>]

Returns an array with all the methods of `class` or its ancestry if `no_inheritance` is `false`. Every element of the array is a [Dictionary<class_Dictionary>] with the following keys: `args`, `default_args`, `flags`, `id`, `name`, `return: (class_name, hint, hint_string, name, type, usage)`.

\ **Note:** In exported release builds the debug info is not available, so the returned dictionaries will contain only method names.


----



[Variant<class_Variant>] **class_get_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_get_property>]

Returns the value of `property` of `object` or its ancestry.


----



[Variant<class_Variant>] **class_get_property_default_value**\ (\ class\: [StringName<class_StringName>], property\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_get_property_default_value>]

Returns the default value of `property` of `class` or its ancestor classes.


----



[StringName<class_StringName>] **class_get_property_getter**\ (\ class\: [StringName<class_StringName>], property\: [StringName<class_StringName>]\ ) [🔗<class_ClassDB_method_class_get_property_getter>]

Returns the getter method name of `property` of `class`.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **class_get_property_list**\ (\ class\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_property_list>]

Returns an array with all the properties of `class` or its ancestry if `no_inheritance` is `false`.


----



[StringName<class_StringName>] **class_get_property_setter**\ (\ class\: [StringName<class_StringName>], property\: [StringName<class_StringName>]\ ) [🔗<class_ClassDB_method_class_get_property_setter>]

Returns the setter method name of `property` of `class`.


----



[Dictionary<class_Dictionary>] **class_get_signal**\ (\ class\: [StringName<class_StringName>], signal\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_get_signal>]

Returns the `signal` data of `class` or its ancestry. The returned value is a [Dictionary<class_Dictionary>] with the following keys: `args`, `default_args`, `flags`, `id`, `name`, `return: (class_name, hint, hint_string, name, type, usage)`.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **class_get_signal_list**\ (\ class\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_get_signal_list>]

Returns an array with all the signals of `class` or its ancestry if `no_inheritance` is `false`. Every element of the array is a [Dictionary<class_Dictionary>] as described in [class_get_signal()<class_ClassDB_method_class_get_signal>].


----



[bool<class_bool>] **class_has_enum**\ (\ class\: [StringName<class_StringName>], name\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_has_enum>]

Returns whether `class` or its ancestry has an enum called `name` or not.


----



[bool<class_bool>] **class_has_integer_constant**\ (\ class\: [StringName<class_StringName>], name\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_has_integer_constant>]

Returns whether `class` or its ancestry has an integer constant called `name` or not.


----



[bool<class_bool>] **class_has_method**\ (\ class\: [StringName<class_StringName>], method\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_class_has_method>]

Returns whether `class` (or its ancestry if `no_inheritance` is `false`) has a method called `method` or not.


----



[bool<class_bool>] **class_has_signal**\ (\ class\: [StringName<class_StringName>], signal\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_class_has_signal>]

Returns whether `class` or its ancestry has a signal called `signal` or not.


----



[Error<enum_@GlobalScope_Error>] **class_set_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) |const| [🔗<class_ClassDB_method_class_set_property>]

Sets `property` value of `object` to `value`.


----



[PackedStringArray<class_PackedStringArray>] **get_class_list**\ (\ ) |const| [🔗<class_ClassDB_method_get_class_list>]

Returns the names of all engine classes available.

\ **Note:** Script-defined classes with `class_name` are not included in this list. Use [ProjectSettings.get_global_class_list()<class_ProjectSettings_method_get_global_class_list>] to get a list of script-defined classes instead.


----



[PackedStringArray<class_PackedStringArray>] **get_inheriters_from_class**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_get_inheriters_from_class>]

Returns the names of all engine classes that directly or indirectly inherit from `class`.


----



[StringName<class_StringName>] **get_parent_class**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_get_parent_class>]

Returns the parent class of `class`.


----



[Variant<class_Variant>] **instantiate**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_instantiate>]

Creates an instance of `class`.


----



[bool<class_bool>] **is_class_enabled**\ (\ class\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_is_class_enabled>]

Returns whether this `class` is enabled or not.


----



[bool<class_bool>] **is_class_enum_bitfield**\ (\ class\: [StringName<class_StringName>], enum\: [StringName<class_StringName>], no_inheritance\: [bool<class_bool>] = false\ ) |const| [🔗<class_ClassDB_method_is_class_enum_bitfield>]

Returns whether `class` (or its ancestor classes if `no_inheritance` is `false`) has an enum called `enum` that is a bitfield.


----



[bool<class_bool>] **is_parent_class**\ (\ class\: [StringName<class_StringName>], inherits\: [StringName<class_StringName>]\ ) |const| [🔗<class_ClassDB_method_is_parent_class>]

Returns whether `inherits` is an ancestor of `class` or not.

