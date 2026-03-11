# Source: https://novita.ai/docs/api-reference/model-apis-llm-create-rerank.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create rerank

Creates a rerank request.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="model" type="string" required={true}>
  The name of the model to use.
</ParamField>

<ParamField body="query" type="string" required={true}>
  The search query.
</ParamField>

<ParamField body="documents" type="string[]" required={true}>
  Document List.
</ParamField>

<ParamField body="top_n" type="integer" required={false}>
  Number of most relevant documents or indices to return.
</ParamField>

## Response

<ResponseField name="id" type="string" required={true}>
  ID
</ResponseField>

<ResponseField name="results" type="object[]" required={true}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="document" type="object">
      Original document content.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="text" type="string" />
      </Expandable>
    </ResponseField>

    <ResponseField name="index" type="integer">
      The index value of the position in the input candidate doc array.
    </ResponseField>

    <ResponseField name="relevance_score" type="number">
      Similarity score.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="usage" type="object">
  Token usage statistics.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="completion_tokens" type="integer" required={true}>
      The number of tokens in the generated completion.
    </ResponseField>

    <ResponseField name="prompt_tokens" type="integer" required={true}>
      The number of tokens in the prompt.
    </ResponseField>

    <ResponseField name="total_tokens" type="integer" required={true}>
      The total number of tokens used in the request (prompt + completion).
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).