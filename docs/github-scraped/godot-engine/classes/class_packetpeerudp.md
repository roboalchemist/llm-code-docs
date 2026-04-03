:github_url: hide



# PacketPeerUDP

**Inherits:** [PacketPeer<class_PacketPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

UDP packet peer.


## Description

UDP packet peer. Can be used to send and receive raw UDP packets as well as [Variant<class_Variant>]\ s.

\ **Example:** Send a packet:

::

    var peer = PacketPeerUDP.new()

    # Optionally, you can select the local port used to send the packet.
    peer.bind(4444)

    peer.set_dest_address("1.1.1.1", 4433)
    peer.put_packet("hello".to_utf8_buffer())

\ **Example:** Listen for packets:

::

    var peer

    func _ready():
        peer = PacketPeerUDP.new()
        peer.bind(4433)


    func _process(_delta):
        if peer.get_available_packet_count() > 0:
            var array_bytes = peer.get_packet()
            var packet_string = array_bytes.get_string_from_ascii()
            print("Received message: ", packet_string)

\ **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`bind<class_PacketPeerUDP_method_bind>`\ (\ port\: :ref:`int<class_int>`, bind_address\: :ref:`String<class_String>` = "*", recv_buf_size\: :ref:`int<class_int>` = 65536\ )   |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`close<class_PacketPeerUDP_method_close>`\ (\ )                                                                                                                                |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`connect_to_host<class_PacketPeerUDP_method_connect_to_host>`\ (\ host\: :ref:`String<class_String>`, port\: :ref:`int<class_int>`\ )                                          |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_local_port<class_PacketPeerUDP_method_get_local_port>`\ (\ ) |const|                                                                                                      |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_packet_ip<class_PacketPeerUDP_method_get_packet_ip>`\ (\ ) |const|                                                                                                        |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_packet_port<class_PacketPeerUDP_method_get_packet_port>`\ (\ ) |const|                                                                                                    |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`is_bound<class_PacketPeerUDP_method_is_bound>`\ (\ ) |const|                                                                                                                  |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`is_socket_connected<class_PacketPeerUDP_method_is_socket_connected>`\ (\ ) |const|                                                                                            |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`join_multicast_group<class_PacketPeerUDP_method_join_multicast_group>`\ (\ multicast_address\: :ref:`String<class_String>`, interface_name\: :ref:`String<class_String>`\ )   |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`leave_multicast_group<class_PacketPeerUDP_method_leave_multicast_group>`\ (\ multicast_address\: :ref:`String<class_String>`, interface_name\: :ref:`String<class_String>`\ ) |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_broadcast_enabled<class_PacketPeerUDP_method_set_broadcast_enabled>`\ (\ enabled\: :ref:`bool<class_bool>`\ )                                                             |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`set_dest_address<class_PacketPeerUDP_method_set_dest_address>`\ (\ host\: :ref:`String<class_String>`, port\: :ref:`int<class_int>`\ )                                        |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`wait<class_PacketPeerUDP_method_wait>`\ (\ )                                                                                                                                  |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **bind**\ (\ port\: [int<class_int>], bind_address\: [String<class_String>] = "*", recv_buf_size\: [int<class_int>] = 65536\ ) [🔗<class_PacketPeerUDP_method_bind>]

Binds this **PacketPeerUDP** to the specified `port` and `bind_address` with a buffer size `recv_buf_size`, allowing it to receive incoming packets.

If `bind_address` is set to `"*"` (default), the peer will be bound on all available addresses (both IPv4 and IPv6).

If `bind_address` is set to `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6), the peer will be bound to all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`, `"::1"`, etc.), the peer will only be bound to the interface with that address (or fail if no interface with the given address exists).


----



|void| **close**\ (\ ) [🔗<class_PacketPeerUDP_method_close>]

Closes the **PacketPeerUDP**'s underlying UDP socket.


----



[Error<enum_@GlobalScope_Error>] **connect_to_host**\ (\ host\: [String<class_String>], port\: [int<class_int>]\ ) [🔗<class_PacketPeerUDP_method_connect_to_host>]

Calling this method connects this UDP peer to the given `host`/`port` pair. UDP is in reality connectionless, so this option only means that incoming packets from different addresses are automatically discarded, and that outgoing packets are always sent to the connected address (future calls to [set_dest_address()<class_PacketPeerUDP_method_set_dest_address>] are not allowed). This method does not send any data to the remote peer, to do that, use [PacketPeer.put_var()<class_PacketPeer_method_put_var>] or [PacketPeer.put_packet()<class_PacketPeer_method_put_packet>] as usual. See also [UDPServer<class_UDPServer>].

