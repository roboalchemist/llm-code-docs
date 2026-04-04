:github_url: hide

> **META**
	:keywords: network



# MultiplayerPeerExtension

**Inherits:** [MultiplayerPeer<class_MultiplayerPeer>] **<** [PacketPeer<class_PacketPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Class that can be inherited to implement custom multiplayer API networking layers via GDExtension.


## Description

This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods below **must** be implemented to have a working custom multiplayer implementation. See also [MultiplayerAPI<class_MultiplayerAPI>].


## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_close<class_MultiplayerPeerExtension_private_method__close>`\ (\ ) |virtual| |required|                                                                                          |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_disconnect_peer<class_MultiplayerPeerExtension_private_method__disconnect_peer>`\ (\ p_peer\: :ref:`int<class_int>`, p_force\: :ref:`bool<class_bool>`\ ) |virtual| |required|   |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                          | :ref:`_get_available_packet_count<class_MultiplayerPeerExtension_private_method__get_available_packet_count>`\ (\ ) |virtual| |required| |const|                                        |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>` | :ref:`_get_connection_status<class_MultiplayerPeerExtension_private_method__get_connection_status>`\ (\ ) |virtual| |required| |const|                                                  |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                          | :ref:`_get_max_packet_size<class_MultiplayerPeerExtension_private_method__get_max_packet_size>`\ (\ ) |virtual| |required| |const|                                                      |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                          | :ref:`_get_packet<class_MultiplayerPeerExtension_private_method__get_packet>`\ (\ r_buffer\: ``const uint8_t **``, r_buffer_size\: ``int32_t*``\ ) |virtual|                            |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                          | :ref:`_get_packet_channel<class_MultiplayerPeerExtension_private_method__get_packet_channel>`\ (\ ) |virtual| |required| |const|                                                        |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TransferMode<enum_MultiplayerPeer_TransferMode>`         | :ref:`_get_packet_mode<class_MultiplayerPeerExtension_private_method__get_packet_mode>`\ (\ ) |virtual| |required| |const|                                                              |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                          | :ref:`_get_packet_peer<class_MultiplayerPeerExtension_private_method__get_packet_peer>`\ (\ ) |virtual| |required| |const|                                                              |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`                  | :ref:`_get_packet_script<class_MultiplayerPeerExtension_private_method__get_packet_script>`\ (\ ) |virtual|                                                                             |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                          | :ref:`_get_transfer_channel<class_MultiplayerPeerExtension_private_method__get_transfer_channel>`\ (\ ) |virtual| |required| |const|                                                    |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TransferMode<enum_MultiplayerPeer_TransferMode>`         | :ref:`_get_transfer_mode<class_MultiplayerPeerExtension_private_method__get_transfer_mode>`\ (\ ) |virtual| |required| |const|                                                          |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                          | :ref:`_get_unique_id<class_MultiplayerPeerExtension_private_method__get_unique_id>`\ (\ ) |virtual| |required| |const|                                                                  |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                        | :ref:`_is_refusing_new_connections<class_MultiplayerPeerExtension_private_method__is_refusing_new_connections>`\ (\ ) |virtual| |const|                                                 |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                        | :ref:`_is_server<class_MultiplayerPeerExtension_private_method__is_server>`\ (\ ) |virtual| |required| |const|                                                                          |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                        | :ref:`_is_server_relay_supported<class_MultiplayerPeerExtension_private_method__is_server_relay_supported>`\ (\ ) |virtual| |const|                                                     |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_poll<class_MultiplayerPeerExtension_private_method__poll>`\ (\ ) |virtual| |required|                                                                                            |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                          | :ref:`_put_packet<class_MultiplayerPeerExtension_private_method__put_packet>`\ (\ p_buffer\: ``const uint8_t*``, p_buffer_size\: :ref:`int<class_int>`\ ) |virtual|                     |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                          | :ref:`_put_packet_script<class_MultiplayerPeerExtension_private_method__put_packet_script>`\ (\ p_buffer\: :ref:`PackedByteArray<class_PackedByteArray>`\ ) |virtual|                   |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_set_refuse_new_connections<class_MultiplayerPeerExtension_private_method__set_refuse_new_connections>`\ (\ p_enable\: :ref:`bool<class_bool>`\ ) |virtual|                       |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_set_target_peer<class_MultiplayerPeerExtension_private_method__set_target_peer>`\ (\ p_peer\: :ref:`int<class_int>`\ ) |virtual| |required|                                      |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_set_transfer_channel<class_MultiplayerPeerExtension_private_method__set_transfer_channel>`\ (\ p_channel\: :ref:`int<class_int>`\ ) |virtual| |required|                         |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                         | :ref:`_set_transfer_mode<class_MultiplayerPeerExtension_private_method__set_transfer_mode>`\ (\ p_mode\: :ref:`TransferMode<enum_MultiplayerPeer_TransferMode>`\ ) |virtual| |required| |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_close**\ (\ ) |virtual| |required| [🔗<class_MultiplayerPeerExtension_private_method__close>]

Called when the multiplayer peer should be immediately closed (see [MultiplayerPeer.close()<class_MultiplayerPeer_method_close>]).


----



|void| **_disconnect_peer**\ (\ p_peer\: [int<class_int>], p_force\: [bool<class_bool>]\ ) |virtual| |required| [🔗<class_MultiplayerPeerExtension_private_method__disconnect_peer>]

Called when the connected `p_peer` should be forcibly disconnected (see [MultiplayerPeer.disconnect_peer()<class_MultiplayerPeer_method_disconnect_peer>]).


----



[int<class_int>] **_get_available_packet_count**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_available_packet_count>]

