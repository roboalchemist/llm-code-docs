# Source: https://docs.baseten.co/reference/inference-api/wake/development-wake.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Development

Use this endpoint to wake the [development deployment](/deployment/deployments#development-deployment) of your model if it is scaled to zero.

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/development/wake
```

### Parameters

<ParamField path="Model ID" type="string" required>
  The ID of the model you want to wake.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/development/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/development/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>
