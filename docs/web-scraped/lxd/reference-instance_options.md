# Source: https://documentation.ubuntu.com/lxd/en/latest/reference/instance_options/

[]

# Instance options[¶](#instance-options "Link to this heading")

Instance options are configuration options that are directly related to the instance.

See [[Configure instance options]](../../howto/instances_configure/#instances-configure-options) for instructions on how to set the instance options.

The key/value configuration is namespaced. The following options are available:

-   [[Miscellaneous options]](#instance-options-misc)

-   [[Boot-related options]](#instance-options-boot)

-   [[[`cloud-init`] configuration]](#instance-options-cloud-init)

-   [[Resource limits]](#instance-options-limits)

-   [[Migration options]](#instance-options-migration)

-   [[Placement options]](#instance-options-placement)

-   [[NVIDIA and CUDA configuration]](#instance-options-nvidia)

-   [[Raw instance configuration overrides]](#instance-options-raw)

-   [[Security policies]](#instance-options-security)

-   [[Snapshot scheduling and configuration]](#instance-options-snapshots)

-   [[Volatile internal data]](#instance-options-volatile)

Note that while a type is defined for each option, all values are stored as strings and should be exported over the REST API as strings (which makes it possible to support any extra values without breaking backward compatibility).

[]

## Miscellaneous options[¶](#miscellaneous-options "Link to this heading")

In addition to the configuration options listed in the following sections, these instance options are supported:

[[`agent.nic_config`]][]

Whether to use the name and MTU of the default network interfaces

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:agent.nic_config)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`agent.nic_config`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | bool                                                        |
+-----------------------------------+-------------------------------------------------------------+
| **Default:**                      | []                                                |
|                                   |                                                             |
|                                   | [`false`]            |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | no                                                          |
+-----------------------------------+-------------------------------------------------------------+
| **Condition:**                    | []                                                |
|                                   |                                                             |
|                                   | virtual machine                                             |
+-----------------------------------+-------------------------------------------------------------+

When set to true, the name and MTU of the default network interfaces inside the virtual machine will match those of the instance devices.

[[`cluster.evacuate`]][]

What to do when evacuating the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:cluster.evacuate)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`cluster.evacuate`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | string                                                      |
+-----------------------------------+-------------------------------------------------------------+
| **Default:**                      | []                                                |
|                                   |                                                             |
|                                   | [`auto`]             |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | no                                                          |
+-----------------------------------+-------------------------------------------------------------+

The [`cluster.evacuate`] provides control over how instances are handled when a cluster member is being evacuated.

Available Modes:

-   [`auto`] *(default)*: The system will automatically decide the best evacuation method based on the instance's type and configured devices:

    -   If any device is not suitable for migration, the instance will not be migrated (only stopped).

    -   Live migration will be used only for virtual machines with the [`migration.stateful`] setting enabled and for which all its devices can be migrated as well.

-   [`live-migrate`]: Instances are live-migrated to another node. This means the instance remains running and operational during the migration process, ensuring minimal disruption.

-   [`migrate`]: In this mode, instances are migrated to another node in the cluster. The migration process will not be live, meaning there will be a brief downtime for the instance during the migration.

-   [`stop`]: Instances are not migrated. Instead, they are stopped on the current node.

See [[Evacuate a cluster member]](../../howto/cluster_manage/#cluster-evacuate) for more information.

[[`linux.kernel_modules`]][]

Kernel modules to load or allow loading

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:linux.kernel_modules)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`linux.kernel_modules`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | yes                                                             |
+-----------------------------------+-----------------------------------------------------------------+
| **Condition:**                    | []                                                    |
|                                   |                                                                 |
|                                   | container                                                       |
+-----------------------------------+-----------------------------------------------------------------+

Specify the kernel modules as a comma-separated list.

The modules are loaded before the instance starts, or they can be loaded by a privileged user if [[`linux.kernel_modules.load`]](#instance-miscellaneous:linux.kernel_modules.load) is set to [`ondemand`].

[[`linux.kernel_modules.load`]][]

How to load kernel modules

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:linux.kernel_modules.load)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`linux.kernel_modules.load`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+
| **Default:**                      | []                                                         |
|                                   |                                                                      |
|                                   | [`boot`]                      |
+-----------------------------------+----------------------------------------------------------------------+
| **Live update:**                  | []                                                         |
|                                   |                                                                      |
|                                   | no                                                                   |
+-----------------------------------+----------------------------------------------------------------------+
| **Condition:**                    | []                                                         |
|                                   |                                                                      |
|                                   | container                                                            |
+-----------------------------------+----------------------------------------------------------------------+

This option specifies how to load the kernel modules that are specified in [[`linux.kernel_modules`]](#instance-miscellaneous:linux.kernel_modules). Possible values are [`boot`] (load the modules when booting the container) and [`ondemand`] (intercept the [`finit_modules()`] syscall and allow a privileged user in the container's user namespace to load the modules).

[[`linux.sysctl.*`]][]

Override for the corresponding [`sysctl`] setting in the container

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:linux.sysctl.*)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`linux.sysctl.*`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | string                                                    |
+-----------------------------------+-----------------------------------------------------------+
| **Live update:**                  | []                                              |
|                                   |                                                           |
|                                   | no                                                        |
+-----------------------------------+-----------------------------------------------------------+
| **Condition:**                    | []                                              |
|                                   |                                                           |
|                                   | container                                                 |
+-----------------------------------+-----------------------------------------------------------+

[[`ubuntu_pro.guest_attach`]][]

Whether to auto-attach Ubuntu Pro.

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:ubuntu_pro.guest_attach)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`ubuntu_pro.guest_attach`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | string                                                             |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+

Indicate whether the guest should auto-attach Ubuntu Pro at start up.

See [[How to configure Ubuntu Pro guest attachment]](../../howto/instances_ubuntu_pro_attach/#instances-ubuntu-pro-attach) for more information.

[[`user.*`]][]

Free-form user key/value storage

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:user.*)]

+-----------------------------------+---------------------------------------------------+
| **Key:**                          | [`user.*`] |
+-----------------------------------+---------------------------------------------------+
| **Type:**                         | []                                      |
|                                   |                                                   |
|                                   | string                                            |
+-----------------------------------+---------------------------------------------------+
| **Live update:**                  | []                                      |
|                                   |                                                   |
|                                   | no                                                |
+-----------------------------------+---------------------------------------------------+

User keys can be used in search.

[[`environment.*`]][]

Environment variables for the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-miscellaneous:environment.*)]

+-----------------------------------+----------------------------------------------------------+
| **Key:**                          | [`environment.*`] |
+-----------------------------------+----------------------------------------------------------+
| **Type:**                         | []                                             |
|                                   |                                                          |
|                                   | string                                                   |
+-----------------------------------+----------------------------------------------------------+
| **Live update:**                  | []                                             |
|                                   |                                                          |
|                                   | yes (exec)                                               |
+-----------------------------------+----------------------------------------------------------+

You can export key/value environment variables to the instance. These are then set for [[[`lxc`]` `[`exec`]]](../manpages/lxc/exec/#lxc-exec-md).

[]

## Boot-related options[¶](#boot-related-options "Link to this heading")

The following instance options control the boot-related behavior of the instance:

[[`boot.autostart`]][]

Whether to always start the instance when LXD starts

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-boot:boot.autostart)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`boot.autostart`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | bool                                                      |
+-----------------------------------+-----------------------------------------------------------+
| **Live update:**                  | []                                              |
|                                   |                                                           |
|                                   | no                                                        |
+-----------------------------------+-----------------------------------------------------------+

If set to [`true`], the instance will always be auto-started, unless [`security.protection.start`] is also enabled. If set to [`false`], the instance will not be started on LXD start up. If this option is not set, the instance will be restored to its last known state.

[[`boot.autostart.delay`]][]

Delay after starting the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-boot:boot.autostart.delay)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`boot.autostart.delay`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | integer                                                         |
+-----------------------------------+-----------------------------------------------------------------+
| **Default:**                      | []                                                    |
|                                   |                                                                 |
|                                   | [`0`]                    |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | no                                                              |
+-----------------------------------+-----------------------------------------------------------------+

The number of seconds to wait after the instance started before starting the next one.

[[`boot.autostart.priority`]][]

What order to start the instances in

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-boot:boot.autostart.priority)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`boot.autostart.priority`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | integer                                                            |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`0`]                       |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+

The instance with the highest value is started first.

[[`boot.debug_edk2`]][]

Enable debug version of the [`edk2`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-boot:boot.debug_edk2)]

+-----------------------------------+------------------------------------------------------------+
| **Key:**                          | [`boot.debug_edk2`] |
+-----------------------------------+------------------------------------------------------------+
| **Type:**                         | []                                               |
|                                   |                                                            |
|                                   | bool                                                       |
+-----------------------------------+------------------------------------------------------------+

The instance should use a debug version of the [`edk2`]. A log file can be found in [`$LXD_DIR/logs/<instance_name>/edk2.log`].

[[`boot.host_shutdown_timeout`]][]

How long to wait for the instance to shut down

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-boot:boot.host_shutdown_timeout)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`boot.host_shutdown_timeout`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | integer                                                               |
+-----------------------------------+-----------------------------------------------------------------------+
| **Default:**                      | []                                                          |
|                                   |                                                                       |
|                                   | [`30`]                         |
+-----------------------------------+-----------------------------------------------------------------------+
| **Live update:**                  | []                                                          |
|                                   |                                                                       |
|                                   | yes                                                                   |
+-----------------------------------+-----------------------------------------------------------------------+

Number of seconds to wait for the instance to shut down before it is force-stopped.

[[`boot.stop.priority`]][]

What order to shut down the instances in

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-boot:boot.stop.priority)]

+-----------------------------------+---------------------------------------------------------------+
| **Key:**                          | [`boot.stop.priority`] |
+-----------------------------------+---------------------------------------------------------------+
| **Type:**                         | []                                                  |
|                                   |                                                               |
|                                   | integer                                                       |
+-----------------------------------+---------------------------------------------------------------+
| **Default:**                      | []                                                  |
|                                   |                                                               |
|                                   | [`0`]                  |
+-----------------------------------+---------------------------------------------------------------+
| **Live update:**                  | []                                                  |
|                                   |                                                               |
|                                   | no                                                            |
+-----------------------------------+---------------------------------------------------------------+

The instance with the highest value is shut down first.

[]

## [`cloud-init`] configuration[¶](#cloud-init-configuration "Link to this heading")

The following instance options control the [[[`cloud-init`]]](../../cloud-init/#cloud-init) configuration of the instance:

[[`cloud-init.network-config`]][]

Network configuration for [`cloud-init`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:cloud-init.network-config)]

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Key:**                          | [`cloud-init.network-config`]                                                                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | string                                                                                                                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | [`DHCP`]` `[`on`]` `[`eth0`] |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | no                                                                                                                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | If supported by image                                                                                                                                                                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The content is used as seed value for [`cloud-init`].

[[`cloud-init.ssh-keys.KEYNAME`]][]

Additional SSH key to be injected on the instance by [`cloud-init`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:cloud-init.ssh-keys.KEYNAME)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`cloud-init.ssh-keys.KEYNAME`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | string                                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| **Live update:**                  | []                                                           |
|                                   |                                                                        |
|                                   | no                                                                     |
+-----------------------------------+------------------------------------------------------------------------+
| **Condition:**                    | []                                                           |
|                                   |                                                                        |
|                                   | If supported by image                                                  |
+-----------------------------------+------------------------------------------------------------------------+

Represents an additional SSH public key to be merged into existing [`cloud-init`] seed data and injected into an instance. Has the format [`:`], where  is a Linux username and  can be either a pure SSH public key or an import ID for a key hosted elsewhere. // For example: [`root:gh:githubUser`], [`myUser:ssh-keyAlg`]` `[`publicKeyHash`]

[[`cloud-init.user-data`]][]

