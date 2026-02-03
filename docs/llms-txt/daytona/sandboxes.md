# Source: https://www.daytona.io/docs/en/sandboxes.md

Sandboxes are isolated runtime environments managed by Daytona. This guide covers the lifecycle of Sandboxes and how to create, manage, and remove them using the Daytona SDK.

Daytona Sandboxes use **1 vCPU**, **1GB RAM**, and **3GiB disk** by default.
[Organizations](https://www.daytona.io/docs/en/organizations.md) get a maximum sandbox resource limit of **4 vCPUs**, **8GB RAM**, and **10GB disk**.
For more power, contact [support@daytona.io](mailto:support@daytona.io).

## Sandbox lifecycle

Throughout its lifecycle, a Daytona Sandbox can have several different states.
The diagram below shows the states and possible transitions between them.

<SandboxDiagram />

## Multiple runtime support

Daytona Sandboxes support Python, TypeScript, and JavaScript programming language runtimes for direct code execution inside the sandbox.

The `language` parameter controls which programming language runtime is used for the sandbox:

- **`python`**
- **`typescript`**
- **`javascript`**

If omitted, the Daytona SDK will default to `python`. To override this, explicitly set the `language` value when creating the sandbox.

:::note
**Sandbox Names**: You can specify a custom name for your sandbox using the `name` parameter. If not provided, the sandbox ID will be used as the name. Sandbox names are reusable - once a sandbox with a specific name is destroyed, that name becomes available for use again.
:::

## Create Sandboxes

Daytona provides options to programmatically create sandboxes with default or custom configurations.
You can specify [programming language runtime](https://www.daytona.io/docs/sandboxes.md#multiple-runtime-support), [snapshots](https://www.daytona.io/docs/snapshots.md), [resources](https://www.daytona.io/docs/sandboxes.md#resources), [environment variables](https://www.daytona.io/docs/configuration.md#environment-variables), and [volumes](https://www.daytona.io/docs/volumes.md) for each sandbox.
Running sandboxes utilize CPU, memory, and disk storage. Every resource is charged per second of usage.

    ```python
    from daytona import Daytona, CreateSandboxFromSnapshotParams

    daytona = Daytona()

    # Create a sandbox
    sandbox = daytona.create()

    # Create a sandbox with python
    params = CreateSandboxFromSnapshotParams(language="python")
    sandbox = daytona.create(params)

    # Create a sandbox with a custom name
    params = CreateSandboxFromSnapshotParams(name="my_awesome_sandbox")
    sandbox = daytona.create(params)

    # Create a sandbox with custom labels
    params = CreateSandboxFromSnapshotParams(labels={"LABEL": "label"})
    sandbox = daytona.create(params)
    ```

    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona();

    // Create a sandbox
    const sandbox = await daytona.create();

    // Create a sandbox with typescript
    const sandbox = await daytona.create({ language: 'typescript' });

    // Create a sandbox with a custom name
    const sandbox = await daytona.create({ name: 'my_awesome_sandbox' });

    // Create a sandbox with custom labels
    const sandbox = await daytona.create({ labels: { LABEL: 'label' } });
    ```


    ```ruby
    require 'daytona'

    daytona = Daytona::Daytona.new

    # Create a sandbox
    sandbox = daytona.create

    # Create a sandbox with python
    params = Daytona::CreateSandboxFromSnapshotParams.new(language: Daytona::CodeLanguage::PYTHON)
    sandbox = daytona.create(params)

    # Create a sandbox with a custom name
    params = Daytona::CreateSandboxFromSnapshotParams.new(name: 'my_awesome_sandbox')
    sandbox = daytona.create(params)

    # Create a sandbox with custom labels
    params = Daytona::CreateSandboxFromSnapshotParams.new(labels: { 'LABEL' => 'label' })
    sandbox = daytona.create(params)
    ```


To get the preview URL for a specific port, check out [Preview & Authentication](https://www.daytona.io/docs/en/preview-and-authentication.md).

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk.md) references:

> [**create (Python SDK)**](https://www.daytona.io/docs/en/python-sdk/sync/daytona.md#daytonacreate)
>
> [**create (TypeScript SDK)**](https://www.daytona.io/docs/en/typescript-sdk/daytona.md#create)
>
> [**create (Ruby SDK)**](https://www.daytona.io/docs/en/ruby-sdk/daytona.md#create)

### Resources

Daytona Sandbox uses **1 vCPU**, **1GB RAM**, and **3GiB disk** by default.

Daytona keeps a pool of warm sandboxes using default snapshots.
When available, sandboxes launch within milliseconds instead of cold-booting.

To set custom sandbox resources (CPU, memory, and disk space), use the `Resources` class:

    ```python
    from daytona import Daytona, Resources, CreateSandboxFromImageParams, Image

    daytona = Daytona()

    # Create a sandbox with custom resources
    resources = Resources(
        cpu=2,    # 2 CPU cores
        memory=4, # 4GB RAM
        disk=8,   # 8GB disk space
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

      // Create a sandbox with custom resources
      const sandbox = await daytona.create({
        image: Image.debianSlim("3.13"),
        resources: {
          cpu: 2,     // 2 CPU cores
          memory: 4,  // 4GB RAM
          disk: 8,    // 8GB disk space
        },
      });
    }

    main();
    ```


    ```ruby
    require 'daytona'

    daytona = Daytona::Daytona.new

    # Create a sandbox with custom resources
    sandbox = daytona.create(
      Daytona::CreateSandboxFromImageParams.new(
        image: Daytona::Image.debian_slim('3.12'),
        resources: Daytona::Resources.new(
          cpu: 2,     # 2 CPU cores
          memory: 4,  # 4GB RAM
          disk: 8     # 8GB disk space
        )
      )
    )
    ```


All resource parameters are optional. If not specified, Daytona will use default values appropriate for the selected language and use case.

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk/sync/daytona.md#resources), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk/daytona.md#resources), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk/daytona.md#resources) references:

> [**Resources (Python SDK)**](https://www.daytona.io/docs/en/python-sdk/sync/sandbox.md#resources)
>
> [**Resources (TypeScript SDK)**](https://www.daytona.io/docs/en/typescript-sdk/snapshot.md#createsnapshotparams)

### Ephemeral Sandboxes

Ephemeral Sandboxes are automatically deleted once they are stopped. They are useful for short-lived tasks or for testing purposes.

To create an ephemeral Sandbox, set the `ephemeral` parameter to `True` when creating a sandbox:

    ```python
    from daytona import Daytona, CreateSandboxFromSnapshotParams

    daytona = Daytona()

    # Create an ephemeral Sandbox
    params = CreateSandboxFromSnapshotParams(
      ephemeral=True,
      auto_stop_interval=5 # The ephemeral sandbox will be deleted after 5 minutes of inactivity
    )
    sandbox = daytona.create(params)
    ```


    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona();

    // Create an ephemeral sandbox
    const sandbox = await daytona.create({
      ephemeral: true,
      autoStopInterval: 5 // The ephemeral sandbox will be deleted after 5 minutes of inactivity
    });
    ```


    ```ruby
    require 'daytona'

    daytona = Daytona::Daytona.new

    # Create an ephemeral Sandbox
    params = Daytona::CreateSandboxFromSnapshotParams.new(
      ephemeral: true,
      auto_stop_interval: 5 # The ephemeral sandbox will be deleted after 5 minutes of inactivity
    )
    sandbox = daytona.create(params)
    ```


:::note
Setting ["autoDeleteInterval: 0"](#auto-delete-interval) has the same effect as setting "ephemeral" to `true`.
:::

### Network settings (Firewall)

Daytona Sandboxes provide configurable network firewall controls to enhance security and manage connectivity.
By default, network access follows standard security policies, but you can [customize network settings](https://www.daytona.io/docs/en/network-limits.md) when creating a sandbox.

## Start Sandboxes

Daytona provides options to start sandboxes using the [Daytona Dashboard ↗](https://app.daytona.io/dashboard/) or programmatically using the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk.md).

1. Navigate to [Daytona Sandboxes ↗](https://app.daytona.io/dashboard/sandboxes)
2. Click the start icon (**▶**) next to the sandbox you want to start.

```text
Starting sandbox with ID: <sandbox-id>
```

    ```python
    sandbox = daytona.create(CreateSandboxParams(language="python"))
    # Start Sandbox
    sandbox.start()
    ```


    ```typescript
    const sandbox = await daytona.create({ language: 'typescript' });
    // Start Sandbox
    await sandbox.start();
    ```


    ```ruby
    sandbox = daytona.create(Daytona::CreateSandboxFromSnapshotParams.new(language: Daytona::CodeLanguage::PYTHON))
    # Start Sandbox
    sandbox.start
    ```


For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstop), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#stop), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#start) references:

> [**start (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstart)
>
> [**start (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#start)
>
> [**start (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#start)

## List Sandboxes

Daytona provides options to view information about sandboxes (ID, root directory, and status) and manage their lifecycle.

    ```python
    # Get sandbox ID
    sandbox_id = sandbox.id

    # Get the root directory of the sandbox user
    root_dir = sandbox.get_user_root_dir()

    # Get the sandbox id, auto-stop interval and state
    print(sandbox.id)
    print(sandbox.auto_stop_interval)
    print(sandbox.state)
    ```


    ```typescript
    // Get sandbox ID
    const sandboxId = sandbox.id;

    // Get the root directory of the sandbox user
    const rootDir = await sandbox.getUserRootDir();

    // Get the sandbox id, auto-stop interval and state
    console.log(sandbox.id)
    console.log(sandbox.autoStopInterval)
    console.log(sandbox.state)
    ```


    ```ruby
    # Get sandbox ID
    sandbox_id = sandbox.id

    # Get the root directory of the sandbox user
    root_dir = sandbox.get_user_home_dir

    # Get the sandbox id, auto-stop interval and state
    puts sandbox.id
    puts sandbox.auto_stop_interval
    puts sandbox.state
    ```


For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstop), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#stop), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#list) references:

> [**list (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxlist)
>
> [**list (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#list)
>
> [**list (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#list)

## Stop Sandboxes

Daytona provides methods to stop sandboxes using Python, TypeScript, and Ruby.

1. Navigate to [Daytona Sandboxes ↗](https://app.daytona.io/dashboard/sandboxes)
2. Click the stop icon (**⏹**) next to the sandbox you want to stop.

```text
Stopping sandbox with ID: <sandbox-id>
```

Stopped sandboxes maintain filesystem persistence while their memory state is cleared. They incur only disk usage costs and can be started again when needed.

The stopped state should be used when a sandbox is expected to be started again soon. Otherwise, it is recommended to stop and then archive the sandbox to eliminate disk usage costs.

    ```python
    sandbox = daytona.create(CreateSandboxParams(language="python"))

    # Stop sandbox
    sandbox.stop()

    print(sandbox.id) # 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    # The sandbox ID can later be used to find the sandbox and start it
    sandbox = daytona.find_one("7cd11133-96c1-4cc8-9baa-c757b8f8c916")

    # Start sandbox
    sandbox.start()
    ```


    ```typescript
    const sandbox = await daytona.create({ language: 'typescript' });

    // Stop sandbox
    await sandbox.stop();

    console.log(sandbox.id) // 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    // The sandbox ID can later be used to find the sandbox and start it
    const sandbox = await daytona.findOne("7cd11133-96c1-4cc8-9baa-c757b8f8c916");

    // Start sandbox
    await sandbox.start();
    ```


    ```ruby
    sandbox = daytona.create(Daytona::CreateSandboxFromSnapshotParams.new(language: Daytona::CodeLanguage::PYTHON))

    # Stop sandbox
    sandbox.stop

    puts sandbox.id # 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    # The sandbox ID can later be used to find the sandbox and start it
    sandbox = daytona.find_one('7cd11133-96c1-4cc8-9baa-c757b8f8c916')

    # Start sandbox
    sandbox.start
    ```


For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstop), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#stop), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#stop) references:

> [**stop (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstop), [**stop (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#stop), [**stop (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#stop)
>
> [**find_one (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/daytona.md#daytonafind_one), [**findOne (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/daytona.md#findone), [**find_one (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/daytona.md#find_one)

## Archive Sandboxes

Daytona provides methods to archive sandboxes using Python, TypeScript, and Ruby.

When sandboxes are archived, the entire filesystem state is moved to very cost-effective object storage, making it possible to keep sandboxes available for an extended period.
Starting an archived sandbox takes more time than starting a stopped sandbox, depending on its size.

A sandbox must be stopped before it can be archived, and can be started again in the same way as a stopped sandbox.

    ```python
    # Archive Sandbox
    sandbox.archive()
    ```

    ```typescript
    // Archive Sandbox
    await sandbox.archive();
    ```

    ```ruby
    # Archive Sandbox
    sandbox.archive
    ```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk.md) references:

> [**archive (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxarchive)
>
> [**archive (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#archive)
>
> [**archive (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#archive)

## Recover Sandboxes

Daytona provides methods to recover sandboxes using Python, TypeScript, and Ruby.


    ```python
    # Recover sandbox
    sandbox.recover()
    ```


    ```typescript
    // Recover sandbox
    await sandbox.recover();
    ```



    ```ruby
    # Recover sandbox
    sandbox.recover
    ```


For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxrecover), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#recover), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#recover) references:

> [**recover (Python SDK)**](https://www.daytona.io/docs/en/python-sdk/sync/sandbox.md#sandboxrecover)
>
> [**recover (TypeScript SDK)**](https://www.daytona.io/docs/en/typescript-sdk/sandbox.md#recover)
>
> [**recover (Ruby SDK)**](https://www.daytona.io/docs/en/ruby-sdk/sandbox.md#recover)

### Recover from error state

When a sandbox enters an error state, it can sometimes be recovered using the `recover` method, depending on the underlying error reason. The `recoverable` flag indicates whether the error state can be resolved through an automated recovery procedure.

:::note
Recovery actions are not performed automatically because they address errors that require **further user intervention**, such as freeing up storage space.
:::

    ```python
    # Check if the Sandbox is recoverable
    if sandbox.recoverable:
        sandbox.recover()
        print("Sandbox recovered successfully")
    ```

    ```typescript
    // Check if the Sandbox is recoverable
    if (sandbox.recoverable) {
        await sandbox.recover();
        console.log('Sandbox recovered successfully');
    }
    ```

    ```ruby
    # Check if the Sandbox is recoverable
    if sandbox.recoverable
      sandbox.recover
      puts 'Sandbox recovered successfully'
    end
    ```

For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxrecover), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#recover), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#recover) references:

> [**recover (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxrecover)
>
> [**recover (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#recover)
>
> [**recover (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#recover)

## Delete Sandboxes

Daytona provides methods to delete sandboxes.

1. Navigate to [Daytona Sandboxes ↗](https://app.daytona.io/dashboard/sandboxes)
2. Click the **Delete** button next to the sandbox you want to delete.

```text
Stopping sandbox with ID: <sandbox-id>
```

    ```python
    # Delete sandbox
    sandbox.delete()
    ```

    ```typescript
    // Delete sandbox
    await sandbox.delete();
    ```

    ```ruby
    # Delete sandbox
    sandbox.delete
    ```

For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk.md) references:

> [**delete (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxdelete)
>
> [**delete (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#delete)
>
> [**delete (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#delete)

## Automated lifecycle management

Daytona Sandboxes can be automatically stopped, archived, and deleted based on user-defined intervals.

### Auto-stop interval

The auto-stop interval parameter sets the amount of time after which a running sandbox will be automatically stopped.

**Important**: The auto-stop interval will trigger even if there are internal processes running in the sandbox. The system differentiates between "internal processes" and "active user interaction". Merely having a script or background task running is not sufficient to keep the sandbox alive.

#### What resets the timer

The inactivity timer resets only for specific external interactions:

- Opened [preview windows](https://www.daytona.io/docs/en/preview-and-authentication.md)
- Active [SSH connections](https://www.daytona.io/docs/en/ssh-access.md)
- [Daytona Toolbox SDK API](https://www.daytona.io/docs/en/tools/api.md#daytona-toolbox) calls

#### What does not reset the timer

Internal processes running in the background do not reset the timer:

- Background scripts (e.g., `npm run dev` run as a fire-and-forget command)
- Long-running tasks without external interaction
- Processes that don't involve SDK polling or active monitoring

**Example**: If you run a long-running task like LLM inference that takes more than 15 minutes without any external interaction, the sandbox may auto-stop mid-process because the process itself doesn't count as "activity".

The parameter can either be set to:

- a time interval in minutes
- `0`: disables the auto-stop functionality, allowing the sandbox to run indefinitely

If the parameter is not set, the default interval of `15` minutes will be used.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        # Disables the auto-stop feature - default is 15 minutes
        auto_stop_interval=0,
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
         // Disables the auto-stop feature - default is 15 minutes
        autoStopInterval: 0,
    });
    ```

    ```ruby
    sandbox = daytona.create(
      Daytona::CreateSandboxFromSnapshotParams.new(
        snapshot: 'my-snapshot-name',
        # Disables the auto-stop feature - default is 15 minutes
        auto_stop_interval: 0
      )
    )
    ```

For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxset_autostop_interval), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#set_auto_stop_interval), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#set_auto_stop_interval) references:

> [**set_auto_stop_interval (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxset_autostop_interval)
>
> [**setAutostopInterval (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#setautostopinterval)
>
> [**set_auto_stop_interval (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#set_auto_stop_interval)

### Auto-archive interval

The auto-archive interval parameter sets the amount of time after which a continuously stopped sandbox will be automatically archived.

The parameter can either be set to:

- a time interval in minutes
- `0`: means the maximum interval of `30 days` will be used

If the parameter is not set, the default interval of `7 days` days will be used.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        # Auto-archive after a sandbox has been stopped for 1 hour
        auto_archive_interval=60,
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        // Auto-archive after a sandbox has been stopped for 1 hour
        autoArchiveInterval: 60,
    });
    ```

    ```ruby
    sandbox = daytona.create(
      Daytona::CreateSandboxFromSnapshotParams.new(
        snapshot: 'my-snapshot-name',
        # Auto-archive after a sandbox has been stopped for 1 hour
        auto_archive_interval: 60
      )
    )
    ```

For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxset_auto_archive_interval), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#set_auto_archive_interval), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#set_auto_archive_interval) references:

> [**set_auto_archive_interval (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxset_auto_archive_interval)
>
> [**setAutoArchiveInterval (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#setautoarchiveinterval)
>
> [**set_auto_archive_interval (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#set_auto_archive_interval)

### Auto-delete interval

The auto-delete interval parameter sets the amount of time after which a continuously stopped sandbox will be automatically deleted. By default, sandboxes will never be automatically deleted.

The parameter can either be set to:

- a time interval in minutes
- `-1`: disables the auto-delete functionality
- `0`: means the sandbox will be deleted immediately after stopping

If the parameter is not set, the sandbox will not be deleted automatically.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        # Auto-delete after a sandbox has been stopped for 1 hour
        auto_delete_interval=60,
    ))

    # Delete the sandbox immediately after it has been stopped
    sandbox.set_auto_delete_interval(0)

    # Disable auto-deletion
    sandbox.set_auto_delete_interval(-1)
    ```


    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        // Auto-delete after a sandbox has been stopped for 1 hour
        autoDeleteInterval: 60,
    });

    // Delete the sandbox immediately after it has been stopped
    await sandbox.setAutoDeleteInterval(0)

    // Disable auto-deletion
    await sandbox.setAutoDeleteInterval(-1)
    ```


    ```ruby
    sandbox = daytona.create(
      Daytona::CreateSandboxFromSnapshotParams.new(
        snapshot: 'my-snapshot-name',
        # Auto-delete after a sandbox has been stopped for 1 hour
        auto_delete_interval: 60
      )
    )

    # Delete the sandbox immediately after it has been stopped
    sandbox.set_auto_delete_interval(0)

    # Disable auto-deletion
    sandbox.set_auto_delete_interval(-1)
    ```


For more information, see the [Python SDK](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxset_auto_delete_interval), [TypeScript SDK](https://www.daytona.io/docs/typescript-sdk/sandbox.md#set_auto_delete_interval), and [Ruby SDK](https://www.daytona.io/docs/ruby-sdk/sandbox.md#set_auto_delete_interval) references:

> [**set_auto_delete_interval (Python SDK)**](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxset_auto_delete_interval)
>
> [**setAutoDeleteInterval (TypeScript SDK)**](https://www.daytona.io/docs/typescript-sdk/sandbox.md#setautodeleteinterval)
>
> [**set_auto_delete_interval (Ruby SDK)**](https://www.daytona.io/docs/ruby-sdk/sandbox.md#set_auto_delete_interval)

### Running indefinitely

By default, Daytona Sandboxes auto-stop after 15 minutes of inactivity. To keep a sandbox running without interruption, set the auto-stop interval to `0` when creating a new sandbox:

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my_awesome_snapshot",
        # Disables the auto-stop feature - default is 15 minutes
        auto_stop_interval=0,
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my_awesome_snapshot",
        // Disables the auto-stop feature - default is 15 minutes
        autoStopInterval: 0,
    });
    ```

    ```ruby
    sandbox = daytona.create(
      Daytona::CreateSandboxFromSnapshotParams.new(
        snapshot: 'my_awesome_snapshot',
        # Disables the auto-stop feature - default is 15 minutes
        auto_stop_interval: 0
      )
    )
    ```