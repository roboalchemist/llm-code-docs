:github_url: hide



# StreamPeer

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [StreamPeerBuffer<class_StreamPeerBuffer>], [StreamPeerExtension<class_StreamPeerExtension>], [StreamPeerGZIP<class_StreamPeerGZIP>], [StreamPeerSocket<class_StreamPeerSocket>], [StreamPeerTLS<class_StreamPeerTLS>]

Abstract base class for interacting with streams.


## Description

StreamPeer is an abstract base class mostly used for stream-based protocols (such as TCP). It provides an API for sending and receiving data through streams as raw data or strings.

\ **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`big_endian<class_StreamPeer_property_big_endian>` | ``false`` |
> +-------------------------+---------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_8<class_StreamPeer_method_get_8>`\ (\ )                                                                                            |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_16<class_StreamPeer_method_get_16>`\ (\ )                                                                                          |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_32<class_StreamPeer_method_get_32>`\ (\ )                                                                                          |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_64<class_StreamPeer_method_get_64>`\ (\ )                                                                                          |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_available_bytes<class_StreamPeer_method_get_available_bytes>`\ (\ ) |const|                                                        |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`             | :ref:`get_data<class_StreamPeer_method_get_data>`\ (\ bytes\: :ref:`int<class_int>`\ )                                                       |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`get_double<class_StreamPeer_method_get_double>`\ (\ )                                                                                  |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`get_float<class_StreamPeer_method_get_float>`\ (\ )                                                                                    |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`get_half<class_StreamPeer_method_get_half>`\ (\ )                                                                                      |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`             | :ref:`get_partial_data<class_StreamPeer_method_get_partial_data>`\ (\ bytes\: :ref:`int<class_int>`\ )                                       |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_string<class_StreamPeer_method_get_string>`\ (\ bytes\: :ref:`int<class_int>` = -1\ )                                              |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_u8<class_StreamPeer_method_get_u8>`\ (\ )                                                                                          |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_u16<class_StreamPeer_method_get_u16>`\ (\ )                                                                                        |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_u32<class_StreamPeer_method_get_u32>`\ (\ )                                                                                        |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_u64<class_StreamPeer_method_get_u64>`\ (\ )                                                                                        |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_utf8_string<class_StreamPeer_method_get_utf8_string>`\ (\ bytes\: :ref:`int<class_int>` = -1\ )                                    |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`         | :ref:`get_var<class_StreamPeer_method_get_var>`\ (\ allow_objects\: :ref:`bool<class_bool>` = false\ )                                       |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_8<class_StreamPeer_method_put_8>`\ (\ value\: :ref:`int<class_int>`\ )                                                             |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_16<class_StreamPeer_method_put_16>`\ (\ value\: :ref:`int<class_int>`\ )                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_32<class_StreamPeer_method_put_32>`\ (\ value\: :ref:`int<class_int>`\ )                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_64<class_StreamPeer_method_put_64>`\ (\ value\: :ref:`int<class_int>`\ )                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`put_data<class_StreamPeer_method_put_data>`\ (\ data\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                                |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_double<class_StreamPeer_method_put_double>`\ (\ value\: :ref:`float<class_float>`\ )                                               |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_float<class_StreamPeer_method_put_float>`\ (\ value\: :ref:`float<class_float>`\ )                                                 |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_half<class_StreamPeer_method_put_half>`\ (\ value\: :ref:`float<class_float>`\ )                                                   |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`             | :ref:`put_partial_data<class_StreamPeer_method_put_partial_data>`\ (\ data\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_string<class_StreamPeer_method_put_string>`\ (\ value\: :ref:`String<class_String>`\ )                                             |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_u8<class_StreamPeer_method_put_u8>`\ (\ value\: :ref:`int<class_int>`\ )                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_u16<class_StreamPeer_method_put_u16>`\ (\ value\: :ref:`int<class_int>`\ )                                                         |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_u32<class_StreamPeer_method_put_u32>`\ (\ value\: :ref:`int<class_int>`\ )                                                         |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_u64<class_StreamPeer_method_put_u64>`\ (\ value\: :ref:`int<class_int>`\ )                                                         |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_utf8_string<class_StreamPeer_method_put_utf8_string>`\ (\ value\: :ref:`String<class_String>`\ )                                   |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`put_var<class_StreamPeer_method_put_var>`\ (\ value\: :ref:`Variant<class_Variant>`, full_objects\: :ref:`bool<class_bool>` = false\ ) |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **big_endian** = `false` [🔗<class_StreamPeer_property_big_endian>]


- |void| **set_big_endian**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_big_endian_enabled**\ (\ )

If `true`, this **StreamPeer** will using big-endian format for encoding and decoding.


----


## Method Descriptions



[int<class_int>] **get_8**\ (\ ) [🔗<class_StreamPeer_method_get_8>]

Gets a signed byte from the stream.


----



[int<class_int>] **get_16**\ (\ ) [🔗<class_StreamPeer_method_get_16>]

Gets a signed 16-bit value from the stream.


----



[int<class_int>] **get_32**\ (\ ) [🔗<class_StreamPeer_method_get_32>]

Gets a signed 32-bit value from the stream.


----



[int<class_int>] **get_64**\ (\ ) [🔗<class_StreamPeer_method_get_64>]

Gets a signed 64-bit value from the stream.


----



[int<class_int>] **get_available_bytes**\ (\ ) |const| [🔗<class_StreamPeer_method_get_available_bytes>]

Returns the number of bytes this **StreamPeer** has available.


----



[Array<class_Array>] **get_data**\ (\ bytes\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_get_data>]

Returns a chunk data with the received bytes, as an [Array<class_Array>] containing two elements: an [Error<enum_@GlobalScope_Error>] constant and a [PackedByteArray<class_PackedByteArray>]. `bytes` is the number of bytes to be received. If not enough bytes are available, the function will block until the desired amount is received.


----



[float<class_float>] **get_double**\ (\ ) [🔗<class_StreamPeer_method_get_double>]

Gets a double-precision float from the stream.


----



[float<class_float>] **get_float**\ (\ ) [🔗<class_StreamPeer_method_get_float>]

Gets a single-precision float from the stream.


----



[float<class_float>] **get_half**\ (\ ) [🔗<class_StreamPeer_method_get_half>]

Gets a half-precision float from the stream.


----



[Array<class_Array>] **get_partial_data**\ (\ bytes\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_get_partial_data>]

Returns a chunk data with the received bytes, as an [Array<class_Array>] containing two elements: an [Error<enum_@GlobalScope_Error>] constant and a [PackedByteArray<class_PackedByteArray>]. `bytes` is the number of bytes to be received. If not enough bytes are available, the function will return how many were actually received.


----



[String<class_String>] **get_string**\ (\ bytes\: [int<class_int>] = -1\ ) [🔗<class_StreamPeer_method_get_string>]

Gets an ASCII string with byte-length `bytes` from the stream. If `bytes` is negative (default) the length will be read from the stream using the reverse process of [put_string()<class_StreamPeer_method_put_string>].


----



[int<class_int>] **get_u8**\ (\ ) [🔗<class_StreamPeer_method_get_u8>]

Gets an unsigned byte from the stream.


----



[int<class_int>] **get_u16**\ (\ ) [🔗<class_StreamPeer_method_get_u16>]

Gets an unsigned 16-bit value from the stream.


----



[int<class_int>] **get_u32**\ (\ ) [🔗<class_StreamPeer_method_get_u32>]

Gets an unsigned 32-bit value from the stream.


----



[int<class_int>] **get_u64**\ (\ ) [🔗<class_StreamPeer_method_get_u64>]

Gets an unsigned 64-bit value from the stream.


----



[String<class_String>] **get_utf8_string**\ (\ bytes\: [int<class_int>] = -1\ ) [🔗<class_StreamPeer_method_get_utf8_string>]

Gets a UTF-8 string with byte-length `bytes` from the stream (this decodes the string sent as UTF-8). If `bytes` is negative (default) the length will be read from the stream using the reverse process of [put_utf8_string()<class_StreamPeer_method_put_utf8_string>].


----



[Variant<class_Variant>] **get_var**\ (\ allow_objects\: [bool<class_bool>] = false\ ) [🔗<class_StreamPeer_method_get_var>]

Gets a Variant from the stream. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the [@GlobalScope.bytes_to_var()<class_@GlobalScope_method_bytes_to_var>] method.

\ **Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.


----



|void| **put_8**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_8>]

Puts a signed byte into the stream.


----



|void| **put_16**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_16>]

