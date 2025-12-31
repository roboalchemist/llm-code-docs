# Source: https://docs.aimlapi.com/api-references/moderation-safety-models/meta/llamaguard-2-8b.md

# LlamaGuard-2-8b

{% hint style="info" %}
This documentation is valid for the following list of our models:

* `meta-llama/LlamaGuard-2-8b`
  {% endhint %}

## Model Overview

An 8B-parameter Llama 3-based safeguard model, designed for content classification in LLM inputs (prompt classification) and responses (response classification), similar to Llama Guard. Functioning as an LLM, it generates text outputs that indicate whether a given prompt or response is safe or unsafe, and if deemed unsafe, it specifies the violated content categories.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## Submit a request

### API Schema

{% openapi src="<https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-5a0f97b06bec2f52a15ebe9c45d5bf768ce7b482%2FLlamaGuard-2-8b.json?alt=media&token=beac894d-483e-43e2-ae0a-1079b738bee5>" path="/v1/chat/completions" method="post" %}
[LlamaGuard-2-8b.json](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-5a0f97b06bec2f52a15ebe9c45d5bf768ce7b482%2FLlamaGuard-2-8b.json?alt=media\&token=beac894d-483e-43e2-ae0a-1079b738bee5)
{% endopenapi %}
