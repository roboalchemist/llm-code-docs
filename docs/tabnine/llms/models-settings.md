# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/models-settings.md

# Models

Tabnine provides various [AI models](https://docs.tabnine.com/main/welcome/readme/ai-models) for Tabnine Chat. Tabnine Enterprise admins can connect Tabnine to their internal endpoints to enrich the Tabnine Chat experience for users. This allows administrators to integrate their company's private LLM instances, making them accessible to the engineering team directly within Tabnine.

{% hint style="info" %}
**Note**

Tabnine's code completions only use the **Tabnine Universal code completions model,** which is both private and protected.
{% endhint %}

### Private Model Endpoints Supported by Tabnine

{% hint style="info" %}
**Note**

The list of supported models is updated frequently as new models become available.
{% endhint %}

Currently, Tabnine supports the following model providers for private endpoint connections:

<table><thead><tr><th width="61.4912109375"></th><th width="171.7060546875">Model </th><th>Bedrock</th><th>GCP Vertex AI</th><th>Azure</th><th>OpenAI</th><th>OpenAI-Compatible</th></tr></thead><tbody><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt=""></td><td>Claude 4.6 Sonnet</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt=""></td><td>Claude 4.6 Opus</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt=""></td><td>Claude 4.5 Sonnet</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt=""></td><td>Claude 4.5 Opus</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt=""></td><td>Claude 4.5 Haiku</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt=""></td><td>Claude 4 Sonnet</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt=""></td><td>Gemini 3.0 Pro</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt=""></td><td>Gemini 2.5 Flash</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt=""></td><td>Gemini 2.5 Pro</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt=""></td><td>GPT-5.4</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt=""></td><td>GPT-5.3 Codex</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt=""></td><td>GPT-5.2 Codex</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt=""></td><td>GPT-5.2</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt=""></td><td>GPT-5</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt="" data-size="original"></td><td>GPT-4o</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FKbPkgyXoe8RpaRm2CVqe%2Fdevstral.png?alt=media&#x26;token=28a54f54-6803-4bd8-8365-29cdde0900e9" alt="" data-size="original"></td><td>Devstral-Small-2-24B-Instruct-2512</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FKbPkgyXoe8RpaRm2CVqe%2Fdevstral.png?alt=media&#x26;token=28a54f54-6803-4bd8-8365-29cdde0900e9" alt="" data-size="original"></td><td>Devstral-2-123B-Instruct-2512**</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FhoC55ogj5zmtKzmt4OqX%2Fminimax-color.png?alt=media&#x26;token=29fe9411-a413-4c87-9766-7b8ec518d133" alt=""></td><td>MiniMax 2.5</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c800c1f921f0a9179574471daa68624e65ee8aa7%2FTransparent%20Qwen%20logo.png?alt=media" alt=""></td><td>Qwen-3-Coder-480B-A35B-Instruct</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c800c1f921f0a9179574471daa68624e65ee8aa7%2FTransparent%20Qwen%20logo.png?alt=media" alt=""></td><td>Qwen-3-30B <strong>(Chat only)</strong></td><td></td><td></td><td></td><td></td><td>✓</td></tr></tbody></table>

{% hint style="info" %}
\*This list changes frequently\
\
\*\*Devstral 2 (123B parameters) is operating under a modified MIT license. If your organization's global consolidated monthly revenue is exceeding $20 million, utilizing this model requires Devstral's permission.
{% endhint %}

#### Integration Requirements for Models

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e993ad944f9e1f2cf7153646832d154dcd0ff0e6%2Fbedrock-250-removebg-preview.86d95fc7f9a313f21091222ec7b63e1e30ea52ea.png?alt=media" alt="" data-size="line"> **Amazon Bedrock:** Region, Access Key ID, Secret Access Key | [Learn more](https://aws.amazon.com/bedrock/)

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7c750318da4477aa49b555b3a3f3f7e5c6060a2d%2Fazure.png?alt=media" alt="" data-size="line"> **Azure:** Azure endpoint, Key, Deployment ID | [Learn more](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-private-link?view=azureml-api-2\&tabs=cli)

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-3807221a97472486361ebcb3c9c2db2242319374%2Ficon%3Dgpt.svg?alt=media" alt="" data-size="line"> **OpenAI:** Key, OpenAI endpoint | [Learn more](https://platform.openai.com/docs/overview)

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-3807221a97472486361ebcb3c9c2db2242319374%2Ficon%3Dgpt.svg?alt=media" alt="" data-size="line"> **OpenAI-Compatible:** Llama endpoint, OpenAICompatible Model name

<img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7d81bdf14a1abcf26f9fbb4b89313ad1ce39101f%2Fvertex-ai-logo-png_seeklogo-523075.png?alt=media" alt="" data-size="line"> **Google Vertex AI:** Region, Project ID, Service Account | [Learn more](https://cloud.google.com/vertex-ai/docs)

### Viewing and setting up the available chat models

{% hint style="info" %}
**Note**\\

If this functionality isn't visible, we recommend contacting your dedicated account manager at Tabnine. They'll assist you in setting the available chat AI models for your team.
{% endhint %}

Admins manage the available chat models for their accounts and set up private endpoints for chat models:

1. Sign in to the Tabnine console as an admin.
2. Go to the **Models** page under **Settings:**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-6074ab32b948facc2d8264192867d4bbe09cdd8c%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

3. Toggle a model on and enter the relevant provider settings for your private endpoint.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-3a875da051d5ede8c4203dd780602029320d2782%2FScreenshot%202024-11-21%20at%2019.08.07.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9d5f2ad41f09d80b25fcb93638a4a7c14a0505fa%2Fdemo%40tabnine.com.gif?alt=media" alt=""><figcaption></figcaption></figure>

### Setting the default chat model

Admins can set a model as the account's default chat model. The account default model is the default chat model for the account users. However, users can still switch to any other available model.

Change the account default model by expanding a specific model and toggling **Set as default.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-02613a5afe217c1031f06b16a95e7bcd002cf28e%2FSet%20model%20as%20default.png?alt=media" alt=""><figcaption></figcaption></figure>

Change the account default model by expanding a specific model and toggling **Set as default.**

### Bring Your Own AI (BYOAI) – Self‑Managed Models

Bring Your Own AI (BYOAI) lets you connect your own specialized Large Language Models (LLMs) to Tabnine for specific use cases, keep data within your own infrastructure, and configure everything in a self-serve approach. This also enables hybrid deployments with on-premise and cloud models.

#### Adding a self‑managed (BYOAI) model

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FsbfSRXLIgCBXUVI9h7Ri%2Funknown.png?alt=media&#x26;token=0c843aae-371b-45fb-a973-0f51ed5d0f4a" alt=""><figcaption></figcaption></figure>

Tabnine supports OpenAI‑compatible providers for self‑managed models. This includes any provider that exposes an API compatible with the OpenAI format.

To add a new BYOAI model, go to the Models page, then the Self-Managed tab, and click Add model.

In the Provider settings dialog, select Use OpenAI Compatible as a provider for a new model.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FM7It42Q07SmrAwgycbyg%2Funknown.png?alt=media&#x26;token=9708d876-fff4-4c1e-9a91-55b91ea68fed" alt=""><figcaption></figcaption></figure>

Fill in the following fields:

* **Endpoint (required):**- The base URL of your OpenAI‑compatible API endpoint.
* **Key**: The API key used to authenticate requests to your provider. This key is stored securely and used only for requests from your organization.
* **OpenAI Compatible Model name (required):** The model identifier as defined by your provider.
* **Certificate Authority:** Path to a custom certificate authority (CA) bundle if your endpoint uses a private or internal CA. Leave blank if you are using a public certificate authority.
* **Ignore Self Signed Certificate:** Enable this option if your endpoint uses a self‑signed certificate and you want Tabnine to bypass certificate validation.\
  Use this only for internal/testing environments, as it relaxes TLS validation.
* **Max Tokens Per Request:** Upper limit for the total tokens (prompt + response) per request. This helps prevent unexpectedly large or expensive prompts being sent to your model.
* **Max Response Tokens:** Maximum number of tokens that the model is allowed to generate in a response. This controls the length of model outputs and can help manage latency and cost.

Click **Save** to create the model.

Once saved, the new self‑managed model appears in the Self-Managed models list.

<br>