Puts a signed 16-bit value into the stream.


----



|void| **put_32**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_32>]

Puts a signed 32-bit value into the stream.


----



|void| **put_64**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_64>]

Puts a signed 64-bit value into the stream.


----



[Error<enum_@GlobalScope_Error>] **put_data**\ (\ data\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_StreamPeer_method_put_data>]

Sends a chunk of data through the connection, blocking if necessary until the data is done sending. This function returns an [Error<enum_@GlobalScope_Error>] code.


----



|void| **put_double**\ (\ value\: [float<class_float>]\ ) [🔗<class_StreamPeer_method_put_double>]

Puts a double-precision float into the stream.


----



|void| **put_float**\ (\ value\: [float<class_float>]\ ) [🔗<class_StreamPeer_method_put_float>]

Puts a single-precision float into the stream.


----



|void| **put_half**\ (\ value\: [float<class_float>]\ ) [🔗<class_StreamPeer_method_put_half>]

Puts a half-precision float into the stream.


----



[Array<class_Array>] **put_partial_data**\ (\ data\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_StreamPeer_method_put_partial_data>]

Sends a chunk of data through the connection. If all the data could not be sent at once, only part of it will. This function returns two values, an [Error<enum_@GlobalScope_Error>] code and an integer, describing how much data was actually sent.


