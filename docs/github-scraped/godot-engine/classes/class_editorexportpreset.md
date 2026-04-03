:github_url: hide



# EditorExportPreset

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Export preset configuration.


## Description

Represents the configuration of an export preset, as created by the editor's export dialog. An **EditorExportPreset** instance is intended to be used a read-only configuration passed to the [EditorExportPlatform<class_EditorExportPlatform>] methods when exporting the project.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`are_advanced_options_enabled<class_EditorExportPreset_method_are_advanced_options_enabled>`\ (\ ) |const|                                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_custom_features<class_EditorExportPreset_method_get_custom_features>`\ (\ ) |const|                                                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                               | :ref:`get_customized_files<class_EditorExportPreset_method_get_customized_files>`\ (\ ) |const|                                                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_customized_files_count<class_EditorExportPreset_method_get_customized_files_count>`\ (\ ) |const|                                                                                                      |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`get_encrypt_directory<class_EditorExportPreset_method_get_encrypt_directory>`\ (\ ) |const|                                                                                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`get_encrypt_pck<class_EditorExportPreset_method_get_encrypt_pck>`\ (\ ) |const|                                                                                                                            |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_encryption_ex_filter<class_EditorExportPreset_method_get_encryption_ex_filter>`\ (\ ) |const|                                                                                                          |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_encryption_in_filter<class_EditorExportPreset_method_get_encryption_in_filter>`\ (\ ) |const|                                                                                                          |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_encryption_key<class_EditorExportPreset_method_get_encryption_key>`\ (\ ) |const|                                                                                                                      |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_exclude_filter<class_EditorExportPreset_method_get_exclude_filter>`\ (\ ) |const|                                                                                                                      |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ExportFilter<enum_EditorExportPreset_ExportFilter>`         | :ref:`get_export_filter<class_EditorExportPreset_method_get_export_filter>`\ (\ ) |const|                                                                                                                        |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_export_path<class_EditorExportPreset_method_get_export_path>`\ (\ ) |const|                                                                                                                            |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`FileExportMode<enum_EditorExportPreset_FileExportMode>`     | :ref:`get_file_export_mode<class_EditorExportPreset_method_get_file_export_mode>`\ (\ path\: :ref:`String<class_String>`, default\: :ref:`FileExportMode<enum_EditorExportPreset_FileExportMode>` = 0\ ) |const| |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                 | :ref:`get_files_to_export<class_EditorExportPreset_method_get_files_to_export>`\ (\ ) |const|                                                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_include_filter<class_EditorExportPreset_method_get_include_filter>`\ (\ ) |const|                                                                                                                      |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                     | :ref:`get_or_env<class_EditorExportPreset_method_get_or_env>`\ (\ name\: :ref:`StringName<class_StringName>`, env_var\: :ref:`String<class_String>`\ ) |const|                                                   |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                 | :ref:`get_patches<class_EditorExportPreset_method_get_patches>`\ (\ ) |const|                                                                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_preset_name<class_EditorExportPreset_method_get_preset_name>`\ (\ ) |const|                                                                                                                            |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                     | :ref:`get_project_setting<class_EditorExportPreset_method_get_project_setting>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>` | :ref:`get_script_export_mode<class_EditorExportPreset_method_get_script_export_mode>`\ (\ ) |const|                                                                                                              |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_version<class_EditorExportPreset_method_get_version>`\ (\ name\: :ref:`StringName<class_StringName>`, windows_version\: :ref:`bool<class_bool>`\ ) |const|                                             |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`has<class_EditorExportPreset_method_has>`\ (\ property\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`has_export_file<class_EditorExportPreset_method_has_export_file>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`is_dedicated_server<class_EditorExportPreset_method_is_dedicated_server>`\ (\ ) |const|                                                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`is_runnable<class_EditorExportPreset_method_is_runnable>`\ (\ ) |const|                                                                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ExportFilter**: [🔗<enum_EditorExportPreset_ExportFilter>]



[ExportFilter<enum_EditorExportPreset_ExportFilter>] **EXPORT_ALL_RESOURCES** = `0`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[ExportFilter<enum_EditorExportPreset_ExportFilter>] **EXPORT_SELECTED_SCENES** = `1`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[ExportFilter<enum_EditorExportPreset_ExportFilter>] **EXPORT_SELECTED_RESOURCES** = `2`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[ExportFilter<enum_EditorExportPreset_ExportFilter>] **EXCLUDE_SELECTED_RESOURCES** = `3`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[ExportFilter<enum_EditorExportPreset_ExportFilter>] **EXPORT_CUSTOMIZED** = `4`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!




----



enum **FileExportMode**: [🔗<enum_EditorExportPreset_FileExportMode>]



[FileExportMode<enum_EditorExportPreset_FileExportMode>] **MODE_FILE_NOT_CUSTOMIZED** = `0`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[FileExportMode<enum_EditorExportPreset_FileExportMode>] **MODE_FILE_STRIP** = `1`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[FileExportMode<enum_EditorExportPreset_FileExportMode>] **MODE_FILE_KEEP** = `2`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[FileExportMode<enum_EditorExportPreset_FileExportMode>] **MODE_FILE_REMOVE** = `3`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!




