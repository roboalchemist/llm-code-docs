# Source: https://pipedream.com/docs/rest-api/api-reference/workflows/get-workflows-emits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workflow Emits

Retrieve up to the last 100 events emitted from a workflow using [`$send.emit()`](/workflows/data-management/destinations/emit/#emit-events).

#### Endpoint

```
GET /workflows/{workflow_id}/event_summaries
```

#### Notes and Examples

The event data for events larger than `1KB` may get truncated in the response. If you’re retrieving larger events, and need to see the full event data, pass `?expand=event`:

```
GET /workflows/{workflow_id}/event_summaries&expand=event
```

Pass `?limit=N` to retrieve the last **N** events:

```
GET /v1/workflows/{workflow_id}/event_summaries?expand=event&limit=1
```

<RequestExample>
  ```bash  theme={null}
  curl 'https://api.pipedream.com/v1/workflows/p_abc123/event_summaries?expand=event&limit=1' \
    -H 'Authorization: Bearer <token>'
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "page_info": {
      "total_count": 1,
      "start_cursor": "1606511826306-0",
      "end_cursor": "1606511826306-0",
      "count": 1
    },
    "data": [
      {
        "id": "1606511826306-0",
        "indexed_at_ms": 1606511826306,
        "event": {
          "raw_event": {
            "name": "Luke",
            "title": "Jedi"
          }
        },
        "metadata": {
          "emit_id": "1ktF96gAMsLqdYSRWYL9KFS5QqW",
          "name": "",
          "emitter_id": "p_abc123"
        }
      }
    ]
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
