# Source: https://firebase.google.com/docs/ai-assistance/prompt-catalog/deploy-to-hosting.md.txt

<br />

This prompt can help you deploy your web app to an appropriate Firebase hosting
service.

This prompt instructs the AI to analyze your code and choose the correct
Firebase hosting service based on the app's needs. No more decision-making or
misconfigured services.

- [**Firebase Hosting**](https://firebase.google.com/products/hosting) for your static web apps.

- [**Firebase App Hosting**](https://firebase.google.com/products/app-hosting) for your full-stack
  Angular and Next.js apps.

You can use this prompt with an existing Firebase project; however, if you don't
have a Firebase project, the prompt will guide you through setting up everything
for Firebase.

<br />

|---|
| **If you're using the [Firebase extension for the Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension), just run this command:** `/firebase:deploy` Below, you can find important prerequisites and limitations for this prompt, as well as usage instructions for other agentive MCP-capable AI assistants. |

<br />

## Prerequisites and Limitations

We're working hard to improve the experience, so this list of prerequisites and
imitations may change frequently. So check back often to see if more
capabilities are supported!

- This prompt deploys an ***existing*** codebase of a
  **web** app.

- This prompt is not yet optimized for:

  - Flutter apps that target web
- For deployment to Firebase App Hosting, your Firebase Project must be on the
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

       /firebase:deploy

You can also adapt any of the Firebase pre-written prompts for your specific
environment or requirements.

## Review the prompt's content

You can review the contents of the
[`deploy` prompt](https://github.com/firebase/firebase-tools/blob/master/src/mcp/prompts/core/deploy.ts)
in the Firebase GitHub repo.

This `deploy` prompt orchestrates several service-specific prompts for
each constituent task or Firebase service.