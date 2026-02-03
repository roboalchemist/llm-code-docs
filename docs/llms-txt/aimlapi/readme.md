# Source: https://docs.aimlapi.com/quickstart/readme.md

# Documentation Map

This page helps you quickly find the right AI model or ready-to-use solution for your task. Open the API reference and copy a working example to integrate it into your code in minutes.

***

**Trending Models**

<table data-column-title-hidden data-view="cards" data-full-width="false"><thead><tr><th align="center"></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td align="center">Pro-Grade Image Model</td><td><a href="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-206ef7d160b344d59b740e041812b186f33c6eb1%2Fphoto_2025-11-21%2020.42.54.jpeg?alt=media">photo_2025-11-21 20.42.54.jpeg</a></td><td><a href="../api-references/image-models/google/gemini-3-pro-image-preview">gemini-3-pro-image-preview</a></td></tr><tr><td align="center">Top Video Generator</td><td><a href="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-daefe57d7e1fb595691c1b5d21945be789e0963a%2Fphoto_2025-11-10_18-53-24.jpg?alt=media">photo_2025-11-10_18-53-24.jpg</a></td><td><a href="../api-references/video-models/openai/sora-2-t2v">sora-2-t2v</a></td></tr><tr><td align="center">Smarter Reasoning &#x26; Coding</td><td><a href="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-60c739eefe5f711f5850377c0126816b9c88c566%2F2025-11-25%2014.33.02.jpg?alt=media">2025-11-25 14.33.02.jpg</a></td><td><a href="../api-references/text-models-llm/google/gemini-3-pro-preview">gemini-3-pro-preview</a></td></tr></tbody></table>

***

<table data-header-hidden data-full-width="false"><thead><tr><th width="281.09991455078125" valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top"><p><strong>Start with this code block</strong><br><br>🚀 <a href="setting-up"><strong>Setup guide</strong></a> <br><br>🧩 <a href="supported-sdks"><strong>SDKs</strong></a>  </p><p></p><p>▶️ <a href="https://aimlapi.com/app/"><strong>Run in Playground</strong></a></p></td><td valign="top"><pre class="language-python" data-overflow="wrap"><code class="lang-python">from openai import OpenAI
client = OpenAI(
base_url="https://api.aimlapi.com/v1",
api_key="&#x3C;YOUR_AIMLAPI_KEY>",
)
response = client.chat.completions.create(
model="gpt-4o",
messages=[{"role": "user", "content": "Write a one-sentence story about numbers."}]
)
print(response.choices[0].message.content)
</code></pre></td></tr><tr><td valign="top"></td><td valign="top"></td></tr></tbody></table>

***

## Browse Models

