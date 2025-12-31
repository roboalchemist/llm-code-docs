# Source: https://docs.aimlapi.com/integrations/cline.md

# Cline

## About

Cline is an open-source AI coding assistant with two working modes (Plan/Act), terminal command execution, and support for the Model Context Protocol (MCP) in VS Code.

You can find the Cline repository and community on [GitHub](https://github.com/cline).

## Installing Cline in VS Code

1. Open the **Extensions** tab in the VS Code sidebar.

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4f3015a743429973cae02b25cfb9227814e94412%2Ffile-MSoV7yWuiF.png?alt=media" alt=""><figcaption></figcaption></figure>

2. In the search bar, type **Cline**.
3. Find the extension and click **Install**.

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-8d2380734a9df818597f03c0d7419e521e78b7b0%2Ffile-EtVsh1r3HJ.png?alt=media" alt=""><figcaption></figcaption></figure>

4. After installation, a separate **Cline** tab will appear in the sidebar.

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-7018954f2c60c1dd3b1348146331e7d992feafea%2Ffile-2M7nFjSF7c.png?alt=media" alt=""><figcaption></figcaption></figure>

## **Configuring Cline**

1. Go to the **Cline** tab in the sidebar.
2. Click the gear icon in the top-right corner.

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-e0a862f7fa2c871a91ef56b59feb496c48867df4%2Ffile-jxjkvunu8d.png?alt=media" alt=""><figcaption></figcaption></figure>

In the settings:

* Set **API Provider** to **OpenAI Compatible**.
* In **Base URL**, enter one of our available endpoints.
* In **API Key**, enter your [AI/ML API key](https://aimlapi.com/app/keys).
* In **Model ID**, specify the model name. You can find some model selection tips in our [description of code generation as a capability](https://docs.aimlapi.com/capabilities/code-generation).
* Click **Save**.

All done — start coding with Cline!

## Usage Example

Here’s the request we made:

```
Create a Python file named test and add code to print Hello, world
```

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-ffccb4d6a1169d5d5e9ef2e080bdd325784289b7%2Ffile-hUIEu0dwuF.png?alt=media" alt=""><figcaption></figcaption></figure>

If you expand the **API Request** section, you can view the data — including your prompt.

Since I asked to create a file in the request, the file was generated. You can see a preview and its contents, but it hasn’t been saved yet.

To save the file, Cline asks for confirmation.

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-39a5822c073b775cd6f5de8be6af8c671b0009fa%2Ffile-vI3i1xgY23.png?alt=media" alt=""><figcaption></figcaption></figure>

Once the file is saved, a second API request appears with metadata, along with a notification that the task was successfully completed.

## **Supported Models**

These models have been tested by our team for compatibility with Cline integration.

<details>

<summary>Supported Model List</summary>

* [gpt-3.5-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo)
* [gpt-3.5-turbo-0125](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo)
* [gpt-3.5-turbo-1106](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo)
* [gpt-4o](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-05-13](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-08-06](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini)
* [gpt-4o-mini-2024-07-18](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o-mini)
* [chatgpt-4o-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-05-13](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4o-2024-08-06](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o)
* [gpt-4-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo)
* [gpt-4-turbo-2024-04-09](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo)
* [gpt-4-0125-preview](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-preview)
* [gpt-4-1106-preview](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-preview)
* [o3-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/o3-mini)
* [openai/gpt-4.1-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1)
* [openai/gpt-4.1-mini-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1-mini)
* [openai/gpt-4.1-nano-2025-04-14](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1-nano)
* [openai/o4-mini-2025-04-16](https://docs.aimlapi.com/api-references/text-models-llm/openai/o4-mini)
* [deepseek/deepseek-chat](https://docs.aimlapi.com/api-references/text-models-llm/deepseek/deepseek-chat)
* [deepseek/deepseek-r1](https://docs.aimlapi.com/api-references/text-models-llm/deepseek/deepseek-r1)
* [meta-llama/Llama-3.3-70B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-3.3-70b-instruct-turbo)
* [meta-llama/Llama-3.2-3B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-3.2-3b-instruct-turbo)
* [meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-405b-instruct-turbo)
* [meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-8b-instruct-turbo)
* [meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/meta/meta-llama-3.1-70b-instruct-turbo)
* [meta-llama/llama-4-maverick](https://docs.aimlapi.com/api-references/text-models-llm/meta/llama-4-maverick)
* [Qwen/Qwen2.5-7B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen2.5-7b-instruct-turbo)
* [Qwen/Qwen2.5-Coder-32B-Instruct](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen2.5-coder-32b-instruct)
* [qwen-max](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-max)
* [qwen-max-2025-01-25](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-max)
* [qwen-plus](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-plus)
* [qwen-turbo](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen-turbo)
* [Qwen/Qwen2.5-72B-Instruct-Turbo](https://docs.aimlapi.com/api-references/text-models-llm/alibaba-cloud/qwen2.5-72b-instruct-turbo)
* [mistralai/Mixtral-8x7B-Instruct-v0.1](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mixtral-8x7b-instruct-v0.1)
* [mistralai/Mistral-7B-Instruct-v0.1](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-7b-instruct)
* [mistralai/Mistral-7B-Instruct-v0.2](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-7b-instruct)
* [mistralai/Mistral-7B-Instruct-v0.3](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-7b-instruct)
* [mistralai/mistral-tiny](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-tiny)
* [mistralai/mistral-nemo](https://docs.aimlapi.com/api-references/text-models-llm/mistral-ai/mistral-nemo)
* [google/gemini-2.0-flash-exp](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash-exp)
* [gemini-2.0-flash-exp](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash-exp)
* [google/gemini-2.0-flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash)
* [x-ai/grok-3-beta](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-3-beta)
* [x-ai/grok-3-mini-beta](https://docs.aimlapi.com/api-references/text-models-llm/xai/grok-3-mini-beta)
* [anthracite-org/magnum-v4-72b](https://docs.aimlapi.com/api-references/text-models-llm/anthracite/magnum-v4)
* [MiniMax-Text-01](https://docs.aimlapi.com/api-references/text-models-llm/minimax/text-01)

</details>

## Troubleshooting

Possible Issues:

* **403 status code (no body)** — This is the most common error. Possible causes:
  * You might need to use a different endpoint. Be sure to refer to the documentation for the specific model you've selected from our catalog!
  * The user may have run out of tokens or doesn’t have enough. Check your balance in your account dashboard.
* **400 status code (no body)** — This error occurs when using models that are not compatible with the integration. See the previous section [Supported Models](#supported-models) :point\_up:
