# Source: https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini-search-preview.md

# gpt-4o-mini-search-preview

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `gpt-4o-mini-search-preview`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/gpt-4o-mini-search-preview" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A specialized model trained to understand and execute web search queries with the [Chat completions](https://docs.aimlapi.com/capabilities/completion-or-chat-models) API.

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

:digit\_one: **Setup You Can’t Skip**

:black\_small\_square: [**Create an Account**](https://aimlapi.com/app/sign-up): Visit the AI/ML API website and create an account (if you don’t have one yet).\
:black\_small\_square: [**Generate an API Key**](https://aimlapi.com/app/keys): After logging in, navigate to your account dashboard and generate your API key. Ensure that key is enabled on UI.

:digit\_two: **Copy the code example**

At the bottom of this page, you'll find [a code example](#code-example) that shows how to structure the request. Choose the code snippet in your preferred programming language and copy it into your development environment.

:digit\_three: **Modify the code example**

:black\_small\_square: Replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key from your account.\
:black\_small\_square: Insert your question or request into the `content` field—this is what the model will respond to.

:digit\_four: <sup><sub><mark style="background-color:yellow;">**(Optional)**<mark style="background-color:yellow;"><sub></sup>**&#x20;Adjust other optional parameters if needed**

Only `model` and `messages` are required parameters for this model (and we’ve already filled them in for you in the example), but you can include optional parameters if needed to adjust the model’s behavior. Below, you can find the corresponding [API schema](#api-schema), which lists all available parameters along with notes on how to use them.

:digit\_five: **Run your modified code**

Run your modified code in your development environment. Response time depends on various factors, but for simple prompts it rarely exceeds a few seconds.

{% hint style="success" %}
If you need a more detailed walkthrough for setting up your development environment and making a request step by step — feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).
{% endhint %}

</details>

## API Schema

## POST /v1/chat/completions

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/chat/completions":{"post":{"operationId":"_v1_chat_completions","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["gpt-4o-mini-search-preview"]},"messages":{"type":"array","items":{"oneOf":[{"type":"object","properties":{"role":{"type":"string","enum":["user"],"description":"The role of the author of the message — in this case, the user"},"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]}}],"description":"The contents of the user message."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role","content"]},{"type":"object","properties":{"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]}}],"description":"The contents of the developer message."},"role":{"type":"string","enum":["developer"],"description":"The role of the author of the message — in this case, the developer."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["content","role"],"additionalProperties":false},{"type":"object","properties":{"role":{"type":"string","enum":["system"],"description":"The role of the author of the message — in this case, the system."},"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]}}],"description":"The contents of the system message."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role","content"],"additionalProperties":false},{"type":"object","properties":{"role":{"type":"string","enum":["assistant"],"description":"The role of the author of the message — in this case, the Assistant."},"content":{"anyOf":[{"type":"string","description":"The contents of the Assistant message."},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]},"description":"An array of content parts with a defined type. Can be one or more of type text, or exactly one of type refusal."}],"description":"The contents of the Assistant message. Required unless tool_calls or function_call is specified."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role"]}]},"description":"A list of messages comprising the conversation so far. Depending on the model you use, different message types (modalities) are supported, like text, documents (txt, pdf), images, and audio."},"max_tokens":{"type":"number","minimum":1,"description":"The maximum number of tokens that can be generated in the chat completion. This value can be used to control costs for text generated via API."},"stream":{"type":"boolean","default":false,"description":"If set to True, the model response data will be streamed to the client as it is generated using server-sent events."},"stream_options":{"type":"object","properties":{"include_usage":{"type":"boolean"}},"required":["include_usage"]}},"required":["model","messages"],"title":"gpt-4o-mini-search-preview"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"A unique identifier for the chat completion."},"object":{"type":"string","enum":["chat.completion"],"description":"The object type."},"created":{"type":"number","description":"The Unix timestamp (in seconds) of when the chat completion was created."},"choices":{"type":"array","items":{"type":"object","properties":{"index":{"type":"number","description":"The index of the choice in the list of choices."},"message":{"type":"object","properties":{"role":{"type":"string","description":"The role of the author of this message."},"content":{"type":"string","description":"The contents of the message."},"refusal":{"type":"string","nullable":true,"description":"The refusal message generated by the model."},"annotations":{"type":"array","nullable":true,"items":{"type":"object","properties":{"type":{"type":"string","enum":["url_citation"],"description":"The type of the URL citation. Always url_citation."},"url_citation":{"type":"object","properties":{"end_index":{"type":"integer","description":"The index of the last character of the URL citation in the message."},"start_index":{"type":"integer","description":"The index of the first character of the URL citation in the message."},"title":{"type":"string","description":"The title of the web resource."},"url":{"type":"string","description":"The URL of the web resource."}},"required":["end_index","start_index","title","url"],"description":"A URL citation when using web search."}},"required":["type","url_citation"]},"description":"Annotations for the message, when applicable, as when using the web search tool."},"audio":{"type":"object","nullable":true,"properties":{"id":{"type":"string","description":"Unique identifier for this audio response."},"data":{"type":"string","description":"Base64 encoded audio bytes generated by the model, in the format specified in the request."},"transcript":{"type":"string","description":"Transcript of the audio generated by the model."},"expires_at":{"type":"integer","description":"The Unix timestamp (in seconds) for when this audio response will no longer be accessible on the server for use in multi-turn conversations."}},"required":["id","data","transcript","expires_at"],"description":"A chat completion message generated by the model."},"tool_calls":{"type":"array","nullable":true,"items":{"oneOf":[{"type":"object","properties":{"id":{"type":"string","description":"The ID of the tool call."},"type":{"type":"string","enum":["function"],"description":"The type of the tool."},"function":{"type":"object","properties":{"arguments":{"type":"string","description":"The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."},"name":{"type":"string","description":"The name of the function to call."}},"required":["arguments","name"],"description":"The function that the model called."}},"required":["id","type","function"]},{"type":"object","properties":{"id":{"type":"string","description":"The ID of the tool call."},"type":{"type":"string","enum":["custom"],"description":"The type of the tool."},"custom":{"type":"object","properties":{"input":{"type":"string","description":"The input for the custom tool call generated by the model."},"name":{"type":"string","description":"The name of the custom tool to call."}},"required":["input","name"],"description":"The custom tool that the model called."}},"required":["id","type","custom"]}]},"description":"The tool calls generated by the model, such as function calls."}},"required":["role","content"],"description":"A chat completion message generated by the model."},"finish_reason":{"type":"string","enum":["stop","length","content_filter","tool_calls"],"description":"The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence, length if the maximum number of tokens specified in the request was reached, content_filter if content was omitted due to a flag from our content filters, tool_calls if the model called a tool"},"logprobs":{"type":"object","nullable":true,"properties":{"content":{"type":"array","items":{"type":"object","properties":{"bytes":{"type":"array","items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"bytes":{"type":"array","nullable":true,"items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."}},"required":["logprob","token"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["bytes","logprob","token"]},"description":"A list of message content tokens with log probability information."},"refusal":{"type":"array","items":{"type":"object","properties":{"bytes":{"type":"array","items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"bytes":{"type":"array","nullable":true,"items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."}},"required":["logprob","token"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["bytes","logprob","token"]},"description":"A list of message refusal tokens with log probability information."}},"required":["content","refusal"],"description":"Log probability information for the choice."}},"required":["index","message","finish_reason"]}},"model":{"type":"string","description":"The model used for the chat completion."},"usage":{"type":"object","properties":{"prompt_tokens":{"type":"number","description":"Number of tokens in the prompt."},"completion_tokens":{"type":"number","description":"Number of tokens in the generated completion."},"total_tokens":{"type":"number","description":"Total number of tokens used in the request (prompt + completion)."},"completion_tokens_details":{"type":"object","nullable":true,"properties":{"accepted_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion."},"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens generated by the model."},"reasoning_tokens":{"type":"integer","nullable":true,"description":"Tokens generated by the model for reasoning."},"rejected_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total completion tokens for purposes of billing, output, and context window limits."}},"description":"Breakdown of tokens used in a completion."},"prompt_tokens_details":{"type":"object","nullable":true,"properties":{"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens present in the prompt."},"cached_tokens":{"type":"integer","nullable":true,"description":"Cached tokens present in the prompt."}},"description":"Breakdown of tokens used in the prompt."}},"required":["prompt_tokens","completion_tokens","total_tokens"],"description":"Usage statistics for the completion request."}},"required":["id","object","created","choices","model","usage"]}},"text/event-stream":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"A unique identifier for the chat completion."},"choices":{"type":"array","items":{"type":"object","properties":{"delta":{"type":"object","nullable":true,"properties":{"content":{"type":"string","description":"The contents of the chunk message."},"refusal":{"type":"string","nullable":true,"description":"The refusal message generated by the model."},"role":{"type":"string","enum":["user","assistant","developer","system","tool"],"description":"The role of the author of this message."},"tool_calls":{"type":"array","nullable":true,"items":{"type":"object","properties":{"index":{"type":"number"},"id":{"type":"string","description":"The ID of the tool call."},"function":{"type":"object","properties":{"arguments":{"type":"string","description":"The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."},"name":{"type":"string"}},"required":["arguments","name"],"description":"The function that the model called."},"type":{"type":"string","enum":["function"],"description":"The type of the tool."}},"required":["index","id","function","type"]},"description":"The tool calls generated by the model, such as function calls."}},"required":["content","role"],"description":"A chat completion delta generated by streamed model responses."},"finish_reason":{"type":"string","enum":["length","function_call","stop","tool_calls","content_filter"]},"index":{"type":"number","description":"The index of the choice in the list of choices."},"logprobs":{"type":"object","nullable":true,"properties":{"content":{"type":"array","items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."}},"required":["token","bytes","logprob"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["token","bytes","logprob"]}},"refusal":{"type":"array","items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."}},"required":["token","bytes","logprob"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["token","bytes","logprob"]}}},"required":["content","refusal"],"description":"Log probability information for the choice."}},"required":["finish_reason","index"]},"description":"A list of chat completion choices. Can be more than one if n is greater than 1."},"created":{"type":"number","description":"The Unix timestamp (in seconds) of when the chat completion was created."},"model":{"type":"string","description":"The model used for the chat completion."},"object":{"type":"string","enum":["chat.completion.chunk"],"description":"The object type."},"service_tier":{"type":"string","nullable":true,"enum":["auto","default","flex","scale","priority"],"description":"Specifies the processing type used for serving the request."},"usage":{"type":"object","nullable":true,"properties":{"prompt_tokens":{"type":"number","description":"Number of tokens in the prompt."},"completion_tokens":{"type":"number","description":"Number of tokens in the generated completion."},"total_tokens":{"type":"number","description":"Total number of tokens used in the request (prompt + completion)."},"completion_tokens_details":{"type":"object","nullable":true,"properties":{"accepted_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion."},"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens generated by the model."},"reasoning_tokens":{"type":"integer","nullable":true,"description":"Tokens generated by the model for reasoning."},"rejected_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total completion tokens for purposes of billing, output, and context window limits."}},"description":"Breakdown of tokens used in a completion."},"prompt_tokens_details":{"type":"object","nullable":true,"properties":{"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens present in the prompt."},"cached_tokens":{"type":"integer","nullable":true,"description":"Cached tokens present in the prompt."}},"description":"Breakdown of tokens used in the prompt."}},"required":["prompt_tokens","completion_tokens","total_tokens"],"description":"Usage statistics for the completion request."}},"required":["id","choices","created","model","object"]}}}}}}}}}
```

## Code Example

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json  # for getting a structured output with indentation 

response = requests.post(
    "https://api.aimlapi.com/v1/chat/completions",
    headers={
        # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization":"Bearer <YOUR_AIMLAPI_KEY>",
        "Content-Type":"application/json"
    },
    json={
        "model":"gpt-4o-mini-search-preview",
        "messages":[
            {
                "role":"user",
                "content":"Hello"  # insert your prompt here, instead of Hello
            }
        ]
    }
)

data = response.json()
print(json.dumps(data, indent=2, ensure_ascii=False))
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
async function main() {
  const response = await fetch('https://api.aimlapi.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      // insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>
      'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini-search-preview',
      messages:[
          {
              role:'user',
              content: 'Hello'  // insert your prompt here, instead of Hello
          }
      ],
    }),
  });

  const data = await response.json();
  console.log(JSON.stringify(data, null, 2));
}

main();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
{'id': 'chatcmpl-d5329df8-efab-48d8-b607-9e61dd14553b', 'object': 'chat.completion', 'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'Hello! How can I assist you today? ', 'refusal': None, 'annotations': []}}], 'created': 1744217025, 'model': 'gpt-4o-mini-search-preview-2025-03-11', 'usage': {'prompt_tokens': 0, 'completion_tokens': 13, 'total_tokens': 13, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'system_fingerprint': ''}
```

{% endcode %}

</details>
