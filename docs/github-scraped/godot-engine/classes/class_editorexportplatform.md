:github_url: hide



# EditorExportPlatform

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [EditorExportPlatformAndroid<class_EditorExportPlatformAndroid>], [EditorExportPlatformAppleEmbedded<class_EditorExportPlatformAppleEmbedded>], [EditorExportPlatformExtension<class_EditorExportPlatformExtension>], [EditorExportPlatformMacOS<class_EditorExportPlatformMacOS>], [EditorExportPlatformPC<class_EditorExportPlatformPC>], [EditorExportPlatformWeb<class_EditorExportPlatformWeb>]

Identifies a supported export platform, and internally provides the functionality of exporting to that platform.


## Description

Base resource that provides the functionality of exporting a release build of a project to a platform, from the editor. Stores platform-specific metadata such as the name and supported features of the platform, and performs the exporting of projects, PCK files, and ZIP files. Uses an export template for the platform provided at the time of project exporting.

Used in scripting by [EditorExportPlugin<class_EditorExportPlugin>] to configure platform-specific customization of scenes and resources. See [EditorExportPlugin._begin_customize_scenes()<class_EditorExportPlugin_private_method__begin_customize_scenes>] and [EditorExportPlugin._begin_customize_resources()<class_EditorExportPlugin_private_method__begin_customize_resources>] for more details.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`add_message<class_EditorExportPlatform_method_add_message>`\ (\ type\: :ref:`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`, category\: :ref:`String<class_String>`, message\: :ref:`String<class_String>`\ )                                                                                                                                                         |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`clear_messages<class_EditorExportPlatform_method_clear_messages>`\ (\ )                                                                                                                                                                                                                                                                                                                |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorExportPreset<class_EditorExportPreset>`                   | :ref:`create_preset<class_EditorExportPlatform_method_create_preset>`\ (\ )                                                                                                                                                                                                                                                                                                                  |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`export_pack<class_EditorExportPlatform_method_export_pack>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`, flags\: |bitfield|\[:ref:`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\] = 0\ )                                                                                                |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`export_pack_patch<class_EditorExportPlatform_method_export_pack_patch>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`, patches\: :ref:`PackedStringArray<class_PackedStringArray>` = PackedStringArray(), flags\: |bitfield|\[:ref:`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\] = 0\ ) |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`export_project<class_EditorExportPlatform_method_export_project>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`, flags\: |bitfield|\[:ref:`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\] = 0\ )                                                                                          |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`export_project_files<class_EditorExportPlatform_method_export_project_files>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, save_cb\: :ref:`Callable<class_Callable>`, shared_cb\: :ref:`Callable<class_Callable>` = Callable()\ )                                                                                                |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`export_zip<class_EditorExportPlatform_method_export_zip>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`, flags\: |bitfield|\[:ref:`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\] = 0\ )                                                                                                  |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`export_zip_patch<class_EditorExportPlatform_method_export_zip_patch>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`, patches\: :ref:`PackedStringArray<class_PackedStringArray>` = PackedStringArray(), flags\: |bitfield|\[:ref:`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\] = 0\ )   |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                   | :ref:`find_export_template<class_EditorExportPlatform_method_find_export_template>`\ (\ template_file_name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                                                                                                          |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                     | :ref:`gen_export_flags<class_EditorExportPlatform_method_gen_export_flags>`\ (\ flags\: |bitfield|\[:ref:`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]\ )                                                                                                                                                                                                                             |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                             | :ref:`get_current_presets<class_EditorExportPlatform_method_get_current_presets>`\ (\ ) |const|                                                                                                                                                                                                                                                                                              |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                     | :ref:`get_forced_export_files<class_EditorExportPlatform_method_get_forced_export_files>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>` = null\ ) |static|                                                                                                                                                                                                                |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                   | :ref:`get_internal_export_files<class_EditorExportPlatform_method_get_internal_export_files>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`\ )                                                                                                                                                                                           |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                           | :ref:`get_message_category<class_EditorExportPlatform_method_get_message_category>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                             |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_message_count<class_EditorExportPlatform_method_get_message_count>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                  |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                           | :ref:`get_message_text<class_EditorExportPlatform_method_get_message_text>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                     |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>` | :ref:`get_message_type<class_EditorExportPlatform_method_get_message_type>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                     |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                           | :ref:`get_os_name<class_EditorExportPlatform_method_get_os_name>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                              |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>` | :ref:`get_worst_message_type<class_EditorExportPlatform_method_get_worst_message_type>`\ (\ ) |const|                                                                                                                                                                                                                                                                                        |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                   | :ref:`save_pack<class_EditorExportPlatform_method_save_pack>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`, embed\: :ref:`bool<class_bool>` = false\ )                                                                                                                                              |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                   | :ref:`save_pack_patch<class_EditorExportPlatform_method_save_pack_patch>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`\ )                                                                                                                                                                           |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                   | :ref:`save_zip<class_EditorExportPlatform_method_save_zip>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`\ )                                                                                                                                                                                         |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                   | :ref:`save_zip_patch<class_EditorExportPlatform_method_save_zip_patch>`\ (\ preset\: :ref:`EditorExportPreset<class_EditorExportPreset>`, debug\: :ref:`bool<class_bool>`, path\: :ref:`String<class_String>`\ )                                                                                                                                                                             |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`ssh_push_to_remote<class_EditorExportPlatform_method_ssh_push_to_remote>`\ (\ host\: :ref:`String<class_String>`, port\: :ref:`String<class_String>`, scp_args\: :ref:`PackedStringArray<class_PackedStringArray>`, src_file\: :ref:`String<class_String>`, dst_file\: :ref:`String<class_String>`\ ) |const|                                                                          |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                                 | :ref:`ssh_run_on_remote<class_EditorExportPlatform_method_ssh_run_on_remote>`\ (\ host\: :ref:`String<class_String>`, port\: :ref:`String<class_String>`, ssh_arg\: :ref:`PackedStringArray<class_PackedStringArray>`, cmd_args\: :ref:`String<class_String>`, output\: :ref:`Array<class_Array>` = [], port_fwd\: :ref:`int<class_int>` = -1\ ) |const|                                     |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`ssh_run_on_remote_no_wait<class_EditorExportPlatform_method_ssh_run_on_remote_no_wait>`\ (\ host\: :ref:`String<class_String>`, port\: :ref:`String<class_String>`, ssh_args\: :ref:`PackedStringArray<class_PackedStringArray>`, cmd_args\: :ref:`String<class_String>`, port_fwd\: :ref:`int<class_int>` = -1\ ) |const|                                                             |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ExportMessageType**: [🔗<enum_EditorExportPlatform_ExportMessageType>]



