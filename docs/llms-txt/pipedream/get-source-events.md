# Source: https://pipedream.com/docs/rest-api/api-reference/events/get-source-events.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Source Events

Retrieve up to the last 100 events emitted by a source.

#### Endpoint

```
GET /sources/{id}/event_summaries
```

#### Notes and Examples

The event data for events larger than `1KB` may get truncated in the response. If you’re processing larger events, and need to see the full event data, pass `?expand=event`:

```
GET /sources/{id}/event_summaries?expand=event
```

Pass `?limit=N` to retrieve the last **N** events:

```
GET /sources/{id}/event_summaries?limit=10
```

Built with [Mintlify](https://mintlify.com).
