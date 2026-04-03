:github_url: hide



# UPNP

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Universal Plug and Play (UPnP) functions for network device discovery, querying and port forwarding.


## Description

This class can be used to discover compatible [UPNPDevice<class_UPNPDevice>]\ s on the local network and execute commands on them, like managing port mappings (for port forwarding/NAT traversal) and querying the local and remote network IP address. Note that methods on this class are synchronous and block the calling thread.

To forward a specific port (here `7777`, note both [discover()<class_UPNP_method_discover>] and [add_port_mapping()<class_UPNP_method_add_port_mapping>] can return errors that should be checked):

::

    var upnp = UPNP.new()
    upnp.discover()
    upnp.add_port_mapping(7777)

To close a specific port (e.g. after you have finished using it):

::

    upnp.delete_port_mapping(port)

\ **Note:** UPnP discovery blocks the current thread. To perform discovery without blocking the main thread, use [Thread<class_Thread>]\ s like this:

::

    # Emitted when UPnP port mapping setup is completed (regardless of success or failure).
    signal upnp_completed(error)

    # Replace this with your own server port number between 1024 and 65535.
    const SERVER_PORT = 3928
    var thread = null

    func _upnp_setup(server_port):
        # UPNP queries take some time.
        var upnp = UPNP.new()
        var err = upnp.discover()

        if err != OK:
            push_error(str(err))
            upnp_completed.emit(err)
            return

        if upnp.get_gateway() and upnp.get_gateway().is_valid_gateway():
            upnp.add_port_mapping(server_port, server_port, ProjectSettings.get_setting("application/config/name"), "UDP")
            upnp.add_port_mapping(server_port, server_port, ProjectSettings.get_setting("application/config/name"), "TCP")
            upnp_completed.emit(OK)

    func _ready():
        thread = Thread.new()
        thread.start(_upnp_setup.bind(SERVER_PORT))

    func _exit_tree():
        # Wait for thread finish here to handle game exit while the thread is running.
        thread.wait_to_finish()

\ **Terminology:** In the context of UPnP networking, "gateway" (or "internet gateway device", short IGD) refers to network devices that allow computers in the local network to access the internet ("wide area network", WAN). These gateways are often also called "routers".

\ **Pitfalls:**\ 

- As explained above, these calls are blocking and shouldn't be run on the main thread, especially as they can block for multiple seconds at a time. Use threading!

- Networking is physical and messy. Packets get lost in transit or get filtered, addresses, free ports and assigned mappings change, and devices may leave or join the network at any time. Be mindful of this, be diligent when checking and handling errors, and handle these gracefully if you can: add clear error UI, timeouts and re-try handling.

- Port mappings may change (and be removed) at any time, and the remote/external IP address of the gateway can change likewise. You should consider re-querying the external IP and try to update/refresh the port mapping periodically (for example, every 5 minutes and on networking failures).

- Not all devices support UPnP, and some users disable UPnP support. You need to handle this (e.g. documenting and requiring the user to manually forward ports, or adding alternative methods of NAT traversal, like a relay/mirror server, or NAT hole punching, STUN/TURN, etc.).

- Consider what happens on mapping conflicts. Maybe multiple users on the same network would like to play your game at the same time, or maybe another application uses the same port. Make the port configurable, and optimally choose a port automatically (re-trying with a different port on failure).

