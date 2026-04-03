# PacketPeerDTLS

# PacketPeerDTLS
Inherits:PacketPeer<RefCounted<Object
DTLS packet peer.

## Description
This class represents a DTLS peer connection. It can be used to connect to a DTLS server, and is returned byDTLSServer.take_connection().
Note:When exporting to Android, make sure to enable theINTERNETpermission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.
Warning:TLS certificate revocation and certificate pinning are currently not supported. Revoked certificates are accepted as long as they are otherwise valid. If this is a concern, you may want to use automatically managed certificates with a short validity period.

## Methods

| Error | connect_to_peer(packet_peer:PacketPeerUDP, hostname:String, client_options:TLSOptions= null) |
|---|---|
| void | disconnect_from_peer() |
| Status | get_status()const |
| void | poll() |

Error
connect_to_peer(packet_peer:PacketPeerUDP, hostname:String, client_options:TLSOptions= null)
void
disconnect_from_peer()
Status
get_status()const
void
poll()

## Enumerations
enumStatus:🔗
StatusSTATUS_DISCONNECTED=0
A status representing aPacketPeerDTLSthat is disconnected.
StatusSTATUS_HANDSHAKING=1
A status representing aPacketPeerDTLSthat is currently performing the handshake with a remote peer.
StatusSTATUS_CONNECTED=2
A status representing aPacketPeerDTLSthat is connected to a remote peer.
StatusSTATUS_ERROR=3
A status representing aPacketPeerDTLSin a generic error state.
StatusSTATUS_ERROR_HOSTNAME_MISMATCH=4
An error status that shows a mismatch in the DTLS certificate domain presented by the host and the domain requested for validation.

## Method Descriptions
Errorconnect_to_peer(packet_peer:PacketPeerUDP, hostname:String, client_options:TLSOptions= null)🔗
Connects apacket_peerbeginning the DTLS handshake using the underlyingPacketPeerUDPwhich must be connected (seePacketPeerUDP.connect_to_host()). You can optionally specify theclient_optionsto be used while verifying the TLS connections. SeeTLSOptions.client()andTLSOptions.client_unsafe().
voiddisconnect_from_peer()🔗
Disconnects this peer, terminating the DTLS session.
Statusget_status()const🔗
Returns the status of the connection.
voidpoll()🔗
Poll the connection to check for incoming packets. Call this frequently to update the status and keep the connection working.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.