[ExportMessageType<enum_EditorExportPlatform_ExportMessageType>] **EXPORT_MESSAGE_NONE** = `0`

Invalid message type used as the default value when no type is specified.



[ExportMessageType<enum_EditorExportPlatform_ExportMessageType>] **EXPORT_MESSAGE_INFO** = `1`

Message type for informational messages that have no effect on the export.



[ExportMessageType<enum_EditorExportPlatform_ExportMessageType>] **EXPORT_MESSAGE_WARNING** = `2`

Message type for warning messages that should be addressed but still allow to complete the export.



[ExportMessageType<enum_EditorExportPlatform_ExportMessageType>] **EXPORT_MESSAGE_ERROR** = `3`

Message type for error messages that must be addressed and fail the export.


----



flags **DebugFlags**: [🔗<enum_EditorExportPlatform_DebugFlags>]



[DebugFlags<enum_EditorExportPlatform_DebugFlags>] **DEBUG_FLAG_DUMB_CLIENT** = `1`

Flag is set if the remotely debugged project is expected to use the remote file system. If set, [gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>] will append `--remote-fs` and `--remote-fs-password` (if [EditorSettings.filesystem/file_server/password<class_EditorSettings_property_filesystem/file_server/password>] is defined) command line arguments to the returned list.



[DebugFlags<enum_EditorExportPlatform_DebugFlags>] **DEBUG_FLAG_REMOTE_DEBUG** = `2`

Flag is set if remote debug is enabled. If set, [gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>] will append `--remote-debug` and `--breakpoints` (if breakpoints are selected in the script editor or added by the plugin) command line arguments to the returned list.



[DebugFlags<enum_EditorExportPlatform_DebugFlags>] **DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST** = `4`

Flag is set if remotely debugged project is running on the localhost. If set, [gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>] will use `localhost` instead of [EditorSettings.network/debug/remote_host<class_EditorSettings_property_network/debug/remote_host>] as remote debugger host.



[DebugFlags<enum_EditorExportPlatform_DebugFlags>] **DEBUG_FLAG_VIEW_COLLISIONS** = `8`

Flag is set if the "Visible Collision Shapes" remote debug option is enabled. If set, [gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>] will append the `--debug-collisions` command line argument to the returned list.



[DebugFlags<enum_EditorExportPlatform_DebugFlags>] **DEBUG_FLAG_VIEW_NAVIGATION** = `16`

Flag is set if the "Visible Navigation" remote debug option is enabled. If set, [gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>] will append the `--debug-navigation` command line argument to the returned list.


