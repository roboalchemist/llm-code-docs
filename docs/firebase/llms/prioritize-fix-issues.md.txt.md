# Source: https://firebase.google.com/docs/ai-assistance/prompt-catalog/prioritize-fix-issues.md.txt

<br />

This prompt can help you prioritize and fix issues in your mobile apps that have
already integrated Crashlytics.

- [**Firebase Crashlytics**](https://firebase.google.com/products/crashlytics) is a lightweight, realtime crash reporter.   
  This prompt provides a conversational and flexible guided workflow to help you prioritize and fix Crashlytics issues in your app.

Find a
[detailed guide about this prompt (and other MCP features for Crashlytics)](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp)
in the Crashlytics documentation.

<br />

|---|
| **If you're using the [Firebase extension for the Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension), just run this command:** `/crashlytics:connect` Below, you can find important prerequisites and limitations for this prompt, as well as usage instructions for other MCP-capable AI tools. |

<br />

## Prerequisites and Limitations

We're working hard to improve the experience, so this list of prerequisites and
imitations may change frequently. Check back often to see if more
capabilities are supported!

- This prompt can only be used with mobile apps that have an ***existing***
  integration with Crashlytics and have reported issues.

- This prompt works with the platforms supported by Crashlytics:
  **Apple, Android, Flutter, and Unity**.

  If you're working with a Unity project, review the
  [FAQ about loading Crashlytics MCP tools and prompts](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp#faq-crashlytics-mcp-tools-and-prompts-not-loading).

## Use the prompt

> [!NOTE]
> **Important** : Keep the following in mind when using generative AI with your app:
>
> - Generative AI can make mistakes. Always check its changes or output before deploying to production.
> - Frequently commit snapshots of your code, especially before making major changes to your app.

Find a
[detailed guide about this prompt (and other MCP features for Crashlytics)](https://firebase.google.com/docs/crashlytics/ai-assistance-mcp)
in the Crashlytics documentation.

1. If you haven't already,
   [install the Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server).   

   Once installed, your MCP-capable AI-powered development tool can access our
   MCP tools and prompts.

   Note that the
   [Firebase extension for Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension)
   automatically installs the Firebase MCP server.
2. Most MCP-capable AI tools provide a way to conveniently run
   this prompt. For example, the Gemini CLI makes MCP prompts available as
   slash commands:

       /crashlytics:connect

3. The prompt launches a guided workflow that helps you prioritize and fix
   issues in your app, for example:

   - View a list of prioritized issues.
   - Debug a specific issue by providing its ID or URL.
   - Request more information about a crash.
   - Ask the agent its reasoning for a suggested root cause.

You can also adapt any of the Firebase pre-written prompts for your specific
environment or requirements.

## Review the prompt's content

You can review the contents of the
[`crashlytics:connect` prompt](https://github.com/firebase/firebase-tools/blob/master/src/mcp/prompts/crashlytics/connect.ts)
in the Firebase GitHub repo.