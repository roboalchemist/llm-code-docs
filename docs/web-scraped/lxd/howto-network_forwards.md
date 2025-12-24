# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/network_forwards/

[]

# How to configure network forwards[¶](#how-to-configure-network-forwards "Link to this heading")

Note

Network forwards are available for the [[OVN network]](../../reference/network_ovn/#network-ovn) and the [[Bridge network]](../../reference/network_bridge/#network-bridge).

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=B-Uzo9WldMs)

Network forwards allow an external IP address (or specific ports on it) to be forwarded to an internal IP address (or specific ports on it) in the network that the forward belongs to.

This feature can be useful if you have limited external IP addresses and want to share a single external address between multiple instances. In this case, you have two options:

-   Forward all traffic from the external address to the internal address of one instance. This method makes it easy to move the traffic destined for the external address to another instance by simply reconfiguring the network forward.

-   Forward traffic from different port numbers of the external address to different instances (and optionally different ports on those instances). This method allows to "share" your external IP address and expose more than one instance at a time.

For [[OVN networks]](../../reference/network_ovn/#network-ovn), network forwards also allow an internal IP address (or specific ports on it) to be forwarded to another internal IP address (or specific ports).

Tip

Network forwards are very similar to using a [[proxy device]](../../reference/devices_proxy/#devices-proxy) in NAT mode.

The difference is that network forwards are applied on a network level, while a proxy device is added for an instance. In addition, proxy devices can be used to proxy traffic between different connection types (for example, TCP and Unix sockets).

## List network forwards[¶](#list-network-forwards "Link to this heading")

View a list of all forwards configured on a network:

CLI

API

UI

    lxc network forward list <network_name>

Example:

    lxc network forward list lxdbr0

Note

This list displays the listen address of the network forward and its default target address, if set. To view the target addresses for a network forward's ports [[set in its port specifications]](#network-forwards-port-specifications), you can [[show details about the network forward]](#network-forward-show) or [[edit the network forward]](#network-forward-edit).

Query the [`/1.0/networks/`] endpoint to list all forwards for a network.

    lxc query --request GET /1.0/networks//forwards

Example:

    lxc query --request GET /1.0/networks/lxdbr0/forwards

See [the API reference](/lxd/latest/api/#/network-forwards/network_forwards_get) for more information.

You can also use [[recursion]](../../rest-api/#rest-api-recursion) to list the forwards with a higher level of detail:

    lxc query --request GET /1.0/networks//forwards?recursion=1

In [[the web UI]](../access_ui/#access-ui), select [Networks] in the left sidebar, then select the desired network. On the resulting screen, view the [Forwards] tab:

<figure class="align-default">
<a href="../../_images/forwards_view.png" class="reference internal image-reference"><img src="../../_images/forwards_view.png" style="width: 95%;" alt="View a list of forwards on a network" /></a>
</figure>

[]

## Show a network forward[¶](#show-a-network-forward "Link to this heading")

Show details about a specific network forward:

CLI

API

UI

    lxc network forward show <network_name> <listen_address>

Example:

    lxc network forward show lxdbr0 192.0.2.1

Query the following endpoint for details about a specific forward:

    lxc query --request GET /1.0/networks//forwards/

See [the API reference](/lxd/latest/api/#/network-forwards/network_forward_get) for more information.

Example:

    lxc query --request GET /1.0/networks/ovn1/forwards/10.152.119.200

In [[the web UI]](../access_ui/#access-ui), select [Networks] in the left sidebar, then select the desired network. On the resulting screen, view the [Forwards] tab. This tab shows you information about all forwards on the network. You can click the [Edit] icon to view details for a specific forward:

<figure class="align-default">
<a href="../../_images/forward_edit_ex1.png" class="reference internal image-reference"><img src="../../_images/forward_edit_ex1.png" style="width: 95%;" alt="View details about a specific forward on a network through its edit screen" /></a>
</figure>

[]

## Create a network forward[¶](#create-a-network-forward "Link to this heading")

[]

### Requirements for listen addresses[¶](#requirements-for-listen-addresses "Link to this heading")

Before you can create a network forward, you must understand the requirements for listen addresses.

For both OVN and bridge networks, the listen addresses must not overlap with any subnet in use by other networks on the host. Otherwise, the listen address requirements differ by network type.

OVN network

Bridge network

For an OVN network, the allowed listen addresses that are external IPs must be defined in at least one of the following configuration options, using [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing):

-   [[`ipv4.routes`]](../../reference/network_bridge/#network-bridge-network-conf:ipv4.routes) or [[`ipv6.routes`]](../../reference/network_bridge/#network-bridge-network-conf:ipv6.routes) in the OVN network's uplink network configuration

-   [[`restricted.networks.subnets`]](../../reference/projects/#project-restricted:restricted.networks.subnets) in the OVN network's project configuration

The allowed internal IPs do not need to be defined. Use any non-conflicting internal IP address available on the OVN network.

A bridge network does not require you to define allowed listen addresses. Use any non-conflicting IP address available on the host.

### Create a forward in an OVN network[¶](#create-a-forward-in-an-ovn-network "Link to this heading")

Note

You must configure the [[allowed listen addresses]](#network-forwards-listen-addresses) before you can create a forward in an OVN network.

The IP addresses and ports shown in the examples below are only examples. It is up to you to choose the allowed and available addresses and ports for your setup.

CLI

API

UI

Use the following command to create a forward in an OVN network:

    lxc network forward create <ovn_network_name> <listen_address>|--allocate=ipv [target_address=<target_address>] [user.<key>=<value>]

-   For [`<ovn_network_name>`], specify the name of the OVN network on which to create the forward.

-   Immediately following the network name, provide only one of the following for the listen address:

    -   A listen IP address allowed by the [[Requirements for listen addresses]](#network-forwards-listen-addresses) (no port number)

    -   The [`--allocate=`] flag with a value of either [`ipv4`] or [`ipv6`] for automatic allocation of an allowed external IP address

-   Optionally provide a default [`target_address`] (no port number). Any traffic that does not match a port specification is forwarded to this address. This must be an IP address within the OVN network's subnet; typically, the static IP address of an instance is used.

-   Optionally provide custom user.\* keys to be stored in the network forward's configuration.

Examples

This example shows how to create a network forward on a network named [`ovn1`] with an allocated listen address and no default target address:

    lxc network forward create ovn1 --allocate=ipv4

This example shows how to create a network forward on a network named [`ovn1`] with a specific listen address and a default target address:

    lxc network forward create ovn1 192.0.2.1 target_address=10.41.211.2

To create a network forward in an OVN network, send a POST request to the [`/1.0/networks//forwards`] endpoint:

    lxc query --request POST /1.0/networks//forwards --data ',
      "ports": [                                        # optional
        
      ]
    }'

-   For [``], specify the name of the OVN network on which to create the forward.

-   For [`<listen_address>`], provide only one of the following:

    -   A listen IP address allowed by the [[Requirements for listen addresses]](#network-forwards-listen-addresses) (no port number)

    -   For automatic allocation of an allowed IP address, use [`"0.0.0.0"`] for IPv4 and [`"::"`] for IPv6.

-   Optionally provide a description of the forward.

-   Optionally provide a default [`target_address`] as part of the [`config`] object (no port number). Any traffic that does not match a port specification is forwarded to this address. This must be an IP address within the OVN network's subnet; typically, the static IP address of an instance is used.

-   Optionally provide custom [`user.*`] keys, also as part of the [`config`] object.

-   Optionally set up port specifications during forward creation. These specifications allow forwarding traffic from specific ports on the listen address to ports on a target address. For details on how to configure ports, see: [[Configure ports]](#network-forwards-port-specifications).

See [the API reference](/lxd/latest/api/#/network-forwards/network_forward_post) for more information.

Examples

This example shows how to create a network forward on a network named [`ovn1`] with an allocated listen address and no default target address:

    lxc query --request POST /1.0/networks/ovn1/forwards --data ''

This example shows how to create a network forward on a network named [`ovn1`] with a specific listen address and a default target address:

    lxc query --request POST /1.0/networks/ovn1/forwards --data '
    }'

In [[the web UI]](../access_ui/#access-ui), select [Networks] in the left sidebar, then select the desired OVN network. On the resulting screen, view the [Forwards] tab. Click the [Create forward] button.

In the [Create a new forward] panel, only the [Listen address] field is required.

<figure class="align-default">
<a href="../../_images/forward_create_ovn.png" class="reference internal image-reference"><img src="../../_images/forward_create_ovn.png" style="width: 95%;" alt="Create an OVN network forward" /></a>
</figure>

-   For the [Listen address], provide an IP address allowed by the [[Requirements for listen addresses]](#network-forwards-listen-addresses) (no port number).

-   Optionally provide a [Default target address] (no port number). Any traffic that does not match a port specification is forwarded to this address. This must be an IP address within the OVN network's subnet; typically, the static IP address of an instance is used.

You can optionally set up port specifications for the network forward by clicking the [Add port] button. These specifications allow forwarding traffic from specific ports on the listen address to ports on a target address. For details on how to configure this section, see: [[Configure ports]](#network-forwards-port-specifications).

Once you have finished setting up the network forward, click the [Create] button.

### Create a forward in a bridge network[¶](#create-a-forward-in-a-bridge-network "Link to this heading")

Note

The IP addresses and ports shown in the examples below are only examples. It is up to you to choose the allowed and available addresses and ports for your setup.

CLI

API

UI

Use the following command to create a forward in a bridge network:

    lxc network forward create <bridge_network_name> <listen_address> [target_address=<target_address>] [user.<key>=<value>]

-   For [`<bridge_network_name>`], specify the name of the bridge network on which to create the forward.

-   Immediately following the network name, provide an IP address allowed by the [[Requirements for listen addresses]](#network-forwards-listen-addresses) (no port number).

-   Optionally provide a default [`target_address`] (no port number). Any traffic that does not match a port specification is forwarded to this address. This must be an IP address within the bridge network's subnet; typically, the static IP address of an instance is used.

-   Optionally provide custom user.\* keys to be stored in the network forward's configuration.

-   You cannot use the [`--allocate`] flag with bridge networks.

Example

This example shows how to create a forward on a network named [`bridge1`]. The listen address is required, and the default target address is optional:

    lxc network forward create bridge1 192.0.2.1 target_address=10.41.211.2

To create a network forward in a bridge network, send a POST request to the [`/1.0/networks//forwards`] endpoint:

    lxc query --request POST /1.0/networks//forwards --data ',
      "ports": [                                        # optional
        
      ]
    }'

-   For [``], specify the name of the bridge network on which to create the forward.

-   For [`<listen_address>`], provide an IP address allowed by the [[Requirements for listen addresses]](#network-forwards-listen-addresses) (no port number).

    -   With bridge networks, you cannot dynamically allocate the listen address. You must input a specific address.

-   Optionally provide a description of the forward.

-   Optionally provide a default [`target_address`] as part of the [`config`] object (no port number). Any traffic that does not match a port specification is forwarded to this address. This must be an IP address within the OVN network's subnet; typically, the static IP address of an instance is used.

-   Optionally provide custom [`user.*`] keys, also as part of the [`config`] object.

-   Optionally set up port specifications during forward creation. These specifications allow forwarding traffic from specific ports on the listen address to ports on a target address. For details on how to configure ports, see: [[Configure ports]](#network-forwards-port-specifications).

See [the API reference](/lxd/latest/api/#/network-forwards/network_forward_post) for more information.

Example

This example shows how to create a forward on a network named [`bridge1`]. The listen address is required, and the default target address is optional:

    lxc query --request POST /1.0/networks/bridge1/forwards --data '
    }'

In [[the web UI]](../access_ui/#access-ui), select [Networks] in the left sidebar, then select the desired bridge network. On the resulting screen, view the [Forwards] tab. Click the [Create forward] button.

In the [Create a new forward] panel, only the [Listen address] field is required.

<figure class="align-default">
<a href="../../_images/forward_create_bridge.png" class="reference internal image-reference"><img src="../../_images/forward_create_bridge.png" style="width: 95%;" alt="Create a bridge network forward" /></a>
</figure>

-   For the [Listen address], provide a listen IP address allowed by the [[Requirements for listen addresses]](#network-forwards-listen-addresses) (no port number).

-   Optionally provide a [Default target address] (no port number). Any traffic that does not match a port specification is forwarded to this address. This must be an IP address within the bridge network's subnet; typically, the static IP address of an instance is used.

You can optionally set up port specifications for the network forward by clicking the [Add port] button. These specifications allow forwarding traffic from specific ports on the listen address to ports on a target address. For details on how to configure this section, see: [[Configure ports]](#network-forwards-port-specifications).

Once you have finished setting up the network forward, click the [Create] button.

### Forward properties[¶](#forward-properties "Link to this heading")

Network forwards have the following properties:

[[`config`]][]

User-provided free-form key/value pairs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-forward-properties:config)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`config`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | string set                                        |
+-----------------------------------+---------------------------------------------------+
| **Required:**                     | []                                      |
|                                   |                                                   |
|                                   | no                                                |
+-----------------------------------+---------------------------------------------------+

The only supported keys are [`target_address`] and [`user.*`] custom keys.

The [`target_address`] key is for the default target address of the network forward. It must be an IP address within the subnet of the network the forward belongs to.

[[`description`]][]

Description of the network forward

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-forward-properties:description)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`description`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | yes                                                    |
+-----------------------------------+--------------------------------------------------------+

[[`listen_address`]][]

IP address to listen on

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-forward-properties:listen_address)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`listen_address`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | string                                                    |
+-----------------------------------+-----------------------------------------------------------+
| **Required:**                     | []                                              |
|                                   |                                                           |
|                                   | no                                                        |
+-----------------------------------+-----------------------------------------------------------+

See [[Requirements for listen addresses]](#network-forwards-listen-addresses).

[[`ports`]][]

List of port specifications

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-forward-properties:ports)]

+-----------------------------------+--------------------------------------------------+
| **Key:**                          | [`ports`] |
+-----------------------------------+--------------------------------------------------+
| **Type:**                         | []                                     |
|                                   |                                                  |
|                                   | port list                                        |
+-----------------------------------+--------------------------------------------------+
| **Required:**                     | []                                     |
|                                   |                                                  |
|                                   | no                                               |
+-----------------------------------+--------------------------------------------------+

See [[Configure ports]](#network-forwards-port-specifications).

[]

## Configure ports[¶](#configure-ports "Link to this heading")

Once a forward is created on a network (whether bridge or OVN), it can be configured with port specifications. These specifications allow forwarding traffic from ports on the listen address to ports on a target address.

CLI

API

UI

When using the CLI, you must first [[create a network forward]](#network-forward-create) before you can add port specifications to it.

Use the following command to add port specifications on a forward:

    lxc network forward port add <network_name> <listen_address> <protocol> <listen_ports> <target_address> [<target_ports>]

-   Use the network name and listen address of the forward for which you want to add port specifications.

-   Use either [`tcp`] or [`udp`] as the protocol.

-   For the listen ports, you can specify a single listen port, a port range, or a comma-separated set of ports/port ranges.

-   Specify a target address. This address must be within the network's subnet, and it must be different from the forward's default target address. Typically, the static IP address of an instance is used.

-   Optionally specify a target port or ports. You can:

    -   Specify a single target port to forward traffic from all listen ports to this target port.

    -   Specify a set of target ports with the same number of set items as the listen ports. This forwards traffic from the first listen port to the first target port, the second listen port to the second target port, and so on.

-   If no target port is specified, the listen port value is used for the target port.

-   You can add multiple port configurations to the same network forward.

Examples

The example below shows how to configure a forward with a single listen port. Since no target port is specified, the target port defaults to the value of the listen port:

    lxc network forward port add network1 192.0.2.1 tcp 22 10.41.211.2

The example below shows how to configure a forward with a set of listen ports mapped to a single target port. Traffic to the listen address at ports 80 and 90 through 100 is forwarded to port 443 of the target address:

    lxc network forward port add network1 192.0.2.1 tcp 80,90-100 10.41.211.2 443

The example below shows how to configure a forward with a set of listen ports mapped to a set of target ports. Traffic to the listen address at port 22 is forwarded to port 22 of the target address, whereas traffic to port 80 is forwarded to port 443:

    lxc network forward port add network1 192.0.2.1 tcp 22,80 10.41.211.2 22,443

Using the API, you can configure port specifications on a network forward at the time you [[create the forward]](#network-forward-create), or by [[editing the forward]](#network-forward-edit) after creation.

In either case, you must configure the [`ports`] object shown below:

     1,
     8  "ports": [
     9    
    16  ]
    17}

-   For [`"listen_port"`], you can specify a single listen port, a port range, or a comma-separated set of ports/port ranges.

-   Use either [`"tcp"`] or [`"udp"`] as the [`"protocol"`].

-   Specify a [`"target_address"`]. This address must be within the network's subnet, and it must be different from the forward's default target address that is configured in the [`config`] object. Typically, the static IP address of an instance is used.

-   Optionally specify a target port or ports. You can:

    -   Specify a single target port to forward traffic from all listen ports to this target port.

    -   Specify a set of target ports with the same number of set items as the listen ports. This forwards traffic from the first listen port to the first target port, the second listen port to the second target port, and so on.

-   If no target port is specified, the listen port value is used for the target port.

-   The [`"ports"`] JSON property is configured as an array (list) of objects. You can set multiple port configurations on the same network forward, each as a separate JSON object in the array.

Examples

    "ports": [
       ,
       
    ]

In the example above, traffic to the network forward's listen ports of 80, 81, or 8080-8090 is explicitly forwarded to the same ports on the target address. Traffic to the forward's listen port of 3000 is explicitly forwarded to port 8080 on the target address.

More examples;

-   If the [`"listen_port"`] is set to [`"22"`] and no [`"target_port`]" is specified, the target port value defaults to [`"22"`].

-   If the [`"listen_port"`] is set to [`"80,90-100"`] and the [`"target_port`]" is set to [`"442"`], all traffic to the listen address at ports 80 and 90 through 100 is forwarded to port 443 of the target address.

-   If the [`"listen_port"`] is set to [`"22,80"`] and the [`"target_port`]" is set to [`"22,443"`], all traffic to the listen address at port 22 is forwarded to port 22 of the target address, whereas traffic to port 80 is forwarded to port 443.

In the web UI, you can configure port specifications on a network forward at the time you [[create the forward]](#network-forward-create), or by [[editing the forward]](#network-forward-edit) after creation.

<figure class="align-default">
<a href="../../_images/forward_create_port.png" class="reference internal image-reference"><img src="../../_images/forward_create_port.png" style="width: 95%;" alt="Configure a network forward&#39;s port specifications" /></a>
</figure>

-   For the [Listen port], you can specify a single port, a port range, or a comma-separated set of ports/port ranges.

-   Select either [TCP] or [UDP] as the protocol.

-   Specify a [Target address]. This address must be within the network's subnet, and it must be different from the forward's [Default target address]. Typically, the static IP address of an instance is used.

-   Optionally specify a target port or ports. You can:

    -   Specify a single target port to forward traffic from all listen ports to this target port.

    -   Specify a set of target ports with the same number of set items as the listen ports. This forwards traffic from the first listen port to the first target port, the second listen port to the second target port, and so on.

-   If no target port is specified, the listen port value is used for the target port.

Examples

-   If the [Listen port] is set to [`22`] and no [Target port] is specified, the target port value defaults to 22.

-   If the [Listen port] is set to [`80,90-100`] and the [Target port] is set to [442], all traffic to the listen address at ports 80 and 90 through 100 is forwarded to port 443 of the target address.

-   If the [Listen port] is set to [`22,80`] and the [Target port] is set to [`22,443`], all traffic to the listen address at port 22 is forwarded to port 22 of the target address, whereas traffic to port 80 is forwarded to port 443.

### Port properties[¶](#port-properties "Link to this heading")

Network forward ports have the following properties:

[[`description`]][]

Description of the port or ports

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-port-properties:description)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`description`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | no                                                     |
+-----------------------------------+--------------------------------------------------------+

[[`listen_port`]][]

Listen port or ports

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-port-properties:listen_port)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`listen_port`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+
| **Required:**                     | []                                           |
|                                   |                                                        |
|                                   | yes                                                    |
+-----------------------------------+--------------------------------------------------------+

For example: [`80,90-100`]

[[`protocol`]][]

Protocol for the port or ports

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-port-properties:protocol)]

+-----------------------------------+-----------------------------------------------------+
| **Key:**                          | [`protocol`] |
+-----------------------------------+-----------------------------------------------------+
| **Type:**                         | []                                        |
|                                   |                                                     |
|                                   | string                                              |
+-----------------------------------+-----------------------------------------------------+
| **Required:**                     | []                                        |
|                                   |                                                     |
|                                   | yes                                                 |
+-----------------------------------+-----------------------------------------------------+

Possible values are [`tcp`] and [`udp`].

[[`target_address`]][]

IP address to forward to

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-port-properties:target_address)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`target_address`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | string                                                    |
+-----------------------------------+-----------------------------------------------------------+
| **Required:**                     | []                                              |
|                                   |                                                           |
|                                   | yes                                                       |
+-----------------------------------+-----------------------------------------------------------+

This [`target_address`] must be within the subnet of the network the forward belongs to. Also, it must be different from the forward's default target address.

[[`target_port`]][]

Target port or ports

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-forward-port-properties:target_port)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`target_port`]         |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | string                                                         |
+-----------------------------------+----------------------------------------------------------------+
| **Default:**                      | []                                                   |
|                                   |                                                                |
|                                   | same as [`listen_port`] |
+-----------------------------------+----------------------------------------------------------------+
| **Required:**                     | []                                                   |
|                                   |                                                                |
|                                   | no                                                             |
+-----------------------------------+----------------------------------------------------------------+

For example: [`70,80-90`] or [`90`]

[]

## Edit a network forward[¶](#edit-a-network-forward "Link to this heading")

CLI

API

UI

Use the following command to edit a network forward:

    lxc network forward edit <network_name> <listen_address>

This command opens the network forward in YAML format for editing. You can edit both the general configuration and the port specifications.

Partial update

To update a subset of the network forward configuration, send a PATCH request to the [`/1.0/networks//forwards/`] endpoint:

    lxc query --request PATCH /1.0/networks//forwards/ --data ',
      "description": "<description of the forward>",
      "ports": [
        
      ]
    }'

See [the API reference](/lxd/latest/api/#/network-forwards/network_forward_patch) for more information.

Example

Update only the default target address of a forward:

    lxc query --request PATCH /1.0/networks/ovn1/forwards/10.152.119.200 --data '
    }'

Full update

To replace the entire configuration of an existing network forward, send a PUT request to the [`/1.0/networks//forwards/`] endpoint:

    lxc query --request PUT /1.0/networks//forwards/ --data ',
      "description": "<description of the forward>",
      "ports": [
        
      ]
    }'

Unlike a [`PATCH`] request, the [`PUT`] request replaces the entire configuration.

See [the API reference](/lxd/latest/api/#/network-forwards/network_forward_put) for more information.

Example

When using PUT, take care to send any data should be kept in the configuration. Consider the following configuration for a network forward:

    ,
      "ports": [
        
      ]
    }'

The following PUT request updates the entire configuration:

    lxc query --request PUT /1.0/networks/ovntest/forwards/10.152.119.200 --data '
      ]
    }'

The forward's configuration after the PUT update:

    ,
      "ports": [
        
      ]
    }

Notice that the [`config`] object no longer contains any values. This is because none were sent as part of the PUT update.

In [[the web UI]](../access_ui/#access-ui), select [Networks] in the left sidebar, then select the desired network. On the resulting screen, view the [Forwards] tab. This tab shows you information about all forwards on the network. Click the [Edit] icon next to a forward to edit it:

<figure class="align-default">
<a href="../../_images/forward_edit_ex1.png" class="reference internal image-reference"><img src="../../_images/forward_edit_ex1.png" style="width: 95%;" alt="Choose to edit a forward on a network" /></a>
</figure>

In the resulting screen, you can edit the forward's general configuration as well as its port specifications:

<figure class="align-default">
<a href="../../_images/forward_edit_ex2.png" class="reference internal image-reference"><img src="../../_images/forward_edit_ex2.png" style="width: 95%;" alt="Edit a forward on a network" /></a>
</figure>

## Delete a network forward[¶](#delete-a-network-forward "Link to this heading")

CLI

API

UI

Use the following command to delete a network forward:

    lxc network forward delete <network_name> <listen_address>

To delete a network forward, send a DELETE request to the [`/1.0/networks//forwards/`] endpoint:

    lxc query --request DELETE /1.0/networks//forwards/

Example:

    lxc query --request DELETE /1.0/networks/ovn1/forwards/192.0.2.21

See [the API reference](/lxd/latest/api/#/network-forwards/network_forward_delete) for more information.

In [[the web UI]](../access_ui/#access-ui), select [Networks] in the left sidebar, then select the desired network. On the resulting screen, view the [Forwards] tab. This tab shows you information about all forwards on the network. Click the [Delete] icon next to a forward to delete it:

<figure class="align-default">
<a href="../../_images/forward_delete.png" class="reference internal image-reference"><img src="../../_images/forward_delete.png" style="width: 95%;" alt="Delete a forward on a network" /></a>
</figure>