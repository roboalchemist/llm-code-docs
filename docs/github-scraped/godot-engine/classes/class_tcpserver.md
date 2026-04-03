:github_url: hide



# TCPServer

**Inherits:** [SocketServer<class_SocketServer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A TCP server.


## Description

A TCP server. Listens to connections on a port and returns a [StreamPeerTCP<class_StreamPeerTCP>] when it gets an incoming connection.

\ **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`get_local_port<class_TCPServer_method_get_local_port>`\ (\ ) |const|                                                         |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`     | :ref:`listen<class_TCPServer_method_listen>`\ (\ port\: :ref:`int<class_int>`, bind_address\: :ref:`String<class_String>` = "*"\ ) |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StreamPeerTCP<class_StreamPeerTCP>` | :ref:`take_connection<class_TCPServer_method_take_connection>`\ (\ )                                                               |
> +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_local_port**\ (\ ) |const| [🔗<class_TCPServer_method_get_local_port>]

Returns the local port this server is listening to.


----



[Error<enum_@GlobalScope_Error>] **listen**\ (\ port\: [int<class_int>], bind_address\: [String<class_String>] = "*"\ ) [🔗<class_TCPServer_method_listen>]

Listen on the `port` binding to `bind_address`.

If `bind_address` is set as `"*"` (default), the server will listen on all available addresses (both IPv4 and IPv6).

If `bind_address` is set as `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6), the server will listen on all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`, `"::1"`, etc.), the server will only listen on the interface with that address (or fail if no interface with the given address exists).


----



[StreamPeerTCP<class_StreamPeerTCP>] **take_connection**\ (\ ) [🔗<class_TCPServer_method_take_connection>]

If a connection is available, returns a StreamPeerTCP with the connection.

