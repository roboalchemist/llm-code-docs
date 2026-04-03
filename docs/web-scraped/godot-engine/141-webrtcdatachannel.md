# WebRTCDataChannel

# WebRTCDataChannel

Inherits:PacketPeer<RefCounted<Object
Inherited By:WebRTCDataChannelExtension
There is currently no description for this class. Please help us bycontributing one!

## Properties

| WriteMode | write_mode | 1 |

WriteMode
write_mode

## Methods

| void | close() |
|---|---|
| int | get_buffered_amount()const |
| int | get_id()const |
| String | get_label()const |
| int | get_max_packet_life_time()const |
| int | get_max_retransmits()const |
| String | get_protocol()const |
| ChannelState | get_ready_state()const |
| bool | is_negotiated()const |
| bool | is_ordered()const |
| Error | poll() |
| bool | was_string_packet()const |

void
close()
get_buffered_amount()const
get_id()const
String
get_label()const
get_max_packet_life_time()const
get_max_retransmits()const
String
get_protocol()const
ChannelState
get_ready_state()const
bool
is_negotiated()const
bool
is_ordered()const
Error
poll()
bool
was_string_packet()const

## Enumerations

enumWriteMode:🔗
WriteModeWRITE_MODE_TEXT=0
Tells the channel to send data over this channel as text. An external peer (non-Godot) would receive this as a string.
WriteModeWRITE_MODE_BINARY=1
Tells the channel to send data over this channel as binary. An external peer (non-Godot) would receive this as array buffer or blob.
enumChannelState:🔗
ChannelStateSTATE_CONNECTING=0
The channel was created, but it's still trying to connect.
ChannelStateSTATE_OPEN=1
The channel is currently open, and data can flow over it.
ChannelStateSTATE_CLOSING=2
The channel is being closed, no new messages will be accepted, but those already in queue will be flushed.
ChannelStateSTATE_CLOSED=3
The channel was closed, or connection failed.

## Property Descriptions

WriteModewrite_mode=1🔗

- voidset_write_mode(value:WriteMode)
voidset_write_mode(value:WriteMode)
- WriteModeget_write_mode()
WriteModeget_write_mode()
The transfer mode to use when sending outgoing packet. Either text or binary.

## Method Descriptions

voidclose()🔗
Closes this data channel, notifying the other peer.
intget_buffered_amount()const🔗
Returns the number of bytes currently queued to be sent over this channel.
intget_id()const🔗
Returns the ID assigned to this channel during creation (or auto-assigned during negotiation).
If the channel is not negotiated out-of-band the ID will only be available after the connection is established (will return65535until then).
Stringget_label()const🔗
Returns the label assigned to this channel during creation.
intget_max_packet_life_time()const🔗
Returns themaxPacketLifeTimevalue assigned to this channel during creation.
Will be65535if not specified.
intget_max_retransmits()const🔗
Returns themaxRetransmitsvalue assigned to this channel during creation.
Will be65535if not specified.
Stringget_protocol()const🔗
Returns the sub-protocol assigned to this channel during creation. An empty string if not specified.
ChannelStateget_ready_state()const🔗
Returns the current state of this channel.
boolis_negotiated()const🔗
Returnstrueif this channel was created with out-of-band configuration.
boolis_ordered()const🔗
Returnstrueif this channel was created with ordering enabled (default).
Errorpoll()🔗
Reserved, but not used for now.
boolwas_string_packet()const🔗
Returnstrueif the last received packet was transferred as text. Seewrite_mode.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
