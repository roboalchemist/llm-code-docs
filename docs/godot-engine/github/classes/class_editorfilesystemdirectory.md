:github_url: hide



# EditorFileSystemDirectory

**Inherits:** [Object<class_Object>]

A directory for the resource filesystem.


## Description

A more generalized, low-level variation of the directory concept.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`find_dir_index<class_EditorFileSystemDirectory_method_find_dir_index>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                        |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`find_file_index<class_EditorFileSystemDirectory_method_find_file_index>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                      |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_file<class_EditorFileSystemDirectory_method_get_file>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                           |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_file_count<class_EditorFileSystemDirectory_method_get_file_count>`\ (\ ) |const|                                                            |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`get_file_import_is_valid<class_EditorFileSystemDirectory_method_get_file_import_is_valid>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|           |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_file_path<class_EditorFileSystemDirectory_method_get_file_path>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                 |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_file_script_class_extends<class_EditorFileSystemDirectory_method_get_file_script_class_extends>`\ (\ idx\: :ref:`int<class_int>`\ ) |const| |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_file_script_class_name<class_EditorFileSystemDirectory_method_get_file_script_class_name>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|       |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                               | :ref:`get_file_type<class_EditorFileSystemDirectory_method_get_file_type>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                 |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_name<class_EditorFileSystemDirectory_method_get_name>`\ (\ )                                                                                |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` | :ref:`get_parent<class_EditorFileSystemDirectory_method_get_parent>`\ (\ )                                                                            |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`get_path<class_EditorFileSystemDirectory_method_get_path>`\ (\ ) |const|                                                                        |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` | :ref:`get_subdir<class_EditorFileSystemDirectory_method_get_subdir>`\ (\ idx\: :ref:`int<class_int>`\ )                                               |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`get_subdir_count<class_EditorFileSystemDirectory_method_get_subdir_count>`\ (\ ) |const|                                                        |
> +-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **find_dir_index**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_find_dir_index>]

Returns the index of the directory with name `name` or `-1` if not found.


----



[int<class_int>] **find_file_index**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_find_file_index>]

Returns the index of the file with name `name` or `-1` if not found.


----



[String<class_String>] **get_file**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file>]

Returns the name of the file at index `idx`.


----



[int<class_int>] **get_file_count**\ (\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file_count>]

Returns the number of files in this directory.


----



[bool<class_bool>] **get_file_import_is_valid**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file_import_is_valid>]

Returns `true` if the file at index `idx` imported properly.


----



[String<class_String>] **get_file_path**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file_path>]

Returns the path to the file at index `idx`.


----



[String<class_String>] **get_file_script_class_extends**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file_script_class_extends>]

Returns the base class of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.


----



[String<class_String>] **get_file_script_class_name**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file_script_class_name>]

Returns the name of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.


----



[StringName<class_StringName>] **get_file_type**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_file_type>]

Returns the resource type of the file at index `idx`. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.


----



[String<class_String>] **get_name**\ (\ ) [🔗<class_EditorFileSystemDirectory_method_get_name>]

Returns the name of this directory.


----



[EditorFileSystemDirectory<class_EditorFileSystemDirectory>] **get_parent**\ (\ ) [🔗<class_EditorFileSystemDirectory_method_get_parent>]

Returns the parent directory for this directory or `null` if called on a directory at `res://` or `user://`.


----



[String<class_String>] **get_path**\ (\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_path>]

Returns the path to this directory.


----



[EditorFileSystemDirectory<class_EditorFileSystemDirectory>] **get_subdir**\ (\ idx\: [int<class_int>]\ ) [🔗<class_EditorFileSystemDirectory_method_get_subdir>]

Returns the subdirectory at index `idx`.


----



[int<class_int>] **get_subdir_count**\ (\ ) |const| [🔗<class_EditorFileSystemDirectory_method_get_subdir_count>]

Returns the number of subdirectories in this directory.