User data for [`cloud-init`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:cloud-init.user-data)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`cloud-init.user-data`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Default:**                      | []                                                    |
|                                   |                                                                 |
|                                   | [`#cloud-config`]        |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | no                                                              |
+-----------------------------------+-----------------------------------------------------------------+
| **Condition:**                    | []                                                    |
|                                   |                                                                 |
|                                   | If supported by image                                           |
+-----------------------------------+-----------------------------------------------------------------+

The content is used as seed value for [`cloud-init`].

[[`cloud-init.vendor-data`]][]

Vendor data for [`cloud-init`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:cloud-init.vendor-data)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`cloud-init.vendor-data`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`#cloud-config`]          |
+-----------------------------------+-------------------------------------------------------------------+
| **Live update:**                  | []                                                      |
|                                   |                                                                   |
|                                   | no                                                                |
+-----------------------------------+-------------------------------------------------------------------+
| **Condition:**                    | []                                                      |
|                                   |                                                                   |
|                                   | If supported by image                                             |
+-----------------------------------+-------------------------------------------------------------------+

The content is used as seed value for [`cloud-init`].

[[`user.network-config`]][]

Legacy version of [`cloud-init.network-config`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:user.network-config)]

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Key:**                          | [`user.network-config`]                                                                                                                                                      |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | string                                                                                                                                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | [`DHCP`]` `[`on`]` `[`eth0`] |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | no                                                                                                                                                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                     |
|                                   | If supported by image                                                                                                                                                                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[`user.user-data`]][]

Legacy version of [`cloud-init.user-data`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:user.user-data)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`user.user-data`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | string                                                    |
+-----------------------------------+-----------------------------------------------------------+
| **Default:**                      | []                                              |
|                                   |                                                           |
|                                   | [`#cloud-config`]  |
+-----------------------------------+-----------------------------------------------------------+
| **Live update:**                  | []                                              |
|                                   |                                                           |
|                                   | no                                                        |
+-----------------------------------+-----------------------------------------------------------+
| **Condition:**                    | []                                              |
|                                   |                                                           |
|                                   | If supported by image                                     |
+-----------------------------------+-----------------------------------------------------------+

[[`user.vendor-data`]][]

Legacy version of [`cloud-init.vendor-data`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-cloud-init:user.vendor-data)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`user.vendor-data`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | string                                                      |
+-----------------------------------+-------------------------------------------------------------+
| **Default:**                      | []                                                |
|                                   |                                                             |
|                                   | [`#cloud-config`]    |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | no                                                          |
+-----------------------------------+-------------------------------------------------------------+
| **Condition:**                    | []                                                |
|                                   |                                                             |
|                                   | If supported by image                                       |
+-----------------------------------+-------------------------------------------------------------+

Support for these options depends on the image that is used and is not guaranteed.

If you specify both [`cloud-init.user-data`] and [`cloud-init.vendor-data`], the content of both options is merged. Therefore, make sure that the [`cloud-init`] configuration you specify in those options does not contain the same keys.

[]

## Resource limits[¶](#resource-limits "Link to this heading")

The following instance options specify resource limits for the instance:

[[`limits.cpu`]][]

Which CPUs to expose to the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.cpu)]

+-----------------------------------+-------------------------------------------------------+
| **Key:**                          | [`limits.cpu`] |
+-----------------------------------+-------------------------------------------------------+
| **Type:**                         | []                                          |
|                                   |                                                       |
|                                   | string                                                |
+-----------------------------------+-------------------------------------------------------+
| **Default:**                      | []                                          |
|                                   |                                                       |
|                                   | 1 (VMs)                                               |
+-----------------------------------+-------------------------------------------------------+
| **Live update:**                  | []                                          |
|                                   |                                                       |
|                                   | yes                                                   |
+-----------------------------------+-------------------------------------------------------+

A number or a specific range of CPUs to expose to the instance.

See [[CPU pinning]](#instance-options-limits-cpu) for more information.

[[`limits.cpu.allowance`]][]

How much of the CPU can be used

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.cpu.allowance)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`limits.cpu.allowance`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Default:**                      | []                                                    |
|                                   |                                                                 |
|                                   | 100%                                                            |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | yes                                                             |
+-----------------------------------+-----------------------------------------------------------------+
| **Condition:**                    | []                                                    |
|                                   |                                                                 |
|                                   | container                                                       |
+-----------------------------------+-----------------------------------------------------------------+

To control how much of the CPU can be used, specify either a percentage ([`50%`]) for a soft limit or a chunk of time ([`25ms/100ms`]) for a hard limit.

See [[Allowance and priority (container only)]](#instance-options-limits-cpu-container) for more information.

[[`limits.cpu.nodes`]][]

Which NUMA nodes to place the instance CPUs on

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.cpu.nodes)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`limits.cpu.nodes`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | string                                                      |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | yes                                                         |
+-----------------------------------+-------------------------------------------------------------+

A comma-separated list of NUMA node IDs or ranges to place the instance CPUs on.

See [[Allowance and priority (container only)]](#instance-options-limits-cpu-container) for more information.

[[`limits.cpu.pin_strategy`]][]

VM CPU auto pinning strategy

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.cpu.pin_strategy)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`limits.cpu.pin_strategy`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | string                                                             |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`none`]                    |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+
| **Condition:**                    | []                                                       |
|                                   |                                                                    |
|                                   | virtual machine                                                    |
+-----------------------------------+--------------------------------------------------------------------+

Specify the strategy for VM CPU auto pinning. Possible values: [`none`] (disables CPU auto pinning) and [`auto`] (enables CPU auto pinning).

See [[CPU limits for virtual machines]](#instance-options-limits-cpu-vm) for more information.

[[`limits.cpu.priority`]][]

CPU scheduling priority compared to other instances

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.cpu.priority)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`limits.cpu.priority`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | integer                                                        |
+-----------------------------------+----------------------------------------------------------------+
| **Default:**                      | []                                                   |
|                                   |                                                                |
|                                   | [`10`] (maximum)        |
+-----------------------------------+----------------------------------------------------------------+
| **Live update:**                  | []                                                   |
|                                   |                                                                |
|                                   | yes                                                            |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | container                                                      |
+-----------------------------------+----------------------------------------------------------------+

When overcommitting resources, specify the CPU scheduling priority compared to other instances that share the same CPUs. Specify an integer between 0 and 10.

See [[Allowance and priority (container only)]](#instance-options-limits-cpu-container) for more information.

[[`limits.disk.priority`]][]

Priority of the instance's I/O requests

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.disk.priority)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`limits.disk.priority`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | integer                                                         |
+-----------------------------------+-----------------------------------------------------------------+
| **Default:**                      | []                                                    |
|                                   |                                                                 |
|                                   | [`5`] (medium)           |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | yes                                                             |
+-----------------------------------+-----------------------------------------------------------------+

Controls how much priority to give to the instance's I/O requests when under load.

Specify an integer between 0 and 10.

[[`limits.hugepages.1GB`]][]

Limit for the number of 1 GB huge pages

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.hugepages.1GB)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`limits.hugepages.1GB`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | yes                                                             |
+-----------------------------------+-----------------------------------------------------------------+
| **Condition:**                    | []                                                    |
|                                   |                                                                 |
|                                   | container                                                       |
+-----------------------------------+-----------------------------------------------------------------+

Fixed value (in bytes) to limit the number of 1 GB huge pages. Various suffixes are supported (see [[Units for storage and network limits]](../instance_units/#instances-limit-units)).

See [[Huge page limits]](#instance-options-limits-hugepages) for more information.

[[`limits.hugepages.1MB`]][]

Limit for the number of 1 MB huge pages

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.hugepages.1MB)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`limits.hugepages.1MB`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | yes                                                             |
+-----------------------------------+-----------------------------------------------------------------+
| **Condition:**                    | []                                                    |
|                                   |                                                                 |
|                                   | container                                                       |
+-----------------------------------+-----------------------------------------------------------------+

Fixed value (in bytes) to limit the number of 1 MB huge pages. Various suffixes are supported (see [[Units for storage and network limits]](../instance_units/#instances-limit-units)).

See [[Huge page limits]](#instance-options-limits-hugepages) for more information.

[[`limits.hugepages.2MB`]][]

Limit for the number of 2 MB huge pages

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.hugepages.2MB)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`limits.hugepages.2MB`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | string                                                          |
+-----------------------------------+-----------------------------------------------------------------+
| **Live update:**                  | []                                                    |
|                                   |                                                                 |
|                                   | yes                                                             |
+-----------------------------------+-----------------------------------------------------------------+
| **Condition:**                    | []                                                    |
|                                   |                                                                 |
|                                   | container                                                       |
+-----------------------------------+-----------------------------------------------------------------+

Fixed value (in bytes) to limit the number of 2 MB huge pages. Various suffixes are supported (see [[Units for storage and network limits]](../instance_units/#instances-limit-units)).

See [[Huge page limits]](#instance-options-limits-hugepages) for more information.

[[`limits.hugepages.64KB`]][]

Limit for the number of 64 KB huge pages

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.hugepages.64KB)]

+-----------------------------------+------------------------------------------------------------------+
| **Key:**                          | [`limits.hugepages.64KB`] |
+-----------------------------------+------------------------------------------------------------------+
| **Type:**                         | []                                                     |
|                                   |                                                                  |
|                                   | string                                                           |
+-----------------------------------+------------------------------------------------------------------+
| **Live update:**                  | []                                                     |
|                                   |                                                                  |
|                                   | yes                                                              |
+-----------------------------------+------------------------------------------------------------------+
| **Condition:**                    | []                                                     |
|                                   |                                                                  |
|                                   | container                                                        |
+-----------------------------------+------------------------------------------------------------------+

Fixed value (in bytes) to limit the number of 64 KB huge pages. Various suffixes are supported (see [[Units for storage and network limits]](../instance_units/#instances-limit-units)).

See [[Huge page limits]](#instance-options-limits-hugepages) for more information.

[[`limits.memory`]][]

Usage limit for the host's memory

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.memory)]

+-----------------------------------+----------------------------------------------------------+
| **Key:**                          | [`limits.memory`] |
+-----------------------------------+----------------------------------------------------------+
| **Type:**                         | []                                             |
|                                   |                                                          |
|                                   | string                                                   |
+-----------------------------------+----------------------------------------------------------+
| **Default:**                      | []                                             |
|                                   |                                                          |
|                                   | [`1GiB`] (VMs)    |
+-----------------------------------+----------------------------------------------------------+
| **Live update:**                  | []                                             |
|                                   |                                                          |
|                                   | yes                                                      |
+-----------------------------------+----------------------------------------------------------+

Percentage of the host's memory or a fixed value in bytes. Various suffixes are supported.

See [[Units for storage and network limits]](../instance_units/#instances-limit-units) for details.

[[`limits.memory.enforce`]][]

Whether the memory limit is [`hard`] or [`soft`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.memory.enforce)]

+-----------------------------------+------------------------------------------------------------------+
| **Key:**                          | [`limits.memory.enforce`] |
+-----------------------------------+------------------------------------------------------------------+
| **Type:**                         | []                                                     |
|                                   |                                                                  |
|                                   | string                                                           |
+-----------------------------------+------------------------------------------------------------------+
| **Default:**                      | []                                                     |
|                                   |                                                                  |
|                                   | [`hard`]                  |
+-----------------------------------+------------------------------------------------------------------+
| **Live update:**                  | []                                                     |
|                                   |                                                                  |
|                                   | yes                                                              |
+-----------------------------------+------------------------------------------------------------------+
| **Condition:**                    | []                                                     |
|                                   |                                                                  |
|                                   | container                                                        |
+-----------------------------------+------------------------------------------------------------------+

If the instance's memory limit is [`hard`], the instance cannot exceed its limit. If it is [`soft`], the instance can exceed its memory limit when extra host memory is available.

[[`limits.memory.hugepages`]][]

Whether to back the instance using huge pages

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.memory.hugepages)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`limits.memory.hugepages`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | bool                                                               |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`false`]                   |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+
| **Condition:**                    | []                                                       |
|                                   |                                                                    |
|                                   | virtual machine                                                    |
+-----------------------------------+--------------------------------------------------------------------+

If this option is set to [`false`], regular system memory is used.

[[`limits.memory.swap`]][]

Whether to encourage/discourage swapping less used pages for this instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.memory.swap)]

+-----------------------------------+---------------------------------------------------------------+
| **Key:**                          | [`limits.memory.swap`] |
+-----------------------------------+---------------------------------------------------------------+
| **Type:**                         | []                                                  |
|                                   |                                                               |
|                                   | bool                                                          |
+-----------------------------------+---------------------------------------------------------------+
| **Default:**                      | []                                                  |
|                                   |                                                               |
|                                   | [`true`]               |
+-----------------------------------+---------------------------------------------------------------+
| **Live update:**                  | []                                                  |
|                                   |                                                               |
|                                   | yes                                                           |
+-----------------------------------+---------------------------------------------------------------+
| **Condition:**                    | []                                                  |
|                                   |                                                               |
|                                   | container                                                     |
+-----------------------------------+---------------------------------------------------------------+

[[`limits.memory.swap.priority`]][]

Prevents the instance from being swapped to disk

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.memory.swap.priority)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`limits.memory.swap.priority`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | integer                                                                |
+-----------------------------------+------------------------------------------------------------------------+
| **Default:**                      | []                                                           |
|                                   |                                                                        |
|                                   | [`10`] (maximum)                |
+-----------------------------------+------------------------------------------------------------------------+
| **Live update:**                  | []                                                           |
|                                   |                                                                        |
|                                   | yes                                                                    |
+-----------------------------------+------------------------------------------------------------------------+
| **Condition:**                    | []                                                           |
|                                   |                                                                        |
|                                   | container                                                              |
+-----------------------------------+------------------------------------------------------------------------+

Specify an integer between 0 and 10. The higher the value, the less likely the instance is to be swapped to disk.

[[`limits.processes`]][]

Maximum number of processes that can run in the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.processes)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`limits.processes`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | integer                                                     |
+-----------------------------------+-------------------------------------------------------------+
| **Default:**                      | []                                                |
|                                   |                                                             |
|                                   | empty                                                       |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | yes                                                         |
+-----------------------------------+-------------------------------------------------------------+
| **Condition:**                    | []                                                |
|                                   |                                                             |
|                                   | container                                                   |
+-----------------------------------+-------------------------------------------------------------+

