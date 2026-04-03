:github_url: hide



# WebRTCDataChannel

**Inherits:** [PacketPeer<class_PacketPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [WebRTCDataChannelExtension<class_WebRTCDataChannelExtension>]

> **CONTAINER**
>
	There is currently no description for this class. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+----------------------------------------------------------------+-------+
> | :ref:`WriteMode<enum_WebRTCDataChannel_WriteMode>` | :ref:`write_mode<class_WebRTCDataChannel_property_write_mode>` | ``1`` |
> +----------------------------------------------------+----------------------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | |void|                                                   | :ref:`close<class_WebRTCDataChannel_method_close>`\ (\ )                                               |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                    | :ref:`get_buffered_amount<class_WebRTCDataChannel_method_get_buffered_amount>`\ (\ ) |const|           |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                    | :ref:`get_id<class_WebRTCDataChannel_method_get_id>`\ (\ ) |const|                                     |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                              | :ref:`get_label<class_WebRTCDataChannel_method_get_label>`\ (\ ) |const|                               |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                    | :ref:`get_max_packet_life_time<class_WebRTCDataChannel_method_get_max_packet_life_time>`\ (\ ) |const| |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                    | :ref:`get_max_retransmits<class_WebRTCDataChannel_method_get_max_retransmits>`\ (\ ) |const|           |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                              | :ref:`get_protocol<class_WebRTCDataChannel_method_get_protocol>`\ (\ ) |const|                         |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`ChannelState<enum_WebRTCDataChannel_ChannelState>` | :ref:`get_ready_state<class_WebRTCDataChannel_method_get_ready_state>`\ (\ ) |const|                   |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`is_negotiated<class_WebRTCDataChannel_method_is_negotiated>`\ (\ ) |const|                       |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`is_ordered<class_WebRTCDataChannel_method_is_ordered>`\ (\ ) |const|                             |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                    | :ref:`poll<class_WebRTCDataChannel_method_poll>`\ (\ )                                                 |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`was_string_packet<class_WebRTCDataChannel_method_was_string_packet>`\ (\ ) |const|               |
> +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **WriteMode**: [🔗<enum_WebRTCDataChannel_WriteMode>]



[WriteMode<enum_WebRTCDataChannel_WriteMode>] **WRITE_MODE_TEXT** = `0`

Tells the channel to send data over this channel as text. An external peer (non-Godot) would receive this as a string.



[WriteMode<enum_WebRTCDataChannel_WriteMode>] **WRITE_MODE_BINARY** = `1`

Tells the channel to send data over this channel as binary. An external peer (non-Godot) would receive this as array buffer or blob.


----



enum **ChannelState**: [🔗<enum_WebRTCDataChannel_ChannelState>]



[ChannelState<enum_WebRTCDataChannel_ChannelState>] **STATE_CONNECTING** = `0`

The channel was created, but it's still trying to connect.



[ChannelState<enum_WebRTCDataChannel_ChannelState>] **STATE_OPEN** = `1`

The channel is currently open, and data can flow over it.



[ChannelState<enum_WebRTCDataChannel_ChannelState>] **STATE_CLOSING** = `2`

The channel is being closed, no new messages will be accepted, but those already in queue will be flushed.



[ChannelState<enum_WebRTCDataChannel_ChannelState>] **STATE_CLOSED** = `3`

The channel was closed, or connection failed.


----


## Property Descriptions



[WriteMode<enum_WebRTCDataChannel_WriteMode>] **write_mode** = `1` [🔗<class_WebRTCDataChannel_property_write_mode>]


- |void| **set_write_mode**\ (\ value\: [WriteMode<enum_WebRTCDataChannel_WriteMode>]\ )
- [WriteMode<enum_WebRTCDataChannel_WriteMode>] **get_write_mode**\ (\ )

The transfer mode to use when sending outgoing packet. Either text or binary.


----


## Method Descriptions



|void| **close**\ (\ ) [🔗<class_WebRTCDataChannel_method_close>]

Closes this data channel, notifying the other peer.


----



[int<class_int>] **get_buffered_amount**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_buffered_amount>]

Returns the number of bytes currently queued to be sent over this channel.


----



[int<class_int>] **get_id**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_id>]

Returns the ID assigned to this channel during creation (or auto-assigned during negotiation).

If the channel is not negotiated out-of-band the ID will only be available after the connection is established (will return `65535` until then).


----



[String<class_String>] **get_label**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_label>]

Returns the label assigned to this channel during creation.


----



[int<class_int>] **get_max_packet_life_time**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_max_packet_life_time>]

Returns the `maxPacketLifeTime` value assigned to this channel during creation.

Will be `65535` if not specified.


----



[int<class_int>] **get_max_retransmits**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_max_retransmits>]

Returns the `maxRetransmits` value assigned to this channel during creation.

Will be `65535` if not specified.


----



[String<class_String>] **get_protocol**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_protocol>]

Returns the sub-protocol assigned to this channel during creation. An empty string if not specified.


----



[ChannelState<enum_WebRTCDataChannel_ChannelState>] **get_ready_state**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_get_ready_state>]

Returns the current state of this channel.


----



[bool<class_bool>] **is_negotiated**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_is_negotiated>]

Returns `true` if this channel was created with out-of-band configuration.


----



[bool<class_bool>] **is_ordered**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_is_ordered>]

Returns `true` if this channel was created with ordering enabled (default).


----



[Error<enum_@GlobalScope_Error>] **poll**\ (\ ) [🔗<class_WebRTCDataChannel_method_poll>]

Reserved, but not used for now.


----



[bool<class_bool>] **was_string_packet**\ (\ ) |const| [🔗<class_WebRTCDataChannel_method_was_string_packet>]

Returns `true` if the last received packet was transferred as text. See [write_mode<class_WebRTCDataChannel_property_write_mode>].

