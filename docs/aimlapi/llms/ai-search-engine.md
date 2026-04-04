# Source: https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine.md

# AI Search Engine

## Overview

AI Web Search Engine is designed to retrieve real-time information from the internet. This solution processes user queries and return relevant data from various online sources, making them useful for tasks that require up-to-date knowledge beyond static datasets. It supports **two** usage options:

{% stepper %}
{% step %}
**Using six specialized API endpoints**, each designed to search for only one specific type of information. These endpoints return structured responses, making them more suitable for integration into specialized services (e.g., a weather widget). Here are the types of information you can retrieve this way:

* [Links](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-links)
* [Images](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-images)
* [Videos](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-videos)
* [Weather details for a specified location](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-the-weather)
* [Locations](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/find-a-local-map)
* [Knowledge about a topic, structured as a small knowledge base](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine/get-a-knowledge-structure)

See API references and examples on the subpages.
{% endstep %}

{% step %}
**As a general** [**chat completion**](https://docs.aimlapi.com/capabilities/completion-or-chat-models) **solution** (but searching on the internet): enter a query in the prompt and receive an internet-sourced answer, similar to asking a question on a search engine through a browser. See the API Schema below or check how this call is made in the Python example on the bottom of this page.
{% endstep %}
{% endstepper %}

## How to make a call

Check how this call is made in the [examples](#example-1) below.

{% hint style="success" %}
Note that queries can include advanced search syntax:

* **Search for an exact match:** Enter a word or phrase using `\"` before and after it.\
  For example, `\"tallest building\"`.
* **Search for a specific site:** Enter `site:` in front of a site or domain.\
  For example, `site:youtube.com cat videos`.
* **Exclude words from your search:** Enter `-` in front of a word that you want to leave out.\
  For example, `jaguar speed -car`.
  {% endhint %}

{% hint style="success" %}
You can also personalize the AI Search Engine output by passing the `ip` parameter.\
See [Example #2](#example-2-using-the-ip-parameter-for-personalized-model-output) below.
{% endhint %}

### API Schema

## POST /v1/chat/completions

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/chat/completions":{"post":{"operationId":"_v1_chat_completions","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["bagoodex/bagoodex-search-v1"]},"messages":{"type":"array","items":{"oneOf":[{"type":"object","properties":{"role":{"type":"string","enum":["user"],"description":"The role of the author of the message — in this case, the user"},"content":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]}}],"description":"The contents of the user message."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role","content"]},{"type":"object","properties":{"role":{"type":"string","enum":["assistant"],"description":"The role of the author of the message — in this case, the Assistant."},"content":{"anyOf":[{"type":"string","description":"The contents of the Assistant message."},{"type":"array","items":{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of the content part."},"text":{"type":"string","description":"The text content."}},"required":["type","text"]},"description":"An array of content parts with a defined type. Can be one or more of type text, or exactly one of type refusal."}],"description":"The contents of the Assistant message. Required unless tool_calls or function_call is specified."},"name":{"type":"string","description":"An optional name for the participant. Provides the model information to differentiate between participants of the same role."}},"required":["role"]}]},"description":"A list of messages comprising the conversation so far. Depending on the model you use, different message types (modalities) are supported, like text, documents (txt, pdf), images, and audio."},"max_tokens":{"type":"number","minimum":1,"description":"The maximum number of tokens that can be generated in the chat completion. This value can be used to control costs for text generated via API."},"stream":{"type":"boolean","default":false,"description":"If set to True, the model response data will be streamed to the client as it is generated using server-sent events."},"stream_options":{"type":"object","properties":{"include_usage":{"type":"boolean"}},"required":["include_usage"]},"frequency_penalty":{"type":"number","nullable":true,"minimum":-2,"maximum":2,"description":"Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim."},"logit_bias":{"type":"object","nullable":true,"additionalProperties":{"type":"number","minimum":-100,"maximum":100},"description":"Modify the likelihood of specified tokens appearing in the completion.\n  \n  Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token."},"logprobs":{"type":"boolean","nullable":true,"description":"Whether to return log probabilities of the output tokens or not. If True, returns the log probabilities of each output token returned in the content of message."},"top_logprobs":{"type":"number","nullable":true,"minimum":0,"maximum":20,"description":"An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to True if this parameter is used."},"n":{"type":"integer","nullable":true,"minimum":1,"description":"How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs."},"presence_penalty":{"type":"number","nullable":true,"minimum":-2,"maximum":2,"description":"Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics."},"response_format":{"oneOf":[{"type":"object","properties":{"type":{"type":"string","enum":["text"],"description":"The type of response format being defined. Always text."}},"required":["type"],"additionalProperties":false,"description":"Default response format. Used to generate text responses."},{"type":"object","properties":{"type":{"type":"string","enum":["json_object"],"description":"The type of response format being defined. Always json_object."}},"required":["type"],"additionalProperties":false,"description":"An older method of generating JSON responses. Using json_schema is recommended for models that support it. Note that the model will not generate JSON without a system or user message instructing it to do so."},{"type":"object","properties":{"type":{"type":"string","enum":["json_schema"],"description":"The type of response format being defined. Always json_schema."},"json_schema":{"type":"object","properties":{"name":{"type":"string","description":"The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."},"schema":{"type":"object","additionalProperties":{"nullable":true},"description":"The schema for the response format, described as a JSON Schema object."},"strict":{"type":"boolean","nullable":true,"description":"Whether to enable strict schema adherence when generating the output. If set to True, the model will always follow the exact schema defined in the schema field. Only a subset of JSON Schema is supported when strict is True."},"description":{"type":"string","description":"A description of what the response format is for, used by the model to determine how to respond in the format."}},"required":["name"],"additionalProperties":false,"description":"JSON Schema response format. Used to generate structured JSON responses."}},"required":["type","json_schema"],"additionalProperties":false,"description":"JSON Schema response format. Used to generate structured JSON responses."}],"description":"An object specifying the format that the model must output."},"seed":{"type":"integer","minimum":1,"description":"This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result."},"stop":{"anyOf":[{"type":"string"},{"type":"array","items":{"type":"string"}},{"nullable":true}],"description":"Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence."},"temperature":{"type":"number","minimum":0,"maximum":2,"description":"What sampling temperature to use. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both."},"top_p":{"type":"number","minimum":0.01,"maximum":1,"description":"An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.\n  We generally recommend altering this or temperature but not both."},"echo":{"type":"boolean","description":"If True, the response will contain the prompt. Can be used with logprobs to return prompt logprobs."},"repetition_penalty":{"type":"number","nullable":true,"description":"A number that controls the diversity of generated text by reducing the likelihood of repeated sequences. Higher values decrease repetition."},"top_k":{"type":"number","description":"Only sample from the top K options for each subsequent token. Used to remove \"long tail\" low probability responses. Recommended for advanced use cases only. You usually only need to use temperature."},"min_p":{"type":"number","minimum":0.001,"maximum":0.999,"description":"A number between 0.001 and 0.999 that can be used as an alternative to top_p and top_k."},"user":{"type":"string"},"best_of":{"type":"integer","nullable":true,"minimum":1},"use_beam_search":{"type":"boolean","nullable":true},"length_penalty":{"type":"number","nullable":true},"early_stopping":{"type":"boolean","nullable":true},"ignore_eos":{"type":"boolean","nullable":true},"min_tokens":{"type":"integer","nullable":true},"stop_token_ids":{"type":"array","nullable":true,"items":{"type":"integer"}},"skip_special_tokens":{"type":"boolean","nullable":true},"spaces_between_special_tokens":{"nullable":true},"add_generation_prompt":{"type":"boolean","nullable":true,"description":"If True, the generation prompt will be added to the chat template. This is a parameter used by chat template in tokenizer config of the model."},"add_special_tokens":{"type":"boolean","nullable":true,"description":"If True, special tokens (e.g. BOS) will be added to the prompt on top of what is added by the chat template. For most models, the chat template takes care of adding the special tokens so this should be set to False (as is the default)."},"documents":{"type":"array","nullable":true,"items":{"type":"object","additionalProperties":{"type":"string"}},"description":"'A list of dicts representing documents that will be accessible to the model if it is performing RAG (retrieval-augmented generation). If the template does not support RAG, this argument will have no effect. We recommend that each document should be a dict containing \"title\" and \"text\" keys."},"chat_template":{"type":"string","nullable":true,"description":"A Jinja template to use for this conversion. If this is not passed, the model's default chat template will be used instead."},"chat_template_kwargs":{"type":"object","nullable":true,"additionalProperties":{"nullable":true},"description":"Additional kwargs to pass to the template renderer. Will be accessible by the chat template"},"include_stop_str_in_output":{"type":"boolean","nullable":true,"description":"Whether to include the stop string in the output. This is only applied when the stop or stop_token_ids is set"},"guided_json":{"anyOf":[{"type":"string"},{"type":"object","additionalProperties":{"nullable":true}},{"nullable":true}],"description":"If specified, the output will follow the JSON schema."},"guided_regex":{"type":"string","nullable":true,"description":"If specified, the output will follow the regex pattern."},"guided_choice":{"type":"array","nullable":true,"items":{"type":"string"},"description":"If specified, the output will be exactly one of the choices."},"guided_grammar":{"type":"string","nullable":true,"description":"If specified, the output will follow the context free grammar."},"guided_decoding_backend":{"type":"string","nullable":true,"enum":["outlines","lm-format-enforcer"],"description":"If specified, will override the default guided decoding backend of the server for this specific request. If set, must be either 'outlines' / 'lm-format-enforcer'"},"guided_whitespace_pattern":{"type":"string","nullable":true,"description":"If specified, will override the default whitespace pattern for guided json decoding."},"ip":{"type":"string","format":"ip","description":"IP from which a request is executed"}},"required":["model","messages"],"title":"bagoodex/bagoodex-search-v1"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"A unique identifier for the chat completion."},"object":{"type":"string","enum":["chat.completion"],"description":"The object type."},"created":{"type":"number","description":"The Unix timestamp (in seconds) of when the chat completion was created."},"choices":{"type":"array","items":{"type":"object","properties":{"index":{"type":"number","description":"The index of the choice in the list of choices."},"message":{"type":"object","properties":{"role":{"type":"string","description":"The role of the author of this message."},"content":{"type":"string","description":"The contents of the message."},"refusal":{"type":"string","nullable":true,"description":"The refusal message generated by the model."},"annotations":{"type":"array","nullable":true,"items":{"type":"object","properties":{"type":{"type":"string","enum":["url_citation"],"description":"The type of the URL citation. Always url_citation."},"url_citation":{"type":"object","properties":{"end_index":{"type":"integer","description":"The index of the last character of the URL citation in the message."},"start_index":{"type":"integer","description":"The index of the first character of the URL citation in the message."},"title":{"type":"string","description":"The title of the web resource."},"url":{"type":"string","description":"The URL of the web resource."}},"required":["end_index","start_index","title","url"],"description":"A URL citation when using web search."}},"required":["type","url_citation"]},"description":"Annotations for the message, when applicable, as when using the web search tool."},"audio":{"type":"object","nullable":true,"properties":{"id":{"type":"string","description":"Unique identifier for this audio response."},"data":{"type":"string","description":"Base64 encoded audio bytes generated by the model, in the format specified in the request."},"transcript":{"type":"string","description":"Transcript of the audio generated by the model."},"expires_at":{"type":"integer","description":"The Unix timestamp (in seconds) for when this audio response will no longer be accessible on the server for use in multi-turn conversations."}},"required":["id","data","transcript","expires_at"],"description":"A chat completion message generated by the model."},"tool_calls":{"type":"array","nullable":true,"items":{"oneOf":[{"type":"object","properties":{"id":{"type":"string","description":"The ID of the tool call."},"type":{"type":"string","enum":["function"],"description":"The type of the tool."},"function":{"type":"object","properties":{"arguments":{"type":"string","description":"The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."},"name":{"type":"string","description":"The name of the function to call."}},"required":["arguments","name"],"description":"The function that the model called."}},"required":["id","type","function"]},{"type":"object","properties":{"id":{"type":"string","description":"The ID of the tool call."},"type":{"type":"string","enum":["custom"],"description":"The type of the tool."},"custom":{"type":"object","properties":{"input":{"type":"string","description":"The input for the custom tool call generated by the model."},"name":{"type":"string","description":"The name of the custom tool to call."}},"required":["input","name"],"description":"The custom tool that the model called."}},"required":["id","type","custom"]}]},"description":"The tool calls generated by the model, such as function calls."}},"required":["role","content"],"description":"A chat completion message generated by the model."},"finish_reason":{"type":"string","enum":["stop","length","content_filter","tool_calls"],"description":"The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence, length if the maximum number of tokens specified in the request was reached, content_filter if content was omitted due to a flag from our content filters, tool_calls if the model called a tool"},"logprobs":{"type":"object","nullable":true,"properties":{"content":{"type":"array","items":{"type":"object","properties":{"bytes":{"type":"array","items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"bytes":{"type":"array","nullable":true,"items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."}},"required":["logprob","token"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["bytes","logprob","token"]},"description":"A list of message content tokens with log probability information."},"refusal":{"type":"array","items":{"type":"object","properties":{"bytes":{"type":"array","items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"bytes":{"type":"array","nullable":true,"items":{"type":"integer"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"token":{"type":"string","description":"The token."}},"required":["logprob","token"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["bytes","logprob","token"]},"description":"A list of message refusal tokens with log probability information."}},"required":["content","refusal"],"description":"Log probability information for the choice."}},"required":["index","message","finish_reason"]}},"model":{"type":"string","description":"The model used for the chat completion."},"usage":{"type":"object","properties":{"prompt_tokens":{"type":"number","description":"Number of tokens in the prompt."},"completion_tokens":{"type":"number","description":"Number of tokens in the generated completion."},"total_tokens":{"type":"number","description":"Total number of tokens used in the request (prompt + completion)."},"completion_tokens_details":{"type":"object","nullable":true,"properties":{"accepted_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion."},"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens generated by the model."},"reasoning_tokens":{"type":"integer","nullable":true,"description":"Tokens generated by the model for reasoning."},"rejected_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total completion tokens for purposes of billing, output, and context window limits."}},"description":"Breakdown of tokens used in a completion."},"prompt_tokens_details":{"type":"object","nullable":true,"properties":{"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens present in the prompt."},"cached_tokens":{"type":"integer","nullable":true,"description":"Cached tokens present in the prompt."}},"description":"Breakdown of tokens used in the prompt."}},"required":["prompt_tokens","completion_tokens","total_tokens"],"description":"Usage statistics for the completion request."}},"required":["id","object","created","choices","model","usage"]}},"text/event-stream":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"A unique identifier for the chat completion."},"choices":{"type":"array","items":{"type":"object","properties":{"delta":{"type":"object","nullable":true,"properties":{"content":{"type":"string","description":"The contents of the chunk message."},"refusal":{"type":"string","nullable":true,"description":"The refusal message generated by the model."},"role":{"type":"string","enum":["user","assistant","developer","system","tool"],"description":"The role of the author of this message."},"tool_calls":{"type":"array","nullable":true,"items":{"type":"object","properties":{"index":{"type":"number"},"id":{"type":"string","description":"The ID of the tool call."},"function":{"type":"object","properties":{"arguments":{"type":"string","description":"The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."},"name":{"type":"string"}},"required":["arguments","name"],"description":"The function that the model called."},"type":{"type":"string","enum":["function"],"description":"The type of the tool."}},"required":["index","id","function","type"]},"description":"The tool calls generated by the model, such as function calls."}},"required":["content","role"],"description":"A chat completion delta generated by streamed model responses."},"finish_reason":{"type":"string","enum":["length","function_call","stop","tool_calls","content_filter"]},"index":{"type":"number","description":"The index of the choice in the list of choices."},"logprobs":{"type":"object","nullable":true,"properties":{"content":{"type":"array","items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."}},"required":["token","bytes","logprob"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["token","bytes","logprob"]}},"refusal":{"type":"array","items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."},"top_logprobs":{"type":"array","nullable":true,"items":{"type":"object","properties":{"token":{"type":"string","description":"The token."},"bytes":{"type":"array","items":{"type":"number"},"description":"A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token."},"logprob":{"type":"number","description":"The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value -9999.0 is used to signify that the token is very unlikely."}},"required":["token","bytes","logprob"]},"description":"List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned."}},"required":["token","bytes","logprob"]}}},"required":["content","refusal"],"description":"Log probability information for the choice."}},"required":["finish_reason","index"]},"description":"A list of chat completion choices. Can be more than one if n is greater than 1."},"created":{"type":"number","description":"The Unix timestamp (in seconds) of when the chat completion was created."},"model":{"type":"string","description":"The model used for the chat completion."},"object":{"type":"string","enum":["chat.completion.chunk"],"description":"The object type."},"service_tier":{"type":"string","nullable":true,"enum":["auto","default","flex","scale","priority"],"description":"Specifies the processing type used for serving the request."},"usage":{"type":"object","nullable":true,"properties":{"prompt_tokens":{"type":"number","description":"Number of tokens in the prompt."},"completion_tokens":{"type":"number","description":"Number of tokens in the generated completion."},"total_tokens":{"type":"number","description":"Total number of tokens used in the request (prompt + completion)."},"completion_tokens_details":{"type":"object","nullable":true,"properties":{"accepted_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that appeared in the completion."},"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens generated by the model."},"reasoning_tokens":{"type":"integer","nullable":true,"description":"Tokens generated by the model for reasoning."},"rejected_prediction_tokens":{"type":"integer","nullable":true,"description":"When using Predicted Outputs, the number of tokens in the prediction that did not appear in the completion. However, like reasoning tokens, these tokens are still counted in the total completion tokens for purposes of billing, output, and context window limits."}},"description":"Breakdown of tokens used in a completion."},"prompt_tokens_details":{"type":"object","nullable":true,"properties":{"audio_tokens":{"type":"integer","nullable":true,"description":"Audio input tokens present in the prompt."},"cached_tokens":{"type":"integer","nullable":true,"description":"Cached tokens present in the prompt."}},"description":"Breakdown of tokens used in the prompt."}},"required":["prompt_tokens","completion_tokens","total_tokens"],"description":"Usage statistics for the completion request."}},"required":["id","choices","created","model","object"]}}}}}}}}}
```

## Example #1

{% tabs %}
{% tab title="Python" %}

```python
import requests
from openai import OpenAI

# Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
API_KEY = '<YOUR_AIMLAPI_KEY>'
API_URL = 'https://api.aimlapi.com'

def complete_chat():
    client = OpenAI(
        base_url=API_URL,
        api_key=API_KEY,
    )    

    response = client.chat.completions.create(
        model="bagoodex/bagoodex-search-v1",
        messages=[
            {
                "role": "user",
                
                # Enter your query here
                "content": 'how to make a slingshot',
            },
        ],
    )
    
    
    print(response.choices[0].message.content)


# Run the function
complete_chat()
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
const API_KEY = '<YOUR_AIMLAPI_KEY>';
const API_URL = 'https://api.aimlapi.com/v1/chat/completions';

async function completeChat() {
    const requestBody = {
        model: "bagoodex/bagoodex-search-v1",
        messages: [
            {
                role: "user",
                content: "how to make a slingshot"
            }
        ]
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${API_KEY}`
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        console.log(data.choices[0].message.content);
    } catch (error) {
        console.error("Error fetching completion:", error);
    }
}

// Run the function
completeChat();

```

{% endtab %}
{% endtabs %}

<details>

<summary><strong>Response</strong></summary>

{% code overflow="wrap" %}

```
To make a slingshot, you can follow the instructions provided in the two sources:

**Option 1: Make a Giant Slingshot**

* Start by cutting two 2x4's to a length of 40 inches each, which will be the main arms of the slingshot.
* Attach the arms to a base made of plywood using screws, and then add side braces to support the arms.
* Install an exercise band as the launching mechanism, making sure to tighten it to achieve the desired distance.
* Add a cross brace to keep the arms rigid and prevent them from spreading or caving in.

**Option 2: Make a Stick Slingshot**

* Find a sturdy, Y-shaped stick and break it down to the desired shape.
* Cut notches on the ends of the stick to hold the rubber bands in place.
* Create a pouch by folding a piece of fabric in half and then half again, and then cutting small holes for the rubber bands.        
* Thread the rubber bands through the holes and tie them securely to the stick using thread.
* Decorate the slingshot with coloured yarn or twine if desired.

You can choose to make either a giant slingshot or a stick slingshot, depending on your preference and the materials available.  
```

{% endcode %}

</details>

## Example #2: Using the IP Parameter for Personalized Model Output

When using regular search engines in browsers, we can simply ask, '*Weather today*' without specifying our location. In this case, the search engine automatically uses your IP address to determine your location and provide a more relevant response. The AI Search Engine also supports IP-based personalization.

In the example below, the query does not specify a city, but since the request includes an IP address registered in Stockholm, the system automatically adjusts, and the response will contain today's weather forecast for that city.

{% hint style="warning" %}
Note that when making a request via Python, the `ip` parameter should be included inside the `extra_body` parameter (see example below). When using other languages, this is not required, and the `ip` parameter can be passed like any other parameter.
{% endhint %}

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
from openai import OpenAI

# Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
API_KEY = '<YOUR_AIMLAPI_KEY>'
API_URL = 'https://api.aimlapi.com'

# Call the standart chat completion endpoint to get an ID
def complete_chat():
    client = OpenAI(
        base_url=API_URL,
        api_key=API_KEY,
    )    

    response = client.chat.completions.create(
        model="bagoodex/bagoodex-search-v1",
        messages=[
            {
                "role": "user",
                "content": "Weather today",
            },
        ],
        
        # insert your IP into this section
        extra_body={
            'ip': '192.44.242.19' # we used a random IP address from Stockholm
        }
    )
    print(response.choices[0].message.content)
    return response


# Run the function
complete_chat()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
import fetch from 'node-fetch';

// Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
const API_KEY = '<YOUR_AIMLAPI_KEY>';
const API_URL = 'https://api.aimlapi.com/v1/chat/completions';

async function completeChat() {
    const requestBody = {
        model: "bagoodex/bagoodex-search-v1",
        messages: [
            {
                role: "user",
                content: "Weather today"
            }
        ],
        extra_body: {
            ip: "192.44.242.19" // We used a random IP address from Stockholm
        }
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`
            },
            body: JSON.stringify(requestBody)
        });
        
        const data = await response.json();
        console.log(data.choices[0].message.content);
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Run the function
completeChat();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response When Using IP Parameter</summary>

{% code overflow="wrap" %}

```
"According to the forecast, today's weather in Stockholm is partly cloudy with light winds. The temperature is expected to be around 6°C (43°F) with a gentle breeze. \n\nThe forecast also mentions that the weather will be sunny intervals and light winds throughout the day."
```

{% endcode %}

</details>

{% hint style="warning" %}
Keep in mind that the system caches the IP address for a period of two weeks. This means that after specifying an IP address once, any queries <mark style="background-color:orange;">**without an explicit location**</mark> will continue to return responses linked to Stockholm for the next two weeks, even if you don't include the IP address in subsequent requests. If you need to change the location, simply provide a new IP address in your next request.
{% endhint %}

If an IP address registered in one location is used while explicitly specifying a different location in the query, AI Search Engine will prioritize the location from the query:

<details>

<summary>Response when the IP parameter is used (from Stockholm), but the request also includes a different location (San Francisco)</summary>

{% code overflow="wrap" %}

```
"According to the weather forecast, today in San Francisco, there will be a strong cold front moving through the Bay Area from late morning into the afternoon, boosting wind speeds with gusts at around 45 mph midday and featuring high rain rates at times. This may lead to localized runoff issues. The high temperature is expected to be around 56F, with a chance of rain 100% and rainfall near a half an inch. \n\nYou can check the latest forecast and weather conditions on websites such as [https://weather.com/weather/today/l/USCA0987:1:US] or [https://www.accuweather.com/en/us/san-francisco/94103/weather-forecast/347629]."
```

{% endcode %}

</details>
