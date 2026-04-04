:github_url: hide



# EditorFileSystemImportFormatSupportQuery

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Used to query and configure import format support.


## Description

This class is used to query and configure a certain import format. It is used in conjunction with asset format import plugins.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`_get_file_extensions<class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions>`\ (\ ) |virtual| |required| |const| |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`_is_active<class_EditorFileSystemImportFormatSupportQuery_private_method__is_active>`\ (\ ) |virtual| |required| |const|                     |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`_query<class_EditorFileSystemImportFormatSupportQuery_private_method__query>`\ (\ ) |virtual| |required| |const|                             |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[PackedStringArray<class_PackedStringArray>] **_get_file_extensions**\ (\ ) |virtual| |required| |const| [🔗<class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions>]

Return the file extensions supported.


----



[bool<class_bool>] **_is_active**\ (\ ) |virtual| |required| |const| [🔗<class_EditorFileSystemImportFormatSupportQuery_private_method__is_active>]

Return whether this importer is active.


----



[bool<class_bool>] **_query**\ (\ ) |virtual| |required| |const| [🔗<class_EditorFileSystemImportFormatSupportQuery_private_method__query>]

Query support. Return `false` if import must not continue.