If left empty, no limit is set.

[[`limits.kernel.*`]][]

Kernel resources per instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-resource-limits:limits.kernel.*)]

+-----------------------------------+------------------------------------------------------------+
| **Key:**                          | [`limits.kernel.*`] |
+-----------------------------------+------------------------------------------------------------+
| **Type:**                         | []                                               |
|                                   |                                                            |
|                                   | string                                                     |
+-----------------------------------+------------------------------------------------------------+
| **Live update:**                  | []                                               |
|                                   |                                                            |
|                                   | no                                                         |
+-----------------------------------+------------------------------------------------------------+
| **Condition:**                    | []                                               |
|                                   |                                                            |
|                                   | container                                                  |
+-----------------------------------+------------------------------------------------------------+

You can set kernel limits on an instance, for example, you can limit the number of open files. See [[Kernel resource limits]](#instance-options-limits-kernel) for more information.

### CPU limits[¶](#cpu-limits "Link to this heading")

You have different options to limit CPU usage:

-   Set [[`limits.cpu`]](#instance-resource-limits:limits.cpu) to restrict which CPUs the instance can see and use. See [[CPU pinning]](#instance-options-limits-cpu) for how to set this option.

-   Set [[`limits.cpu.allowance`]](#instance-resource-limits:limits.cpu.allowance) to restrict the load an instance can put on the available CPUs. This option is available only for containers. See [[Allowance and priority (container only)]](#instance-options-limits-cpu-container) for how to set this option.

-   Set [[`limits.cpu.pin_strategy`]](#instance-resource-limits:limits.cpu.pin_strategy) to specify the strategy for virtual-machine CPU auto pinning. This option is available only for virtual machines. See [[CPU limits for virtual machines]](#instance-options-limits-cpu-vm) for how to set this option.

It is possible to set both options at the same time to restrict both which CPUs are visible to the instance and the allowed usage of those instances. However, if you use [[`limits.cpu.allowance`]](#instance-resource-limits:limits.cpu.allowance) with a time limit, you should avoid using [[`limits.cpu`]](#instance-resource-limits:limits.cpu) in addition, because that puts a lot of constraints on the scheduler and might lead to less efficient allocations.

The CPU limits are implemented through a mix of the [`cpuset`] and [`cpu`] cgroup controllers.

[]

#### CPU pinning[¶](#cpu-pinning "Link to this heading")

[[`limits.cpu`]](#instance-resource-limits:limits.cpu) results in CPU pinning through the [`cpuset`] controller. You can specify either which CPUs or how many CPUs are visible and available to the instance:

-   To specify which CPUs to use, set [`limits.cpu`] to either a set of CPUs (for example, [`1,2,3`]) or a CPU range (for example, [`0-3`]).

    To pin to a single CPU, use the range syntax (for example, [`1-1`]) to differentiate it from a number of CPUs.

-   If you specify a number (for example, [`4`]) of CPUs, LXD will do dynamic load-balancing of all instances that aren't pinned to specific CPUs, trying to spread the load on the machine. Instances are re-balanced every time an instance starts or stops, as well as whenever a CPU is added to the system.

[]

##### CPU limits for virtual machines[¶](#cpu-limits-for-virtual-machines "Link to this heading")

Note

LXD supports live-updating the [[`limits.cpu`]](#instance-resource-limits:limits.cpu) option. However, for virtual machines, this only means that the respective CPUs are hotplugged. Depending on the guest operating system, you might need to either restart the instance or complete some manual actions to bring the new CPUs online.

LXD virtual machines default to having just one vCPU allocated, which shows up as matching the host CPU vendor and type, but has a single core and no threads.

When [[`limits.cpu`]](#instance-resource-limits:limits.cpu) is set to a single integer, LXD allocates multiple vCPUs and exposes them to the guest as full cores. Unless [[`limits.cpu.pin_strategy`]](#instance-resource-limits:limits.cpu.pin_strategy) is set to [`auto`], those vCPUs are not pinned to specific cores on the host. The number of vCPUs can be updated while the VM is running.

When [[`limits.cpu`]](#instance-resource-limits:limits.cpu) is set to a range or comma-separated list of CPU IDs (as provided by [[[`lxc`]` `[`info`]` `[`--resources`]]](../manpages/lxc/info/#lxc-info-md)), the vCPUs are pinned to those cores. In this scenario, LXD checks whether the CPU configuration lines up with a realistic hardware topology and if it does, it replicates that topology in the guest. When doing CPU pinning, it is not possible to change the configuration while the VM is running.

For example, if the pinning configuration includes eight threads, with each pair of thread coming from the same core and an even number of cores spread across two CPUs, the guest will show two CPUs, each with two cores and each core with two threads. The NUMA layout is similarly replicated and in this scenario, the guest would most likely end up with two NUMA nodes, one for each CPU socket.

In such an environment with multiple NUMA nodes, the memory is similarly divided across NUMA nodes and be pinned accordingly on the host and then exposed to the guest.

All this allows for very high performance operations in the guest as the guest scheduler can properly reason about sockets, cores and threads as well as consider NUMA topology when sharing memory or moving processes across NUMA nodes.

[]

#### Allowance and priority (container only)[¶](#allowance-and-priority-container-only "Link to this heading")

[[`limits.cpu.allowance`]](#instance-resource-limits:limits.cpu.allowance) drives either the CFS scheduler quotas when passed a time constraint, or the generic CPU shares mechanism when passed a percentage value:

-   The time constraint (for example, [`20ms/50ms`]) is a hard limit. For example, if you want to allow the container to use a maximum of one CPU, set [[`limits.cpu.allowance`]](#instance-resource-limits:limits.cpu.allowance) to a value like [`100ms/100ms`]. The value is relative to one CPU worth of time, so to restrict to two CPUs worth of time, use something like [`100ms/50ms`] or [`200ms/100ms`].

-   When using a percentage value, the limit is a soft limit that is applied only when under load. It is used to calculate the scheduler priority for the instance, relative to any other instance that is using the same CPU or CPUs. For example, to limit the CPU usage of the container to one CPU when under load, set [[`limits.cpu.allowance`]](#instance-resource-limits:limits.cpu.allowance) to [`100%`].

[[`limits.cpu.nodes`]](#instance-resource-limits:limits.cpu.nodes) can be used to restrict the CPUs that the instance can use to a specific set of NUMA nodes. To specify which NUMA nodes to use, set [[`limits.cpu.nodes`]](#instance-resource-limits:limits.cpu.nodes) to either a set of NUMA node IDs (for example, [`0,1`]) or a set of NUMA node ranges (for example, [`0-1,2-4`]).

[[`limits.cpu.priority`]](#instance-resource-limits:limits.cpu.priority) is another factor that is used to compute the scheduler priority score when a number of instances sharing a set of CPUs have the same percentage of CPU assigned to them.

[]

### Huge page limits[¶](#huge-page-limits "Link to this heading")

LXD allows to limit the number of huge pages available to a container through the [`limits.hugepage.[size]`] key (for example, [[`limits.hugepages.1MB`]](#instance-resource-limits:limits.hugepages.1MB)).

Architectures often expose multiple huge-page sizes. The available huge-page sizes depend on the architecture.

Setting limits for huge pages is especially useful when LXD is configured to intercept the [`mount`] syscall for the [`hugetlbfs`] file system in unprivileged containers. When LXD intercepts a [`hugetlbfs`] [`mount`] syscall, it mounts the [`hugetlbfs`] file system for a container with correct [`uid`] and [`gid`] values as mount options. This makes it possible to use huge pages from unprivileged containers. However, it is recommended to limit the number of huge pages available to the container through [`limits.hugepages.[size]`] to stop the container from being able to exhaust the huge pages available to the host.

Limiting huge pages is done through the [`hugetlb`] cgroup controller, which means that the host system must expose the [`hugetlb`] controller in the legacy or unified cgroup hierarchy for these limits to apply.

[]

### Kernel resource limits[¶](#kernel-resource-limits "Link to this heading")

For container instances, LXD exposes a generic namespaced key [[`limits.kernel.*`]](#instance-resource-limits:limits.kernel.*) that can be used to set resource limits.

It is generic in the sense that LXD does not perform any validation on the resource that is specified following the [`limits.kernel.*`] prefix. LXD cannot know about all the possible resources that a given kernel supports. Instead, LXD simply passes down the corresponding resource key after the [`limits.kernel.*`] prefix and its value to the kernel. The kernel does the appropriate validation. This allows users to specify any supported limit on their system.

Some common limits are:

  Key                                                                   Resource                                                       Description
  --------------------------------------------------------------------- -------------------------------------------------------------- -------------------------------------------------------------------------------------
  [`limits.kernel.as`]           [`RLIMIT_AS`]           Maximum size of the process's virtual memory
  [`limits.kernel.core`]         [`RLIMIT_CORE`]         Maximum size of the process's core dump file
  [`limits.kernel.cpu`]          [`RLIMIT_CPU`]          Limit in seconds on the amount of CPU time the process can consume
  [`limits.kernel.data`]         [`RLIMIT_DATA`]         Maximum size of the process's data segment
  [`limits.kernel.fsize`]        [`RLIMIT_FSIZE`]        Maximum size of files the process may create
  [`limits.kernel.locks`]        [`RLIMIT_LOCKS`]        Limit on the number of file locks that this process may establish
  [`limits.kernel.memlock`]      [`RLIMIT_MEMLOCK`]      Limit on the number of bytes of memory that the process may lock in RAM
  [`limits.kernel.nice`]         [`RLIMIT_NICE`]         Maximum value to which the process's nice value can be raised
  [`limits.kernel.nofile`]       [`RLIMIT_NOFILE`]       Maximum number of open files for the process
  [`limits.kernel.nproc`]        [`RLIMIT_NPROC`]        Maximum number of processes that can be created for the user of the calling process
  [`limits.kernel.rtprio`]       [`RLIMIT_RTPRIO`]       Maximum value on the real-time-priority that may be set for this process
  [`limits.kernel.sigpending`]   [`RLIMIT_SIGPENDING`]   Maximum number of signals that may be queued for the user of the calling process

A full list of all available limits can be found in the manpages for the [`getrlimit(2)`]/[`setrlimit(2)`] system calls.

To specify a limit within the [`limits.kernel.*`] namespace, use the resource name in lowercase without the [`RLIMIT_`] prefix. For example, [`RLIMIT_NOFILE`] should be specified as [`nofile`].

A limit is specified as two colon-separated values that are either numeric or the word [`unlimited`] (for example, [`limits.kernel.nofile=1000:2000`]). A single value can be used as a shortcut to set both soft and hard limit to the same value (for example, [`limits.kernel.nofile=3000`]).

A resource with no explicitly configured limit will inherit its limit from the process that starts up the container. Note that this inheritance is not enforced by LXD but by the kernel.

[]

## Migration options[¶](#migration-options "Link to this heading")

The following instance options control the behavior if the instance is [[moved from one LXD server to another]](../../howto/instances_migrate/#howto-instances-migrate):

[[`migration.incremental.memory`]][]

Whether to use incremental memory transfer

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-migration:migration.incremental.memory)]

+-----------------------------------+-------------------------------------------------------------------------+
| **Key:**                          | [`migration.incremental.memory`] |
+-----------------------------------+-------------------------------------------------------------------------+
| **Type:**                         | []                                                            |
|                                   |                                                                         |
|                                   | bool                                                                    |
+-----------------------------------+-------------------------------------------------------------------------+
| **Default:**                      | []                                                            |
|                                   |                                                                         |
|                                   | [`false`]                        |
+-----------------------------------+-------------------------------------------------------------------------+
| **Live update:**                  | []                                                            |
|                                   |                                                                         |
|                                   | yes                                                                     |
+-----------------------------------+-------------------------------------------------------------------------+
| **Condition:**                    | []                                                            |
|                                   |                                                                         |
|                                   | container                                                               |
+-----------------------------------+-------------------------------------------------------------------------+

Using incremental memory transfer of the instance's memory can reduce downtime.

[[`migration.incremental.memory.goal`]][]

Percentage of memory to have in sync before stopping the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-migration:migration.incremental.memory.goal)]

+-----------------------------------+------------------------------------------------------------------------------+
| **Key:**                          | [`migration.incremental.memory.goal`] |
+-----------------------------------+------------------------------------------------------------------------------+
| **Type:**                         | []                                                                 |
|                                   |                                                                              |
|                                   | integer                                                                      |
+-----------------------------------+------------------------------------------------------------------------------+
| **Default:**                      | []                                                                 |
|                                   |                                                                              |
|                                   | [`70`]                                |
+-----------------------------------+------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                 |
|                                   |                                                                              |
|                                   | yes                                                                          |
+-----------------------------------+------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                 |
|                                   |                                                                              |
|                                   | container                                                                    |
+-----------------------------------+------------------------------------------------------------------------------+

[[`migration.incremental.memory.iterations`]][]

Maximum number of transfer operations to go through before stopping the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-migration:migration.incremental.memory.iterations)]

+-----------------------------------+------------------------------------------------------------------------------------+
| **Key:**                          | [`migration.incremental.memory.iterations`] |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                       |
|                                   |                                                                                    |
|                                   | integer                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                       |
|                                   |                                                                                    |
|                                   | [`10`]                                      |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                       |
|                                   |                                                                                    |
|                                   | yes                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                       |
|                                   |                                                                                    |
|                                   | container                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------+

[[`migration.stateful`]][]

Whether to allow for stateful stop/start and snapshots

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-migration:migration.stateful)]

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Key:**                          | [`migration.stateful`]                                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                                                                                                |
|                                   |                                                                                                                                                             |
|                                   | bool                                                                                                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                                                                                                |
|                                   |                                                                                                                                                             |
|                                   | [`false`] or value from profiles or [`instances.migration.stateful`] (if set) |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                                                                                                |
|                                   |                                                                                                                                                             |
|                                   | no                                                                                                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                                                                                                |
|                                   |                                                                                                                                                             |
|                                   | virtual machine                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enabling this option prevents the use of some features that are incompatible with it.

[]

## Placement options[¶](#placement-options "Link to this heading")

The following instance option controls the placement of instances in a cluster:

[[`placement.group`]][]

Placement group controlling instance scheduling

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-placement:placement.group)]

+-----------------------------------+------------------------------------------------------------+
| **Key:**                          | [`placement.group`] |
+-----------------------------------+------------------------------------------------------------+
| **Type:**                         | []                                               |
|                                   |                                                            |
|                                   | string                                                     |
+-----------------------------------+------------------------------------------------------------+
| **Live update:**                  | []                                               |
|                                   |                                                            |
|                                   | yes                                                        |
+-----------------------------------+------------------------------------------------------------+

Specifies the placement group that determines where this instance is scheduled within the cluster. The placement group defines the placement policy (e.g. spread or compact) and rigor (e.g. strict or permissive) used to determine eligible cluster members during LXD scheduling events.

See [[How to use placement groups]](../../howto/cluster_placement_groups/#cluster-placement-groups) for more information about placement groups.

[]

## NVIDIA and CUDA configuration[¶](#nvidia-and-cuda-configuration "Link to this heading")

The following instance options specify the NVIDIA and CUDA configuration of the instance:

[[`nvidia.driver.capabilities`]][]

What driver capabilities the instance needs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-nvidia:nvidia.driver.capabilities)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`nvidia.driver.capabilities`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | string                                                                |
+-----------------------------------+-----------------------------------------------------------------------+
| **Default:**                      | []                                                          |
|                                   |                                                                       |
|                                   | [`compute,utility`]            |
+-----------------------------------+-----------------------------------------------------------------------+
| **Live update:**                  | []                                                          |
|                                   |                                                                       |
|                                   | no                                                                    |
+-----------------------------------+-----------------------------------------------------------------------+
| **Condition:**                    | []                                                          |
|                                   |                                                                       |
|                                   | container                                                             |
+-----------------------------------+-----------------------------------------------------------------------+

The specified driver capabilities are used to set [`libnvidia-container`]` `[`NVIDIA_DRIVER_CAPABILITIES`].

[[`nvidia.require.cuda`]][]

Required CUDA version

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-nvidia:nvidia.require.cuda)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`nvidia.require.cuda`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | string                                                         |
+-----------------------------------+----------------------------------------------------------------+
| **Live update:**                  | []                                                   |
|                                   |                                                                |
|                                   | no                                                             |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | container                                                      |
+-----------------------------------+----------------------------------------------------------------+

The specified version expression is used to set [`libnvidia-container`]` `[`NVIDIA_REQUIRE_CUDA`].

[[`nvidia.require.driver`]][]

Required driver version

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-nvidia:nvidia.require.driver)]

+-----------------------------------+------------------------------------------------------------------+
| **Key:**                          | [`nvidia.require.driver`] |
+-----------------------------------+------------------------------------------------------------------+
| **Type:**                         | []                                                     |
|                                   |                                                                  |
|                                   | string                                                           |
+-----------------------------------+------------------------------------------------------------------+
| **Live update:**                  | []                                                     |
|                                   |                                                                  |
|                                   | no                                                               |
+-----------------------------------+------------------------------------------------------------------+
| **Condition:**                    | []                                                     |
|                                   |                                                                  |
|                                   | container                                                        |
+-----------------------------------+------------------------------------------------------------------+

The specified version expression is used to set [`libnvidia-container`]` `[`NVIDIA_REQUIRE_DRIVER`].

[[`nvidia.runtime`]][]

Whether to pass the host NVIDIA and CUDA runtime libraries into the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-nvidia:nvidia.runtime)]

+-----------------------------------+-----------------------------------------------------------+
| **Key:**                          | [`nvidia.runtime`] |
+-----------------------------------+-----------------------------------------------------------+
| **Type:**                         | []                                              |
|                                   |                                                           |
|                                   | bool                                                      |
+-----------------------------------+-----------------------------------------------------------+
| **Default:**                      | []                                              |
|                                   |                                                           |
|                                   | [`false`]          |
+-----------------------------------+-----------------------------------------------------------+
| **Live update:**                  | []                                              |
|                                   |                                                           |
|                                   | no                                                        |
+-----------------------------------+-----------------------------------------------------------+
| **Condition:**                    | []                                              |
|                                   |                                                           |
|                                   | container                                                 |
+-----------------------------------+-----------------------------------------------------------+

[]

## Raw instance configuration overrides[¶](#raw-instance-configuration-overrides "Link to this heading")

The following instance options allow direct interaction with the backend features that LXD itself uses:

[[`raw.apparmor`]][]

AppArmor profile entries

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-raw:raw.apparmor)]

+-----------------------------------+---------------------------------------------------------+
| **Key:**                          | [`raw.apparmor`] |
+-----------------------------------+---------------------------------------------------------+
| **Type:**                         | []                                            |
|                                   |                                                         |
|                                   | blob                                                    |
+-----------------------------------+---------------------------------------------------------+
| **Live update:**                  | []                                            |
|                                   |                                                         |
|                                   | yes                                                     |
+-----------------------------------+---------------------------------------------------------+

The specified entries are appended to the generated profile.

[[`raw.idmap`]][]

Raw idmap configuration

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-raw:raw.idmap)]

