# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/instances_create/

[]

# How to create instances[¶](#how-to-create-instances "Link to this heading")

When creating an instance, you must specify the [[image]](../../image-handling/#about-images) on which the instance should be based.

Images contain a basic operating system (for example, a Linux distribution) and some LXD-related information. Images for various operating systems are available on the built-in remote image servers. See [[Images]](../../images/#images) for more information.

If you don't specify a name for the instance, LXD will automatically generate one. Instance names must be unique within a LXD deployment (also within a cluster). See [[Instance name requirements]](../../reference/instance_properties/#instance-name-requirements) for additional requirements.

CLI

API

UI

To create an instance, you can use either the [[[`lxc`]` `[`init`]]](../../reference/manpages/lxc/init/#lxc-init-md) or the [[[`lxc`]` `[`launch`]]](../../reference/manpages/lxc/launch/#lxc-launch-md) command. The [[[`lxc`]` `[`init`]]](../../reference/manpages/lxc/init/#lxc-init-md) command only creates the instance, while the [[[`lxc`]` `[`launch`]]](../../reference/manpages/lxc/launch/#lxc-launch-md) command creates and starts it.

Enter the following command to create a container:

    lxc launch|init <image_server>:<image_name> <instance_name> [flags]

Unless the image is available locally, you must specify the name of the image server and the name of the image (for example, [`ubuntu:24.04`] for the official Ubuntu 24.04 LTS image).

See [[[`lxc`]` `[`launch`]` `[`--help`]]](../../reference/manpages/lxc/launch/#lxc-launch-md) or [[[`lxc`]` `[`init`]` `[`--help`]]](../../reference/manpages/lxc/init/#lxc-init-md) for a full list of flags. The most common flags are:

-   [`--config`] to specify a configuration option for the new instance

-   [`--device`] to override [[device options]](../../reference/devices/#devices) for a device provided through a profile, or to specify an [[initial configuration for the root disk device]](../../reference/devices_disk/#devices-disk-initial-config) (syntax: [`--device`]` `[`<device_name>,<device_option>=<value>`])

-   [`--profile`] to specify a [[profile]](../../profiles/#profiles) to use for the new instance

-   [`--network`] or [`--storage`] to make the new instance use a specific network or storage pool

-   [`--target`] to create the instance on a specific cluster member

-   [`--vm`] to create a virtual machine instead of a container

Instead of specifying the instance configuration as flags, you can pass it to the command as a YAML file.

For example, to launch a container with the configuration from [`config.yaml`], enter the following command:

    lxc launch ubuntu:24.04 ubuntu-config < config.yaml

Tip

Check the contents of an existing instance configuration ([[[`lxc`]` `[`config`]` `[`show`]` `[`<instance_name>`]` `[`--expanded`]]](../../reference/manpages/lxc/config/show/#lxc-config-show-md)) to see the required syntax of the YAML file.

To create an instance, send a POST request to the [`/1.0/instances`] endpoint:

    lxc query --request POST /1.0/instances --data '
    }'

The return value of this query contains an operation ID, which you can use to query the status of the operation:

    lxc query --request GET /1.0/operations/<operation_ID>

Use the following query to monitor the state of the instance:

    lxc query --request GET /1.0/instances/<instance_name>/state

See [[`POST`]` `[`/1.0/instances`]](/lxd/latest/api/#/instances/instances_post) and [[`GET`]` `[`/1.0/instances//state`]](/lxd/latest/api/#/instances/instance_state_get) for more information.

The request creates the instance, but does not start it. To start an instance, send a PUT request to change the instance state:

    lxc query --request PUT /1.0/instances/<instance_name>/state --data ''

See [[Start an instance]](../instances_manage/#instances-manage-start) for more information.

If you would like to start the instance upon creation, set the [`start`] property to true. The following example will create the container, then start it:

    lxc query --request POST /1.0/instances --data ',
      "start": true
    }'

To create an instance, go to the [Instances] section and click [Create instance].

On the resulting screen, optionally enter a name and description for the instance. Then click [Browse images] to select the image to be used for the instance. Depending on the selected image, you might be able to select the [[instance type]](../../explanation/instances/#expl-instances) (container or virtual machine). You can also specify one or more profiles to use for the instance.

To further tweak the instance configuration or add devices to the instance, go to any of the tabs under [Advanced]. You can also edit the full instance configuration on the [YAML configuration] tab.

Finally, click [Create] or [Create and start] to create the instance.

## Examples[¶](#examples "Link to this heading")

The following CLI and API examples create the instances, but don't start them. If you are using the CLI client, you can use [[[`lxc`]` `[`launch`]]](../../reference/manpages/lxc/launch/#lxc-launch-md) instead of [[[`lxc`]` `[`init`]]](../../reference/manpages/lxc/init/#lxc-init-md) to automatically start them after creation.

In the UI, you can choose between [Create] and [Create and start] when you are ready to create the instance.

### Create a container[¶](#create-a-container "Link to this heading")

To create a container with an Ubuntu 24.04 LTS image from the [`ubuntu`] server using the instance name [`ubuntu-container`]:

CLI

API

UI

    lxc init ubuntu:24.04 ubuntu-container

    lxc query --request POST /1.0/instances --data '
    }'

<figure class="align-default">
<a href="../../_images/create_instance_ex1.png" class="reference internal image-reference"><img src="../../_images/create_instance_ex1.png" style="width: 80%;" alt="Create an Ubuntu 24.04 LTS container" /></a>
</figure>

### Create a virtual machine[¶](#create-a-virtual-machine "Link to this heading")

To create a virtual machine with an Ubuntu 24.04 LTS image from the [`ubuntu`] server using the instance name [`ubuntu-vm`]:

CLI

API

UI

    lxc init ubuntu:24.04 ubuntu-vm --vm

    lxc query --request POST /1.0/instances --data ',
      "type": "virtual-machine"
    }'

<figure class="align-default">
<a href="../../_images/create_instance_ex2.png" class="reference internal image-reference"><img src="../../_images/create_instance_ex2.png" style="width: 80%;" alt="Create an Ubuntu 24.04 LTS VM" /></a>
</figure>

Or with a bigger disk:

CLI

API

UI

    lxc init ubuntu:24.04 ubuntu-vm-big --vm --device root,size=30GiB

    lxc query --request POST /1.0/instances --data '
      },
      "name": "ubuntu-vm-big",
      "source": ,
      "type": "virtual-machine"
    }'

<figure class="align-default">
<a href="../../_images/create_instance_ex2-2.png" class="reference internal image-reference"><img src="../../_images/create_instance_ex2-2.png" style="width: 80%;" alt="Configure the size of the root disk" /></a>
</figure>

### Create a container with specific configuration options[¶](#create-a-container-with-specific-configuration-options "Link to this heading")

To create a container and limit its resources to one vCPU and 8 GiB of RAM:

CLI

API

UI

    lxc init ubuntu:24.04 ubuntu-limited --config limits.cpu=1 --config limits.memory=8GiB

    lxc query --request POST /1.0/instances --data ',
      "name": "ubuntu-limited",
      "source": 
    }'

<figure class="align-default">
<a href="../../_images/create_instance_ex3.png" class="reference internal image-reference"><img src="../../_images/create_instance_ex3.png" style="width: 80%;" alt="Configure resource limits" /></a>
</figure>

### Create a VM on a specific cluster member[¶](#create-a-vm-on-a-specific-cluster-member "Link to this heading")

To create a virtual machine on the cluster member [`micro2`], enter the following command:

CLI

API

UI

    lxc init ubuntu:24.04 ubuntu-vm-server2 --vm --target micro2

    lxc query --request POST /1.0/instances?target=micro2 --data ',
      "type": "virtual-machine"
    }'

<figure class="align-default">
<a href="../../_images/create_instance_ex4.png" class="reference internal image-reference"><img src="../../_images/create_instance_ex4.png" style="width: 80%;" alt="Specify which cluster member to create an instance on" /></a>
</figure>

### Create a container with a specific instance type[¶](#create-a-container-with-a-specific-instance-type "Link to this heading")

LXD supports simple instance types for clouds. Those are represented as a string that can be passed at instance creation time.

The list of supported clouds and instance types can be found at [[`images.lxd.canonical.com/meta/instance-types/all.yaml`]](https://images.lxd.canonical.com/meta/instance-types/all.yaml).

The syntax allows the three following forms:

-   [`<instance`]` `[`type>`]

-   [`<cloud>:<instance`]` `[`type>`]

-   [`c<CPU>-m<RAM`]` `[`in`]` `[`GiB>`]

For example, the following three instance types are equivalent:

-   [`t2.micro`]

-   [`aws:t2.micro`]

-   [`c1-m1`]

To create a container with this instance type:

CLI

API

UI

    lxc init ubuntu:24.04 my-instance --type t2.micro

    lxc query --request POST /1.0/instances --data '
    }'

Creating an instance with a specific cloud instance type is currently not possible through the UI. Configure the corresponding options manually or through a profile.

[]

### Create a VM that boots from an ISO[¶](#create-a-vm-that-boots-from-an-iso "Link to this heading")

To create a VM that boots from an ISO:

CLI

API

UI

First, create an empty VM that we can later install from the ISO image:

    lxc init iso-vm --empty --vm --config limits.cpu=2 --config limits.memory=4GiB --device root,size=30GiB

Note

Adapt the [`limits.cpu`], [`limits.memory`], and root size based on the hardware recommendations for the ISO image used.

The second step is to import an ISO image that can later be attached to the VM as a storage volume:

    lxc storage volume import <pool> <path-to-image.iso> iso-volume --type=iso

Lastly, attach the custom ISO volume to the VM using the following command:

    lxc config device add iso-vm iso-volume disk pool=<pool> source=iso-volume boot.priority=10

The [[`boot.priority`]](../../reference/devices_disk/#device-disk-device-conf:boot.priority) configuration key ensures that the VM will boot from the ISO first. Start the VM and [[connect to the console]](../instances_console/#instances-console) as there might be a menu you need to interact with:

    lxc start iso-vm --console

Once you're done in the serial console, disconnect from the console using [Ctrl]+[a] [q] and [[connect to the VGA console]](../instances_console/#instances-console) using the following command:

    lxc console iso-vm --type=vga

You should now see the installer. After the installation is done, detach the custom ISO volume:

    lxc storage volume detach <pool> iso-volume iso-vm

Now the VM can be rebooted, and it will boot from disk.

Note

On Linux virtual machines, the [[LXD agent can be manually installed]](#lxd-agent-manual-install).

First, create an empty VM that we can later install from the ISO image:

    lxc query --request POST /1.0/instances --data ',
      "devices": 
      },
      "source": ,
      "type": "virtual-machine"
    }'

Note

Adapt the values for [`limits.cpu`], [`limits.memory`], and [`root:`]` `[`size`] based on the hardware recommendations for the ISO image used.

The second step is to import an ISO image that can later be attached to the VM as a storage volume:

    curl -X POST -H "Content-Type: application/octet-stream" -H "X-LXD-name: iso-volume" \
    -H "X-LXD-type: iso" --data-binary @<path-to-image.iso> --unix-socket /var/snap/lxd/common/lxd/unix.socket \
    lxd/1.0/storage-pools/<pool>/volumes/custom

Note

When importing an ISO image, you must send both binary data from a file and additional headers. The [[[`lxc`]` `[`query`]]](../../reference/manpages/lxc/query/#lxc-query-md) command cannot do this, so you need to use [`curl`] or another tool instead.

Lastly, attach the custom ISO volume to the VM using the following command:

    lxc query --request PATCH /1.0/instances/iso-vm --data '
      }
    }'

The [[`boot.priority`]](../../reference/devices_disk/#device-disk-device-conf:boot.priority) configuration key ensures that the VM will boot from the ISO first. Start the VM and [[connect to the console]](../instances_console/#instances-console) as there might be a menu you need to interact with:

    lxc query --request PUT /1.0/instances/iso-vm/state --data ''
    lxc query --request POST /1.0/instances/iso-vm/console --data ''

Once you're done in the serial console, disconnect from the console using [Ctrl]+[a] [q] and [[connect to the VGA console]](../instances_console/#instances-console) using the following command:

    lxc query --request POST /1.0/instances/iso-vm/console --data ''

You should now see the installer. After the installation is done, detach the custom ISO volume:

    lxc query --request GET /1.0/instances/iso-vm
    lxc query --request PUT /1.0/instances/iso-vm --data '
      [...]
    }'

Note

You cannot remove the device through a PATCH request, but you must use a PUT request. Therefore, get the current configuration first and then provide the relevant configuration with an empty devices list through the PUT request.

Now the VM can be rebooted, and it will boot from disk.

       :end-before: 

In the [Create instance] dialog, click [Use custom ISO] instead of [Browse images]. You can then upload your ISO file and install a VM from it.

[]

### Install the LXD agent into virtual machine instances[¶](#install-the-lxd-agent-into-virtual-machine-instances "Link to this heading")

In order for features like direct command execution ([`lxc`]` `[`exec`] & [`lxc`]` `[`shell`]), file transfers ([`lxc`]` `[`file`]) and detailed usage metrics ([`lxc`]` `[`info`]) to work properly with virtual machines, an agent software is provided by LXD.

The virtual machine images from the official [[remote image servers]](../../reference/remote_image_servers/#remote-image-servers) are pre-configured to load that agent on startup.

For other virtual machines, you may want to manually install the agent.

Note

The LXD agent is currently available only on Linux virtual machines using [`systemd`].

LXD provides the agent through a remote [`9p`] file system and a [`virtiofs`] one that are both available under the mount name [`config`]. To install the agent, you'll need to get access to the virtual machine and run the following commands as root:

    modprobe 9pnet_virtio
    mount -t 9p config /mnt -o access=0,transport=virtio || mount -t virtiofs config /mnt
    cd /mnt
    ./install.sh
    cd /
    umount /mnt
    reboot

You need to perform this task once.

### Create a Windows VM[¶](#create-a-windows-vm "Link to this heading")

To create a Windows VM, you must first prepare a Windows image. See [[Repack a Windows image]](../images_create/#images-repack-windows).

The [How to install a Windows 11 VM using LXD](https://ubuntu.com/tutorials/how-to-install-a-windows-11-vm-using-lxd) tutorial shows how to prepare the image and create a Windows VM from it.