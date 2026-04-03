:github_url: hide



# ZIPReader

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Allows reading the content of a ZIP file.


## Description

This class implements a reader that can extract the content of individual files inside a ZIP archive. See also [ZIPPacker<class_ZIPPacker>].

::

    # Read a single file from a ZIP archive.
    func read_zip_file():
        var reader = ZIPReader.new()
        var err = reader.open("user://archive.zip")
        if err != OK:
            return PackedByteArray()
        var res = reader.read_file("hello.txt")
        reader.close()
        return res

    # Extract all files from a ZIP archive, preserving the directories within.
    # This acts like the "Extract all" functionality from most archive managers.
    func extract_all_from_zip():
        var reader = ZIPReader.new()
        reader.open("res://archive.zip")

        # Destination directory for the extracted files (this folder must exist before extraction).
        # Not all ZIP archives put everything in a single root folder,
        # which means several files/folders may be created in `root_dir` after extraction.
        var root_dir = DirAccess.open("user://")

        var files = reader.get_files()
        for file_path in files:
            # If the current entry is a directory.
            if file_path.ends_with("/"):
                root_dir.make_dir_recursive(file_path)
                continue

            # Write file contents, creating folders automatically when needed.
            # Not all ZIP archives are strictly ordered, so we need to do this in case
            # the file entry comes before the folder entry.
            root_dir.make_dir_recursive(root_dir.get_current_dir().path_join(file_path).get_base_dir())
            var file = FileAccess.open(root_dir.get_current_dir().path_join(file_path), FileAccess.WRITE)
            var buffer = reader.read_file(file_path)
            file.store_buffer(buffer)


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`             | :ref:`close<class_ZIPReader_method_close>`\ (\ )                                                                                                                      |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`file_exists<class_ZIPReader_method_file_exists>`\ (\ path\: :ref:`String<class_String>`, case_sensitive\: :ref:`bool<class_bool>` = true\ )                     |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_compression_level<class_ZIPReader_method_get_compression_level>`\ (\ path\: :ref:`String<class_String>`, case_sensitive\: :ref:`bool<class_bool>` = true\ ) |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_files<class_ZIPReader_method_get_files>`\ (\ )                                                                                                              |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`             | :ref:`open<class_ZIPReader_method_open>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                    |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`     | :ref:`read_file<class_ZIPReader_method_read_file>`\ (\ path\: :ref:`String<class_String>`, case_sensitive\: :ref:`bool<class_bool>` = true\ )                         |
> +---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **close**\ (\ ) [🔗<class_ZIPReader_method_close>]

Closes the underlying resources used by this instance.


----



[bool<class_bool>] **file_exists**\ (\ path\: [String<class_String>], case_sensitive\: [bool<class_bool>] = true\ ) [🔗<class_ZIPReader_method_file_exists>]

Returns `true` if the file exists in the loaded zip archive.

Must be called after [open()<class_ZIPReader_method_open>].


----



[int<class_int>] **get_compression_level**\ (\ path\: [String<class_String>], case_sensitive\: [bool<class_bool>] = true\ ) [🔗<class_ZIPReader_method_get_compression_level>]

Returns the compression level of the file in the loaded zip archive. Returns `-1` if the file doesn't exist or any other error occurs. Must be called after [open()<class_ZIPReader_method_open>].


----



[PackedStringArray<class_PackedStringArray>] **get_files**\ (\ ) [🔗<class_ZIPReader_method_get_files>]

Returns the list of names of all files in the loaded archive.

Must be called after [open()<class_ZIPReader_method_open>].


----



[Error<enum_@GlobalScope_Error>] **open**\ (\ path\: [String<class_String>]\ ) [🔗<class_ZIPReader_method_open>]

Opens the zip archive at the given `path` and reads its file index.


----



[PackedByteArray<class_PackedByteArray>] **read_file**\ (\ path\: [String<class_String>], case_sensitive\: [bool<class_bool>] = true\ ) [🔗<class_ZIPReader_method_read_file>]

Loads the whole content of a file in the loaded zip archive into memory and returns it.

Must be called after [open()<class_ZIPReader_method_open>].

