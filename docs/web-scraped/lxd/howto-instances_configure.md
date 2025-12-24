# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/instances_configure/

[]

# How to configure instances[¶](#how-to-configure-instances "Link to this heading")

You can configure instances by setting [[Instance properties]](../../reference/instance_properties/#instance-properties), [[Instance options]](../../reference/instance_options/#instance-options), or by adding and configuring [[Devices]](../../reference/devices/#devices).

See the following sections for instructions.

Note

To store and reuse different instance configurations, use [[profiles]](../../profiles/#profiles).

[]

## Configure instance options[¶](#configure-instance-options "Link to this heading")

You can specify instance options when you [[create an instance]](../instances_create/#instances-create). Alternatively, you can update the instance options after the instance is created.

CLI

API

UI

Use the [[[`lxc`]` `[`config`]` `[`set`]]](../../reference/manpages/lxc/config/set/#lxc-config-set-md) command to update instance options. Specify the instance name and the key and value of the instance option:

    lxc config set <instance_name> <option_key>=<option_value> <option_key>=<option_value> ...

Send a PATCH request to the instance to update instance options. Specify the instance name and the key and value of the instance option:

    lxc query --request PATCH /1.0/instances/<instance_name> --data '
    }'

See [[`PATCH`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_patch) for more information.

To update instance options, go to the [Configuration] tab of the instance detail page and click [Edit instance].

Find the configuration option that you want to update and change its value. Click [Save changes] to save the updated configuration.

To configure instance options that are not displayed in the UI, follow the instructions in [[Edit the full instance configuration]](#instances-configure-edit).

See [[Instance options]](../../reference/instance_options/#instance-options) for a list of available options and information about which options are available for which instance type.

For example, change the memory limit for your container:

CLI

API

UI

To set the memory limit to 8 GiB, enter the following command:

    lxc config set my-container limits.memory=8GiB

To set the memory limit to 8 GiB, send the following request:

    lxc query --request PATCH /1.0/instances/my-container --data '
    }'

To set the memory limit to 8 GiB, go to the [Configuration] tab of the instance detail page and select [Advanced \> Resource limits]. Then click [Edit instance].

Select [Override] for the **Memory limit** and enter 8 GiB as the absolute value.

<figure class="align-default">
<a href="../../_images/limits_memory_example.png" class="reference internal image-reference"><img src="../../_images/limits_memory_example.png" style="width: 80%;" alt="Setting the memory limit for an instance to 8 GiB" /></a>
</figure>

Note

Some of the instance options are updated immediately while the instance is running. Others are updated only when the instance is restarted.

See the "Live update" information in the [[Instance options]](../../reference/instance_options/#instance-options) reference for information about which options are applied immediately while the instance is running.

[]

## Configure instance properties[¶](#configure-instance-properties "Link to this heading")

CLI

API

UI

To update instance properties after the instance is created, use the [[[`lxc`]` `[`config`]` `[`set`]]](../../reference/manpages/lxc/config/set/#lxc-config-set-md) command with the [`--property`] flag. Specify the instance name and the key and value of the instance property:

    lxc config set <instance_name> <property_key>=<property_value> <property_key>=<property_value> ... --property

Using the same flag, you can also unset a property just like you would unset a configuration option:

    lxc config unset <instance_name> <property_key> --property

You can also retrieve a specific property value with:

    lxc config get <instance_name> <property_key> --property

To update instance properties through the API, use the same mechanism as for configuring instance options. The only difference is that properties are on the root level of the configuration, while options are under the [`config`] field.

Therefore, to set an instance property, send a PATCH request to the instance:

    lxc query --request PATCH /1.0/instances/<instance_name> --data '
    }'

To unset an instance property, send a PUT request that contains the full instance configuration that you want except for the property that you want to unset.

See [[`PATCH`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_patch) and [[`PUT`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_put) for more information.

The LXD UI does not distinguish between instance options and instance properties. Therefore, you can configure instance properties in the same way as you [[configure instance options]](#instances-configure-options).

[]

## Configure devices[¶](#configure-devices "Link to this heading")

Generally, devices can be added or removed for a container while it is running. VMs support hotplugging for some device types, but not all.

See [[Devices]](../../reference/devices/#devices) for a list of available device types and their options.

Note

Every device entry is identified by a name unique to the instance.

Devices from profiles are applied to the instance in the order in which the profiles are assigned to the instance. Devices defined directly in the instance configuration are applied last. At each stage, if a device with the same name already exists from an earlier stage, the whole device entry is overridden by the latest definition.

Device names are limited to a maximum of 64 characters.

CLI

API

UI

To add and configure an instance device for your instance, use the [[[`lxc`]` `[`config`]` `[`device`]` `[`add`]]](../../reference/manpages/lxc/config/device/add/#lxc-config-device-add-md) command.

Specify the instance name, a device name, the device type and maybe device options (depending on the [[device type]](../../reference/devices/#devices)):

    lxc config device add <instance_name> <device_name> <device_type> <device_option_key>=<device_option_value> <device_option_key>=<device_option_value> ...

For example, to add the storage at [`/share/c1`] on the host system to your instance at path [`/opt`], enter the following command:

    lxc config device add my-container disk-storage-device disk source=/share/c1 path=/opt

To configure instance device options for a device that you have added earlier, use the [[[`lxc`]` `[`config`]` `[`device`]` `[`set`]]](../../reference/manpages/lxc/config/device/set/#lxc-config-device-set-md) command:

    lxc config device set <instance_name> <device_name> <device_option_key>=<device_option_value> <device_option_key>=<device_option_value> ...

Device options for a device inherited from a profile cannot be updated within the instance. Use the [[[`lxc`]` `[`config`]` `[`device`]` `[`override`]]](../../reference/manpages/lxc/config/device/override/#lxc-config-device-override-md) command to create a copy of the profile device with updated device options. The newly created instance device will override the inherited device.

Specify the instance name, device name and the device options that should be overridden:

    lxc config device override <instance_name> <device_name> <device_option_key>=<device_option_value> <device_option_key>=<device_option_value> ...

Note

You can also specify device options by using the [`--device`] flag when [[creating an instance]](../instances_create/#instances-create). This is useful if you want to override device options for a device that is provided through a [[profile]](../../profiles/#profiles).

To remove a device, use the [[[`lxc`]` `[`config`]` `[`device`]` `[`remove`]]](../../reference/manpages/lxc/config/device/remove/#lxc-config-device-remove-md) command. See [[[`lxc`]` `[`config`]` `[`device`]` `[`--help`]]](../../reference/manpages/lxc/config/device/#lxc-config-device-md) for a full list of available commands.

To add or configure an instance device for your instance, use the same mechanism of patching the instance configuration. The device configuration is located under the [`devices`] field of the configuration.

Caution

Patching a device's configuration unsets any omitted options for that device, along with the instance's [`description`] property. See [[Effects of patching device options]](#instances-configure-devices-api-patch-effects) for details.

Specify the instance name, a device name, and any [[Required device options]](#instances-configure-devices-api-required) (depending on the [[device type]](../../reference/devices/#devices)):

    lxc query --request PATCH /1.0/instances/<instance_name> --data '
      }
    }'

For example, to add the storage at [`/share/c1`] on the host system to your instance at path [`/opt`], enter the following command:

    lxc query --request PATCH /1.0/instances/my-container --data '
      }
    }'

See [[`PATCH`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_patch) for more information.

[]Required device options

When using a PATCH request to update an instance's [`devices`] property, you must include any required options for each device in the request body. The device's [`type`] option is always required. To find any other required keys for a specific device type, view the [[Devices]](../../reference/devices/#devices) reference guides. For example, for an OVN NIC device, the [[`network`]](../../reference/devices_nic/#device-nic-ovn-device-conf:network) key is required.

[]Effects of patching device options

For any device in your PATCH request, the request acts similar to a conventional PUT: it replaces all options for that device. This means that if you omit a non-required option, it is unset. Thus, include not only the options you want to add or update in your patch, but also any other existing options whose values you want to keep.

This behavior only affects the specific device or devices that you are patching; if there are other devices, you don't need to include them. It also does not affect any other instance properties, with one exception: if the instance includes a [`description`] property, that property must be passed along with [`devices`]; otherwise, it is unset.

For example, consider an instance that contains this [`devices`] property:

    "devices": ,
      "my-ovn-nic": 
    }

Let's say the following PATCH request is sent for this instance:

    lxc query --request PATCH /1.0/instances/my-instance --data '
      }
    }'

This PATCH request updates only the [`my-bridge-nic`] device, without affecting the [`my-ovn-nic`] device. The device options defined in the request body replace the existing options. After the request, this is the [`devices`] property's configuration:

    "devices": ,
      "my-ovn-nic": 
    }

Notice that in the updated [`my-bridge-nic`] device, the [`name`] option is unset and no longer appears, due to not being sent in the PATCH request.

The UI does not support all device types yet, but you can configure disk and network devices for your instances.

To attach a device to your instance, or modify an existing device, update your instance configuration (in the same way as you [[configure instance options]](#instances-configure-options)). Select [Advanced] \> [Disk devices] \> [Attach disk device] or [Advanced] \> [Network devices] \> [Attach network] to create a device and attach it to your instance.

Note

Some of the devices that are displayed in the instance configuration are inherited from a [[profile]](../../profiles/#profiles) or defined through a [[project]](../../projects/#projects). Depending on the type of device, it might not be possible to edit these devices for an instance.

To add and configure devices that are not currently supported in the UI, follow the instructions in [[Edit the full instance configuration]](#instances-configure-edit).

## Display instance configuration[¶](#display-instance-configuration "Link to this heading")

CLI

API

UI

To display the current configuration of your instance, including writable instance properties, instance options, devices and device options, enter the following command:

    lxc config show <instance_name> --expanded

To retrieve the current configuration of your instance, including writable instance properties, instance options, devices and device options, send a GET request to the instance:

    lxc query --request GET /1.0/instances/<instance_name>

See [[`GET`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_get) for more information.

To view the current configuration of your instance, go to [Instances], select your instance, and then switch to the [Configuration] tab.

To see the full configuration including instance properties, instance options, devices and device options (also the ones that aren't yet supported by the UI), select [YAML configuration]. This view shows the full YAML of the instance configuration.

[]

## Edit the full instance configuration[¶](#edit-the-full-instance-configuration "Link to this heading")

CLI

API

UI

To edit the full instance configuration, including writable instance properties, instance options, devices and device options, enter the following command:

    lxc config edit <instance_name>

Note

For convenience, the [[[`lxc`]` `[`config`]` `[`edit`]]](../../reference/manpages/lxc/config/edit/#lxc-config-edit-md) command displays the full configuration including read-only instance properties. However, you cannot edit those properties. Any changes are ignored.

To update the full instance configuration, including writable instance properties, instance options, devices and device options, send a PUT request to the instance:

    lxc query --request PUT /1.0/instances/<instance_name> --data '<instance_configuration>'

See [[`PUT`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_put) for more information.

Note

If you include changes to any read-only instance properties in the configuration you provide, they are ignored.

Instead of using the UI forms to configure your instance, you can choose to edit the YAML configuration of the instance. You must use this method if you need to update any configurations that are not available in the UI.

Important

When doing updates, do not navigate away from the YAML configuration without saving your changes. If you do, your updates are lost.

To edit the YAML configuration of your instance, go to the instance detail page, switch to the [Configuration] tab and select [YAML configuration]. Then click [Edit instance].

Edit the YAML configuration as required. Then click [Save changes] to save the updated configuration.

Note

For convenience, the YAML contains the full configuration including read-only instance properties. However, you cannot edit those properties. Any changes are ignored.