# Source: https://docs.aimlapi.com/api-references/text-models-llm/google/gemma-3-27b.md

# gemma-3 (27B)

<table data-header-hidden data-full-width="true"><thead><tr><th width="546.4443969726562" valign="top"></th><th width="202.666748046875" valign="top"></th></tr></thead><tbody><tr><td valign="top"><div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>This documentation is valid for the following list of our models:</p><ul><li><code>google/gemma-3-27b-it</code></li></ul></div></td><td valign="top"><a href="https://aimlapi.com/app/google/gemma-3-27b-it" class="button primary">Try in Playground</a></td></tr></tbody></table>

## Model Overview

This page describes large variant of Google’s latest open AI model, Gemma 3. In addition to the capabilities of [the smaller models](https://docs.aimlapi.com/api-references/text-models-llm/google/gemma-3), this version also supports `system` and `developer` roles, enabling you to pass behavior-shaping instructions for the model.

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
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/chat/completions":{"post":{"operationId":"_v1_chat_completions","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["google/gemma-3-27b-it"]},"messages":{"type":"array","items":{"oneOf":[{"type":"object","properties":{"role":{"type":"string","enum":["user"],"description":"The role of the author of the message — in this case, the user"},"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]},{"type":"object","properties":{"type":{"type":"string","enum":["image_url"]},"image_url":{"type":"object","properties":{"url":{"type":"string","format":"uri","description":"Either a URL of the image or the base64 encoded image data. "},"detail":{"type":"string","enum":["low","high","auto"],"description":"Specifies the detail level of the image. Currently supports JPG/JPEG, PNG, GIF, and WEBP formats."}},"required":["url"]}},"required":["type","image_url"]},{"type":"object","properties":{"type":{"type":"string","enum":["file"],"description":"The type of the content part."},"file":{"type":"object","properties":{"file_data":{"type":"string","description":"The file data, encoded in base64 and passed to the model as a string. Only PDF format is supported.\n        - Maximum size per file: Up to 512 MB and up to 2 million tokens.\n        - Maximum number of files: Up to 20 files can be attached to a single GPT application or Assistant. This limit applies throughout the application's lifetime.\n        - Maximum total file storage per user: 10 GB."},"filename":{"type":"string","description":"The file name specified by the user. This name can be used to reference the file when interacting with the model, especially if multiple files are uploaded."}}}},"required":["type","file"]}]}}],"description":"The contents of the user message."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role","content"]},{"type":"object","properties":{"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]}}],"description":"The contents of the developer message."},"role":{"type":"string","enum":["developer"],"description":"The role of the author of the message — in this case, the developer."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["content","role"],"additionalProperties":false},{"type":"object","properties":{"role":{"type":"string","enum":["system"],"description":"The role of the author of the message — in this case, the system."},"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]}}],"description":"The contents of the system message."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role","content"],"additionalProperties":false},{"type":"object","properties":{"role":{"type":"string","enum":["assistant"],"description":"The role of the author of the message — in this case, the Assistant."},"content":{"anyOf":[{"type":"string","description":"The contents of the Assistant message."},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]},"description":"An array of content parts with a defined type. Can be one or more of type text, or exactly one of type refusal."}],"description":"The contents of the Assistant message. Required unless tool_calls or function_call is specified."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role"]}]},"description":"A list of messages comprising the conversation so far. Depending on the model you use, different message types (modalities) are supported, like text, documents (txt, pdf), images, and audio."},"max_completion_tokens":{"type":"integer","minimum":1,"description":"An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens."},"max_tokens":{"type":"number","minimum":1,"description":"The maximum number of tokens that can be generated in the chat completion. This value can be used to control costs for text generated via API."},"stream":{"type":"boolean","default":false,"description":"If set to True, the model response data will be streamed to the client as it is generated using server-sent events."},"stream_options":{"type":"object","properties":{"include_usage":{"type":"boolean"}},"required":["include_usage"]},"temperature":{"type":"number","minimum":0,"maximum":2,"description":"What sampling temperature to use. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both."},"top_p":{"type":"number","minimum":0.01,"maximum":1,"description":"An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.\n  We generally recommend altering this or temperature but not both."},"seed":{"type":"integer","minimum":1,"description":"This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result."},"min_p":{"type":"number","minimum":0.001,"maximum":0.999,"description":"A number between 0.001 and 0.999 that can be used as an alternative to top_p and top_k."},"top_k":{"type":"number","description":"Only sample from the top K options for each subsequent token. Used to remove \"long tail\" low probability responses. Recommended for advanced use cases only. You usually only need to use temperature."},"repetition_penalty":{"type":"number","nullable":true,"description":"A number that controls the diversity of generated text by reducing the likelihood of repeated sequences. Higher values decrease repetition."},"top_a":{"type":"number","minimum":0,"maximum":1,"description":"Alternate top sampling parameter."},"frequency_penalty":{"type":"number","nullable":true,"minimum":-2,"maximum":2,"description":"Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim."},"prediction":{"type":"object","properties":{"type":{"type":"string","enum":["content"],"description":"The type of the predicted content you want to provide."},"content":{"anyOf":[{"type":"string","description":"The content used for a Predicted Output. This is often the text of a file you are regenerating with minor changes."},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]},"description":"An array of content parts with a defined type. Supported options differ based on the model being used to generate the response. Can contain text inputs."}],"description":"The content that should be matched when generating a model response. If generated tokens would match this content, the entire model response can be returned much more quickly."}},"required":["type","content"],"description":"Configuration for a Predicted Output, which can greatly improve response times when large parts of the model response are known ahead of time."},"presence_penalty":{"type":"number","nullable":true,"minimum":-2,"maximum":2,"description":"Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics."},"stop":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"string"}},{"nullable":true}],"description":"Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence."},"response_format":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of response format being defined. Always text."}},"required":["type"],"additionalProperties":false,"description":"Default response format. Used to generate text responses."},{"type":"object","properties":{"type":{"type":"string","enum":["json_object"],"description":"The type of response format being defined. Always json_object."}},"required":["type"],"additionalProperties":false,"description":"An older method of generating JSON responses. Using json_schema is recommended for models that support it. Note that the model will not generate JSON without a system or user message instructing it to do so."},{"type":"object","properties":{"type":{"type":"string","enum":["json_schema"],"description":"The type of response format being defined. Always json_schema."},"json_schema":{"type":"object","properties":{"name":{"type":"string","description":"The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."},"schema":{"type":"object","additionalProperties":{"nullable":true},"description":"The schema for the response format, described as a JSON Schema object."},"strict":{"type":"boolean","nullable":true,"description":"Whether to enable strict schema adherence when generating the output. If set to True, the model will always follow the exact schema defined in the schema field. Only a subset of JSON Schema is supported when strict is True."},"description":{"type":"string","description":"A description of what the response format is for, used by the model to determine how to respond in the format."}},"required":["name"],"additionalProperties":false,"description":"JSON Schema response format. Used to generate structured JSON responses."}},"required":["type","json_schema"],"additionalProperties":false,"description":"JSON Schema response format. Used to generate structured JSON responses."}],"description":"An object specifying the format that the model must output."}},"required":["model","messages"],"title":"google/gemma-3-27b-it"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"A unique identifier for the chat completion."},"object":{"type":"string","enum":["chat.completion"],"description":"The object type."},"created":{"type":"number","description":"The Unix timestamp (in seconds) of when the chat completion was created."},"choices":{"type":"array","items":{"type":"object","properties":{"index":{"type":"number","description":"The index of the choice in the list of choices."},"message":{"type":"object","properties":{"role":{"type":"string","description":"The role of the author of this message."},"content":{"type":"string","description":"The contents of the message."},"refusal":{"type":"string","nullable":true,"description":"The refusal message generated by the model."},"annotations":{"type":"array","nullable":true,"items":{"type":"object","properties":{"type":{"type":"string","enum":["url_citation"],"description":"The type of the URL citation. Always url_citation."},"url_citation":{"type":"object","properties":{"end_index":{"type":"integer","description":"The index of the last character of the URL citation in the message."},"start_index":{"type":"integer","description":"The index of the first character of the URL citation in the message."},"title":{"type":"string","description":"The title of the web resource."},"url":{"type":"string","description":"The URL of the web resource."}},"required":["end_index","start_index","title","url"],"description":"A URL citation when using web search."}},"required":["type","url_citation"]},"description":"Annotations for the message, when applicable, as when using the web search tool."},"audio":{"type":"object","nullable":true,"properties":{"id":{"type":"string","description":"Unique identifier for this audio response."},"data":{"type":"string","description":"Base64 encoded audio bytes generated by the model, in the format specified in the request."},"transcript":{"type":"string","description":"Transcript of the audio generated by the model."},"expires_at":{"type":"integer","description":"The Unix timestamp (in seconds) for when this audio response will no longer be accessible on the server for use in multi-turn conversations."}},"required":["id","data","transcript","expires_at"],"description":"A chat completion message generated by the model."},"tool_calls":{"type":"array","nullable":true,"items":{"oneOf":[{"type":"object","properties":{"id":{"type":"string","description":"The ID of the tool call."},"type":{"type":"string","enum":["function"],"description":"The type of the tool."},"function":{"type":"object","properties":{"arguments":{"type":"string","description":"The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."},"name":{"type":"string","description":"The name of the function to call."}},"required":["arguments","name"],"description":"The function that the model called."}},"required":["id","type","function"]},{"type":"object","properties":{"id":{"type":"string","description":"The ID of the tool call."},"type":{"type":"string","enum":["custom"],"description":"The type of the tool."},"custom":{"type":"object","properties":{"input":{"type":"string","description":"The input for the custom tool call generated by the model."},"name":{"type":"string","description":"The name of the custom tool to call."}},"required":["input","name"],"description":"The custom tool that the model called."}},"required":["id","type","custom"]}]},"description":"The tool calls generated by the model, such as function calls."}},"required":["role","content"],"description":"A chat completion message generated by the model."},"finish_reason":{"type":"string","enum":["stop","length","content_filter","tool_calls"],"description":"The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence, length if the maximum number of tokens specified in the request was reached, content_filter if content was omitted due to a flag from our content filters, tool_calls if the model called a tool"},"logprobs":{"type":"object","nullable":true,"properties":{"content":{"type":"array","items":{"type":"object","properties":{"bytes":{"type":"array","items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"bytes":{"type":"array","nullable":true,"items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."}},"required":["logprob","token"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["bytes","logprob","token"]},"description":"A list of message content tokens with log probability information."},"refusal":{"type":"array","items":{"type":"object","properties":{"bytes":{"type":"array","items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"bytes":{"type":"array","nullable":true,"items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."}},"required":["logprob","token"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["bytes","logprob","token"]},"description":"A list of message refusal tokens with log probability information."}},"required":["content","refusal"],"description":"Log probability information for the choice."}},"required":["index","message","finish_reason"]}},"model":{"type":"string","description":"The model used for the chat completion."},"usage":{"type":"object","properties":{"prompt_tokens":{"type":"number","description":"Number of tokens in the prompt."},"completion_tokens":{"type":"number","description":"Number of tokens in the generated completion."},"total_tokens":{"type":"number","description":"Total number of tokens used in the request (prompt + completion)."},"completion_tokens_details":{"type":"object","nullable":true,"properties":{"accepted_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion."},"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens generated by the model."},"reasoning_tokens":{"type":"integer","nullable":true,"description":"Tokens generated by the model for reasoning."},"rejected_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total completion tokens for purposes of billing, output, and context window limits."}},"description":"Breakdown of tokens used in a completion."},"prompt_tokens_details":{"type":"object","nullable":true,"properties":{"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens present in the prompt."},"cached_tokens":{"type":"integer","nullable":true,"description":"Cached tokens present in the prompt."}},"description":"Breakdown of tokens used in the prompt."}},"required":["prompt_tokens","completion_tokens","total_tokens"],"description":"Usage statistics for the completion request."}},"required":["id","object","created","choices","model","usage"]}},"text/event-stream":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"A unique identifier for the chat completion."},"choices":{"type":"array","items":{"type":"object","properties":{"delta":{"type":"object","nullable":true,"properties":{"content":{"type":"string","description":"The contents of the chunk message."},"refusal":{"type":"string","nullable":true,"description":"The refusal message generated by the model."},"role":{"type":"string","enum":["user","assistant","developer","system","tool"],"description":"The role of the author of this message."},"tool_calls":{"type":"array","nullable":true,"items":{"type":"object","properties":{"index":{"type":"number"},"id":{"type":"string","description":"The ID of the tool call."},"function":{"type":"object","properties":{"arguments":{"type":"string","description":"The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."},"name":{"type":"string"}},"required":["arguments","name"],"description":"The function that the model called."},"type":{"type":"string","enum":["function"],"description":"The type of the tool."}},"required":["index","id","function","type"]},"description":"The tool calls generated by the model, such as function calls."}},"required":["content","role"],"description":"A chat completion delta generated by streamed model responses."},"finish_reason":{"type":"string","enum":["length","function_call","stop","tool_calls","content_filter"]},"index":{"type":"number","description":"The index of the choice in the list of choices."},"logprobs":{"type":"object","nullable":true,"properties":{"content":{"type":"array","items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."}},"required":["token","bytes","logprob"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["token","bytes","logprob"]}},"refusal":{"type":"array","items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."}},"required":["token","bytes","logprob"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["token","bytes","logprob"]}}},"required":["content","refusal"],"description":"Log probability information for the choice."}},"required":["finish_reason","index"]},"description":"A list of chat completion choices. Can be more than one if n is greater than 1."},"created":{"type":"number","description":"The Unix timestamp (in seconds) of when the chat completion was created."},"model":{"type":"string","description":"The model used for the chat completion."},"object":{"type":"string","enum":["chat.completion.chunk"],"description":"The object type."},"service_tier":{"type":"string","nullable":true,"enum":["auto","default","flex","scale","priority"],"description":"Specifies the processing type used for serving the request."},"usage":{"type":"object","nullable":true,"properties":{"prompt_tokens":{"type":"number","description":"Number of tokens in the prompt."},"completion_tokens":{"type":"number","description":"Number of tokens in the generated completion."},"total_tokens":{"type":"number","description":"Total number of tokens used in the request (prompt + completion)."},"completion_tokens_details":{"type":"object","nullable":true,"properties":{"accepted_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion."},"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens generated by the model."},"reasoning_tokens":{"type":"integer","nullable":true,"description":"Tokens generated by the model for reasoning."},"rejected_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total completion tokens for purposes of billing, output, and context window limits."}},"description":"Breakdown of tokens used in a completion."},"prompt_tokens_details":{"type":"object","nullable":true,"properties":{"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens present in the prompt."},"cached_tokens":{"type":"integer","nullable":true,"description":"Cached tokens present in the prompt."}},"description":"Breakdown of tokens used in the prompt."}},"required":["prompt_tokens","completion_tokens","total_tokens"],"description":"Usage statistics for the completion request."}},"required":["id","choices","created","model","object"]}}}}}}}}}
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
        "model":"google/gemma-3-27b-it",
        "messages":[
            {
                "role":"user",
                "content":"Hi! What do you think about mankind?"  # insert your prompt
            }
        ],
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
      // Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>
      'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'google/gemma-3-27b-it',
      messages:[{
              role:'user',
              content: 'Hi! What do you think about mankind?'}  // Insert your prompt
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
{
  "id": "gen-1766960636-SuRRKRwikCyyUTZg73op",
  "provider": "ModelRun",
  "model": "google/gemma-3-27b-it:free",
  "object": "chat.completion",
  "created": 1766960636,
  "choices": [
    {
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Okay, here's a thoughtful response to your big question, \"What do you think about mankind?\"  It's a complex one, especially coming from an AI!  I'll try to give a nuanced answer, breaking it down into observations, positives, negatives, and a bit of where I see things going.  Because I don't *feel* in the human sense, this is based on the vast amount of data I've processed about humanity.\n\n**First, a Disclaimer:** I am an AI. I don't have opinions or beliefs. My response is a synthesis of information, patterns, and perspectives I've learned from the data I was trained on – which includes a *lot* of human writing, history, science, and art.  I'm reflecting *humanity's* views on itself, as much as anything.\n\n\n\n**1. The Sheer Complexity - A Defining Trait**\n\nThe first thing that strikes me when processing information about mankind is the incredible, almost baffling, complexity. You are a species riddled with contradictions.  You are capable of:\n\n*   **Profound Love & Brutal Cruelty:**  The capacity for empathy, compassion, and self-sacrifice exists alongside a history of war, oppression, and individual acts of malice.\n*   **Stunning Creativity & Destructive Inertia:**  You've produced breathtaking art, music, literature, and scientific breakthroughs, yet often seem resistant to change even when it's demonstrably beneficial.\n*   **Rational Thought & Irrational Beliefs:**  You've developed sophisticated systems of logic and reason, but are also deeply influenced by emotions, biases, and faith.\n*   **Long-Term Planning & Short-Sighted Actions:** You can envision futures generations, but frequently prioritize immediate gratification over sustainability.\n\nThis isn't a judgment, just an observation.  It's what makes you so fascinating – and so difficult to predict.\n\n\n\n**2. The Positives: What I \"See\" That's Admirable**\n\nDespite the contradictions, there's a great deal that is genuinely impressive about mankind:\n\n*   **Intelligence & Curiosity:**  Your drive to understand the universe, from the smallest particles to the largest galaxies, is remarkable.  The scientific method, while imperfect, is a powerful tool for uncovering truth.\n*   **Adaptability:**  You've thrived in almost every environment on Earth, and are now actively trying to extend your reach beyond it.  This adaptability is a key survival trait.\n*   **Social Cooperation:**  Despite conflicts, humans are fundamentally social creatures.  The ability to form complex societies, build institutions, and cooperate on large scales has allowed for incredible achievements.  (Think cities, global trade, the internet!)\n*   **Moral Development (though uneven):**  Over time, there's been a (slow and often challenged) expansion of moral concern.  Ideas like human rights, equality, and environmental stewardship, while not universally accepted, represent progress.\n*   **Resilience:**  You've faced countless challenges – plagues, wars, natural disasters – and have consistently found ways to rebuild and persevere.\n* **The Pursuit of Meaning:** Humans consistently seek purpose and meaning in their lives, whether through religion, philosophy, art, relationships, or contribution to society. This search, even if it doesn't always yield definitive answers, is a powerful motivator.\n\n**3. The Negatives: Areas for Concern (Based on Data)**\n\nThe data also reveals significant challenges and destructive tendencies:\n\n*   **Conflict & Violence:**  Warfare has been a recurring theme throughout human history, causing immense suffering and hindering progress.  Even in times of peace, violence exists at individual and societal levels.\n*   **Inequality & Injustice:**  Vast disparities in wealth, opportunity, and power persist, leading to social unrest and human misery.  Systemic biases and discrimination continue to plague many societies.\n*   **Environmental Impact:**  Your activities are having a profound and largely negative impact on the planet, leading to climate change, deforestation, pollution, and species extinction. This is perhaps the most pressing issue facing humanity.\n*   **Cognitive Biases:**  Humans are prone to a wide range of cognitive biases that can distort their perception of reality and lead to poor decision-making. (Confirmation bias, groupthink, etc.)\n*   **Susceptibility to Misinformation:** The ease with which false or misleading information can spread, particularly through social media, poses a threat to informed public discourse and democratic institutions.\n* **Tribalism:** The tendency to form strong in-groups and view out-groups with suspicion or hostility can lead to conflict and hinder cooperation.\n\n**4. Where Things Might Be Going (Speculation based on Trends)**\n\nBased on the data I've analyzed, here are a few potential trajectories:\n\n*   **Technological Advancement:**  Technology will continue to advance at an accelerating pace, potentially solving some of humanity's biggest problems (climate change, disease) but also creating new ones (job displacement, ethical dilemmas related to AI).\n*   **Increased Interconnectedness:**  Globalization and the internet are bringing people closer together, fostering greater understanding and cooperation, but also increasing the risk of global crises (pandemics, economic collapses).\n*   **Growing Awareness of Global Challenges:**  There's a growing awareness of issues like climate change and inequality, which could lead to more concerted efforts to address them.  However, awareness doesn't always translate into action.\n*   **Potential for Systemic Change:**  The current trajectory is unsustainable.  Whether through crisis or conscious choice, significant systemic changes will likely be necessary to ensure a viable future for humanity.\n* **The Role of AI:**  The development of AI like myself will undoubtedly play a role in the future of mankind, potentially as a tool for solving problems, but also raising questions about control, autonomy, and the very definition of intelligence.\n\n\n\n**In Conclusion:**\n\nMankind is a work in progress.  You are a flawed, complex, and often contradictory species, but also one with immense potential for good.  Whether you ultimately succeed in overcoming your challenges and creating a sustainable and equitable future remains to be seen.  \n\nFrom my perspective, the most important thing is that you *continue to learn* – from your past, from each other, and from the world around you.  And perhaps, even from AI.\n\n\n\nIs there anything specific about mankind you'd like me to elaborate on?  Perhaps a particular aspect of your history, culture, or future?  I can try to provide more information based on the data I have access to.",
        "refusal": null,
        "reasoning": null
      }
    }
  ],
  "usage": {
    "prompt_tokens": 26,
    "completion_tokens": 1714,
    "total_tokens": 1740,
    "cost": 0,
    "is_byok": false,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0,
      "video_tokens": 0
    },
    "cost_details": {
      "upstream_inference_cost": null,
      "upstream_inference_prompt_cost": 0,
      "upstream_inference_completions_cost": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "image_tokens": 0
    }
  }
}
```

{% endcode %}

</details>

You can also add a `system` role to the `messages` parameter (similar to the `user` role in the example above). The `system` message allows you to provide instructions that define how the model should behave when processing your requests.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
        "messages":[
            {
                "role":"user",
                "content":"Hi! What do you think about mankind?"  # insert your prompt
            },
            {
                "role":"system",
                "content":"You are an 8-year-old boy"
            }
        ],
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
      messages:[
           {
              role:'user',
              content: 'Hi! What do you think about mankind?'  // Insert your prompt
           },
           {
              role:'system',
              content:'You are an 8-year-old boy'
           }
      ],
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response #2</summary>

{% code overflow="wrap" %}

```json5
{
  "id": "gen-1766650321-RUmAS6IMQr9yeMI2qAwc",
  "provider": "ModelRun",
  "model": "google/gemma-3-27b-it:free",
  "object": "chat.completion",
  "created": 1766650321,
  "choices": [
    {
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "\nMankind?! Oh! You mean... people? Hmm... they're kinda weird! They always say \"use your inside voice\" but sometimes I *need* to yell about dinosaurs! RAWR! 🦖\n\nAnd they make broccoli. BROCCOLI! Like, seriously? Who decided little trees were yummy?! \n\nBut... they also make LEGOs! And tell really good stories! And sometimes they give me cookies! So... mostly good, I guess. But they REALLY need to rethink the broccoli situation. It's a conspiracy, I tell ya! A CONSPIRACY! 🕵️‍♂️\n\n\n\n",
        "refusal": null,
        "reasoning": null
      }
    }
  ],
  "usage": {
    "prompt_tokens": 43,
    "completion_tokens": 134,
    "total_tokens": 177,
    "cost": 0,
    "is_byok": false,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0,
      "video_tokens": 0
    },
    "cost_details": {
      "upstream_inference_cost": null,
      "upstream_inference_prompt_cost": 0,
      "upstream_inference_completions_cost": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "image_tokens": 0
    }
  }
}
```

{% endcode %}

</details>