+-----------------------------------+------------------------------------------------------+
| **Key:**                          | [`raw.idmap`] |
+-----------------------------------+------------------------------------------------------+
| **Type:**                         | []                                         |
|                                   |                                                      |
|                                   | blob                                                 |
+-----------------------------------+------------------------------------------------------+
| **Live update:**                  | []                                         |
|                                   |                                                      |
|                                   | no                                                   |
+-----------------------------------+------------------------------------------------------+

For example: [`both`]` `[`1000`]` `[`1000`]

[[`raw.lxc`]][]

Raw LXC configuration to be appended to the generated one

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-raw:raw.lxc)]

+-----------------------------------+----------------------------------------------------+
| **Key:**                          | [`raw.lxc`] |
+-----------------------------------+----------------------------------------------------+
| **Type:**                         | []                                       |
|                                   |                                                    |
|                                   | blob                                               |
+-----------------------------------+----------------------------------------------------+
| **Live update:**                  | []                                       |
|                                   |                                                    |
|                                   | no                                                 |
+-----------------------------------+----------------------------------------------------+
| **Condition:**                    | []                                       |
|                                   |                                                    |
|                                   | container                                          |
+-----------------------------------+----------------------------------------------------+

[[`raw.qemu`]][]

Raw QEMU configuration to be appended to the generated command line

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-raw:raw.qemu)]

+-----------------------------------+-----------------------------------------------------+
| **Key:**                          | [`raw.qemu`] |
+-----------------------------------+-----------------------------------------------------+
| **Type:**                         | []                                        |
|                                   |                                                     |
|                                   | blob                                                |
+-----------------------------------+-----------------------------------------------------+
| **Live update:**                  | []                                        |
|                                   |                                                     |
|                                   | no                                                  |
+-----------------------------------+-----------------------------------------------------+
| **Condition:**                    | []                                        |
|                                   |                                                     |
|                                   | virtual machine                                     |
+-----------------------------------+-----------------------------------------------------+

[[`raw.qemu.conf`]][]

Addition/override to the generated [`qemu.conf`] file

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-raw:raw.qemu.conf)]

