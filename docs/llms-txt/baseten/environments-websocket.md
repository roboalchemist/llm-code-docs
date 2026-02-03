# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-websocket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Websocket environment

Use this endpoint to connect via WebSockets to the deployment associated with the specified [environment](/deployment/environments).

Note that `entity` here could be either `model` or `chain`, depending on whether you using Baseten models or Chains.

```sh  theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/environments/{env_name}/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField path="entity" type="string" required>
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField path="entity_id" type="string" required>
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the environment you want to connect to.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{model_id}.api.baseten.co/environments/{env_name}/websocket
  ```
</RequestExample>
