# Snapshots
Source: https://www.meilisearch.com/docs/reference/api/snapshots

The /snapshots route creates database snapshots. Use snapshots to backup your Meilisearch data.

The `/snapshot` route allows you to create database snapshots. Snapshots are `.snapshot` files that can be used to make quick backups of Meilisearch data.

[Learn more about snapshots.](/learn/data_backup/snapshots)

<Warning>
  Meilisearch Cloud does not support the `/snapshots` route.
</Warning>

## Create a snapshot

<RouteHighlighter method="POST" />

Triggers a snapshot creation task. Once the process is complete, Meilisearch creates a snapshot in the [snapshot directory](/learn/self_hosted/configure_meilisearch_at_launch#snapshot-destination). If the snapshot directory does not exist yet, it will be created.

Snapshot tasks take priority over other tasks in the queue.

[Learn more about asynchronous operations](/learn/async/asynchronous_operations).

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/snapshots'
  ```

  ```javascript JS theme={null}
  client.createSnapshot()
  ```

  ```python Python theme={null}
  client.create_snapshot()
  ```

  ```php PHP theme={null}
  $client->createSnapshot();
  ```

  ```java Java theme={null}
  client.createSnapshot();
  ```

  ```ruby Ruby theme={null}
  client.create_snapshot
  ```

  ```go Go theme={null}
  client.CreateSnapshot()
  ```

  ```csharp C# theme={null}
  await client.CreateSnapshotAsync();
  ```

  ```rust Rust theme={null}
  client
    .create_snapshot()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let task = try await self.client.createSnapshot()
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": null,
  "status": "enqueued",
  "type": "snapshotCreation",
  "enqueuedAt": "2023-06-21T11:09:36.417758Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task)