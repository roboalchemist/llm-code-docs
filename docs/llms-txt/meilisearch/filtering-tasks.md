# Filtering tasks
Source: https://www.meilisearch.com/docs/learn/async/filtering_tasks

This guide shows you how to use query parameters to filter tasks and obtain a more readable list of asynchronous operations.

Querying the [get tasks endpoint](/reference/api/tasks#get-tasks) returns all tasks that have not been deleted. This unfiltered list may be difficult to parse in large projects.

This guide shows you how to use query parameters to filter tasks and obtain a more readable list of asynchronous operations.

<Tip>
  Filtering batches with [the `/batches` route](/reference/api/batches) follows the same rules as filtering tasks. Keep in mind that many `/batches` parameters such as `uids` target the tasks included in batches, instead of the batches themselves.
</Tip>

## Requirements

* a command-line terminal
* a running Meilisearch project

## Filtering tasks with a single parameter

Use the get tasks endpoint to fetch all `canceled` tasks:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks?statuses=failed'
  ```

  ```javascript JS theme={null}
  client.tasks.getTasks({ statuses: ['failed', 'canceled'] })
  ```

  ```python Python theme={null}
  client.get_tasks({'statuses': ['failed', 'canceled']})
  ```

  ```php PHP theme={null}
  $client->getTasks((new TasksQuery())->setStatuses(['failed', 'canceled']));
  ```

  ```java Java theme={null}
  TasksQuery query = new TasksQuery().setStatuses(new String[] {"failed", "canceled"});
  client.getTasks(query);
  ```

  ```ruby Ruby theme={null}
  client.get_tasks(statuses: ['failed', 'canceled'])
  ```

  ```go Go theme={null}
  client.GetTasks(&meilisearch.TasksQuery{
    Statuses: []meilisearch.TaskStatus{
      meilisearch.TaskStatusFailed,
      meilisearch.TaskStatusCanceled,
    },
  })
  ```

  ```csharp C# theme={null}
  await client.GetTasksAsync(new TasksQuery { Statuses = new List<TaskInfoStatus> { TaskInfoStatus.Failed, TaskInfoStatus.Canceled } });
  ```

  ```rust Rust theme={null}
  let mut query = TasksQuery::new(&client);
  let tasks = query
    .with_statuses(["failed"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.getTasks(params: TasksQuery(statuses: [.failed, .canceled])) { result in
    switch result {
    case .success(let taskResult):
      print(taskResult)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.getTasks(
    params: TasksQuery(
      statuses: ['failed', 'canceled'],
    ),
  );
  ```
</CodeGroup>

Use a comma to separate multiple values and fetch both `canceled` and `failed` tasks:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks?statuses=failed,canceled'
  ```

  ```rust Rust theme={null}
  let mut query = TasksQuery::new(&client);
  let tasks = query
    .with_statuses(["failed", "canceled"])
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

You may filter tasks based on `uid`, `status`, `type`, `indexUid`, `canceledBy`, or date. Consult the API reference for a full list of task filtering parameters.

## Combining filters

Use the ampersand character (`&`) to combine filters, equivalent to a logical `AND`:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks?indexUids=movies&types=documentAdditionOrUpdate,documentDeletion&statuses=processing'
  ```

  ```javascript JS theme={null}
  client.tasks.getTasks({
    indexUids: ['movies'],
    types: ['documentAdditionOrUpdate','documentDeletion'],
    statuses: ['processing']
  })
  ```

  ```python Python theme={null}
  client.get_tasks(
    {
        'indexUids': 'movies',
        'types': ['documentAdditionOrUpdate', 'documentDeletion'],
        'statuses': ['processing'],
    }
  )
  ```

  ```php PHP theme={null}
  $client->getTasks(
    (new TasksQuery())
      ->setStatuses(['processing'])
      ->setUids(['movies'])
      ->setTypes(['documentAdditionOrUpdate', 'documentDeletion'])
  );
  ```

  ```java Java theme={null}
  TasksQuery query =
          new TasksQuery()
                  .setStatuses(new String[] {"processing"})
                  .setTypes(new String[] {"documentAdditionOrUpdate", "documentDeletion"})
                  .setIndexUids(new String[] {"movies"});

  client.getTasks(query);
  ```

  ```ruby Ruby theme={null}
  client.get_tasks(index_uids: ['movies'], types: ['documentAdditionOrUpdate', 'documentDeletion'], statuses: ['processing'])
  ```

  ```go Go theme={null}
  client.GetTasks(&meilisearch.TasksQuery{
    IndexUIDS: []string{"movie"},
    Types:     []meilisearch.TaskType{
      meilisearch.TaskTypeDocumentAdditionOrUpdate,
      meilisearch.TaskTypeDocumentDeletion,
    },
    Statuses:  []meilisearch.TaskStatus{
      meilisearch.TaskStatusProcessing,
    },
  })
  ```

  ```csharp C# theme={null}
  var query = new TasksQuery { IndexUids = new List<string> { "movies" }, Types = new List<TaskInfo> { TaskInfo.DocumentAdditionOrUpdate, TaskInfo.DocumentDeletion }, Statuses = new List<TaskInfoStatus> { TaskInfoStatus.Processing } };

  await client.GetTasksAsync(query);
  ```

  ```rust Rust theme={null}
  let mut query = TasksQuery::new(&client);
  let tasks = query
    .with_index_uids(["movies"])
    .with_types(["documentAdditionOrUpdate","documentDeletion"])
    .with_statuses(["processing"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.getTasks(params: TasksQuery(indexUids: "movies", types: ["documentAdditionOrUpdate", "documentDeletion"], statuses: ["processing"])) { result in
    switch result {
    case .success(let taskResult):
      print(taskResult)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.getTasks(
    params: TasksQuery(
      indexUids: ['movies'],
      types: ['documentAdditionOrUpdate', 'documentDeletion'],
      statuses: ['processing'],
    ),
  );
  ```
</CodeGroup>

This code sample returns all tasks in the `movies` index that have the type `documentAdditionOrUpdate` or `documentDeletion` and have the `status` of `processing`.

<Warning>
  **`OR` operations between different filters are not supported.** For example, you cannot view tasks which have a type of `documentAddition` **or** a status of `failed`.
</Warning>