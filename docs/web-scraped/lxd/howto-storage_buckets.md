# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/storage_buckets/

[]

# How to manage storage buckets[¶](#how-to-manage-storage-buckets "Link to this heading")

[[Storage buckets]](../../explanation/storage/#storage-buckets) let you store and manage object-based data using either local or distributed storage.

Unlike custom storage volumes, storage buckets cannot be attached to instances. Instead, applications access them directly via a URL using the S3 protocol.

-   For local buckets, the LXD server provides the S3-compatible URL via its [[S3 address setting]](#howto-storage-buckets-create-requirements-local-s3).

-   For distributed buckets, a [[Ceph RADOS Gateway endpoint]](../storage_pools/#howto-storage-pools-ceph-requirements-radosgw-endpoint) provides the S3-compatible URL.

[]

## View storage buckets[¶](#view-storage-buckets "Link to this heading")

CLI

UI

To list all available storage buckets in a storage pool, run:

    lxc storage bucket list <pool-name>

To show detailed information about a specific bucket, run:

    lxc storage bucket show <pool-name> <bucket-name>

Select [Buckets] from the [Storage] section of the main navigation.

[]

## Create a storage bucket[¶](#create-a-storage-bucket "Link to this heading")

[]

### Requirements[¶](#requirements "Link to this heading")

Storage buckets can only be created in storage pools that use a driver capable of **object storage**. View the [[Storage buckets]](../../explanation/storage/#storage-buckets) reference guide's [[Feature comparison]](../../reference/storage_drivers/#storage-drivers-features) table to see which drivers support object storage.

Other requirements must be met before you can create a storage bucket, depending on whether you want to create a distributed or local storage bucket.

[]

#### Distributed storage buckets[¶](#distributed-storage-buckets "Link to this heading")

To create a distributed storage bucket, your LXD server must have access to a [[Ceph Object]](../../reference/storage_cephobject/#storage-cephobject) storage pool.

CLI

UI

To view available storage pools, run:

    lxc storage list

If you see a storage pool in the output with the [`cephobject`] driver, you're all set. Continue on to the instructions below to [[create a storage bucket]](#howto-storage-buckets-create-single).

If you don't see a pool that uses a [`cephobject`] storage driver, you must create one before you can continue. This requires a [Ceph](https://ceph.io) cluster with a RADOS Gateway ([`radosgw`]) enabled. See our how-to guide for storage pools: [[Requirements for Ceph-based storage pools]](../storage_pools/#howto-storage-pools-ceph-requirements).

To create a storage bucket, select [Buckets] from the [Storage] section of the main navigation.

On the resulting screen, click [Create bucket] in the upper-right corner.

In the form that appears, set a unique name for the storage bucket and select a storage pool. You can optionally configure the bucket's size and description.

Finally, click [Create bucket].

<figure class="align-default">
<a href="../../_images/storage_bucket_create.png" class="reference internal image-reference"><img src="../../_images/storage_bucket_create.png" style="width: 60%;" alt="Create Storage Buckets in LXD UI" /></a>
</figure>

[]

#### Local storage buckets[¶](#local-storage-buckets "Link to this heading")

[]

##### MinIO[¶](#minio "Link to this heading")

LXD uses [MinIO](https://www.min.io/) to set up local storage buckets. To use this feature with LXD, you must install both the server and client binaries.

-   MinIO Server:

    -   Source:

        -   [MinIO Server on GitHub](https://github.com/minio/minio)

    -   Direct download for various architectures:

        -   [MinIO Server pre-built for [`amd64`]](https://dl.min.io/server/minio/release/linux-amd64/minio)

        -   [MinIO Server pre-built for [`arm64`]](https://dl.min.io/server/minio/release/linux-arm64/minio)

        -   [MinIO Server pre-built for [`arm`]](https://dl.min.io/server/minio/release/linux-arm/minio)

        -   [MinIO Server pre-built for [`ppc64le`]](https://dl.min.io/server/minio/release/linux-ppc64le/minio)

        -   [MinIO Server pre-built for [`s390x`]](https://dl.min.io/server/minio/release/linux-s390x/minio)

-   MinIO Client:

    -   Source:

        -   [MinIO Client on GitHub](https://github.com/minio/mc)

    -   Direct download for various architectures:

        -   [MinIO Client pre-built for [`amd64`]](https://dl.min.io/client/mc/release/linux-amd64/mc)

        -   [MinIO Client pre-built for [`arm64`]](https://dl.min.io/client/mc/release/linux-arm64/mc)

        -   [MinIO Client pre-built for [`arm`]](https://dl.min.io/client/mc/release/linux-arm/mc)

        -   [MinIO Client pre-built for [`ppc64le`]](https://dl.min.io/client/mc/release/linux-ppc64le/mc)

        -   [MinIO Client pre-built for [`s390x`]](https://dl.min.io/client/mc/release/linux-s390x/mc)

If LXD is installed from a Snap, you must configure the snap environment to detect the binaries, and restart LXD. Note that the path to the directory containing the binaries must not be under the home directory of any user.

    snap set lxd minio.path=/path/to/directory/containing/both/binaries
    snap restart lxd

If LXD is installed from another source, both binaries must be included in the [`$PATH`] that LXD was started with.

[]

##### Configure the S3 address[¶](#configure-the-s3-address "Link to this heading")

Storage buckets provide access to object storage exposed using the S3 protocol.

If you want to use storage buckets on local storage (thus in a [`dir`], [`btrfs`], [`lvm`], or [`zfs`] pool), you must configure the S3 address for your LXD server. This is the address that you can then use to access the buckets through the S3 protocol.

To configure the S3 address, set the [[`core.storage_buckets_address`]](../../server/#server-core:core.storage_buckets_address) server configuration option. For example:

    lxc config set core.storage_buckets_address :8555

[]

### Create a bucket on a single, non-clustered LXD server[¶](#create-a-bucket-on-a-single-non-clustered-lxd-server "Link to this heading")

To create a local or distributed storage bucket on a non-clustered LXD server, run:

    lxc storage bucket create <pool-name> <bucket-name> [configuration_options...]

See the [[Storage drivers]](../../reference/storage_drivers/#storage-drivers) documentation for a list of available storage bucket configuration options for each driver that supports object storage.

[]

### Create a bucket on a cluster member[¶](#create-a-bucket-on-a-cluster-member "Link to this heading")

#### Distributed storage buckets[¶](#id1 "Link to this heading")

Storage buckets created in [`cephobject`] storage pools are available from any LXD cluster member. Thus, to create this bucket, the command remains the same as for a non-clustered LXD server:

    lxc storage bucket create <pool-name> <bucket-name> [configuration_options...]

#### Local storage buckets[¶](#id2 "Link to this heading")

For local storage drivers, storage buckets are not replicated across the cluster and exist only on the member for which they were created. To create a storage bucket on a cluster member, add the [`--target`] flag:

    lxc storage bucket create <pool-name> <bucket-name> --target=<cluster-member> [configuration_options...]

[]

## Configure storage bucket settings[¶](#configure-storage-bucket-settings "Link to this heading")

See the [[Storage drivers]](../../reference/storage_drivers/#storage-drivers) documentation for the available configuration options for each storage driver that supports object storage.

CLI

UI

Use the following command to set configuration options for a storage bucket:

    lxc storage bucket set <pool-name> <bucket-name> <key> <value>

For example, to set the size (quota) of a bucket, use the following command:

    lxc storage bucket set my-pool my-bucket size 1MiB

You can also edit the storage bucket configuration by using the following command:

    lxc storage bucket edit <pool-name> <bucket-name>

Use the following command to delete a storage bucket and its keys:

    lxc storage bucket delete <pool-name> <bucket-name>

To configure a storage bucket, select [Buckets] from the [Storage] section of the main navigation.

The resulting screen shows a list of existing storage buckets. Click the [Edit] button on the row of the desired bucket to access its details.

After making changes, click the [Save changes] button. This button also displays the number of changes you have made.

[]

## Resize a storage bucket[¶](#resize-a-storage-bucket "Link to this heading")

By default, storage buckets do not have a quota applied.

CLI

UI

To set or change a quota for a storage bucket, set its size configuration:

    lxc storage bucket set <pool-name> <bucket-name> size <new-size>

Important

-   Growing a storage bucket usually works (if the storage pool has sufficient storage).

-   You cannot shrink a storage bucket below its current used size.

To configure a storage bucket, select [Buckets] from the [Storage] section of the main navigation.

The resulting screen shows a list of existing storage buckets. Change the quota of the bucket by changing the values in the [Size] fields.

After making changes, click the [Save changes] button. This button also displays the number of changes you have made.

[]

## Manage storage bucket keys[¶](#manage-storage-bucket-keys "Link to this heading")

To access a storage bucket, applications must use a set of S3 credentials made up of an *access key* and a *secret key*. You can create multiple sets of credentials for a specific bucket.

Each set of credentials is given a key name. The key name is used only for reference and does not need to be provided to the application that uses the credentials.

Each set of credentials has a *role* that specifies what operations they can perform on the bucket.

The roles available are:

-   [`admin`] - Full access to the bucket

-   [`read-only`] - Read-only access to the bucket (list and get files only)

If the role is not specified when creating a bucket key, the role used is [`read-only`].

[]

### View storage bucket keys[¶](#view-storage-bucket-keys "Link to this heading")

CLI

UI

Use the following command to see the keys defined for an existing bucket:

    lxc storage bucket key list <pool-name> <bucket-name>

Use the following command to see a specific bucket key:

    lxc storage bucket key show <pool-name> <bucket-name> <key-name>

To view storage bucket keys, select [Buckets] from the [Storage] section of the main navigation.

Click the name of a storage bucket to display its key management page, where you can view and manage a list of keys for that bucket.

<figure class="align-default">
<a href="../../_images/storage_bucket_key_list.png" class="reference internal image-reference"><img src="../../_images/storage_bucket_key_list.png" style="width: 80%;" alt="List Storage Bucket keys in LXD UI" /></a>
</figure>

[]

### Create keys[¶](#create-keys "Link to this heading")

CLI

UI

Use the following command to create a set of credentials for a storage bucket:

    lxc storage bucket key create <pool-name> <bucket-name> <key-name> [configuration_options...]

Use the following command to create a set of credentials for a storage bucket with a specific role:

    lxc storage bucket key create <pool-name> <bucket-name> <key-name> --role=admin [configuration_options...]

These commands will generate and display a random set of credential keys.

To create a storage bucket key, go to the [[key management page]](#howto-storage-buckets-keys-view) of the desired bucket.

On the resulting screen, click [Create key] in the upper-right corner.

In the form that appears, set a unique name for the key. You can optionally configure the role, description of your storage bucket key.

While you can enter values for the [Access] and [Secret Key] fields, this is not necessary. You can leave them blank, and LXD will generate random values for those credential keys.

Finally, click [Create key].

<figure class="align-default">
<a href="../../_images/storage_bucket_create_key.png" class="reference internal image-reference"><img src="../../_images/storage_bucket_create_key.png" style="width: 60%;" alt="Create Storage Bucket keys in LXD UI" /></a>
</figure>

[]

### Edit or delete storage bucket keys[¶](#edit-or-delete-storage-bucket-keys "Link to this heading")

CLI

UI

Use the following command to edit an existing bucket key:

    lxc storage bucket key edit <pool-name> <bucket-name> <key-name>

Use the following command to delete an existing bucket key:

    lxc storage bucket key delete <pool-name> <bucket-name> <key-name>

To edit or delete storage bucket keys, go to the [[key management page]](#howto-storage-buckets-keys-view) of the desired bucket.

From here, use the [Edit] or [Delete] button in the row of the target key.