:github_url: hide



# SocketServer

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [TCPServer<class_TCPServer>], [UDSServer<class_UDSServer>]

An abstract class for servers based on sockets.


## Description

A socket server.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_connection_available<class_SocketServer_method_is_connection_available>`\ (\ ) |const| |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_listening<class_SocketServer_method_is_listening>`\ (\ ) |const|                       |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`stop<class_SocketServer_method_stop>`\ (\ )                                               |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`StreamPeerSocket<class_StreamPeerSocket>` | :ref:`take_socket_connection<class_SocketServer_method_take_socket_connection>`\ (\ )           |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **is_connection_available**\ (\ ) |const| [🔗<class_SocketServer_method_is_connection_available>]

Returns `true` if a connection is available for taking.


----



[bool<class_bool>] **is_listening**\ (\ ) |const| [🔗<class_SocketServer_method_is_listening>]

Returns `true` if the server is currently listening for connections.


----



|void| **stop**\ (\ ) [🔗<class_SocketServer_method_stop>]

Stops listening.


----



[StreamPeerSocket<class_StreamPeerSocket>] **take_socket_connection**\ (\ ) [🔗<class_SocketServer_method_take_socket_connection>]

If a connection is available, returns a StreamPeerSocket with the connection.

