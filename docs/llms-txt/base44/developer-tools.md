# Source: https://docs.base44.com/documentation/building-your-app/developer-tools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Base44 developer tools

> Build, debug, and ship smarter on Base44.

Base44 gives you a flexible, developer friendly environment to build, extend, and maintain your apps on top of the Base44 platform. You can work directly with your app’s code, use in product developer tools, integrate with GitHub for version control, and rely more and more on Base44 as a backend service as the platform evolves.

***

## Working with your app’s code

Base44 lets you work with your app’s code so you can create custom experiences while still relying on the platform for infrastructure and runtime. You stay close to the Base44 app model and APIs, which helps your app behave consistently across environments and makes it easier to adopt new platform capabilities over time.

You can mix low code and full code in the same project. Start from Base44 primitives, then drop into code when you need custom logic, integrations, or UI that go beyond what is available out of the box. This balance gives you both speed and control without forcing you to maintain your own underlying platform.

<Frame caption="Editing your app's code in Base44">
    <img src="https://mintcdn.com/base44/HSXlsKQvBkYN-DXR/codeer.png?fit=max&auto=format&n=HSXlsKQvBkYN-DXR&q=85&s=845561c033d8e1acadf501429ed5efbb" alt="Editing your app's code in Base44" width="1915" height="958" data-path="codeer.png" />
</Frame>

<Tip>
  Learn more about [editing your app's code](https://docs.base44.com/developers/app-code/editor/code-tab)
</Tip>

***

## Using in-product developer tools

Base44 includes developer tools that help you understand how your app behaves in real time and debug issues more efficiently. Instead of adding your own ad hoc logging or building separate dashboards, you can inspect what is happening directly from the Base44 environment.

These tools let you see how your app talks to Base44 services and external integrations, monitor requests and responses, and surface important events, errors, or warnings. You can validate assumptions while you work, then iterate safely in staging or preview environments before you roll changes out more broadly.

<Tip>
  Learn more about the [activity monitor](https://docs.base44.com/developers/app-code/editor/activity-monitor)
</Tip>

***

## Integrating with GitHub

Base44 supports a GitHub based workflow so you can manage your app code with modern version control practices. Connecting your app to GitHub makes it easier to collaborate with your team and keep a clean history of every change that goes into your app.

You can use branches and pull requests to review work before it goes live, enforce review or check requirements, and keep your main branches stable. When you connect GitHub workflows and checks, you can test and validate each change, then let Base44 handle deployment from the reviewed code. This creates a clear, auditable path from commit to production.

<Frame caption="Connecting your app to GitHub for automatic syncing">
    <img src="https://mintcdn.com/base44/8-JwIy7QUSD-rZKI/images/ConnectGitHub.png?fit=max&auto=format&n=8-JwIy7QUSD-rZKI&q=85&s=4ec089fc2931c1bdfb98c4aca283182b" alt="Connecting your app to GitHub for automatic syncing" width="429" height="218" data-path="images/ConnectGitHub.png" />
</Frame>

<Tip>
  Learn more about [connecting your app to GitHub](https://docs.base44.com/developers/app-code/local-development/github)
</Tip>

***

## Connecting to external services/ APIs

Base44 includes an integrations layer that lets your app call external services without you managing every API call by hand. Instead of wiring each provider yourself, you use Base44 integrations to handle common patterns like talking to AI models, working with files, sending email, or calling custom APIs, while Base44 manages credentials and execution on the backend.

There are two main types of integrations:

* Built in integrations cover common tasks such as generating text or images with AI, uploading and serving files, or extracting structured data from documents.
* Custom integrations let a workspace administrator import an OpenAPI specification for almost any external API and expose it to your apps as a reusable, named integration that is proxied through the Base44 backend.

Integration calls always run on Base44 infrastructure, so secrets and tokens never live in your frontend. You can invoke them either in the context of the current person using your app or with a service role that has elevated permissions for admin and automation workflows. This gives you a flexible way to connect Base44 to the rest of your stack while keeping security and access control in one place.

<Tip>
  [Learn more about integrations](/Integrations/Using-integrations)
</Tip>

***

## Using Base44 as a backend service (BaaS)

Base44 includes a managed backend platform that is built with AI agents and modern full stack apps in mind. It handles core backend concerns such as data storage, authentication, real time updates, serverless functions, integrations, and hosting so you can focus on product logic and experience.

<Frame>
    <img src="https://mintcdn.com/base44/s2QhPPQ9QJdts6M8/images/baas.png?fit=max&auto=format&n=s2QhPPQ9QJdts6M8&q=85&s=709802bf4eab7c400294b3dd8b9eb363" alt="Baas" width="825" height="402" data-path="images/baas.png" />
</Frame>

You can run Base44 as a backend only service when you bring your own frontend or connect existing applications, or use it as the backend for full stack projects generated from Base44 templates. The CLI scaffolds projects with the configuration you need and connects them to your Base44 backend, while the dashboard lets you manage data, auth, functions, and integrations.

Any frontend framework can talk to Base44 through the JavaScript SDK. During local development your frontend runs on its own dev server and connects to the hosted Base44 backend for data and functions. When you are ready to go live, you can either keep hosting your frontend elsewhere or deploy its built assets to Base44 hosting with custom domains and automatic HTTPS.

Base44 provides a flexible NoSQL data layer, built in authentication and access control, and real time subscriptions so your app can react to changes as they happen. You can add custom backend logic with TypeScript based functions and plug in external services through connectors and integrations, for example for AI models, email, or file handling.

<Tip>
  Learn more about [using Base44 as a backend service](https://docs.base44.com/developers/backend/overview/introduction)
</Tip>


Built with [Mintlify](https://mintlify.com).