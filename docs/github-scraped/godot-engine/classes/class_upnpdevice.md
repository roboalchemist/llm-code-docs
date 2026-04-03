:github_url: hide



# UPNPDevice

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Universal Plug and Play (UPnP) device.


## Description

Universal Plug and Play (UPnP) device. See [UPNP<class_UPNP>] for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows to manage port mappings (port forwarding) and to query network information of the device (like local and external IP address and status). Note that methods on this class are synchronous and block the calling thread.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+---------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                 | :ref:`description_url<class_UPNPDevice_property_description_url>`   | ``""`` |
> +---------------------------------------------+---------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                 | :ref:`igd_control_url<class_UPNPDevice_property_igd_control_url>`   | ``""`` |
> +---------------------------------------------+---------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                 | :ref:`igd_our_addr<class_UPNPDevice_property_igd_our_addr>`         | ``""`` |
> +---------------------------------------------+---------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                 | :ref:`igd_service_type<class_UPNPDevice_property_igd_service_type>` | ``""`` |
> +---------------------------------------------+---------------------------------------------------------------------+--------+
> | :ref:`IGDStatus<enum_UPNPDevice_IGDStatus>` | :ref:`igd_status<class_UPNPDevice_property_igd_status>`             | ``9``  |
> +---------------------------------------------+---------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                 | :ref:`service_type<class_UPNPDevice_property_service_type>`         | ``""`` |
> +---------------------------------------------+---------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`add_port_mapping<class_UPNPDevice_method_add_port_mapping>`\ (\ port\: :ref:`int<class_int>`, port_internal\: :ref:`int<class_int>` = 0, desc\: :ref:`String<class_String>` = "", proto\: :ref:`String<class_String>` = "UDP", duration\: :ref:`int<class_int>` = 0\ ) |const| |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`delete_port_mapping<class_UPNPDevice_method_delete_port_mapping>`\ (\ port\: :ref:`int<class_int>`, proto\: :ref:`String<class_String>` = "UDP"\ ) |const|                                                                                                                     |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`is_valid_gateway<class_UPNPDevice_method_is_valid_gateway>`\ (\ ) |const|                                                                                                                                                                                                      |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`query_external_address<class_UPNPDevice_method_query_external_address>`\ (\ ) |const|                                                                                                                                                                                          |
> +-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **IGDStatus**: [🔗<enum_UPNPDevice_IGDStatus>]



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_OK** = `0`

OK.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_HTTP_ERROR** = `1`

HTTP error.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_HTTP_EMPTY** = `2`

Empty HTTP response.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_NO_URLS** = `3`

**Deprecated:** This value is no longer used.

Returned response contained no URLs.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_NO_IGD** = `4`

Not a valid IGD.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_DISCONNECTED** = `5`

Disconnected.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_UNKNOWN_DEVICE** = `6`

Unknown device.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_INVALID_CONTROL** = `7`

Invalid control.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_MALLOC_ERROR** = `8`

**Deprecated:** This value is no longer used.

Memory allocation error.



[IGDStatus<enum_UPNPDevice_IGDStatus>] **IGD_STATUS_UNKNOWN_ERROR** = `9`

Unknown error.


----


## Property Descriptions



[String<class_String>] **description_url** = `""` [🔗<class_UPNPDevice_property_description_url>]


- |void| **set_description_url**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_description_url**\ (\ )

URL to the device description.


----



[String<class_String>] **igd_control_url** = `""` [🔗<class_UPNPDevice_property_igd_control_url>]


- |void| **set_igd_control_url**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_igd_control_url**\ (\ )

IDG control URL.


----



[String<class_String>] **igd_our_addr** = `""` [🔗<class_UPNPDevice_property_igd_our_addr>]


- |void| **set_igd_our_addr**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_igd_our_addr**\ (\ )

Address of the local machine in the network connecting it to this **UPNPDevice**.


----



[String<class_String>] **igd_service_type** = `""` [🔗<class_UPNPDevice_property_igd_service_type>]


- |void| **set_igd_service_type**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_igd_service_type**\ (\ )

IGD service type.


----



[IGDStatus<enum_UPNPDevice_IGDStatus>] **igd_status** = `9` [🔗<class_UPNPDevice_property_igd_status>]


- |void| **set_igd_status**\ (\ value\: [IGDStatus<enum_UPNPDevice_IGDStatus>]\ )
- [IGDStatus<enum_UPNPDevice_IGDStatus>] **get_igd_status**\ (\ )

IGD status.


----



[String<class_String>] **service_type** = `""` [🔗<class_UPNPDevice_property_service_type>]


- |void| **set_service_type**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_service_type**\ (\ )

Service type.


----


## Method Descriptions



[int<class_int>] **add_port_mapping**\ (\ port\: [int<class_int>], port_internal\: [int<class_int>] = 0, desc\: [String<class_String>] = "", proto\: [String<class_String>] = "UDP", duration\: [int<class_int>] = 0\ ) |const| [🔗<class_UPNPDevice_method_add_port_mapping>]

Adds a port mapping to forward the given external port on this **UPNPDevice** for the given protocol to the local machine. See [UPNP.add_port_mapping()<class_UPNP_method_add_port_mapping>].


----



[int<class_int>] **delete_port_mapping**\ (\ port\: [int<class_int>], proto\: [String<class_String>] = "UDP"\ ) |const| [🔗<class_UPNPDevice_method_delete_port_mapping>]

Deletes the port mapping identified by the given port and protocol combination on this device. See [UPNP.delete_port_mapping()<class_UPNP_method_delete_port_mapping>].


----



[bool<class_bool>] **is_valid_gateway**\ (\ ) |const| [🔗<class_UPNPDevice_method_is_valid_gateway>]

Returns `true` if this is a valid IGD (InternetGatewayDevice) which potentially supports port forwarding.


----



[String<class_String>] **query_external_address**\ (\ ) |const| [🔗<class_UPNPDevice_method_query_external_address>]

Returns the external IP address of this **UPNPDevice** or an empty string.

