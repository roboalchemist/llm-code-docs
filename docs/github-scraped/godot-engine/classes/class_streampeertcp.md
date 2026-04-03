:github_url: hide



# StreamPeerTCP

**Inherits:** [StreamPeerSocket<class_StreamPeerSocket>] **<** [StreamPeer<class_StreamPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A stream peer that handles TCP connections.


## Description

A stream peer that handles TCP connections. This object can be used to connect to TCP servers, or also is returned by a TCP server.

\ **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`bind<class_StreamPeerTCP_method_bind>`\ (\ port\: :ref:`int<class_int>`, host\: :ref:`String<class_String>` = "*"\ )                 |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`connect_to_host<class_StreamPeerTCP_method_connect_to_host>`\ (\ host\: :ref:`String<class_String>`, port\: :ref:`int<class_int>`\ ) |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_connected_host<class_StreamPeerTCP_method_get_connected_host>`\ (\ ) |const|                                                     |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_connected_port<class_StreamPeerTCP_method_get_connected_port>`\ (\ ) |const|                                                     |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_local_port<class_StreamPeerTCP_method_get_local_port>`\ (\ ) |const|                                                             |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_no_delay<class_StreamPeerTCP_method_set_no_delay>`\ (\ enabled\: :ref:`bool<class_bool>`\ )                                      |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **bind**\ (\ port\: [int<class_int>], host\: [String<class_String>] = "*"\ ) [🔗<class_StreamPeerTCP_method_bind>]

Opens the TCP socket, and binds it to the specified local address.

This method is generally not needed, and only used to force the subsequent call to [connect_to_host()<class_StreamPeerTCP_method_connect_to_host>] to use the specified `host` and `port` as source address. This can be desired in some NAT punchthrough techniques, or when forcing the source network interface.


----



[Error<enum_@GlobalScope_Error>] **connect_to_host**\ (\ host\: [String<class_String>], port\: [int<class_int>]\ ) [🔗<class_StreamPeerTCP_method_connect_to_host>]

Connects to the specified `host:port` pair. A hostname will be resolved if valid. Returns [@GlobalScope.OK<class_@GlobalScope_constant_OK>] on success.


----



[String<class_String>] **get_connected_host**\ (\ ) |const| [🔗<class_StreamPeerTCP_method_get_connected_host>]

Returns the IP of this peer.


----



[int<class_int>] **get_connected_port**\ (\ ) |const| [🔗<class_StreamPeerTCP_method_get_connected_port>]

Returns the port of this peer.


----



[int<class_int>] **get_local_port**\ (\ ) |const| [🔗<class_StreamPeerTCP_method_get_local_port>]

Returns the local port to which this peer is bound.


----



|void| **set_no_delay**\ (\ enabled\: [bool<class_bool>]\ ) [🔗<class_StreamPeerTCP_method_set_no_delay>]

If `enabled` is `true`, packets will be sent immediately. If `enabled` is `false` (the default), packet transfers will be delayed and combined using [Nagle's algorithm ](https://en.wikipedia.org/wiki/Nagle%27s_algorithm)_.

\ **Note:** It's recommended to leave this disabled for applications that send large packets or need to transfer a lot of data, as enabling this can decrease the total available bandwidth.

