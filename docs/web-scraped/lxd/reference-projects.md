# Source: https://documentation.ubuntu.com/lxd/en/latest/reference/projects/

[]

# Project configuration[¶](#project-configuration "Link to this heading")

Projects can be configured through a set of key/value configuration options. See [[Configure a project]](../../howto/projects_create/#projects-configure) for instructions on how to set these options.

The key/value configuration is namespaced. The following options are available:

-   [[Project features]](#project-features)

-   [[Project limits]](#project-limits)

-   [[Project restrictions]](#project-restrictions)

-   [[Project-specific configuration]](#project-specific-config)

[]

## Project features[¶](#project-features "Link to this heading")

The project features define which entities are isolated in the project and which are inherited from the [`default`] project.

If a [`feature.*`] option is set to [`true`], the corresponding entity is isolated in the project.

Note

When you create a project without explicitly configuring a specific option, this option is set to the initial value given in the following table.

However, if you unset one of the [`feature.*`] options, it does not go back to the initial value, but to the default value. The default value for all [`feature.*`] options is [`false`].

[[`features.images`]][]

Whether to use a separate set of images for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-features:features.images)]

+-----------------------------------+------------------------------------------------------------+
| **Key:**                          | [`features.images`] |
+-----------------------------------+------------------------------------------------------------+
| **Type:**                         | []                                               |
|                                   |                                                            |
|                                   | bool                                                       |
+-----------------------------------+------------------------------------------------------------+
| **Default:**                      | []                                               |
|                                   |                                                            |
|                                   | [`false`]           |
+-----------------------------------+------------------------------------------------------------+
| **Initial value:**                | []                                               |
|                                   |                                                            |
|                                   | [`true`]            |
+-----------------------------------+------------------------------------------------------------+

This setting applies to both images and image aliases.

[[`features.networks`]][]

Whether to use a separate set of networks for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-features:features.networks)]

+-----------------------------------+--------------------------------------------------------------+
| **Key:**                          | [`features.networks`] |
+-----------------------------------+--------------------------------------------------------------+
| **Type:**                         | []                                                 |
|                                   |                                                              |
|                                   | bool                                                         |
+-----------------------------------+--------------------------------------------------------------+
| **Default:**                      | []                                                 |
|                                   |                                                              |
|                                   | [`false`]             |
+-----------------------------------+--------------------------------------------------------------+
| **Initial value:**                | []                                                 |
|                                   |                                                              |
|                                   | [`false`]             |
+-----------------------------------+--------------------------------------------------------------+

[[`features.networks.zones`]][]

Whether to use a separate set of network zones for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-features:features.networks.zones)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`features.networks.zones`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | bool                                                               |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`false`]                   |
+-----------------------------------+--------------------------------------------------------------------+
| **Initial value:**                | []                                                       |
|                                   |                                                                    |
|                                   | [`false`]                   |
+-----------------------------------+--------------------------------------------------------------------+

[[`features.profiles`]][]

Whether to use a separate set of profiles for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-features:features.profiles)]

+-----------------------------------+--------------------------------------------------------------+
| **Key:**                          | [`features.profiles`] |
+-----------------------------------+--------------------------------------------------------------+
| **Type:**                         | []                                                 |
|                                   |                                                              |
|                                   | bool                                                         |
+-----------------------------------+--------------------------------------------------------------+
| **Default:**                      | []                                                 |
|                                   |                                                              |
|                                   | [`false`]             |
+-----------------------------------+--------------------------------------------------------------+
| **Initial value:**                | []                                                 |
|                                   |                                                              |
|                                   | [`true`]              |
+-----------------------------------+--------------------------------------------------------------+

[[`features.storage.buckets`]][]

Whether to use a separate set of storage buckets for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-features:features.storage.buckets)]

+-----------------------------------+---------------------------------------------------------------------+
| **Key:**                          | [`features.storage.buckets`] |
+-----------------------------------+---------------------------------------------------------------------+
| **Type:**                         | []                                                        |
|                                   |                                                                     |
|                                   | bool                                                                |
+-----------------------------------+---------------------------------------------------------------------+
| **Default:**                      | []                                                        |
|                                   |                                                                     |
|                                   | [`false`]                    |
+-----------------------------------+---------------------------------------------------------------------+
| **Initial value:**                | []                                                        |
|                                   |                                                                     |
|                                   | [`true`]                     |
+-----------------------------------+---------------------------------------------------------------------+

