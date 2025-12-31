# Source: https://docs.aimlapi.com/integrations/elizaos.md

# ElizaOS

## About

[ElizaOS](https://eliza.how/docs/intro) is a powerful multi-agent simulation framework designed to create, deploy, and manage autonomous AI agents. Built with TypeScript, it provides a flexible and extensible platform for developing intelligent agents that can interact across multiple platforms while maintaining consistent personalities and knowledge.

## Installation

1. Install `bun` и `Node.js` (v18+)
2. Clone the repo and run:

```bash
git clone <https://github.com/elizaos/eliza-starter.git> 
cd eliza-starter 
cp .env.example .env 
bun i && bun run build && bun start
```

You can find more details in the [official documentation](https://eliza.how/docs/intro#installation).

## How to Use AIML API via ElizaOS

1. Define your [AIMLAPI key](https://aimlapi.com/app/keys) and other environment variables:

```bash
AIMLAPI_API_KEY=sk-***
AIMLAPI_SMALL_MODEL=openai/gpt-3.5-turbo
AIMLAPI_MEDIUM_MODEL=anthropic/claude-3-5-sonnet-20240521-v2:0
AIMLAPI_LARGE_MODEL=google/gemini-2.0-pro
```

2. Configure your character in the `character.json` file as follows:

```json
{
  "modelProvider": "aimlapi",
  "settings": {
    "model": "gpt-4",
    "maxInputTokens": 200000,
	...
  }
}
```

ElizaOS provides a UI at <http://localhost:3000>. Each configured character appears as a separate conversation partner in the left-hand panel:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-90ea96f4911eea149df4b7c2d16caa76cf80e551%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Click the small speaker icon below any message to hear it read aloud:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-8596dd084dbb6fc191adc6baf9c0d346bbec3866%2F%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png?alt=media" alt=""><figcaption></figcaption></figure>

## Our Supported Models

In the environment variables for ElizaOS, you can specify almost any of our [text models](https://docs.aimlapi.com/api-references/text-models-llm#complete-text-model-list), including:

* OpenAI ChatGPT ([openai/gpt-3.5-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-3.5-turbo), [gpt-4-turbo](https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4-turbo), ...),
* Google Gemini ([google/gemini-2.0-flash](https://docs.aimlapi.com/api-references/text-models-llm/google/gemini-2.0-flash), ...)
