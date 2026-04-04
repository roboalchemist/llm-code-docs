:github_url: hide

> **META**
	:keywords: dns



# IP

**Inherits:** [Object<class_Object>]

Internet protocol (IP) support functions such as DNS resolution.


## Description

IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see [StreamPeerTCP<class_StreamPeerTCP>] and [TCPServer<class_TCPServer>]). IP provides DNS hostname resolution support, both blocking and threaded.


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`clear_cache<class_IP_method_clear_cache>`\ (\ hostname\: :ref:`String<class_String>` = ""\ )                                                                 |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`erase_resolve_item<class_IP_method_erase_resolve_item>`\ (\ id\: :ref:`int<class_int>`\ )                                                                    |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`get_local_addresses<class_IP_method_get_local_addresses>`\ (\ ) |const|                                                                                      |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_local_interfaces<class_IP_method_get_local_interfaces>`\ (\ ) |const|                                                                                    |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`get_resolve_item_address<class_IP_method_get_resolve_item_address>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                        | :ref:`get_resolve_item_addresses<class_IP_method_get_resolve_item_addresses>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                            |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ResolverStatus<enum_IP_ResolverStatus>`                    | :ref:`get_resolve_item_status<class_IP_method_get_resolve_item_status>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                  |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`resolve_hostname<class_IP_method_resolve_hostname>`\ (\ host\: :ref:`String<class_String>`, ip_type\: :ref:`Type<enum_IP_Type>` = 3\ )                       |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`resolve_hostname_addresses<class_IP_method_resolve_hostname_addresses>`\ (\ host\: :ref:`String<class_String>`, ip_type\: :ref:`Type<enum_IP_Type>` = 3\ )   |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`resolve_hostname_queue_item<class_IP_method_resolve_hostname_queue_item>`\ (\ host\: :ref:`String<class_String>`, ip_type\: :ref:`Type<enum_IP_Type>` = 3\ ) |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ResolverStatus**: [🔗<enum_IP_ResolverStatus>]



[ResolverStatus<enum_IP_ResolverStatus>] **RESOLVER_STATUS_NONE** = `0`

DNS hostname resolver status: No status.



[ResolverStatus<enum_IP_ResolverStatus>] **RESOLVER_STATUS_WAITING** = `1`

DNS hostname resolver status: Waiting.



[ResolverStatus<enum_IP_ResolverStatus>] **RESOLVER_STATUS_DONE** = `2`

DNS hostname resolver status: Done.



[ResolverStatus<enum_IP_ResolverStatus>] **RESOLVER_STATUS_ERROR** = `3`

DNS hostname resolver status: Error.


----



enum **Type**: [🔗<enum_IP_Type>]



[Type<enum_IP_Type>] **TYPE_NONE** = `0`

Address type: None.



[Type<enum_IP_Type>] **TYPE_IPV4** = `1`

Address type: Internet protocol version 4 (IPv4).



[Type<enum_IP_Type>] **TYPE_IPV6** = `2`

Address type: Internet protocol version 6 (IPv6).



[Type<enum_IP_Type>] **TYPE_ANY** = `3`

Address type: Any.


----


## Constants



**RESOLVER_MAX_QUERIES** = `256` [🔗<class_IP_constant_RESOLVER_MAX_QUERIES>]

Maximum number of concurrent DNS resolver queries allowed, [RESOLVER_INVALID_ID<class_IP_constant_RESOLVER_INVALID_ID>] is returned if exceeded.



**RESOLVER_INVALID_ID** = `-1` [🔗<class_IP_constant_RESOLVER_INVALID_ID>]

Invalid ID constant. Returned if [RESOLVER_MAX_QUERIES<class_IP_constant_RESOLVER_MAX_QUERIES>] is exceeded.


----


## Method Descriptions



|void| **clear_cache**\ (\ hostname\: [String<class_String>] = ""\ ) [🔗<class_IP_method_clear_cache>]

Removes all of a `hostname`'s cached references. If no `hostname` is given, all cached IP addresses are removed.


----



|void| **erase_resolve_item**\ (\ id\: [int<class_int>]\ ) [🔗<class_IP_method_erase_resolve_item>]

Removes a given item `id` from the queue. This should be used to free a queue after it has completed to enable more queries to happen.


----



[PackedStringArray<class_PackedStringArray>] **get_local_addresses**\ (\ ) |const| [🔗<class_IP_method_get_local_addresses>]

Returns all the user's current IPv4 and IPv6 addresses as an array.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_local_interfaces**\ (\ ) |const| [🔗<class_IP_method_get_local_interfaces>]

Returns all network adapters as an array.

Each adapter is a dictionary of the form:

::

    {
        "index": "1", # Interface index.
        "name": "eth0", # Interface name.
        "friendly": "Ethernet One", # A friendly name (might be empty).
        "addresses": ["192.168.1.101"], # An array of IP addresses associated to this interface.
    }


----



[String<class_String>] **get_resolve_item_address**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_IP_method_get_resolve_item_address>]

Returns a queued hostname's IP address, given its queue `id`. Returns an empty string on error or if resolution hasn't happened yet (see [get_resolve_item_status()<class_IP_method_get_resolve_item_status>]).


----



[Array<class_Array>] **get_resolve_item_addresses**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_IP_method_get_resolve_item_addresses>]

Returns resolved addresses, or an empty array if an error happened or resolution didn't happen yet (see [get_resolve_item_status()<class_IP_method_get_resolve_item_status>]).


----



[ResolverStatus<enum_IP_ResolverStatus>] **get_resolve_item_status**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_IP_method_get_resolve_item_status>]

Returns a queued hostname's status as a [ResolverStatus<enum_IP_ResolverStatus>] constant, given its queue `id`.


----



[String<class_String>] **resolve_hostname**\ (\ host\: [String<class_String>], ip_type\: [Type<enum_IP_Type>] = 3\ ) [🔗<class_IP_method_resolve_hostname>]

Returns a given hostname's IPv4 or IPv6 address when resolved (blocking-type method). The address type returned depends on the [Type<enum_IP_Type>] constant given as `ip_type`.


----



[PackedStringArray<class_PackedStringArray>] **resolve_hostname_addresses**\ (\ host\: [String<class_String>], ip_type\: [Type<enum_IP_Type>] = 3\ ) [🔗<class_IP_method_resolve_hostname_addresses>]

Resolves a given hostname in a blocking way. Addresses are returned as an [Array<class_Array>] of IPv4 or IPv6 addresses depending on `ip_type`.


----



[int<class_int>] **resolve_hostname_queue_item**\ (\ host\: [String<class_String>], ip_type\: [Type<enum_IP_Type>] = 3\ ) [🔗<class_IP_method_resolve_hostname_queue_item>]

Creates a queue item to resolve a hostname to an IPv4 or IPv6 address depending on the [Type<enum_IP_Type>] constant given as `ip_type`. Returns the queue ID if successful, or [RESOLVER_INVALID_ID<class_IP_constant_RESOLVER_INVALID_ID>] on error.

