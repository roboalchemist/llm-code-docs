# [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#snapshots) Snapshots

_Available as of v0.8.4_

Snapshots are `tar` archive files that contain data and configuration of a specific collection on a specific node at a specific time. In a distributed setup, when you have multiple nodes in your cluster, you must create snapshots for each node separately when dealing with a single collection.

This feature can be used to archive data or easily replicate an existing deployment. For disaster recovery, Qdrant Cloud users may prefer to use [Backups](https://qdrant.tech/documentation/cloud/backups/) instead, which are physical disk-level copies of your data.

For a step-by-step guide on how to use snapshots, see our [tutorial](https://qdrant.tech/documentation/tutorials/create-snapshot/).

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#create-snapshot) Create snapshot

To create a new snapshot for an existing collection:

httppythontypescriptrustjavacsharpgo

```http
POST /collections/{collection_name}/snapshots

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.create_snapshot(collection_name="{collection_name}")

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createSnapshot("{collection_name}");

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_snapshot("{collection_name}").await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
      new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.createSnapshotAsync("{collection_name}").get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.CreateSnapshotAsync("{collection_name}");

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.CreateSnapshot(context.Background(), "{collection_name}")

```

This is a synchronous operation for which a `tar` archive file will be generated into the `snapshot_path`.

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#delete-snapshot) Delete snapshot

_Available as of v1.0.0_

httppythontypescriptrustjavacsharpgo

```http
DELETE /collections/{collection_name}/snapshots/{snapshot_name}

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.delete_snapshot(
    collection_name="{collection_name}", snapshot_name="{snapshot_name}"
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.deleteSnapshot("{collection_name}", "{snapshot_name}");

```

```rust
use qdrant_client::qdrant::DeleteSnapshotRequestBuilder;
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client
    .delete_snapshot(DeleteSnapshotRequestBuilder::new(
        "{collection_name}",
        "{snapshot_name}",
    ))
    .await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.deleteSnapshotAsync("{collection_name}", "{snapshot_name}").get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeleteSnapshotAsync(collectionName: "{collection_name}", snapshotName: "{snapshot_name}");

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.DeleteSnapshot(context.Background(), "{collection_name}", "{snapshot_name}")

```

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#list-snapshot) List snapshot

List of snapshots for a collection:

httppythontypescriptrustjavacsharpgo

```http
GET /collections/{collection_name}/snapshots

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.list_snapshots(collection_name="{collection_name}")

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.listSnapshots("{collection_name}");

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.list_snapshots("{collection_name}").await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.listSnapshotAsync("{collection_name}").get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ListSnapshotsAsync("{collection_name}");

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.ListSnapshots(context.Background(), "{collection_name}")

```

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#retrieve-snapshot) Retrieve snapshot

To download a specified snapshot from a collection as a file:

httpshell

```http
GET /collections/{collection_name}/snapshots/{snapshot_name}

```

```shell
curl 'http://{qdrant-url}:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.snapshot' \
    -H 'api-key: ********' \
    --output 'filename.snapshot'

```

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#restore-snapshot) Restore snapshot

Snapshots can be restored in three possible ways:

1. [Recovering from a URL or local file](https://qdrant.tech/documentation/concepts/snapshots/#recover-from-a-url-or-local-file) (useful for restoring a snapshot file that is on a remote server or already stored on the node)
2. [Recovering from an uploaded file](https://qdrant.tech/documentation/concepts/snapshots/#recover-from-an-uploaded-file) (useful for migrating data to a new cluster)
3. [Recovering during start-up](https://qdrant.tech/documentation/concepts/snapshots/#recover-during-start-up) (useful when running a self-hosted single-node Qdrant instance)

Regardless of the method used, Qdrant will extract the shard data from the snapshot and properly register shards in the cluster.
If there are other active replicas of the recovered shards in the cluster, Qdrant will replicate them to the newly recovered node by default to maintain data consistency.

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#recover-from-a-url-or-local-file) Recover from a URL or local file

_Available as of v0.11.3_

This method of recovery requires the snapshot file to be downloadable from a URL or exist as a local file on the node (like if you [created the snapshot](https://qdrant.tech/documentation/concepts/snapshots/#create-snapshot) on this node previously). If instead you need to upload a snapshot file, see the next section.

To recover from a URL or local file use the [snapshot recovery endpoint](https://api.qdrant.tech/master/api-reference/snapshots/recover-from-snapshot). This endpoint accepts either a URL like `https://example.com` or a [file URI](https://en.wikipedia.org/wiki/File_URI_scheme) like `file:///tmp/snapshot-2022-10-10.snapshot`. If the target collection does not exist, it will be created.

httppythontypescript

```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot"
}

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://qdrant-node-2:6333")

client.recover_snapshot(
    "{collection_name}",
    "http://qdrant-node-1:6333/collections/collection_name/snapshots/snapshot-2022-10-10.shapshot",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.recoverSnapshot("{collection_name}", {
  location: "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot",
});

```

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#recover-from-an-uploaded-file) Recover from an uploaded file

The snapshot file can also be uploaded as a file and restored using the [recover from uploaded snapshot](https://api.qdrant.tech/master/api-reference/snapshots/recover-from-uploaded-snapshot). This endpoint accepts the raw snapshot data in the request body. If the target collection does not exist, it will be created.

```bash
curl -X POST 'http://{qdrant-url}:6333/collections/{collection_name}/snapshots/upload?priority=snapshot' \
    -H 'api-key: ********' \
    -H 'Content-Type:multipart/form-data' \
    -F 'snapshot=@/path/to/snapshot-2022-10-10.shapshot'

```

This method is typically used to migrate data from one cluster to another, so we recommend setting the [priority](https://qdrant.tech/documentation/concepts/snapshots/#snapshot-priority) to “snapshot” for that use-case.

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#recover-during-start-up) Recover during start-up

If you have a single-node deployment, you can recover any collection at start-up and it will be immediately available.
Restoring snapshots is done through the Qdrant CLI at start-up time via the `--snapshot` argument which accepts a list of pairs such as `<snapshot_file_path>:<target_collection_name>`

For example:

```bash
./qdrant --snapshot /snapshots/test-collection-archive.snapshot:test-collection --snapshot /snapshots/test-collection-archive.snapshot:test-copy-collection

```

The target collection **must** be absent otherwise the program will exit with an error.

If you wish instead to overwrite an existing collection, use the `--force_snapshot` flag with caution.

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#snapshot-priority) Snapshot priority

When recovering a snapshot to a non-empty node, there may be conflicts between the snapshot data and the existing data. The “priority” setting controls how Qdrant handles these conflicts. The priority setting is important because different priorities can give very
different end results. The default priority may not be best for all situations.

The available snapshot recovery priorities are:

- `replica`: _(default)_ prefer existing data over the snapshot.
- `snapshot`: prefer snapshot data over existing data.
- `no_sync`: restore snapshot without any additional synchronization.

To recover a new collection from a snapshot, you need to set
the priority to `snapshot`. With `snapshot` priority, all data from the snapshot
will be recovered onto the cluster. With `replica` priority _(default)_, you’d
end up with an empty collection because the collection on the cluster did not
contain any points and that source was preferred.

`no_sync` is for specialized use cases and is not commonly used. It allows
managing shards and transferring shards between clusters manually without any
additional synchronization. Using it incorrectly will leave your cluster in a
broken state.

To recover from a URL, you specify an additional parameter in the request body:

httpbashpythontypescript

```http
PUT /collections/{collection_name}/snapshots/recover
{
  "location": "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot",
  "priority": "snapshot"
}

```

```bash
curl -X POST 'http://qdrant-node-1:6333/collections/{collection_name}/snapshots/upload?priority=snapshot' \
    -H 'api-key: ********' \
    -H 'Content-Type:multipart/form-data' \
    -F 'snapshot=@/path/to/snapshot-2022-10-10.shapshot'

```

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://qdrant-node-2:6333")

client.recover_snapshot(
    "{collection_name}",
    "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot",
    priority=models.SnapshotPriority.SNAPSHOT,
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.recoverSnapshot("{collection_name}", {
  location: "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot",
  priority: "snapshot"
});

```

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#snapshots-for-the-whole-storage) Snapshots for the whole storage

_Available as of v0.8.5_

Sometimes it might be handy to create snapshot not just for a single collection, but for the whole storage, including collection aliases.
Qdrant provides a dedicated API for that as well. It is similar to collection-level snapshots, but does not require `collection_name`.

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#create-full-storage-snapshot) Create full storage snapshot

httppythontypescriptrustjavacsharpgo

```http
POST /snapshots

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.create_full_snapshot()

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.createFullSnapshot();

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.create_full_snapshot().await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.createFullSnapshotAsync().get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.CreateFullSnapshotAsync();

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.CreateFullSnapshot(context.Background())

```

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#delete-full-storage-snapshot) Delete full storage snapshot

_Available as of v1.0.0_

httppythontypescriptrustjavacsharpgo

```http
DELETE /snapshots/{snapshot_name}

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

client.delete_full_snapshot(snapshot_name="{snapshot_name}")

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.deleteFullSnapshot("{snapshot_name}");

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.delete_full_snapshot("{snapshot_name}").await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.deleteFullSnapshotAsync("{snapshot_name}").get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.DeleteFullSnapshotAsync("{snapshot_name}");

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.DeleteFullSnapshot(context.Background(), "{snapshot_name}")

```

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#list-full-storage-snapshots) List full storage snapshots

httppythontypescriptrustjavacsharpgo

```http
GET /snapshots

```

```python
from qdrant_client import QdrantClient

client = QdrantClient("localhost", port=6333)

client.list_full_snapshots()

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ host: "localhost", port: 6333 });

client.listFullSnapshots();

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

client.list_full_snapshots().await?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(QdrantGrpcClient.newBuilder("localhost", 6334, false).build());

client.listFullSnapshotAsync().get();

```

```csharp
using Qdrant.Client;

var client = new QdrantClient("localhost", 6334);

await client.ListFullSnapshotsAsync();

```

```go
import (
	"context"

	"github.com/qdrant/go-client/qdrant"
)

client, err := qdrant.NewClient(&qdrant.Config{
	Host: "localhost",
	Port: 6334,
})

client.ListFullSnapshots(context.Background())

```

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#download-full-storage-snapshot) Download full storage snapshot

```http
GET /snapshots/{snapshot_name}

```

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#restore-full-storage-snapshot) Restore full storage snapshot

Restoring snapshots can only be done through the Qdrant CLI at startup time.

For example:

```bash
./qdrant --storage-snapshot /snapshots/full-snapshot-2022-07-18-11-20-51.snapshot

```

## [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#storage) Storage

Created, uploaded and recovered snapshots are stored as `.snapshot` files. By
default, they’re stored on the [local file system](https://qdrant.tech/documentation/concepts/snapshots/#local-file-system). You may
also configure to use an [S3 storage](https://qdrant.tech/documentation/concepts/snapshots/#s3) service for them.

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#local-file-system) Local file system

By default, snapshots are stored at `./snapshots` or at `/qdrant/snapshots` when
using our Docker image.

The target directory can be controlled through the [configuration](https://qdrant.tech/documentation/guides/configuration/):

```yaml
storage:
  # Specify where you want to store snapshots.
  snapshots_path: ./snapshots

```

Alternatively you may use the environment variable `QDRANT__STORAGE__SNAPSHOTS_PATH=./snapshots`.

_Available as of v1.3.0_

While a snapshot is being created, temporary files are placed in the configured
storage directory by default. In case of limited capacity or a slow
network attached disk, you can specify a separate location for temporary files:

```yaml
storage:
  # Where to store temporary files
  temp_path: /tmp

```

### [Anchor](https://qdrant.tech/documentation/concepts/snapshots/\#s3) S3

_Available as of v1.10.0_

Rather than storing snapshots on the local file system, you may also configure
to store snapshots in an S3-compatible storage service. To enable this, you must
configure it in the [configuration](https://qdrant.tech/documentation/guides/configuration/) file.

For example, to configure for AWS S3:

```yaml
storage:
  snapshots_config:
    # Use 's3' to store snapshots on S3
    snapshots_storage: s3

    s3_config:
      # Bucket name
      bucket: your_bucket_here

      # Bucket region (e.g. eu-central-1)
      region: your_bucket_region_here

      # Storage access key
      # Can be specified either here or in the `QDRANT__STORAGE__SNAPSHOTS_CONFIG__S3_CONFIG__ACCESS_KEY` environment variable.
      access_key: your_access_key_here

      # Storage secret key
      # Can be specified either here or in the `QDRANT__STORAGE__SNAPSHOTS_CONFIG__S3_CONFIG__SECRET_KEY` environment variable.
      secret_key: your_secret_key_here

      # S3-Compatible Storage URL
      # Can be specified either here or in the `QDRANT__STORAGE__SNAPSHOTS_CONFIG__S3_CONFIG__ENDPOINT_URL` environment variable.
      endpoint_url: your_url_here

```

Apart from Snapshots, Qdrant also provides the [Qdrant Migration Tool](https://github.com/qdrant/migration) that supports:

- Migration between Qdrant Cloud instances.
- Migrating vectors from other providers into Qdrant.
- Migrating from Qdrant OSS to Qdrant Cloud.

Follow our [migration guide](https://qdrant.tech/documentation/database-tutorials/migration/) to learn how to effectively use the Qdrant Migration tool.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/snapshots.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/snapshots.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-71-lllmstxt|>
## examples
- [Documentation](https://qdrant.tech/documentation/)
- Build Prototypes