# Source: https://www.daytona.io/docs/en/volumes.md

Volumes are FUSE-based mounts that provide shared file access across Sandboxes. They allow Sandboxes to read from large files instantly - no need to upload files manually to each Sandbox. Volume data is stored on an S3-compatible object store.

- Multiple volumes can be mounted to a single Sandbox  
- A single volume can be mounted to multiple Sandboxes

## Creating Volumes

Before mounting a volume to a Sandbox, it must be created.

```bash
volume = daytona.volume.get("my-volume", create=True)
```
```bash
const volume = await daytona.volume.get('my-volume', true)
```

See: [volume.get (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/volume.md#volumeserviceget), [volume.get (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/volume.md#get)

## Mounting Volumes

Once a volume is created, it can be mounted to a Sandbox by specifying it in the `CreateSandboxFromSnapshotParams` object. Volume mount paths must meet the following requirements:

- **Must be absolute paths**: Mount paths must start with `/` (e.g., `/home/daytona/volume`)
- **Cannot be root directory**: Cannot mount to `/` or `//`
- **No relative path components**: Cannot contain `/../`, `/./`, or end with `/..` or `/.`
- **No consecutive slashes**: Cannot contain multiple consecutive slashes like `//` (except at the beginning)
- **Cannot mount to system directories**: The following system directories are prohibited:
  - `/proc`, `/sys`, `/dev`, `/boot`, `/etc`, `/bin`, `/sbin`, `/lib`, `/lib64`

```python
import os
from daytona import CreateSandboxFromSnapshotParams, Daytona, VolumeMount

daytona = Daytona()

# Create a new volume or get an existing one
volume = daytona.volume.get("my-volume", create=True)

# Mount the volume to the sandbox
mount_dir_1 = "/home/daytona/volume"

params = CreateSandboxFromSnapshotParams(
    language="python",
    volumes=[VolumeMount(volumeId=volume.id, mountPath=mount_dir_1)],
)
sandbox = daytona.create(params)
```

```typescript
import { Daytona } from '@daytonaio/sdk'
import path from 'path'

const daytona = new Daytona()

//  Create a new volume or get an existing one
const volume = await daytona.volume.get('my-volume', true)

// Mount the volume to the sandbox
const mountDir1 = '/home/daytona/volume'

const sandbox1 = await daytona.create({
  language: 'typescript',
  volumes: [{ volumeId: volume.id, mountPath: mountDir1 }],
})
```


See: [CreateSandboxFromSnapshotParams (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/daytona.md#createSandboxBaseParams), [CreateSandboxFromSnapshotParams (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/daytona.md#createSandboxBaseParams)

## Working with Volumes

Once mounted, you can read from and write to the volume just like any other directory in the Sandbox file system. Files written to the volume persist beyond the lifecycle of any individual Sandbox.

    ```python
    # Write to a file in the mounted volume
    with open("/home/daytona/volume/example.txt", "w") as f:
        f.write("Hello from Daytona volume!")

    # When you're done with the sandbox, you can remove it
    # The volume will persist even after the sandbox is removed
    sandbox.delete()
    ```
    ```typescript
    import fs from 'fs/promises'

    // Write to a file in the mounted volume
    await fs.writeFile('/home/daytona/volume/example.txt', 'Hello from Daytona volume!')

    // When you're done with the sandbox, you can remove it
    // The volume will persist even after the sandbox is removed
    await daytona.delete(sandbox1)
    ```

## Deleting Volumes

When a volume is no longer needed, it can be deleted.

```python
volume = daytona.volume.get("my-volume", create=True)
daytona.volume.delete(volume)
```
```typescript
const volume = await daytona.volume.get('my-volume', true)
await daytona.volume.delete(volume)
```

## Limitations

Since volumes are FUSE-based mounts, they can not be used for applications that require block storage access (like database tables).
Volumes are generally slower for both read and write operations compared to the local Sandbox file system.