+-----------------------------------+----------------------------------------------------------+
| **Key:**                          | [`raw.qemu.conf`] |
+-----------------------------------+----------------------------------------------------------+
| **Type:**                         | []                                             |
|                                   |                                                          |
|                                   | blob                                                     |
+-----------------------------------+----------------------------------------------------------+
| **Live update:**                  | []                                             |
|                                   |                                                          |
|                                   | no                                                       |
+-----------------------------------+----------------------------------------------------------+
| **Condition:**                    | []                                             |
|                                   |                                                          |
|                                   | virtual machine                                          |
+-----------------------------------+----------------------------------------------------------+

See [[Override QEMU configuration]](#instance-options-qemu) for more information.

[[`raw.seccomp`]][]

Raw Seccomp configuration

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-raw:raw.seccomp)]

+-----------------------------------+--------------------------------------------------------+
| **Key:**                          | [`raw.seccomp`] |
+-----------------------------------+--------------------------------------------------------+
| **Type:**                         | []                                           |
|                                   |                                                        |
|                                   | blob                                                   |
+-----------------------------------+--------------------------------------------------------+
| **Live update:**                  | []                                           |
|                                   |                                                        |
|                                   | no                                                     |
+-----------------------------------+--------------------------------------------------------+
| **Condition:**                    | []                                           |
|                                   |                                                        |
|                                   | container                                              |
+-----------------------------------+--------------------------------------------------------+

Important

Setting these [`raw.*`] keys might break LXD in non-obvious ways. Therefore, you should avoid setting any of these keys.

[]

### Override QEMU configuration[¶](#override-qemu-configuration "Link to this heading")

For VM instances, LXD configures QEMU through a configuration file that is passed to QEMU with the [`-readconfig`] command-line option. This configuration file is generated for each instance before boot. It can be found at [`/var/log/lxd/<instance_name>/qemu.conf`].

The default configuration works fine for LXD's most common use case: modern UEFI guests with VirtIO devices. In some situations, however, you might need to override the generated configuration. For example:

-   To run an old guest OS that doesn't support UEFI.

-   To specify custom virtual devices when VirtIO is not supported by the guest OS.

-   To add devices that are not supported by LXD before the machines boots.

-   To remove devices that conflict with the guest OS.

To override the configuration, set the [[`raw.qemu.conf`]](#instance-raw:raw.qemu.conf) option. It supports a format similar to [`qemu.conf`], with some additions. Since it is a multi-line configuration option, you can use it to modify multiple sections or keys.

-   To replace a section or key in the generated configuration file, add a section with a different value.

    For example, use the following section to override the default [`virtio-gpu-pci`] GPU driver:

    ::: 
    ::: highlight
        raw.qemu.conf: |-
            [device "qemu_gpu"]
            driver = "qxl-vga"
    :::
    :::

-   To remove a section, specify a section without any keys. For example:

    ::: 
    ::: highlight
        raw.qemu.conf: |-
            [device "qemu_gpu"]
    :::
    :::

-   To remove a key, specify an empty string as the value. For example:

    ::: 
    ::: highlight
        raw.qemu.conf: |-
            [device "qemu_gpu"]
            driver = ""
    :::
    :::

-   To add a new section, specify a section name that is not present in the configuration file.

The configuration file format used by QEMU allows multiple sections with the same name. Here's a piece of the configuration generated by LXD:

    [global]
    driver = "ICH9-LPC"
    property = "disable_s3"
    value = "1"

    [global]
    driver = "ICH9-LPC"
    property = "disable_s4"
    value = "1"

To specify which section to override, specify an index. For example:

    raw.qemu.conf: |-
        [global][1]
        value = "0"

Section indexes start at 0 (which is the default value when not specified), so the above example would generate the following configuration:

    [global]
    driver = "ICH9-LPC"
    property = "disable_s3"
    value = "1"

    [global]
    driver = "ICH9-LPC"
    property = "disable_s4"
    value = "0"

[]

## Security policies[¶](#security-policies "Link to this heading")

The following instance options control the [[Security]](../../explanation/security/#security) policies of the instance:

[[`security.agent.metrics`]][]

Whether the [`lxd-agent`] is queried for state information and metrics

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.agent.metrics)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`security.agent.metrics`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | bool                                                              |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`true`]                   |
+-----------------------------------+-------------------------------------------------------------------+
| **Live update:**                  | []                                                      |
|                                   |                                                                   |
|                                   | no                                                                |
+-----------------------------------+-------------------------------------------------------------------+
| **Condition:**                    | []                                                      |
|                                   |                                                                   |
|                                   | virtual machine                                                   |
+-----------------------------------+-------------------------------------------------------------------+

[[`security.csm`]][]

Whether to use a firmware that supports UEFI-incompatible operating systems

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.csm)]

+-----------------------------------+---------------------------------------------------------+
| **Key:**                          | [`security.csm`] |
+-----------------------------------+---------------------------------------------------------+
| **Type:**                         | []                                            |
|                                   |                                                         |
|                                   | bool                                                    |
+-----------------------------------+---------------------------------------------------------+
| **Default:**                      | []                                            |
|                                   |                                                         |
|                                   | [`false`]        |
+-----------------------------------+---------------------------------------------------------+
| **Live update:**                  | []                                            |
|                                   |                                                         |
|                                   | no                                                      |
+-----------------------------------+---------------------------------------------------------+
| **Condition:**                    | []                                            |
|                                   |                                                         |
|                                   | virtual machine                                         |
+-----------------------------------+---------------------------------------------------------+

When enabling this option, set [[`security.secureboot`]](#instance-security:security.secureboot) to [`false`].

[[`security.delegate_bpf`]][]

Whether to enable eBPF delegation using BPF Token mechanism

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.delegate_bpf)]

+-----------------------------------+------------------------------------------------------------------+
| **Key:**                          | [`security.delegate_bpf`] |
+-----------------------------------+------------------------------------------------------------------+
| **Type:**                         | []                                                     |
|                                   |                                                                  |
|                                   | bool                                                             |
+-----------------------------------+------------------------------------------------------------------+
| **Default:**                      | []                                                     |
|                                   |                                                                  |
|                                   | [`false`]                 |
+-----------------------------------+------------------------------------------------------------------+
| **Live update:**                  | []                                                     |
|                                   |                                                                  |
|                                   | no                                                               |
+-----------------------------------+------------------------------------------------------------------+
| **Condition:**                    | []                                                     |
|                                   |                                                                  |
|                                   | unprivileged container                                           |
+-----------------------------------+------------------------------------------------------------------+

This option enables BPF functionality delegation mechanism (using BPF Token).

Note: [`security.delegate_bpf.cmd_types`], [`security.delegate_bpf.map_types`], [`security.delegate_bpf.prog_types`], [`security.delegate_bpf.attach_types`] need to be configured depending on BPF workload in the container.

See [[Privilege delegation using BPF Token]](../../explanation/bpf/#bpf-delegation-token) for more information.

[[`security.delegate_bpf.attach_types`]][]

Which eBPF attach types to allow with delegation mechanism

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.delegate_bpf.attach_types)]

+-----------------------------------+-------------------------------------------------------------------------------+
| **Key:**                          | [`security.delegate_bpf.attach_types`] |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Type:**                         | []                                                                  |
|                                   |                                                                               |
|                                   | bool                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Default:**                      | []                                                                  |
|                                   |                                                                               |
|                                   | [`false`]                              |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                  |
|                                   |                                                                               |
|                                   | no                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                  |
|                                   |                                                                               |
|                                   | unprivileged container                                                        |
+-----------------------------------+-------------------------------------------------------------------------------+

Which eBPF program attachment types to allow with delegation mechanism. Syntax follows a kernel one for [`delegate_attachs`] bpffs mount option. A number (bitmask) or [`:`]-separated list of attachment types to allow can be specified. For example, [`cgroup_inet_ingress`] allows [`BPF_CGROUP_INET_INGRESS`] attachment type.

[[`security.delegate_bpf.cmd_types`]][]

Which eBPF commands to allow with delegation mechanism

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.delegate_bpf.cmd_types)]

+-----------------------------------+----------------------------------------------------------------------------+
| **Key:**                          | [`security.delegate_bpf.cmd_types`] |
+-----------------------------------+----------------------------------------------------------------------------+
| **Type:**                         | []                                                               |
|                                   |                                                                            |
|                                   | bool                                                                       |
+-----------------------------------+----------------------------------------------------------------------------+
| **Default:**                      | []                                                               |
|                                   |                                                                            |
|                                   | [`false`]                           |
+-----------------------------------+----------------------------------------------------------------------------+
| **Live update:**                  | []                                                               |
|                                   |                                                                            |
|                                   | no                                                                         |
+-----------------------------------+----------------------------------------------------------------------------+
| **Condition:**                    | []                                                               |
|                                   |                                                                            |
|                                   | unprivileged container                                                     |
+-----------------------------------+----------------------------------------------------------------------------+

Which eBPF commands to allow with delegation mechanism. Syntax follows a kernel one for [`delegate_cmds`] bpffs mount option. A number (bitmask) or [`:`]-separated list of commands to allow can be specified. For example, [`prog_load:map_create`] allows eBPF programs loading and eBPF maps creation. Notice: [`security.delegate_bpf.prog_types`] and [`security.delegate_bpf.map_types`] still need to be configured accordingly.

[[`security.delegate_bpf.map_types`]][]

Which eBPF maps to allow with delegation mechanism

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.delegate_bpf.map_types)]

+-----------------------------------+----------------------------------------------------------------------------+
| **Key:**                          | [`security.delegate_bpf.map_types`] |
+-----------------------------------+----------------------------------------------------------------------------+
| **Type:**                         | []                                                               |
|                                   |                                                                            |
|                                   | bool                                                                       |
+-----------------------------------+----------------------------------------------------------------------------+
| **Default:**                      | []                                                               |
|                                   |                                                                            |
|                                   | [`false`]                           |
+-----------------------------------+----------------------------------------------------------------------------+
| **Live update:**                  | []                                                               |
|                                   |                                                                            |
|                                   | no                                                                         |
+-----------------------------------+----------------------------------------------------------------------------+
| **Condition:**                    | []                                                               |
|                                   |                                                                            |
|                                   | unprivileged container                                                     |
+-----------------------------------+----------------------------------------------------------------------------+

Which eBPF maps to allow with delegation mechanism. Syntax follows a kernel one for [`delegate_maps`] bpffs mount option. A number (bitmask) or [`:`]-separated list of map types to allow can be specified. For example, [`ringbuf`] allows [`BPF_MAP_TYPE_RINGBUF`] map.

[[`security.delegate_bpf.prog_types`]][]

Which eBPF program types to allow with delegation mechanism

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.delegate_bpf.prog_types)]

+-----------------------------------+-----------------------------------------------------------------------------+
| **Key:**                          | [`security.delegate_bpf.prog_types`] |
+-----------------------------------+-----------------------------------------------------------------------------+
| **Type:**                         | []                                                                |
|                                   |                                                                             |
|                                   | bool                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------+
| **Default:**                      | []                                                                |
|                                   |                                                                             |
|                                   | [`false`]                            |
+-----------------------------------+-----------------------------------------------------------------------------+
| **Live update:**                  | []                                                                |
|                                   |                                                                             |
|                                   | no                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------+
| **Condition:**                    | []                                                                |
|                                   |                                                                             |
|                                   | unprivileged container                                                      |
+-----------------------------------+-----------------------------------------------------------------------------+

Which eBPF program types to allow with delegation mechanism. Syntax follows a kernel one for [`delegate_progs`] bpffs mount option. A number (bitmask) or [`:`]-separated list of program types to allow can be specified. For example, [`socket_filter`] allows [`BPF_PROG_TYPE_SOCKET_FILTER`] program type.

[[`security.devlxd`]][]

Whether [`/dev/lxd`] is present in the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.devlxd)]

