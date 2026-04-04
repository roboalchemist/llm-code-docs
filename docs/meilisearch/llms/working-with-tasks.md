# Working with tasks
Source: https://www.meilisearch.com/docs/learn/async/working_with_tasks

In this tutorial, you'll use the Meilisearch API to add documents to an index, and then monitor its status.

[Many Meilisearch operations are processed asynchronously](/learn/async/asynchronous_operations) in a task. Asynchronous tasks allow you to make resource-intensive changes to your Meilisearch project without any downtime for users.

In this tutorial, you'll use the Meilisearch API to add documents to an index, and then monitor its status.

## Requirements

* a running Meilisearch project
* a command-line console

## Adding a task to the task queue

Operations that require indexing, such as adding and updating documents or changing an index's settings, will always generate a task.

Start by creating an index, then add a large number of documents to this index:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/documents'\
    -H 'Content-Type: application/json' \
    --data-binary @movies.json
  ```

  ```javascript JS theme={null}
  const movies = require('./movies.json')
  client.index('movies').addDocuments(movies).then((res) => console.log(res))
  ```

  ```python Python theme={null}
  import json

  json_file = open('movies.json', encoding='utf-8')
  movies = json.load(json_file)
  client.index('movies').add_documents(movies)
  ```

  ```php PHP theme={null}
  $moviesJson = file_get_contents('movies.json');
  $movies = json_decode($moviesJson);

  $client->index('movies')->addDocuments($movies);
  ```

  ```java Java theme={null}
  import com.meilisearch.sdk;
  import org.json.JSONArray;
  import java.nio.file.Files;
  import java.nio.file.Path;

  Path fileName = Path.of("movies.json");
  String moviesJson = Files.readString(fileName);
  Client client = new Client(new Config("http://localhost:7700", "masterKey"));
  Index index = client.index("movies");
  index.addDocuments(moviesJson);
  ```

  ```ruby Ruby theme={null}
  require 'json'

  movies_json = File.read('movies.json')
  movies = JSON.parse(movies_json)
  client.index('movies').add_documents(movies)
  ```

  ```go Go theme={null}
  import (
    "encoding/json"
    "os"
  )

  file, _ := os.ReadFile("movies.json")

  var movies interface{}
  json.Unmarshal([]byte(file), &movies)

  client.Index("movies").AddDocuments(&movies, nil)
  ```

  ```csharp C# theme={null}
  // Make sure to add this using to your code
  using System.IO;

  var jsonDocuments = await File.ReadAllTextAsync("movies.json");
  await client.Index("movies").AddDocumentsJsonAsync(jsonDocuments);
  ```

  ```rust Rust theme={null}
  use meilisearch_sdk::{
    indexes::*,
    client::*,
    search::*,
    settings::*
  };
  use serde::{Serialize, Deserialize};
  use std::{io::prelude::*, fs::File};
  use futures::executor::block_on;

  fn main() { block_on(async move {
    let client = Client::new("http://localhost:7700", Some("masterKey"));

    // reading and parsing the file
    let mut file = File::open("movies.json")
      .unwrap();
    let mut content = String::new();
    file
      .read_to_string(&mut content)
      .unwrap();
    let movies_docs: Vec<Movie> = serde_json::from_str(&content)
      .unwrap();

    // adding documents
    client
      .index("movies")
      .add_documents(&movies_docs, None)
      .await
      .unwrap();
  })}
  ```

  ```swift Swift theme={null}
  let path = Bundle.main.url(forResource: "movies", withExtension: "json")!
  let documents: Data = try Data(contentsOf: path)

  client.index("movies").addDocuments(documents: documents) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  // import 'dart:io';
  // import 'dart:convert';
  final json = await File('movies.json').readAsString();
  await client.index('movies').addDocumentsJson(json);
  ```
</CodeGroup>

Instead of processing your request immediately, Meilisearch will add it to a queue and return a summarized task object:

```json theme={null}
{
  "taskUid": 0,
  "indexUid": "movies",
  "status": "enqueued",
  "type": "documentAdditionOrUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

The summarized task object is confirmation your request has been accepted. It also gives you information you can use to monitor the status of your request, such as the `taskUid`.

<Note>
  You can add documents to a new Meilisearch Cloud index using the Cloud interface. To get the `taskUid` of this task, visit the "Task" overview and look for a "Document addition or update" task associated with your newly created index.
</Note>

## Monitoring task status

Meilisearch processes tasks in the order they were added to the queue. You can check the status of a task using the Meilisearch Cloud interface or the Meilisearch API.

### Monitoring task status in the Meilisearch Cloud interface

Log into your [Meilisearch Cloud](https://meilisearch.com/cloud) account and navigate to your project. Click the "Tasks" link in the project menu:

<img alt="Meilisearch Cloud menu with &#x22;Tasks&#x22; highlighted" />

This will lead you to the task overview, which shows a list of all batches enqueued, processing, and completed in your project:

<img alt="A table listing multiple Meilisearch Cloud tasks" />

All Meilisearch tasks are processed in batches. When the batch containing your task changes its `status` to `succeeded`, Meilisearch has finished processing your request.

If the `status` changes to `failed`, Meilisearch was not able to fulfill your request. Check the object's `error` field for more information.

### Monitoring task status with the Meilisearch API

Use the `taskUid` from your request's response to check the status of a task:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks/1'
  ```

  ```javascript JS theme={null}
  client.tasks.getTask(1)
  ```

  ```python Python theme={null}
  client.get_task(1)
  ```

  ```php PHP theme={null}
  $client->getTask(1);
  ```

  ```java Java theme={null}
  client.getTask(1);
  ```

  ```ruby Ruby theme={null}
  client.task(1)
  ```

  ```go Go theme={null}
  client.GetTask(1);
  ```

  ```csharp C# theme={null}
  TaskInfo task = await client.GetTaskAsync(1);

  ```

  ```rust Rust theme={null}
  let task: Task = client
    .get_task(1)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.getTask(taskUid: 1) { (result) in
        switch result {
        case .success(let task):
            print(task)
        case .failure(let error):
            print(error)
        }
    }
  ```

  ```dart Dart theme={null}
  await client.getTask(1);
  ```
</CodeGroup>

This will return the full task object:

```json theme={null}
{
  "uid": 4,
  "indexUid" :"movie",
  "status": "succeeded",
  "type": "documentAdditionOrUpdate",
  "canceledBy": null,
  "details": {
    …
  },
  "error": null,
  "duration": "PT0.001192S",
  "enqueuedAt": "2022-08-04T12:28:15.159167Z",
  "startedAt": "2022-08-04T12:28:15.161996Z",
  "finishedAt": "2022-08-04T12:28:15.163188Z"
}
```

If the task is still `enqueued` or `processing`, wait a few moments and query the database once again. You may also [set up a webhook listener](/reference/api/webhooks).

When `status` changes to `succeeded`, Meilisearch has finished processing your request.

If the task `status` changes to `failed`, Meilisearch was not able to fulfill your request. Check the task object's `error` field for more information.

## Conclusion

You have seen what happens when an API request adds a task to the task queue, and how to check the status of a that task. Consult the [task API reference](/reference/api/tasks) and the [asynchronous operations explanation](/learn/async/asynchronous_operations) for more information on how tasks work.