[[`features.storage.volumes`]][]

Whether to use a separate set of storage volumes for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-features:features.storage.volumes)]

+-----------------------------------+---------------------------------------------------------------------+
| **Key:**                          | [`features.storage.volumes`] |
+-----------------------------------+---------------------------------------------------------------------+
| **Type:**                         | []                                                        |
|                                   |                                                                     |
|                                   | bool                                                                |
+-----------------------------------+---------------------------------------------------------------------+
| **Default:**                      | []                                                        |
|                                   |                                                                     |
|                                   | [`false`]                    |
+-----------------------------------+---------------------------------------------------------------------+
| **Initial value:**                | []                                                        |
|                                   |                                                                     |
|                                   | [`true`]                     |
+-----------------------------------+---------------------------------------------------------------------+

[]

## Project limits[¶](#project-limits "Link to this heading")

Project limits define a hard upper bound for the resources that can be used by the containers and VMs that belong to a project.

Depending on the [`limits.*`] option, the limit applies to the number of entities that are allowed in the project (for example, [[`limits.containers`]](#project-limits:limits.containers) or [[`limits.networks`]](#project-limits:limits.networks)) or to the aggregate value of resource usage for all instances in the project (for example, [[`limits.cpu`]](#project-limits:limits.cpu) or [[`limits.processes`]](#project-limits:limits.processes)). In the latter case, the limit usually applies to the [[Resource limits]](../instance_options/#instance-options-limits) that are configured for each instance (either directly or via a profile), and not to the resources that are actually in use.

For example, if you set the project's [[`limits.memory`]](#project-limits:limits.memory) configuration to [`50GiB`], the sum of the individual values of all [[`limits.memory`]](../instance_options/#instance-resource-limits:limits.memory) configuration keys defined on the project's instances will be kept under 50 GiB.

Similarly, setting the project's [[`limits.cpu`]](#project-limits:limits.cpu) configuration key to [`100`] means that the sum of individual [[`limits.cpu`]](../instance_options/#instance-resource-limits:limits.cpu) values will be kept below 100.

When using project limits, the following conditions must be fulfilled:

-   When you set one of the [`limits.*`] configurations and there is a corresponding configuration for the instance, all instances in the project must have the corresponding configuration defined (either directly or via a profile). See [[Resource limits]](../instance_options/#instance-options-limits) for the instance configuration options.

-   The [[`limits.cpu`]](#project-limits:limits.cpu) configuration cannot be used if [[CPU pinning]](../instance_options/#instance-options-limits-cpu) is enabled. This means that to use [[`limits.cpu`]](#project-limits:limits.cpu) on a project, the [[`limits.cpu`]](../instance_options/#instance-resource-limits:limits.cpu) configuration of each instance in the project must be set to a number of CPUs, not a set or a range of CPUs.

-   The [[`limits.memory`]](#project-limits:limits.memory) configuration must be set to an absolute value, not a percentage.

[[`limits.containers`]][]

Maximum number of containers that can be created in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.containers)]

+-----------------------------------+--------------------------------------------------------------+
| **Key:**                          | [`limits.containers`] |
+-----------------------------------+--------------------------------------------------------------+
| **Type:**                         | []                                                 |
|                                   |                                                              |
|                                   | integer                                                      |
+-----------------------------------+--------------------------------------------------------------+

[[`limits.cpu`]][]

Maximum number of CPUs to use in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.cpu)]

+-----------------------------------+-------------------------------------------------------+
| **Key:**                          | [`limits.cpu`] |
+-----------------------------------+-------------------------------------------------------+
| **Type:**                         | []                                          |
|                                   |                                                       |
|                                   | integer                                               |
+-----------------------------------+-------------------------------------------------------+

This value is the maximum value for the sum of the individual [[`limits.cpu`]](../instance_options/#instance-resource-limits:limits.cpu) configurations set on the instances of the project.

[[`limits.disk`]][]

Maximum disk space used by the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.disk)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`limits.disk`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | string                                                 |
+-----------------------------------+--------------------------------------------------------+

This value is the maximum value of the aggregate disk space used by all instance volumes, custom volumes, and images of the project.

[[`limits.disk.pool.POOL_NAME`]][]

Maximum disk space used by the project on this pool

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.disk.pool.POOL_NAME)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`limits.disk.pool.POOL_NAME`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | string                                                                |
+-----------------------------------+-----------------------------------------------------------------------+

