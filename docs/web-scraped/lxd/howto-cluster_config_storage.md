# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/cluster_config_storage/

[]

# How to configure storage for a cluster[¶](#how-to-configure-storage-for-a-cluster "Link to this heading")

All members of a cluster must have identical storage pools. The only configuration keys that may differ between pools on different members are [[[`source`]]](../../reference/storage_drivers/#storage-drivers), [[[`size`]]](../../reference/storage_drivers/#storage-drivers), [[`zfs.pool_name`]](../../reference/storage_zfs/#storage-zfs-pool-conf:zfs.pool_name), [[`lvm.thinpool_name`]](../../reference/storage_lvm/#storage-lvm-pool-conf:lvm.thinpool_name) and [[`lvm.vg_name`]](../../reference/storage_lvm/#storage-lvm-pool-conf:lvm.vg_name). See [[Member configuration]](../../explanation/clusters/#clustering-member-config) for more information.

LXD creates a default [`local`] storage pool for each cluster member during initialization.

Creating additional storage pools is a two-step process:

1.  Define and configure the new storage pool across all cluster members. For example, for a cluster that has three members:

    ::: 
    ::: highlight
        lxc storage create --target server1 data zfs source=/dev/vdb1
        lxc storage create --target server2 data zfs source=/dev/vdc1
        lxc storage create --target server3 data zfs source=/dev/vdb1 size=10GiB
    :::
    :::

    ::: 
    Note

    You can pass only the member-specific configuration keys [`source`], [`size`], [`zfs.pool_name`], [`lvm.thinpool_name`] and [`lvm.vg_name`]. Passing other configuration keys results in an error.
    :::

    These commands define the storage pool, but they don't create it. If you run [[[`lxc`]` `[`storage`]` `[`list`]]](../../reference/manpages/lxc/storage/list/#lxc-storage-list-md), you can see that the pool is marked as "pending".

2.  Run the following command to instantiate the storage pool on all cluster members:

    ::: 
    ::: highlight
        lxc storage create data zfs
    :::
    :::

    ::: 
    Note

    You can add configuration keys that are not member-specific to this command.
    :::

    If you missed a cluster member when defining the storage pool, or if a cluster member is down, you get an error.

Also see [[Create a storage pool in a cluster]](../storage_pools/#storage-pools-cluster).

## View member-specific pool configuration[¶](#view-member-specific-pool-configuration "Link to this heading")

Running [[[`lxc`]` `[`storage`]` `[`show`]` `[`<pool_name>`]]](../../reference/manpages/lxc/storage/show/#lxc-storage-show-md) shows the cluster-wide configuration of the storage pool.

To view the member-specific configuration, use the [`--target`] flag. For example:

    lxc storage show data --target server2

## Create storage volumes[¶](#create-storage-volumes "Link to this heading")

For most storage drivers (all except for Ceph-based storage drivers), storage volumes are not replicated across the cluster and exist only on the member for which they were created. Run [[[`lxc`]` `[`storage`]` `[`volume`]` `[`list`]` `[`<pool_name>`]]](../../reference/manpages/lxc/storage/volume/list/#lxc-storage-volume-list-md) to see on which member a certain volume is located.

When creating a storage volume, use the [`--target`] flag to create a storage volume on a specific cluster member. Without the flag, the volume is created on the cluster member on which you run the command. For example, to create a volume on the current cluster member [`server1`]:

    lxc storage volume create local vol1

To create a volume with the same name on another cluster member:

    lxc storage volume create local vol1 --target server2

Different volumes can have the same name as long as they live on different cluster members. Typical examples for this are image volumes.

You can manage storage volumes in a cluster in the same way as you do in non-clustered deployments, except that you must pass the [`--target`] flag to your commands if more than one cluster member has a volume with the given name. For example, to show information about the storage volumes:

    lxc storage volume show local vol1 --target server1
    lxc storage volume show local vol1 --target server2