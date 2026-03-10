# Source: https://modal.com/docs/guide/sandbox-snapshots.md

# Snapshots

Sandboxes support snapshotting, allowing you to save your Sandbox's state
and restore it later. This is useful for:

* Reducing startup latency
* Creating custom environments for your Sandboxes to run in
* Backing up your Sandbox's state for debugging
* Running large-scale experiments with the same initial state
* Branching your Sandbox's state to test different code changes independently

Modal currently supports three different kinds of Sandbox snapshots:

1. [Filesystem Snapshots](#filesystem-snapshots)
2. [Directory Snapshots (Beta)](#directory-snapshots-beta)
3. [Memory Snapshots (Alpha)](#memory-snapshots-alpha)

## Filesystem Snapshots

Filesystem Snapshots are copies of the Sandbox's filesystem at a given point in time.
These Snapshots are [Images](/docs/reference/modal.Image) and can be used to create
new Sandboxes.

To create a Filesystem Snapshot, you can use the
[`Sandbox.snapshot_filesystem()`](/docs/reference/modal.Sandbox#snapshot_filesystem) method:

```python notest
import modal

app = modal.App.lookup("sandbox-fs-snapshot-test", create_if_missing=True)

sb = modal.Sandbox.create(app=app)
p = sb.exec("bash", "-c", "echo 'test' > /test")
p.wait()
assert p.returncode == 0, "failed to write to file"
image = sb.snapshot_filesystem()
sb.terminate()

sb2 = modal.Sandbox.create(image=image, app=app)
p2 = sb2.exec("bash", "-c", "cat /test")
assert p2.stdout.read().strip() == "test"
```

Filesystem Snapshots are optimized for performance: they are calculated as the difference
from your base image, so only modified files are stored. Restoring a Filesystem Snapshot
utilizes the same infrastructure we use to get fast cold starts for your Sandboxes.

Filesystem Snapshots will generally persist indefinitely.

## Directory Snapshots (Beta)

Directory Snapshots allow you to snapshot a specific directory within a running Sandbox. The resulting snapshot is an Image that can then be mounted into another already-running Sandbox (typically at a later time), which can be useful for:

* **Updating system dependencies separately from application code**: Base dependencies can be updated by starting a new Sandbox from an updated base Image, and then mounting in previously snapshotted application code.
* **Using warm pools in combination with snapshots**: For use cases that benefit from a [warm pool](https://github.com/modal-labs/modal-examples/blob/main/13_sandboxes/sandbox_pool.py) of Sandboxes to reduce start-up latency, the first initialization can now happen in the warm pool without losing the ability to restore application-specific code at a later point in time.
* **Speeding up resumptions of previous sessions**: Files in mounted Images are prioritized when containers load files, so mounting a directory can speed up Sandbox resumptions vs. starting from a full file system image.

### Usage

Use `snapshot_directory` to snapshot a directory and `mount_image` to mount a previous directory snapshot at a directory path.

<CodeTabs>
  {#snippet python()}

```python notest
sb = modal.Sandbox.create(app=app)
# Write some dummy data
sb.exec("bash", "-c", "mkdir /project && echo 'data' > /project/file.txt").wait()

# Snapshot the directory
snapshot = sb.snapshot_directory("/project")

# Ok to throw away the old sandbox at this point
sb.terminate()

# Mount the snapshot in a new Sandbox
sb2 = modal.Sandbox.create(app=app)
try:
    sb2.mount_image("/project", snapshot)
except modal.exception.NotFoundError:
    # Handle a potential ttl expiry of the old snapshot here
    ...

# The sandbox now has access to the previous project state
assert sb2.exec("cat", "/project/file.txt").stdout.read().strip() == "data"

```

{/snippet}
{#snippet javascript()}

```javascript notest
import { NotFoundError } from "@modal/client";

const sb = await modal.sandboxes.create(app, image);
// Write some dummy data
const p = await sb.exec([
  "bash",
  "-c",
  "mkdir /project && echo 'data' > /project/file.txt",
]);
await p.wait();

// Snapshot the directory
const snapshot = await sb.snapshotDirectory("/project");

// Ok to throw away the old sandbox at this point
await sb.terminate();
sb.detach();

// Mount the snapshot in a new Sandbox
const sb2 = await modal.sandboxes.create(app, image);
try {
  await sb2.mountImage("/project", snapshot);
} catch (e) {
  if (e instanceof NotFoundError) {
    // Handle a potential ttl expiry of the old snapshot here
  }
}

// The sandbox now has access to the previous project state
const p2 = await sb2.exec(["cat", "/project/file.txt"]);
console.assert((await p2.stdout.readText()).trim() === "data");
sb2.detach();
```

{/snippet}
{#snippet go()}

```go notest
sb, _ := mc.Sandboxes.Create(ctx, app, image, nil)
defer sb.Detach()

// Write some dummy data
p, _ := sb.Exec(ctx, []string{"bash", "-c", "mkdir /project && echo 'data' > /project/file.txt"}, nil)
p.Wait(ctx)

// Snapshot the directory
snapshot, _ := sb.SnapshotDirectory(ctx, "/project")

// Ok to throw away the old sandbox at this point
sb.Terminate(ctx, nil)

// Mount the snapshot in a new Sandbox
sb2, _ := mc.Sandboxes.Create(ctx, app, image, nil)
defer sb2.Detach()

if err := sb2.MountImage(ctx, "/project", snapshot); err != nil {
  if errors.Is(err, modal.NotFoundError) {
    // Handle a potential ttl expiry of the old snapshot here
  }
}

// The sandbox now has access to the previous project state
p2, _ := sb2.Exec(ctx, []string{"cat", "/project/file.txt"}, nil)
stdout, _ := io.ReadAll(p2.Stdout)
fmt.Println(strings.TrimSpace(string(stdout))) // "data"
```

{/snippet} </CodeTabs>

### Persistence

Directory snapshots are currently persisted for 30 days after they were last created or used. If you try to use an expired snapshot, Modal will raise a `NotFoundError`, letting you handle the case gracefully.

## Memory Snapshots (Alpha)

> 🌱 Sandbox memory snapshots are in **Alpha.**

Sandbox memory snapshots are copies of a Sandbox’s entire state, both in memory and on the filesystem. These Snapshots can be restored later to create a new Sandbox, which is an exact clone of the original Sandbox.

To snapshot a Sandbox, create it with `_experimental_enable_snapshot` set to `True`, and use the `_experimental_snapshot` method, which returns a `SandboxSnapshot` object:

```python notest
image = modal.Image.debian_slim().apt_install("curl", "procps")
app = modal.App.lookup("sandbox-snapshot", create_if_missing=True)

with modal.enable_output():
    sb = modal.Sandbox.create(
        "python3", "-m", "http.server", "8000",
        app=app, image=image, _experimental_enable_snapshot=True
    )

print(f"Performing snapshot of {sb.object_id} ...")
snapshot = sb._experimental_snapshot()
```

Create a new Sandbox from the returned SandboxSnapshot with `Sandbox._experimental_from_snapshot`:

```python notest
print(f"Restoring from snapshot {sb.object_id} ...")
sb2 = modal.Sandbox._experimental_from_snapshot(snapshot)

print("Let's see that the http.server is still running...")
p = sb2.exec("ps", "aux")
print(p.stdout.read())

# Talk to snapshotted sandbox http.server
p = sb2.exec("curl", "http://localhost:8000/")
reply = p.stdout.read()
print(reply)  # <!DOCTYPE HTML><html lang...
```

The new Sandbox will be a duplicate of your original Sandbox. All running processes will still be running, in the same state as when they were snapshotted, and any changes made to the filesystem will be visible.

You can retrieve the ID of any Sandbox Snapshot with `snapshot.object_id` . To restore from a snapshot by ID, first rehydrate the Snapshot with `SandboxSnapshot.from_id` and then restore from it:

```python notest
snapshot_id = snapshot.object_id
# ... save the Sandbox ID (sb-123abc) for later
# sometime in the future...
snapshot = modal.SandboxSnapshot.from_id(snapshot_id)
sandbox = modal.Sandbox._experimental_from_snapshot(snapshot)
```

Note that these methods are *experimental*, and we may change them in the future.

### Re-snapshotting

Modal supports creating a new snapshot from a restored Sandbox snapshot. To maintain the snapshot’s expiration window, the new snapshot inherits the expiration of its parent.

Continuing from the example code above, we demonstrate re-snapshotting:

```python notest
# Add a file to the snapshotted sandbox
p = sb2.exec("touch", "/foo")
p.wait()

snapshot2 = sb2._experimental_snapshot()
print(f"Restoring from new snapshot {snapshot2.object_id} ...")
sb3 = modal.Sandbox._experimental_from_snapshot(snapshot2)
# Talk to re-snapshotted sandbox http.server
p = sb3.exec("curl", "http://localhost:8000/")
reply = p.stdout.read()
print(reply)  # Shows the new 'foo' directory in the HTML listing.
```

### Limitations

Currently, Sandbox Memory Snapshots will expire 7 days after creation. For longer persisting snapshots, try [Filesystem Snapshots](/docs/guide/sandbox-snapshots).

Open TCP connections will be closed automatically when a Snapshot is taken, and will need to be reopened when the Snapshot is restored.

Snapshotting a sandbox will currently cause it to terminate. We intend to remove this limitation soon.

Sandboxes created with `_experimental_enable_snapshot=True` or restored from Snapshots cannot run with GPUs.

It is not possible to snapshot a sandbox while a `Sandbox.exec` command is still running. Furthermore, any background processes launched by a call to `Sandbox.exec` will not be properly restored after a snapshot.

## Persisting Sandbox State

To persist state across Sandbox sessions, you need to:

1. **Trigger the snapshot.** Snapshots are triggered from outside the Sandbox, typically just before termination. A common pattern is to run an exec process inside the Sandbox and wait for it to exit. Once it does, the controller takes a snapshot and terminates the Sandbox.
2. **Store the snapshot ID.** The `object_id` string must be persisted so you can restore from it later. This is typically keyed by a session or user ID, and can be stored in your database, an external key-value store, or a [Modal Dict](/docs/guide/dicts).

The following example shows this pattern. This code would typically run in a Modal Function or your own backend, orchestrating the Sandbox:

```python notest
import modal

app = modal.App.lookup("sandbox-snapshot-lifecycle", create_if_missing=True)
snapshot_store = modal.Dict.from_name("sandbox-snapshots", create_if_missing=True)
session_id = "sess_a1b2c3d4"

# Restore from snapshot, or use base image
if session_id in snapshot_store:
    image = modal.Image.from_id(snapshot_store[session_id])
else:
    image = modal.Image.debian_slim()

sb = modal.Sandbox.create(image=image, app=app)

# Run agent which exits when ready to be snapshotted
p = sb.exec("python", "agent.py")
p.wait()

# Snapshot and store the object_id
snapshot_store[session_id] = sb.snapshot_filesystem().object_id
sb.terminate()
```