Called when the available packet count is internally requested by the [MultiplayerAPI<class_MultiplayerAPI>].


----



[ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>] **_get_connection_status**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_connection_status>]

Called when the connection status is requested on the [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.get_connection_status()<class_MultiplayerPeer_method_get_connection_status>]).


----



[int<class_int>] **_get_max_packet_size**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_max_packet_size>]

Called when the maximum allowed packet size (in bytes) is requested by the [MultiplayerAPI<class_MultiplayerAPI>].


----



[Error<enum_@GlobalScope_Error>] **_get_packet**\ (\ r_buffer\: `const uint8_t **`, r_buffer_size\: `int32_t*`\ ) |virtual| [🔗<class_MultiplayerPeerExtension_private_method__get_packet>]

Called when a packet needs to be received by the [MultiplayerAPI<class_MultiplayerAPI>], with `r_buffer_size` being the size of the binary `r_buffer` in bytes.


----



[int<class_int>] **_get_packet_channel**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_packet_channel>]

Called to get the channel over which the next available packet was received. See [MultiplayerPeer.get_packet_channel()<class_MultiplayerPeer_method_get_packet_channel>].


----



[TransferMode<enum_MultiplayerPeer_TransferMode>] **_get_packet_mode**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_packet_mode>]

Called to get the transfer mode the remote peer used to send the next available packet. See [MultiplayerPeer.get_packet_mode()<class_MultiplayerPeer_method_get_packet_mode>].


----



[int<class_int>] **_get_packet_peer**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_packet_peer>]

Called when the ID of the [MultiplayerPeer<class_MultiplayerPeer>] who sent the most recent packet is requested (see [MultiplayerPeer.get_packet_peer()<class_MultiplayerPeer_method_get_packet_peer>]).


----



[PackedByteArray<class_PackedByteArray>] **_get_packet_script**\ (\ ) |virtual| [🔗<class_MultiplayerPeerExtension_private_method__get_packet_script>]

Called when a packet needs to be received by the [MultiplayerAPI<class_MultiplayerAPI>], if [_get_packet()<class_MultiplayerPeerExtension_private_method__get_packet>] isn't implemented. Use this when extending this class via GDScript.


----



[int<class_int>] **_get_transfer_channel**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_transfer_channel>]

Called when the transfer channel to use is read on this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.transfer_channel<class_MultiplayerPeer_property_transfer_channel>]).


----



[TransferMode<enum_MultiplayerPeer_TransferMode>] **_get_transfer_mode**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_transfer_mode>]

