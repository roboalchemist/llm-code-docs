:github_url: hide



# StreamPeerSocket

**Inherits:** [StreamPeer<class_StreamPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [StreamPeerTCP<class_StreamPeerTCP>], [StreamPeerUDS<class_StreamPeerUDS>]

Abstract base class for interacting with socket streams.


## Description

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+---------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`disconnect_from_host<class_StreamPeerSocket_method_disconnect_from_host>`\ (\ ) |
> +---------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`Status<enum_StreamPeerSocket_Status>` | :ref:`get_status<class_StreamPeerSocket_method_get_status>`\ (\ ) |const|             |
> +---------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`       | :ref:`poll<class_StreamPeerSocket_method_poll>`\ (\ )                                 |
> +---------------------------------------------+---------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Status**: [🔗<enum_StreamPeerSocket_Status>]



[Status<enum_StreamPeerSocket_Status>] **STATUS_NONE** = `0`

The initial status of the **StreamPeerSocket**. This is also the status after disconnecting.



[Status<enum_StreamPeerSocket_Status>] **STATUS_CONNECTING** = `1`

A status representing a **StreamPeerSocket** that is connecting to a host.



[Status<enum_StreamPeerSocket_Status>] **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerSocket** that is connected to a host.



[Status<enum_StreamPeerSocket_Status>] **STATUS_ERROR** = `3`

A status representing a **StreamPeerSocket** in error state.


----


## Method Descriptions



|void| **disconnect_from_host**\ (\ ) [🔗<class_StreamPeerSocket_method_disconnect_from_host>]

Disconnects from host.


----



[Status<enum_StreamPeerSocket_Status>] **get_status**\ (\ ) |const| [🔗<class_StreamPeerSocket_method_get_status>]

Returns the status of the connection.


----



[Error<enum_@GlobalScope_Error>] **poll**\ (\ ) [🔗<class_StreamPeerSocket_method_poll>]

Polls the socket, updating its state. See [get_status()<class_StreamPeerSocket_method_get_status>].