+-----------------------------------+------------------------------------------------------------+
| **Key:**                          | [`security.devlxd`] |
+-----------------------------------+------------------------------------------------------------+
| **Type:**                         | []                                               |
|                                   |                                                            |
|                                   | bool                                                       |
+-----------------------------------+------------------------------------------------------------+
| **Default:**                      | []                                               |
|                                   |                                                            |
|                                   | [`true`]            |
+-----------------------------------+------------------------------------------------------------+
| **Live update:**                  | []                                               |
|                                   |                                                            |
|                                   | no                                                         |
+-----------------------------------+------------------------------------------------------------+

See [[Communication between instance and host]](../../dev-lxd/#dev-lxd) for more information.

[[`security.devlxd.images`]][]

Controls the availability of the [`/1.0/images`] API over [`devlxd`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.devlxd.images)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`security.devlxd.images`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | bool                                                              |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`false`]                  |
+-----------------------------------+-------------------------------------------------------------------+
| **Live update:**                  | []                                                      |
|                                   |                                                                   |
|                                   | yes                                                               |
+-----------------------------------+-------------------------------------------------------------------+

[[`security.devlxd.management.volumes`]][]

Controls the availability of the volume management API over [`devlxd`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.devlxd.management.volumes)]

+-----------------------------------+-------------------------------------------------------------------------------+
| **Key:**                          | [`security.devlxd.management.volumes`] |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Type:**                         | []                                                                  |
|                                   |                                                                               |
|                                   | bool                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Default:**                      | []                                                                  |
|                                   |                                                                               |
|                                   | [`false`]                              |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                  |
|                                   |                                                                               |
|                                   | yes                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------+

[[`security.idmap.base`]][]

The base host ID to use for the allocation

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.idmap.base)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`security.idmap.base`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | integer                                                        |
+-----------------------------------+----------------------------------------------------------------+
| **Live update:**                  | []                                                   |
|                                   |                                                                |
|                                   | no                                                             |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | unprivileged container                                         |
+-----------------------------------+----------------------------------------------------------------+

Setting this option overrides auto-detection.

[[`security.idmap.isolated`]][]

Whether to use a unique idmap for this instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.idmap.isolated)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`security.idmap.isolated`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | bool                                                               |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`false`]                   |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+
| **Condition:**                    | []                                                       |
|                                   |                                                                    |
|                                   | unprivileged container                                             |
+-----------------------------------+--------------------------------------------------------------------+

If specified, the idmap used for this instance is unique among instances that have this option set.

[[`security.idmap.size`]][]

The size of the idmap to use

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.idmap.size)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`security.idmap.size`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | integer                                                        |
+-----------------------------------+----------------------------------------------------------------+
| **Live update:**                  | []                                                   |
|                                   |                                                                |
|                                   | no                                                             |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | unprivileged container                                         |
+-----------------------------------+----------------------------------------------------------------+

[[`security.nesting`]][]

Whether to support running LXD (nested) inside the instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.nesting)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`security.nesting`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | bool                                                        |
+-----------------------------------+-------------------------------------------------------------+
| **Default:**                      | []                                                |
|                                   |                                                             |
|                                   | [`false`]            |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | yes                                                         |
+-----------------------------------+-------------------------------------------------------------+
| **Condition:**                    | []                                                |
|                                   |                                                             |
|                                   | container                                                   |
+-----------------------------------+-------------------------------------------------------------+

[[`security.privileged`]][]

Whether to run the instance in privileged mode

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.privileged)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`security.privileged`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | bool                                                           |
+-----------------------------------+----------------------------------------------------------------+
| **Default:**                      | []                                                   |
|                                   |                                                                |
|                                   | [`false`]               |
+-----------------------------------+----------------------------------------------------------------+
| **Live update:**                  | []                                                   |
|                                   |                                                                |
|                                   | no                                                             |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | container                                                      |
+-----------------------------------+----------------------------------------------------------------+

See [[Container security]](../../explanation/security/#container-security) for more information.

[[`security.protection.delete`]][]

Whether to prevent the instance from being deleted

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.protection.delete)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`security.protection.delete`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | bool                                                                  |
+-----------------------------------+-----------------------------------------------------------------------+
| **Default:**                      | []                                                          |
|                                   |                                                                       |
|                                   | [`false`]                      |
+-----------------------------------+-----------------------------------------------------------------------+
| **Live update:**                  | []                                                          |
|                                   |                                                                       |
|                                   | container                                                             |
+-----------------------------------+-----------------------------------------------------------------------+

[[`security.protection.shift`]][]

Whether to protect the file system from being UID/GID shifted

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.protection.shift)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`security.protection.shift`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | bool                                                                 |
+-----------------------------------+----------------------------------------------------------------------+
| **Default:**                      | []                                                         |
|                                   |                                                                      |
|                                   | [`false`]                     |
+-----------------------------------+----------------------------------------------------------------------+
| **Live update:**                  | []                                                         |
|                                   |                                                                      |
|                                   | yes                                                                  |
+-----------------------------------+----------------------------------------------------------------------+
| **Condition:**                    | []                                                         |
|                                   |                                                                      |
|                                   | container                                                            |
+-----------------------------------+----------------------------------------------------------------------+

Set this option to [`true`] to prevent the instance's file system from being UID/GID shifted on startup.

[[`security.protection.start`]][]

Whether to prevent the instance from being started

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.protection.start)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`security.protection.start`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | bool                                                                 |
+-----------------------------------+----------------------------------------------------------------------+
| **Default:**                      | []                                                         |
|                                   |                                                                      |
|                                   | [`false`]                     |
+-----------------------------------+----------------------------------------------------------------------+
| **Live update:**                  | []                                                         |
|                                   |                                                                      |
|                                   | container                                                            |
+-----------------------------------+----------------------------------------------------------------------+

[[`security.secureboot`]][]

Whether UEFI secure boot is enabled with the default Microsoft keys

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.secureboot)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`security.secureboot`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | bool                                                           |
+-----------------------------------+----------------------------------------------------------------+
| **Default:**                      | []                                                   |
|                                   |                                                                |
|                                   | [`true`]                |
+-----------------------------------+----------------------------------------------------------------+
| **Live update:**                  | []                                                   |
|                                   |                                                                |
|                                   | no                                                             |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | virtual machine                                                |
+-----------------------------------+----------------------------------------------------------------+

When disabling this option, consider enabling [[`security.csm`]](#instance-security:security.csm).

[[`security.sev`]][]

Whether AMD SEV (Secure Encrypted Virtualization) is enabled for this VM

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.sev)]

+-----------------------------------+---------------------------------------------------------+
| **Key:**                          | [`security.sev`] |
+-----------------------------------+---------------------------------------------------------+
| **Type:**                         | []                                            |
|                                   |                                                         |
|                                   | bool                                                    |
+-----------------------------------+---------------------------------------------------------+
| **Default:**                      | []                                            |
|                                   |                                                         |
|                                   | [`false`]        |
+-----------------------------------+---------------------------------------------------------+
| **Live update:**                  | []                                            |
|                                   |                                                         |
|                                   | no                                                      |
+-----------------------------------+---------------------------------------------------------+
| **Condition:**                    | []                                            |
|                                   |                                                         |
|                                   | virtual machine                                         |
+-----------------------------------+---------------------------------------------------------+

[[`security.sev.policy.es`]][]

Whether AMD SEV-ES (SEV Encrypted State) is enabled for this VM

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.sev.policy.es)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`security.sev.policy.es`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | bool                                                              |
+-----------------------------------+-------------------------------------------------------------------+
| **Default:**                      | []                                                      |
|                                   |                                                                   |
|                                   | [`false`]                  |
+-----------------------------------+-------------------------------------------------------------------+
| **Live update:**                  | []                                                      |
|                                   |                                                                   |
|                                   | no                                                                |
+-----------------------------------+-------------------------------------------------------------------+
| **Condition:**                    | []                                                      |
|                                   |                                                                   |
|                                   | virtual machine                                                   |
+-----------------------------------+-------------------------------------------------------------------+

[[`security.sev.session.data`]][]

The guest owner's [`base64`]-encoded session blob

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.sev.session.data)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`security.sev.session.data`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+
| **Default:**                      | []                                                         |
|                                   |                                                                      |
|                                   | [`true`]                      |
+-----------------------------------+----------------------------------------------------------------------+
| **Live update:**                  | []                                                         |
|                                   |                                                                      |
|                                   | no                                                                   |
+-----------------------------------+----------------------------------------------------------------------+
| **Condition:**                    | []                                                         |
|                                   |                                                                      |
|                                   | virtual machine                                                      |
+-----------------------------------+----------------------------------------------------------------------+

[[`security.sev.session.dh`]][]

The guest owner's [`base64`]-encoded Diffie-Hellman key

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.sev.session.dh)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`security.sev.session.dh`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | string                                                             |
+-----------------------------------+--------------------------------------------------------------------+
| **Default:**                      | []                                                       |
|                                   |                                                                    |
|                                   | [`true`]                    |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+
| **Condition:**                    | []                                                       |
|                                   |                                                                    |
|                                   | virtual machine                                                    |
+-----------------------------------+--------------------------------------------------------------------+

[[`security.syscalls.allow`]][]

List of syscalls to allow

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.allow)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.allow`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | string                                                             |
+-----------------------------------+--------------------------------------------------------------------+
| **Live update:**                  | []                                                       |
|                                   |                                                                    |
|                                   | no                                                                 |
+-----------------------------------+--------------------------------------------------------------------+
| **Condition:**                    | []                                                       |
|                                   |                                                                    |
|                                   | container                                                          |
+-----------------------------------+--------------------------------------------------------------------+

A [`\n`]-separated list of syscalls to allow. This list must be mutually exclusive with [`security.syscalls.deny*`].

[[`security.syscalls.deny`]][]

List of syscalls to deny

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.deny)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.deny`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Live update:**                  | []                                                      |
|                                   |                                                                   |
|                                   | no                                                                |
+-----------------------------------+-------------------------------------------------------------------+
| **Condition:**                    | []                                                      |
|                                   |                                                                   |
|                                   | container                                                         |
+-----------------------------------+-------------------------------------------------------------------+

A [`\n`]-separated list of syscalls to deny. This list must be mutually exclusive with [`security.syscalls.allow`].

[[`security.syscalls.deny_compat`]][]

Whether to block [`compat_*`] syscalls ([`x86_64`] only)

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.deny_compat)]

+-----------------------------------+--------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.deny_compat`] |
+-----------------------------------+--------------------------------------------------------------------------+
| **Type:**                         | []                                                             |
|                                   |                                                                          |
|                                   | bool                                                                     |
+-----------------------------------+--------------------------------------------------------------------------+
| **Default:**                      | []                                                             |
|                                   |                                                                          |
|                                   | [`false`]                         |
+-----------------------------------+--------------------------------------------------------------------------+
| **Live update:**                  | []                                                             |
|                                   |                                                                          |
|                                   | no                                                                       |
+-----------------------------------+--------------------------------------------------------------------------+
| **Condition:**                    | []                                                             |
|                                   |                                                                          |
|                                   | container                                                                |
+-----------------------------------+--------------------------------------------------------------------------+

On [`x86_64`], this option controls whether to block [`compat_*`] syscalls. On other architectures, the option is ignored.

[[`security.syscalls.deny_default`]][]

Whether to enable the default syscall deny

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.deny_default)]

+-----------------------------------+---------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.deny_default`] |
+-----------------------------------+---------------------------------------------------------------------------+
| **Type:**                         | []                                                              |
|                                   |                                                                           |
|                                   | bool                                                                      |
+-----------------------------------+---------------------------------------------------------------------------+
| **Default:**                      | []                                                              |
|                                   |                                                                           |
|                                   | [`true`]                           |
+-----------------------------------+---------------------------------------------------------------------------+
| **Live update:**                  | []                                                              |
|                                   |                                                                           |
|                                   | no                                                                        |
+-----------------------------------+---------------------------------------------------------------------------+
| **Condition:**                    | []                                                              |
|                                   |                                                                           |
|                                   | container                                                                 |
+-----------------------------------+---------------------------------------------------------------------------+

