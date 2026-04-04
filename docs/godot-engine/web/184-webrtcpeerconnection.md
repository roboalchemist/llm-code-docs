# WebRTCPeerConnection

# WebRTCPeerConnection

Inherits:RefCounted<Object
Inherited By:WebRTCPeerConnectionExtension
Interface to a WebRTC peer connection.

## Description

A WebRTC connection between the local computer and a remote peer. Provides an interface to connect, maintain, and monitor the connection.
Setting up a WebRTC connection between two peers may not seem a trivial task, but it can be broken down into 3 main steps:

- The peer that wants to initiate the connection (Afrom now on) creates an offer and sends it to the other peer (Bfrom now on).
The peer that wants to initiate the connection (Afrom now on) creates an offer and sends it to the other peer (Bfrom now on).
- Breceives the offer, generates an answer, and sends it toA.
Breceives the offer, generates an answer, and sends it toA.
- AandBthen generate and exchange ICE candidates with each other.
AandBthen generate and exchange ICE candidates with each other.
After these steps, the connection should be established. Refer to the linked tutorials for details.

## Tutorials

- WebRTC documentation
WebRTC documentation
- High-level multiplayer
High-level multiplayer

## Methods

| Error | add_ice_candidate(media:String, index:int, name:String) |
|---|---|
| void | close() |
| WebRTCDataChannel | create_data_channel(label:String, options:Dictionary= {}) |
| Error | create_offer() |
| ConnectionState | get_connection_state()const |
| GatheringState | get_gathering_state()const |
| SignalingState | get_signaling_state()const |
| Error | initialize(configuration:Dictionary= {}) |
| Error | poll() |
| void | set_default_extension(extension_class:StringName)static |
| Error | set_local_description(type:String, sdp:String) |
| Error | set_remote_description(type:String, sdp:String) |

Error
add_ice_candidate(media:String, index:int, name:String)
void
close()
WebRTCDataChannel
create_data_channel(label:String, options:Dictionary= {})
Error
create_offer()
ConnectionState
get_connection_state()const
GatheringState
get_gathering_state()const
SignalingState
get_signaling_state()const
Error
initialize(configuration:Dictionary= {})
Error
poll()
void
set_default_extension(extension_class:StringName)static
Error
set_local_description(type:String, sdp:String)
Error
set_remote_description(type:String, sdp:String)

## Signals

data_channel_received(channel:WebRTCDataChannel)🔗
Emitted when a new in-band channel is received, i.e. when the channel was created withnegotiated:false(default).
The object will be an instance ofWebRTCDataChannel. You must keep a reference of it or it will be closed automatically. Seecreate_data_channel().
ice_candidate_created(media:String, index:int, name:String)🔗
Emitted when a new ICE candidate has been created. The three parameters are meant to be passed to the remote peer over the signaling server.
session_description_created(type:String, sdp:String)🔗
Emitted after a successful call tocreate_offer()orset_remote_description()(when it generates an answer). The parameters are meant to be passed toset_local_description()on this object, and sent to the remote peer over the signaling server.

## Enumerations

enumConnectionState:🔗
ConnectionStateSTATE_NEW=0
The connection is new, data channels and an offer can be created in this state.
ConnectionStateSTATE_CONNECTING=1
The peer is connecting, ICE is in progress, none of the transports has failed.
ConnectionStateSTATE_CONNECTED=2
The peer is connected, all ICE transports are connected.
ConnectionStateSTATE_DISCONNECTED=3
At least one ICE transport is disconnected.
ConnectionStateSTATE_FAILED=4
One or more of the ICE transports failed.
ConnectionStateSTATE_CLOSED=5
The peer connection is closed (after callingclose()for example).
enumGatheringState:🔗
GatheringStateGATHERING_STATE_NEW=0
The peer connection was just created and hasn't done any networking yet.
GatheringStateGATHERING_STATE_GATHERING=1
The ICE agent is in the process of gathering candidates for the connection.
GatheringStateGATHERING_STATE_COMPLETE=2
The ICE agent has finished gathering candidates. If something happens that requires collecting new candidates, such as a new interface being added or the addition of a new ICE server, the state will revert to gathering to gather those candidates.
enumSignalingState:🔗
SignalingStateSIGNALING_STATE_STABLE=0
There is no ongoing exchange of offer and answer underway. This may mean that theWebRTCPeerConnectionis new (STATE_NEW) or that negotiation is complete and a connection has been established (STATE_CONNECTED).
SignalingStateSIGNALING_STATE_HAVE_LOCAL_OFFER=1
The local peer has calledset_local_description(), passing in SDP representing an offer (usually created by callingcreate_offer()), and the offer has been applied successfully.
SignalingStateSIGNALING_STATE_HAVE_REMOTE_OFFER=2
The remote peer has created an offer and used the signaling server to deliver it to the local peer, which has set the offer as the remote description by callingset_remote_description().
SignalingStateSIGNALING_STATE_HAVE_LOCAL_PRANSWER=3
The offer sent by the remote peer has been applied and an answer has been created and applied by callingset_local_description(). This provisional answer describes the supported media formats and so forth, but may not have a complete set of ICE candidates included. Further candidates will be delivered separately later.
SignalingStateSIGNALING_STATE_HAVE_REMOTE_PRANSWER=4
A provisional answer has been received and successfully applied in response to an offer previously sent and established by callingset_local_description().
SignalingStateSIGNALING_STATE_CLOSED=5
TheWebRTCPeerConnectionhas been closed.

