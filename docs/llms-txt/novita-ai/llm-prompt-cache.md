# Source: https://novita.ai/docs/guides/llm-prompt-cache.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt Cache

export const PromptCacheModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("prompt-cache-models");
      if (clientComponent && window.novitaRemoteData.llmModels.status === 'loaded') {
        const modelList = window.novitaRemoteData.llmModels.data.filter(model => {
          return !!model.support_prompt_cache;
        });
        let displayModels = modelList.slice(0, INIT_DISPLAY_COUNT).map(model => {
          return `<li><span class="model-id-item">${model.id}</span></li>`;
        }).join('');
        let showMoreButton = '';
        if (modelList.length > INIT_DISPLAY_COUNT) {
          showMoreButton = `<button id="show-more-prompt-cache-model-btn" style="margin-left: 32px; color: rgb(40 116 255)">View More</button>`;
        }
        clientComponent.innerHTML = `
          <ul>${displayModels}</ul>
          ${showMoreButton}
        `;
        document.getElementById('show-more-prompt-cache-model-btn')?.addEventListener('click', () => {
          clientComponent.innerHTML = `
            <ul>${modelList.map(model => {
            return `<li><span class="model-id-item">${model.id}</span></li>`;
          }).join('')}</ul>
          `;
        });
        clearInterval(interval);
      }
      attempts++;
      if (attempts >= maxAttempts) {
        clearInterval(interval);
      }
    }, 200);
    return <div id="prompt-cache-models"></div>;
  }
};

Prompt Cache is a cost-optimization feature provided by the Novita inference engine.

When a request matches a previous Prompt, the system returns a cached result and charges only a minimal cache token fee — significantly reducing cost and improving response latency.

## 1. Benefits

With Prompt Cache enabled, you gain:

* **Lower Cost**

  Repeated Prompts no longer require full inference. Only minimal cache token fees are charged.

* **Lower Latency**

  Cached results are returned instantly without running the model.

* **Higher Throughput**

  In high-QPS scenarios, Prompt Cache reduces compute load and improves overall system capacity.

* **Transparent to Your Application**

  no additional logic or system changes are required.

## 2. Supported Models

Several serverless open-source models currently support prompt cache billing, including:

<PromptCacheModels />

For pricing details regarding the prompt cache feature of supported models, please refer to: [https://novita.ai/pricing](https://novita.ai/pricing) (see "Cache" section).

## 3. Use Cases

Prompt Cache is highly effective in workloads with **frequent repeated Prompts**, including but not limited to:

* **Template-based Generation**
  * Fixed-format summaries
  * Template-driven rewriting
  * Prompts reused across tasks
* **Text Classification & Field Extraction**
  * Content type classification
  * Tag or key information extraction
* **Content Moderation**
  * Review of comments, ads, or titles
  * Many moderation prompts repeat across users and time
* **Repeated System Prompts in Chat Applications**
  * Chatbot persona definitions
  * Global conversation rules
  * Background information reused across multiple turns
* **Workflow / Assistant-style Prompts**
  * SQL generation assistants
  * Code repair assistants
  * Summary assistants with fixed output formats

These scenarios naturally achieve high cache hit rates, reducing inference cost significantly.

## 4. Response Examples

<Note>
  When the cache is hit, no inference is performed, resulting in significantly lower cost and faster responses.
</Note>

If the model supports prompt caching, your API calls require no modifications. Below is a sample response when hitting the cached result:

```JSON  theme={"system"}
{
    "prompt_tokens": 3295,
    "completion_tokens": 137,
    "total_tokens": 3432,
    "prompt_tokens_details":
    {
        "audio_tokens": 0,
        "cached_tokens": 448,
        "cache_creation_Prompt_tokens": 0,
        "cache_read_Prompt_tokens": 0
    }
}
```


Built with [Mintlify](https://mintlify.com).