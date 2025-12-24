# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/cluster_config_networks/

[]

# How to configure networks for a cluster[¶](#how-to-configure-networks-for-a-cluster "Link to this heading")

All members of a cluster must have identical networks defined. The only configuration keys that may differ between networks on different members are [[`bridge.external_interfaces`]](../../reference/network_bridge/#network-bridge-network-conf:bridge.external_interfaces), [[`parent`]](../../reference/network_physical/#network-physical-network-conf:parent), [[`bgp.ipv4.nexthop`]](../../reference/network_bridge/#network-bridge-network-conf:bgp.ipv4.nexthop), and [[`bgp.ipv6.nexthop`]](../../reference/network_bridge/#network-bridge-network-conf:bgp.ipv6.nexthop). See [[Member configuration]](../../explanation/clusters/#clustering-member-config) for more information.

Creating additional networks is a two-step process:

1.  Define and configure the new network across all cluster members. For example, for a cluster that has three members:

    ::: 
    ::: highlight
        lxc network create --target server1 my-network
        lxc network create --target server2 my-network
        lxc network create --target server3 my-network
    :::
    :::

    ::: 
    Note

    You can pass only the member-specific configuration keys [`bridge.external_interfaces`], [`parent`], [`bgp.ipv4.nexthop`] and [`bgp.ipv6.nexthop`]. Passing other configuration keys results in an error.
    :::

    These commands define the network, but they don't create it. If you run [[[`lxc`]` `[`network`]` `[`list`]]](../../reference/manpages/lxc/network/list/#lxc-network-list-md), you can see that the network is marked as "pending".

2.  Run the following command to instantiate the network on all cluster members:

    ::: 
    ::: highlight
        lxc network create my-network
    :::
    :::

    ::: 
    Note

    You can add configuration keys that are not member-specific to this command.
    :::

    If you missed a cluster member when defining the network, or if a cluster member is down, you get an error.

Also see [[Create a network in a cluster]](../network_create/#network-create-cluster).

[]

## Separate REST API and clustering networks[¶](#separate-rest-api-and-clustering-networks "Link to this heading")

You can configure different networks for the REST API endpoint of your clients and for internal traffic between the members of your cluster. This separation can be useful, for example, to use a virtual address for your REST API, with DNS round robin.

To do so, you must specify different addresses for [[`cluster.https_address`]](../../server/#server-cluster:cluster.https_address) (the address for internal cluster traffic) and [[`core.https_address`]](../../server/#server-core:core.https_address) (the address for the REST API):

1.  Create your cluster as usual, and make sure to use the address that you want to use for internal cluster traffic as the cluster address. This address is set as the [`cluster.https_address`] configuration.

2.  After joining your members, set the [`core.https_address`] configuration to the address for the REST API. For example:

    ::: 
    ::: highlight
        lxc config set core.https_address 0.0.0.0:8443
    :::
    :::

    ::: 
    Note

    [`core.https_address`] is specific to the cluster member, so you can use different addresses on different members. You can also use a wildcard address to make the member listen on multiple interfaces.
    :::