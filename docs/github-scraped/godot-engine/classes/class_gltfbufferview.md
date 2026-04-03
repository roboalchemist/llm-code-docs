:github_url: hide



# GLTFBufferView

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a glTF buffer view.


## Description

GLTFBufferView is a data structure representing a glTF `bufferView` that would be found in the `"bufferViews"` array. A buffer is a blob of binary data. A buffer view is a slice of a buffer that can be used to identify and extract data from the buffer.

Most custom uses of buffers only need to use the [buffer<class_GLTFBufferView_property_buffer>], [byte_length<class_GLTFBufferView_property_byte_length>], and [byte_offset<class_GLTFBufferView_property_byte_offset>]. The [byte_stride<class_GLTFBufferView_property_byte_stride>] and [indices<class_GLTFBufferView_property_indices>] properties are for more advanced use cases such as interleaved mesh data encoded for the GPU.


## Tutorials

- [Buffers, BufferViews, and Accessors in Khronos glTF specification ](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)_

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`buffer<class_GLTFBufferView_property_buffer>`                       | ``-1``    |
> +-------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`byte_length<class_GLTFBufferView_property_byte_length>`             | ``0``     |
> +-------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`byte_offset<class_GLTFBufferView_property_byte_offset>`             | ``0``     |
> +-------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`byte_stride<class_GLTFBufferView_property_byte_stride>`             | ``-1``    |
> +-------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`indices<class_GLTFBufferView_property_indices>`                     | ``false`` |
> +-------------------------+---------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`vertex_attributes<class_GLTFBufferView_property_vertex_attributes>` | ``false`` |
> +-------------------------+---------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFBufferView<class_GLTFBufferView>`   | :ref:`from_dictionary<class_GLTFBufferView_method_from_dictionary>`\ (\ dictionary\: :ref:`Dictionary<class_Dictionary>`\ ) |static|     |
> +-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`load_buffer_view_data<class_GLTFBufferView_method_load_buffer_view_data>`\ (\ state\: :ref:`GLTFState<class_GLTFState>`\ ) |const| |
> +-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`           | :ref:`to_dictionary<class_GLTFBufferView_method_to_dictionary>`\ (\ ) |const|                                                            |
> +-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **buffer** = `-1` [🔗<class_GLTFBufferView_property_buffer>]


- |void| **set_buffer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_buffer**\ (\ )

The index of the buffer this buffer view is referencing. If `-1`, this buffer view is not referencing any buffer.


----



[int<class_int>] **byte_length** = `0` [🔗<class_GLTFBufferView_property_byte_length>]


- |void| **set_byte_length**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_byte_length**\ (\ )

The length, in bytes, of this buffer view. If `0`, this buffer view is empty.


----



[int<class_int>] **byte_offset** = `0` [🔗<class_GLTFBufferView_property_byte_offset>]


- |void| **set_byte_offset**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_byte_offset**\ (\ )

The offset, in bytes, from the start of the buffer to the start of this buffer view.


----



[int<class_int>] **byte_stride** = `-1` [🔗<class_GLTFBufferView_property_byte_stride>]


- |void| **set_byte_stride**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_byte_stride**\ (\ )

The stride, in bytes, between interleaved data. If `-1`, this buffer view is not interleaved.


----



[bool<class_bool>] **indices** = `false` [🔗<class_GLTFBufferView_property_indices>]


- |void| **set_indices**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_indices**\ (\ )

`true` if the GLTFBufferView's OpenGL GPU buffer type is an `ELEMENT_ARRAY_BUFFER` used for vertex indices (integer constant `34963`). `false` if the buffer type is any other value. See [Buffers, BufferViews, and Accessors ](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)_ for possible values. This property is set on import and used on export.


----



[bool<class_bool>] **vertex_attributes** = `false` [🔗<class_GLTFBufferView_property_vertex_attributes>]


- |void| **set_vertex_attributes**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_vertex_attributes**\ (\ )

`true` if the GLTFBufferView's OpenGL GPU buffer type is an `ARRAY_BUFFER` used for vertex attributes (integer constant `34962`). `false` if the buffer type is any other value. See [Buffers, BufferViews, and Accessors ](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)_ for possible values. This property is set on import and used on export.


----


## Method Descriptions



[GLTFBufferView<class_GLTFBufferView>] **from_dictionary**\ (\ dictionary\: [Dictionary<class_Dictionary>]\ ) |static| [🔗<class_GLTFBufferView_method_from_dictionary>]

Creates a new GLTFBufferView instance by parsing the given [Dictionary<class_Dictionary>].


----



[PackedByteArray<class_PackedByteArray>] **load_buffer_view_data**\ (\ state\: [GLTFState<class_GLTFState>]\ ) |const| [🔗<class_GLTFBufferView_method_load_buffer_view_data>]

Loads the buffer view data from the buffer referenced by this buffer view in the given [GLTFState<class_GLTFState>]. Interleaved data with a byte stride is not yet supported by this method. The data is returned as a [PackedByteArray<class_PackedByteArray>].


----



[Dictionary<class_Dictionary>] **to_dictionary**\ (\ ) |const| [🔗<class_GLTFBufferView_method_to_dictionary>]

Serializes this GLTFBufferView instance into a [Dictionary<class_Dictionary>].

