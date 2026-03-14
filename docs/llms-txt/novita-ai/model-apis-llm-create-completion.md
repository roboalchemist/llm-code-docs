# Source: https://novita.ai/docs/api-reference/model-apis-llm-create-completion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create completion

Creates a completion for the provided prompt and parameters.

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

<ParamField body="prompt" type="string" required={true}>
  The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.
</ParamField>

<ParamField body="max_tokens" type="integer" required={false}>
  The maximum number of tokens that can be generated in the completion.

  The token count of your prompt plus max\_tokens cannot exceed the model's context length.
</ParamField>

<ParamField body="stream" type="boolean | null" default={false}>
  Whether to stream back partial progress. If set, tokens will be sent as data-only server-sent events (SSE) as they become available, with the stream terminated by a `data: [DONE]` message.
</ParamField>

<ParamField body="stream_options" type="object | null">
  Options for streaming response. Only set this when you set stream: true.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="include_usage" type="boolean">
      If set, an additional chunk will be streamed before the data: \[DONE] message. The usage field on this chunk shows the token usage statistics for the entire request, and the choices field will always be an empty array. All other chunks will also include a usage field, but with a null value.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="n" type="integer | null" default={1}>
  How many completions to generate for each prompt.

  Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max\_tokens and stop.

  Required range: `1 < x < 128`
</ParamField>

<ParamField body="seed" type="integer | null">
  If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.
</ParamField>

<ParamField body="frequency_penalty" type="number | null" default={0}>
  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

  Reasonable value is around 0.1 to 1 if the aim is to just reduce repetitive samples somewhat. If the aim is to strongly suppress repetition, then one can increase the coefficients up to 2, but this can noticeably degrade the quality of samples. Negative values can be used to increase the likelihood of repetition.

  See also presence\_penalty for penalizing tokens that have at least one appearance at a fixed rate.

  Required range: `-2 < x < 2`
</ParamField>

<ParamField body="presence_penalty" type="number | null" default={0}>
  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

  Reasonable value is around 0.1 to 1 if the aim is to just reduce repetitive samples somewhat. If the aim is to strongly suppress repetition, then one can increase the coefficients up to 2, but this can noticeably degrade the quality of samples. Negative values can be used to increase the likelihood of repetition.

  See also `frequency_penalty` for penalizing tokens at an increasing rate depending on how often they appear.

  Required range: `-2 < x < 2`
</ParamField>

<ParamField body="repetition_penalty" type="number | null">
  Applies a penalty to repeated tokens to discourage or encourage repetition. A value of 1.0 means no penalty, allowing free repetition. Values above 1.0 penalize repetition, reducing the likelihood of repeating tokens. Values between 0.0 and 1.0 reward repetition, increasing the chance of repeated tokens. For a good balance, a value of 1.2 is often recommended. Note that the penalty is applied to both the generated output and the prompt in decoder-only models.

  Required range: `0 < x < 2`
</ParamField>

<ParamField body="stop" type="string | null">
  Up to 4 sequences where the API will stop generating further tokens. The returned text will contain the stop sequence.
</ParamField>

<ParamField body="temperature" type="number | null" default={1}>
  What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  We generally recommend altering this or `top_p` but not both.

  Required range: `0 < x < 2`
</ParamField>

<ParamField body="top_p" type="number | null">
  An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.

  Required range: `0 < x <= 1`
</ParamField>

<ParamField body="top_k" type="integer | null">
  Top-k sampling is another sampling method where the k most probable next tokens are filtered and the probability mass is redistributed among only those k next tokens. The value of k controls the number of candidates for the next token at each step during text generation.

  Required range: `1 < x < 128`
</ParamField>

<ParamField body="min_p" type="number | null">
  float that represents the minimum probability for a token to be considered, relative to the probability of the most likely token.

  Required range: `0 <= x <= 1`
</ParamField>

<ParamField body="logit_bias" type="map[string, integer] | null" required={false}>
  Modify the likelihood of specified tokens appearing in the completion.

  Accepts a JSON object that maps tokens to an associated bias value from -100 to 100.
  Mathematically, the bias is added to the logits generated by the model prior to
  sampling. The exact effect will vary per model.

  For example, by setting `"logit_bias":{"1639": 6}` will increase the likelihood of the token with token ID 1639.
</ParamField>

<ParamField body="logprobs" type="integer | null">
  Include the log probabilities on the logprobs most likely output tokens, as well the chosen tokens. For example, if logprobs is 5, the API will return a list of the 5 most likely tokens.

  The maximum value for logprobs is 5.
</ParamField>

<ParamField body="best_of" type="integer" required={false}>
  Defaults to 1. Generates best\_of completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.

  When used with n, best\_of controls the number of candidate completions and n specifies how many to return – best\_of must be greater than n.

  Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max\_tokens and stop.
</ParamField>

## Response

<ResponseField name="choices" type="array" required={true}>
  The list of generated completion choices.

  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="finish_reason" type="string" required={true}>
      The reason the model stopped generating tokens. This will be "stop" if the model hit a natural stop point or a provided stop sequence, or "length" if the maximum number of tokens specified in the request was reached.

      Enum: `stop`, `length`
    </ResponseField>

    <ResponseField name="index" type="integer" required={true}>
      The index of the completion choice.
    </ResponseField>

    <ResponseField name="logprobs" type="object" required={true}>
      The log probabilities of the most likely tokens.

      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="text_offset" type="array">
          Array of integers representing text offsets.
        </ResponseField>

        <ResponseField name="token_logprobs" type="array">
          Array of numbers representing token log probabilities.
        </ResponseField>

        <ResponseField name="tokens" type="array">
          Array of strings representing tokens.
        </ResponseField>

        <ResponseField name="top_logprobs" type="array">
          Array of objects containing top log probabilities.

          <Expandable title="properties" defaultOpen={false}>
            <ResponseField name="{key}" type="integer" required={true}>
              Log probability value for the given key.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="text" type="string" required={true}>
      The completion response.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="created" type="integer" required={true}>
  The Unix time in seconds when the response was generated.
</ResponseField>

<ResponseField name="id" type="string" required={true}>
  A unique identifier of the response.
</ResponseField>

<ResponseField name="model" type="string" required={true}>
  The model used for the completion.
</ResponseField>

<ResponseField name="object" type="string" required={true}>
  The object type, which is always `text_completion`.
</ResponseField>

<ResponseField name="usage" type="object" required={true}>
  Usage statistics.

  For streaming responses, usage field is included in the very last response chunk returned.

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