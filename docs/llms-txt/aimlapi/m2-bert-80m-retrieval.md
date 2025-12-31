# Source: https://docs.aimlapi.com/api-references/embedding-models/together-ai/m2-bert-80m-retrieval.md

# m2-bert-80M-retrieval

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `togethercomputer/m2-bert-80M-32k-retrieval`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/togethercomputer/m2-bert-80M-32k-retrieval" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The model integrates advanced machine learning techniques to excel in searching and retrieving relevant information from vast datasets. With its 8k parameter design, it balances performance and efficiency, making it suitable for applications requiring high-speed data access and analysis.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/embeddings

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}}},"paths":{"/v1/embeddings":{"post":{"operationId":"EmbeddingsController_createEmbeddings_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"enum":["togethercomputer/m2-bert-80M-32k-retrieval"]},"input":{"anyOf":[{"type":"string","minLength":1},{"type":"array","items":{"type":"string"},"minItems":1}],"description":"Input text to embed, encoded as a string or array of tokens."}},"required":["model","input"]}}}},"responses":{"201":{"description":""}},"tags":["Embeddings"]}}}}
```