----



enum **ScriptExportMode**: [🔗<enum_EditorExportPreset_ScriptExportMode>]



[ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>] **MODE_SCRIPT_TEXT** = `0`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>] **MODE_SCRIPT_BINARY_TOKENS** = `1`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>] **MODE_SCRIPT_BINARY_TOKENS_COMPRESSED** = `2`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!




----


## Method Descriptions



[bool<class_bool>] **are_advanced_options_enabled**\ (\ ) |const| [🔗<class_EditorExportPreset_method_are_advanced_options_enabled>]

Returns `true` if the "Advanced" toggle is enabled in the export dialog.


----



[String<class_String>] **get_custom_features**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_custom_features>]

Returns a comma-separated list of custom features added to this preset, as a string. See [../tutorials/export/feature_tags](Feature tags .md) in the documentation for more information.


----



[Dictionary<class_Dictionary>] **get_customized_files**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_customized_files>]

Returns a dictionary of files selected in the "Resources" tab of the export dialog. The dictionary's keys are file paths, and its values are the corresponding export modes: `"strip"`, `"keep"`, or `"remove"`. See also [get_file_export_mode()<class_EditorExportPreset_method_get_file_export_mode>].


----



[int<class_int>] **get_customized_files_count**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_customized_files_count>]

Returns the number of files selected in the "Resources" tab of the export dialog.


----



[bool<class_bool>] **get_encrypt_directory**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_encrypt_directory>]

Returns `true` if PCK directory encryption is enabled in the export dialog.


----



[bool<class_bool>] **get_encrypt_pck**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_encrypt_pck>]

Returns `true` if PCK encryption is enabled in the export dialog.


----



[String<class_String>] **get_encryption_ex_filter**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_encryption_ex_filter>]

Returns file filters to exclude during PCK encryption.


----



[String<class_String>] **get_encryption_in_filter**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_encryption_in_filter>]

Returns file filters to include during PCK encryption.


----



[String<class_String>] **get_encryption_key**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_encryption_key>]

Returns PCK encryption key.


----



[String<class_String>] **get_exclude_filter**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_exclude_filter>]

Returns file filters to exclude during export.


----



[ExportFilter<enum_EditorExportPreset_ExportFilter>] **get_export_filter**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_export_filter>]

Returns export file filter mode selected in the "Resources" tab of the export dialog.


----



[String<class_String>] **get_export_path**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_export_path>]

Returns export target path.


----



[FileExportMode<enum_EditorExportPreset_FileExportMode>] **get_file_export_mode**\ (\ path\: [String<class_String>], default\: [FileExportMode<enum_EditorExportPreset_FileExportMode>] = 0\ ) |const| [🔗<class_EditorExportPreset_method_get_file_export_mode>]

Returns file export mode for the specified file.


----



[PackedStringArray<class_PackedStringArray>] **get_files_to_export**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_files_to_export>]

Returns array of files to export.


----



[String<class_String>] **get_include_filter**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_include_filter>]

Returns file filters to include during export.


----



[Variant<class_Variant>] **get_or_env**\ (\ name\: [StringName<class_StringName>], env_var\: [String<class_String>]\ ) |const| [🔗<class_EditorExportPreset_method_get_or_env>]

Returns export option value or value of environment variable if it is set.


----



[PackedStringArray<class_PackedStringArray>] **get_patches**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_patches>]

Returns the list of packs on which to base a patch export on.


----



[String<class_String>] **get_preset_name**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_preset_name>]

Returns this export preset's name.


----



[Variant<class_Variant>] **get_project_setting**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_EditorExportPreset_method_get_project_setting>]

Returns the value of the setting identified by `name` using export preset feature tag overrides instead of current OS features.


----



[ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>] **get_script_export_mode**\ (\ ) |const| [🔗<class_EditorExportPreset_method_get_script_export_mode>]

Returns the export mode used by GDScript files. `0` for "Text", `1` for "Binary tokens", and `2` for "Compressed binary tokens (smaller files)".


----



[String<class_String>] **get_version**\ (\ name\: [StringName<class_StringName>], windows_version\: [bool<class_bool>]\ ) |const| [🔗<class_EditorExportPreset_method_get_version>]

Returns the preset's version number, or fall back to the [ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>] project setting if set to an empty string.

If `windows_version` is `true`, formats the returned version number to be compatible with Windows executable metadata.


----



[bool<class_bool>] **has**\ (\ property\: [StringName<class_StringName>]\ ) |const| [🔗<class_EditorExportPreset_method_has>]

Returns `true` if the preset has the property named `property`.


----



[bool<class_bool>] **has_export_file**\ (\ path\: [String<class_String>]\ ) [🔗<class_EditorExportPreset_method_has_export_file>]

Returns `true` if the file at the specified `path` will be exported.


----



[bool<class_bool>] **is_dedicated_server**\ (\ ) |const| [🔗<class_EditorExportPreset_method_is_dedicated_server>]

Returns `true` if the dedicated server export mode is selected in the export dialog.


----



[bool<class_bool>] **is_runnable**\ (\ ) |const| [🔗<class_EditorExportPreset_method_is_runnable>]

Returns `true` if the "Runnable" toggle is enabled in the export dialog.

