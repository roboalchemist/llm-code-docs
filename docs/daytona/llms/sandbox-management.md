# Source: https://www.daytona.io/docs/en/sandbox-management.md

import Image from 'astro/components/Image.astro'

Sandboxes are isolated development environments managed by Daytona. This guide covers how to create, manage, and remove Sandboxes using the SDK.
By default, Sandboxes auto-stop after 15 minutes of inactivity and use **1 vCPU**, **1GB RAM**, and **3GiB disk**.

## Sandbox Lifecycle

Throughout its lifecycle, a Daytona Sandbox can have several different states. The diagram below shows the states and possible transitions between them.

<Fragment set:html={sandboxDiagram} />

By default, sandboxes auto-stop after `15 minutes` of inactivity and auto-archive after `7 days` of being stopped. To keep the Sandbox running indefinitely without interruption, set the auto-stop value to `0` during creation.

## Creating Sandboxes

The Daytona SDK provides an option to create Sandboxes with default or custom configurations. You can specify the language, [Snapshot](https://www.daytona.io/docs/en/snapshots.md), resources, environment variables, and volumes for the Sandbox.
Running Sandboxes utilize CPU, memory, and disk storage. Every resource is charged per second of usage.

:::tip
If you want to prolong the auto-stop interval, you can [set the auto-stop interval parameter](https://www.daytona.io/docs/en/sandbox-management.md#auto-stop-interval) when creating a Sandbox.
:::

### Basic Sandbox Creation

The Daytona SDK provides methods to create Sandboxes with default configurations, specific languages, custom names, or custom labels using Python and TypeScript.

    ```python
    from daytona import Daytona, CreateSandboxFromSnapshotParams

    daytona = Daytona()

    # Create a basic Sandbox

    sandbox = daytona.create()

    # Create a Sandbox with specific language

    params = CreateSandboxFromSnapshotParams(language="python")
    sandbox = daytona.create(params)

    # Create a Sandbox with a custom name

    params = CreateSandboxFromSnapshotParams(name="my-sandbox")
    sandbox = daytona.create(params)

    # Create a Sandbox with custom labels

    params = CreateSandboxFromSnapshotParams(labels={"SOME_LABEL": "my-label"})
    sandbox = daytona.create(params)

    ```


    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona();

    // Create a basic Sandbox
    const sandbox = await daytona.create();

    // Create a Sandbox with specific language
    const sandbox = await daytona.create({ language: 'typescript' });

    // Create a Sandbox with a custom name
    const sandbox = await daytona.create({ name: 'my-sandbox' });

    // Create a Sandbox with custom labels
    const sandbox = await daytona.create({ labels: { SOME_LABEL: 'my-label' } });
    ```


:::note
**Sandbox Names**: You can specify a custom name for your sandbox using the `name` parameter. If not provided, the sandbox ID will be used as the name. Sandbox names are reusable - once a sandbox with a specific name is destroyed, that name becomes available for use again.
:::

See: [create (Python SDK)](https://www.daytona.io/docs/en/python-sdk/sync/daytona.md#daytonacreate), [create (TypeScript SDK)](https://www.daytona.io/docs/en/typescript-sdk/daytona.md#create)

When Sandboxes are not actively used, it is recommended that they be stopped. This can be done manually [using the stop command](https://www.daytona.io/docs/en/sandbox-management.md#stop-and-start-sandbox) or automatically by [setting the auto-stop interval](https://www.daytona.io/docs/en/sandbox-management.md#auto-stop-and-auto-archive).

:::note
Daytona keeps a pool of warm Sandboxes using default Snapshots.\
When available, your Sandbox will launch in milliseconds instead of cold-booting.
:::

### Sandbox Resources

Daytona Sandboxes come with **1 vCPU**, **1GB RAM**, and **3GiB disk** by default.

Use the `Resources` class to define exactly what you need: CPU, memory, and disk space are all customizable.

Organizations get a maximum Sandbox resource limit of 4 vCPUs, 8GB RAM, and 10GB disk. Need more power? Contact [support@daytona.io](mailto:support@daytona.io) and let us know your use case.

Check your available resources and limits in the [dashboard](https://app.daytona.io/dashboard/limits).

    ```python
    from daytona import Daytona, Resources, CreateSandboxFromImageParams, Image

    daytona = Daytona()

    # Create a Sandbox with custom resources

    resources = Resources(
        cpu=2,  # 2 CPU cores
        memory=4,  # 4GB RAM
        disk=8,  # 8GB disk space
    )

    params = CreateSandboxFromImageParams(
        image=Image.debian_slim("3.12"),
        resources=resources
    )

    sandbox = daytona.create(params)

    ```


    ```typescript
    import { Daytona, Image } from "@daytonaio/sdk";

    async function main() {
      const daytona = new Daytona();

      // Create a Sandbox with custom resources
      const sandbox = await daytona.create({
        image: Image.debianSlim("3.13"),
        resources: {
          cpu: 2, // 2 CPU cores
          memory: 4, // 4GB RAM
          disk: 8, // 8GB disk space
        },
      });
    }

    main();
    ```


:::note
All resource parameters are optional. If not specified, Daytona will use default values appropriate for the selected language and use case.
:::

### Ephemeral Sandboxes

Ephemeral Sandboxes are Sandboxes that are automatically deleted once they are stopped. They are useful for short-lived tasks or for testing purposes.

To create an ephemeral Sandbox, set `ephemeral` to `True` when creating a Sandbox:

    ```python
    from daytona import Daytona, CreateSandboxFromSnapshotParams

    daytona = Daytona()

    # Create an ephemeral Sandbox

    params = CreateSandboxFromSnapshotParams(
      ephemeral=True,
      auto_stop_interval=5 # the ephemeral sandbox will be deleted after 5 minutes of inactivity
    )
    sandbox = daytona.create(params)
    ```


    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona();

    // Create an ephemeral Sandbox
    const sandbox = await daytona.create({
      ephemeral: true,
      autoStopInterval: 5 // the ephemeral sandbox will be deleted after 5 minutes of inactivity
    });
    ```


:::note
Setting ["autoDeleteInterval: 0"](#auto-delete-interval) has the same effect as setting "ephemeral" to `true`.
:::

### Network Settings (Firewall)

Daytona Sandboxes provide configurable network firewall controls to enhance security and manage connectivity. By default, network access follows standard security policies, but you can customize network settings when creating a Sandbox.
Learn more about network limits in the [Network Limits](https://www.daytona.io/docs/en/network-limits.md) documentation.

## Sandbox Information

The Daytona SDK provides methods to get information about a Sandbox, such as ID, root directory, and status using Python and TypeScript.

    ```python
    # Get Sandbox ID
    sandbox_id = sandbox.id

    # Get the root directory of the Sandbox user

    root_dir = sandbox.get_user_root_dir()

    # Get the Sandbox id, auto-stop interval and state

    print(sandbox.id)
    print(sandbox.auto_stop_interval)
    print(sandbox.state)

    ```


    ```typescript
    // Get Sandbox ID
    const sandboxId = sandbox.id;

    // Get the root directory of the Sandbox user
    const rootDir = await sandbox.getUserRootDir();

    // Get the Sandbox id, auto-stop interval and state
    console.log(sandbox.id)
    console.log(sandbox.autoStopInterval)
    console.log(sandbox.state)
    ```


To get the preview URL for a specific port, check out [Preview & Authentication](https://www.daytona.io/docs/en/preview-and-authentication.md).

## Stop and Start Sandbox

The Daytona SDK provides methods to stop and start Sandboxes using Python and TypeScript.

Stopped Sandboxes maintain filesystem persistence while their memory state is cleared. They incur only disk usage costs and can be started again when needed.

    ```python
    sandbox = daytona.create(CreateSandboxParams(language="python"))

    # Stop Sandbox

    sandbox.stop()

    print(sandbox.id) # 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    # The sandbox ID can later be used to find the sandbox and start it

    sandbox = daytona.find_one("7cd11133-96c1-4cc8-9baa-c757b8f8c916")

    # Start Sandbox

    sandbox.start()

    ```


    ```typescript
    const sandbox = await daytona.create({ language: 'typescript' });

    // Stop Sandbox
    await sandbox.stop();

    console.log(sandbox.id) // 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    // The sandbox ID can later be used to find the sandbox and start it

    const sandbox = await daytona.findOne("7cd11133-96c1-4cc8-9baa-c757b8f8c916");

    // Start Sandbox
    await sandbox.start();
    ```


See: [stop (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstop), [start (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstart), [find_one (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/daytona.md#daytonafind_one), [stop (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#stop), [start (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#start), [findOne (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/daytona.md#findone)

The stopped state should be used when the Sandbox is expected to be started again soon. Otherwise, it is recommended to stop and then archive the Sandbox to eliminate disk usage costs.

## Archive Sandbox

The Daytona SDK provides methods to archive Sandboxes using Python and TypeScript.

When Sandboxes are archived, the entire filesystem state is moved to very cost-effective object storage, making it possible to keep Sandboxes available for an extended period.
Starting an archived Sandbox takes more time than starting a stopped Sandbox, depending on its size.

A Sandbox must be stopped before it can be archived, and can be started again in the same way as a stopped Sandbox.

    ```python
    # Archive Sandbox
    sandbox.archive()
    ```

    ```typescript
    // Archive Sandbox
    await sandbox.archive();
    ```

See: [archive (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxarchive), [archive (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#archive)

## Delete Sandbox

The Daytona SDK provides methods to delete Sandboxes using Python and TypeScript.

    ```python
    # Delete Sandbox
    sandbox.delete()
    ```

    ```typescript
    // Delete Sandbox
    await sandbox.delete();
    ```

See: [delete (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxdelete), [delete (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#delete)

:::tip
Check out the [Daytona CLI](https://www.daytona.io/docs/en/getting-started.md#setting-up-the-daytona-cli) if you prefer managing Sandboxes through the terminal:

```bash
daytona sandbox list
```

```text
Sandbox               State           Region        Last Event
───────────────────────────────────────────────────────────────────────────
ugliest_quokka        STARTED         us            1 hour ago

associated_yak        STARTED         us            14 hours ago

developed_lemur       STARTED         us            17 hours ago
```

```bash
daytona sandbox start|stop|remove --all
```

```text
All sandboxes have been deleted
```

:::

## Automated Lifecycle Management

Daytona Sandboxes can be automatically stopped, archived, and deleted based on user-defined intervals.

### Auto-stop Interval

The auto-stop interval parameter sets the amount of time after which a running Sandbox will be automatically stopped.

Sandbox activity, such as SDK API calls or network requests through [preview URLs](https://www.daytona.io/docs/en/preview-and-authentication.md), will reset the auto-stop timer.

The parameter can either be set to:

- a time interval in minutes
- `0`, which disables the auto-stop functionality, allowing the sandbox to run indefinitely

If the parameter is not set, the default interval of `15` minutes will be used.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_stop_interval=0,  # Disables the auto-stop feature - default is 15 minutes
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoStopInterval: 0, // Disables the auto-stop feature - default is 15 minutes
    });
    ```

### Auto-archive Interval

The auto-archive interval parameter sets the amount of time after which a continuously stopped Sandbox will be automatically archived.

The parameter can either be set to:

- a time interval in minutes
- `0`, which means the maximum interval of `30 days` will be used

If the parameter is not set, the default interval of `7 days` days will be used.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_archive_interval=60 # Auto-archive after a Sandbox has been stopped for 1 hour
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoArchiveInterval: 60 // Auto-archive after a Sandbox has been stopped for 1 hour
    });
    ```

### Auto-delete Interval

The auto-delete interval parameter sets the amount of time after which a continuously stopped Sandbox will be automatically deleted. By default, Sandboxes will never be automatically deleted.

The parameter can either be set to:

- a time interval in minutes
- `-1`, which disables the auto-delete functionality
- `0`, which means the Sandbox will be deleted immediately after stopping

If the parameter is not set, the Sandbox will not be deleted automatically.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_delete_interval=60,  # Auto-delete after a Sandbox has been stopped for 1 hour
    ))

    # Delete the Sandbox immediately after it has been stopped

    sandbox.set_auto_delete_interval(0)

    # Disable auto-deletion

    sandbox.set_auto_delete_interval(-1)

    ```


    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoDeleteInterval: 60, // Auto-delete after a Sandbox has been stopped for 1 hour
    });

    // Delete the Sandbox immediately after it has been stopped
    await sandbox.setAutoDeleteInterval(0)

    // Disable auto-deletion
    await sandbox.setAutoDeleteInterval(-1)
    ```


## Run Indefinitely

By default, Sandboxes auto-stop after 15 minutes of inactivity. To keep a Sandbox running without interruption, set the auto-stop interval to `0` when creating a new Sandbox:

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_stop_interval=0,  # Disables the auto-stop feature - default is 15 minutes
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoStopInterval: 0, // Disables the auto-stop feature - default is 15 minutes
    });
    ```