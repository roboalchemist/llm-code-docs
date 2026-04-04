:github_url: hide



# EditorSceneFormatImporter

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [EditorSceneFormatImporterBlend<class_EditorSceneFormatImporterBlend>], [EditorSceneFormatImporterFBX2GLTF<class_EditorSceneFormatImporterFBX2GLTF>], [EditorSceneFormatImporterGLTF<class_EditorSceneFormatImporterGLTF>], [EditorSceneFormatImporterUFBX<class_EditorSceneFormatImporterUFBX>]

Imports scenes from third-parties' 3D files.


## Description

**EditorSceneFormatImporter** allows to define an importer script for a third-party 3D format.

To use **EditorSceneFormatImporter**, register it using the [EditorPlugin.add_scene_format_importer_plugin()<class_EditorPlugin_method_add_scene_format_importer_plugin>] method first.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`_get_extensions<class_EditorSceneFormatImporter_private_method__get_extensions>`\ (\ ) |virtual| |required| |const|                                                                                                                                                                                                                                                                                          |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`_get_import_options<class_EditorSceneFormatImporter_private_method__get_import_options>`\ (\ path\: :ref:`String<class_String>`\ ) |virtual|                                                                                                                                                                                                                                                                 |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                     | :ref:`_get_option_visibility<class_EditorSceneFormatImporter_private_method__get_option_visibility>`\ (\ path\: :ref:`String<class_String>`, for_animation\: :ref:`bool<class_bool>`, option\: :ref:`String<class_String>`\ ) |virtual| |const|                                                                                                                                                                    |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                       | :ref:`_import_scene<class_EditorSceneFormatImporter_private_method__import_scene>`\ (\ path\: :ref:`String<class_String>`, flags\: :ref:`int<class_int>`, options\: :ref:`Dictionary<class_Dictionary>`\ ) |virtual| |required|                                                                                                                                                                                    |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_import_option<class_EditorSceneFormatImporter_method_add_import_option>`\ (\ name\: :ref:`String<class_String>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                                                                                                                                                |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_import_option_advanced<class_EditorSceneFormatImporter_method_add_import_option_advanced>`\ (\ type\: :ref:`Variant.Type<enum_@GlobalScope_Variant.Type>`, name\: :ref:`String<class_String>`, default_value\: :ref:`Variant<class_Variant>`, hint\: :ref:`PropertyHint<enum_@GlobalScope_PropertyHint>` = 0, hint_string\: :ref:`String<class_String>` = "", usage_flags\: :ref:`int<class_int>` = 6\ ) |
> +---------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**IMPORT_SCENE** = `1` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_SCENE>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





**IMPORT_ANIMATION** = `2` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_ANIMATION>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





**IMPORT_FAIL_ON_MISSING_DEPENDENCIES** = `4` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_FAIL_ON_MISSING_DEPENDENCIES>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





**IMPORT_GENERATE_TANGENT_ARRAYS** = `8` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_GENERATE_TANGENT_ARRAYS>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





**IMPORT_USE_NAMED_SKIN_BINDS** = `16` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_USE_NAMED_SKIN_BINDS>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





**IMPORT_DISCARD_MESHES_AND_MATERIALS** = `32` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_DISCARD_MESHES_AND_MATERIALS>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





**IMPORT_FORCE_DISABLE_MESH_COMPRESSION** = `64` [🔗<class_EditorSceneFormatImporter_constant_IMPORT_FORCE_DISABLE_MESH_COMPRESSION>]

> **CONTAINER**
>
	There is currently no description for this constant. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!




----


## Method Descriptions



[PackedStringArray<class_PackedStringArray>] **_get_extensions**\ (\ ) |virtual| |required| |const| [🔗<class_EditorSceneFormatImporter_private_method__get_extensions>]

Return supported file extensions for this scene importer.


----



|void| **_get_import_options**\ (\ path\: [String<class_String>]\ ) |virtual| [🔗<class_EditorSceneFormatImporter_private_method__get_import_options>]

Override to add general import options. These will appear in the main import dock on the editor. Add options via [add_import_option()<class_EditorSceneFormatImporter_method_add_import_option>] and [add_import_option_advanced()<class_EditorSceneFormatImporter_method_add_import_option_advanced>].

\ **Note:** All **EditorSceneFormatImporter** and [EditorScenePostImportPlugin<class_EditorScenePostImportPlugin>] instances will add options for all files. It is good practice to check the file extension when `path` is non-empty.

When the user is editing project settings, `path` will be empty. It is recommended to add all options when `path` is empty to allow the user to customize Import Defaults.


----



[Variant<class_Variant>] **_get_option_visibility**\ (\ path\: [String<class_String>], for_animation\: [bool<class_bool>], option\: [String<class_String>]\ ) |virtual| |const| [🔗<class_EditorSceneFormatImporter_private_method__get_option_visibility>]

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.


----



[Object<class_Object>] **_import_scene**\ (\ path\: [String<class_String>], flags\: [int<class_int>], options\: [Dictionary<class_Dictionary>]\ ) |virtual| |required| [🔗<class_EditorSceneFormatImporter_private_method__import_scene>]

Perform the bulk of the scene import logic here, for example using [GLTFDocument<class_GLTFDocument>] or [FBXDocument<class_FBXDocument>].


----



|void| **add_import_option**\ (\ name\: [String<class_String>], value\: [Variant<class_Variant>]\ ) [🔗<class_EditorSceneFormatImporter_method_add_import_option>]

Add a specific import option (name and default value only). This function can only be called from [_get_import_options()<class_EditorSceneFormatImporter_private_method__get_import_options>].


----



|void| **add_import_option_advanced**\ (\ type\: [Variant.Type<enum_@GlobalScope_Variant.Type>], name\: [String<class_String>], default_value\: [Variant<class_Variant>], hint\: [PropertyHint<enum_@GlobalScope_PropertyHint>] = 0, hint_string\: [String<class_String>] = "", usage_flags\: [int<class_int>] = 6\ ) [🔗<class_EditorSceneFormatImporter_method_add_import_option_advanced>]

Add a specific import option. This function can only be called from [_get_import_options()<class_EditorSceneFormatImporter_private_method__get_import_options>].