Popular | [View all 400+ models >](https://docs.aimlapi.com/api-references/model-database)

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="../api-references/text-models-llm/openai">ChatGPT</a></td><td></td><td></td><td><a href="../api-references/text-models-llm/openai">openai</a></td></tr><tr><td><a href="../api-references/text-models-llm/deepseek">DeepSeek</a></td><td></td><td></td><td><a href="../api-references/text-models-llm/deepseek">deepseek</a></td></tr><tr><td><a href="../api-references/image-models/flux">Flux</a></td><td></td><td></td><td><a href="../api-references/image-models/flux">flux</a></td></tr></tbody></table>

Select the model by its **Task**, by its **Developer** or by the supported **Capabilities**:

{% hint style="info" %}
If you've already made your choice and know the model ID, use the [Search panel](https://docs.aimlapi.com/?q=) on your right.
{% endhint %}

{% tabs %}
{% tab title="Models by TASK" %}
{% content-ref url="../api-references/text-models-llm" %}
[text-models-llm](https://docs.aimlapi.com/api-references/text-models-llm)
{% endcontent-ref %}

{% content-ref url="../api-references/image-models" %}
[image-models](https://docs.aimlapi.com/api-references/image-models)
{% endcontent-ref %}

{% content-ref url="../api-references/video-models" %}
[video-models](https://docs.aimlapi.com/api-references/video-models)
{% endcontent-ref %}

{% content-ref url="../api-references/music-models" %}
[music-models](https://docs.aimlapi.com/api-references/music-models)
{% endcontent-ref %}

{% content-ref url="../api-references/speech-models" %}
[speech-models](https://docs.aimlapi.com/api-references/speech-models)
{% endcontent-ref %}

{% content-ref url="../api-references/moderation-safety-models" %}
[moderation-safety-models](https://docs.aimlapi.com/api-references/moderation-safety-models)
{% endcontent-ref %}

{% content-ref url="../api-references/3d-generating-models" %}
[3d-generating-models](https://docs.aimlapi.com/api-references/3d-generating-models)
{% endcontent-ref %}

{% content-ref url="../api-references/vision-models" %}
[vision-models](https://docs.aimlapi.com/api-references/vision-models)
{% endcontent-ref %}

{% content-ref url="../api-references/embedding-models" %}
[embedding-models](https://docs.aimlapi.com/api-references/embedding-models)
{% endcontent-ref %}
{% endtab %}

{% tab title="Models by DEVELOPER" %}
**Alibaba Cloud**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud) [Image](https://docs.aimlapi.com/api-references/video-models/alibaba-cloud) [Video](https://docs.aimlapi.com/api-references/image-models/alibaba-cloud) [Text-to-Speech](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/alibaba-cloud) [Embedding](https://docs.aimlapi.com/api-references/embedding-models/alibaba-cloud)

**Anthracite**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/anthracite)

<mark style="background-color:green;">**Anthropic**</mark>: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/anthropic) [Embedding](https://docs.aimlapi.com/api-references/embedding-models/anthropic)

**Assembly AI:** [Speech-To-Text](https://docs.aimlapi.com/api-references/speech-models/speech-to-text/assembly-ai)

**BAAI**: [Embedding](https://docs.aimlapi.com/api-references/embedding-models/baai)

**Baidu**:    [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/baidu)

**ByteDance**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/bytedance)  [Image](https://docs.aimlapi.com/api-references/video-models/bytedance) [Video](https://docs.aimlapi.com/api-references/image-models/bytedance)

**Cohere**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/cohere)

<mark style="background-color:green;">**DeepSeek**</mark>: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/deepseek)

**Deepgram**: [Speech-To-Text](https://docs.aimlapi.com/api-references/speech-models/speech-to-text/deepgram) [Text-to-Speech](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/deepgram)

<mark style="background-color:green;">**ElevenLabs**</mark>**:** [Text-to-Speech](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/elevenlabs) [Voice Chat](https://docs.aimlapi.com/api-references/speech-models/voice-chat/elevenlabs) [Music](https://docs.aimlapi.com/api-references/music-models/elevenlabs)

<mark style="background-color:green;">**Flux**</mark>: [Image](https://docs.aimlapi.com/api-references/image-models/flux)

**Google**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/google) [Image](https://docs.aimlapi.com/api-references/image-models/google) [Video](https://docs.aimlapi.com/api-references/video-models/google) [Music](https://docs.aimlapi.com/api-references/vision-models/ocr-optical-character-recognition/google) [Vision(OCR)](https://docs.aimlapi.com/api-references/music-models/google) [Embedding](https://docs.aimlapi.com/api-references/embedding-models/google)

**Gryphe**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/gryphe)

**Hume AI**: [Text-to-Speech](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/hume-ai)

**Inworld**: [Text-to-Speech](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/inworld)

<mark style="background-color:green;">**Kling AI**</mark>: [Image](https://docs.aimlapi.com/api-references/image-models/kling-ai)  [Video](https://docs.aimlapi.com/api-references/video-models/kling-ai)

**Krea**: [Video](https://docs.aimlapi.com/api-references/video-models/krea)

**LTXV**: [Video](https://docs.aimlapi.com/api-references/video-models/ltxv)

**Meta**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/meta)

**Microsoft**: [Text-to-Speech](https://docs.aimlapi.com/api-references/speech-models/text-to-speech/microsoft)

<mark style="background-color:green;">**MiniMax**</mark>: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/minimax) [Video](https://docs.aimlapi.com/api-references/video-models/minimax) [Music](https://docs.aimlapi.com/api-references/music-models/minimax) [Voice-Chat](https://docs.aimlapi.com/api-references/speech-models/voice-chat)

**Mistral AI**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai) [Vision(OCR)](https://docs.aimlapi.com/api-references/vision-models/ocr-optical-character-recognition/mistral-ai)

**Moonshot**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/moonshot)

**NousResearch**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/nousresearch)

**NVIDIA**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/nvidia)

<mark style="background-color:green;">**OpenAI**</mark>: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/openai) [Image](https://docs.aimlapi.com/api-references/image-models/openai) [Speech-To-Text](https://docs.aimlapi.com/api-references/speech-models/speech-to-text/openai) [Embedding](https://docs.aimlapi.com/api-references/embedding-models/openai)

**Perplexity**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/perplexity)

**PixVerse:** [Video](https://docs.aimlapi.com/api-references/video-models/pixverse)

**RecraftAI**: [Image](https://docs.aimlapi.com/api-references/image-models/recraftai)

**Reve**: [Image](https://docs.aimlapi.com/api-references/image-models/reve)

**Runway**: [Video](https://docs.aimlapi.com/api-references/video-models/runway)

<mark style="background-color:green;">**Stability AI**</mark>: [Image](https://docs.aimlapi.com/api-references/image-models/stability-ai) [Music](https://docs.aimlapi.com/api-references/music-models/stability-ai) [3D-Generation](https://docs.aimlapi.com/api-references/3d-generating-models/stability-ai)

**Sber AI**: [Video](https://docs.aimlapi.com/api-references/video-models/sber-ai)

**Tencent**: [Image](https://docs.aimlapi.com/api-references/image-models/tencent)  [Video](https://docs.aimlapi.com/api-references/video-models/tencent)  [3D](https://docs.aimlapi.com/api-references/3d-generating-models/tencent)

**Together AI**: [Embedding](https://docs.aimlapi.com/api-references/embedding-models/together-ai)

**VEED**: [Video](https://docs.aimlapi.com/api-references/video-models/veed)

**xAI**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/xai) [Image](https://docs.aimlapi.com/api-references/image-models/xai)

**Zhipu**: [Text/Chat](https://docs.aimlapi.com/api-references/text-models-llm/zhipu)
{% endtab %}

{% tab title="Text Models by CAPABILITY" %}
{% content-ref url="../capabilities/completion-or-chat-models" %}
[completion-or-chat-models](https://docs.aimlapi.com/capabilities/completion-or-chat-models)
{% endcontent-ref %}

{% content-ref url="../capabilities/streaming-mode" %}
[streaming-mode](https://docs.aimlapi.com/capabilities/streaming-mode)
{% endcontent-ref %}

{% content-ref url="../capabilities/code-generation" %}
[code-generation](https://docs.aimlapi.com/capabilities/code-generation)
{% endcontent-ref %}

{% content-ref url="../capabilities/thinking-reasoning" %}
[thinking-reasoning](https://docs.aimlapi.com/capabilities/thinking-reasoning)
{% endcontent-ref %}

{% content-ref url="../capabilities/function-calling" %}
[function-calling](https://docs.aimlapi.com/capabilities/function-calling)
{% endcontent-ref %}

{% content-ref url="../capabilities/image-to-text-vision" %}
[image-to-text-vision](https://docs.aimlapi.com/capabilities/image-to-text-vision)
{% endcontent-ref %}

{% content-ref url="../capabilities/web-search" %}
[web-search](https://docs.aimlapi.com/capabilities/web-search)
{% endcontent-ref %}
{% endtab %}
{% endtabs %}

## Browse Solutions

* [AI Search Engine](https://docs.aimlapi.com/solutions/bagoodex/ai-search-engine) – if you need to create a project where information must be found on the internet and then presented to you in a structured format, use this solution.
* [OpenAI Assistants](https://docs.aimlapi.com/solutions/openai/assistants) – if you need to create tailored AI Assistants capable of handling customer support, data analysis, content generation, and more.

***

## Going Deeper

<table data-header-hidden data-full-width="false"><thead><tr><th width="409.4000244140625"></th><th valign="top"></th></tr></thead><tbody><tr><td><p><strong>Use more text model capabilities in your project:</strong><br><br><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/completion-or-chat-models">​Completion and Chat Completion</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/function-calling">Function Calling</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/streaming-mode">Streaming Mode</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/image-to-text-vision">Vision in Text Models (Image-to-Text)</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/code-generation">Code Generation</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/thinking-reasoning">Thinking / Reasoning</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/web-search">Web Search</a><br><br></p></td><td valign="top"><p><strong>Miscellaneous</strong>:<br><br><span data-gb-custom-inline data-tag="emoji" data-code="1f517">🔗</span> <a href="../integrations/our-integration-list">Integrations</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="1f4d7">📗</span> <a href="../glossary">Glossary</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="26a0">⚠️</span> <a href="../errors-and-messages">Errors and Messages</a></p><p><span data-gb-custom-inline data-tag="emoji" data-code="2753">❓</span> <a href="../faq">FAQ </a>​</p><p><br></p></td></tr><tr><td><strong>Learn more about developer-specific features:</strong><br><br><span data-gb-custom-inline data-tag="emoji" data-code="1f4d6">📖</span> <a href="../capabilities/anthropic">Features of Anthropic Models</a><br></td><td valign="top"></td></tr></tbody></table>

## Have a Minute? Help Make the Docs Better!

We’re currently working on improving our documentation portal, and your feedback would be **incredibly** helpful! Take [**a quick 5-question survey**](https://tally.so/r/w4G9Er) (no personal info required!)

You can also rate each individual page using the built-in form on the right side of the screen:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-62017f43d426ea34ff2a6cb09df4076bd12628ee%2Frateform-5.webp?alt=media" alt=""><figcaption></figcaption></figure>

Have suggestions for improvement? [**Let us know!**](https://forms.aimlapi.com/doc)
