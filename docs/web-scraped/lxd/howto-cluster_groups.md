# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/cluster_groups/

[]

# How to set up cluster groups[¶](#how-to-set-up-cluster-groups "Link to this heading")

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=t_3YJo_xItM)

Cluster members can be assigned to [[Cluster groups]](../../explanation/clusters/#cluster-groups). By default, all cluster members belong to the [`default`] group.

To create a cluster group, use the [[[`lxc`]` `[`cluster`]` `[`group`]` `[`create`]]](../../reference/manpages/lxc/cluster/group/create/#lxc-cluster-group-create-md) command. For example:

    lxc cluster group create gpu

To assign a cluster member to one or more groups, use the [[[`lxc`]` `[`cluster`]` `[`group`]` `[`assign`]]](../../reference/manpages/lxc/cluster/group/assign/#lxc-cluster-group-assign-md) command. This command removes the specified cluster member from all the cluster groups it currently is a member of and then adds it to the specified group or groups.

For example, to assign [`server1`] to only the [`gpu`] group, use the following command:

    lxc cluster group assign server1 gpu

To assign [`server1`] to the [`gpu`] group and also keep it in the [`default`] group, use the following command:

    lxc cluster group assign server1 default,gpu

To add a cluster member to a specific group without removing it from other groups, use the [[[`lxc`]` `[`cluster`]` `[`group`]` `[`add`]]](../../reference/manpages/lxc/cluster/group/add/#lxc-cluster-group-add-md) command.

For example, to add [`server1`] to the [`gpu`] group and also keep it in the [`default`] group, use the following command:

    lxc cluster group add server1 gpu

## Launch an instance on a cluster group member[¶](#launch-an-instance-on-a-cluster-group-member "Link to this heading")

With cluster groups, you can target an instance to run on one of the members of the cluster group, instead of targeting it to run on a specific member.

Note

[[`scheduler.instance`]](../../reference/cluster_member_config/#cluster-cluster:scheduler.instance) must be set to either [`all`] (the default) or [`group`] to allow instances to be targeted to a cluster group.

See [[Automatic placement of instances]](../../explanation/clusters/#clustering-instance-placement) for more information.

To launch an instance on a member of a cluster group, follow the instructions in [[Launch an instance on a specific cluster member]](../cluster_manage_instance/#cluster-target-instance), but use the group name prefixed with [`@`] for the [`--target`] flag. For example:

    lxc launch ubuntu:24.04 c1 --target=@gpu