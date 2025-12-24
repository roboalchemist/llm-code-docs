# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/network_create/

[]

# How to create a network[¶](#how-to-create-a-network "Link to this heading")

To create a managed network, use the [[[`lxc`]` `[`network`]]](../../reference/manpages/lxc/network/#lxc-network-md) command and its subcommands. Append [`--help`] to any command to see more information about its usage and available flags.

[]

## Network types[¶](#network-types "Link to this heading")

The following network types are available:

  Network type                                          Documentation                                                                                                   Configuration options
  ----------------------------------------------------- --------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  [`bridge`]     [[Bridge network]](../../reference/network_bridge/#network-bridge)         [[Configuration options]](../../reference/network_bridge/#network-bridge-options)
  [`ovn`]        [[OVN network]](../../reference/network_ovn/#network-ovn)                  [[Configuration options]](../../reference/network_ovn/#network-ovn-options)
  [`macvlan`]    [[Macvlan network]](../../reference/network_macvlan/#network-macvlan)      [[Configuration options]](../../reference/network_macvlan/#network-macvlan-options)
  [`sriov`]      [[SR-IOV network]](../../reference/network_sriov/#network-sriov)           [[Configuration options]](../../reference/network_sriov/#network-sriov-options)
  [`physical`]   [[Physical network]](../../reference/network_physical/#network-physical)   [[Configuration options]](../../reference/network_physical/#network-physical-options)

## Create a network[¶](#create-a-network "Link to this heading")

CLI

UI

Use the following command to create a network:

    lxc network create <name> --type=<network_type> [configuration_options...]

See [[Network types]](#network-types) for a list of available network types and links to their configuration options.

If you do not specify a [`--type`] argument, the default type of [`bridge`] is used.

[]Create a network in a cluster

If you are running a LXD cluster and want to create a network, you must create the network for each cluster member separately. The reason for this is that the network configuration, for example, the name of the parent network interface, might be different between cluster members.

Therefore, you must first create a pending network on each member with the [`--target=<cluster_member>`] flag and the appropriate configuration for the member. Make sure to use the same network name for all members. Then create the network without specifying the [`--target`] flag to actually set it up.

For example, the following series of commands sets up a physical network with the name [`UPLINK`] on three cluster members:

[`user@host:~$`]` `

[[`lxc`]` `[`network`]` `[`create`]` `[`UPLINK`]` `[`--type=physical`]` `[`parent=br0`]` `[`--target=vm01`]` `]

    Network UPLINK pending on member vm01

[`user@host:~$`]` `

[[`lxc`]` `[`network`]` `[`create`]` `[`UPLINK`]` `[`--type=physical`]` `[`parent=br0`]` `[`--target=vm02`]` `]

    Network UPLINK pending on member vm02

[`user@host:~$`]` `

[[`lxc`]` `[`network`]` `[`create`]` `[`UPLINK`]` `[`--type=physical`]` `[`parent=br0`]` `[`--target=vm03`]` `]

    Network UPLINK pending on member vm03

[`user@host:~$`]` `

[[`lxc`]` `[`network`]` `[`create`]` `[`UPLINK`]` `[`--type=physical`]` `]

    Network UPLINK created

Also see [[How to configure networks for a cluster]](../cluster_config_networks/#cluster-config-networks).

From the main navigation, select [Networks].

On the resulting page, click [Create network] in the upper-right corner.

You can then configure the network name and type, as well as other attributes. Optional additional attributes are split into the categories [Bridge], [IPv4], [IPv6] and [DNS], which can be seen in the submenu on the right.

Click [Create] to create the network.

<figure class="align-default">
<a href="../../_images/network_create.png" class="reference internal image-reference"><img src="../../_images/network_create.png" style="width: 80%;" alt="Create a network in LXD" /></a>
</figure>

[]

## Attach a network to an instance[¶](#attach-a-network-to-an-instance "Link to this heading")

CLI

UI

After creating a managed network, you can attach it to an instance as a [[NIC device]](../../reference/devices_nic/#devices-nic).

To do so, use the following command:

    lxc network attach <network_name> <instance_name> [<device_name>] [<interface_name>]

The device name and the interface name are optional, but we recommend specifying at least the device name. If not specified, LXD uses the network name as the device name, which might be confusing and cause problems. For example, LXD images perform IP auto-configuration on the [`eth0`] interface, which does not work if the interface is called differently.

For example, to attach the network [`my-network`] to the instance [`my-instance`] as [`eth0`] device, enter the following command:

    lxc network attach my-network my-instance eth0

When [[creating]](../instances_create/#instances-create) or [[configuring an instance]](../instances_configure/#instances-configure), go to the [Devices] section in the left-hand submenu, then select [Network] to view and edit the networks linked to the instance.

<figure class="align-default">
<a href="../../_images/network_add_to_instance.png" class="reference internal image-reference"><img src="../../_images/network_add_to_instance.png" style="width: 80%;" alt="Add a network to an instance in LXD" /></a>
</figure>

Click the [Attach network] button to add a new network. From here, you can select an existing network from the [Network] dropdown and assign it a device name.

<figure class="align-default">
<a href="../../_images/network_attach_instance.png" class="reference internal image-reference"><img src="../../_images/network_attach_instance.png" style="width: 80%;" alt="Attach a network to an instance in LXD" /></a>
</figure>

If configuring an instance, select [Save changes] to save your changes. If creating an instance, select [Create] to create your instance.

### Attach the network as a device[¶](#attach-the-network-as-a-device "Link to this heading")

The [[[`lxc`]` `[`network`]` `[`attach`]]](../../reference/manpages/lxc/network/attach/#lxc-network-attach-md) command is a shortcut for adding a NIC device to an instance. Alternatively, you can add a NIC device based on the network configuration in the usual way:

    lxc config device add <instance_name> <device_name> nic network=<network_name>

When using this way, you can add further configuration to the command to override the default settings for the network if needed. See [[NIC device]](../../reference/devices_nic/#devices-nic) for all available device options.