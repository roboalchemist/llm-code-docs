# Source: https://firebase.google.com/docs/ai-assistance/prompt-catalog.md.txt

<br />

The [Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server) comes with a library
of pre-written prompts optimized for developing and running an app with
Firebase.

You can use these prompts to complete various common tasks or goals with your
agentic AI assistants like
Antigravity, Gemini CLI and Gemini Code Assist,
Firebase Studio, Claude Code and Claude Desktop, Cline, Cursor,
GitHub Copilot in VS Code, Windsurf, and more!

Most AI assistants that support MCP provide a convenient way to run these
prompts. For example, if you use the
[Firebase extension for Gemini CLI](https://firebase.google.com/docs/ai-assistance/gcli-extension),
these prompts are available as slash commands:

    /firebase:init

In Gemini CLI, start typing `/firebase:` to see a list of available
commands applicable to your app.

> [!NOTE]
> **Important** : Keep the following in mind when using generative AI with your app:
>
> - Generative AI can make mistakes. Always check its changes or output before deploying to production.
> - Frequently commit snapshots of your code, especially before making major changes to your app.

> [!TIP]
> **Tip:** While the MCP server provides many pre-written prompts for AI assistants, you can also use [Firebase agent skills](https://firebase.google.com/docs/ai-assistance/agent-skills) alongside the MCP server to help your AI assistant understand Firebase best practices and execute complex tasks with higher accuracy and lower cost. Agent skills can assist with setting up services like Authentication, Cloud Firestore, or Firebase AI Logic, or deploying web apps to Firebase Hosting or App Hosting. When you have both the Firebase MCP server and Firebase agent skills installed, skills can teach models how to use the MCP tools to accomplish complex tasks efficiently.

*** ** * ** ***

## Available pre-written prompts

DATABASE AND SECURITY

### Set up backend services

`/firebase:init`


Set up Cloud Firestore and Firebase Authentication in your web app.
[Learn more](https://firebase.google.com/docs/ai-assistance/prompt-catalog/set-up-backend) SECURITY

### Write Firebase Security Rules

`/firebase:generate_security_rules`


Generate and test Firebase Security Rules for Cloud Firestore and
Cloud Storage for Firebase.
[Learn more](https://firebase.google.com/docs/ai-assistance/prompt-catalog/write-security-rules)

<br />

GEN AI

### Add AI features

`/firebase:init`


Add AI features that use Firebase AI Logic in your mobile or web
app.
[Learn more](https://firebase.google.com/docs/ai-assistance/prompt-catalog/add-ai-features) HOSTING

### Deploy to a Firebase hosting service

`/firebase:deploy`


Deploy your web app to the appropriate Firebase hosting service
for your app.
[Learn more](https://firebase.google.com/docs/ai-assistance/prompt-catalog/deploy-to-hosting)

<br />

DEV OPS

### Prioritize \& fix stability issues

`/crashlytics:connect`


Prioritize and fix reported issues in your mobile apps that have
already integrated Firebase Crashlytics.
[Learn more](https://firebase.google.com/docs/ai-assistance/prompt-catalog/prioritize-fix-issues)