# WebSocketPeer in English

# WebSocketPeer

Inherits:PacketPeer<RefCounted<Object
A WebSocket connection.

## Description

This class represents WebSocket connection, and can be used as a WebSocket client (RFC 6455-compliant) or as a remote peer of a WebSocket server.
You can send WebSocket binary frames usingPacketPeer.put_packet(), and WebSocket text frames usingsend()(prefer text frames when interacting with text-based API). You can check the frame type of the last packet viawas_string_packet().
To start a WebSocket client, first callconnect_to_url(), then regularly callpoll()(e.g. duringNodeprocess). You can query the socket state viaget_ready_state(), get the number of pending packets usingPacketPeer.get_available_packet_count(), and retrieve them viaPacketPeer.get_packet().

```
extends Node

var socket = WebSocketPeer.new()

func _ready():
    socket.connect_to_url("wss://example.com")

func _process(delta):
    socket.poll()
    var state = socket.get_ready_state()
    if state == WebSocketPeer.STATE_OPEN:
        while socket.get_available_packet_count():
            print("Packet: ", socket.get_packet())
    elif state == WebSocketPeer.STATE_CLOSING:
        # Keep polling to achieve proper close.
        pass
    elif state == WebSocketPeer.STATE_CLOSED:
        var code = socket.get_close_code()
        var reason = socket.get_close_reason()
        print("WebSocket closed with code: %d, reason %s. Clean: %s" % [code, reason, code != -1])
        set_process(false) # Stop processing.
```

To use the peer as part of a WebSocket server refer toaccept_stream()and the online tutorial.

## Properties

| PackedStringArray | handshake_headers | PackedStringArray() |
|---|---|---|
| float | heartbeat_interval | 0.0 |
| int | inbound_buffer_size | 65535 |
| int | max_queued_packets | 4096 |
| int | outbound_buffer_size | 65535 |
| PackedStringArray | supported_protocols | PackedStringArray() |

PackedStringArray
handshake_headers
PackedStringArray()
float
heartbeat_interval
inbound_buffer_size
65535
max_queued_packets
4096
outbound_buffer_size
65535
PackedStringArray
supported_protocols
PackedStringArray()

## Methods

| Error | accept_stream(stream:StreamPeer) |
|---|---|
| void | close(code:int= 1000, reason:String= "") |
| Error | connect_to_url(url:String, tls_client_options:TLSOptions= null) |
| int | get_close_code()const |
| String | get_close_reason()const |
| String | get_connected_host()const |
| int | get_connected_port()const |
| int | get_current_outbound_buffered_amount()const |
| State | get_ready_state()const |
| String | get_requested_url()const |
| String | get_selected_protocol()const |
| void | poll() |
| Error | send(message:PackedByteArray, write_mode:WriteMode= 1) |
| Error | send_text(message:String) |
| void | set_no_delay(enabled:bool) |
| bool | was_string_packet()const |

Error
accept_stream(stream:StreamPeer)
void
close(code:int= 1000, reason:String= "")
Error
connect_to_url(url:String, tls_client_options:TLSOptions= null)
get_close_code()const
String
get_close_reason()const
String
get_connected_host()const
get_connected_port()const
get_current_outbound_buffered_amount()const
State
get_ready_state()const
String
get_requested_url()const
String
get_selected_protocol()const
void
poll()
Error
send(message:PackedByteArray, write_mode:WriteMode= 1)
Error
send_text(message:String)
void
set_no_delay(enabled:bool)
bool
was_string_packet()const

## Enumerations

enumWriteMode:🔗
WriteModeWRITE_MODE_TEXT=0
Specifies that WebSockets messages should be transferred as text payload (only valid UTF-8 is allowed).
WriteModeWRITE_MODE_BINARY=1
Specifies that WebSockets messages should be transferred as binary payload (any byte combination is allowed).
enumState:🔗
StateSTATE_CONNECTING=0
Socket has been created. The connection is not yet open.
StateSTATE_OPEN=1
The connection is open and ready to communicate.
StateSTATE_CLOSING=2
The connection is in the process of closing. This means a close request has been sent to the remote peer but confirmation has not been received.
StateSTATE_CLOSED=3
The connection is closed or couldn't be opened.

## Property Descriptions

PackedStringArrayhandshake_headers=PackedStringArray()🔗

