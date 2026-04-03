# MultiplayerPeerExtension

# MultiplayerPeerExtension
Inherits:MultiplayerPeer<PacketPeer<RefCounted<Object
Class that can be inherited to implement custom multiplayer API networking layers via GDExtension.

## Description
This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods belowmustbe implemented to have a working custom multiplayer implementation. See alsoMultiplayerAPI.

## Methods

| void | _close()virtualrequired |
|---|---|
| void | _disconnect_peer(p_peer:int, p_force:bool)virtualrequired |
| int | _get_available_packet_count()virtualrequiredconst |
| ConnectionStatus | _get_connection_status()virtualrequiredconst |
| int | _get_max_packet_size()virtualrequiredconst |
| Error | _get_packet(r_buffer:constuint8_t**, r_buffer_size:int32_t*)virtual |
| int | _get_packet_channel()virtualrequiredconst |
| TransferMode | _get_packet_mode()virtualrequiredconst |
| int | _get_packet_peer()virtualrequiredconst |
| PackedByteArray | _get_packet_script()virtual |
| int | _get_transfer_channel()virtualrequiredconst |
| TransferMode | _get_transfer_mode()virtualrequiredconst |
| int | _get_unique_id()virtualrequiredconst |
| bool | _is_refusing_new_connections()virtualconst |
| bool | _is_server()virtualrequiredconst |
| bool | _is_server_relay_supported()virtualconst |
| void | _poll()virtualrequired |
| Error | _put_packet(p_buffer:constuint8_t*, p_buffer_size:int)virtual |
| Error | _put_packet_script(p_buffer:PackedByteArray)virtual |
| void | _set_refuse_new_connections(p_enable:bool)virtual |
| void | _set_target_peer(p_peer:int)virtualrequired |
| void | _set_transfer_channel(p_channel:int)virtualrequired |
| void | _set_transfer_mode(p_mode:TransferMode)virtualrequired |

void
_close()virtualrequired
void
_disconnect_peer(p_peer:int, p_force:bool)virtualrequired
_get_available_packet_count()virtualrequiredconst
ConnectionStatus
_get_connection_status()virtualrequiredconst
_get_max_packet_size()virtualrequiredconst
Error
_get_packet(r_buffer:constuint8_t**, r_buffer_size:int32_t*)virtual
_get_packet_channel()virtualrequiredconst
TransferMode
_get_packet_mode()virtualrequiredconst
_get_packet_peer()virtualrequiredconst
PackedByteArray
_get_packet_script()virtual
_get_transfer_channel()virtualrequiredconst
TransferMode
_get_transfer_mode()virtualrequiredconst
_get_unique_id()virtualrequiredconst
bool
_is_refusing_new_connections()virtualconst
bool
_is_server()virtualrequiredconst
bool
_is_server_relay_supported()virtualconst
void
_poll()virtualrequired
Error
_put_packet(p_buffer:constuint8_t*, p_buffer_size:int)virtual
Error
_put_packet_script(p_buffer:PackedByteArray)virtual
void
_set_refuse_new_connections(p_enable:bool)virtual
void
_set_target_peer(p_peer:int)virtualrequired
void
_set_transfer_channel(p_channel:int)virtualrequired
void
_set_transfer_mode(p_mode:TransferMode)virtualrequired

## Method Descriptions
void_close()virtualrequired🔗
Called when the multiplayer peer should be immediately closed (seeMultiplayerPeer.close()).
void_disconnect_peer(p_peer:int, p_force:bool)virtualrequired🔗
Called when the connectedp_peershould be forcibly disconnected (seeMultiplayerPeer.disconnect_peer()).
int_get_available_packet_count()virtualrequiredconst🔗
Called when the available packet count is internally requested by theMultiplayerAPI.
ConnectionStatus_get_connection_status()virtualrequiredconst🔗
Called when the connection status is requested on theMultiplayerPeer(seeMultiplayerPeer.get_connection_status()).
int_get_max_packet_size()virtualrequiredconst🔗
Called when the maximum allowed packet size (in bytes) is requested by theMultiplayerAPI.
Error_get_packet(r_buffer:constuint8_t**, r_buffer_size:int32_t*)virtual🔗
Called when a packet needs to be received by theMultiplayerAPI, withr_buffer_sizebeing the size of the binaryr_bufferin bytes.
int_get_packet_channel()virtualrequiredconst🔗
Called to get the channel over which the next available packet was received. SeeMultiplayerPeer.get_packet_channel().
TransferMode_get_packet_mode()virtualrequiredconst🔗
Called to get the transfer mode the remote peer used to send the next available packet. SeeMultiplayerPeer.get_packet_mode().
int_get_packet_peer()virtualrequiredconst🔗
Called when the ID of theMultiplayerPeerwho sent the most recent packet is requested (seeMultiplayerPeer.get_packet_peer()).
PackedByteArray_get_packet_script()virtual🔗
Called when a packet needs to be received by theMultiplayerAPI, if_get_packet()isn't implemented. Use this when extending this class via GDScript.
int_get_transfer_channel()virtualrequiredconst🔗
Called when the transfer channel to use is read on thisMultiplayerPeer(seeMultiplayerPeer.transfer_channel).
TransferMode_get_transfer_mode()virtualrequiredconst🔗
Called when the transfer mode to use is read on thisMultiplayerPeer(seeMultiplayerPeer.transfer_mode).
int_get_unique_id()virtualrequiredconst🔗
Called when the unique ID of thisMultiplayerPeeris requested (seeMultiplayerPeer.get_unique_id()). The value must be between1and2147483647.
bool_is_refusing_new_connections()virtualconst🔗
Called when the "refuse new connections" status is requested on thisMultiplayerPeer(seeMultiplayerPeer.refuse_new_connections).
bool_is_server()virtualrequiredconst🔗
Called when the "is server" status is requested on theMultiplayerAPI. SeeMultiplayerAPI.is_server().
bool_is_server_relay_supported()virtualconst🔗
Called to check if the server can act as a relay in the current configuration. SeeMultiplayerPeer.is_server_relay_supported().
void_poll()virtualrequired🔗
Called when theMultiplayerAPIis polled. SeeMultiplayerAPI.poll().
Error_put_packet(p_buffer:constuint8_t*, p_buffer_size:int)virtual🔗
Called when a packet needs to be sent by theMultiplayerAPI, withp_buffer_sizebeing the size of the binaryp_bufferin bytes.
Error_put_packet_script(p_buffer:PackedByteArray)virtual🔗
Called when a packet needs to be sent by theMultiplayerAPI, if_put_packet()isn't implemented. Use this when extending this class via GDScript.
void_set_refuse_new_connections(p_enable:bool)virtual🔗
Called when the "refuse new connections" status is set on thisMultiplayerPeer(seeMultiplayerPeer.refuse_new_connections).
void_set_target_peer(p_peer:int)virtualrequired🔗
Called when the target peer to use is set for thisMultiplayerPeer(seeMultiplayerPeer.set_target_peer()).
void_set_transfer_channel(p_channel:int)virtualrequired🔗
Called when the channel to use is set for thisMultiplayerPeer(seeMultiplayerPeer.transfer_channel).
void_set_transfer_mode(p_mode:TransferMode)virtualrequired🔗
Called when the transfer mode is set on thisMultiplayerPeer(seeMultiplayerPeer.transfer_mode).

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.