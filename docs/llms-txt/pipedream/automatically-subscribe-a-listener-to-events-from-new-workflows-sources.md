# Source: https://pipedream.com/docs/rest-api/api-reference/subscription/automatically-subscribe-a-listener-to-events-from-new-workflows-sources.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automatically subscribe a listener to events from new workflows / sources

You can use this endpoint to automatically receive events, like workflow errors, in another listening workflow or event source. Once you setup the auto-subscription, any new workflows or event sources you create will automatically deliver the specified events to the listener.

Note: this will configure subscriptions for *new* workflows and sources after the time you configure the subscription. To deliver events to your listener from *existing* workflows or sources, use the [`POST /subscriptions` endpoint](/rest-api/#listen-for-events-from-another-source-or-workflow).

**Currently, this feature is enabled only on the API. The Pipedream UI will not display the sources configured as listeners using this API**.

#### Endpoint

```
POST /auto_subscriptions?event_name={event_name}&listener_id={receiving_source_id}
```

#### Parameters

<ParamField body="event_name" type="string">
  The name of the event stream whose events you’d like to receive:

* `$errors`: Any errors thrown by workflows or sources are emitted to this stream
* `$logs`: Any logs produced by **event sources** are emitted to this stream
</ParamField>

***

<ParamField body="listener_id" type="string">
  The ID of the component or workflow you’d like to receive events.

  [See the component endpoints](/rest-api/#components) for information on how to retrieve the ID of existing components. You can retrieve the ID of your workflow in your workflow’s URL - it’s the string `p_2gCPml` in `https://pipedream.com/@dylan/example-rss-sql-workflow-p_2gCPml/edit`.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  # You can configure workflow `p_abc123` to listen to events from the source `dc_def456` using the following command:
  curl "https://api.pipedream.com/v1/auto_subscriptions?event_name=$errors&listener_id=p_abc123" \
    -X POST \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

Built with [Mintlify](https://mintlify.com).