- voidset_handshake_headers(value:PackedStringArray)
voidset_handshake_headers(value:PackedStringArray)
- PackedStringArrayget_handshake_headers()
PackedStringArrayget_handshake_headers()
The extra HTTP headers to be sent during the WebSocket handshake.
Note:Not supported in Web exports due to browsers' restrictions.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedStringArrayfor more details.
floatheartbeat_interval=0.0🔗
- voidset_heartbeat_interval(value:float)
voidset_heartbeat_interval(value:float)
- floatget_heartbeat_interval()
floatget_heartbeat_interval()
The interval (in seconds) at which the peer will automatically send WebSocket "ping" control frames. When set to0, no "ping" control frames will be sent.
Note:Has no effect in Web exports due to browser restrictions.
intinbound_buffer_size=65535🔗
- voidset_inbound_buffer_size(value:int)
voidset_inbound_buffer_size(value:int)
- intget_inbound_buffer_size()
intget_inbound_buffer_size()
The size of the input buffer in bytes (roughly the maximum amount of memory that will be allocated for the inbound packets).
intmax_queued_packets=4096🔗
- voidset_max_queued_packets(value:int)
voidset_max_queued_packets(value:int)
- intget_max_queued_packets()
intget_max_queued_packets()
The maximum amount of packets that will be allowed in the queues (both inbound and outbound).
intoutbound_buffer_size=65535🔗
- voidset_outbound_buffer_size(value:int)
voidset_outbound_buffer_size(value:int)
- intget_outbound_buffer_size()
intget_outbound_buffer_size()
The size of the input buffer in bytes (roughly the maximum amount of memory that will be allocated for the outbound packets).
PackedStringArraysupported_protocols=PackedStringArray()🔗
- voidset_supported_protocols(value:PackedStringArray)
voidset_supported_protocols(value:PackedStringArray)
- PackedStringArrayget_supported_protocols()
PackedStringArrayget_supported_protocols()
The WebSocket sub-protocols allowed during the WebSocket handshake.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedStringArrayfor more details.

## Method Descriptions

Erroraccept_stream(stream:StreamPeer)🔗
Accepts a peer connection performing the HTTP handshake as a WebSocket server. Thestreammust be a valid TCP stream retrieved viaTCPServer.take_connection(), or a TLS stream accepted viaStreamPeerTLS.accept_stream().
Note:Not supported in Web exports due to browsers' restrictions.
voidclose(code:int= 1000, reason:String= "")🔗
Closes this WebSocket connection.
codeis the status code for the closure (seeRFC 6455 section 7.4for a list of valid status codes). Ifcodeis negative, the connection will be closed immediately without notifying the remote peer.
reasonis the human-readable reason for closing the connection. It can be any UTF-8 string that's smaller than 123 bytes.
Note:To achieve a clean closure, you will need to keep polling untilSTATE_CLOSEDis reached.
Note:The Web export might not support all status codes. Please refer to browser-specific documentation for more details.
Errorconnect_to_url(url:String, tls_client_options:TLSOptions= null)🔗
Connects to the given URL. TLS certificates will be verified against the hostname when connecting using thewss://protocol. You can pass the optionaltls_client_optionsparameter to customize the trusted certification authorities, or disable the common name verification. SeeTLSOptions.client()andTLSOptions.client_unsafe().
Note:This method is non-blocking, and will return@GlobalScope.OKbefore the connection is established as long as the provided parameters are valid and the peer is not in an invalid state (e.g. already connected). Regularly callpoll()(e.g. duringNodeprocess) and check the result ofget_ready_state()to know whether the connection succeeds or fails.
Note:To avoid mixed content warnings or errors in Web, you may have to use aurlthat starts withwss://(secure) instead ofws://. When doing so, make sure to use the fully qualified domain name that matches the one defined in the server's TLS certificate. Do not connect directly via the IP address forwss://connections, as it won't match with the TLS certificate.
intget_close_code()const🔗
Returns the received WebSocket close frame status code, or-1when the connection was not cleanly closed. Only call this method whenget_ready_state()returnsSTATE_CLOSED.
Stringget_close_reason()const🔗
Returns the received WebSocket close frame status reason string. Only call this method whenget_ready_state()returnsSTATE_CLOSED.
Stringget_connected_host()const🔗
Returns the IP address of the connected peer.
Note:Not available in the Web export.
intget_connected_port()const🔗
Returns the remote port of the connected peer.
Note:Not available in the Web export.
intget_current_outbound_buffered_amount()const🔗
Returns the current amount of data in the outbound websocket buffer.Note:Web exports use WebSocket.bufferedAmount, while other platforms use an internal buffer.
Stateget_ready_state()const🔗
Returns the ready state of the connection.
Stringget_requested_url()const🔗
Returns the URL requested by this peer. The URL is derived from theurlpassed toconnect_to_url()or from the HTTP headers when acting as server (i.e. when usingaccept_stream()).
Stringget_selected_protocol()const🔗
Returns the selected WebSocket sub-protocol for this connection or an empty string if the sub-protocol has not been selected yet.
voidpoll()🔗
Updates the connection state and receive incoming packets. Call this function regularly to keep it in a clean state.
Errorsend(message:PackedByteArray, write_mode:WriteMode= 1)🔗
Sends the givenmessageusing the desiredwrite_mode. When sending aString, prefer usingsend_text().
Errorsend_text(message:String)🔗
Sends the givenmessageusing WebSocket text mode. Prefer this method overPacketPeer.put_packet()when interacting with third-party text-based API (e.g. when usingJSONformatted messages).
voidset_no_delay(enabled:bool)🔗
Disable Nagle's algorithm on the underlying TCP socket (default). SeeStreamPeerTCP.set_no_delay()for more information.
Note:Not available in the Web export.
boolwas_string_packet()const🔗
Returnstrueif the last received packet was sent as a text payload. SeeWriteMode.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
