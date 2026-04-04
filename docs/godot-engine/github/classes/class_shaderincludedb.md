:github_url: hide



# ShaderIncludeDB

**Inherits:** [Object<class_Object>]

Internal database of built in shader include files.


## Description

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`get_built_in_include_file<class_ShaderIncludeDB_method_get_built_in_include_file>`\ (\ filename\: :ref:`String<class_String>`\ ) |static| |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`has_built_in_include_file<class_ShaderIncludeDB_method_has_built_in_include_file>`\ (\ filename\: :ref:`String<class_String>`\ ) |static| |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`list_built_in_include_files<class_ShaderIncludeDB_method_list_built_in_include_files>`\ (\ ) |static|                                     |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[String<class_String>] **get_built_in_include_file**\ (\ filename\: [String<class_String>]\ ) |static| [🔗<class_ShaderIncludeDB_method_get_built_in_include_file>]

Returns the code for the built-in shader fragment. You can also access this in your shader code through `#include "filename"`.


----



[bool<class_bool>] **has_built_in_include_file**\ (\ filename\: [String<class_String>]\ ) |static| [🔗<class_ShaderIncludeDB_method_has_built_in_include_file>]

Returns `true` if an include file with this name exists.


----



[PackedStringArray<class_PackedStringArray>] **list_built_in_include_files**\ (\ ) |static| [🔗<class_ShaderIncludeDB_method_list_built_in_include_files>]

Returns a list of built-in include files that are currently registered.

