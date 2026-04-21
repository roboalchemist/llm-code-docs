<!-- Source: https://namespace.so/docs/architecture/storage/persistent-volumes -->

# Persistent Volumes

Namespace Persistent Volumes provide durable block storage that is guaranteed to persist across instance
lifetimes. Unlike [cache volumes](/docs/architecture/storage/cache-volumes) which follow a best-effort
fork model, persistent volumes maintain a single durable copy of data with automatic snapshotting.

## How it works

When a persistent volume is attached to an instance, it provides read-write access to the volume's data.
On instance shutdown, the volume's data is automatically snapshotted to ensure integrity.

Persistent volumes are identified by a **tag** — a logical name used to reference the volume across
instances. Each tag maps to a single durable volume within a region.

## Snapshots

Data is automatically snapshotted when an instance shuts down. Snapshots enable:

- **Initialization from a snapshot**: New persistent volumes can be initialized from a specific snapshot
  using `from_snapshot_id`, allowing you to seed a volume with data from a previous run.
- **Snapshot management**: Snapshots can be listed and abandoned via the API. Abandoned snapshots are
  excluded when selecting a base snapshot for new volumes, which is useful for marking corrupted or
  unwanted snapshots.

## API Access

Persistent volumes can be managed programmatically via the
[StorageService API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta):

- **`ListPersistentVolumes`**: List persistent volumes, optionally filtered by tag or site.
- **`DescribePersistentVolume`**: Get details of a specific persistent volume.
- **`DestroyPersistentVolumes`**: Destroy volumes matching given criteria.
- **`ListPersistentVolumeSnapshots`**: List all snapshots of a persistent volume.
- **`DestroyPersistentVolumeSnapshot`**: Mark a snapshot as abandoned.

To create a persistent volume, set `persistency_kind` to `PERSISTENT` in the `VolumeRequest` when
creating an instance.

Last updated March 20, 2026
