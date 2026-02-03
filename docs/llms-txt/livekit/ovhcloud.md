# Source: https://docs.livekit.io/agents/models/stt/plugins/ovhcloud.md

# Source: https://docs.livekit.io/agents/models/llm/plugins/ovhcloud.md

LiveKit docs › Models › LLM › Plugins › OVHCloud

---

# OVHCloud LLM plugin guide

> How to use the OVHCloud LLM plugin for LiveKit Agents.

Available in:
- [x] Node.js
- [x] Python

## Overview

This plugin allows you to use [OVHCloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/) as an LLM provider for your voice agents. OVHCloud compatibility is provided by the OpenAI plugin using the Chat Completions API format.

## Quick reference

This section includes a basic usage example and some reference material. For links to more detailed documentation, see [Additional resources](#additional-resources).

### Installation

Install the OpenAI plugin to add OVHCloud AI Endpoints support:

**Python**:

```shell
uv add "livekit-agents[openai]~=1.3"

```

---

**Node.js**:

```shell
pnpm add @livekit/agents-plugin-openai@1.x

```

### Authentication

The OVHCloud AI Endpoints plugin requires an [API key](https://ovh.com/manager). You can generate one by creating a new Public Cloud project, then navigate to **AI Endpoints** > **API key**.

Set `OVHCLOUD_API_KEY` in your `.env` file.

### Usage

Use OVHCloud AI Endpoints LLM in your `AgentSession` or as a standalone LLM service. For example, you can use this LLM in the [Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md).

**Python**:

```python
from livekit.plugins import openai

session = AgentSession(
    llm=openai.LLM.with_ovhcloud(
        model="gpt-oss-120b",
    ),
    # ... tts, stt, vad, turn_detection, etc.
)

```

---

**Node.js**:

```typescript
import * as openai from '@livekit/agents-plugin-openai';

const session = new voice.AgentSession({
    llm: new openai.LLM.withOVHcloud(
        model: "gpt-oss-120b"
    ),
    // ... tts, stt, vad, turn_detection, etc.
});

```

### Parameters

This section describes some of the available parameters. See the plugin reference links in the [Additional resources](#additional-resources) section for a complete list of all available parameters.

- **`model`** _(string)_ (optional) - Default: `gpt-oss-120b`: Model to use for inference. To learn more, see [supported models](https://help.ovhcloud.com/csm/en-ca-public-cloud-ai-endpoints-getting-started?id=kb_article_view&sysparm_article=KB0070726).

- **`temperature`** _(float)_ (optional) - Default: `1.0`: Controls the randomness of the model's output. Higher values, for example 0.8, make the output more random, while lower values, for example 0.2, make it more focused and deterministic.

Valid values are between `0` and `1`.

- **`parallel_tool_calls`** _(bool)_ (optional): Controls whether the model can make multiple tool calls in parallel. When enabled, the model can make multiple tool calls simultaneously, which can improve performance for complex tasks.

- **`tool_choice`** _(ToolChoice | Literal['auto', 'required', 'none'])_ (optional) - Default: `auto`: Controls how the model uses tools. Set to 'auto' to let the model decide, 'required' to force tool usage, or 'none' to turn off tool usage.

## Additional resources

The following resources provide more information about using OVHCloud AI Endpoints with LiveKit Agents.

- **[OVHCloud AI Endpoints docs](https://help.ovhcloud.com/csm/en-ca-public-cloud-ai-endpoints-getting-started?id=kb_article_view&sysparm_article=KB0070726)**: OVHCloud AI Endpoints API documentation.

- **[Voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai.md)**: Get started with LiveKit Agents and OVHCloud AI Endpoints.

---

This document was rendered at 2026-02-03T03:25:01.305Z.
For the latest version of this document, see [https://docs.livekit.io/agents/models/llm/plugins/ovhcloud.md](https://docs.livekit.io/agents/models/llm/plugins/ovhcloud.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).