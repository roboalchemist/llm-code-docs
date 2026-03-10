# Launch Meilisearch
./meilisearch --master-key="aSampleMasterKey"
```

<Note>
  This tutorial uses `aSampleMasterKey` as a master key, but you may change it to any alphanumeric string with 16 or more bytes. In most cases, one character corresponds to one byte.
</Note>

You should see something like this in response:

```
888b     d888          d8b 888 d8b                                            888
8888b   d8888          Y8P 888 Y8P                                            888
88888b.d88888              888                                                888
888Y88888P888  .d88b.  888 888 888 .d8888b   .d88b.   8888b.  888d888 .d8888b 88888b.
888 Y888P 888 d8P  Y8b 888 888 888 88K      d8P  Y8b     "88b 888P"  d88P"    888 "88b
888  Y8P  888 88888888 888 888 888 "Y8888b. 88888888 .d888888 888    888      888  888
888   "   888 Y8b.     888 888 888      X88 Y8b.     888  888 888    Y88b.    888  888
888       888  "Y8888  888 888 888  88888P'  "Y8888  "Y888888 888     "Y8888P 888  888

Database path:       "./data.ms"
Server listening on: "localhost:7700"
```

You now have a Meilisearch instance running in your terminal window. Keep this window open for the rest of this tutorial.

<Note>
  The above command uses the `--master-key` configuration option to secure Meilisearch. Setting a master key is optional but strongly recommended in development environments. Master keys are mandatory in production environments.
</Note>

To learn more about securing Meilisearch, refer to the [security tutorial](/learn/security/basic_security).

## Add documents

In this quick start, you will search through a collection of movies.

To follow along, first click this link to download the file: <a href="https://www.meilisearch.com/movies.json">movies.json</a>. Then, move the downloaded file into your working directory.

<Note>
  Meilisearch accepts data in JSON, NDJSON, and CSV formats.
</Note>

Open a new terminal window and run the following command:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/documents?primaryKey=id' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer aSampleMasterKey' \
    --data-binary @movies.json
  ```

  ```javascript JS theme={null}
  // With npm:
  // npm install meilisearch

  // Or with pnpm:
  // pnpm add meilisearch

  // In your .js file:
  // With the `require` syntax:
  const { MeiliSearch } = require('meilisearch')
  const movies = require('./movies.json')
  // With the `import` syntax:
  import { MeiliSearch } from 'meilisearch'
  import movies from './movies.json'

  const client = new MeiliSearch({
    host: 'http://localhost:7700',
    apiKey: 'aSampleMasterKey'
  })
  client.index('movies').addDocuments(movies)
    .then((res) => console.log(res))
  ```

  ```python Python theme={null}
  # In the command line:
  # pip3 install meilisearch

  # In your .py file:
  import meilisearch
  import json

  client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

  json_file = open('movies.json', encoding='utf-8')
  movies = json.load(json_file)
  client.index('movies').add_documents(movies)
  ```

  ```php PHP theme={null}
  /**
   * Using `meilisearch-php` with the Guzzle HTTP client, in the command line:
   *   composer require meilisearch/meilisearch-php \
   *     guzzlehttp/guzzle \
   *     http-interop/http-factory-guzzle:^1.0
   */

  /**
   * In your PHP file:
   */
  <?php

  require_once __DIR__ . '/vendor/autoload.php';

  use Meilisearch\Client;

  $client = new Client('http://localhost:7700', 'aSampleMasterKey');

  $movies_json = file_get_contents('movies.json');
  $movies = json_decode($movies_json);

  $client->index('movies')->addDocuments($movies);
  ```

  ```java Java theme={null}
  // For Maven:
  // Add the following code to the `<dependencies>` section of your project:
  //
  // <dependency>
  //   <groupId>com.meilisearch.sdk</groupId>
  //   <artifactId>meilisearch-java</artifactId>
  //   <version>0.18.0</version>
  //   <type>pom</type>
  // </dependency>

  // For Gradle
  // Add the following line to the `dependencies` section of your `build.gradle`:
  //
  // implementation 'com.meilisearch.sdk:meilisearch-java:0.18.0'

  // In your .java file:
  import com.meilisearch.sdk;
  import java.nio.file.Files;
  import java.nio.file.Path;

  Path fileName = Path.of("movies.json");
  String moviesJson = Files.readString(fileName);
  Client client = new Client(new Config("http://localhost:7700", "aSampleMasterKey"));
  Index index = client.index("movies");
  index.addDocuments(moviesJson);
  ```

  ```ruby Ruby theme={null}
  # In the command line:
  # bundle add meilisearch

  # In your .rb file:
  require 'json'
  require 'meilisearch'

  client = MeiliSearch::Client.new('http://localhost:7700', 'aSampleMasterKey')

  movies_json = File.read('movies.json')
  movies = JSON.parse(movies_json)

  client.index('movies').add_documents(movies)
  ```

  ```go Go theme={null}
  // In the command line:
  // go get -u github.com/meilisearch/meilisearch-go

  // In your .go file:
  package main

  import (
    "os"
    "encoding/json"
    "io"

    "github.com/meilisearch/meilisearch-go"
  )

  func main() {
    client := meilisearch.New("http://localhost:7700", meilisearch.WithAPIKey("masterKey"))

    jsonFile, _ := os.Open("movies.json")
    defer jsonFile.Close()

    byteValue, _ := io.ReadAll(jsonFile)
    var movies []map[string]interface{}
    json.Unmarshal(byteValue, &movies)

    _, err := client.Index("movies").AddDocuments(movies, nil)
    if err != nil {
        panic(err)
    }
  }
  ```

  ```csharp C# theme={null}
  // In the command line:
  // dotnet add package Meilisearch

  // In your .cs file:
  using System.IO;
  using System.Text.Json;
  using Meilisearch;
  using System.Threading.Tasks;
  using System.Collections.Generic;

  namespace Meilisearch_demo
  {
      public class Movie
      {
          public string Id { get; set; }
          public string Title { get; set; }
          public string Poster { get; set; }
          public string Overview { get; set; }
          public IEnumerable<string> Genres { get; set; }
      }

      internal class Program
      {
          static async Task Main(string[] args)
          {
              MeilisearchClient client = new MeilisearchClient("http://localhost:7700", "aSampleMasterKey");
              var options = new JsonSerializerOptions
              {
                  PropertyNameCaseInsensitive = true
              };

              string jsonString = await File.ReadAllTextAsync("movies.json");
              var movies = JsonSerializer.Deserialize<IEnumerable<Movie>>(jsonString, options);

              var index = client.Index("movies");
              await index.AddDocumentsAsync<Movie>(movies);
          }
      }
  }
  ```

  ```text Rust theme={null}
  // In your .toml file:
    [dependencies]
    meilisearch-sdk = "0.32.0"
    # futures: because we want to block on futures
    futures = "0.3"
    # serde: required if you are going to use documents
    serde = { version="1.0",   features = ["derive"] }
    # serde_json: required in some parts of this guide
    serde_json = "1.0"



  // In your .rs file:
  // Documents in the Rust library are strongly typed
  #[derive(Serialize, Deserialize)]
  struct Movie {
    id: i64,
    title: String,
    poster: String,
    overview: String,
    release_date: i64,
    genres: Vec<String>
  }

  // You will often need this `Movie` struct in other parts of this documentation. (you will have to change it a bit sometimes)
  // You can also use schemaless values, by putting a `serde_json::Value` inside your own struct like this:
  #[derive(Serialize, Deserialize)]
  struct Movie {
    id: i64,
    #[serde(flatten)]
    value: serde_json::Value,
  }

  // Then, add documents into the index:
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
    let client = Client::new("http://localhost:7700", Some("aSampleMasterKey"));

    // Reading and parsing the file
    let mut file = File::open("movies.json")
      .unwrap();
    let mut content = String::new();
    file
      .read_to_string(&mut content)
      .unwrap();
    let movies_docs: Vec<Movie> = serde_json::from_str(&content)
      .unwrap();

    // Adding documents
    client
      .index("movies")
      .add_documents(&movies_docs, None)
      .await
      .unwrap();
  })}
  ```

  ```swift Swift theme={null}
  // Add this to your `Package.swift`
  dependencies: [
    .package(url: "https://github.com/meilisearch/meilisearch-swift.git", from: "0.17.0")
  ]

  // In your .swift file:
  let path = Bundle.main.url(forResource: "movies", withExtension: "json")!
  let documents: Data = try Data(contentsOf: path)
  let client = try MeiliSearch(host: "http://localhost:7700", apiKey: "aSampleMasterKey")

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
  // In the command line:
  // dart pub add meilisearch
  // In your .dart file:
  import 'package:meilisearch/meilisearch.dart';
  import 'dart:io';
  import 'dart:convert';
  var client = MeiliSearchClient('http://localhost:7700', 'aSampleMasterKey');
  final json = await File('movies.json').readAsString();
  await client.index('movies').addDocumentsJson(json);
  ```
