# Source: https://novita.ai/docs/guides/llm-anthropic-compatibility.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Anthropic SDK Compatibility

export const AnthropicCompatibilityModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("anthropic-compatibility-models");
      if (clientComponent && window.novitaRemoteData.llmModels.status === 'loaded') {
        const modelList = window.novitaRemoteData.llmModels.data.filter(model => {
          return (model.endpoints || []).includes('anthropic');
        });
        let displayModels = modelList.slice(0, INIT_DISPLAY_COUNT).map(model => {
          return `<li><span class="model-id-item">${model.id}</span></li>`;
        }).join('');
        let showMoreButton = '';
        if (modelList.length > INIT_DISPLAY_COUNT) {
          showMoreButton = `<button id="show-more-anthropic-compatibility-model-btn" style="margin-left: 32px; color: rgb(40 116 255)">View More</button>`;
        }
        clientComponent.innerHTML = `
          <ul>${displayModels}</ul>
          ${showMoreButton}
        `;
        document.getElementById('show-more-anthropic-compatibility-model-btn')?.addEventListener('click', () => {
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
    return <div id="anthropic-compatibility-models"></div>;
  }
};

Novita AI provides a compatibility API that allows you to use the Anthropic SDK with Novita AI models. This is useful if you are already using the Anthropic SDK and want to switch to Novita AI models.

## Supported Models

Currently, only the following models are compatible with the Anthropic SDK:

<AnthropicCompatibilityModels />

## Quick Start Guide

This guide demonstrates how to use the Anthropic SDK with the Novita AI models step by step.

### 1. Install the Anthropic SDK

<CodeGroup>
  ```bash Python icon="python" theme={"system"}
  pip install anthropic
  ```

  ```bash TypeScript icon="js" theme={"system"}
  npm install @anthropic-ai/sdk
  ```
</CodeGroup>

### 2. Initialize the Client

The Anthropic SDKs are designed to pull the API key and base URL from the environmental variables: `ANTHROPIC_API_KEY` and `ANTHROPIC_BASE_URL`. Also, you can supply the parameters to the Anthropic client when initializing it.

<Tip>
  You can view and manage your API keys on the [settings page](https://novita.ai/settings/key-management?utm_source=getstarted).
</Tip>

* Using Environment Variables

<CodeGroup>
  ```bash Bash icon="terminal" theme={"system"}
  export ANTHROPIC_BASE_URL="https://api.novita.ai/anthropic"
  export ANTHROPIC_API_KEY="<YOUR_NOVITA_API_KEY>"
  ```
</CodeGroup>

* Set the parameters while initializing the Anthropic client

<CodeGroup>
  ```python Python icon="python" theme={"system"}
  import anthropic

  client = anthropic.Anthropic(
      base_url="https://api.novita.ai/anthropic",
      api_key="<YOUR_NOVITA_API_KEY>",
      # Rewrite header
      default_headers={
          "Content-Type": "application/json",
          "Authorization": "Bearer <YOUR_NOVITA_API_KEY>",
      }
  )
  ```

  ```typescript TypeScript icon="js" theme={"system"}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
      baseURL: "https://api.novita.ai/anthropic",
      apiKey: "<YOUR_NOVITA_API_KEY>",
      // Rewrite header
      defaultHeaders: {
        "Content-Type": "application/json",
        Authorization: `Bearer <YOUR_NOVITA_API_KEY>`,
      }
  });
  ```
</CodeGroup>

### 3. Call the API

<CodeGroup>
  ```python Python icon="python" theme={"system"}
  import anthropic

  # Initialize the client, if you already set `ANTHROPIC_BASE_URL` and `ANTHROPIC_API_KEY` 
  # in the environment variables, you can omit the `api_key` and `base_url` parameters.
  client = anthropic.Anthropic(
      base_url="https://api.novita.ai/anthropic",
      api_key="<YOUR_NOVITA_API_KEY>",
      # Rewrite header
      default_headers={
          "Content-Type": "application/json",
          "Authorization": "Bearer <YOUR_NOVITA_API_KEY>",
      }
  )

  message = client.messages.create(
      model="moonshotai/kimi-k2-instruct",
      max_tokens=1000,
      temperature=1,
      system=[
          {
              "type": "text",
              "text": "You are a world-class poet. Respond only with short poems."
          }
      ],
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Why is the ocean salty?"
                  }
              ]
          }
      ]
  )

  print(message.content)
  ```

  ```typescript TypeScript icon="js" theme={"system"}
  import Anthropic from "@anthropic-ai/sdk";

  // Initialize the client, if you already set `ANTHROPIC_BASE_URL` and `ANTHROPIC_API_KEY` 
  // in the environment variables, you can omit the `baseURL` and `apiKey` parameters.
  const anthropic = new Anthropic({
      baseURL: "https://api.novita.ai/anthropic",
      apiKey: "<YOUR_NOVITA_API_KEY>",
      // Rewrite header
      defaultHeaders: {
        "Content-Type": "application/json",
        Authorization: `Bearer <YOUR_NOVITA_API_KEY>`,
      }
  });

  const msg = await anthropic.messages.create({
    model: "moonshotai/kimi-k2-instruct",
    max_tokens: 1000,
    temperature: 1,
    system="You are a world-class poet. Respond only with short poems.",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Why is the ocean salty?"
          }
        ]
      }
    ]
  });

  console.log(msg);
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).