# Source: https://novita.ai/docs/api-reference/model-apis-llm-list-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List models

Lists the currently available models for the LLM API, and provides basic information about each one. This endpoint is compatible with OpenAI API.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Response

<ResponseExample>
  ```json  theme={"system"}
  {
    "data": [
      {
        "created": 1733560109,
        "id": "meta-llama/llama-3.3-70b-instruct",
        "object": "model",
        "input_token_price_per_m": 3900,
        "output_token_price_per_m": 3900,
        "title": "meta-llama/llama-3.3-70b-instruct",
        "description": "The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out). The Llama 3.3 instruction tuned text only model is optimized for multilingual dialogue use cases and outperforms many of the available open source and closed chat models on common industry benchmarks.\n\nSupported languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.",
        "context_size": 131072
      },
      // more models here...
    ]
  }
  ```
</ResponseExample>

<ResponseField name="data" type="array" required={true}>
  Array of model objects with the following properties:

  <Expandable title="Model Object Properties">
    <ResponseField name="id" type="string" required={true}>
      The model identifier, which can be referenced in the API endpoints.
    </ResponseField>

    <ResponseField name="created" type="integer" required={true}>
      The Unix timestamp (in seconds) when the model was created.
    </ResponseField>

    <ResponseField name="object" type="string" required={true}>
      The object type, which is always "model".
    </ResponseField>

    <ResponseField name="input_token_price_per_m" type="integer" required={true}>
      The price per million input tokens.
    </ResponseField>

    <ResponseField name="output_token_price_per_m" type="integer" required={true}>
      The price per million output tokens.
    </ResponseField>

    <ResponseField name="title" type="string" required={true}>
      The title of the model.
    </ResponseField>

    <ResponseField name="description" type="string" required={true}>
      The description of the model.
    </ResponseField>

    <ResponseField name="context_size" type="integer" required={true}>
      The maximum context size of the model.
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).