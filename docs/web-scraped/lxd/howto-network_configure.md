# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/network_configure/

[]

# How to configure a network[¶](#how-to-configure-a-network "Link to this heading")

CLI

UI

To configure an existing network, use either the [[[`lxc`]` `[`network`]` `[`set`]]](../../reference/manpages/lxc/network/set/#lxc-network-set-md) and [[[`lxc`]` `[`network`]` `[`unset`]]](../../reference/manpages/lxc/network/unset/#lxc-network-unset-md) commands (to configure single settings) or the [`lxc`]` `[`network`]` `[`edit`] command (to edit the full configuration). To configure settings for specific cluster members, add the [`--target`] flag.

For example, the following command configures a DNS server for a physical network:

    lxc network set UPLINK dns.nameservers=8.8.8.8

The available configuration options differ depending on the network type. See [[Network types]](../network_create/#network-types) for links to the configuration options for each network type.

To edit the configuration of a network, navigate to the overview page for the network, and observe its attributes and settings.

Within the Configuration tab, you can edit key settings of the network by clicking on the [Edit] pencil icon inline with the desired configuration setting.

<figure class="align-default">
<a href="../../_images/network_configuration.png" class="reference internal image-reference"><img src="../../_images/network_configuration.png" style="width: 80%;" alt="LXD Network overview page" /></a>
</figure>

There are separate commands to configure advanced networking features. See the following documentation:

-   [[How to configure network ACLs]](../network_acls/)

-   [[How to configure network forwards]](../network_forwards/)

-   [[How to configure network load balancers]](../network_load_balancers/)

-   [[How to configure network zones]](../network_zones/)

-   [[How to create OVN peer routing relationships]](../network_ovn_peers/) (OVN only)