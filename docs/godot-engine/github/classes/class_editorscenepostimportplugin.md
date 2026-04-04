:github_url: hide



# EditorScenePostImportPlugin

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Plugin to control and modifying the process of importing a scene.


## Description

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`_get_import_options<class_EditorScenePostImportPlugin_private_method__get_import_options>`\ (\ path\: :ref:`String<class_String>`\ ) |virtual|                                                                                                                                                                                                                                                                 |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`_get_internal_import_options<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`\ (\ category\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                                                                                                                                                 |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`_get_internal_option_update_view_required<class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required>`\ (\ category\: :ref:`int<class_int>`, option\: :ref:`String<class_String>`\ ) |virtual| |const|                                                                                                                                                                         |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`_get_internal_option_visibility<class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility>`\ (\ category\: :ref:`int<class_int>`, for_animation\: :ref:`bool<class_bool>`, option\: :ref:`String<class_String>`\ ) |virtual| |const|                                                                                                                                                    |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`_get_option_visibility<class_EditorScenePostImportPlugin_private_method__get_option_visibility>`\ (\ path\: :ref:`String<class_String>`, for_animation\: :ref:`bool<class_bool>`, option\: :ref:`String<class_String>`\ ) |virtual| |const|                                                                                                                                                                    |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`_internal_process<class_EditorScenePostImportPlugin_private_method__internal_process>`\ (\ category\: :ref:`int<class_int>`, base_node\: :ref:`Node<class_Node>`, node\: :ref:`Node<class_Node>`, resource\: :ref:`Resource<class_Resource>`\ ) |virtual|                                                                                                                                                      |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`_post_process<class_EditorScenePostImportPlugin_private_method__post_process>`\ (\ scene\: :ref:`Node<class_Node>`\ ) |virtual|                                                                                                                                                                                                                                                                                |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`_pre_process<class_EditorScenePostImportPlugin_private_method__pre_process>`\ (\ scene\: :ref:`Node<class_Node>`\ ) |virtual|                                                                                                                                                                                                                                                                                  |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_import_option<class_EditorScenePostImportPlugin_method_add_import_option>`\ (\ name\: :ref:`String<class_String>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                                                                                                                                                |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_import_option_advanced<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`\ (\ type\: :ref:`Variant.Type<enum_@GlobalScope_Variant.Type>`, name\: :ref:`String<class_String>`, default_value\: :ref:`Variant<class_Variant>`, hint\: :ref:`PropertyHint<enum_@GlobalScope_PropertyHint>` = 0, hint_string\: :ref:`String<class_String>` = "", usage_flags\: :ref:`int<class_int>` = 6\ ) |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_option_value<class_EditorScenePostImportPlugin_method_get_option_value>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                                                         |
> +-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **InternalImportCategory**: [🔗<enum_EditorScenePostImportPlugin_InternalImportCategory>]



[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_NODE** = `0`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE** = `1`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_MESH** = `2`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_MATERIAL** = `3`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_ANIMATION** = `4`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE** = `5`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE** = `6`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>] **INTERNAL_IMPORT_CATEGORY_MAX** = `7`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!




----


## Method Descriptions



|void| **_get_import_options**\ (\ path\: [String<class_String>]\ ) |virtual| [🔗<class_EditorScenePostImportPlugin_private_method__get_import_options>]

Override to add general import options. These will appear in the main import dock on the editor. Add options via [add_import_option()<class_EditorScenePostImportPlugin_method_add_import_option>] and [add_import_option_advanced()<class_EditorScenePostImportPlugin_method_add_import_option_advanced>].


----



|void| **_get_internal_import_options**\ (\ category\: [int<class_int>]\ ) |virtual| [🔗<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>]

Override to add internal import options. These will appear in the 3D scene import dialog. Add options via [add_import_option()<class_EditorScenePostImportPlugin_method_add_import_option>] and [add_import_option_advanced()<class_EditorScenePostImportPlugin_method_add_import_option_advanced>].


----



[Variant<class_Variant>] **_get_internal_option_update_view_required**\ (\ category\: [int<class_int>], option\: [String<class_String>]\ ) |virtual| |const| [🔗<class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required>]

Should return `true` if the 3D view of the import dialog needs to update when changing the given option.


----



[Variant<class_Variant>] **_get_internal_option_visibility**\ (\ category\: [int<class_int>], for_animation\: [bool<class_bool>], option\: [String<class_String>]\ ) |virtual| |const| [🔗<class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility>]

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.


----



[Variant<class_Variant>] **_get_option_visibility**\ (\ path\: [String<class_String>], for_animation\: [bool<class_bool>], option\: [String<class_String>]\ ) |virtual| |const| [🔗<class_EditorScenePostImportPlugin_private_method__get_option_visibility>]

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.


----



|void| **_internal_process**\ (\ category\: [int<class_int>], base_node\: [Node<class_Node>], node\: [Node<class_Node>], resource\: [Resource<class_Resource>]\ ) |virtual| [🔗<class_EditorScenePostImportPlugin_private_method__internal_process>]

Process a specific node or resource for a given category.


----



|void| **_post_process**\ (\ scene\: [Node<class_Node>]\ ) |virtual| [🔗<class_EditorScenePostImportPlugin_private_method__post_process>]

Post-process the scene. This function is called after the final scene has been configured.


----



|void| **_pre_process**\ (\ scene\: [Node<class_Node>]\ ) |virtual| [🔗<class_EditorScenePostImportPlugin_private_method__pre_process>]

Pre-process the scene. This function is called right after the scene format loader loaded the scene and no changes have been made.

Pre-process may be used to adjust internal import options in the `"nodes"`, `"meshes"`, `"animations"` or `"materials"` keys inside `get_option_value("_subresources")`.


----



|void| **add_import_option**\ (\ name\: [String<class_String>], value\: [Variant<class_Variant>]\ ) [🔗<class_EditorScenePostImportPlugin_method_add_import_option>]

Add a specific import option (name and default value only). This function can only be called from [_get_import_options()<class_EditorScenePostImportPlugin_private_method__get_import_options>] and [_get_internal_import_options()<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>].


----



|void| **add_import_option_advanced**\ (\ type\: [Variant.Type<enum_@GlobalScope_Variant.Type>], name\: [String<class_String>], default_value\: [Variant<class_Variant>], hint\: [PropertyHint<enum_@GlobalScope_PropertyHint>] = 0, hint_string\: [String<class_String>] = "", usage_flags\: [int<class_int>] = 6\ ) [🔗<class_EditorScenePostImportPlugin_method_add_import_option_advanced>]

Add a specific import option. This function can only be called from [_get_import_options()<class_EditorScenePostImportPlugin_private_method__get_import_options>] and [_get_internal_import_options()<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>].


----



[Variant<class_Variant>] **get_option_value**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_EditorScenePostImportPlugin_method_get_option_value>]

Query the value of an option. This function can only be called from those querying visibility, or processing.

