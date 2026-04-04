:github_url: hide



# ZIPPacker

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Allows the creation of ZIP files.


## Description

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also [ZIPReader<class_ZIPReader>] and [PCKPacker<class_PCKPacker>].

::

    # Create a ZIP archive with a single file at its root.
    func write_zip_file():
        var writer = ZIPPacker.new()
        var err = writer.open("user://archive.zip")
        if err != OK:
            return err
        writer.start_file("hello.txt")
        writer.write_file("Hello World".to_utf8_buffer())
        writer.close_file()

        writer.close()
        return OK


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+----------------------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`compression_level<class_ZIPPacker_property_compression_level>` | ``-1`` |
> +-----------------------+----------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`close<class_ZIPPacker_method_close>`\ (\ )                                                                                            |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`close_file<class_ZIPPacker_method_close_file>`\ (\ )                                                                                  |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`open<class_ZIPPacker_method_open>`\ (\ path\: :ref:`String<class_String>`, append\: :ref:`ZipAppend<enum_ZIPPacker_ZipAppend>` = 0\ ) |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`start_file<class_ZIPPacker_method_start_file>`\ (\ path\: :ref:`String<class_String>`\ )                                              |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`write_file<class_ZIPPacker_method_write_file>`\ (\ data\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                            |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ZipAppend**: [🔗<enum_ZIPPacker_ZipAppend>]



[ZipAppend<enum_ZIPPacker_ZipAppend>] **APPEND_CREATE** = `0`

Create a new zip archive at the given path.



[ZipAppend<enum_ZIPPacker_ZipAppend>] **APPEND_CREATEAFTER** = `1`

Append a new zip archive to the end of the already existing file at the given path.



[ZipAppend<enum_ZIPPacker_ZipAppend>] **APPEND_ADDINZIP** = `2`

Add new files to the existing zip archive at the given path.


----



enum **CompressionLevel**: [🔗<enum_ZIPPacker_CompressionLevel>]



[CompressionLevel<enum_ZIPPacker_CompressionLevel>] **COMPRESSION_DEFAULT** = `-1`

Start a file with the default Deflate compression level (`6`). This is a good compromise between speed and file size.



[CompressionLevel<enum_ZIPPacker_CompressionLevel>] **COMPRESSION_NONE** = `0`

Start a file with no compression. This is also known as the "Store" compression mode and is the fastest method of packing files inside a ZIP archive. Consider using this mode for files that are already compressed (such as JPEG, PNG, MP3, or Ogg Vorbis files).



[CompressionLevel<enum_ZIPPacker_CompressionLevel>] **COMPRESSION_FAST** = `1`

Start a file with the fastest Deflate compression level (`1`). This is fast to compress, but results in larger file sizes than [COMPRESSION_DEFAULT<class_ZIPPacker_constant_COMPRESSION_DEFAULT>]. Decompression speed is generally unaffected by the chosen compression level.



[CompressionLevel<enum_ZIPPacker_CompressionLevel>] **COMPRESSION_BEST** = `9`

Start a file with the best Deflate compression level (`9`). This is slow to compress, but results in smaller file sizes than [COMPRESSION_DEFAULT<class_ZIPPacker_constant_COMPRESSION_DEFAULT>]. Decompression speed is generally unaffected by the chosen compression level.


----


## Property Descriptions



[int<class_int>] **compression_level** = `-1` [🔗<class_ZIPPacker_property_compression_level>]


- |void| **set_compression_level**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_compression_level**\ (\ )

The compression level used when [start_file()<class_ZIPPacker_method_start_file>] is called. Use [CompressionLevel<enum_ZIPPacker_CompressionLevel>] as a reference.


----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **close**\ (\ ) [🔗<class_ZIPPacker_method_close>]

Closes the underlying resources used by this instance.


----



[Error<enum_@GlobalScope_Error>] **close_file**\ (\ ) [🔗<class_ZIPPacker_method_close_file>]

Stops writing to a file within the archive.

It will fail if there is no open file.


----



[Error<enum_@GlobalScope_Error>] **open**\ (\ path\: [String<class_String>], append\: [ZipAppend<enum_ZIPPacker_ZipAppend>] = 0\ ) [🔗<class_ZIPPacker_method_open>]

Opens a zip file for writing at the given path using the specified write mode.

This must be called before everything else.


----



[Error<enum_@GlobalScope_Error>] **start_file**\ (\ path\: [String<class_String>]\ ) [🔗<class_ZIPPacker_method_start_file>]

Starts writing to a file within the archive. Only one file can be written at the same time.

Must be called after [open()<class_ZIPPacker_method_open>].


----



[Error<enum_@GlobalScope_Error>] **write_file**\ (\ data\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_ZIPPacker_method_write_file>]

Write the given `data` to the file.

Needs to be called after [start_file()<class_ZIPPacker_method_start_file>].

