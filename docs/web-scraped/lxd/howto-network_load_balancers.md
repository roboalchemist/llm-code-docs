# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/network_load_balancers/

[]

# How to configure network load balancers[¶](#how-to-configure-network-load-balancers "Link to this heading")

Note

Network load balancers are currently available for the [[OVN network]](../../reference/network_ovn/#network-ovn).

Network load balancers are similar to forwards in that they allow specific ports on an IP address (external or internal) to be forwarded to specific ports on internal IP addresses in the same network as the load balancer.

The difference between load balancers and forwards is that load balancers can be used to share ingress traffic between multiple internal backend addresses. This feature can be useful if you have limited external IP addresses or want to share a single external address and ports over multiple instances.

A load balancer is made up of:

-   A single listen IP address (external or internal).

-   One or more named backends consisting of an internal IP and optional port ranges.

-   One or more listen port ranges that are configured to forward to one or more named backends.

## Create a network load balancer[¶](#create-a-network-load-balancer "Link to this heading")

Use the following command to create a network load balancer:

    lxc network load-balancer create <network_name> [<listen_address>] [--allocate=ipv] [configuration_options...]

Example with a specified listen address:

    lxc network load-balancer create my-ovn-network 192.0.2.178

Example with an allocated listen address:

    lxc network load-balancer create my-ovn-network --allocate=ipv4

Each load balancer is assigned to a network.

Listen addresses are subject to restrictions. If a listen address is not specified, the [`--allocate`] flag must be provided. See [[Requirements for listen addresses]](#network-load-balancers-listen-addresses) for more information about which addresses can be load-balanced, as well as how to use the [`--allocate`] flag.

### Load balancer properties[¶](#load-balancer-properties "Link to this heading")

Network load balancers have the following properties:

[[`backends`]][]

List of backend specifications

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-properties:backends)]

+-----------------------------------+-----------------------------------------------------+
| **Key:**                          | [`backends`] |
+-----------------------------------+-----------------------------------------------------+
| **Type:**                         | []                                        |
|                                   |                                                     |
|                                   | backend list                                        |
+-----------------------------------+-----------------------------------------------------+
| **Required:**                     | []                                        |
|                                   |                                                     |
|                                   | no                                                  |
+-----------------------------------+-----------------------------------------------------+

See [[Configure backends]](#network-load-balancers-backend-specifications).

[[`config`]][]

User-provided free-form key/value pairs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-properties:config)]

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

The only supported keys are [`user.*`] custom keys.

[[`description`]][]

Description of the network load balancer

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-properties:description)]

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

[[`listen_address`]][]

IP address to listen on

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-properties:listen_address)]

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

[[`ports`]][]

List of port specifications

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-properties:ports)]

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

See [[Configure ports]](#network-load-balancers-port-specifications).

[]

### Requirements for listen addresses[¶](#requirements-for-listen-addresses "Link to this heading")

The following requirements must be met for valid listen addresses:

For external listen IP addresses:

-   Allowed listen addresses must be defined in the uplink network's [`ipv.routes`] settings or the project's [[`restricted.networks.subnets`]](../../reference/projects/#project-restricted:restricted.networks.subnets) setting.

    -   If you specify a listen address when creating a load balancer, it must be within the range of allowed addresses.

    -   If you do not specify a listen address, you must use either [`--allocate`]` `[`ipv4`] or [`--allocate`]` `[`ipv6`]. This will allocate a listen address from the range of allowed addresses.

-   The listen address must not overlap with a subnet that is in use with another network or entity in that network.

For internal listen IP addresses:

-   Allowed listen addresses must not be used by the associated network's gateway, other existing load balancers and network forwards, or instance NICs.

[]

## Configure backends[¶](#configure-backends "Link to this heading")

You can add backend specifications to the network load balancer to define target addresses (and optionally ports). The backend target address must be within the same subnet as the network associated with the load balancer.

Use the following command to add a backend specification:

    lxc network load-balancer backend add <network_name> <listen_address> <backend_name> <target_address> [<target_ports>]

Example:

    lxc network load-balancer backend add my-ovn-network 192.0.2.178 test-backend 10.41.211.5

If no target ports are specified when adding the backend:

-   The load balancer uses the listen ports defined in the [port specification](#port-properties) associated with that backend, if any.

-   If no such listen ports are defined, the backend has no target ports and is inactive. You must either [add a port specification](#port-properties) or [edit the load balancer configuration](#edit-a-network-load-balancer) to include a [`target_port`] value in the backend specification or a [`listen_port`] value in the ports specification.

If you want to forward the traffic to different ports, you have two options:

-   Specify a single target port to forward traffic from all listen ports to this target port.

-   Specify a set of target ports with the same number of ports as the listen ports to forward traffic from the first listen port to the first target port, the second listen port to the second target port, and so on.

### Backend properties[¶](#backend-properties "Link to this heading")

Network load balancer backends have the following properties:

[[`description`]][]

Description of the backend

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-backend-properties:description)]

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

[[`name`]][]

Name of the backend

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-backend-properties:name)]

