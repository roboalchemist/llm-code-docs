# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-run-remote.md

# Chains development

Use this endpoint to call the [development deployment](/development/chain/deploy#development) of
your chain.

```sh  theme={"system"}
https://chain-{chain_id}.api.baseten.co/development/run_remote
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain-{chain_id}.api.baseten.co/development/run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/development/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/development/run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response theme={"system"}
  // JSON-serializable output varies by chain
  {}
  ```
</ResponseExample>
