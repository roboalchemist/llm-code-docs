# Source: https://documentation.ubuntu.com/lxd/en/latest/reference/

[]

# Reference[¶](#reference "Link to this heading")

The reference material in this section provides technical descriptions of LXD.

[]

## General information[¶](#general-information "Link to this heading")

Before you start using LXD, you should check the system requirements. You should also be aware of the supported architectures, its release types and snap information, the available image servers, the format for images, and the environment used for containers.

-   [Requirements](../requirements/)
-   [Architectures](../architectures/)
-   [Release notes](release-notes/)
    -   [LXD 6.6](release-notes/release-notes-6.6/)
-   [Releases and snap](releases-snap/)
-   [Remote image servers](remote_image_servers/)
-   [Image format](image_format/)
-   [Guest OS compatibility](../guest-os-compatibility/)
-   [Container environment](../container-environment/)

[]

## Configuration options[¶](#configuration-options "Link to this heading")

LXD is highly configurable. Check the available configuration options for the LXD server and the different entities used in LXD.

-   [Configuration option index](../config-options/)
-   [Server configuration](../server/)
-   [Instance configuration](../explanation/instance_config/)
    -   [Instance properties](instance_properties/)
    -   [Instance options](instance_options/)
    -   [Devices](devices/)
    -   [Units for storage and network limits](instance_units/)
-   [Preseed YAML file fields](preseed_yaml_fields/)
-   [Project configuration](projects/)
-   [Storage drivers](storage_drivers/)
    -   [Directory - [`dir`]](storage_dir/)
    -   [Btrfs - [`btrfs`]](storage_btrfs/)
    -   [LVM - [`lvm`]](storage_lvm/)
    -   [ZFS - [`zfs`]](storage_zfs/)
    -   [Ceph RBD - [`ceph`]](storage_ceph/)
    -   [Dell PowerFlex - [`powerflex`]](storage_powerflex/)
    -   [Pure Storage - [`pure`]](storage_pure/)
    -   [HPE Alletra - [`alletra`]](storage_alletra/)
    -   [CephFS - [`cephfs`]](storage_cephfs/)
    -   [Ceph Object - [`cephobject`]](storage_cephobject/)
-   [Networks](networks/)
    -   [Bridge network](network_bridge/)
    -   [OVN network](network_ovn/)
    -   [Macvlan network](network_macvlan/)
    -   [Physical network](network_physical/)
    -   [SR-IOV network](network_sriov/)
-   [Cluster configuration](cluster_member_config/)
-   [Placement group configuration](placement_groups/)

[]

## Production setup[¶](#production-setup "Link to this heading")

Once you are ready for production, make sure your LXD server is configured to support the required load. You should also regularly [[monitor the server metrics]](../metrics/#metrics).

-   [Production server settings](server_settings/)
-   [Provided metrics](provided_metrics/)

## Fine-grained permissions[¶](#fine-grained-permissions "Link to this heading")

If you are managing user access via [[Fine-grained authorization]](../explanation/authorization/#fine-grained-authorization), check which [[permissions]](../explanation/authorization/#permissions) can be assigned to groups.

-   [Permissions](permissions/)

[]

## REST API[¶](#rest-api "Link to this heading")

All communication between LXD and its clients happens using a RESTful API over HTTP. Check the list of API extensions to see if a feature is available in your version of the API.

-   [REST API](../restapi_landing/)
    -   [Main API documentation](../rest-api/)
    -   [Main API specification](../api/)
    -   [Main API extensions](../api-extensions/)
    -   [Events API documentation](../events/)
    -   [Instance API](../dev-lxd/)

[]

## The LXD CSI driver reference[¶](#the-lxd-csi-driver-reference "Link to this heading")

Find reference information about the LXD Container Storage Interface (CSI) driver, used to integrate LXD storage backends with Kubernetes.

-   [LXD CSI driver reference](driver_csi/)

[]

## Man pages[¶](#man-pages "Link to this heading")

[`lxc`] is the command line client for LXD. Its usage is documented in the help pages for the [`lxc`] commands and subcommands.

-   [Man pages](manpages/)
    -   [[`lxc`]](manpages/lxc/)

[]

## Implementation details[¶](#implementation-details "Link to this heading")

You don't need to be aware of the internal implementation details to use LXD. However, advanced users might be interested in knowing what happens internally.

-   [Internals](../internals/)
    -   [Environment variables](../environment/)
    -   [UEFI variables for VMs](uefi_variables/)
    -   [Daemon behavior](../daemon-behavior/)
    -   [System call interception](../syscall-interception/)
    -   [User namespace setup](../userns-idmap/)
    -   [OVN implementation](ovn-internals/)
    -   [VM live migration implementation](vm_live_migration_internals/)
    -   [Dqlite](dqlite-internals/)