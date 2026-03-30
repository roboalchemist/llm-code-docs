# Source: https://docs.api7.ai/enterprise/api-portal/custom-portal.md

# Customize Developer Portal

This guide covers how to customize the **Developer Portal** based on [API7 Developer Portal Boilerplate](https://github.com/api7/api7-portal-boilerplate).

## Overview[â](#overview "Direct link to Overview")

[API Portal](https://docs.api7.ai/enterprise/key-concepts/api-portal.md) includes a customizable Developer Portal for developers to discover and consume APIs. API7 provides an open-source [Developer Portal Boilerplate](https://github.com/api7/api7-portal-boilerplate) as the foundation, which includes:

**Built-in Components:**

* Built with [Next.js](https://nextjs.org/), allowing frontend engineers to use familiar technology stacks
* Complete user management system built with [Better Auth](https://www.better-auth.com/)
* Integrated with [@api7/portal-sdk](https://github.com/api7/portal-sdk-typescript) for API Portal API integration

**Built-in Features:**

* Email/Password authentication (SSO can be enabled)
* Display API Products with OpenAPI documentation rendering
* Support for `Try it Out` to test APIs
* Support for creating Applications and Credentials
* Support for integration with Identity Provider using DCR protocol

Your frontend engineers can customize and extend this foundation to meet your requirements.

For more details, see the [Boilerplate repository](https://github.com/api7/api7-portal-boilerplate).

## Configuration[â](#configuration "Direct link to Configuration")

All configuration is managed via `apps/site/config.yaml`. Copy from `config.yaml.example` and customize for your environment. The configuration supports environment variable substitution:

| Syntax           | Behavior                                      |
| ---------------- | --------------------------------------------- |
| `${VAR}`         | Required - error if `VAR` is not set          |
| `${VAR:default}` | Optional - uses `default` if `VAR` is not set |

### Connect to API Portal Backend[â](#connect-to-api-portal-backend "Direct link to Connect to API Portal Backend")

The Developer Portal connects to the API Portal backend API. Ensure this endpoint is accessible from your Developer Portal:

config.yaml

```
portal:
  url: ${PORTAL_URL}
  token: ${PORTAL_TOKEN}
```

**Creating Portal Token:**

1. Log in to API7 Enterprise Dashboard and switch to API7 Provider Portal.
2. Navigate to **Developer Portal Settings**.
3. Generate a **Token** for API access.
4. Copy the token (format: `a7prt-xxxxxxxxxxxx`).

### Application Settings[â](#application-settings "Direct link to Application Settings")

config.yaml

```
app:
  name: "Your Developer Portal"      # Displayed in browser title and header
  desc: "Your portal description"    # Used for SEO meta description
  baseURL: "https://your-portal.example.com"  # Public URL for generating links and SEO
  trustedOrigins:                    # Allowed origins for CORS and authentication callbacks
    - "https://your-portal.example.com"
```

## Branding Customization[â](#branding-customization "Direct link to Branding Customization")

note

Changes in this section require rebuilding and redeploying the application to take effect. Changes to `config.yaml` require restarting the application.

### Logo and Assets[â](#logo-and-assets "Direct link to Logo and Assets")

Replace the following files with your organization's assets:

| File    | Location                    | Purpose          |
| ------- | --------------------------- | ---------------- |
| Favicon | `apps/site/app/favicon.ico` | Browser tab icon |
| Logo    | `apps/site/public/logo.svg` | Header logo      |

### Theme Customization[â](#theme-customization "Direct link to Theme Customization")

Edit `apps/site/app/globals.css` to customize colors and styling. The portal uses Tailwind CSS, Shadcn UI, and Ant Design.

**Example: Customize primary color**

globals.css

```
:root {
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
}
```

For available theme variables, see the `globals.css` file in the Boilerplate repository.

## Authentication[â](#authentication "Direct link to Authentication")

The boilerplate uses [Better Auth](https://www.better-auth.com/) for authentication.

### Email and Password[â](#email-and-password "Direct link to Email and Password")

This configuration controls email-and-password authentication for user sign-up and sign-in.

config.yaml

```
auth:
  emailAndPassword:
    enabled: true
    requireEmailVerification: false
```

Better Auth does not provide built-in email provider integration. To enable email verification, you need to integrate your preferred email provider SDK in `apps/site/src/lib/auth/server.ts`. Setting `requireEmailVerification: true` without this integration will not send any emails. For more details, see the [Better Auth Email Documentation](https://www.better-auth.com/docs/concepts/email).

### SSO Integration[â](#sso-integration "Direct link to SSO Integration")

Better Auth supports integration with a variety of popular OAuth providers, such as Github and Google.

config.yaml

```
auth:
  socialProviders:
    github:
      clientId: ${GITHUB_CLIENT_ID}
      clientSecret: ${GITHUB_CLIENT_SECRET}
    google:
      clientId: ${GOOGLE_CLIENT_ID}
      clientSecret: ${GOOGLE_CLIENT_SECRET}
```

For enterprise identity providers, you can configure a generic OAuth plugin. This requires modifying the code in `apps/site/src/lib/auth/server.ts`. For more details, see the [Better Auth OAuth Documentation](https://www.better-auth.com/docs/concepts/oauth).

## Extending the Portal[â](#extending-the-portal "Direct link to Extending the Portal")

The boilerplate provides extension points for custom development:

| Extension Point | Location                  | Description                  |
| --------------- | ------------------------- | ---------------------------- |
| Pages           | `apps/site/app/`          | Add or modify Next.js pages  |
| Components      | `apps/site/components/`   | Custom UI components         |
| Auth Logic      | `apps/site/src/lib/auth/` | Authentication customization |
| API Routes      | `apps/site/app/api/`      | Custom backend endpoints     |

For advanced customization, refer to [Next.js](https://nextjs.org/docs) and [Better Auth](https://www.better-auth.com) documentation.

## Portal SDK[â](#portal-sdk "Direct link to Portal SDK")

The [Portal SDK](https://github.com/api7/portal-sdk-typescript) (`@api7/portal-sdk`) provides a TypeScript client for interacting with the API Portal backend API. The boilerplate has this SDK pre-integrated. You can also use it independently to build custom integrations.

### Installation[â](#installation "Direct link to Installation")

```
npm install @api7/portal-sdk
```

### Server-Side Usage[â](#server-side-usage "Direct link to Server-Side Usage")

For backend applications or BFF (Backend for Frontend):

```
import { API7Portal } from '@api7/portal-sdk'

const client = new API7Portal({
  endpoint: 'https://api7-portal-api.example.com',  // API Portal backend API URL
  token: 'a7prt-...',
  getDeveloperId: async () => await getDeveloperIdFromSession(),
});

const products = await client.apiProduct.list();
```

### Client-Side Usage[â](#client-side-usage "Direct link to Client-Side Usage")

For browser-based applications with a BFF proxy:

```
import { API7Portal } from '@api7/portal-sdk/browser'

const client = new API7Portal();
const products = await client.apiProduct.list();
```

For complete SDK documentation and available APIs, see the [Portal SDK repository](https://github.com/api7/portal-sdk-typescript). You can also refer to the [Boilerplate repository](https://github.com/api7/api7-portal-boilerplate) for real-world usage examples.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* [Developer Portal Boilerplate](https://github.com/api7/api7-portal-boilerplate)

* [Portal SDK (TypeScript)](https://github.com/api7/portal-sdk-typescript)

* [Better Auth Documentation](https://www.better-auth.com/docs)

* Key Concepts

  <!-- -->

  * [API Portal](https://docs.api7.ai/enterprise/key-concepts/api-portal.md)
  * [API Products](https://docs.api7.ai/enterprise/key-concepts/api-products.md)
  * [Developers](https://docs.api7.ai/enterprise/key-concepts/developers.md)
