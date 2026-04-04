# Source: https://docs.wandb.ai/inference/api-reference/list-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Models

> Retrieve a list of all available W&B Inference models and their IDs using the models API endpoint.

Get all available models and their IDs. Use this to select models dynamically or check what's available.

## Request examples

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import openai

    client = openai.OpenAI(
        base_url="https://api.inference.wandb.ai/v1",
        api_key="<your-api-key>",
        project="<your-team>/<your-project>"  # Optional, for usage tracking
    )

    response = client.models.list()

    for model in response.data:
        print(model.id)
    ```
  </Tab>

  <Tab title="Bash">
    ```bash  theme={null}
    curl https://api.inference.wandb.ai/v1/models \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <your-api-key>" \
      -H "OpenAI-Project: <your-team>/<your-project>"
    ```
  </Tab>
</Tabs>

## Response format

The API returns responses in OpenAI-compatible format:

```json  theme={null}
{
  "object": "list",
  "data": [
    {
      "id": "deepseek-ai/DeepSeek-V3.1",
      "object": "model",
      "created": 0,
      "owned_by": "system",
      "root": "deepseek-ai/DeepSeek-V3.1"
    },
    {
      "id": "openai/gpt-oss-20b",
      "object": "model",
      "created": 0,
      "owned_by": "system",
      "root": "openai/gpt-oss-20b"
    }
    // ... more models
  ]
}
```
