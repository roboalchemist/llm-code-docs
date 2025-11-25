# Source: https://docs.fireworks.ai/api-reference/get-generated-image-from-flux-kontex.md

# Get generated image from FLUX.1 Kontext

<Tabs>
  <Tab title="FLUX.1 Kontext Pro">
    Replace **model** with **flux-kontext-pro** in the API to get the result.
  </Tab>

  <Tab title="FLUX.1 Kontext Max">
    Replace **model** with **flux-kontext-max** in the API to get the result.
  </Tab>
</Tabs>

## Path

<ParamField path="model" type="string" required initialValue="flux-kontext-pro" placeholder="flux-kontext-pro">
  The model to use for image generation. Use **flux-kontext-pro** or  **flux-kontext-max** as the model name in the API.
</ParamField>

## Headers

<ParamField header="Content-Type" type="string" initialValue="application/json" placeholder="application/json">
  The media type of the request body.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key.
</ParamField>

## Request Body

<ParamField body="id" type="string" required>
  Request id generated from create/edit image request.
</ParamField>

<RequestExample>
  ```python Python theme={null}
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      id: "request_id"
  }

  response = requests.post(url, headers=headers, json=data)

  print(response.text)
  ```

  ```typescript TypeScript theme={null}
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          id: "request_id"
        }),
      });
  })().catch(console.error);
  ```

  ```shell curl theme={null}
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    id: "request_id"
  }'
  ```
</RequestExample>

## Response

<ResponseField name="id" type="string" required>
  Task id for retrieving result
</ResponseField>

<ResponseField name="status" type="enum<string>" required>
  Available options: Task not found, Pending, Request Moderated, Content Moderated, Ready, Error
</ResponseField>

<ResponseField name="result" type="any" />

<ResponseField name="progress" type="number | null" />

<ResponseField name="details" type="object | null" />
