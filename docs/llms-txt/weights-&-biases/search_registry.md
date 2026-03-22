# Source: https://docs.wandb.ai/models/registry/search_registry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Find registry items

> Learn how to search for registries, collections, and artifact versions in the W&B Registry using the global search bar or queries.

Use the [global search bar in the W\&B Registry](./search_registry#search-for-registry-items) to find a registry, collection, artifact version tag, collection tag, or alias. You can use queries to [filter registries, collections, and artifact versions](/models/registry/search_registry#query-registry-items) based on specific criteria using the W\&B Python SDK.

<Info>
  The syntax and available operators you can use to query W\&B Registry is similar, but not identical, to MongoDB queries.
</Info>

Only items that you have permission to view appear in the search results.

## Search for registry items

Use the W\&B App to search for a registry item:

1. Navigate to the W\&B Registry.
2. Specify the search term in the search bar at the top of the page. Press Enter to search.

Search results appear below the search bar if the term you specify matches an existing registry, collection name, artifact version tag, collection tag, or alias.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/registry/search_registry.gif?s=dcce25ebf01774345dcfc2123d60f6b2" alt="Searching within a Registry" width="3250" height="2934" data-path="images/registry/search_registry.gif" />
</Frame>

## Query registry items

Use [`wandb.Api().registries()`](/models/ref/python/public-api/api#registries) and *query predicates* to filter registries, collections, and artifact versions. A query predicate is a condition that specifies the criteria that returned items must meet.

To create a query predicate, use a JSON-like dictionary that consists of [query name](/models/registry/search_registry#filterable-fields), one or more [operators](/models/registry/search_registry#supported-operators), and values. The following code snippet shows the general structure of a query predicate:

```python  theme={null}
{
    "query_name": {
        "operator": value
    }
}
```

The following sections describe the available registry [query names](/models/registry/search_registry#filterable-fields), [supported operators](/models/registry/search_registry#supported-operators), and [example queries](/models/registry/search_registry#example-queries).

### Filterable fields

The following table lists query names you can use based on the type of item you want to filter:

|             | query name                                               |
| ----------- | -------------------------------------------------------- |
| registries  | `name`, `description`, `created_at`, `updated_at`        |
| collections | `name`, `tag`, `description`, `created_at`, `updated_at` |
| versions    | `tag`, `alias`, `created_at`, `updated_at`, `metadata`   |

### Supported operators

W\&B supports the following comparison and logical operators for filtering registry items:

#### Comparison operators

| Operator | Description              |
| -------- | ------------------------ |
| `$eq`    | Equal to                 |
| `$ne`    | Not equal to             |
| `$gt`    | Greater than             |
| `$gte`   | Greater than or equal to |
| `$lt`    | Less than                |
| `$lte`   | Less than or equal to    |

#### Logical operators

| Operator | Description                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------- |
| `$and`   | Performs [AND](https://en.wikipedia.org/wiki/Logical_conjunction) logic to one or more conditions |
| `$or`    | Performs [OR](https://en.wikipedia.org/wiki/Logical_disjunction) logic to one or more conditions  |
| `$nor`   | Performs [NOR](https://en.wikipedia.org/wiki/Logical_NOR) logic to one or more conditions         |
| `$not`   | Performs [NOT](https://en.wikipedia.org/wiki/Negation) logic to a condition                       |

#### Other operators

| Operator    | Description                         |
| ----------- | ----------------------------------- |
| `$regex`    | Regular expression pattern matching |
| `$exists`   | Field exists/doesn't exist          |
| `$contains` | String contains value               |

### Example queries

The following code examples demonstrate some common search scenarios.

To use the `wandb.Api().registries()` method, first import the W\&B Python SDK ([`wandb`](/models/ref/python/)) library:

```python  theme={null}
import wandb

# (Optional) Create an instance of the wandb.Api() class for readability
api = wandb.Api()
```

Filter all registries that contain the string `model`:

```python  theme={null}
# Filter all registries that contain the string `model`
registry_filters = {
    "name": {"$regex": "model"}
}

# Returns an iterable of all registries that match the filters
registries = api.registries(filter=registry_filters)
```

Filter all collections, independent of registry, that contains the string `yolo` in the collection name:

```python  theme={null}
# Filter all collections, independent of registry, that 
# contains the string `yolo` in the collection name
collection_filters = {
    "name": {"$regex": "yolo"}
}

# Returns an iterable of all collections that match the filters
collections = api.registries().collections(filter=collection_filters)
```

Filter all collections, independent of registry, that contains the string `yolo` in the collection name and possesses `cnn` as a tag:

```python  theme={null}
# Filter all collections, independent of registry, that contains the
# string `yolo` in the collection name and possesses `cnn` as a tag
collection_filters = {
    "name": {"$regex": "yolo"},
    "tag": "cnn"
}

# Returns an iterable of all collections that match the filters
collections = api.registries().collections(filter=collection_filters)
```

Find all artifact versions that contains the string `model` and has either the tag `image-classification` or an `latest` alias:

```python  theme={null}
# Find all artifact versions that contains the string `model` and 
# has either the tag `image-classification` or an `latest` alias
registry_filters = {
    "name": {"$regex": "model"}
}

# Use logical $or operator to filter artifact versions
version_filters = {
    "$or": [
        {"tag": "image-classification"},
        {"alias": "production"}
    ]
}

# Returns an iterable of all artifact versions that match the filters
artifacts = api.registries(filter=registry_filters).collections().versions(filter=version_filters)
```

Each item in the `artifacts` iterable in the previous code snippet is an instance of the `Artifact` class. This means that you can access each artifact's attributes, such as `name`, `collection`, `aliases`, `tags`, `created_at`, and more:

```python  theme={null}
for art in artifacts:
    print(f"artifact name: {art.name}")
    print(f"collection artifact belongs to: { art.collection.name}")
    print(f"artifact aliases: {art.aliases}")
    print(f"tags attached to artifact: {art.tags}")
    print(f"artifact created at: {art.created_at}\n")
```

For a complete list of an artifact object's attributes, see the [Artifacts Class](/models/ref/python/experiments/artifact/) in the API Reference docs.

Filter all artifact versions, independent of registry or collection, created between 2024-01-08 and 2025-03-04 at 13:10 UTC:

```python  theme={null}
# Find all artifact versions created between 2024-01-08 and 2025-03-04 at 13:10 UTC. 

artifact_filters = {
    "alias": "latest",
    "created_at" : {"$gte": "2024-01-08", "$lte": "2025-03-04 13:10:00"},
}

# Returns an iterable of all artifact versions that match the filters
artifacts = api.registries().collections().versions(filter=artifact_filters)
```

<Note>
  Specify the date and time in `YYYY-MM-DD HH:MM:SS` format for `created_at` and `updated_at` queries. You can omit the hours, minutes, and seconds if you want to filter by date only.
</Note>
