# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-websocket.md

# Websocket deployment

Use this endpoint to connect via WebSockets to a specific deployment.

Note that `entity` here could be either `model` or `chain`, depending on whether you using Baseten models or Chains.

```sh  theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/deployment/{deployment_id}/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField path="entity" type="string" required>
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField path="entity_id" type="string" required>
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the deployment you want to connect to.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{model_id}.api.baseten.co/deployment/{deployment_id}/websocket
  ```
</RequestExample>
