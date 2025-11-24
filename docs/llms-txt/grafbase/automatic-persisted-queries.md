# Source: https://grafbase.com/docs/gateway/configuration/automatic-persisted-queries.md

# Source: https://grafbase.com/docs/gateway/performance/automatic-persisted-queries.md

# Automatic Persisted Queries

Automatic Persisted Queries let you avoid sending the query string each time and help prepare the execution. By default, they are enabled in the Grafbase Gateway. You can [disable them from the configuration](https://grafbase.com/docs/gateway/configuration/automatic-persisted-queries.md).

First, associate a query with a unique identifier: the SHA-256 hash of the query string:

```text
# SHA-256
4ef8d269e7944ef2cd6554ecb3d73164546945cf935806933448905abec554e5
```

```graphql
query {
  __typename
}
```

You can persist the query at any time. Send the following payload, and the system will cache it as part of the operation cache:

```json
{
  "query": "query { __typename }",
  "extensions": {
    "persistedQuery": {
      "version": 1,
      "sha256Hash": "4ef8d269e7944ef2cd6554ecb3d73164546945cf935806933448905abec554e5"
    }
  }
}
```

The next time you execute the same query, omit the query field as follows:

```json
{
  "extensions": {
    "persistedQuery": {
      "version": 1,
      "sha256Hash": "4ef8d269e7944ef2cd6554ecb3d73164546945cf935806933448905abec554e5"
    }
  }
}
```

If Grafbase does not find the query, it returns the following error:

```json
{
  "errors": [
    {
      "message": "Persisted query not found",
      "extensions": {
        "code": "PERSISTED_QUERY_NOT_FOUND"
      }
    }
  ]
}
```

In this case, send the request with the full query string.

## Using GET requests

Grafbase also supports executing GET HTTP requests. You must pass fields as query parameters, encoding their values in JSON format first. To execute a persisted query:

```bash
curl --get 'http://localhost:4000/graphql' \
  --data-urlencode 'extensions={"persistedQuery":{"version":1,"sha256Hash":"4ef8d269e7944ef2cd6554ecb3d73164546945cf935806933448905abec554e5"}}'
```

To register a query:

```bash
curl --get 'http://localhost:4000/graphql' \
  --data-urlencode 'query=query { __typename }' \
  --data-urlencode 'extensions={"persistedQuery":{"version":1,"sha256Hash":"4ef8d269e7944ef2cd6554ecb3d73164546945cf935806933448905abec554e5"}}'
```