This value is the maximum value of the aggregate disk space used by all instance volumes, custom volumes, and images of the project on this specific storage pool.

When set to 0, the pool is excluded from storage pool list for the project.

[[`limits.instances`]][]

Maximum number of instances that can be created in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.instances)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`limits.instances`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | integer                                                     |
+-----------------------------------+-------------------------------------------------------------+

[[`limits.memory`]][]

Usage limit for the host's memory for the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.memory)]

+-----------------------------------+----------------------------------------------------------+
| **Key:**                          | [`limits.memory`] |
+-----------------------------------+----------------------------------------------------------+
| **Type:**                         | []                                             |
|                                   |                                                          |
|                                   | string                                                   |
+-----------------------------------+----------------------------------------------------------+

The value is the maximum value for the sum of the individual [[`limits.memory`]](../instance_options/#instance-resource-limits:limits.memory) configurations set on the instances of the project.

[[`limits.networks`]][]

Maximum number of networks that the project can have

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.networks)]

+-----------------------------------+------------------------------------------------------------+
| **Key:**                          | [`limits.networks`] |
+-----------------------------------+------------------------------------------------------------+
| **Type:**                         | []                                               |
|                                   |                                                            |
|                                   | integer                                                    |
+-----------------------------------+------------------------------------------------------------+

[[`limits.networks.uplink_ips.ipv4.NETWORK_NAME`]][]

Quota of IPv4 addresses from a specified uplink network that can be used by entities in this project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.networks.uplink_ips.ipv4.NETWORK_NAME)]

+-----------------------------------+-----------------------------------------------------------------------------------------+
| **Key:**                          | [`limits.networks.uplink_ips.ipv4.NETWORK_NAME`] |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                            |
|                                   |                                                                                         |
|                                   | string                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------+

Maximum number of IPv4 addresses that this project can consume from the specified uplink network. This number of IPs can be consumed by networks, forwards and load balancers in this project.

[[`limits.networks.uplink_ips.ipv6.NETWORK_NAME`]][]

Quota of IPv6 addresses from a specified uplink network that can be used by entities in this project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.networks.uplink_ips.ipv6.NETWORK_NAME)]

+-----------------------------------+-----------------------------------------------------------------------------------------+
| **Key:**                          | [`limits.networks.uplink_ips.ipv6.NETWORK_NAME`] |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                            |
|                                   |                                                                                         |
|                                   | string                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------+

Maximum number of IPv6 addresses that this project can consume from the specified uplink network. This number of IPs can be consumed by networks, forwards and load balancers in this project.

[[`limits.processes`]][]

Maximum number of processes within the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.processes)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`limits.processes`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | integer                                                     |
+-----------------------------------+-------------------------------------------------------------+

This value is the maximum value for the sum of the individual [[`limits.processes`]](../instance_options/#instance-resource-limits:limits.processes) configurations set on the instances of the project.

[[`limits.virtual-machines`]][]

Maximum number of VMs that can be created in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-limits:limits.virtual-machines)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`limits.virtual-machines`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | integer                                                            |
+-----------------------------------+--------------------------------------------------------------------+

[]

## Project restrictions[¶](#project-restrictions "Link to this heading")

To prevent the instances of a project from accessing security-sensitive features (such as container nesting or raw LXC configuration), set the [[`restricted`]](#project-restricted:restricted) configuration option to [`true`]. You can then use the various [`restricted.*`] options to pick individual features that would normally be blocked by [[`restricted`]](#project-restricted:restricted) and allow them, so they can be used by the instances of the project.

For example, to restrict a project and block all security-sensitive features, but allow container nesting, enter the following commands:

    lxc project set <project_name> restricted=true
    lxc project set <project_name> restricted.containers.nesting=allow

Each security-sensitive feature has an associated [`restricted.*`] project configuration option. If you want to allow the usage of a feature, change the value of its [`restricted.*`] option. Most [`restricted.*`] configurations are binary switches that can be set to either [`block`] (the default) or [`allow`]. However, some options support other values for more fine-grained control.

Note

You must set the [`restricted`] configuration to [`true`] for any of the [`restricted.*`] options to be effective. If [`restricted`] is set to [`false`], changing a [`restricted.*`] option has no effect.

Setting all [`restricted.*`] keys to [`allow`] is equivalent to setting [`restricted`] itself to [`false`].

[[`restricted`]][]

Whether to block access to security-sensitive features

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted)]