[[`security.syscalls.intercept.bpf`]][]

Whether to handle the [`bpf()`] system call

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.bpf)]

+-----------------------------------+----------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.bpf`] |
+-----------------------------------+----------------------------------------------------------------------------+
| **Type:**                         | []                                                               |
|                                   |                                                                            |
|                                   | bool                                                                       |
+-----------------------------------+----------------------------------------------------------------------------+
| **Default:**                      | []                                                               |
|                                   |                                                                            |
|                                   | [`false`]                           |
+-----------------------------------+----------------------------------------------------------------------------+
| **Live update:**                  | []                                                               |
|                                   |                                                                            |
|                                   | no                                                                         |
+-----------------------------------+----------------------------------------------------------------------------+
| **Condition:**                    | []                                                               |
|                                   |                                                                            |
|                                   | container                                                                  |
+-----------------------------------+----------------------------------------------------------------------------+

[[`security.syscalls.intercept.bpf.devices`]][]

Whether to allow BPF programs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.bpf.devices)]

+-----------------------------------+------------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.bpf.devices`] |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                       |
|                                   |                                                                                    |
|                                   | bool                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                       |
|                                   |                                                                                    |
|                                   | [`false`]                                   |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                       |
|                                   |                                                                                    |
|                                   | no                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                       |
|                                   |                                                                                    |
|                                   | container                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------+

This option controls whether to allow BPF programs for the devices cgroup in the unified hierarchy to be loaded.

[[`security.syscalls.intercept.mknod`]][]

Whether to handle the [`mknod`] and [`mknodat`] system calls

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.mknod)]

+-----------------------------------+------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.mknod`] |
+-----------------------------------+------------------------------------------------------------------------------+
| **Type:**                         | []                                                                 |
|                                   |                                                                              |
|                                   | bool                                                                         |
+-----------------------------------+------------------------------------------------------------------------------+
| **Default:**                      | []                                                                 |
|                                   |                                                                              |
|                                   | [`false`]                             |
+-----------------------------------+------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                 |
|                                   |                                                                              |
|                                   | no                                                                           |
+-----------------------------------+------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                 |
|                                   |                                                                              |
|                                   | container                                                                    |
+-----------------------------------+------------------------------------------------------------------------------+

These system calls allow creation of a limited subset of char/block devices.

[[`security.syscalls.intercept.mount`]][]

Whether to handle the [`mount`] system call

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.mount)]

+-----------------------------------+------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.mount`] |
+-----------------------------------+------------------------------------------------------------------------------+
| **Type:**                         | []                                                                 |
|                                   |                                                                              |
|                                   | bool                                                                         |
+-----------------------------------+------------------------------------------------------------------------------+
| **Default:**                      | []                                                                 |
|                                   |                                                                              |
|                                   | [`false`]                             |
+-----------------------------------+------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                 |
|                                   |                                                                              |
|                                   | no                                                                           |
+-----------------------------------+------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                 |
|                                   |                                                                              |
|                                   | container                                                                    |
+-----------------------------------+------------------------------------------------------------------------------+

[[`security.syscalls.intercept.mount.allowed`]][]

File systems that can be mounted

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.mount.allowed)]

+-----------------------------------+--------------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.mount.allowed`] |
+-----------------------------------+--------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                         |
|                                   |                                                                                      |
|                                   | string                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                         |
|                                   |                                                                                      |
|                                   | yes                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                         |
|                                   |                                                                                      |
|                                   | container                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------+

Specify a comma-separated list of file systems that are safe to mount for processes inside the instance.

[[`security.syscalls.intercept.mount.fuse`]][]

File system that should be redirected to FUSE implementation

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.mount.fuse)]

+-----------------------------------+-----------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.mount.fuse`] |
+-----------------------------------+-----------------------------------------------------------------------------------+
| **Type:**                         | []                                                                      |
|                                   |                                                                                   |
|                                   | string                                                                            |
+-----------------------------------+-----------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                      |
|                                   |                                                                                   |
|                                   | yes                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                      |
|                                   |                                                                                   |
|                                   | container                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------+

Specify the mounts of a given file system that should be redirected to their FUSE implementation (for example, [`ext4=fuse2fs`]).

[[`security.syscalls.intercept.mount.shift`]][]

Whether to use idmapped mounts for syscall interception

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.mount.shift)]

+-----------------------------------+------------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.mount.shift`] |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                       |
|                                   |                                                                                    |
|                                   | bool                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                       |
|                                   |                                                                                    |
|                                   | [`false`]                                   |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                       |
|                                   |                                                                                    |
|                                   | yes                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                       |
|                                   |                                                                                    |
|                                   | container                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------+

[[`security.syscalls.intercept.sched_setscheduler`]][]

Whether to handle the [`sched_setscheduler`] system call

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.sched_setscheduler)]

+-----------------------------------+-------------------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.sched_setscheduler`] |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                              |
|                                   |                                                                                           |
|                                   | bool                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **Default:**                      | []                                                                              |
|                                   |                                                                                           |
|                                   | [`false`]                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                              |
|                                   |                                                                                           |
|                                   | no                                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                              |
|                                   |                                                                                           |
|                                   | container                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+

This system call allows increasing process priority.

[[`security.syscalls.intercept.setxattr`]][]

Whether to handle the [`setxattr`] system call

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.setxattr)]

+-----------------------------------+---------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.setxattr`] |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Type:**                         | []                                                                    |
|                                   |                                                                                 |
|                                   | bool                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Default:**                      | []                                                                    |
|                                   |                                                                                 |
|                                   | [`false`]                                |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                    |
|                                   |                                                                                 |
|                                   | no                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                    |
|                                   |                                                                                 |
|                                   | container                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------+

This system call allows setting a limited subset of restricted extended attributes.

[[`security.syscalls.intercept.sysinfo`]][]

Whether to handle the [`sysinfo`] system call

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-security:security.syscalls.intercept.sysinfo)]

+-----------------------------------+--------------------------------------------------------------------------------+
| **Key:**                          | [`security.syscalls.intercept.sysinfo`] |
+-----------------------------------+--------------------------------------------------------------------------------+
| **Type:**                         | []                                                                   |
|                                   |                                                                                |
|                                   | bool                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------+
| **Default:**                      | []                                                                   |
|                                   |                                                                                |
|                                   | [`false`]                               |
+-----------------------------------+--------------------------------------------------------------------------------+
| **Live update:**                  | []                                                                   |
|                                   |                                                                                |
|                                   | no                                                                             |
+-----------------------------------+--------------------------------------------------------------------------------+
| **Condition:**                    | []                                                                   |
|                                   |                                                                                |
|                                   | container                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------+

This system call can be used to get cgroup-based resource usage information.

[]

## Snapshot scheduling and configuration[¶](#snapshot-scheduling-and-configuration "Link to this heading")

The following instance options control the creation and expiry of [[instance snapshots]](../../howto/instances_backup/#instances-snapshots):

[[`snapshots.expiry`]][]

When snapshots are to be deleted

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-snapshots:snapshots.expiry)]

+-----------------------------------+-------------------------------------------------------------+
| **Key:**                          | [`snapshots.expiry`] |
+-----------------------------------+-------------------------------------------------------------+
| **Type:**                         | []                                                |
|                                   |                                                             |
|                                   | string                                                      |
+-----------------------------------+-------------------------------------------------------------+
| **Live update:**                  | []                                                |
|                                   |                                                             |
|                                   | no                                                          |
+-----------------------------------+-------------------------------------------------------------+

Specify an expression like [`1M`]` `[`2H`]` `[`3d`]` `[`4w`]` `[`5m`]` `[`6y`].

[[`snapshots.pattern`]][]

Template for the snapshot name

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-snapshots:snapshots.pattern)]

+-----------------------------------+--------------------------------------------------------------+
| **Key:**                          | [`snapshots.pattern`] |
+-----------------------------------+--------------------------------------------------------------+
| **Type:**                         | []                                                 |
|                                   |                                                              |
|                                   | string                                                       |
+-----------------------------------+--------------------------------------------------------------+
| **Default:**                      | []                                                 |
|                                   |                                                              |
|                                   | [`snap%d`]            |
+-----------------------------------+--------------------------------------------------------------+
| **Live update:**                  | []                                                 |
|                                   |                                                              |
|                                   | no                                                           |
+-----------------------------------+--------------------------------------------------------------+

Specify a Pongo2 template string that represents the snapshot name. This template is used for scheduled snapshots and for unnamed snapshots.

See [[Automatic snapshot names]](#instance-options-snapshots-names) for more information.

[[`snapshots.schedule`]][]

Schedule for automatic instance snapshots

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-snapshots:snapshots.schedule)]

+-----------------------------------+---------------------------------------------------------------+
| **Key:**                          | [`snapshots.schedule`] |
+-----------------------------------+---------------------------------------------------------------+
| **Type:**                         | []                                                  |
|                                   |                                                               |
|                                   | string                                                        |
+-----------------------------------+---------------------------------------------------------------+
| **Default:**                      | []                                                  |
|                                   |                                                               |
|                                   | empty                                                         |
+-----------------------------------+---------------------------------------------------------------+
| **Live update:**                  | []                                                  |
|                                   |                                                               |
|                                   | no                                                            |
+-----------------------------------+---------------------------------------------------------------+

Specify either a cron expression ([`<minute>`]` `[`<hour>`]` `[`<dom>`]` `[`<month>`]` `[`<dow>`]), a comma-separated list of schedule aliases ([`@hourly`], [`@daily`], [`@midnight`], [`@weekly`], [`@monthly`], [`@annually`], [`@yearly`]), or leave empty to disable automatic snapshots.

[[`snapshots.schedule.stopped`]][]

Whether to automatically snapshot stopped instances

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-snapshots:snapshots.schedule.stopped)]

+-----------------------------------+-----------------------------------------------------------------------+
| **Key:**                          | [`snapshots.schedule.stopped`] |
+-----------------------------------+-----------------------------------------------------------------------+
| **Type:**                         | []                                                          |
|                                   |                                                                       |
|                                   | bool                                                                  |
+-----------------------------------+-----------------------------------------------------------------------+
| **Default:**                      | []                                                          |
|                                   |                                                                       |
|                                   | [`false`]                      |
+-----------------------------------+-----------------------------------------------------------------------+
| **Live update:**                  | []                                                          |
|                                   |                                                                       |
|                                   | no                                                                    |
+-----------------------------------+-----------------------------------------------------------------------+

[]

### Automatic snapshot names[¶](#automatic-snapshot-names "Link to this heading")

The [`snapshots.pattern`] option takes a Pongo2 template string to format the snapshot name.

To add a time stamp to the snapshot name, use the Pongo2 context variable [`creation_date`]. Make sure to format the date in your template string to avoid forbidden characters in the snapshot name. For example, set [`snapshots.pattern`] to [`]` `[`creation_date|date:'2006-01-02_15-04-05'`]` `[`}}`] to name the snapshots after their time of creation, down to the precision of a second.

Another way to avoid name collisions is to use the placeholder [`%d`] in the pattern. For the first snapshot, the placeholder is replaced with [`0`]. For subsequent snapshots, the existing snapshot names are taken into account to find the highest number at the placeholder's position. This number is then incremented by one for the new name.

[]

## Volatile internal data[¶](#volatile-internal-data "Link to this heading")

Warning

The [`volatile.*`] keys cannot be manipulated by the user. Do not attempt to modify these keys in any way. LXD modifies these keys, and attempting to manipulate them yourself might break LXD in non-obvious ways.

The following volatile keys are currently used internally by LXD to store internal data specific to an instance:

[[`volatile.<name>.apply_quota`]][]

Disk quota

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.apply_quota)]

