# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_fetch_step.md

### WorkflowFetchStep

A fetch function step. Retrieves data from an external source and merges it into the workflow's `data` scope for use in later steps. Read more in the [docs](https://docs.knock.app/designing-workflows/fetch-function).

#### Attributes

- **conditions** (object) - A conditions object that describes one or more conditions to be met in order for the step to be executed.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - A request template for a fetch function step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "name": "Fetch step",
  "ref": "fetch_1",
  "settings": {
    "body": null,
    "headers": [
      {
        "key": "X-API-Key",
        "value": "1234567890"
      }
    ],
    "method": "get",
    "query_params": [
      {
        "key": "key",
        "value": "value"
      }
    ],
    "url": "https://example.com"
  },
  "type": "http_fetch"
}
```

