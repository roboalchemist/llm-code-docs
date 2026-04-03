:github_url: hide



# EditorFileSystem

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

Resource filesystem, as the editor sees it.


## Description

This object holds information of all resources in the filesystem, their types, etc.

\ **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_filesystem()<class_EditorInterface_method_get_resource_filesystem>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_file_type<class_EditorFileSystem_method_get_file_type>`\ (\ path\: :ref:`String<class_String>`\ ) |const|                  |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` | :ref:`get_filesystem<class_EditorFileSystem_method_get_filesystem>`\ (\ )                                                            |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` | :ref:`get_filesystem_path<class_EditorFileSystem_method_get_filesystem_path>`\ (\ path\: :ref:`String<class_String>`\ )              |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                         | :ref:`get_scanning_progress<class_EditorFileSystem_method_get_scanning_progress>`\ (\ ) |const|                                      |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`is_scanning<class_EditorFileSystem_method_is_scanning>`\ (\ ) |const|                                                          |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`reimport_files<class_EditorFileSystem_method_reimport_files>`\ (\ files\: :ref:`PackedStringArray<class_PackedStringArray>`\ ) |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`scan<class_EditorFileSystem_method_scan>`\ (\ )                                                                                |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`scan_sources<class_EditorFileSystem_method_scan_sources>`\ (\ )                                                                |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`update_file<class_EditorFileSystem_method_update_file>`\ (\ path\: :ref:`String<class_String>`\ )                              |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**filesystem_changed**\ (\ ) [🔗<class_EditorFileSystem_signal_filesystem_changed>]

Emitted if the filesystem changed.


----



**resources_reimported**\ (\ resources\: [PackedStringArray<class_PackedStringArray>]\ ) [🔗<class_EditorFileSystem_signal_resources_reimported>]

Emitted if a resource is reimported.


----



**resources_reimporting**\ (\ resources\: [PackedStringArray<class_PackedStringArray>]\ ) [🔗<class_EditorFileSystem_signal_resources_reimporting>]

Emitted before a resource is reimported.


----



**resources_reload**\ (\ resources\: [PackedStringArray<class_PackedStringArray>]\ ) [🔗<class_EditorFileSystem_signal_resources_reload>]

Emitted if at least one resource is reloaded when the filesystem is scanned.


----



**script_classes_updated**\ (\ ) [🔗<class_EditorFileSystem_signal_script_classes_updated>]

Emitted when the list of global script classes gets updated.


----



**sources_changed**\ (\ exist\: [bool<class_bool>]\ ) [🔗<class_EditorFileSystem_signal_sources_changed>]

Emitted if the source of any imported file changed.


----


## Method Descriptions



[String<class_String>] **get_file_type**\ (\ path\: [String<class_String>]\ ) |const| [🔗<class_EditorFileSystem_method_get_file_type>]

Returns the resource type of the file, given the full path. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.


----



[EditorFileSystemDirectory<class_EditorFileSystemDirectory>] **get_filesystem**\ (\ ) [🔗<class_EditorFileSystem_method_get_filesystem>]

Gets the root directory object.


----



[EditorFileSystemDirectory<class_EditorFileSystemDirectory>] **get_filesystem_path**\ (\ path\: [String<class_String>]\ ) [🔗<class_EditorFileSystem_method_get_filesystem_path>]

Returns a view into the filesystem at `path`.


----



[float<class_float>] **get_scanning_progress**\ (\ ) |const| [🔗<class_EditorFileSystem_method_get_scanning_progress>]

Returns the scan progress for 0 to 1 if the FS is being scanned.


----



[bool<class_bool>] **is_scanning**\ (\ ) |const| [🔗<class_EditorFileSystem_method_is_scanning>]

Returns `true` if the filesystem is being scanned.


----



|void| **reimport_files**\ (\ files\: [PackedStringArray<class_PackedStringArray>]\ ) [🔗<class_EditorFileSystem_method_reimport_files>]

Reimports a set of files. Call this if these files or their `.import` files were directly edited by script or an external program.

If the file type changed or the file was newly created, use [update_file()<class_EditorFileSystem_method_update_file>] or [scan()<class_EditorFileSystem_method_scan>].

\ **Note:** This function blocks until the import is finished. However, the main loop iteration, including timers and [Node._process()<class_Node_private_method__process>], will occur during the import process due to progress bar updates. Avoid calls to [reimport_files()<class_EditorFileSystem_method_reimport_files>] or [scan()<class_EditorFileSystem_method_scan>] while an import is in progress.


----



|void| **scan**\ (\ ) [🔗<class_EditorFileSystem_method_scan>]

Scan the filesystem for changes.


----



|void| **scan_sources**\ (\ ) [🔗<class_EditorFileSystem_method_scan_sources>]

Check if the source of any imported resource changed.


----



|void| **update_file**\ (\ path\: [String<class_String>]\ ) [🔗<class_EditorFileSystem_method_update_file>]

Add a file in an existing directory, or schedule file information to be updated on editor restart. Can be used to update text files saved by an external program.

This will not import the file. To reimport, call [reimport_files()<class_EditorFileSystem_method_reimport_files>] or [scan()<class_EditorFileSystem_method_scan>] methods.

