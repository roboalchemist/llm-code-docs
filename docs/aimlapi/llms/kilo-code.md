# Source: https://docs.aimlapi.com/integrations/kilo-code.md

# Kilo Code

## About

[Kilo Code](https://kilocode.ai/) is an open-source AI coding assistant and VS Code extension that enables natural-language code generation, debugging, and refactoring through customizable modes (Architect, Code, Debug, etc.). It supports multiple model providers, integrates with the Model Context Protocol (MCP), and allows developers to extend functionality with custom tools and workflows.

This guide shows how to connect **AI/ML API** as a **custom provider** in **Kilo Code** for VS Code, using the **OpenAI-compatible** path.\
Follow the steps and screenshots below.

***

## Summary

* **Provider:** OpenAI Compatible (inside Kilo Code)
* **Base URL:** `https://api.aimlapi.com/v1`
* **API Key:** from your AI/ML API dashboard
* **Recommended Model IDs:** [openai/gpt-5-chat-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-chat), [openai/o4-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/o4-mini), [openai/gpt-4.1](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1) ( or any other supported model)

***

## 0) Install Kilo Code Extension

If you haven’t installed Kilo Code yet:

1. Open VS Code.
2. Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X).
3. Search for “Kilo Code”.
4. Install the extension by Kilo Code.
5. Reload VS Code if prompted.

After installation, you’ll see the Kilo Code icon in the sidebar.

Or you can install it from the official site: [**kilocode.ai**](https://kilocode.ai/)

***

## 1) Open Kilo Code → “Use your own API key”

From the Kilo Code welcome screen, click **Use your own API key**.

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4b37ce412a842074f98dafac60380443c5a4c8ac%2F01-welcome.png?alt=media" alt=""><figcaption></figcaption></figure></div>

***

## 2) Choose Provider: **OpenAI Compatible**

Open the provider dropdown and select **OpenAI Compatible**.

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4c20ff2ef0a9621bf86a4c2af71dcba4009c2a5f%2F02-provider-dropdown.png?alt=media" alt=""><figcaption></figcaption></figure></div>

{% hint style="info" %}
Tip: Kilo Code also lists many other providers. For AI/ML API use the **OpenAI Compatible** option.
{% endhint %}

***

## 3) Configure AI/ML API Settings

Fill the form as follows:

* **Base URL**

  ```
  https://api.aimlapi.com/v1
  ```
* **API Key**\
  Paste your key from [**https://aimlapi.com/app/keys**](https://aimlapi.com/app/keys)
* **Model** (examples)
  * [openai/gpt-5-chat-latest](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5-chat) ← recommended universal chat
  * [openai/gpt-5-2025-08-07](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-5) ← pinned dated release
  * [openai/o4-mini](https://docs.aimlapi.com/api-references/text-models-llm/openai/o4-mini) ← fast, low-cost
  * [openai/gpt-4.1](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4.1) ← stable classic
  * *any other supported model by your account*
* **Use Azure**: `OFF`
* **Set Azure API version**: leave disabled
* **Image Support**: `ON` if you plan to send images (e.g., 4o / o4-mini)
* **Max Output Tokens**: `-1` (let server decide)
* **Context Window Size**: up to `128000` (adjust as needed)

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-f940a4b63919f8bbb6e4a29c478ed99b69522824%2F03-openai-compatible-config.png?alt=media" alt=""><figcaption></figcaption></figure></div>

{% hint style="info" %}
**Note**: If you have custom headers (e.g., for proxies), add them in the **Custom Headers** field.
{% endhint %}

***

## 4) Run Your First Task

Open the Kilo Code panel, start a task (Ask/Code/Debug), and send a short test message, for example:

```
Hi from AI/ML API!
```

<div align="left" data-with-frame="true"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-32e35e41a4dbff28f03e4268bad890842881a72d%2F04-first-task-success.png?alt=media" alt=""><figcaption></figcaption></figure></div>

You should see a successful response with tokens/usage bars as in the screenshot.

***

## 🔬 Quick API Sanity Check (optional)

You can also sanity-check your key via `curl`:

{% code overflow="wrap" %}

```bash
curl -X POST https://api.aimlapi.com/v1/chat/completions   -H "Authorization: Bearer $AIMLAPI_KEY"   -H "Content-Type: application/json"   -d '{
    "model": "openai/gpt-5-chat-latest",
    "messages": [
      {"role":"system","content":"You are a concise assistant."},
      {"role":"user","content":"Say hello in one sentence."}
    ]
  }'
```

{% endcode %}

If the request succeeds, you’re ready to use the same model inside Kilo Code.

***

## 💡 Tips

* **Profiles**: Create multiple *API Configuration Profiles* (e.g., default = `openai/gpt-5-chat-latest`, heavy = `openai/gpt-5-2025-08-07`, budget = `openai/o4-mini`). Switch per task.
* **Images**: For vision tasks, keep **Image Support** enabled and use a vision-capable model.
* **Token Limits**: Large responses may require raising *Max Output Tokens* or splitting the task.
* **Headers**: If you need custom headers, add them in **Custom Headers**.

***

## 🧰 Troubleshooting

* **401 / Unauthorized**: Re-check your API key and that it’s pasted without spaces. Regenerate if needed.
* **404 / Model not found**: Verify the **exact Model ID** you selected is available to your account.
* **No response / Network issues**: Corporate VPN/Proxy may block `api.aimlapi.com`. Whitelist the domain.
* **Azure mode confusion**: Leave **Use Azure** toggled **off** unless you specifically need Azure routes.

***

## 📚 Helpful Links

* **AI/ML API Keys**: <https://aimlapi.com/app/keys>
* **AI/ML API Dashboard**: <https://aimlapi.com/app>
* **Kilo Code Docs**: <https://kilocode.ai/docs>

***

Enjoy coding with **Kilo Code + AI/ML API**! 🚀
