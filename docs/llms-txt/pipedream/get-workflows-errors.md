# Source: https://pipedream.com/docs/rest-api/api-reference/workflows/get-workflows-errors.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workflow Errors

Retrieve up to the last 100 events for a workflow that threw an error. The details of the error, along with the original event data, will be included

#### Endpoint

```
GET /workflows/{workflow_id}/$errors/event_summaries
```

#### Notes and Examples

The event data for events larger than `1KB` may get truncated in the response. If you’re processing larger events, and need to see the full event data, pass `?expand=event`:

```
GET /workflows/{workflow_id}/$errors/event_summaries&expand=event
```

Pass `?limit=N` to retrieve the last **N** events:

```
GET /v1/workflows/{workflow_id}/$errors/event_summaries?expand=event&limit=1
```

<RequestExample>
  ```bash  theme={null}
  curl 'https://api.pipedream.com/v1/workflows/p_abc123/$errors/event_summaries?expand=event&limit=1' \
    -H 'Authorization: Bearer <token>'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "page_info": {
      "total_count": 100,
      "start_cursor": "1606370816223-0",
      "end_cursor": "1606370816223-0",
      "count": 1
    },
    "data": [
      {
        "id": "1606370816223-0",
        "indexed_at_ms": 1606370816223,
        "event": {
          "original_event": {
            "name": "Luke",
            "title": "Jedi"
          },
          "original_context": {
            "id": "1kodJIW7jVnKfvB2yp1OoPrtbFk",
            "ts": "2020-11-26T06:06:44.652Z",
            "workflow_id": "p_abc123",
            "deployment_id": "d_abc123",
            "source_type": "SDK",
            "verified": false,
            "owner_id": "u_abc123",
            "platform_version": "3.1.20"
          },
          "error": {
            "code": "InternalFailure",
            "cellId": "c_abc123",
            "ts": "2020-11-26T06:06:56.077Z",
            "stack": "    at Request.extractError ..."
          },
          "metadata": {
            "emitter_id": "p_abc123",
            "emit_id": "1kodKnAdWGeJyhqYbqyW6lEXVAo",
            "name": "$errors"
          }
        }
      }
    ]
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
