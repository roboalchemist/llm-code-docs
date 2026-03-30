# Source: https://docs.xano.com/connecting-to-a-frontend.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting a Frontend

> Learn how to connect your Xano backend to popular frontends like WeWeb, Bubble, and AI builders like Lovable, use the Swagger (OpenAPI) specification with AI copilots, or integrate with traditional TypeScript development.

<Tip>
  You can also use [Static Hosting](/xano-features/static-hosting) to host your frontend right alongside your backend in Xano.
</Tip>

This guide covers multiple ways to connect a Xano backend to your frontend of choice, whether you’re using **no-code tools**, **AI builders**, or **traditional development**.

***

## Prerequisites & Best Practices

* **Swagger/OpenAPI Documentation**\
  Every Xano API group automatically provides a [Swagger/OpenAPI specification](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation).\
  Use this as your single source of truth for endpoints, headers, and request/response schemas.

* **Personal Access Tokens (PATs)**\
  Many platforms with a native Xano integration require a PAT (personal access token) for authentication. PATs are managed through the [Metadata API](/xano-features/metadata-api) in Xano, which is where you generate and maintain them.

* **Platform Docs First**\
  For frontend-specific instructions, **always start with the platform’s own documentation**. Links to key platform docs are included in each section below.

***

## WeWeb + Xano

WeWeb provides dedicated plugins for connecting to Xano.

### Data Source Plugin

1. In WeWeb, navigate to **Plugins → Data Sources → Xano**.
2. Add your Xano connection and supply your **Personal Access Token** (from the Metadata API).
3. Create **Collections** to fetch data and optionally set global headers at the plugin or collection level.
4. If you also use the Auth plugin, tokens are forwarded automatically.

[WeWeb Xano Data Source Docs](https://docs.weweb.io/plugins/data-sources/xano-data.html)

### Auth Plugin

Use the [WeWeb Xano Auth Plugin](https://docs.weweb.io/plugins/auth-systems/xano-auth.html) to handle signup/login flows, gated content, and role-based redirects.

***

## Bubble + Xano

Bubble can integrate with Xano in two primary ways:

### Xano Connector Plugin

Community-driven plugin built around the official JS SDK. It simplifies authentication and supports real-time features.\
[Bubble Xano Connector Guide](https://elibeachy.gitbook.io/xano-connector/)

### Bubble API Connector

Use Bubble’s native API Connector to configure endpoints manually. Copy endpoint URLs, headers, and payloads directly from your Swagger docs.
[Bubble API Connector Guide](https://www.xano.com/learn/Connect-Xano-Bubble/)

***

## AI Builders (e.g. Lovable)

AI app builders like **Lovable** can ingest your OpenAPI specification to generate an entire frontend with connected API calls.

1. In Xano, open your API group and click **Swagger (OpenAPI Documentation)**.
2. Copy the **OpenAPI/JSON** link.
3. In Lovable (or a similar AI builder), import the spec to auto-generate endpoints, forms, and API actions.

* [Lovable AI Builder](https://lovable.dev/) (see their docs for details)
* Xano’s [Swagger/OpenAPI Documentation](https://docs.xano.com/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation)

***

## Using Swagger with IDE Copilots

Provide the OpenAPI file to your IDE’s AI assistant (e.g. Cursor, GitHub Copilot Chat) to generate accurate code and types.

1. In Xano, open your API group and click **Swagger (OpenAPI Documentation)**.
2. Copy the **OpenAPI/JSON** link.
3. In your IDE of choice, either provide the link to the OpenAPI spec for your API groups, or download them and store them as a part of your project.

***

## Traditional Development (TypeScript / JavaScript)

You can connect to Xano with plain `fetch`/`axios` or use the [offical JS SDK](https://gitlab.com/xano/js-sdk).

### Fetch Example

```ts  theme={null}
const XANO_BASE = "https://your-instance.xanoapi.com/api:x123";
const token = "<USER_JWT_OR_PAT>";

async function getMe() {
  const res = await fetch(`${XANO_BASE}/auth/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error(`Xano error ${res.status}`);
  return res.json();
}
```

### JS SDK

The [Xano JS SDK](https://gitlab.com/xano/js-sdk) provides helpers for authentication and API calls and powers several third-party plugins.

***

## Environment & Troubleshooting Tips

* **Branching**: Use branches for backend logic changes, but keep schemas consistent across branches to avoid frontend mismatches. Read more about [Branching & Merging](/team-collaboration/branching-and-merging).
* **Data Sources**: In WeWeb, you can set different data sources for editor, staging, and production environments. Read more about [WeWeb Xano Data Source](/the-database/database-basics/data-sources).
* **Platform Docs**: For details like real-time features, caching, or auth strategies, always refer to the frontend platform’s official documentation.

***

## Quick Links

* [Xano Swagger/OpenAPI Docs](https://docs.xano.com/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation)
* [WeWeb Xano Data Source](https://docs.weweb.io/plugins/data-sources/xano-data.html)
* [WeWeb Xano Auth](https://docs.weweb.io/plugins/auth-systems/xano-auth.html)
* [Bubble Xano Connector](https://elibeachy.gitbook.io/xano-connector/)
* [Xano JS SDK (GitLab)](https://gitlab.com/xano/js-sdk)
* [Lovable AI Builder](https://lovable.dev/)

***

> 💡 **Reminder**: For frontend-specific configuration (authentication flows, deployment steps, plugin settings, etc.), the **best source of truth is the documentation provided by the frontend platform itself**.


Built with [Mintlify](https://mintlify.com).