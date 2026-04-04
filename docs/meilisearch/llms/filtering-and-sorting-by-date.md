# Filtering and sorting by date
Source: https://www.meilisearch.com/docs/learn/filtering_and_sorting/working_with_dates

Learn how to index documents with chronological data, and how to sort and filter search results based on time.

In this guide, you will learn about Meilisearch's approach to date and time values, how to prepare your dataset for indexing, and how to chronologically sort and filter search results.

## Preparing your documents

To filter and sort search results chronologically, your documents must have at least one field containing a [UNIX timestamp](https://kb.narrative.io/what-is-unix-time). You may also use a string with a date in a format that can be sorted lexicographically, such as `"2025-01-13"`.

As an example, consider a database of video games. In this dataset, the release year is formatted as a timestamp:

```json theme={null}
[
  {
    "id": 0,
    "title": "Return of the Obra Dinn",
    "genre": "adventure",
    "release_timestamp": 1538949600
  },
  {
    "id": 1,
    "title": "The Excavation of Hob's Barrow",
    "genre": "adventure",
    "release_timestamp": 1664316000
  },
  {
    "id": 2,
    "title": "Bayonetta 2",
    "genre": "action",
    "release_timestamp": 1411164000
  }
]
```

Once all documents in your dataset have a date field, [index your data](/reference/api/documents#add-or-replace-documents) as usual. The example below adds a <a href="/assets/datasets/videogames.json">videogame dataset</a> to a `games` index:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -x POST 'MEILISEARCH_URL/indexes/games/documents' \
    -h 'content-type: application/json' \
    --data-binary @games.json
  ```

  ```javascript JS theme={null}
  const games = require('./games.json')
  client.index('games').addDocuments(games).then((res) => console.log(res))
  ```

  ```python Python theme={null}
  import json

  json_file = open('./games.json', encoding='utf-8')
  games = json.load(json_file)
  client.index('games').add_documents(games)
  ```

  ```php PHP theme={null}
  $gamesJson = file_get_contents('games.json');
  $games = json_decode($gamesJson);

  $client->index('games')->addDocuments($games);
  ```

  ```java Java theme={null}
  import com.meilisearch.sdk;
  import org.json.JSONArray;
  import java.nio.file.Files;
  import java.nio.file.Path;

  Path fileName = Path.of("games.json");
  String gamesJson = Files.readString(fileName);
  Index index = client.index("games");
  index.addDocuments(gamesJson);
  ```

  ```ruby Ruby theme={null}
  require 'json'

  games = JSON.parse(File.read('games.json'))
  client.index('games').add_documents(games)
  ```

  ```go Go theme={null}
  jsonFile, _ := os.Open("games.json")
  defer jsonFile.Close()

  byteValue, _ := io.ReadAll(jsonFile)
  var games []map[string]interface{}
  json.Unmarshal(byteValue, &games)

  client.Index("games").AddDocuments(games, nil)
  ```

  ```csharp C# theme={null}
  string jsonString = await File.ReadAllTextAsync("games.json");
  var games = JsonSerializer.Deserialize<IEnumerable<Movie>>(jsonString, options);
  var index = client.Index("games");
  await index.AddDocumentsAsync<Movie>(games);
  ```

  ```rust Rust theme={null}
  let mut file = File::open("games.json")
    .unwrap();
  let mut content = String::new();
  file
    .read_to_string(&mut content)
    .unwrap();
  let docs: Vec<Game> = serde_json::from_str(&content)
    .unwrap();

  client
    .index("games")
    .add_documents(&docs, None)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let path = Bundle.main.url(forResource: "games", withExtension: "json")!
  let documents: Data = try Data(contentsOf: path)

  client.index("games").addDocuments(documents: documents) { (result) in
    switch result {
    case .success(let task):
        print(task)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  //import 'dart:io';
  //import 'dart:convert';
  final json = await File('games.json').readAsString();
  await client.index('games').addDocumentsJson(json);
  ```
</CodeGroup>

## Filtering by date

To filter search results based on their timestamp, add your document's timestamp field to the list of [`filterableAttributes`](/reference/api/settings#update-filterable-attributes):

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/games/settings/filterable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "release_timestamp"
    ]'
  ```

  ```javascript JS theme={null}
  client.index('games').updateFilterableAttributes(['release_timestamp'])
  ```

  ```python Python theme={null}
  client.index('games').update_filterable_attributes(['release_timestamp'])
  ```

  ```php PHP theme={null}
  $client->index('games')->updateFilterableAttributes(['release_timestamp']);
  ```

  ```java Java theme={null}
  client.index("movies").updateFilterableAttributesSettings(new String[] { "release_timestamp" });
  ```

  ```ruby Ruby theme={null}
  client.index('games').update_filterable_attributes(['release_timestamp'])
  ```

  ```go Go theme={null}
  filterableAttributes := []interface{}{"release_timestamp"}
  client.Index("games").UpdateFilterableAttributes(&filterableAttributes)
  ```

  ```csharp C# theme={null}
  await client.Index("games").UpdateFilterableAttributesAsync(new string[] { "release_timestamp" });
  ```

  ```rust Rust theme={null}
  let settings = Settings::new()
    .with_filterable_attributes(["release_timestamp"]);

  let task: TaskInfo = client
    .index("games")
    .set_settings(&settings)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("games").updateFilterableAttributes(["release_timestamp"]) { (result) in
    switch result {
    case .success(let task):
        print(task)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('games')
      .updateFilterableAttributes(['release_timestamp']);
  ```
</CodeGroup>

Once you have configured `filterableAttributes`, you can filter search results by date. The following query only returns games released between 2018 and 2022:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/games/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "",
      "filter": "release_timestamp >= 1514761200 AND release_timestamp < 1672527600"
    }'
  ```

  ```javascript JS theme={null}
  client.index('games').search('', {
    filter: 'release_timestamp >= 1514761200 AND release_timestamp < 1672527600'
  })
  ```

  ```python Python theme={null}
  client.index('games').search('', {
    'filter': 'release_timestamp >= 1514761200 AND release_timestamp < 1672527600'
  })
  ```

  ```php PHP theme={null}
  $client->index('games')->search('', [
    'filter' => ['release_timestamp >= 1514761200 AND release_timestamp < 1672527600']
  ]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("").filter(new String[] {"release_timestamp >= 1514761200 AND release_timestamp < 1672527600"}).build();
  client.index("games").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('games').search('', {
    filter: 'release_timestamp >= 1514761200 AND release_timestamp < 1672527600'
  })
  ```

  ```go Go theme={null}
  client.Index("games").Search("", &meilisearch.SearchRequest{
    Filter: "release_timestamp >= 1514761200 AND release_timestamp < 1672527600",
  })
  ```

  ```csharp C# theme={null}
  var filters = new SearchQuery() { Filter = "release_timestamp >= 1514761200 AND release_timestamp < 1672527600" };
  var games = await client.Index("games").SearchAsync<Game>("", filters);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Game> = client
    .index("games")
    .search()
    .with_filter("release_timestamp >= 1514761200 AND release_timestamp < 1672527600")
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
    query: "",
    filter: "release_timestamp >= 1514761200 AND release_timestamp < 1672527600"
  )
  client.index("games").search(searchParameters) { (result: Result<Searchable<Game>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
        print(searchResult)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client.index('games').search(
        '',
        SearchQuery(
          filterExpression: Meili.and([
            Meili.gte(
              'release_timestamp'.toMeiliAttribute(),
              Meili.value(DateTime(2017, 12, 31, 23, 0)),
            ),
            Meili.lt(
              'release_timestamp'.toMeiliAttribute(),
              Meili.value(DateTime(2022, 12, 31, 23, 0)),
            ),
          ]),
        ),
      );
  ```
</CodeGroup>

## Sorting by date

To sort search results chronologically, add your document's timestamp field to the list of [`sortableAttributes`](/reference/api/settings#update-sortable-attributes):

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/games/settings/sortable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "release_timestamp"
    ]'
  ```

  ```javascript JS theme={null}
  client.index('games').updateSortableAttributes(['release_timestamp'])
  ```

  ```python Python theme={null}
  client.index('games').update_sortable_attributes(['release_timestamp'])
  ```

  ```php PHP theme={null}
  $client->index('games')->updateSortableAttributes(['release_timestamp']);
  ```

  ```java Java theme={null}
  Settings settings = new Settings();
  settings.setSortableAttributes(new String[] {"release_timestamp"});
  client.index("games").updateSettings(settings);
  ```

  ```ruby Ruby theme={null}
  client.index('games').update_sortable_attributes(['release_timestamp'])
  ```

  ```go Go theme={null}
  sortableAttributes := []string{"release_timestamp","author"}
  client.Index("games").UpdateSortableAttributes(&sortableAttributes)
  ```

  ```csharp C# theme={null}
  await client.Index("games").UpdateSortableAttributesAsync(new string[] { "release_timestamp" });
  ```

  ```rust Rust theme={null}
  let settings = Settings::new()
    .with_sortable_attributes(["release_timestamp"]);

  let task: TaskInfo = client
    .index("games")
    .set_settings(&settings)
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.index("games").updateSortableAttributes(["release_timestamp"]) { (result) in
    switch result {
    case .success(let task):
      print(task)
    case .failure(let error):
      print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('games')
      .updateSortableAttributes(['release_timestamp']);
  ```
</CodeGroup>

Once you have configured `sortableAttributes`, you can sort your search results based on their timestamp. The following query returns all games sorted from most recent to oldest:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X POST 'MEILISEARCH_URL/indexes/games/search' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "q": "",
      "sort": ["release_timestamp:desc"]
    }'
  ```

  ```javascript JS theme={null}
  client.index('games').search('', {
    sort: ['release_timestamp:desc'],
  })
  ```

  ```python Python theme={null}
  client.index('games').search('', {
    'sort': ['release_timestamp:desc']
  })
  ```

  ```php PHP theme={null}
  $client->index('games')->search('', ['sort' => ['release_timestamp:desc']]);
  ```

  ```java Java theme={null}
  SearchRequest searchRequest = SearchRequest.builder().q("").sort(new String[] {"release_timestamp:desc"}).build();
  client.index("games").search(searchRequest);
  ```

  ```ruby Ruby theme={null}
  client.index('games').search('', sort: ['release_timestamp:desc'])
  ```

  ```go Go theme={null}
  client.Index("games").Search("", &meilisearch.SearchRequest{
    Sort: []string{
      "release_timestamp:desc",
    },
  })
  ```

  ```csharp C# theme={null}
  SearchQuery sort = new SearchQuery() { Sort = new string[] { "release_timestamp:desc" }};
  await client.Index("games").SearchAsync<Game>("", sort);
  ```

  ```rust Rust theme={null}
  let results: SearchResults<Game> = client
    .index("games")
    .search()
    .with_sort(["release_timestamp:desc"])
    .execute()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  let searchParameters = SearchParameters(
    query: "",
    sort: ["release_timestamp:desc"],
  )

  client.index("games").search(searchParameters) { (result: Result<Searchable<Game>, Swift.Error>) in
    switch result {
    case .success(let searchResult):
        print(searchResult)
    case .failure(let error):
        print(error)
    }
  }
  ```

  ```dart Dart theme={null}
  await client
      .index('games')
      .search('', SearchQuery(sort: ['release_timestamp:desc']));
  ```
</CodeGroup>