+-----------------------------------+-------------------------------------------------+
| **Key:**                          | [`name`] |
+-----------------------------------+-------------------------------------------------+
| **Type:**                         | []                                    |
|                                   |                                                 |
|                                   | string                                          |
+-----------------------------------+-------------------------------------------------+
| **Required:**                     | []                                    |
|                                   |                                                 |
|                                   | yes                                             |
+-----------------------------------+-------------------------------------------------+

[[`target_address`]][]

IP address to forward to

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-backend-properties:target_address)]

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

[[`target_port`]][]

Target port or ports

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-backend-properties:target_port)]

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Key:**                          | [`target_port`]                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                                                                                                        |
|                                   |                                                                                                                                                                     |
|                                   | string                                                                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                                                                                                        |
|                                   |                                                                                                                                                                     |
|                                   | same as [[`listen_port`]](#network-load-balancer-load-balancer-port-properties:listen_port) |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Required:**                     | []                                                                                                                                                        |
|                                   |                                                                                                                                                                     |
|                                   | no                                                                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For example: [`70,80-90`] or [`90`]

[]

## Configure ports[¶](#configure-ports "Link to this heading")

You can add port specifications to the network load balancer to forward traffic from specific ports on the listen address to specific ports on one or more target backends.

Use the following command to add a port specification:

    lxc network load-balancer port add <network_name> <listen_address> <protocol> <listen_ports> <backend_name>[,<backend_name>...]

Example:

    lxc network load-balancer port add my-ovn-network 192.0.2.178 tcp 80 test-backend

You can specify a single listen port or a set of ports. The backend(s) specified must have target port(s) settings compatible with the port's listen port(s) setting.

### Port properties[¶](#port-properties "Link to this heading")

Network load balancer ports have the following properties:

[[`description`]][]

Description of the port or ports

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-port-properties:description)]

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

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-port-properties:listen_port)]

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

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-port-properties:protocol)]

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

[[`target_backend`]][]

Backend name or names to forward to

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#network-load-balancer-load-balancer-port-properties:target_backend)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`target_backend`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | backend list                                              |
+-----------------------------------+-----------------------------------------------------------+
| **Required:**                     | []                                              |
|                                   |                                                           |
|                                   | yes                                                       |
+-----------------------------------+-----------------------------------------------------------+

## Edit a network load balancer[¶](#edit-a-network-load-balancer "Link to this heading")

Use the following command to edit a network load balancer:

    lxc network load-balancer edit <network_name> <listen_address>

This command opens the network load balancer in YAML format for editing. You can edit the general configuration, as well as the backend and port specifications.

Example load balancer configuration YAML file:

    listen_address: 192.0.2.178
    location: ""
    description: ""
    config: 
    backends:
    - name: test-backend
      description: ""
      target_port: ""
      target_address: 10.41.211.5
    ports:
    - description: ""
      protocol: tcp
      listen_port: 70,80-90
      target_backend:
      - test-backend

## Delete a network load balancer[¶](#delete-a-network-load-balancer "Link to this heading")

Use the following command to delete a network load balancer:

    lxc network load-balancer delete <network_name> <listen_address>