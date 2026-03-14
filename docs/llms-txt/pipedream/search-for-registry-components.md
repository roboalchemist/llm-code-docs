# Source: https://pipedream.com/docs/rest-api/api-reference/components/search-for-registry-components.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for registry components

Search for components in the global registry with natural language. Pipedream will use AI to match your query to the most relevant components.

#### Endpoint

```
GET /components/search
```

#### Parameters

<ParamField body="query" type="string" required>
  The query string to search for components in the global registry, e.g. “Send a message to Slack on new HubSpot contacts”
</ParamField>

***

<ParamField body="app" type="string">
  The name slug the app you’d like to filter results for. For example, Slack’s name slug is `slack`. Returned sources and actions are filtered to only those tied to the specified app.

  You can find the name slug under the **Authentication** section of any [app page](https://pipedream.com/apps).
</ParamField>

***

<ParamField body="similarity_threshold" type="number">
  The minimum similarity score required for a component to be returned. The similarity score is a number between 0 and 1, where 1 is a perfect match. Similarity here is computed as the cosine distance between the embedding of the user query and the embedding of the component’s metadata.
</ParamField>

***

<ParamField body="debug" type="boolean">
  Pass `debug=true` to return additional data in the response, useful for inspecting the results.
</ParamField>

<RequestExample>
  ```bash  theme={null}
  curl -G https://api.pipedream.com/v1/components/search \
    --data-urlencode "query=When a new HubSpot contact is added, send me an SMS" \
    -d "limit=1" \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "sources": [
      "hubspot-new-contact"
    ],
    "actions": [
      "twilio-send-sms"
    ]
  }
  ```
</ResponseExample>

Built with [Mintlify](https://mintlify.com).