+-----------------------------------+-------------------------------------------------------+
| **Key:**                          | [`restricted`] |
+-----------------------------------+-------------------------------------------------------+
| **Type:**                         | []                                          |
|                                   |                                                       |
|                                   | bool                                                  |
+-----------------------------------+-------------------------------------------------------+
| **Default:**                      | []                                          |
|                                   |                                                       |
|                                   | [`false`]      |
+-----------------------------------+-------------------------------------------------------+

This option must be enabled to allow the [`restricted.*`] keys to take effect. To temporarily remove the restrictions, you can disable this option instead of clearing the related keys.

[[`restricted.backups`]][]

When set to [`block`], creating instance or volume backups is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.backups)]

+-----------------------------------+---------------------------------------------------------------+
| **Key:**                          | [`restricted.backups`] |
+-----------------------------------+---------------------------------------------------------------+
| **Type:**                         | []                                                  |
|                                   |                                                               |
|                                   | string                                                        |
+-----------------------------------+---------------------------------------------------------------+
| **Default:**                      | []                                                  |
|                                   |                                                               |
|                                   | [`block`]              |
+-----------------------------------+---------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.cluster.groups`]][]

Cluster groups that can be targeted

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.cluster.groups)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`restricted.cluster.groups`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+

If specified, this option prevents targeting cluster groups other than the provided ones.

[[`restricted.cluster.target`]][]

When set to [`block`], targeting of cluster members is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.cluster.target)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`restricted.cluster.target`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+
| **Default:**                      | []                                                         |
|                                   |                                                                      |
|                                   | [`block`]                     |
+-----------------------------------+----------------------------------------------------------------------+

Possible values are [`allow`] or [`block`]. When set to [`allow`], this option allows targeting of cluster members (either directly or via a group) when creating or moving instances.

[[`restricted.containers.interception`]][]

When set to [`block`], using system call interception options is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.containers.interception)]

+-----------------------------------+-------------------------------------------------------------------------------+
| **Key:**                          | [`restricted.containers.interception`] |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Type:**                         | []                                                                  |
|                                   |                                                                               |
|                                   | string                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Default:**                      | []                                                                  |
|                                   |                                                                               |
|                                   | [`block`]                              |
+-----------------------------------+-------------------------------------------------------------------------------+

Possible values are [`allow`], [`block`], or [`full`]. When set to [`allow`], interception options that are usually safe are allowed. File system mounting remains blocked.

[[`restricted.containers.lowlevel`]][]

When set to [`block`], using low-level container options is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.containers.lowlevel)]

+-----------------------------------+---------------------------------------------------------------------------+
| **Key:**                          | [`restricted.containers.lowlevel`] |
+-----------------------------------+---------------------------------------------------------------------------+
| **Type:**                         | []                                                              |
|                                   |                                                                           |
|                                   | string                                                                    |
+-----------------------------------+---------------------------------------------------------------------------+
| **Default:**                      | []                                                              |
|                                   |                                                                           |
|                                   | [`block`]                          |
+-----------------------------------+---------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`]. When set to [`allow`], low-level container options like [[`raw.lxc`]](../instance_options/#instance-raw:raw.lxc), [[`raw.idmap`]](../instance_options/#instance-raw:raw.idmap), [`volatile.*`], etc. can be used.

[[`restricted.containers.nesting`]][]

When set to [`block`], running nested LXD is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.containers.nesting)]

