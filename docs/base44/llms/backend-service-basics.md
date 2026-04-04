# Source: https://docs.base44.com/developers/backend/overview/backend-service-basics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backend Service Basics

> What the Base44 backend service is, who it's for, and how it fits with the main Base44 platform

The Base44 backend service is the same backend that powers Base44's app editor, available as a standalone service. It's a complete backend-as-a-service (BaaS) that includes:

* <Icon icon="database" /> **Data management**: Store and query data without managing servers.
* <Icon icon="user-lock" /> **User authentication**: Built-in login, social auth, and session handling.
* <Icon icon="code" /> **Backend functions**: Custom backend code, callable from your app or externally.
* <Icon icon="plug" /> **Integrations**: Pre-built connections to AI, email, file storage, and more.
* <Icon icon="globe" /> **Hosting**: Deploy your frontend with HTTPS and custom domains.

For more details on these features and others, see [Features](/developers/backend/overview/features).

## Base44 app editor vs the Base44 backend service

The Base44 app editor generates complete apps, frontend and backend together. The Base44 backend service gives you just the backend, so you can build your own frontend or skip the frontend entirely.

|                    | Base44 App Editor               | Base44 Backend Service                                                                                                                              |
| ------------------ | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What you get**   | AI-generated frontend + backend | Backend only                                                                                                                                        |
| **How you build**  | Describe what you want in chat  | Code in your own IDE, or use an AI coding assistant                                                                                                 |
| **Frontend**       | Auto-generated React app        | Bring your own on any framework, or don't have one at all                                                                                           |
| **Best for**       | Non-developers, quick builds    | Developers, custom projects                                                                                                                         |
| **Starting point** | base44.com                      | [Base44 CLI](/developers/references/cli/commands/introduction), or [skills](/developers/backend/overview/base44-skills) in your AI coding assistant |

**Use the backend service if you:**

* Need pixel-perfect control over your frontend design and UX.
* Have an existing frontend project that needs a backend.
* Want to build for platforms the app editor doesn't support, like mobile.
* Want to integrate Base44's backend into a larger system.

**You might prefer the app editor if you:**

* Want to build entirely in Base44's interface.
* Want the fastest path from idea to working app.
* Prefer a guided, visual experience over a code-first workflow.

## How the backend service works

You create and manage backend service projects using the Base44 CLI. The CLI sets up a local project structure where you define your backend resources, such as entities and functions, and optionally include frontend code.

You interact with your backend using the [JavaScript SDK](/developers/references/sdk/getting-started/overview). This is the same SDK used in Base44's AI-generated apps. Use it in your own frontend, or from any other app or service that needs to connect to your backend.

When you're ready, deploy your project with a single CLI command. Your backend resources and any frontend files are deployed to Base44's infrastructure.

## Example use cases

* **Custom-designed web apps**: Design your own frontend when you need full creative control. Match your brand exactly or craft unique experiences. Use any framework while Base44 handles the backend.
* **Headless apps**: Build apps without a traditional frontend, like a Telegram bot that calls your backend functions via HTTP.
* **Mobile apps**: Build a mobile app with a JavaScript-based mobile framework like React Native, using the SDK to connect to your Base44 backend.
* **Extend existing projects**: Add Base44's data management, authentication, or backend logic to a project you've already built.

<CardGroup cols={2}>
  <Card title="Get started" icon="rocket" href="/developers/backend/overview/introduction">
    Set up the CLI and create your first project.
  </Card>

  <Card title="Explore features" icon="list" href="/developers/backend/overview/features">
    Learn more about what the backend service includes.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).