----



|void| **put_string**\ (\ value\: [String<class_String>]\ ) [🔗<class_StreamPeer_method_put_string>]

Puts a zero-terminated ASCII string into the stream prepended by a 32-bit unsigned integer representing its size.

\ **Note:** To put an ASCII string without prepending its size, you can use [put_data()<class_StreamPeer_method_put_data>]:


> **TABS**
>

    put_data("Hello world".to_ascii_buffer())


    PutData("Hello World".ToAsciiBuffer());




----



|void| **put_u8**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_u8>]

Puts an unsigned byte into the stream.


----



|void| **put_u16**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_u16>]

Puts an unsigned 16-bit value into the stream.


----



|void| **put_u32**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_u32>]

Puts an unsigned 32-bit value into the stream.


----



|void| **put_u64**\ (\ value\: [int<class_int>]\ ) [🔗<class_StreamPeer_method_put_u64>]

Puts an unsigned 64-bit value into the stream.


----



|void| **put_utf8_string**\ (\ value\: [String<class_String>]\ ) [🔗<class_StreamPeer_method_put_utf8_string>]

Puts a zero-terminated UTF-8 string into the stream prepended by a 32 bits unsigned integer representing its size.

\ **Note:** To put a UTF-8 string without prepending its size, you can use [put_data()<class_StreamPeer_method_put_data>]:


> **TABS**
>

    put_data("Hello world".to_utf8_buffer())


    PutData("Hello World".ToUtf8Buffer());




----



|void| **put_var**\ (\ value\: [Variant<class_Variant>], full_objects\: [bool<class_bool>] = false\ ) [🔗<class_StreamPeer_method_put_var>]

Puts a Variant into the stream. If `full_objects` is `true` encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the [@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>] method.