+-----------------------------------+--------------------------------------------------------------------------+
| **Key:**                          | [`restricted.containers.nesting`] |
+-----------------------------------+--------------------------------------------------------------------------+
| **Type:**                         | []                                                             |
|                                   |                                                                          |
|                                   | string                                                                   |
+-----------------------------------+--------------------------------------------------------------------------+
| **Default:**                      | []                                                             |
|                                   |                                                                          |
|                                   | [`block`]                         |
+-----------------------------------+--------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`]. When set to [`allow`], [[`security.nesting`]](../instance_options/#instance-security:security.nesting) can be set to [`true`] for an instance.

[[`restricted.containers.privilege`]][]

Which settings for privileged containers to prevent

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.containers.privilege)]

+-----------------------------------+----------------------------------------------------------------------------+
| **Key:**                          | [`restricted.containers.privilege`] |
+-----------------------------------+----------------------------------------------------------------------------+
| **Type:**                         | []                                                               |
|                                   |                                                                            |
|                                   | string                                                                     |
+-----------------------------------+----------------------------------------------------------------------------+
| **Default:**                      | []                                                               |
|                                   |                                                                            |
|                                   | [`unprivileged`]                    |
+-----------------------------------+----------------------------------------------------------------------------+

Possible values are [`unprivileged`], [`isolated`], and [`allow`].

-   When set to [`unpriviliged`], this option prevents setting [[`security.privileged`]](../instance_options/#instance-security:security.privileged) to [`true`].

-   When set to [`isolated`], this option prevents setting [[`security.privileged`]](../instance_options/#instance-security:security.privileged) to [`true`] and forces using a unique idmap per container using [[`security.idmap.isolated`]](../instance_options/#instance-security:security.idmap.isolated) set to [`true`].

-   When set to [`allow`], there is no restriction.

[[`restricted.devices.disk`]][]

Which disk devices can be used

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.disk)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.disk`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | string                                                             |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`managed`]                 |
+-----------------------------------+--------------------------------------------------------------------+

Possible values are [`allow`], [`block`], or [`managed`].

-   When set to [`block`], this option prevents using all disk devices except the root one.

-   When set to [`managed`], this option allows using disk devices only if [`pool=`] is set.

-   When set to [`allow`], there is no restriction on which disk devices can be used.

    ::: 
    Important

    When allowing all disk devices, make sure to set [[`restricted.devices.disk.paths`]](#project-restricted:restricted.devices.disk.paths) to a list of path prefixes that you want to allow. If you do not restrict the allowed paths, users can attach any disk device, including shifted devices ([`disk`] devices with [[[`shift`]]](../devices_disk/#devices-disk-options) set to [`true`]), which can be used to gain root access to the system.
    :::

[[`restricted.devices.disk.paths`]][]

Which [`source`] can be used for [`disk`] devices

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.disk.paths)]

+-----------------------------------+--------------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.disk.paths`] |
+-----------------------------------+--------------------------------------------------------------------------+
| **Type:**                         | []                                                             |
|                                   |                                                                          |
|                                   | string                                                                   |
+-----------------------------------+--------------------------------------------------------------------------+

If [[`restricted.devices.disk`]](#project-restricted:restricted.devices.disk) is set to [`allow`], this option controls which [`source`] can be used for [`disk`] devices. Specify a comma-separated list of path prefixes that restrict the [`source`] setting. If this option is left empty, all paths are allowed.

[[`restricted.devices.gpu`]][]

When set to [`block`], using devices of type [`gpu`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.gpu)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.gpu`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`block`]                  |
+-----------------------------------+-------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.infiniband`]][]

When set to [`block`], using devices of type [`infiniband`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.infiniband)]

+-----------------------------------+--------------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.infiniband`] |
+-----------------------------------+--------------------------------------------------------------------------+
| **Type:**                         | []                                                             |
|                                   |                                                                          |
|                                   | string                                                                   |
+-----------------------------------+--------------------------------------------------------------------------+
| **Default:**                      | []                                                             |
|                                   |                                                                          |
|                                   | [`block`]                         |
+-----------------------------------+--------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.nic`]][]

Which network devices can be used

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.nic)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.nic`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`managed`]                |
+-----------------------------------+-------------------------------------------------------------------+

Possible values are [`allow`], [`block`], or [`managed`].

-   When set to [`block`], this option prevents using all network devices.

-   When set to [`managed`], this option allows using network devices only if [`network=`] is set.

-   When set to [`allow`], there is no restriction on which network devices can be used.

[[`restricted.devices.pci`]][]

When set to [`block`], using devices of type [`pci`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.pci)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.pci`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`block`]                  |
+-----------------------------------+-------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.proxy`]][]

When set to [`block`], using devices of type [`proxy`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.proxy)]

