# Source: https://firebase.google.com/docs/ai-assistance/agent-skills.md.txt

[Video](https://www.youtube.com/watch?v=8V_I4jsXXyo)

Firebase agent skills
([GitHub](https://github.com/firebase/agent-skills)) are portable,
self-contained modules of Firebase-specific
knowledge, instructions, and workflows. They're designed to help AI assistants
understand Firebase best practices and execute complex tasks with higher
accuracy and lower token cost. For a full list of the Firebase agent skills, see
[Available skills](https://firebase.google.com/docs/ai-assistance/agent-skills#available-skills).

## Get started

Firebase agent skills work with any AI assistant that supports skills, including
Antigravity, Gemini CLI, Claude Code, Cursor, and GitHub Copilot.

### Install Firebase agent skills

In most cases, Firebase agent skills can be installed in your preferred editor
with a single command:

### Antigravity

    npx skills add firebase/agent-skills

### Gemini CLI

    gemini extensions install https://github.com/firebase/agent-skills

### Claude Code

    claude plugin marketplace add firebase/agent-skills
    claude plugin install firebase@firebase

### Cursor

    npx skills add firebase/agent-skills

### GitHub Copilot in VS Code

    npx skills add firebase/agent-skills

### Other agents

    npx skills add firebase/agent-skills

### Update Firebase agent skills

We recommend periodically updating your installed skills to get access to new
skills and improvements to existing skills.

You can get all available updates by running the `update` command:

### Antigravity

    npx skills update --all

### Gemini CLI

    gemini extensions update --all

### Claude Code

    claude plugin marketplace update firebase

### Cursor

    npx skills update --all

### GitHub Copilot in VS Code

    npx skills update --all

### Other agents

    npx skills update --all

### Use Firebase agent skills

AI assistants are designed to use skills automatically whenever they detect that
a skill's description matches your current request. However, skills can also be
manually invoked. This is often done by typing `/` in the agent chat and
searching for the skill name.

## Core components of a skill

Each agent skill is a specialized package that can provide the AI assistant with
the following components:

- **Specialized instructions** : Detailed guidance on achieving specific tasks, such as implementing authentication or provisioning a Cloud Firestore database.
- **Best practices**: Built-in security and performance patterns to ensure your app follows Firebase recommendations from the start.
- **Automation scripts**: Executable code that allows your AI agent to perform local environment setup or configuration automatically.

## Benefits to using skills

Using agent skills reduces the manual effort of searching documentation while
improving the efficiency of your AI interactions.

### Reduced token costs

Conventional AI integrations often load massive amounts of documentation
upfront, which consumes significant tokens and increases session costs. Agent
skills use **progressive disclosure** to minimize this overhead:

- The agent initially only "scans" brief metadata to see if a skill is relevant.
- Detailed instructions and resources are only loaded when the agent determines they're necessary for your specific task.

### AI-guided implementation

Instead of manually searching through documentation, you can describe your
intent in natural language. Skills guide your AI assistant to perform tasks such
as the following:

- *Add a sign-in screen to my web app.*
- *Save my to-do list items to a database.*
- *Help me deploy my new web app.*

For a full list of the Firebase agent skills, see
[Available skills](https://firebase.google.com/docs/ai-assistance/agent-skills#available-skills).

## Use skills alongside the Firebase MCP server

Agent skills are designed to complement the
[Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server):

- **Firebase MCP server**: Designed for AI-assisted development workflows, enabling AI assistants to interact with your Firebase projects, resources, and data programmatically.
- **Firebase agent skills** : Provide the quick instructions and recommended practices that tell an agent how to perform Firebase tasks through token-efficient progressive disclosure. They educate the agent on how to use tools like the Firebase CLI and MCP server effectively.

> [!TIP]
> **Tip:** When you have both the Firebase MCP server and Firebase agent skills installed, skills can teach models how to use the MCP tools to accomplish complex tasks efficiently.

## Available skills

Firebase provides a suite of skills for core products. Skills for additional
Firebase products and features are coming soon!

> [!NOTE]
> **Note:** Firebase agent skills are currently optimized for **web apps**.

| Skill | Description |
|---|---|
| `firebase-ai-logic-basics` | Helps integrate Firebase AI Logic (Gemini API) into web applications. Covers setup, multimodal inference, structured output, and security. |
| `firebase-app-hosting-basics` | Streamlines the process of deploying and managing modern web frameworks like Next.js and Angular that require backend support. |
| `firebase-auth-basics` | Helps you implement secure sign-in, manage your user base, and protect your data using authentication-based Security Rules. |
| `firebase-basics` | Assists with setting up your local environment, adding Firebase to your app for the first time, and learning general platform workflows. |
| `firebase-data-connect-basics` | Helps implement and manage Firebase Data Connect to build type-safe, PostgreSQL-backed applications using GraphQL. |
| `firebase-firestore-basics` | Covers the essentials of Cloud Firestore, including database provisioning, writing Security Rules, and performing data operations with the SDK. |
| `firebase-hosting-basics` | Assists with deploying static websites, Single Page Apps (SPAs), and simple microservices. |

## Next steps

- [Learn how to use agent skills with Gemini CLI.](https://geminicli.com/docs/cli/skills/)
- [Learn how to use agent skills with Antigravity.](https://antigravity.google/docs/skills)