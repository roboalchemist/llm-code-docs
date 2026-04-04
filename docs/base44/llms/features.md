# Source: https://docs.base44.com/developers/backend/overview/features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Features

> What the Base44 backend service includes

The Base44 backend service is a managed backend platform that handles data management, authentication, backend functions, and hosting. Define your data models, build your frontend with any framework, and use the Base44 SDK to connect your app.

Base44 provides everything you need to build and deploy full-stack applications:

## Data management

Base44 provides a NoSQL database where you define your data models as [entities](/developers/backend/resources/entities/overview). Each entity is a schema that defines the structure for documents in a collection.

* The database is MongoDB compatible, allowing you to use all MongoDB operators when querying through the SDK.
* Schemas are not enforced, so you can update your data model at any point without running migrations.
* [Row-level and field-level security](/developers/backend/resources/entities/security) control who can access which records and fields with fine-grained authorization rules.
* Realtime subscriptions are available through [`entities.subscribe()`](/developers/references/sdk/docs/type-aliases/entities#subscribe) in the SDK, allowing your app to receive updates when records are created, updated, or deleted.

## Authentication and user management

Built-in authentication handles user registration, login, and session management. Multiple authentication methods are supported out of the box:

* Email and password authentication
* Support for login through social providers like Google, Microsoft, Facebook, and Apple
* Custom identity provider support through SSO

The SDK provides methods for user management, including registration, login, password reset, and profile updates. Learn more in the [`auth` module documentation](/developers/references/sdk/docs/interfaces/auth).

## Backend functions

Write custom backend logic using [Deno](https://docs.deno.com/runtime/)-based serverless functions. Functions run TypeScript code in a secure runtime environment with full access to your app's data and integrations. [Learn more about backend functions](/developers/backend/resources/backend-functions/overview).

## Connectors and integrations

Base44 provides pre-built integrations for common tasks and [OAuth connectors](/developers/backend/resources/connectors) for direct third-party API access. See the [connectors article](/developers/backend/resources/connectors) for setup and configuration.

* [**Built-in integrations**](/developers/references/sdk/docs/type-aliases/integrations): Ready-to-use functionality for common tasks like AI text generation, image creation, file uploads, and email.
* [**Custom integrations**](/developers/references/sdk/docs/type-aliases/integrations#customintegrationsmodule): Pre-configured external APIs, set up by a workspace administrator who imports an OpenAPI specification. Calls are proxied through Base44's backend, so credentials are never exposed to the frontend.
* [**Connectors**](/developers/references/sdk/docs/interfaces/connectors): OAuth connections to third-party services that provide access tokens for direct API interactions.

## Local development

Run your backend project on your own machine to test changes instantly and catch issues before deploying. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for details.

## Deployment and hosting

Deploy your frontend apps' built files to Base44's site hosting platform with the CLI using a single command. The platform supports custom domains and provides automatic HTTPS.

Base44 site hosting currently supports Single Page Applications (SPAs) only. Frameworks must be configured for static export. Server-side rendering or server components are not supported. If you need server features, you can still use the Base44 backend services with any client type and deploy your frontend to an external hosting provider.

## See also

* [CLI command reference](/developers/references/cli/commands/introduction): All available CLI commands
* [JavaScript SDK](/developers/references/sdk/getting-started/overview): Connect your app to the backend


Built with [Mintlify](https://mintlify.com).