\ **Further reading:** If you want to know more about UPnP (and the Internet Gateway Device (IGD) and Port Control Protocol (PCP) specifically), [Wikipedia ](https://en.wikipedia.org/wiki/Universal_Plug_and_Play)_ is a good first stop, the specification can be found at the [Open Connectivity Foundation ](https://openconnectivity.org/developer/specifications/upnp-resources/upnp/)_ and Godot's implementation is based on the [MiniUPnP client ](https://github.com/miniupnp/miniupnp)_.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`discover_ipv6<class_UPNP_property_discover_ipv6>`                 | ``false`` |
> +-----------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`       | :ref:`discover_local_port<class_UPNP_property_discover_local_port>`     | ``0``     |
> +-----------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`discover_multicast_if<class_UPNP_property_discover_multicast_if>` | ``""``    |
> +-----------------------------+-------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`add_device<class_UPNP_method_add_device>`\ (\ device\: :ref:`UPNPDevice<class_UPNPDevice>`\ )                                                                                                                                                                            |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`add_port_mapping<class_UPNP_method_add_port_mapping>`\ (\ port\: :ref:`int<class_int>`, port_internal\: :ref:`int<class_int>` = 0, desc\: :ref:`String<class_String>` = "", proto\: :ref:`String<class_String>` = "UDP", duration\: :ref:`int<class_int>` = 0\ ) |const| |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`clear_devices<class_UPNP_method_clear_devices>`\ (\ )                                                                                                                                                                                                                    |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`delete_port_mapping<class_UPNP_method_delete_port_mapping>`\ (\ port\: :ref:`int<class_int>`, proto\: :ref:`String<class_String>` = "UDP"\ ) |const|                                                                                                                     |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`discover<class_UPNP_method_discover>`\ (\ timeout\: :ref:`int<class_int>` = 2000, ttl\: :ref:`int<class_int>` = 2, device_filter\: :ref:`String<class_String>` = "InternetGatewayDevice"\ )                                                                              |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`UPNPDevice<class_UPNPDevice>` | :ref:`get_device<class_UPNP_method_get_device>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                   |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`               | :ref:`get_device_count<class_UPNP_method_get_device_count>`\ (\ ) |const|                                                                                                                                                                                                      |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`UPNPDevice<class_UPNPDevice>` | :ref:`get_gateway<class_UPNP_method_get_gateway>`\ (\ ) |const|                                                                                                                                                                                                                |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`         | :ref:`query_external_address<class_UPNP_method_query_external_address>`\ (\ ) |const|                                                                                                                                                                                          |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`remove_device<class_UPNP_method_remove_device>`\ (\ index\: :ref:`int<class_int>`\ )                                                                                                                                                                                     |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_device<class_UPNP_method_set_device>`\ (\ index\: :ref:`int<class_int>`, device\: :ref:`UPNPDevice<class_UPNPDevice>`\ )                                                                                                                                             |
> +-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **UPNPResult**: [🔗<enum_UPNP_UPNPResult>]



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_SUCCESS** = `0`

UPNP command or discovery was successful.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_NOT_AUTHORIZED** = `1`

Not authorized to use the command on the [UPNPDevice<class_UPNPDevice>]. May be returned when the user disabled UPNP on their router.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_PORT_MAPPING_NOT_FOUND** = `2`

No port mapping was found for the given port, protocol combination on the given [UPNPDevice<class_UPNPDevice>].



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INCONSISTENT_PARAMETERS** = `3`

Inconsistent parameters.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_NO_SUCH_ENTRY_IN_ARRAY** = `4`

No such entry in array. May be returned if a given port, protocol combination is not found on a [UPNPDevice<class_UPNPDevice>].



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_ACTION_FAILED** = `5`

The action failed.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_SRC_IP_WILDCARD_NOT_PERMITTED** = `6`

The [UPNPDevice<class_UPNPDevice>] does not allow wildcard values for the source IP address.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_EXT_PORT_WILDCARD_NOT_PERMITTED** = `7`

The [UPNPDevice<class_UPNPDevice>] does not allow wildcard values for the external port.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INT_PORT_WILDCARD_NOT_PERMITTED** = `8`

The [UPNPDevice<class_UPNPDevice>] does not allow wildcard values for the internal port.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_REMOTE_HOST_MUST_BE_WILDCARD** = `9`

The remote host value must be a wildcard.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_EXT_PORT_MUST_BE_WILDCARD** = `10`

The external port value must be a wildcard.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_NO_PORT_MAPS_AVAILABLE** = `11`

No port maps are available. May also be returned if port mapping functionality is not available.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_CONFLICT_WITH_OTHER_MECHANISM** = `12`

Conflict with other mechanism. May be returned instead of [UPNP_RESULT_CONFLICT_WITH_OTHER_MAPPING<class_UPNP_constant_UPNP_RESULT_CONFLICT_WITH_OTHER_MAPPING>] if a port mapping conflicts with an existing one.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_CONFLICT_WITH_OTHER_MAPPING** = `13`

Conflict with an existing port mapping.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_SAME_PORT_VALUES_REQUIRED** = `14`

External and internal port values must be the same.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_ONLY_PERMANENT_LEASE_SUPPORTED** = `15`

Only permanent leases are supported. Do not use the `duration` parameter when adding port mappings.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_GATEWAY** = `16`

Invalid gateway.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_PORT** = `17`

Invalid port.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_PROTOCOL** = `18`

Invalid protocol.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_DURATION** = `19`

Invalid duration.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_ARGS** = `20`

Invalid arguments.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_RESPONSE** = `21`

Invalid response.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_INVALID_PARAM** = `22`

Invalid parameter.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_HTTP_ERROR** = `23`

HTTP error.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_SOCKET_ERROR** = `24`

Socket error.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_MEM_ALLOC_ERROR** = `25`

Error allocating memory.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_NO_GATEWAY** = `26`

No gateway available. You may need to call [discover()<class_UPNP_method_discover>] first, or discovery didn't detect any valid IGDs (InternetGatewayDevices).



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_NO_DEVICES** = `27`

No devices available. You may need to call [discover()<class_UPNP_method_discover>] first, or discovery didn't detect any valid [UPNPDevice<class_UPNPDevice>]\ s.



[UPNPResult<enum_UPNP_UPNPResult>] **UPNP_RESULT_UNKNOWN_ERROR** = `28`

Unknown error.


----


## Property Descriptions



[bool<class_bool>] **discover_ipv6** = `false` [🔗<class_UPNP_property_discover_ipv6>]


- |void| **set_discover_ipv6**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_discover_ipv6**\ (\ )

If `true`, IPv6 is used for [UPNPDevice<class_UPNPDevice>] discovery.


----



[int<class_int>] **discover_local_port** = `0` [🔗<class_UPNP_property_discover_local_port>]


- |void| **set_discover_local_port**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_discover_local_port**\ (\ )

If `0`, the local port to use for discovery is chosen automatically by the system. If `1`, discovery will be done from the source port 1900 (same as destination port). Otherwise, the value will be used as the port.


----



[String<class_String>] **discover_multicast_if** = `""` [🔗<class_UPNP_property_discover_multicast_if>]


- |void| **set_discover_multicast_if**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_discover_multicast_if**\ (\ )

Multicast interface to use for discovery. Uses the default multicast interface if empty.


----


## Method Descriptions



|void| **add_device**\ (\ device\: [UPNPDevice<class_UPNPDevice>]\ ) [🔗<class_UPNP_method_add_device>]

Adds the given [UPNPDevice<class_UPNPDevice>] to the list of discovered devices.


----



[int<class_int>] **add_port_mapping**\ (\ port\: [int<class_int>], port_internal\: [int<class_int>] = 0, desc\: [String<class_String>] = "", proto\: [String<class_String>] = "UDP", duration\: [int<class_int>] = 0\ ) |const| [🔗<class_UPNP_method_add_port_mapping>]

Adds a mapping to forward the external `port` (between 1 and 65535, although recommended to use port 1024 or above) on the default gateway (see [get_gateway()<class_UPNP_method_get_gateway>]) to the `port_internal` on the local machine for the given protocol `proto` (either `"TCP"` or `"UDP"`, with UDP being the default). If a port mapping for the given port and protocol combination already exists on that gateway device, this method tries to overwrite it. If that is not desired, you can retrieve the gateway manually with [get_gateway()<class_UPNP_method_get_gateway>] and call [add_port_mapping()<class_UPNP_method_add_port_mapping>] on it, if any. Note that forwarding a well-known port (below 1024) with UPnP may fail depending on the device.

Depending on the gateway device, if a mapping for that port already exists, it will either be updated or it will refuse this command due to that conflict, especially if the existing mapping for that port wasn't created via UPnP or points to a different network address (or device) than this one.

If `port_internal` is `0` (the default), the same port number is used for both the external and the internal port (the `port` value).

The description (`desc`) is shown in some routers management UIs and can be used to point out which application added the mapping.

The mapping's lease `duration` can be limited by specifying a duration in seconds. The default of `0` means no duration, i.e. a permanent lease and notably some devices only support these permanent leases. Note that whether permanent or not, this is only a request and the gateway may still decide at any point to remove the mapping (which usually happens on a reboot of the gateway, when its external IP address changes, or on some models when it detects a port mapping has become inactive, i.e. had no traffic for multiple minutes). If not `0` (permanent), the allowed range according to spec is between `120` (2 minutes) and `86400` seconds (24 hours).

See [UPNPResult<enum_UPNP_UPNPResult>] for possible return values.


----



|void| **clear_devices**\ (\ ) [🔗<class_UPNP_method_clear_devices>]

Clears the list of discovered devices.


----



[int<class_int>] **delete_port_mapping**\ (\ port\: [int<class_int>], proto\: [String<class_String>] = "UDP"\ ) |const| [🔗<class_UPNP_method_delete_port_mapping>]

Deletes the port mapping for the given port and protocol combination on the default gateway (see [get_gateway()<class_UPNP_method_get_gateway>]) if one exists. `port` must be a valid port between 1 and 65535, `proto` can be either `"TCP"` or `"UDP"`. May be refused for mappings pointing to addresses other than this one, for well-known ports (below 1024), or for mappings not added via UPnP. See [UPNPResult<enum_UPNP_UPNPResult>] for possible return values.


----



[int<class_int>] **discover**\ (\ timeout\: [int<class_int>] = 2000, ttl\: [int<class_int>] = 2, device_filter\: [String<class_String>] = "InternetGatewayDevice"\ ) [🔗<class_UPNP_method_discover>]

Discovers local [UPNPDevice<class_UPNPDevice>]\ s. Clears the list of previously discovered devices.

Filters for IGD (InternetGatewayDevice) type devices by default, as those manage port forwarding. `timeout` is the time to wait for responses in milliseconds. `ttl` is the time-to-live; only touch this if you know what you're doing.

See [UPNPResult<enum_UPNP_UPNPResult>] for possible return values.


----



[UPNPDevice<class_UPNPDevice>] **get_device**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_UPNP_method_get_device>]

Returns the [UPNPDevice<class_UPNPDevice>] at the given `index`.


----



[int<class_int>] **get_device_count**\ (\ ) |const| [🔗<class_UPNP_method_get_device_count>]

Returns the number of discovered [UPNPDevice<class_UPNPDevice>]\ s.


----



[UPNPDevice<class_UPNPDevice>] **get_gateway**\ (\ ) |const| [🔗<class_UPNP_method_get_gateway>]

Returns the default gateway. That is the first discovered [UPNPDevice<class_UPNPDevice>] that is also a valid IGD (InternetGatewayDevice).


----



[String<class_String>] **query_external_address**\ (\ ) |const| [🔗<class_UPNP_method_query_external_address>]

Returns the external [IP<class_IP>] address of the default gateway (see [get_gateway()<class_UPNP_method_get_gateway>]) as string. Returns an empty string on error.


----



|void| **remove_device**\ (\ index\: [int<class_int>]\ ) [🔗<class_UPNP_method_remove_device>]

Removes the device at `index` from the list of discovered devices.


----



|void| **set_device**\ (\ index\: [int<class_int>], device\: [UPNPDevice<class_UPNPDevice>]\ ) [🔗<class_UPNP_method_set_device>]

Sets the device at `index` from the list of discovered devices to `device`.

