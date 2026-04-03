:github_url: hide



# PacketPeer

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [ENetPacketPeer<class_ENetPacketPeer>], [MultiplayerPeer<class_MultiplayerPeer>], [PacketPeerDTLS<class_PacketPeerDTLS>], [PacketPeerExtension<class_PacketPeerExtension>], [PacketPeerStream<class_PacketPeerStream>], [PacketPeerUDP<class_PacketPeerUDP>], [WebRTCDataChannel<class_WebRTCDataChannel>], [WebSocketPeer<class_WebSocketPeer>]

Abstraction and base class for packet-based protocols.


## Description

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low-level bytes or having to worry about network ordering.

\ **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+---------------------------------------------------------------------------------+-------------+
> | :ref:`int<class_int>` | :ref:`encode_buffer_max_size<class_PacketPeer_property_encode_buffer_max_size>` | ``8388608`` |
> +-----------------------+---------------------------------------------------------------------------------+-------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                         | :ref:`get_available_packet_count<class_PacketPeer_method_get_available_packet_count>`\ (\ ) |const|                                        |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`get_packet<class_PacketPeer_method_get_packet>`\ (\ )                                                                                |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`         | :ref:`get_packet_error<class_PacketPeer_method_get_packet_error>`\ (\ ) |const|                                                            |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                 | :ref:`get_var<class_PacketPeer_method_get_var>`\ (\ allow_objects\: :ref:`bool<class_bool>` = false\ )                                     |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`         | :ref:`put_packet<class_PacketPeer_method_put_packet>`\ (\ buffer\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                        |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`         | :ref:`put_var<class_PacketPeer_method_put_var>`\ (\ var\: :ref:`Variant<class_Variant>`, full_objects\: :ref:`bool<class_bool>` = false\ ) |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **encode_buffer_max_size** = `8388608` [🔗<class_PacketPeer_property_encode_buffer_max_size>]


- |void| **set_encode_buffer_max_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_encode_buffer_max_size**\ (\ )

Maximum buffer size allowed when encoding [Variant<class_Variant>]\ s. Raise this value to support heavier memory allocations.

The [put_var()<class_PacketPeer_method_put_var>] method allocates memory on the stack, and the buffer used will grow automatically to the closest power of two to match the size of the [Variant<class_Variant>]. If the [Variant<class_Variant>] is bigger than [encode_buffer_max_size<class_PacketPeer_property_encode_buffer_max_size>], the method will error out with [@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>].


----


## Method Descriptions



[int<class_int>] **get_available_packet_count**\ (\ ) |const| [🔗<class_PacketPeer_method_get_available_packet_count>]

Returns the number of packets currently available in the ring-buffer.


----



[PackedByteArray<class_PackedByteArray>] **get_packet**\ (\ ) [🔗<class_PacketPeer_method_get_packet>]

Gets a raw packet.


----



[Error<enum_@GlobalScope_Error>] **get_packet_error**\ (\ ) |const| [🔗<class_PacketPeer_method_get_packet_error>]

Returns the error state of the last packet received (via [get_packet()<class_PacketPeer_method_get_packet>] and [get_var()<class_PacketPeer_method_get_var>]).


----



[Variant<class_Variant>] **get_var**\ (\ allow_objects\: [bool<class_bool>] = false\ ) [🔗<class_PacketPeer_method_get_var>]

Gets a Variant. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the [@GlobalScope.bytes_to_var()<class_@GlobalScope_method_bytes_to_var>] method.

\ **Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.


----



[Error<enum_@GlobalScope_Error>] **put_packet**\ (\ buffer\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_PacketPeer_method_put_packet>]

Sends a raw packet.


----



[Error<enum_@GlobalScope_Error>] **put_var**\ (\ var\: [Variant<class_Variant>], full_objects\: [bool<class_bool>] = false\ ) [🔗<class_PacketPeer_method_put_var>]

Sends a [Variant<class_Variant>] as a packet. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the [@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>] method.