\ **Note:** Connecting to the remote peer does not help to protect from malicious attacks like IP spoofing, etc. Think about using an encryption technique like TLS or DTLS if you feel like your application is transferring sensitive information.


----



[int<class_int>] **get_local_port**\ (\ ) |const| [🔗<class_PacketPeerUDP_method_get_local_port>]

Returns the local port to which this peer is bound.


----



[String<class_String>] **get_packet_ip**\ (\ ) |const| [🔗<class_PacketPeerUDP_method_get_packet_ip>]

Returns the IP of the remote peer that sent the last packet(that was received with [PacketPeer.get_packet()<class_PacketPeer_method_get_packet>] or [PacketPeer.get_var()<class_PacketPeer_method_get_var>]).


----



[int<class_int>] **get_packet_port**\ (\ ) |const| [🔗<class_PacketPeerUDP_method_get_packet_port>]

Returns the port of the remote peer that sent the last packet(that was received with [PacketPeer.get_packet()<class_PacketPeer_method_get_packet>] or [PacketPeer.get_var()<class_PacketPeer_method_get_var>]).


----



[bool<class_bool>] **is_bound**\ (\ ) |const| [🔗<class_PacketPeerUDP_method_is_bound>]

Returns whether this **PacketPeerUDP** is bound to an address and can receive packets.


----



[bool<class_bool>] **is_socket_connected**\ (\ ) |const| [🔗<class_PacketPeerUDP_method_is_socket_connected>]

Returns `true` if the UDP socket is open and has been connected to a remote address. See [connect_to_host()<class_PacketPeerUDP_method_connect_to_host>].


----



[Error<enum_@GlobalScope_Error>] **join_multicast_group**\ (\ multicast_address\: [String<class_String>], interface_name\: [String<class_String>]\ ) [🔗<class_PacketPeerUDP_method_join_multicast_group>]

Joins the multicast group specified by `multicast_address` using the interface identified by `interface_name`.

You can join the same multicast group with multiple interfaces. Use [IP.get_local_interfaces()<class_IP_method_get_local_interfaces>] to know which are available.

\ **Note:** Some Android devices might require the `CHANGE_WIFI_MULTICAST_STATE` permission for multicast to work.


----



[Error<enum_@GlobalScope_Error>] **leave_multicast_group**\ (\ multicast_address\: [String<class_String>], interface_name\: [String<class_String>]\ ) [🔗<class_PacketPeerUDP_method_leave_multicast_group>]

Removes the interface identified by `interface_name` from the multicast group specified by `multicast_address`.


----



|void| **set_broadcast_enabled**\ (\ enabled\: [bool<class_bool>]\ ) [🔗<class_PacketPeerUDP_method_set_broadcast_enabled>]

Enable or disable sending of broadcast packets (e.g. `set_dest_address("255.255.255.255", 4343)`. This option is disabled by default.

\ **Note:** Some Android devices might require the `CHANGE_WIFI_MULTICAST_STATE` permission and this option to be enabled to receive broadcast packets too.


----



[Error<enum_@GlobalScope_Error>] **set_dest_address**\ (\ host\: [String<class_String>], port\: [int<class_int>]\ ) [🔗<class_PacketPeerUDP_method_set_dest_address>]

Sets the destination address and port for sending packets and variables. A hostname will be resolved using DNS if needed.

\ **Note:** [set_broadcast_enabled()<class_PacketPeerUDP_method_set_broadcast_enabled>] must be enabled before sending packets to a broadcast address (e.g. `255.255.255.255`).


----



[Error<enum_@GlobalScope_Error>] **wait**\ (\ ) [🔗<class_PacketPeerUDP_method_wait>]

Waits for a packet to arrive on the bound address. See [bind()<class_PacketPeerUDP_method_bind>].

\ **Note:** [wait()<class_PacketPeerUDP_method_wait>] can't be interrupted once it has been called. This can be worked around by allowing the other party to send a specific "death pill" packet like this:


> **TABS**
>

    socket = PacketPeerUDP.new()
    # Server
    socket.set_dest_address("127.0.0.1", 789)
    socket.put_packet("Time to stop".to_ascii_buffer())

    # Client
    while socket.wait() == OK:
        var data = socket.get_packet().get_string_from_ascii()
        if data == "Time to stop":
            return


    var socket = new PacketPeerUdp();
    // Server
    socket.SetDestAddress("127.0.0.1", 789);
    socket.PutPacket("Time to stop".ToAsciiBuffer());

    // Client
    while (socket.Wait() == OK)
    {
        string data = socket.GetPacket().GetStringFromASCII();
        if (data == "Time to stop")
        {
            return;
## }