----


## Method Descriptions



|void| **add_message**\ (\ type\: [ExportMessageType<enum_EditorExportPlatform_ExportMessageType>], category\: [String<class_String>], message\: [String<class_String>]\ ) [🔗<class_EditorExportPlatform_method_add_message>]

Adds a message to the export log that will be displayed when exporting ends.


----



|void| **clear_messages**\ (\ ) [🔗<class_EditorExportPlatform_method_clear_messages>]

Clears the export log.


----



[EditorExportPreset<class_EditorExportPreset>] **create_preset**\ (\ ) [🔗<class_EditorExportPlatform_method_create_preset>]

Create a new preset for this platform.


----



[Error<enum_@GlobalScope_Error>] **export_pack**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>], flags\: |bitfield|\[[DebugFlags<enum_EditorExportPlatform_DebugFlags>]\] = 0\ ) [🔗<class_EditorExportPlatform_method_export_pack>]

Creates a PCK archive at `path` for the specified `preset`.


----



[Error<enum_@GlobalScope_Error>] **export_pack_patch**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>], patches\: [PackedStringArray<class_PackedStringArray>] = PackedStringArray(), flags\: |bitfield|\[[DebugFlags<enum_EditorExportPlatform_DebugFlags>]\] = 0\ ) [🔗<class_EditorExportPlatform_method_export_pack_patch>]

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

\ **Note:** `patches` is an optional override of the set of patches defined in the export preset. When empty the patches defined in the export preset will be used instead.


----



[Error<enum_@GlobalScope_Error>] **export_project**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>], flags\: |bitfield|\[[DebugFlags<enum_EditorExportPlatform_DebugFlags>]\] = 0\ ) [🔗<class_EditorExportPlatform_method_export_project>]

Creates a full project at `path` for the specified `preset`.


----



[Error<enum_@GlobalScope_Error>] **export_project_files**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], save_cb\: [Callable<class_Callable>], shared_cb\: [Callable<class_Callable>] = Callable()\ ) [🔗<class_EditorExportPlatform_method_export_project_files>]

Exports project files for the specified preset. This method can be used to implement custom export format, other than PCK and ZIP. One of the callbacks is called for each exported file.

\ `save_cb` is called for all exported files and have the following arguments: `file_path: String`, `file_data: PackedByteArray`, `file_index: int`, `file_count: int`, `encryption_include_filters: PackedStringArray`, `encryption_exclude_filters: PackedStringArray`, `encryption_key: PackedByteArray`.

\ `shared_cb` is called for exported native shared/static libraries and have the following arguments: `file_path: String`, `tags: PackedStringArray`, `target_folder: String`.

\ **Note:** `file_index` and `file_count` are intended for progress tracking only and aren't necessarily unique and precise.


----



[Error<enum_@GlobalScope_Error>] **export_zip**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>], flags\: |bitfield|\[[DebugFlags<enum_EditorExportPlatform_DebugFlags>]\] = 0\ ) [🔗<class_EditorExportPlatform_method_export_zip>]

Create a ZIP archive at `path` for the specified `preset`.


----



[Error<enum_@GlobalScope_Error>] **export_zip_patch**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>], patches\: [PackedStringArray<class_PackedStringArray>] = PackedStringArray(), flags\: |bitfield|\[[DebugFlags<enum_EditorExportPlatform_DebugFlags>]\] = 0\ ) [🔗<class_EditorExportPlatform_method_export_zip_patch>]

Create a patch ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

\ **Note:** `patches` is an optional override of the set of patches defined in the export preset. When empty the patches defined in the export preset will be used instead.


----



[Dictionary<class_Dictionary>] **find_export_template**\ (\ template_file_name\: [String<class_String>]\ ) |const| [🔗<class_EditorExportPlatform_method_find_export_template>]

Locates export template for the platform, and returns [Dictionary<class_Dictionary>] with the following keys: `path: String` and `error: String`. This method is provided for convenience and custom export platforms aren't required to use it or keep export templates stored in the same way official templates are.


----



[PackedStringArray<class_PackedStringArray>] **gen_export_flags**\ (\ flags\: |bitfield|\[[DebugFlags<enum_EditorExportPlatform_DebugFlags>]\]\ ) [🔗<class_EditorExportPlatform_method_gen_export_flags>]

Generates array of command line arguments for the default export templates for the debug flags and editor settings.


----



[Array<class_Array>] **get_current_presets**\ (\ ) |const| [🔗<class_EditorExportPlatform_method_get_current_presets>]

Returns array of [EditorExportPreset<class_EditorExportPreset>]\ s for this platform.


----



