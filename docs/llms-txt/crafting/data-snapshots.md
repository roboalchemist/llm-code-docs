<!-- Source: https://docs.sandboxes.cloud/docs/data-snapshots.md -->

# Save and load data snapshots

In this page, we describe how to use data snapshots to help your development. A `Data Snapshot` (a.k.a. `Dependency Snapshot` or `Container Snapshot`) is to capture the filesystem state of a dependency or a custom container.

Note that for built-in dependencies, such as `postgres`, `redis`, etc., Crafting platform will automatically save the data. But for custom containers, a snapshot can be taken only to save the defined `Volume` mounted on the container. Typically for a stateful service released as a container, there is clear documentation on where is the persistent data should should be stored.

In the remainder of this page, we will cover:

* [How to save data as a data snapshot](#how-to-save-data-as-a-data-snapshot)
* [How to load a data snapshot](#how-to-load-a-data-snapshot)
* [Admin guide: setup default data snapshot in template](#admin-guide-setup-default-data-snapshot-in-template)

## How to save data as a data snapshot

To take a data snapshot for a dependency or container, we can do it directly on the web console, as shown below.

<Image align="center" className="border" border={true} src="https://files.readme.io/6150910-guide-data-snapshot-take.jpg" />

After clicking the save snapshot button highlighted above, we can input the name of the snapshot and click `Confirm` to save it.

<Image align="center" width="80% " src="https://files.readme.io/5ea959d-image.png" />

During saving of the snapshot, it would temporarily bring the service offline and restart the service when the snapshot is successfully taken. Then the snapshot will show up under the `Resource -> Snapshots` page from the menu.

<Image align="center" className="border" border={true} src="https://files.readme.io/e5a859c-image.png" />

We can also take a snapshot using CLI command `cs snapshot create` as follows

```shell
$ cs snapshot create <SNAPSHOT-NAME> -W [DEPENDENCY|CONTAINER]
```

## How to load a data snapshot

To load a data snapshot into an existing sandbox, it can be done via web console as follows

<Image align="center" className="border" border={true} src="https://files.readme.io/3360943-guide-data-snapshot-restore.jpg" />

After clicking the restore snapshot button highlighted above, we can select the snapshot to load and click `Confirm` to load the snapshot into the sandbox.

![](https://files.readme.io/0c79e7c-image.png)

Note that the existing data for the target service in the sandbox will be overwritten by the snapshot. And during the restore, the service will be brought down for some time. Also please keep in mind that sometimes the data format used in one version of the database are not compatible with another version, using an incompatible data snapshot may not be able to launch the service properly.

We can also restore a snapshot using CLI command `cs snapshot restore` as follows

```shell
$ cs snapshot restore <SNAPSHOT-NAME> -W [DEPENDENCY|CONTAINER]
```

To load a snapshot in a new sandbox, we can simply select the snapshot in the drop down from the customization page. This way, we can select a snapshot other than the default one specified in the Template.

<Image align="center" className="border" border={true} src="https://files.readme.io/9d59a52-guide_create_customize_data_snapshot.jpg" />

### Admin guide: setup default data snapshot in template

A default data snapshot can be set for a dependency or container to preload the newly created sandbox with standard test data by default. After a snapshot is taken from a sandbox, we can modify the Template to use a snapshot by default. It can be done from web console

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/36b2bc5-image.png" />

Or in the yaml file of the [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition)

```yaml
dependencies:
  - name: mysql
    service_type: mysql
    snapshot: snapshot-mysql
```