+-----------------------------------+---------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.proxy`] |
+-----------------------------------+---------------------------------------------------------------------+
| **Type:**                         | []                                                        |
|                                   |                                                                     |
|                                   | string                                                              |
+-----------------------------------+---------------------------------------------------------------------+
| **Default:**                      | []                                                        |
|                                   |                                                                     |
|                                   | [`block`]                    |
+-----------------------------------+---------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.unix-block`]][]

When set to [`block`], using devices of type [`unix-block`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.unix-block)]

+-----------------------------------+--------------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.unix-block`] |
+-----------------------------------+--------------------------------------------------------------------------+
| **Type:**                         | []                                                             |
|                                   |                                                                          |
|                                   | string                                                                   |
+-----------------------------------+--------------------------------------------------------------------------+
| **Default:**                      | []                                                             |
|                                   |                                                                          |
|                                   | [`block`]                         |
+-----------------------------------+--------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.unix-char`]][]

When set to [`block`], using devices of type [`unix-char`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.unix-char)]

+-----------------------------------+-------------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.unix-char`] |
+-----------------------------------+-------------------------------------------------------------------------+
| **Type:**                         | []                                                            |
|                                   |                                                                         |
|                                   | string                                                                  |
+-----------------------------------+-------------------------------------------------------------------------+
| **Default:**                      | []                                                            |
|                                   |                                                                         |
|                                   | [`block`]                        |
+-----------------------------------+-------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.unix-hotplug`]][]

When set to [`block`], using devices of type [`unix-hotplug`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.unix-hotplug)]

+-----------------------------------+----------------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.unix-hotplug`] |
+-----------------------------------+----------------------------------------------------------------------------+
| **Type:**                         | []                                                               |
|                                   |                                                                            |
|                                   | string                                                                     |
+-----------------------------------+----------------------------------------------------------------------------+
| **Default:**                      | []                                                               |
|                                   |                                                                            |
|                                   | [`block`]                           |
+-----------------------------------+----------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.devices.usb`]][]

When set to [`block`], using devices of type [`usb`] is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.devices.usb)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`restricted.devices.usb`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`block`]                  |
+-----------------------------------+-------------------------------------------------------------------+

Possible values are [`allow`] or [`block`].

[[`restricted.idmap.gid`]][]

Which host GID ranges are allowed in [`raw.idmap`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.idmap.gid)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`restricted.idmap.gid`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+

This option specifies the host GID ranges that are allowed in the instance's [[`raw.idmap`]](../instance_options/#instance-raw:raw.idmap) setting.

[[`restricted.idmap.uid`]][]

Which host UID ranges are allowed in [`raw.idmap`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.idmap.uid)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`restricted.idmap.uid`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+

This option specifies the host UID ranges that are allowed in the instance's [[`raw.idmap`]](../instance_options/#instance-raw:raw.idmap) setting.

[[`restricted.networks.access`]][]

Which network names are allowed for use in this project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.networks.access)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`restricted.networks.access`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | string                                                                |
+-----------------------------------+-----------------------------------------------------------------------+

Specify a comma-delimited list of network names that are allowed for use in this project. If this option is not set, all networks are accessible.

Note that this setting depends on the [[`restricted.devices.nic`]](#project-restricted:restricted.devices.nic) setting.

[[`restricted.networks.subnets`]][]

Which network subnets are allocated for use in this project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.networks.subnets)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`restricted.networks.subnets`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | string                                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| **Default:**                      | []                                                           |
|                                   |                                                                        |
|                                   | [`block`]                       |
+-----------------------------------+------------------------------------------------------------------------+

Specify a comma-delimited list of CIDR network routes from the uplink network's [[`ipv4.routes`]](../network_physical/#network-physical-network-conf:ipv4.routes) [[`ipv6.routes`]](../network_physical/#network-physical-network-conf:ipv6.routes) that are allowed for use in this project. Use the form [`<uplink>:<subnet>`].

Example value: [`lxdbr0:192.0.168.0/24,lxdbr0:10.1.19.5/32`]

[[`restricted.networks.uplinks`]][]

Which network names can be used as uplink in this project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.networks.uplinks)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`restricted.networks.uplinks`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | string                                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| **Default:**                      | []                                                           |
|                                   |                                                                        |
|                                   | [`block`]                       |
+-----------------------------------+------------------------------------------------------------------------+