## Method Descriptions

Erroradd_ice_candidate(media:String, index:int, name:String)🔗
Add an ice candidate generated by a remote peer (and received over the signaling server). Seeice_candidate_created.
voidclose()🔗
Close the peer connection and all data channels associated with it.
Note:You cannot reuse this object for a new connection unless you callinitialize().
WebRTCDataChannelcreate_data_channel(label:String, options:Dictionary= {})🔗
Returns a newWebRTCDataChannel(ornullon failure) with givenlabeland optionally configured via theoptionsdictionary. This method can only be called when the connection is in stateSTATE_NEW.
There are two ways to create a working data channel: either callcreate_data_channel()on only one of the peer and listen todata_channel_receivedon the other, or callcreate_data_channel()on both peers, with the same values, and the"negotiated"option set totrue.
Validoptionsare:

```
{
    "negotiated": true, # When set to true (default off), means the channel is negotiated out of band. "id" must be set too. "data_channel_received" will not be called.
    "id": 1, # When "negotiated" is true this value must also be set to the same value on both peer.

    # Only one of maxRetransmits and maxPacketLifeTime can be specified, not both. They make the channel unreliable (but also better at real time).
    "maxRetransmits": 1, # Specify the maximum number of attempt the peer will make to retransmits packets if they are not acknowledged.
    "maxPacketLifeTime": 100, # Specify the maximum amount of time before giving up retransmitions of unacknowledged packets (in milliseconds).
    "ordered": true, # When in unreliable mode (i.e. either "maxRetransmits" or "maxPacketLifetime" is set), "ordered" (true by default) specify if packet ordering is to be enforced.

    "protocol": "my-custom-protocol", # A custom sub-protocol string for this channel.
}
```

Note:You must keep a reference to channels created this way, or it will be closed.
Errorcreate_offer()🔗
Creates a new SDP offer to start a WebRTC connection with a remote peer. At least oneWebRTCDataChannelmust have been created before calling this method.
If this functions returns@GlobalScope.OK,session_description_createdwill be called when the session is ready to be sent.
ConnectionStateget_connection_state()const🔗
Returns the connection state.
GatheringStateget_gathering_state()const🔗
Returns the ICEGatheringStateof the connection. This lets you detect, for example, when collection of ICE candidates has finished.
SignalingStateget_signaling_state()const🔗
Returns the signaling state on the local end of the connection while connecting or reconnecting to another peer.
Errorinitialize(configuration:Dictionary= {})🔗
Re-initialize this peer connection, closing any previously active connection, and going back to stateSTATE_NEW. A dictionary ofconfigurationoptions can be passed to configure the peer connection.
Validconfigurationoptions are:

```
{
    "iceServers": [
        {
            "urls": [ "stun:stun.example.com:3478" ], # One or more STUN servers.
        },
        {
            "urls": [ "turn:turn.example.com:3478" ], # One or more TURN servers.
            "username": "a_username", # Optional username for the TURN server.
            "credential": "a_password", # Optional password for the TURN server.
        }
    ]
}
```

Errorpoll()🔗
Call this method frequently (e.g. inNode._process()orNode._physics_process()) to properly receive signals.
voidset_default_extension(extension_class:StringName)static🔗
Sets theextension_classas the defaultWebRTCPeerConnectionExtensionreturned when creating a newWebRTCPeerConnection.
Errorset_local_description(type:String, sdp:String)🔗
Sets the SDP description of the local peer. This should be called in response tosession_description_created.
After calling this function the peer will start emittingice_candidate_created(unless anErrordifferent from@GlobalScope.OKis returned).
Errorset_remote_description(type:String, sdp:String)🔗
Sets the SDP description of the remote peer. This should be called with the values generated by a remote peer and received over the signaling server.
Iftypeis"offer"the peer will emitsession_description_createdwith the appropriate answer.
Iftypeis"answer"the peer will start emittingice_candidate_created.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
