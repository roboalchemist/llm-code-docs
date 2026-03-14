# Source: https://pipedream.com/docs/rest-api/api-reference/subscription/delete-a-subscription.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a subscription

Use this endpoint to delete an existing subscription. This endpoint accepts the same parameters as the [`POST /subscriptions` endpoint](/rest-api/#listen-for-events-from-another-source-or-workflow) for creating subscriptions.

#### Endpoint

```
DELETE /subscriptions?emitter_id={emitting_component_id}&listener_id={receiving_source_id}&event_name={event_name}
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

<ParamField body="listener_id" type="string" required>
  The ID of the component or workflow you’d like to receive events.

  [See the component endpoints](/rest-api/#components) for information on how to retrieve the ID of existing components. You can retrieve the ID of your workflow in your workflow’s URL - it’s the string `p_2gCPml` in `https://pipedream.com/@dylan/example-rss-sql-workflow-p_2gCPml/edit`.
</ParamField>

***

<ParamField body="event_name" type="string" required>
  The name of the event stream tied to your subscription. **If you didn’t specify an `event_name` when creating your subscription, pass `event_name=`**.

  You’ll find the `event_name` that’s tied to your subscription when [listing your subscriptions](/rest-api/#get-current-users-subscriptions):

  ```json  theme={null}
  {
    "id": "sub_abc123",
    "emitter_id": "dc_abc123",
    "listener_id": "dc_def456",
    "event_name": "test"
  },
  {
    "id": "sub_def456",
    "emitter_id": "dc_abc123",
    "listener_id": "wh_abc123",
    "event_name": ""
  }
  ```

</ParamField>

<RequestExample>
  ```bash  theme={null}
  # You can delete a subscription you configured for workflow `p_abc123` to listen to events from the source `dc_def456` using the following command:
  curl "https://api.pipedream.com/v1/subscriptions?emitter_id=dc_def456&listener_id=p_abc123" \
    -X DELETE \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

Built with [Mintlify](https://mintlify.com).
