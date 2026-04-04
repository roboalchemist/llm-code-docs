# Source: https://firebase.google.com/docs/ai-assistance/prompt-catalog/add-ai-features.md.txt

<br />

This prompt can help you add AI features to your mobile or web app.

- [**Firebase AI Logic**](https://firebase.google.com/products/firebase-ai-logic) for AI features that securely access the Gemini API directly from your app. This prompt sets up your Firebase Project to use the Gemini Developer API and writes the code in your app for experiences like chat, multimodal analysis, and image generation and editing.

You can use this prompt with an existing Firebase project; however, if you don't
have a Firebase project, the prompt will guide you through setting up everything
for Firebase.

<br />

|---|
| **If you're using the [Firebase extension for the Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension), just run this command:** `/firebase:init` Below, you can find important prerequisites and limitations for this prompt, as well as usage instructions for other agentive MCP-capable AI assistants. |

<br />

## Prerequisites and Limitations

We're working hard to improve the experience, so this list of prerequisites and
imitations may change frequently. So check back often to see if more
capabilities are supported!

- This prompt sets up a AI features within the ***existing*** codebase of an
  **Android** app, **web** app, or **Flutter** app. The app doesn't need to be
  deployed or published yet.

- This prompt is not yet optimized for:

  - iOS apps or Unity games.
  - Some AI capabilities, including bidirectional streaming with the Gemini Live API, access to the Imagen models, hybrid on-device inference, and set up of tools.
- For image generation features, your Firebase Project must be on the
  pay-as-you-go Blaze pricing plan. You might be eligible to claim $300 of
  credits to get started.

## Use the prompt

> [!NOTE]
> **Important** : Keep the following in mind when using generative AI with your app:
>
> - Generative AI can make mistakes. Always check its changes or output before deploying to production.
> - Frequently commit snapshots of your code, especially before making major changes to your app.

1. If you haven't already,
   [install the Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server).   

   Once installed your agentive MCP-capable AI assistant can access our MCP
   tools and prompts.

   Note that the
   [Firebase extension for Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension)
   automatically installs the Firebase MCP server.
2. Most agentive MCP-capable AI assistants provide a way to conveniently run
   this prompt. For example, the Gemini CLI makes these prompts available as
   slash commands:

       /firebase:init

3. You can follow up on the init prompt to let the AI assistant know that you
   want to enable Firebase AI Logic:

       I want to enable Firebase AI Logic in my app

4. After that, you can instruct the AI assistant to implement an AI feature
   upon your behalf:

       Help me add an image generation feature.

You can also adapt any of the Firebase pre-written prompts for your specific
environment or requirements.

## Review the prompt's content

You can review the contents of the
[`firebase:init` prompt](https://github.com/firebase/firebase-tools/blob/master/src/mcp/prompts/core/init.ts)
in the Firebase GitHub repo.

This `firebase:init` prompt orchestrates several service-specific prompts for
each constituent task or Firebase service.