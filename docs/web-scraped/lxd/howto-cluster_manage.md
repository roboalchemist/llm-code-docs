# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/cluster_manage/

[]

# How to manage a cluster[¶](#how-to-manage-a-cluster "Link to this heading")

After your cluster is formed, use [[[`lxc`]` `[`cluster`]` `[`list`]]](../../reference/manpages/lxc/cluster/list/#lxc-cluster-list-md) to see a list of its members and their status. Example output:

[`user@host:~$`]` `

[[`lxc`]` `[`cluster`]` `[`list`]` `]

    +---------+----------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
    | NAME    |            URL             |      ROLES       | ARCHITECTURE | FAILURE DOMAIN | DESCRIPTION | STATE  |      MESSAGE      |
    +---------+----------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
    | server1 | https://192.0.2.101:8443   | database-leader  | x86_64       | default        |             | ONLINE | Fully operational |
    +---------+----------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
    | server2 | https://192.0.2.102:8443   | database-voter   | aarch64      | default        |             | ONLINE | Fully operational |
    +---------+----------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
    | server3 | https://192.0.2.103:8443   | database-standby | aarch64      | default        |             | ONLINE | Fully operational |
    +---------+----------------------------+------------------+--------------+----------------+-------------+--------+-------------------+

To see more detailed information about an individual cluster member, run the following command:

    lxc cluster show <member_name>

To see state and usage information for a cluster member, run the following command:

    lxc cluster info <member_name>

## Configure your cluster[¶](#configure-your-cluster "Link to this heading")

To configure your cluster, use [[[`lxc`]` `[`config`]]](../../reference/manpages/lxc/config/#lxc-config-md):

    lxc config set <server-config-option> <value>

Example:

    lxc config set cluster.max_voters 5

All LXD [[server configuration options]](../../server/#server) can be applied to cluster members.

Keep in mind that some options are global in scope, and others are local. When you configure an option with global scope on any cluster member, the changes are propagated to the other cluster members through the distributed database. The locally scoped options are set only on the cluster member where you configure them, unless you use the [`--target`] flag to specify a different cluster member.

In addition to the server configuration, there are [[cluster member configuration options]](../../reference/cluster_member_config/#cluster-member-config) that are specific to each cluster member. To set these configuration values, use [[[`lxc`]` `[`cluster`]` `[`set`]]](../../reference/manpages/lxc/cluster/set/#lxc-cluster-set-md):

    lxc cluster set <member-name> <member-config-option> <value>

Example:

    lxc cluster set server1 scheduler.instance manual

Alternatively, you can use the [[use the edit command]](#cluster-edit).

### Assign member roles[¶](#assign-member-roles "Link to this heading")

To add or remove a [[member role]](../../explanation/clusters/#clustering-member-roles) for a cluster member, use the [[[`lxc`]` `[`cluster`]` `[`role`]]](../../reference/manpages/lxc/cluster/role/#lxc-cluster-role-md) command:

    lxc cluster role add <member-name> <role>

Example:

    lxc cluster role add server1 event-hub

Note

You can add or remove only those roles that are not assigned automatically by LXD. To find out which roles are automatically assigned, see: [[Member roles]](../../explanation/clusters/#clustering-member-roles).

[]

### Edit the cluster member configuration[¶](#edit-the-cluster-member-configuration "Link to this heading")

To edit all properties of a cluster member, including the member-specific configuration, the member roles, the failure domain and the cluster groups, use the following command:

    lxc cluster edit

For more information, see: [[[`lxc`]` `[`cluster`]` `[`edit`]]](../../reference/manpages/lxc/cluster/edit/#lxc-cluster-edit-md).

[]

## Evacuate and restore cluster members[¶](#evacuate-and-restore-cluster-members "Link to this heading")

There are scenarios where you might need to empty a given cluster member of all its instances (for example, for routine maintenance like applying system updates that require a reboot, or to perform hardware changes). The [[evacuate]](#cluster-evacuate) and [[restore]](#cluster-restore) commands simplify this process.

[]

### Evacuate a cluster member[¶](#evacuate-a-cluster-member "Link to this heading")

The evacuation process migrates all instances on a given cluster member to other members in its cluster. The given member is then set to an "evacuated" state, which prevents the creation of any instances on it.

To begin this process, use the [[[`lxc`]` `[`cluster`]` `[`evacuate`]]](../../reference/manpages/lxc/cluster/evacuate/#lxc-cluster-evacuate-md) command:

    lxc cluster evacuate <member_name>

[]

### Restore an evacuated cluster member[¶](#restore-an-evacuated-cluster-member "Link to this heading")

When the evacuated cluster member is available again, use the [[[`lxc`]` `[`cluster`]` `[`restore`]]](../../reference/manpages/lxc/cluster/restore/#lxc-cluster-restore-md) command to return it to a normal running state:

    lxc cluster restore <member_name>

This command removes the cluster member's "evacuated" state, migrates the evacuated instances back from the cluster members that were temporarily holding them (using live migration if applicable), then restarts any instances that were shut down.

[]

### Evacuation mode and live migration[¶](#evacuation-mode-and-live-migration "Link to this heading")

You can control how each instance is migrated, via the [[`cluster.evacuate`]](../../reference/instance_options/#instance-miscellaneous:cluster.evacuate) instance configuration key. This key applies to the migrations performed during both evacuation and restoration. By default, any instances that are suitable for [[live migration]](../instances_migrate/#live-migration) will be live-migrated, and any that are not suitable will be shut down. See the [[`cluster.evacuate`]](../../reference/instance_options/#instance-miscellaneous:cluster.evacuate) reference documentation for further information.

If an instance is not suitable for live migration, it will be shut down cleanly before evacuation, respecting the [[`boot.host_shutdown_timeout`]](../../reference/instance_options/#instance-boot:boot.host_shutdown_timeout) configuration key.

Note

Any instance that you plan to live-migrate must have its [[`migration.stateful`]](../../reference/instance_options/#instance-migration:migration.stateful) configuration option set to [`true`]. Be aware that this option can only be set while the instance is stopped. Thus, for any instance to have the ability to be live-migrated in the future, this option must be set to [`true`] ahead of time.

[][]

## Cluster healing[¶](#cluster-automatic-evacuation "Link to this heading")

To enable cluster healing, set the [[`cluster.healing_threshold`]](../../server/#server-cluster:cluster.healing_threshold) configuration to a non-zero value (in seconds). If a cluster member is offline for longer than this threshold, LXD automatically sets its state to "evacuated" and starts its instances on another member. This behavior only applies to instances that use shared storage and have no local devices attached.

Syntax:

    lxc cluster set cluster.healing_threshold <value in seconds>

When the healed cluster member is available again, you must manually [[restore]](#cluster-restore) it to remove its "evacuated" state and return instances to it.

Warning

Enabling the cluster healing threshold carries the risk that LXD might incorrectly judge a cluster member as offline while it is still running workloads. Short-lived network issues or temporary high load might cause a cluster member to briefly stop responding to heartbeat or ICMP packets. If a healing threshold is set, LXD might then start that member's instances on another cluster member even though they're still active on the original. Since cluster members share the same storage, this can lead to data corruption.

To avoid this, it's critical to ensure that any server marked as offline is actually offline and not still running instances. You can automate this by monitoring for [`cluster-member-healed`] events and shutting off the affected server through its remote power interface, such as a Baseboard Management Controller (BMC) or Power Distribution Unit (PDU).

To reduce the chance of false healing events, set [[`cluster.healing_threshold`]](../../server/#server-cluster:cluster.healing_threshold) as high as possible within your availability targets.

[]

## Delete cluster members[¶](#delete-cluster-members "Link to this heading")

To cleanly delete a member from the cluster, use the following command:

    lxc cluster remove <member_name>

You can only cleanly delete members that are online and that don't have any instances located on them.

### Deal with offline cluster members[¶](#deal-with-offline-cluster-members "Link to this heading")

If a cluster member goes permanently offline, you can force-remove it from the cluster. Make sure to do so as soon as you discover that you cannot recover the member. If you keep an offline member in your cluster, you might encounter issues when upgrading your cluster to a newer version.

To force-remove a cluster member, enter the following command on one of the cluster members that is still online:

    lxc cluster remove --force <member_name>

Caution

Force-removing a cluster member will leave the member's database in an inconsistent state (for example, the storage pool on the member will not be removed). As a result, it will not be possible to re-initialize LXD later, and the server must be fully reinstalled.

[]

## Update or upgrade cluster members[¶](#update-or-upgrade-cluster-members "Link to this heading")

To update or upgrade a cluster, you must perform the same operation on all of its members, ensuring that they all use the same version of LXD.

Caution

Do not attempt to update or upgrade your cluster if any of its members are offline. Offline members cannot be updated or upgraded, and your cluster will end up in a blocked state.

Also note that if you are using the snap, updates might happen automatically, so to prevent any issues you should always recover or remove offline members immediately.

To update or upgrade the cluster, you must apply the change to each cluster member's LXD installation. If you are using the snap, see [[Manage updates]](../snap/#howto-snap-updates) for update instructions about updates, and [[Change the snap channel]](../snap/#howto-snap-change) for upgrade instructions.

If the new version of the daemon has database schema or API changes, the upgraded member might transition into a "blocked" state. In this case, the member does not serve any LXD API requests (which means that [`lxc`] commands don't work on that member anymore), but any running instances will continue to run.

This happens if there are other cluster members that have not been updated or upgraded, resulting in mismatched versions. Run [[[`lxc`]` `[`cluster`]` `[`list`]]](../../reference/manpages/lxc/cluster/list/#lxc-cluster-list-md) on a cluster member that is not blocked to see if any members are blocked.

As you proceed updating or upgrading the rest of the cluster members, they will all transition to the "blocked" state. When you update or upgrade the last member, the blocked members will notice that all LXD versions now match, and the blocked members become operational again.

## Update the cluster certificate[¶](#update-the-cluster-certificate "Link to this heading")

In a LXD cluster, the API on all servers responds with the same shared certificate, which is usually a standard self-signed certificate with an expiry set to ten years.

The certificate is stored at [`/var/snap/lxd/common/lxd/cluster.crt`] (if you use the snap) or [`/var/lib/lxd/cluster.crt`] (otherwise) and is the same on all cluster members.

You can replace the standard certificate with another one, such as a valid certificate obtained through ACME services (see [[TLS server certificate]](../../authentication/#authentication-server-certificate) for more information). To do so, run the following command on any cluster member:

    lxc cluster update-certificate

This command replaces the certificate on all cluster members. For more information, see: [[[`lxc`]` `[`cluster`]` `[`update-certificate`]]](../../reference/manpages/lxc/cluster/update-certificate/#lxc-cluster-update-certificate-md).