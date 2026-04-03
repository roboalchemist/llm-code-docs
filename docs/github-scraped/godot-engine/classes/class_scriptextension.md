:github_url: hide



# ScriptExtension

**Inherits:** [Script<class_Script>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

> **CONTAINER**
>
	There is currently no description for this class. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_can_instantiate<class_ScriptExtension_private_method__can_instantiate>`\ (\ ) |virtual| |required| |const|                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_editor_can_reload_from_file<class_ScriptExtension_private_method__editor_can_reload_from_file>`\ (\ ) |virtual| |required|                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Script<class_Script>`                                      | :ref:`_get_base_script<class_ScriptExtension_private_method__get_base_script>`\ (\ ) |virtual| |required| |const|                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`_get_class_icon_path<class_ScriptExtension_private_method__get_class_icon_path>`\ (\ ) |virtual| |const|                                                                          |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`_get_constants<class_ScriptExtension_private_method__get_constants>`\ (\ ) |virtual| |required| |const|                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`_get_doc_class_name<class_ScriptExtension_private_method__get_doc_class_name>`\ (\ ) |virtual| |required| |const|                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_documentation<class_ScriptExtension_private_method__get_documentation>`\ (\ ) |virtual| |required| |const|                                                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`_get_global_name<class_ScriptExtension_private_method__get_global_name>`\ (\ ) |virtual| |required| |const|                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`_get_instance_base_type<class_ScriptExtension_private_method__get_instance_base_type>`\ (\ ) |virtual| |required| |const|                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ScriptLanguage<class_ScriptLanguage>`                      | :ref:`_get_language<class_ScriptExtension_private_method__get_language>`\ (\ ) |virtual| |required| |const|                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_get_member_line<class_ScriptExtension_private_method__get_member_line>`\ (\ member\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const|                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`_get_members<class_ScriptExtension_private_method__get_members>`\ (\ ) |virtual| |required| |const|                                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`_get_method_info<class_ScriptExtension_private_method__get_method_info>`\ (\ method\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const|                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`_get_property_default_value<class_ScriptExtension_private_method__get_property_default_value>`\ (\ property\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const| |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`_get_rpc_config<class_ScriptExtension_private_method__get_rpc_config>`\ (\ ) |virtual| |required| |const|                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`_get_script_method_argument_count<class_ScriptExtension_private_method__get_script_method_argument_count>`\ (\ method\: :ref:`StringName<class_StringName>`\ ) |virtual| |const|  |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_script_method_list<class_ScriptExtension_private_method__get_script_method_list>`\ (\ ) |virtual| |required| |const|                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_script_property_list<class_ScriptExtension_private_method__get_script_property_list>`\ (\ ) |virtual| |required| |const|                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_script_signal_list<class_ScriptExtension_private_method__get_script_signal_list>`\ (\ ) |virtual| |required| |const|                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`_get_source_code<class_ScriptExtension_private_method__get_source_code>`\ (\ ) |virtual| |required| |const|                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_has_method<class_ScriptExtension_private_method__has_method>`\ (\ method\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const|                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_has_property_default_value<class_ScriptExtension_private_method__has_property_default_value>`\ (\ property\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const| |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_has_script_signal<class_ScriptExtension_private_method__has_script_signal>`\ (\ signal\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const|                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_has_source_code<class_ScriptExtension_private_method__has_source_code>`\ (\ ) |virtual| |required| |const|                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_has_static_method<class_ScriptExtension_private_method__has_static_method>`\ (\ method\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |const|                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_inherits_script<class_ScriptExtension_private_method__inherits_script>`\ (\ script\: :ref:`Script<class_Script>`\ ) |virtual| |required| |const|                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | ``void*``                                                        | :ref:`_instance_create<class_ScriptExtension_private_method__instance_create>`\ (\ for_object\: :ref:`Object<class_Object>`\ ) |virtual| |required| |const|                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_instance_has<class_ScriptExtension_private_method__instance_has>`\ (\ object\: :ref:`Object<class_Object>`\ ) |virtual| |required| |const|                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_is_abstract<class_ScriptExtension_private_method__is_abstract>`\ (\ ) |virtual| |const|                                                                                          |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_is_placeholder_fallback_enabled<class_ScriptExtension_private_method__is_placeholder_fallback_enabled>`\ (\ ) |virtual| |required| |const|                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_is_tool<class_ScriptExtension_private_method__is_tool>`\ (\ ) |virtual| |required| |const|                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_is_valid<class_ScriptExtension_private_method__is_valid>`\ (\ ) |virtual| |required| |const|                                                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_placeholder_erased<class_ScriptExtension_private_method__placeholder_erased>`\ (\ placeholder\: ``void*``\ ) |virtual|                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | ``void*``                                                        | :ref:`_placeholder_instance_create<class_ScriptExtension_private_method__placeholder_instance_create>`\ (\ for_object\: :ref:`Object<class_Object>`\ ) |virtual| |required| |const|     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                            | :ref:`_reload<class_ScriptExtension_private_method__reload>`\ (\ keep_state\: :ref:`bool<class_bool>`\ ) |virtual| |required|                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_set_source_code<class_ScriptExtension_private_method__set_source_code>`\ (\ code\: :ref:`String<class_String>`\ ) |virtual| |required|                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_update_exports<class_ScriptExtension_private_method__update_exports>`\ (\ ) |virtual| |required|                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **_can_instantiate**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__can_instantiate>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_editor_can_reload_from_file**\ (\ ) |virtual| |required| [🔗<class_ScriptExtension_private_method__editor_can_reload_from_file>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Script<class_Script>] **_get_base_script**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_base_script>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[String<class_String>] **_get_class_icon_path**\ (\ ) |virtual| |const| [🔗<class_ScriptExtension_private_method__get_class_icon_path>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Dictionary<class_Dictionary>] **_get_constants**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_constants>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[StringName<class_StringName>] **_get_doc_class_name**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_doc_class_name>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_documentation**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_documentation>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[StringName<class_StringName>] **_get_global_name**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_global_name>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[StringName<class_StringName>] **_get_instance_base_type**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_instance_base_type>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[ScriptLanguage<class_ScriptLanguage>] **_get_language**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_language>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_member_line**\ (\ member\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_member_line>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **_get_members**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_members>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Dictionary<class_Dictionary>] **_get_method_info**\ (\ method\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_method_info>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Variant<class_Variant>] **_get_property_default_value**\ (\ property\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_property_default_value>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Variant<class_Variant>] **_get_rpc_config**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_rpc_config>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Variant<class_Variant>] **_get_script_method_argument_count**\ (\ method\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_ScriptExtension_private_method__get_script_method_argument_count>]

Return the expected argument count for the given `method`, or `null` if it can't be determined (which will then fall back to the default behavior).


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_script_method_list**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_script_method_list>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_script_property_list**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_script_property_list>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_script_signal_list**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_script_signal_list>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[String<class_String>] **_get_source_code**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__get_source_code>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_has_method**\ (\ method\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__has_method>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_has_property_default_value**\ (\ property\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__has_property_default_value>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_has_script_signal**\ (\ signal\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__has_script_signal>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_has_source_code**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__has_source_code>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_has_static_method**\ (\ method\: [StringName<class_StringName>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__has_static_method>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_inherits_script**\ (\ script\: [Script<class_Script>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__inherits_script>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



`void*` **_instance_create**\ (\ for_object\: [Object<class_Object>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__instance_create>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_instance_has**\ (\ object\: [Object<class_Object>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__instance_has>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_is_abstract**\ (\ ) |virtual| |const| [🔗<class_ScriptExtension_private_method__is_abstract>]

Returns `true` if the script is an abstract script. Abstract scripts cannot be instantiated directly, instead other scripts should inherit them. Abstract scripts will be either unselectable or hidden in the Create New Node dialog (unselectable if there are non-abstract classes inheriting it, otherwise hidden).


----



[bool<class_bool>] **_is_placeholder_fallback_enabled**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__is_placeholder_fallback_enabled>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_is_tool**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__is_tool>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_is_valid**\ (\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__is_valid>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_placeholder_erased**\ (\ placeholder\: `void*`\ ) |virtual| [🔗<class_ScriptExtension_private_method__placeholder_erased>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



`void*` **_placeholder_instance_create**\ (\ for_object\: [Object<class_Object>]\ ) |virtual| |required| |const| [🔗<class_ScriptExtension_private_method__placeholder_instance_create>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Error<enum_@GlobalScope_Error>] **_reload**\ (\ keep_state\: [bool<class_bool>]\ ) |virtual| |required| [🔗<class_ScriptExtension_private_method__reload>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_source_code**\ (\ code\: [String<class_String>]\ ) |virtual| |required| [🔗<class_ScriptExtension_private_method__set_source_code>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_update_exports**\ (\ ) |virtual| |required| [🔗<class_ScriptExtension_private_method__update_exports>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

