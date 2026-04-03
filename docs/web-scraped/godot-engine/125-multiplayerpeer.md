# MultiplayerPeer

# MultiplayerPeer

Inherits:PacketPeer<RefCounted<Object
Inherited By:ENetMultiplayerPeer,MultiplayerPeerExtension,OfflineMultiplayerPeer,WebRTCMultiplayerPeer,WebSocketMultiplayerPeer
Abstract class for specializedPacketPeers used by theMultiplayerAPI.

## Description

Manages the connection with one or more remote peers acting as server or client and assigning unique IDs to each of them. See alsoMultiplayerAPI.
Note:TheMultiplayerAPIprotocol is an implementation detail and isn't meant to be used by non-Godot servers. It may change without notice.
Note:When exporting to Android, make sure to enable theINTERNETpermission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Tutorials

- High-level multiplayer
High-level multiplayer

## Properties

| bool | refuse_new_connections | false |
|---|---|---|
| int | transfer_channel | 0 |
| TransferMode | transfer_mode | 2 |

bool
refuse_new_connections
false
transfer_channel
TransferMode
transfer_mode

## Methods

| void | close() |
|---|---|
| void | disconnect_peer(peer:int, force:bool= false) |
| int | generate_unique_id()const |
| ConnectionStatus | get_connection_status()const |
| int | get_packet_channel()const |
| TransferMode | get_packet_mode()const |
| int | get_packet_peer()const |
| int | get_unique_id()const |
| bool | is_server_relay_supported()const |
| void | poll() |
| void | set_target_peer(id:int) |

void
close()
void
disconnect_peer(peer:int, force:bool= false)
generate_unique_id()const
ConnectionStatus
get_connection_status()const
get_packet_channel()const
TransferMode
get_packet_mode()const
get_packet_peer()const
get_unique_id()const
bool
is_server_relay_supported()const
void
poll()
void
set_target_peer(id:int)

## Signals

peer_connected(id:int)🔗
Emitted when a remote peer connects.
peer_disconnected(id:int)🔗
Emitted when a remote peer has disconnected.

## Enumerations

enumConnectionStatus:🔗
ConnectionStatusCONNECTION_DISCONNECTED=0
The MultiplayerPeer is disconnected.
ConnectionStatusCONNECTION_CONNECTING=1
The MultiplayerPeer is currently connecting to a server.
ConnectionStatusCONNECTION_CONNECTED=2
This MultiplayerPeer is connected.
enumTransferMode:🔗
TransferModeTRANSFER_MODE_UNRELIABLE=0
Packets are not acknowledged, no resend attempts are made for lost packets. Packets may arrive in any order. Potentially faster thanTRANSFER_MODE_UNRELIABLE_ORDERED. Use for non-critical data, and always consider whether the order matters.
TransferModeTRANSFER_MODE_UNRELIABLE_ORDERED=1
Packets are not acknowledged, no resend attempts are made for lost packets. Packets are received in the order they were sent in. Potentially faster thanTRANSFER_MODE_RELIABLE. Use for non-critical data or data that would be outdated if received late due to resend attempt(s) anyway, for example movement and positional data.
TransferModeTRANSFER_MODE_RELIABLE=2
Packets must be received and resend attempts should be made until the packets are acknowledged. Packets must be received in the order they were sent in. Most reliable transfer mode, but potentially the slowest due to the overhead. Use for critical data that must be transmitted and arrive in order, for example an ability being triggered or a chat message. Consider carefully if the information really is critical, and use sparingly.

## Constants

TARGET_PEER_BROADCAST=0🔗
Packets are sent to all connected peers.
TARGET_PEER_SERVER=1🔗
Packets are sent to the remote peer acting as server.

## Property Descriptions

boolrefuse_new_connections=false🔗

- voidset_refuse_new_connections(value:bool)
voidset_refuse_new_connections(value:bool)
- boolis_refusing_new_connections()
boolis_refusing_new_connections()
Iftrue, thisMultiplayerPeerrefuses new connections.
inttransfer_channel=0🔗
- voidset_transfer_channel(value:int)
voidset_transfer_channel(value:int)
- intget_transfer_channel()
intget_transfer_channel()
The channel to use to send packets. Many network APIs such as ENet and WebRTC allow the creation of multiple independent channels which behaves, in a way, like separate connections. This means that reliable data will only block delivery of other packets on that channel, and ordering will only be in respect to the channel the packet is being sent on. Using different channels to senddifferent and independentstate updates is a common way to optimize network usage and decrease latency in fast-paced games.
Note:The default channel (0) actually works as 3 separate channels (one for eachTransferMode) so thatTRANSFER_MODE_RELIABLEandTRANSFER_MODE_UNRELIABLE_ORDEREDdoes not interact with each other by default. Refer to the specific network API documentation (e.g. ENet or WebRTC) to learn how to set up channels correctly.
TransferModetransfer_mode=2🔗
- voidset_transfer_mode(value:TransferMode)
voidset_transfer_mode(value:TransferMode)
- TransferModeget_transfer_mode()
TransferModeget_transfer_mode()
The manner in which to send packets to the target peer. See theset_target_peer()method.

## Method Descriptions

voidclose()🔗
Immediately close the multiplayer peer returning to the stateCONNECTION_DISCONNECTED. Connected peers will be dropped without emittingpeer_disconnected.
voiddisconnect_peer(peer:int, force:bool= false)🔗
Disconnects the givenpeerfrom this host. Ifforceistruethepeer_disconnectedsignal will not be emitted for this peer.
intgenerate_unique_id()const🔗
Returns a randomly generated integer that can be used as a network unique ID.
ConnectionStatusget_connection_status()const🔗
Returns the current state of the connection.
intget_packet_channel()const🔗
Returns the channel over which the next available packet was received. SeePacketPeer.get_available_packet_count().
TransferModeget_packet_mode()const🔗
Returns the transfer mode the remote peer used to send the next available packet. SeePacketPeer.get_available_packet_count().
intget_packet_peer()const🔗
Returns the ID of theMultiplayerPeerwho sent the next available packet. SeePacketPeer.get_available_packet_count().
intget_unique_id()const🔗
Returns the ID of thisMultiplayerPeer.
boolis_server_relay_supported()const🔗
Returnstrueif the server can act as a relay in the current configuration. That is, if the higher levelMultiplayerAPIshould notify connected clients of other peers, and implement a relay protocol to allow communication between them.
voidpoll()🔗
Waits up to 1 second to receive a new network event.
voidset_target_peer(id:int)🔗
Sets the peer to which packets will be sent.
Theidcan be one of:TARGET_PEER_BROADCASTto send to all connected peers,TARGET_PEER_SERVERto send to the peer acting as server, a valid peer ID to send to that specific peer, a negative peer ID to send to all peers except that one. By default, the target peer isTARGET_PEER_BROADCAST.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