Specify a comma-delimited list of network names that can be used as uplink for networks in this project.

[[`restricted.networks.zones`]][]

Which network zones can be used in this project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.networks.zones)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`restricted.networks.zones`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+
| **Default:**                      | []                                                         |
|                                   |                                                                      |
|                                   | [`block`]                     |
+-----------------------------------+----------------------------------------------------------------------+

Specify a comma-delimited list of network zones that can be used (or something under them) in this project.

[[`restricted.snapshots`]][]

When set to [`block`], creating instance or volume snapshots is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.snapshots)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`restricted.snapshots`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Default:**                      | []                                                    |
|                                   |                                                                 |
|                                   | [`block`]                |
+-----------------------------------+-----------------------------------------------------------------+

[[`restricted.virtual-machines.lowlevel`]][]

When set to [`block`], using low-level VM options is prevented

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-restricted:restricted.virtual-machines.lowlevel)]

+-----------------------------------+---------------------------------------------------------------------------------+
| **Key:**                          | [`restricted.virtual-machines.lowlevel`] |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Type:**                         | []                                                                    |
|                                   |                                                                                 |
|                                   | string                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Default:**                      | []                                                                    |
|                                   |                                                                                 |
|                                   | [`block`]                                |
+-----------------------------------+---------------------------------------------------------------------------------+

Possible values are [`allow`] or [`block`]. When set to [`allow`], low-level VM options like [[`raw.qemu`]](../instance_options/#instance-raw:raw.qemu), [`volatile.*`], etc. can be used.

[]

## Project-specific configuration[¶](#project-specific-configuration "Link to this heading")

There are some [[Server configuration]](../../server/#server) options that you can override for a project. In addition, you can add user metadata for a project.

[[`backups.compression_algorithm`]][]

Compression algorithm to use for backups

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:backups.compression_algorithm)]

+-----------------------------------+--------------------------------------------------------------------------+
| **Key:**                          | [`backups.compression_algorithm`] |
+-----------------------------------+--------------------------------------------------------------------------+
| **Type:**                         | []                                                             |
|                                   |                                                                          |
|                                   | string                                                                   |
+-----------------------------------+--------------------------------------------------------------------------+

Specify which compression algorithm to use for backups in this project. Possible values are [`bzip2`], [`gzip`], [`lzma`], [`xz`], or [`none`].

[[`images.auto_update_cached`]][]

Whether to automatically update cached images in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:images.auto_update_cached)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`images.auto_update_cached`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | bool                                                                 |
+-----------------------------------+----------------------------------------------------------------------+

[[`images.auto_update_interval`]][]

Interval at which to look for updates to cached images

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:images.auto_update_interval)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`images.auto_update_interval`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | integer                                                                |
+-----------------------------------+------------------------------------------------------------------------+

Specify the interval in hours. To disable looking for updates to cached images, set this option to [`0`].

[[`images.compression_algorithm`]][]

Compression algorithm to use for new images in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:images.compression_algorithm)]

+-----------------------------------+-------------------------------------------------------------------------+
| **Key:**                          | [`images.compression_algorithm`] |
+-----------------------------------+-------------------------------------------------------------------------+
| **Type:**                         | []                                                            |
|                                   |                                                                         |
|                                   | string                                                                  |
+-----------------------------------+-------------------------------------------------------------------------+

Possible values are [`bzip2`], [`gzip`], [`lzma`], [`xz`], or [`none`].

[[`images.default_architecture`]][]

Default architecture to use in a mixed-architecture cluster

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:images.default_architecture)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`images.default_architecture`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | string                                                                 |
+-----------------------------------+------------------------------------------------------------------------+

[[`images.remote_cache_expiry`]][]

When an unused cached remote image is flushed in the project

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:images.remote_cache_expiry)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`images.remote_cache_expiry`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | integer                                                               |
+-----------------------------------+-----------------------------------------------------------------------+

Specify the number of days after which the unused cached image expires.

[[`user.*`]][]

User-provided free-form key/value pairs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#project-specific:user.*)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`user.*`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | string                                            |
+-----------------------------------+---------------------------------------------------+

## Related topics[¶](#related-topics "Link to this heading")

How-to guides:

-   [[Projects]](../../projects/#projects)

Explanation:

-   [[Instances grouping with projects]](../../explanation/projects/#exp-projects)