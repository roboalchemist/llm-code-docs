# Dumps
Source: https://www.meilisearch.com/docs/reference/api/dump

The /dumps route allows the creation of database dumps. Use dumps to migrate Meilisearch to a new version.

The `/dumps` route allows the creation of database dumps. Dumps are `.dump` files that can be used to restore Meilisearch data or migrate between different versions.

<Warning>
  Meilisearch Cloud does not support the `/dumps` route.
</Warning>

[Learn more about dumps](/learn/data_backup/dumps).

## Create a dump

<RouteHighlighter method="POST" />

Triggers a dump creation task. Once the process is complete, a dump is created in the [dump directory](/learn/self_hosted/configure_meilisearch_at_launch#dump-directory). If the dump directory does not exist yet, it will be created.

Dump tasks take priority over all other tasks in the queue. This means that a newly created dump task will be processed as soon as the current task is finished.

[Learn more about asynchronous operations](/learn/async/asynchronous_operations).

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/dumps'
  ```

  ```javascript JS theme={null}
  client.createDump()
  ```

  ```python Python theme={null}
  client.create_dump()
  ```

  ```php PHP theme={null}
  $client->createDump();
  ```

  ```java Java theme={null}
  client.createDump();
  ```

  ```ruby Ruby theme={null}
  client.create_dump
  ```

  ```go Go theme={null}
  resp, err := client.CreateDump()
  ```

  ```csharp C# theme={null}
  await client.CreateDumpAsync();
  ```

  ```rust Rust theme={null}
  client
    .create_dump()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.createDump { result in
      switch result {
      case .success(let dumpStatus):
          print(dumpStatus)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.createDump();
  ```
</CodeGroup>

#### Response: `202 Accepted`

```json theme={null}
{
  "taskUid": 1,
  "indexUid": null,
  "status": "enqueued",
  "type": "dumpCreation",
  "enqueuedAt": "2022-06-21T16:10:29.217688Z"
}
```

You can use this `taskUid` to get more details on [the status of the task](/reference/api/tasks#get-one-task)