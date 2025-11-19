# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-websocket.md

# Websocket development

Use this endpoint to connect via WebSockets to the development deployment of a model or chain.

```sh  theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/development/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField path="entity" type="string" required>
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField path="entity_id" type="string" required>
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{entity_id}.api.baseten.co/development/websocket
  ```
</RequestExample>
