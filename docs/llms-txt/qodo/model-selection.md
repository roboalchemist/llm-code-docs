# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/chat/model-selection.md

# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/model-selection.md

# Model Selection

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

Qodo supports a wide range of LLMs (Large Language Models). This guide walks you through configuring different models, including commercial APIs, open-source models, and local setups.

{% hint style="success" %}
This feature is available for **On Prem users** only.
{% endhint %}

{% hint style="warning" %}

### **We strongly recommend keeping the default model.**

Only change it when meeting LLM provider limitations on on-prem installations.

**Do not change the default model for any other reason.**

### Qodo **works the best with its default model.**

{% endhint %}

### Default model <a href="#changing-a-model-in-pr-agent" id="changing-a-model-in-pr-agent"></a>

Qodo is continuously benchmarking the performance of the latest LLM models and we always use the models that produce the best results for code review. The default models used by Qodo (as of December 2025) is GPT-5.2. In some cases we use other models from  the major LLM providers (Anthropic and Google) for redundancy and for higher suitability with specific use cases.&#x20;

### Restrict Qodo to use a specific model

To restrict Qodo to using only one model, add this setting to the [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[config]
model = "..."
```

The models currently supported are:

* `gpt-5`
* `claude-4-sonnet`
* `o4-mini`
* `gemini-2.5-pro`
* `deepseek/r1`

### Change model&#x20;

To switch models, edit the [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[config]
model = "..."
fallback_models = ["..."]
```

Some models require additional parameters or API keys, depending on the provider. These can be configured either in `.secrets.toml` or as environment variables.

Refer to the [LiteLLM documentation](https://litellm.vercel.app/docs/proxy/quick_start#supported-llms) for up-to-date model-specific variables.
