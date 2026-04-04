:github_url: hide



# UDPServer

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Helper class to implement a UDP server.


## Description

A simple server that opens a UDP socket and returns connected [PacketPeerUDP<class_PacketPeerUDP>] upon receiving new packets. See also [PacketPeerUDP.connect_to_host()<class_PacketPeerUDP_method_connect_to_host>].

After starting the server ([listen()<class_UDPServer_method_listen>]), you will need to [poll()<class_UDPServer_method_poll>] it at regular intervals (e.g. inside [Node._process()<class_Node_private_method__process>]) for it to process new packets, delivering them to the appropriate [PacketPeerUDP<class_PacketPeerUDP>], and taking new connections.

Below a small example of how it can be used:


> **TABS**
>

    # server_node.gd
    class_name ServerNode
    extends Node

    var server = UDPServer.new()
    var peers = []

    func _ready():
        server.listen(4242)

    func _process(delta):
        server.poll() # Important!
        if server.is_connection_available():
            var peer = server.take_connection()
            var packet = peer.get_packet()
            print("Accepted peer: %s:%s" % [peer.get_packet_ip(), peer.get_packet_port()])
            print("Received data: %s" % [packet.get_string_from_utf8()])
            # Reply so it knows we received the message.
            peer.put_packet(packet)
            # Keep a reference so we can keep contacting the remote peer.
            peers.append(peer)

        for i in range(0, peers.size()):
            pass # Do something with the connected peers.


    // ServerNode.cs
    using Godot;
    using System.Collections.Generic;

    public partial class ServerNode : Node
    {
        private UdpServer _server = new UdpServer();
        private List<PacketPeerUdp> _peers  = new List<PacketPeerUdp>();

        public override void _Ready()
        {
            _server.Listen(4242);
        }

        public override void _Process(double delta)
        {
            _server.Poll(); // Important!
            if (_server.IsConnectionAvailable())
            {
                PacketPeerUdp peer = _server.TakeConnection();
                byte[] packet = peer.GetPacket();
                GD.Print($"Accepted Peer: {peer.GetPacketIP()}:{peer.GetPacketPort()}");
                GD.Print($"Received Data: {packet.GetStringFromUtf8()}");
                // Reply so it knows we received the message.
                peer.PutPacket(packet);
                // Keep a reference so we can keep contacting the remote peer.
                _peers.Add(peer);
            }
            foreach (var peer in _peers)
            {
                // Do something with the peers.
## }
    }




> **TABS**
>

    # client_node.gd
    class_name ClientNode
    extends Node

    var udp = PacketPeerUDP.new()
    var connected = false

    func _ready():
        udp.connect_to_host("127.0.0.1", 4242)

    func _process(delta):
        if !connected:
            # Try to contact server
            udp.put_packet("The answer is... 42!".to_utf8_buffer())
        if udp.get_available_packet_count() > 0:
            print("Connected: %s" % udp.get_packet().get_string_from_utf8())
            connected = true


    // ClientNode.cs
    using Godot;

    public partial class ClientNode : Node
    {
        private PacketPeerUdp _udp = new PacketPeerUdp();
        private bool _connected = false;

        public override void _Ready()
        {
            _udp.ConnectToHost("127.0.0.1", 4242);
        }

        public override void _Process(double delta)
        {
            if (!_connected)
            {
                // Try to contact server
                _udp.PutPacket("The Answer Is..42!".ToUtf8Buffer());
            }
            if (_udp.GetAvailablePacketCount() > 0)
            {
                GD.Print($"Connected: {_udp.GetPacket().GetStringFromUtf8()}");
                _connected = true;
## }
    }




## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+----------------------------------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`max_pending_connections<class_UDPServer_property_max_pending_connections>` | ``16`` |
> +-----------------------+----------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`get_local_port<class_UDPServer_method_get_local_port>`\ (\ ) |const|                                                         |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`is_connection_available<class_UDPServer_method_is_connection_available>`\ (\ ) |const|                                       |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`is_listening<class_UDPServer_method_is_listening>`\ (\ ) |const|                                                             |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`     | :ref:`listen<class_UDPServer_method_listen>`\ (\ port\: :ref:`int<class_int>`, bind_address\: :ref:`String<class_String>` = "*"\ ) |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`     | :ref:`poll<class_UDPServer_method_poll>`\ (\ )                                                                                     |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`stop<class_UDPServer_method_stop>`\ (\ )                                                                                     |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PacketPeerUDP<class_PacketPeerUDP>` | :ref:`take_connection<class_UDPServer_method_take_connection>`\ (\ )                                                               |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **max_pending_connections** = `16` [🔗<class_UDPServer_property_max_pending_connections>]


- |void| **set_max_pending_connections**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_pending_connections**\ (\ )

Define the maximum number of pending connections, during [poll()<class_UDPServer_method_poll>], any new pending connection exceeding that value will be automatically dropped. Setting this value to `0` effectively prevents any new pending connection to be accepted (e.g. when all your players have connected).


----


## Method Descriptions



[int<class_int>] **get_local_port**\ (\ ) |const| [🔗<class_UDPServer_method_get_local_port>]

Returns the local port this server is listening to.


----



[bool<class_bool>] **is_connection_available**\ (\ ) |const| [🔗<class_UDPServer_method_is_connection_available>]

Returns `true` if a packet with a new address/port combination was received on the socket.


----



[bool<class_bool>] **is_listening**\ (\ ) |const| [🔗<class_UDPServer_method_is_listening>]

Returns `true` if the socket is open and listening on a port.


----



[Error<enum_@GlobalScope_Error>] **listen**\ (\ port\: [int<class_int>], bind_address\: [String<class_String>] = "*"\ ) [🔗<class_UDPServer_method_listen>]

Starts the server by opening a UDP socket listening on the given `port`. You can optionally specify a `bind_address` to only listen for packets sent to that address. See also [PacketPeerUDP.bind()<class_PacketPeerUDP_method_bind>].


----



[Error<enum_@GlobalScope_Error>] **poll**\ (\ ) [🔗<class_UDPServer_method_poll>]

Call this method at regular intervals (e.g. inside [Node._process()<class_Node_private_method__process>]) to process new packets. Any packet from a known address/port pair will be delivered to the appropriate [PacketPeerUDP<class_PacketPeerUDP>], while any packet received from an unknown address/port pair will be added as a pending connection (see [is_connection_available()<class_UDPServer_method_is_connection_available>] and [take_connection()<class_UDPServer_method_take_connection>]). The maximum number of pending connections is defined via [max_pending_connections<class_UDPServer_property_max_pending_connections>].


----



|void| **stop**\ (\ ) [🔗<class_UDPServer_method_stop>]

Stops the server, closing the UDP socket if open. Will close all connected [PacketPeerUDP<class_PacketPeerUDP>] accepted via [take_connection()<class_UDPServer_method_take_connection>] (remote peers will not be notified).


----



[PacketPeerUDP<class_PacketPeerUDP>] **take_connection**\ (\ ) [🔗<class_UDPServer_method_take_connection>]

Returns the first pending connection (connected to the appropriate address/port). Will return `null` if no new connection is available. See also [is_connection_available()<class_UDPServer_method_is_connection_available>], [PacketPeerUDP.connect_to_host()<class_PacketPeerUDP_method_connect_to_host>].

