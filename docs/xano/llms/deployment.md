# Source: https://docs.xano.com/enterprise/enterprise-features/deployment.md

# Source: https://docs.xano.com/deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment

> Overview of deployment options and resources for taking your Xano projects from development to production.

Deploying a Xano backend means preparing your project for **production use**, ensuring your APIs, data, and integrations are stable and accessible to end users.\
This page serves as a **landing hub** for all deployment-related topics in Xano.

***

## Key Deployment Topics

### [Publishing Your Logic](/the-function-stack/building-with-visual-development#publishing)

Learn how to **publish** your APIs, Custom Functions, Background Tasks, Triggers, Middleware, and AI tools so that your live environment reflects your latest work.\
This guide covers publishing workflows and best practices for releasing updates safely.

### [Static Hosting](/xano-features/static-hosting)

Learn how to host your static frontend files on your Xano instance. This is great for hosting your frontend right alongside your backend, or even just deploying quick tests as you build and iterate on your application.

### [Branching & Merging](/team-collaboration/branching-and-merging)

Use **branching** to work on new features without affecting production.\
When ready, merge your changes back into the main branch to deploy updates confidently.\
This page explains branching strategies for teams, conflict resolution, and merging guidelines.

### [Swagger/OpenAPI Documentation](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation)

Your Xano API is automatically documented with an **OpenAPI (Swagger)** specification.\
Learn how to share this spec with developers, AI copilots, or frontend tools to streamline integration and ensure accurate deployments.

### [Connecting to a Frontend](/connecting-to-a-frontend)

Once your backend is ready, connect it to a frontend application—whether it’s a **no-code builder** like WeWeb or Bubble, an **AI builder** like Lovable, or a **custom codebase** in TypeScript.\
This guide outlines the different connection methods and how to keep your frontend in sync with your live backend.

***

## Deployment Workflow at a Glance

1. **Develop**: Build and test your API endpoints, database schema, and logic in a safe branch or staging environment.
2. **Test**: Test your API endpoints, database schema, and logic in a safe branch or staging environment.
3. **Document**: Review your automatically generated Swagger/OpenAPI documentation to ensure endpoints are clear and up to date.
4. **Publish**: Push your changes to production.
5. **Connect**: Link your live backend to your frontend or external services using the provided API endpoints.

***

> 💡 **Tip**: For advanced teams, combine branching, publishing, and OpenAPI documentation to create a robust CI/CD workflow, making deployments predictable and repeatable.


Built with [Mintlify](https://mintlify.com).