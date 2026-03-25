# Source: https://virustotal.readme.io/reference/operation-object.md

# Operations

Asynchronous operations

Not all API operations can be executed synchronously (i.e. the API endpoint can't wait for the operation to complete before returning). In those cases, the API returns an operation object so the client can periodically ask about the operation status. Its attributes are:

* `status`: <*string*> can be one of "aborted", "finished" or "running".

```json
{
  "data": {
    "attributes": {
      "status": "<string>"
    },
    "id": "<string>",
    "type": "operation"
  }
}
```

```json
{
  "data": {
    "attributes": {
      "status": "finished"
    },
    "id": "334b32b7fa5b47c78369600fad91d1b4",
    "links": {
      "self": "https://www.virustotal.com/api/v3/operations/334b32b7fa5b47c78369600fad91d1b4"
    },
    "type": "operation"
  }
}
```