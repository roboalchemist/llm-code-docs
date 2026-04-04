:github_url: hide



# PCKPacker

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Creates packages that can be loaded into a running project.


## Description

The **PCKPacker** is used to create packages that can be loaded into a running project using [ProjectSettings.load_resource_pack()<class_ProjectSettings_method_load_resource_pack>].


> **TABS**
>

    var packer = PCKPacker.new()
    packer.pck_start("test.pck")
    packer.add_file("res://text.txt", "text.txt")
    packer.flush()


    var packer = new PckPacker();
    packer.PckStart("test.pck");
    packer.AddFile("res://text.txt", "text.txt");
    packer.Flush();



The above **PCKPacker** creates package `test.pck`, then adds a file named `text.txt` at the root of the package.

\ **Note:** PCK is Godot's own pack file format. To create ZIP archives that can be read by any program, use [ZIPPacker<class_ZIPPacker>] instead.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`add_file<class_PCKPacker_method_add_file>`\ (\ target_path\: :ref:`String<class_String>`, source_path\: :ref:`String<class_String>`, encrypt\: :ref:`bool<class_bool>` = false\ )                                                                                                               |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`add_file_removal<class_PCKPacker_method_add_file_removal>`\ (\ target_path\: :ref:`String<class_String>`\ )                                                                                                                                                                                     |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`flush<class_PCKPacker_method_flush>`\ (\ verbose\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                           |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`pck_start<class_PCKPacker_method_pck_start>`\ (\ pck_path\: :ref:`String<class_String>`, alignment\: :ref:`int<class_int>` = 32, key\: :ref:`String<class_String>` = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory\: :ref:`bool<class_bool>` = false\ ) |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **add_file**\ (\ target_path\: [String<class_String>], source_path\: [String<class_String>], encrypt\: [bool<class_bool>] = false\ ) [🔗<class_PCKPacker_method_add_file>]

Adds the `source_path` file to the current PCK package at the `target_path` internal path. The `res://` prefix for `target_path` is optional and stripped internally. File content is immediately written to the PCK.


----



[Error<enum_@GlobalScope_Error>] **add_file_removal**\ (\ target_path\: [String<class_String>]\ ) [🔗<class_PCKPacker_method_add_file_removal>]

Registers a file removal of the `target_path` internal path to the PCK. This is mainly used for patches. If the file at this path has been loaded from a previous PCK, it will be removed. The `res://` prefix for `target_path` is optional and stripped internally.


----



[Error<enum_@GlobalScope_Error>] **flush**\ (\ verbose\: [bool<class_bool>] = false\ ) [🔗<class_PCKPacker_method_flush>]

Writes the file directory and closes the PCK. If `verbose` is `true`, a list of files added will be printed to the console for easier debugging.

\ **Note:** **PCKPacker** will automatically flush when it's freed, which happens when it goes out of scope or when it gets assigned with `null`. In C# the reference must be disposed after use, either with the `using` statement or by calling the `Dispose` method directly.


----



[Error<enum_@GlobalScope_Error>] **pck_start**\ (\ pck_path\: [String<class_String>], alignment\: [int<class_int>] = 32, key\: [String<class_String>] = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory\: [bool<class_bool>] = false\ ) [🔗<class_PCKPacker_method_pck_start>]

Creates a new PCK file at the file path `pck_path`. The `.pck` file extension isn't added automatically, so it should be part of `pck_path` (even though it's not required).