Called when the transfer mode to use is read on this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.transfer_mode<class_MultiplayerPeer_property_transfer_mode>]).


----



[int<class_int>] **_get_unique_id**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__get_unique_id>]

Called when the unique ID of this [MultiplayerPeer<class_MultiplayerPeer>] is requested (see [MultiplayerPeer.get_unique_id()<class_MultiplayerPeer_method_get_unique_id>]). The value must be between `1` and `2147483647`.


----



[bool<class_bool>] **_is_refusing_new_connections**\ (\ ) |virtual| |const| [🔗<class_MultiplayerPeerExtension_private_method__is_refusing_new_connections>]

Called when the "refuse new connections" status is requested on this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.refuse_new_connections<class_MultiplayerPeer_property_refuse_new_connections>]).


----



[bool<class_bool>] **_is_server**\ (\ ) |virtual| |required| |const| [🔗<class_MultiplayerPeerExtension_private_method__is_server>]

Called when the "is server" status is requested on the [MultiplayerAPI<class_MultiplayerAPI>]. See [MultiplayerAPI.is_server()<class_MultiplayerAPI_method_is_server>].


----



[bool<class_bool>] **_is_server_relay_supported**\ (\ ) |virtual| |const| [🔗<class_MultiplayerPeerExtension_private_method__is_server_relay_supported>]

Called to check if the server can act as a relay in the current configuration. See [MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>].


----



|void| **_poll**\ (\ ) |virtual| |required| [🔗<class_MultiplayerPeerExtension_private_method__poll>]

Called when the [MultiplayerAPI<class_MultiplayerAPI>] is polled. See [MultiplayerAPI.poll()<class_MultiplayerAPI_method_poll>].


----



[Error<enum_@GlobalScope_Error>] **_put_packet**\ (\ p_buffer\: `const uint8_t*`, p_buffer_size\: [int<class_int>]\ ) |virtual| [🔗<class_MultiplayerPeerExtension_private_method__put_packet>]

Called when a packet needs to be sent by the [MultiplayerAPI<class_MultiplayerAPI>], with `p_buffer_size` being the size of the binary `p_buffer` in bytes.


----



[Error<enum_@GlobalScope_Error>] **_put_packet_script**\ (\ p_buffer\: [PackedByteArray<class_PackedByteArray>]\ ) |virtual| [🔗<class_MultiplayerPeerExtension_private_method__put_packet_script>]

Called when a packet needs to be sent by the [MultiplayerAPI<class_MultiplayerAPI>], if [_put_packet()<class_MultiplayerPeerExtension_private_method__put_packet>] isn't implemented. Use this when extending this class via GDScript.


----



|void| **_set_refuse_new_connections**\ (\ p_enable\: [bool<class_bool>]\ ) |virtual| [🔗<class_MultiplayerPeerExtension_private_method__set_refuse_new_connections>]

Called when the "refuse new connections" status is set on this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.refuse_new_connections<class_MultiplayerPeer_property_refuse_new_connections>]).


----



|void| **_set_target_peer**\ (\ p_peer\: [int<class_int>]\ ) |virtual| |required| [🔗<class_MultiplayerPeerExtension_private_method__set_target_peer>]

Called when the target peer to use is set for this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.set_target_peer()<class_MultiplayerPeer_method_set_target_peer>]).


----



|void| **_set_transfer_channel**\ (\ p_channel\: [int<class_int>]\ ) |virtual| |required| [🔗<class_MultiplayerPeerExtension_private_method__set_transfer_channel>]

Called when the channel to use is set for this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.transfer_channel<class_MultiplayerPeer_property_transfer_channel>]).


----



|void| **_set_transfer_mode**\ (\ p_mode\: [TransferMode<enum_MultiplayerPeer_TransferMode>]\ ) |virtual| |required| [🔗<class_MultiplayerPeerExtension_private_method__set_transfer_mode>]

Called when the transfer mode is set on this [MultiplayerPeer<class_MultiplayerPeer>] (see [MultiplayerPeer.transfer_mode<class_MultiplayerPeer_property_transfer_mode>]).