</CodeGroup>

Meilisearch stores data in the form of discrete records, called [documents](/learn/getting_started/documents). Each document is an object composed of multiple fields, which are pairs of one attribute and one value:

```json theme={null}
{
  "attribute": "value"
}
```

Documents are grouped into collections, called [indexes](/learn/getting_started/indexes).

The previous command added documents from `movies.json` to a new index called `movies`. It also set `id` as the primary key.

<Note>
  Every index must have a [primary key](/learn/getting_started/primary_key#primary-field), an attribute shared across all documents in that index. If you try adding documents to an index and even a single one is missing the primary key, none of the documents will be stored.

  If you do not explicitly set the primary key, Meilisearch [infers](/learn/getting_started/primary_key#meilisearch-guesses-your-primary-key) it from your dataset.
</Note>

After adding documents, you should receive a response like this:

```json theme={null}
{
    "taskUid": 0,
    "indexUid": "movies",
    "status": "enqueued",
    "type": "documentAdditionOrUpdate",
    "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

Use the returned `taskUid` to [check the status](/reference/api/tasks) of your documents:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks/0' \
    -H 'Authorization: Bearer aSampleMasterKey'
  ```

  ```javascript JS theme={null}
  client.tasks.getTask(0)
  ```

  ```python Python theme={null}
  client.get_task(0)
  ```

  ```php PHP theme={null}
  $client->getTask(0);
  ```

  ```java Java theme={null}
  client.getTask(0);
  ```

  ```ruby Ruby theme={null}
  client.task(0)
  ```

  ```go Go theme={null}
  client.GetTask(0)
  ```

  ```csharp C# theme={null}
  TaskInfo task = await client.GetTaskAsync(0);
  ```

  ```rust Rust theme={null}
  client
    .get_task(0)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.getTask(taskUid: 0) { (result) in
      switch result {
      case .success(let task):
          print(task)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.getTask(0);
  ```
</CodeGroup>

<Note>
  Most database operations in Meilisearch are [asynchronous](/learn/async/asynchronous_operations). Rather than being processed instantly, **API requests are added to a queue and processed one at a time**.
</Note>

If the document addition is successful, the response should look like this:

```json theme={null}
{
   "uid": 0,
   "indexUid": "movies",
   "status": "succeeded",
   "type": "documentAdditionOrUpdate",
   "canceledBy": null,
   "details": {
      "receivedDocuments": 19547,
      "indexedDocuments": 19547
   },
   "error": null,
   "duration": "PT0.030750S",
   "enqueuedAt": "2021-12-20T12:39:18.349288Z",
   "startedAt": "2021-12-20T12:39:18.352490Z",
   "finishedAt": "2021-12-20T12:39:18.380038Z"
}
```

If `status` is `enqueued` or `processing`, all you have to do is wait a short time and check again. Proceed to the next step once the task `status` has changed to `succeeded`.

## Search

Now that you have Meilisearch set up, you can start searching!

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/movies/search' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer aSampleMasterKey' \
    --data-binary '{ "q": "botman" }'
  ```

  ```javascript JS theme={null}
  client.index('movies').search('botman').then((res) => console.log(res))
  ```

  ```python Python theme={null}
  client.index('movies').search('botman')
  ```

  ```php PHP theme={null}
  $client->index('movies')->search('botman');
  ```

  ```java Java theme={null}
  client.index("movies").search("botman");
  ```

  ```ruby Ruby theme={null}
  client.index('movies').search('botman')
  ```

  ```go Go theme={null}
  client.Index("movies").Search("botman", &meilisearch.SearchRequest{})
  ```

  ```csharp C# theme={null}
  MeilisearchClient client = new MeilisearchClient("http://localhost:7700", "masterKey");
  var index = client.Index("movies");

  var movies = await index.SearchAsync<Movie>("botman");
  foreach (var movie in movies.Hits)
  {
      Console.WriteLine(movie.Title);
  }
  ```

  ```rust Rust theme={null}
  // You can build a `SearchQuery` and execute it later:
  let query: SearchQuery = SearchQuery::new(&movies)
    .with_query("botman")
    .build();

  let results: SearchResults<Movie> = client
    .index("movies")
    .execute_query(&query)
    .await
    .unwrap();

  // You can build a `SearchQuery` and execute it directly:
  let results: SearchResults<Movie> = SearchQuery::new(&movies)
    .with_query("botman")
    .execute()
    .await
    .unwrap();

  // You can search in an index directly:
  let results: SearchResults<Movie> = client
    .index("movies")
    .search()
    .with_query("botman")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("movies").search(SearchParameters(query: "botman")) { (result) in
      switch result {
      case .success(let searchResult):
          print(searchResult)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.index('movies').search('botman');
  ```
</CodeGroup>

<Note>
  This tutorial queries Meilisearch with the master key. In production environments, this is a security risk. Prefer using API keys to access Meilisearch's API in any public-facing application.
</Note>

In the above code sample, the parameter `q` represents the search query. This query instructs Meilisearch to search for `botman` in the documents you added in [the previous step](#add-documents):

```json theme={null}
{
  "hits": [
    {
      "id": 29751,
      "title": "Batman Unmasked: The Psychology of the Dark Knight",
      "poster": "https://image.tmdb.org/t/p/w1280/jjHu128XLARc2k4cJrblAvZe0HE.jpg",
      "overview": "Delve into the world of Batman and the vigilante justice tha",
      "release_date": "2008-07-15"
    },
    {
      "id": 471474,
      "title": "Batman: Gotham by Gaslight",
      "poster": "https://image.tmdb.org/t/p/w1280/7souLi5zqQCnpZVghaXv0Wowi0y.jpg",
      "overview": "ve Victorian Age Gotham City, Batman begins his war on crime",
      "release_date": "2018-01-12"
    },
    …
  ],
  "estimatedTotalHits": 66,
  "query": "botman",
  "limit": 20,
  "offset": 0,
  "processingTimeMs": 12
}
```

By default, Meilisearch only returns the first 20 results for a search query. You can change this using the [`limit` parameter](/reference/api/search#limit).

## What's next?

You now know how to install Meilisearch, create an index, add documents, check the status of an asynchronous task, and make a search request.

If you'd like to search through the documents you just added using a clean browser interface rather than the terminal, you can do so with [our built-in search preview](/learn/getting_started/search_preview). You can also [learn how to quickly build a front-end interface](/guides/front_end/front_end_integration) of your own.

For a more advanced approach, consult the [API reference](/reference/api/overview).