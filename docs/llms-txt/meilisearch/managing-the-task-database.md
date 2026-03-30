# Managing the task database
Source: https://www.meilisearch.com/docs/learn/async/paginating_tasks

Meilisearch uses a task queue to handle asynchronous operations. This document describes how to navigate long task queues with filters and pagination.

By default, Meilisearch returns a list of 20 tasks for each request when you query the [get tasks endpoint](/reference/api/tasks#get-tasks). This guide shows you how to navigate the task list using query parameters.

<Tip>
  Paginating batches with [the `/batches` route](/reference/api/batches) follows the same rules as paginating tasks.
</Tip>

## Configuring the number of returned tasks

Use the `limit` parameter to change the number of returned tasks:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks?limit=2&from=10
  ```

  ```javascript JS theme={null}
  client.tasks.getTasks({ limit: 2, from: 10 })
  ```

  ```python Python theme={null}
  client.get_tasks({
    'limit': 2,
    'from': 10
  })
  ```

  ```php PHP theme={null}
  $taskQuery = (new TasksQuery())->setLimit(2)->setFrom(10));
  $client->getTasks($taskQuery);
  ```

  ```java Java theme={null}
  TasksQuery query = new TasksQuery()
        .setLimit(2)
        .setFrom(10);

  client.index("movies").getTasks(query);
  ```

  ```ruby Ruby theme={null}
  client.tasks(limit: 2, from: 10)
  ```

  ```go Go theme={null}
  client.GetTasks(&meilisearch.TasksQuery{
    Limit: 2,
    From: 10,
  });
  ```

  ```csharp C# theme={null}
  ResourceResults<TaskInfo> taskResult = await client.GetTasksAsync(new TasksQuery { Limit = 2, From = 10 });
  ```

  ```rust Rust theme={null}
  let mut query = TasksSearchQuery::new(&client)
      .with_limit(2)
      .with_from(10)
      .execute()
      .await
      .unwrap();
  ```

  ```swift Swift theme={null}
  client.getTasks(params: TasksQuery(limit: 2, from: 10)) { result in
    switch result {
    case .success(let taskResult):
      print(taskResult)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.getTasks(params: TasksQuery(limit: 2, from: 10));
  ```
</CodeGroup>

Meilisearch will return a batch of tasks. Each batch of returned tasks is often called a "page" of tasks, and the size of that page is determined by `limit`:

```json theme={null}
{
  "results": [
    …
  ],
  "total": 50,
  "limit": 2,
  "from": 10,
  "next": 8
}
```

It is possible none of the returned tasks are the ones you are looking for. In that case, you will need to use the [get all tasks request response](/reference/api/tasks#response) to navigate the results.

## Navigating the task list with `from` and `next`

Use the `next` value included in the response to your previous query together with `from` to fetch the next set of results:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks?limit=2&from=8
  ```

  ```javascript JS theme={null}
  client.tasks.getTasks({ limit: 2, from: 8 })
  ```

  ```python Python theme={null}
  client.get_tasks({
    'limit': 2,
    'from': 8
  })
  ```

  ```php PHP theme={null}
  $taskQuery = (new TasksQuery())->setLimit(2)->setFrom(8));
  $client->getTasks($taskQuery);
  ```

  ```java Java theme={null}
  TasksQuery query = new TasksQuery()
        .setLimit(2)
        .setFrom(8);

  client.index("movies").getTasks(query);
  ```

  ```ruby Ruby theme={null}
  client.tasks(limit: 2, from: 8)
  ```

  ```go Go theme={null}
  client.GetTasks(&meilisearch.TasksQuery{
    Limit: 2,
    From: 8,
  });
  ```

  ```csharp C# theme={null}
  ResourceResults<TaskInfo> taskResult = await client.GetTasksAsync(new TasksQuery { Limit = 2, From = 8 });
  ```

  ```rust Rust theme={null}
  let mut query = TasksSearchQuery::new(&client)
      .with_limit(2)
      .from(8)
      .execute()
      .await
      .unwrap();
  ```

  ```swift Swift theme={null}
  client.getTasks(params: TasksQuery(limit: 2, from: 8)) { result in
    switch result {
    case .success(let taskResult):
      print(taskResult)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.getTasks(params: TasksQuery(limit: 2, from: 8));
  ```
</CodeGroup>

This will return a new batch of tasks:

```json theme={null}
{
  "results": [
    …
  ],
  "total": 50,
  "limit": 2,
  "from": 8,
  "next": 6
}
```

When the value of `next` is `null`, you have reached the final set of results.

<Tip>
  Use `from` and `limit` together with task filtering parameters to navigate filtered task lists.
</Tip>