+-----------------------------------+------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.apply_quota`] |
+-----------------------------------+------------------------------------------------------------------------+
| **Type:**                         | []                                                           |
|                                   |                                                                        |
|                                   | string                                                                 |
+-----------------------------------+------------------------------------------------------------------------+

The disk quota is applied the next time the instance starts.

[[`volatile.<name>.bus`]][]

Persistent VM bus number

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.bus)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.bus`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | integer                                                        |
+-----------------------------------+----------------------------------------------------------------+

Persistent VM bus number.

[[`volatile.<name>.ceph_rbd`]][]

RBD device path for Ceph disk devices

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.ceph_rbd)]

+-----------------------------------+---------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.ceph_rbd`] |
+-----------------------------------+---------------------------------------------------------------------+
| **Type:**                         | []                                                        |
|                                   |                                                                     |
|                                   | string                                                              |
+-----------------------------------+---------------------------------------------------------------------+

RBD device path for Ceph disk devices.

[[`volatile.<name>.devlxd.owner`]][]

DevLXD identity ID that owns the device.

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.devlxd.owner)]

+-----------------------------------+-------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.devlxd.owner`] |
+-----------------------------------+-------------------------------------------------------------------------+
| **Type:**                         | []                                                            |
|                                   |                                                                         |
|                                   | string                                                                  |
+-----------------------------------+-------------------------------------------------------------------------+

ID of the DevLXD identity that owns the device. It is used by DevLXD to restrict access of an identity to devices that were created by that identity.

[[`volatile.<name>.host_name`]][]

Network device name on the host

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.host_name)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.host_name`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+

Network device name on the host.

[[`volatile.<name>.hwaddr`]][]

Network device MAC address

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.hwaddr)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.hwaddr`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+

The network device MAC address is used when no [`hwaddr`] property is set on the device itself.

[[`volatile.<name>.last_state.created`]][]

Whether the network device physical device was created

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.created)]

+-----------------------------------+-------------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.created`] |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Type:**                         | []                                                                  |
|                                   |                                                                               |
|                                   | bool                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------+

Possible values are [`true`] or [`false`].

[[`volatile.<name>.last_state.hwaddr`]][]

Network device original MAC

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.hwaddr)]

+-----------------------------------+------------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.hwaddr`] |
+-----------------------------------+------------------------------------------------------------------------------+
| **Type:**                         | []                                                                 |
|                                   |                                                                              |
|                                   | string                                                                       |
+-----------------------------------+------------------------------------------------------------------------------+

The original MAC that was used when moving a physical device into an instance.

[[`volatile.<name>.last_state.mtu`]][]

Network device original MTU

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.mtu)]

+-----------------------------------+---------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.mtu`] |
+-----------------------------------+---------------------------------------------------------------------------+
| **Type:**                         | []                                                              |
|                                   |                                                                           |
|                                   | string                                                                    |
+-----------------------------------+---------------------------------------------------------------------------+

The original MTU that was used when moving a physical device into an instance.

[[`volatile.<name>.last_state.vdpa.name`]][]

VDPA device name

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.vdpa.name)]

+-----------------------------------+---------------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.vdpa.name`] |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Type:**                         | []                                                                    |
|                                   |                                                                                 |
|                                   | string                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------+

The VDPA device name used when moving a VDPA device file descriptor into an instance.

[[`volatile.<name>.last_state.vf.hwaddr`]][]

SR-IOV virtual function original MAC

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.vf.hwaddr)]

+-----------------------------------+---------------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.vf.hwaddr`] |
+-----------------------------------+---------------------------------------------------------------------------------+
| **Type:**                         | []                                                                    |
|                                   |                                                                                 |
|                                   | string                                                                          |
+-----------------------------------+---------------------------------------------------------------------------------+

The original MAC used when moving a VF into an instance.

[[`volatile.<name>.last_state.vf.id`]][]

SR-IOV virtual function ID

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.vf.id)]

+-----------------------------------+-----------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.vf.id`] |
+-----------------------------------+-----------------------------------------------------------------------------+
| **Type:**                         | []                                                                |
|                                   |                                                                             |
|                                   | string                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------+

The ID used when moving a VF into an instance.

[[`volatile.<name>.last_state.vf.spoofcheck`]][]

SR-IOV virtual function original spoof check setting

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.vf.spoofcheck)]

+-----------------------------------+-------------------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.vf.spoofcheck`] |
+-----------------------------------+-------------------------------------------------------------------------------------+
| **Type:**                         | []                                                                        |
|                                   |                                                                                     |
|                                   | string                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------+

The original spoof check setting used when moving a VF into an instance.

[[`volatile.<name>.last_state.vf.vlan`]][]

SR-IOV virtual function original VLAN

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.%3Cname%3E.last_state.vf.vlan)]

+-----------------------------------+-------------------------------------------------------------------------------+
| **Key:**                          | [`volatile.<name>.last_state.vf.vlan`] |
+-----------------------------------+-------------------------------------------------------------------------------+
| **Type:**                         | []                                                                  |
|                                   |                                                                               |
|                                   | string                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------+

The original VLAN used when moving a VF into an instance.

[[`volatile.apply_nvram`]][]

Whether to regenerate VM NVRAM the next time the instance starts

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.apply_nvram)]

+-----------------------------------+-----------------------------------------------------------------+
| **Key:**                          | [`volatile.apply_nvram`] |
+-----------------------------------+-----------------------------------------------------------------+
| **Type:**                         | []                                                    |
|                                   |                                                                 |
|                                   | bool                                                            |
+-----------------------------------+-----------------------------------------------------------------+

[[`volatile.apply_template`]][]

Template hook

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.apply_template)]

+-----------------------------------+--------------------------------------------------------------------+
| **Key:**                          | [`volatile.apply_template`] |
+-----------------------------------+--------------------------------------------------------------------+
| **Type:**                         | []                                                       |
|                                   |                                                                    |
|                                   | string                                                             |
+-----------------------------------+--------------------------------------------------------------------+

The template with the given name is triggered upon next startup.

[[`volatile.attached_volumes`]][]

JSON-serialized map of attached volume device names to the UUIDs of their corresponding snapshots.

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.attached_volumes)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`volatile.attached_volumes`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+
| **Condition:**                    | []                                                         |
|                                   |                                                                      |
|                                   | snapshot                                                             |
+-----------------------------------+----------------------------------------------------------------------+

JSON-serialized map of attached volume device names to the UUIDs of their corresponding snapshots, created as part of a multi-volume snapshot.

[[`volatile.base_image`]][]

Hash of the base image

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.base_image)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`volatile.base_image`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | string                                                         |
+-----------------------------------+----------------------------------------------------------------+

The hash of the image that the instance was created from (empty if the instance was not created from an image).

[[`volatile.bus.mode`]][]

Device bus allocation mode

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.bus.mode)]

+-----------------------------------+--------------------------------------------------------------+
| **Key:**                          | [`volatile.bus.mode`] |
+-----------------------------------+--------------------------------------------------------------+
| **Type:**                         | []                                                 |
|                                   |                                                              |
|                                   | string                                                       |
+-----------------------------------+--------------------------------------------------------------+

Set to [`persistent`] when persistent bus allocation mode is enabled.

[[`volatile.cloud-init.instance-id`]][]

[`instance-id`] (UUID) exposed to [`cloud-init`]

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.cloud-init.instance-id)]

+-----------------------------------+----------------------------------------------------------------------------+
| **Key:**                          | [`volatile.cloud-init.instance-id`] |
+-----------------------------------+----------------------------------------------------------------------------+
| **Type:**                         | []                                                               |
|                                   |                                                                            |
|                                   | string                                                                     |
+-----------------------------------+----------------------------------------------------------------------------+

[[`volatile.cluster.group`]][]

The target cluster group

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.cluster.group)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`volatile.cluster.group`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+

The target cluster group at instance creation or migration time. This is used during scheduling events such as evacuation to ensure the instance is placed correctly.

[[`volatile.evacuate.origin`]][]

The origin of the evacuated instance

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.evacuate.origin)]

+-----------------------------------+---------------------------------------------------------------------+
| **Key:**                          | [`volatile.evacuate.origin`] |
+-----------------------------------+---------------------------------------------------------------------+
| **Type:**                         | []                                                        |
|                                   |                                                                     |
|                                   | string                                                              |
+-----------------------------------+---------------------------------------------------------------------+

The cluster member that the instance lived on before evacuation.

[[`volatile.idmap.base`]][]

The first ID in the container's primary idmap range

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.idmap.base)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`volatile.idmap.base`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | integer                                                        |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | container                                                      |
+-----------------------------------+----------------------------------------------------------------+

[[`volatile.idmap.current`]][]

The idmap currently in use by the container

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.idmap.current)]

+-----------------------------------+-------------------------------------------------------------------+
| **Key:**                          | [`volatile.idmap.current`] |
+-----------------------------------+-------------------------------------------------------------------+
| **Type:**                         | []                                                      |
|                                   |                                                                   |
|                                   | string                                                            |
+-----------------------------------+-------------------------------------------------------------------+
| **Condition:**                    | []                                                      |
|                                   |                                                                   |
|                                   | container                                                         |
+-----------------------------------+-------------------------------------------------------------------+

[[`volatile.idmap.next`]][]

The idmap to use the next time the container starts

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.idmap.next)]

+-----------------------------------+----------------------------------------------------------------+
| **Key:**                          | [`volatile.idmap.next`] |
+-----------------------------------+----------------------------------------------------------------+
| **Type:**                         | []                                                   |
|                                   |                                                                |
|                                   | string                                                         |
+-----------------------------------+----------------------------------------------------------------+
| **Condition:**                    | []                                                   |
|                                   |                                                                |
|                                   | container                                                      |
+-----------------------------------+----------------------------------------------------------------+

[[`volatile.last_state.idmap`]][]

On-disk UID/GID map for the container's rootfs

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.last_state.idmap)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`volatile.last_state.idmap`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+
| **Condition:**                    | []                                                         |
|                                   |                                                                      |
|                                   | container                                                            |
+-----------------------------------+----------------------------------------------------------------------+

The UID/GID map that has been applied to the container's underlying storage. This is usually set for containers created on older kernels that don't support idmapped mounts.

[[`volatile.last_state.power`]][]

Instance state as of last host shutdown

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.last_state.power)]

+-----------------------------------+----------------------------------------------------------------------+
| **Key:**                          | [`volatile.last_state.power`] |
+-----------------------------------+----------------------------------------------------------------------+
| **Type:**                         | []                                                         |
|                                   |                                                                      |
|                                   | string                                                               |
+-----------------------------------+----------------------------------------------------------------------+

[[`volatile.uuid`]][]

Instance UUID

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.uuid)]

+-----------------------------------+----------------------------------------------------------+
| **Key:**                          | [`volatile.uuid`] |
+-----------------------------------+----------------------------------------------------------+
| **Type:**                         | []                                             |
|                                   |                                                          |
|                                   | string                                                   |
+-----------------------------------+----------------------------------------------------------+

The instance UUID is globally unique across all servers and projects.

[[`volatile.uuid.generation`]][]

Instance generation UUID

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.uuid.generation)]

+-----------------------------------+---------------------------------------------------------------------+
| **Key:**                          | [`volatile.uuid.generation`] |
+-----------------------------------+---------------------------------------------------------------------+
| **Type:**                         | []                                                        |
|                                   |                                                                     |
|                                   | string                                                              |
+-----------------------------------+---------------------------------------------------------------------+

The instance generation UUID changes whenever the instance's place in time moves backwards. It is globally unique across all servers and projects.

[[`volatile.vsock_id`]][]

Instance [`vsock`]` `[`ID`] used as of last start

[[*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctYXJyb3ctcmlnaHQiPjwvdXNlPjwvc3ZnPg==)*](#instance-volatile:volatile.vsock_id)]

+-----------------------------------+--------------------------------------------------------------+
| **Key:**                          | [`volatile.vsock_id`] |
+-----------------------------------+--------------------------------------------------------------+
| **Type:**                         | []                                                 |
|                                   |                                                              |
|                                   | string                                                       |
+-----------------------------------+--------------------------------------------------------------+