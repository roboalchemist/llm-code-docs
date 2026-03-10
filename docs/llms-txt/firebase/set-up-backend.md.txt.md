# Source: https://firebase.google.com/docs/ai-assistance/prompt-catalog/set-up-backend.md.txt

<br />

This prompt can help you set up several backend services for a web app.

- [**Cloud Firestore database**](https://firebase.google.com/products/firestore) for your app's structured
  data.   

  The prompt provisions a database instance, writes the code in your app to
  interact with the database, and writes and deploys Firebase Security Rules
  to help protect user data.

- [**Firebase Authentication**](https://firebase.google.com/products/auth) to secure your app and user
  data.   

  The prompt guides you to enable your chosen sign-in providers and writes the
  code in your app to interact with that provider (like adding sign-up and
  login pages).

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

- This prompt sets up backend services within the ***existing*** codebase of a
  **web** app. The app doesn't need to be deployed yet.

- This prompt is not yet optimized for:
  iOS apps, Android apps, Flutter apps, or Unity games

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

You can also adapt any of the Firebase pre-written prompts for your specific
environment or requirements.

## Review the prompt's content

You can review the contents of the
[`firebase:init` prompt](https://github.com/firebase/firebase-tools/blob/master/src/mcp/prompts/core/init.ts)
in the Firebase GitHub repo.

This `firebase:init` prompt orchestrates several service-specific prompts for
each constituent task or Firebase service.