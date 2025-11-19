# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-predict.md

# Environment

Use this endpoint to call the deployment associated with the specified [environment](/deployment/environments).

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/environments/{env_name}/predict
```

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the model's environment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Model input" type="json" required>
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  env_name = "staging"

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/environments/{env_name}/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/environments/{env_name}/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/environments/{env_name}/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>
