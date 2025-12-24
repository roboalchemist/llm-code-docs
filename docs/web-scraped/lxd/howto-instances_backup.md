# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/instances_backup/

[]

# How to back up instances[¶](#how-to-back-up-instances "Link to this heading")

There are different ways of backing up your instances:

-   [[Use snapshots for instance backup]](#instances-snapshots)

-   [[Use export files for instance backup]](#instances-backup-export)

-   [[Copy an instance to a backup server]](#instances-backup-copy)

Which method to choose depends both on your use case and on the storage driver you use.

In general, snapshots are quick and space efficient (depending on the storage driver), but they are stored in the same storage pool as the instance and therefore not too reliable. Export files can be stored on different disks and are therefore more reliable. They can also be used to restore the instance into a different storage pool. If you have a separate, network-connected LXD server available, regularly copying instances to this other server gives high reliability as well, and this method can also be used to back up snapshots of the instance.

Note

Custom storage volumes might be attached to an instance, but they are not part of the instance. Therefore, the content of a custom storage volume is not stored when you back up your instance. You must back up the data of your storage volume separately. See [[How to back up custom storage volumes]](../storage_backup_volume/#howto-storage-backup-volume) for instructions.

[]

## Use snapshots for instance backup[¶](#use-snapshots-for-instance-backup "Link to this heading")

You can save your instance at a point in time by creating an instance snapshot, which makes it easy to restore the instance to a previous state.

Instance snapshots are stored in the same storage pool as the instance volume itself.

Most storage drivers support optimized snapshot creation (see [[Feature comparison]](../../reference/storage_drivers/#storage-drivers-features)). For these drivers, creating snapshots is both quick and space-efficient. For the [`dir`] driver, snapshot functionality is available but not very efficient. For the [`lvm`] driver, snapshot creation is quick, but restoring snapshots is efficient only when using thin-pool mode.

### Create a snapshot[¶](#create-a-snapshot "Link to this heading")

CLI

API

UI

Use the following command to create a snapshot of an instance:

    lxc snapshot <instance_name> [<snapshot name>]

The snapshot name is optional. If you don't specify one, the name follows the naming pattern defined in [`snapshots.pattern`].

Add the [`--reuse`] flag in combination with a snapshot name to replace an existing snapshot.

By default, snapshots are kept forever, unless the [`snapshots.expiry`] configuration option is set. To retain a specific snapshot even if a general expiry time is set, use the [`--no-expiry`] flag.

For virtual machines, you can add the [`--stateful`] flag to capture not only the data included in the instance volume but also the running state of the instance. Note that this feature is not fully supported for containers because of CRIU limitations.

By default, instance snapshots include a snapshot of the instance's root disk volume only. To include snapshots of attached storage volumes, set the [`--disk-volumes`] flag to "all-exclusive".

To create a snapshot of an instance, send a POST request to the [`snapshots`] endpoint:

    lxc query --request POST /1.0/instances/<instance_name>/snapshots --data ''

The snapshot name is optional. If you set it to an empty string, the name follows the naming pattern defined in [[`snapshots.pattern`]](../../reference/instance_options/#instance-snapshots:snapshots.pattern).

By default, snapshots are kept forever, unless the [[`snapshots.expiry`]](../../reference/instance_options/#instance-snapshots:snapshots.expiry) configuration option is set. To set an expiration date, add the[`expires_at`] field to the request data. To retain a specific snapshot even if a general expiry time is set, set the [`expires_at`] field to [`"0001-01-01T00:00:00Z"`].

If you want to replace an existing snapshot, [[delete it]](#instances-snapshots-delete) first and then create another snapshot with the same name.

For virtual machines, you can add [`"stateful":`]` `[`true`] to the request data to capture not only the data included in the instance volume but also the running state of the instance. Note that this feature is not fully supported for containers because of CRIU limitations.

By default, instance snapshots include a snapshot of the instance's root disk volume only. To include snapshots of attached storage volumes, set the [`disk_volumes_mode`] flag to "all-exclusive" in the request data.

See [[`POST`]` `[`/1.0/instances//snapshots`]](/lxd/latest/api/#/instances/instance_snapshots_post) for more information.

To create a snapshot of an instance, go to the instance detail page and switch to the [Snapshots] tab. Click [Create snapshot] to open the dialog to create a snapshot.

The snapshot name is optional. If you don't specify one, the name follows the naming pattern defined in [[`snapshots.pattern`]](../../reference/instance_options/#instance-snapshots:snapshots.pattern). You can check and update this option by switching to the [Configuration] tab and selecting [Advanced] \> [Snapshots], or simply by clicking [See configuration].

By default, snapshots are kept forever, unless you specify an expiry date and time, or the [[`snapshots.expiry`]](../../reference/instance_options/#instance-snapshots:snapshots.expiry) configuration option is set for the instance.

For virtual machines, you can choose to create a stateful snapshot to capture not only the data included in the instance volume but also the running state of the instance. Note that this feature requires [[`migration.stateful`]](../../reference/instance_options/#instance-migration:migration.stateful) to be enabled.

[]

### View, edit or delete snapshots[¶](#view-edit-or-delete-snapshots "Link to this heading")

CLI

API

UI

Use the following command to display the snapshots for an instance:

    lxc info <instance_name>

You can view or modify snapshots in a similar way to instances, by referring to the snapshot with [`<instance_name>/<snapshot_name>`].

To show configuration information about a snapshot, use the following command:

    lxc config show <instance_name>/<snapshot_name>

To change the expiry date of a snapshot, use the following command:

    lxc config edit <instance_name>/<snapshot_name>

Note

In general, snapshots cannot be edited, because they preserve the state of the instance. The only exception is the expiry date. Other changes to the configuration are silently ignored.

To delete a snapshot, use the following command:

    lxc delete <instance_name>/<snapshot_name>

By default, only the instance's root disk volume snapshot is deleted. To also delete snapshots of attached storage volumes, set the [`--disk-volumes`] flag to "all-exclusive".

To retrieve the snapshots for an instance, send a GET request to the [`snapshots`] endpoint:

    lxc query --request GET /1.0/instances/<instance_name>/snapshots

To show configuration information about a snapshot, send the following request:

    lxc query --request GET /1.0/instances/<instance_name>/snapshots/<snapshot_name>

To change the expiry date of a snapshot, send a PATCH request:

    lxc query --request PATCH /1.0/instances/<instance_name>/snapshots/<snapshot_name> --data ''

Note

In general, snapshots cannot be modified, because they preserve the state of the instance. The only exception is the expiry date. Other changes to the configuration are silently ignored.

To delete a snapshot, send a DELETE request:

    lxc query --request DELETE /1.0/instances/<instance_name>/snapshots/<snapshot_name>

By default, only the instance's root disk volume snapshot is deleted. To also delete snapshots of attached storage volumes, set the [`disk-volumes`] query parameter to "all-exclusive" in the request.

See [[`GET`]` `[`/1.0/instances//snapshots`]](/lxd/latest/api/#/instances/instance_snapshots_get), [[`GET`]` `[`/1.0/instances//snapshots/`]](/lxd/latest/api/#/instances/instance_snapshot_get), [[`PATCH`]` `[`/1.0/instances//snapshots/`]](/lxd/latest/api/#/instances/instance_snapshot_patch), and [[`DELETE`]` `[`/1.0/instances//snapshots/`]](/lxd/latest/api/#/instances/instance_snapshot_delete) for more information.

To see all snapshots for an instance, go to the instance detail page and switch to the [Snapshots] tab.

From the snapshot list, you can choose to edit the name or expiry date of a specific snapshot, create an image based on the snapshot, restore it to the instance, or delete it.

### Schedule instance snapshots[¶](#schedule-instance-snapshots "Link to this heading")

You can configure an instance to automatically create snapshots at specific times (at most once every minute). To do so, set the [[`snapshots.schedule`]](../../reference/instance_options/#instance-snapshots:snapshots.schedule) instance option.

For example, to configure daily snapshots:

CLI

API

UI

    lxc config set <instance_name> snapshots.schedule @daily

    lxc query --request PATCH /1.0/instances/<instance_name> --data '
    }'

<figure class="align-default">
<a href="../../_images/snapshots_daily.png" class="reference internal image-reference"><img src="../../_images/snapshots_daily.png" style="width: 80%;" alt="Configure daily snapshots" /></a>
</figure>

To configure taking a snapshot every day at 6 am:

CLI

API

UI

    lxc config set <instance_name> snapshots.schedule "0 6 * * *"

    lxc query --request PATCH /1.0/instances/<instance_name> --data '
    }'

<figure class="align-default">
<a href="../../_images/snapshots_cron.png" class="reference internal image-reference"><img src="../../_images/snapshots_cron.png" style="width: 80%;" alt="Configure snapshots daily at 6am" /></a>
</figure>

When scheduling regular snapshots, consider setting an automatic expiry ([[`snapshots.expiry`]](../../reference/instance_options/#instance-snapshots:snapshots.expiry)) and a naming pattern for snapshots ([[`snapshots.pattern`]](../../reference/instance_options/#instance-snapshots:snapshots.pattern)). You should also configure whether you want to take snapshots of instances that are not running ([[`snapshots.schedule.stopped`]](../../reference/instance_options/#instance-snapshots:snapshots.schedule.stopped)).

### Restore an instance snapshot[¶](#restore-an-instance-snapshot "Link to this heading")

You can restore an instance to any of its snapshots.

CLI

API

UI

To restore an instance to a snapshot, use the following command:

    lxc restore <instance_name> <snapshot_name>

If the snapshot is stateful (which means that it contains information about the running state of the instance), you can add the [`--stateful`] flag to restore the state.

By default, instance snapshot restores include a snapshot of the instance's root disk volume only. To also restore snapshots of attached storage volumes, set the [`--disk-volumes`] flag to "all-exclusive".

To restore an instance to a snapshot, send a PUT request to the instance:

    lxc query --request PUT /1.0/instances/<instance_name> --data ''

If the snapshot is stateful (which means that it contains information about the running state of the instance), you can add [`"stateful":`]` `[`true`] to the request data:

    lxc query --request PUT /1.0/instances/<instance_name> --data ''

By default, instance snapshot restores include a snapshot of the instance's root disk volume only. To also restore snapshots of attached storage volumes, set the [`restore_disk_volumes_mode`] flag to "all-exclusive" in the request data.

See [[`PUT`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_put) for more information.

To restore an instance to a snapshot, click the [Restore snapshot] button (![](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjE2IiB3aWR0aD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTUuOTQ4IDkuMDEydjEuNWwtMi40NTguMDAxQTUuMTYzIDUuMTYzIDAgMDAxMi43NiAxMGgxLjU5NmE2LjY2NSA2LjY2NSAwIDAxLTExLjgzOSAxLjc4NXYyLjE1OGgtMS41di00LjkzaDQuOTN6TTggMS4zMzhhNi42NTUgNi42NTUgMCAwMTUuNTE2IDIuOTI1VjIuMTFoMS41djQuOTNoLTQuOTN2LTEuNWgyLjQ1M0E1LjE2MyA1LjE2MyAwIDAwMy4yNCA2SDEuNjQzQTYuNjY1IDYuNjY1IDAgMDE4IDEuMzM4eiIgZmlsbD0iJTIzMDAwIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjwvcGF0aD48L3N2Zz4=)) next to the snapshot that you want to restore.

If the snapshot is stateful (which means that it contains information about the running state of the instance), select [Restore the instance state] if you want to restore the state.

[]

## Use export files for instance backup[¶](#use-export-files-for-instance-backup "Link to this heading")

You can export the full content of your instance to a standalone file that can be stored at any location. For highest reliability, store the backup file on a different file system to ensure that it does not get lost or corrupted.

Note

The UI does not currently support exporting and importing instances.

[]

### Export an instance[¶](#export-an-instance "Link to this heading")

CLI

API

UI

Use the following command to export an instance to a compressed file (for example, [`/path/to/my-instance.tgz`]):

    lxc export <instance_name> [<file_path>]

If you do not specify a file path, the export file is saved as [`<instance_name>.<extension>`] in the working directory (for example, [`my-container.tar.gz`]).

Warning

If the output file ([`<instance_name>.<extension>`] or the specified file path) already exists, the command overwrites the existing file without warning.

You can add any of the following flags to the command:

[`--compression`]

:   By default, the output file uses [`gzip`] compression. You can specify a different compression algorithm (for example, [`bzip2`]) or turn off compression with [`--compression=none`].

[`--optimized-storage`]

:   If your storage pool uses the [`btrfs`] or the [`zfs`] driver, add the [`--optimized-storage`] flag to store the data as a driver-specific binary blob instead of an archive of individual files. In this case, the export file can only be used with pools that use the same storage driver.

    Exporting a volume in optimized mode is usually quicker than exporting the individual files. Snapshots are exported as differences from the main volume, which decreases their size (quota) and makes them easily accessible.

[`--export-version`]

:   If you intend to import the backup to an older version of LXD, set the version to [`1`] which will use the original (old) backup metadata format. Backups using the old format can always be imported on newer versions of LXD. If the flag is not specified and the server has support for the [`backup_metadata_version`] API extension, version [`2`] is used by default.

```
<!-- -->
```

[`--instance-only`]

:   By default, the export file contains all snapshots of the instance. Add this flag to export the instance without its snapshots.

To create a backup of an instance, send a POST request to the [`backups`] endpoint:

    lxc query --request POST /1.0/instances/<instance_name>/backups --data ''

You can specify a name for the backup, or use the default ([`backup0`], [`backup1`] and so on).

You can add any of the following fields to the request data:

[`"compression_algorithm":`]` `[`"bzip2"`]

:   By default, the output file uses [`gzip`] compression. You can specify a different compression algorithm (for example, [`bzip2`]) or turn off compression with [`none`].

[`"optimized-storage":`]` `[`true`]

:   If your storage pool uses the [`btrfs`] or the [`zfs`] driver, set the [`"optimized-storage"`] field to [`true`] to store the data as a driver-specific binary blob instead of an archive of individual files. In this case, the backup can only be used with pools that use the same storage driver.

    Exporting a volume in optimized mode is usually quicker than exporting the individual files. Snapshots are exported as differences from the main volume, which decreases their size (quota) and makes them easily accessible.

[`"instance-only":`]` `[`true`]

:   By default, the backup contains all snapshots of the instance. Set this field to [`true`] to back up the instance without its snapshots.

After creating the backup, you can download it with the following request:

    lxc query --request GET /1.0/instances/<instance_name>/backups/<backup_name>/export > <file_name>

Remember to delete the backup when you don't need it anymore:

    lxc query --request DELETE /1.0/instances/<instance_name>/backups/<backup_name>

See [[`POST`]` `[`/1.0/instances//backups`]](/lxd/latest/api/#/instances/instance_backups_post), [[`GET`]` `[`/1.0/instances//backups//export`]](/lxd/latest/api/#/instances/instance_backup_export), and [[`DELETE`]` `[`/1.0/instances//backups/`]](/lxd/latest/api/#/instances/instance_backup_delete) for more information.

From the instance detail page, click [Export].

Modify the default settings if necessary, then export the instance.

Download will start automatically once the export is ready.

[]

### Restore an instance from an export file[¶](#restore-an-instance-from-an-export-file "Link to this heading")

You can import an export file (for example, [`/path/to/my-backup.tgz`]) as a new instance.

CLI

API

UI

To import an export file, use the following command:

    lxc import <file_path> [<instance_name>]

If you do not specify an instance name, the original name of the exported instance is used for the new instance. If an instance with that name already (or still) exists in the specified storage pool, the command returns an error. In that case, either delete the existing instance before importing the backup or specify a different instance name for the import.

Add the [`--storage`] flag to specify which storage pool to use, or the [`--device`] flag to override the device configuration (syntax: [`--device`]` `[`<device_name>,<device_option>=<value>`]).

To import an export file, post it to the [`/1.0/instances`] endpoint:

    curl -X POST -H "Content-Type: application/octet-stream" --data-binary @<file_path> \
    --unix-socket /var/snap/lxd/common/lxd/unix.socket lxd/1.0/instances

If an instance with that name already (or still) exists in the specified storage pool, the command returns an error. In this case, delete the existing instance before importing the backup.

See [[`POST`]` `[`/1.0/instances`]](/lxd/latest/api/#/instances/instances_post) for more information.

To import an export file, go to the instance list and click [Create instance].

From the resulting modal, upload the instance file. The instance name and description fields are optional. If you don't specify the instance name, the name of the export file is used, appended with [`-tar-import`].

Click [Choose file]. Select the export file, then click [Upload and create].

The newly created instance will appear in the instance list.

[]

## Copy an instance to a backup server[¶](#copy-an-instance-to-a-backup-server "Link to this heading")

You can copy an instance to a secondary backup server to back it up.

See [[Secondary backup LXD server]](../../backup/#secondary-backup-server) for more information, and [[How to migrate LXD instances between servers]](../instances_migrate/#howto-instances-migrate) for instructions.