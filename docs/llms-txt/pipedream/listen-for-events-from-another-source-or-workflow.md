# Source: https://pipedream.com/docs/rest-api/api-reference/subscription/listen-for-events-from-another-source-or-workflow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Listen for events from another source or workflow

You can configure a source or workflow to receive events from any number of other workflows or sources. For example, if you want a single workflow to run on 10 different RSS sources, you can configure the workflow to *listen* for events from those 10 sources.

#### Endpoint

```
POST /subscriptions?emitter_id={emitting_component_id}&event_name={event_name}&listener_id={receiving_source_id}
```

#### Parameters

<ParamField body="emitter_id" type="string" required>
  The ID of the workflow or component emitting events. Events from this component trigger the receiving component / workflow.

  `emitter_id` also accepts glob patterns that allow you to subscribe to *all* workflows or components:

* `p_*`: Listen to events from all workflows
* `dc_*`: Listen to events from all event sources

  [See the component endpoints](/rest-api/#components) for information on how to retrieve the ID of existing components. You can retrieve the ID of your workflow in your workflow’s URL - it’s the string `p_2gCPml` in `https://pipedream.com/@dylan/example-rss-sql-workflow-p_2gCPml/edit`.
</ParamField>

***

<ParamField body="event_name" type="string">
  **Only pass `event_name` when you’re listening for events on a custom channel, with the name of the custom channel**:

  ```
  event_name=<custom_channel>
  ```

  See [the `this.$emit` docs](/components/contributing/api/#emit) for more information on how to emit events on custom channels.

  Pipedream also exposes channels for logs and errors:

* `$errors`: Any errors thrown by workflows or sources are emitted to this stream
* `$logs`: Any logs produced by **event sources** are emitted to this stream
</ParamField>

***

<ParamField body="listener_id" type="string" required>
  The ID of the component or workflow you’d like to receive events.

  [See the component endpoints](/rest-api/#components) for information on how to retrieve the ID of existing components. You can retrieve the ID of your workflow in your workflow’s URL - it’s the string `p_2gCPml` in `https://pipedream.com/@dylan/example-rss-sql-workflow-p_2gCPml/edit`.
</ParamField>

#### Example Request

You can configure workflow `p_abc123` to listen to events from the source `dc_def456` using the following command:

<RequestExample>
  ```bash  theme={null}
  curl "https://api.pipedream.com/v1/subscriptions?emitter_id=dc_def456&listener_id=p_abc123" \
    -X POST \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

Built with [Mintlify](https://mintlify.com).