[PackedStringArray<class_PackedStringArray>] **get_forced_export_files**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>] = null\ ) |static| [🔗<class_EditorExportPlatform_method_get_forced_export_files>]

Returns array of core file names that always should be exported regardless of preset config.


----



[Dictionary<class_Dictionary>] **get_internal_export_files**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>]\ ) [🔗<class_EditorExportPlatform_method_get_internal_export_files>]

Returns additional files that should always be exported regardless of preset configuration, and are not part of the project source. The returned [Dictionary<class_Dictionary>] contains filename keys ([String<class_String>]) and their corresponding raw data ([PackedByteArray<class_PackedByteArray>]).


----



[String<class_String>] **get_message_category**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_EditorExportPlatform_method_get_message_category>]

Returns the message category for the message with the given `index`.


----



[int<class_int>] **get_message_count**\ (\ ) |const| [🔗<class_EditorExportPlatform_method_get_message_count>]

Returns the number of messages in the export log.


----



[String<class_String>] **get_message_text**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_EditorExportPlatform_method_get_message_text>]

Returns the text for the message with the given `index`.


----



[ExportMessageType<enum_EditorExportPlatform_ExportMessageType>] **get_message_type**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_EditorExportPlatform_method_get_message_type>]

Returns the type for the message with the given `index`.


----



[String<class_String>] **get_os_name**\ (\ ) |const| [🔗<class_EditorExportPlatform_method_get_os_name>]

Returns the name of the export operating system handled by this **EditorExportPlatform** class, as a friendly string. Possible return values are `Windows`, `Linux`, `macOS`, `Android`, `iOS`, and `Web`.


----



[ExportMessageType<enum_EditorExportPlatform_ExportMessageType>] **get_worst_message_type**\ (\ ) |const| [🔗<class_EditorExportPlatform_method_get_worst_message_type>]

Returns most severe message type currently present in the export log.


----



[Dictionary<class_Dictionary>] **save_pack**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>], embed\: [bool<class_bool>] = false\ ) [🔗<class_EditorExportPlatform_method_save_pack>]

Saves PCK archive and returns [Dictionary<class_Dictionary>] with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

If `embed` is `true`, PCK content is appended to the end of `path` file and return [Dictionary<class_Dictionary>] additionally include following keys: `embedded_start: int` (embedded PCK offset) and `embedded_size: int` (embedded PCK size).


----



[Dictionary<class_Dictionary>] **save_pack_patch**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>]\ ) [🔗<class_EditorExportPlatform_method_save_pack_patch>]

Saves patch PCK archive and returns [Dictionary<class_Dictionary>] with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).


----



[Dictionary<class_Dictionary>] **save_zip**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>]\ ) [🔗<class_EditorExportPlatform_method_save_zip>]

Saves ZIP archive and returns [Dictionary<class_Dictionary>] with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).


----



[Dictionary<class_Dictionary>] **save_zip_patch**\ (\ preset\: [EditorExportPreset<class_EditorExportPreset>], debug\: [bool<class_bool>], path\: [String<class_String>]\ ) [🔗<class_EditorExportPlatform_method_save_zip_patch>]

Saves patch ZIP archive and returns [Dictionary<class_Dictionary>] with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).


----



[Error<enum_@GlobalScope_Error>] **ssh_push_to_remote**\ (\ host\: [String<class_String>], port\: [String<class_String>], scp_args\: [PackedStringArray<class_PackedStringArray>], src_file\: [String<class_String>], dst_file\: [String<class_String>]\ ) |const| [🔗<class_EditorExportPlatform_method_ssh_push_to_remote>]

Uploads specified file over SCP protocol to the remote host.


----



[Error<enum_@GlobalScope_Error>] **ssh_run_on_remote**\ (\ host\: [String<class_String>], port\: [String<class_String>], ssh_arg\: [PackedStringArray<class_PackedStringArray>], cmd_args\: [String<class_String>], output\: [Array<class_Array>] = [], port_fwd\: [int<class_int>] = -1\ ) |const| [🔗<class_EditorExportPlatform_method_ssh_run_on_remote>]

Executes specified command on the remote host via SSH protocol and returns command output in the `output`.


----



[int<class_int>] **ssh_run_on_remote_no_wait**\ (\ host\: [String<class_String>], port\: [String<class_String>], ssh_args\: [PackedStringArray<class_PackedStringArray>], cmd_args\: [String<class_String>], port_fwd\: [int<class_int>] = -1\ ) |const| [🔗<class_EditorExportPlatform_method_ssh_run_on_remote_no_wait>]

Executes specified command on the remote host via SSH protocol and returns process ID (on the remote host) without waiting for command to finish.

