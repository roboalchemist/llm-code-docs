# Source: https://console.groq.com/docs/toolhouse

---
description: Learn how to use Toolhouse with Groq to equip your LLMs with tools for code execution, web search, and more—no coding required.
title: Toolhouse + Groq: Equip LLMs with Powerful Tools - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Toolhouse 🛠️🏠](#toolhouse-)

[Toolhouse](https://toolhouse.ai) is the first Backend-as-a-Service for the agentic stack. Toolhouse allows you to define agents as configuration, and to deploy them as APIs. Toolhouse agents are automatically connected to 40+ tools including RAG, MCP servers, web search, webpage readers, memory, storage, statefulness and more. With Toolhouse, you can build both conversational and autonomous agents without the need to host and maintain your own infrastructure.

You can use Groq’s fast inference with Toolhouse. This page shows you how to use Llama 4 Maverick and Groq’s Compound Beta to build a Toolhouse agent.

### [Getting Started](#getting-started)

#### [Step 1: Download the Toolhouse CLI](#step-1-download-the-toolhouse-cli)

Download the Toolhouse CLI by typing this command on your Terminal:

curl

```
npm i -g @toolhouseai/cli
```

#### [Step 2: Log into Toolhouse](#step-2-log-into-toolhouse)

Log into Toolhouse via the CLI:

curl

```
th login
```

Follow the instructions to create a free Sandbox account.

#### [Step 3: Add your Groq API Key to Toolhouse](#step-3-add-your-groq-api-key-to-toolhouse)

Generate a Groq API Key in your [Groq Console](https://console.groq.com/keys), then copy its value.

In the CLI, set your Groq API Key:

curl

```
th secrets set GROQ_API_KEY=(replace this with your Groq API Key)
```

You’re all set! From now on, you’ll be able to use Groq models with your Toolhouse agents. For a list of supported models, refer to the [Toolhouse models page](https://docs.toolhouse.ai/toolhouse/bring-your-model#supported-models).

## [Using Toolhouse with Llama 4 models](#using-toolhouse-with-llama-4-models)

To use a specific model, simply reference the model identifier in your agent file, for example:

* For Llama 4 Scout: `@groq/meta-llama/llama-4-scout-17b-16e-instruct`

Here's an example of a working agent file. You can copy this file and save it as `groq.yaml` . In this example, we use an image generation tool, along with Llama 4 Scout.

curl

```
title: "Scout Example"
prompt: "Tell me a joke about this topic: {topic} then generate an image!"
vars:
  topic: "bananas"
model: "@groq/meta-llama/llama-4-scout-17b-16e-instruct"
public: true
```

Then, run it:

curl

```
th run groq.yaml
```

You will see something like this:

curl

```
━━━━ Stream output for joke ━━━━
Why did the banana go to the doctor? Because it wasn't peeling well!

Using MCP Server: image_generation_flux()

Why did the banana go to the doctor? Because it wasn't peeling well!

![](https://img.toolhouse.ai/tbR5NI.jpg)
━━━━ End of stream for joke ━━━━
```

If the results look good to you, you can deploy this agent using `th deploy groq.yaml`

## [Using Toolhouse with Compound Beta](#using-toolhouse-with-compound-beta)

Compound Beta is an advanced AI system that is designed to agentically [search the web and execute code](https://console.groq.com/docs/agentic-tooling), while being optimized for latency.

To use Compound Beta, simply specify `@groq/compound-beta` or `@groq/compound-beta-mini` as the model identifier. In this example, Compound Beta will search the web under the hood. Save the following file as `groq.yaml`:

curl

```
title: Compound Example
prompt: Who are the Oilers playing against next, and when/where are they playing? Use the current_time() tool to get the current time.
model: "@groq/compound-beta"
```

Run it with the following command:

curl

```
th run compound.yaml
```

You will see something like this:

curl

```
━━━━ Stream output for compound ━━━━
The Oilers are playing against the Florida Panthers next. The game is scheduled for June 12, 2025, at Amerant Bank Arena.
━━━━ End of stream for compound ━━━━
```

Then to deploy the agent as an API:

curl

```
th deploy
```