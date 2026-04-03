:github_url: hide



# StreamPeerBuffer

**Inherits:** [StreamPeer<class_StreamPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A stream peer used to handle binary data streams.


## Description

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, [FileAccess<class_FileAccess>] can be used directly.

A **StreamPeerBuffer** object keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`data_array<class_StreamPeerBuffer_property_data_array>` | ``PackedByteArray()`` |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`clear<class_StreamPeerBuffer_method_clear>`\ (\ )                                 |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`StreamPeerBuffer<class_StreamPeerBuffer>` | :ref:`duplicate<class_StreamPeerBuffer_method_duplicate>`\ (\ ) |const|                 |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`get_position<class_StreamPeerBuffer_method_get_position>`\ (\ ) |const|           |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`get_size<class_StreamPeerBuffer_method_get_size>`\ (\ ) |const|                   |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`resize<class_StreamPeerBuffer_method_resize>`\ (\ size\: :ref:`int<class_int>`\ ) |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`seek<class_StreamPeerBuffer_method_seek>`\ (\ position\: :ref:`int<class_int>`\ ) |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedByteArray<class_PackedByteArray>] **data_array** = `PackedByteArray()` [🔗<class_StreamPeerBuffer_property_data_array>]


- |void| **set_data_array**\ (\ value\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_data_array**\ (\ )

The underlying data buffer. Setting this value resets the cursor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----


## Method Descriptions



|void| **clear**\ (\ ) [🔗<class_StreamPeerBuffer_method_clear>]

Clears the [data_array<class_StreamPeerBuffer_property_data_array>] and resets the cursor.


----



[StreamPeerBuffer<class_StreamPeerBuffer>] **duplicate**\ (\ ) |const| [🔗<class_StreamPeerBuffer_method_duplicate>]

Returns a new **StreamPeerBuffer** with the same [data_array<class_StreamPeerBuffer_property_data_array>] content.


----



[int<class_int>] **get_position**\ (\ ) |const| [🔗<class_StreamPeerBuffer_method_get_position>]

Returns the current cursor position.


----



[int<class_int>] **get_size**\ (\ ) |const| [🔗<class_StreamPeerBuffer_method_get_size>]

Returns the size of [data_array<class_StreamPeerBuffer_property_data_array>].


----



|void| **resize**\ (\ size\: [int<class_int>]\ ) [🔗<class_StreamPeerBuffer_method_resize>]

Resizes the [data_array<class_StreamPeerBuffer_property_data_array>]. This *doesn't* update the cursor.


----



|void| **seek**\ (\ position\: [int<class_int>]\ ) [🔗<class_StreamPeerBuffer_method_seek>]

Moves the cursor to the specified position. `position` must be a valid index of [data_array<class_StreamPeerBuffer_property_data_array>].

