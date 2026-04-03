# WebRTCMultiplayerPeer in English

# WebRTCMultiplayerPeer
Inherits:MultiplayerPeer<PacketPeer<RefCounted<Object
A simple interface to create a peer-to-peer mesh network composed ofWebRTCPeerConnectionthat is compatible with theMultiplayerAPI.

## Description
This class constructs a full mesh ofWebRTCPeerConnection(one connection for each peer) that can be used as aMultiplayerAPI.multiplayer_peer.
You can add eachWebRTCPeerConnectionviaadd_peer()or remove them viaremove_peer(). Peers must be added inWebRTCPeerConnection.STATE_NEWstate to allow it to create the appropriate channels. This class will not create offers nor set descriptions, it will only poll them, and notify connections and disconnections.
When creating the peer viacreate_client()orcreate_server()theMultiplayerPeer.is_server_relay_supported()method will returntrueenabling peer exchange and packet relaying when supported by theMultiplayerAPIimplementation.
Note:When exporting to Android, make sure to enable theINTERNETpermission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Methods

| Error | add_peer(peer:WebRTCPeerConnection, peer_id:int, unreliable_lifetime:int= 1) |
|---|---|
| Error | create_client(peer_id:int, channels_config:Array= []) |
| Error | create_mesh(peer_id:int, channels_config:Array= []) |
| Error | create_server(channels_config:Array= []) |
| Dictionary | get_peer(peer_id:int) |
| Dictionary | get_peers() |
| bool | has_peer(peer_id:int) |
| void | remove_peer(peer_id:int) |

Error
add_peer(peer:WebRTCPeerConnection, peer_id:int, unreliable_lifetime:int= 1)
Error
create_client(peer_id:int, channels_config:Array= [])
Error
create_mesh(peer_id:int, channels_config:Array= [])
Error
create_server(channels_config:Array= [])
Dictionary
get_peer(peer_id:int)
Dictionary
get_peers()
bool
has_peer(peer_id:int)
void
remove_peer(peer_id:int)

## Method Descriptions
Erroradd_peer(peer:WebRTCPeerConnection, peer_id:int, unreliable_lifetime:int= 1)🔗
Add a new peer to the mesh with the givenpeer_id. TheWebRTCPeerConnectionmust be in stateWebRTCPeerConnection.STATE_NEW.
Three channels will be created for reliable, unreliable, and ordered transport. The value ofunreliable_lifetimewill be passed to the"maxPacketLifetime"option when creating unreliable and ordered channels (seeWebRTCPeerConnection.create_data_channel()).
Errorcreate_client(peer_id:int, channels_config:Array= [])🔗
Initialize the multiplayer peer as a client with the givenpeer_id(must be between 2 and 2147483647). In this mode, you should only calladd_peer()once and withpeer_idof1. This mode enablesMultiplayerPeer.is_server_relay_supported(), allowing the upperMultiplayerAPIlayer to perform peer exchange and packet relaying.
You can optionally specify achannels_configarray ofTransferModewhich will be used to create extra channels (WebRTC only supports one transfer mode per channel).
Errorcreate_mesh(peer_id:int, channels_config:Array= [])🔗
Initialize the multiplayer peer as a mesh (i.e. all peers connect to each other) with the givenpeer_id(must be between 1 and 2147483647).
Errorcreate_server(channels_config:Array= [])🔗
Initialize the multiplayer peer as a server (with unique ID of1). This mode enablesMultiplayerPeer.is_server_relay_supported(), allowing the upperMultiplayerAPIlayer to perform peer exchange and packet relaying.
You can optionally specify achannels_configarray ofTransferModewhich will be used to create extra channels (WebRTC only supports one transfer mode per channel).
Dictionaryget_peer(peer_id:int)🔗
Returns a dictionary representation of the peer with givenpeer_idwith three keys."connection"containing theWebRTCPeerConnectionto this peer,"channels"an array of threeWebRTCDataChannel, and"connected"a boolean representing if the peer connection is currently connected (all three channels are open).
Dictionaryget_peers()🔗
Returns a dictionary which keys are the peer ids and values the peer representation as inget_peer().
boolhas_peer(peer_id:int)🔗
Returnstrueif the givenpeer_idis in the peers map (it might not be connected though).
voidremove_peer(peer_id:int)🔗
Remove the peer with givenpeer_idfrom the mesh. If the peer was connected, andMultiplayerPeer.peer_connectedwas emitted for it, thenMultiplayerPeer.peer_disconnectedwill be emitted.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.