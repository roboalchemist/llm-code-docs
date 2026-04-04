# Source: https://casdoor.github.io/docs/how-to-connect/mcp/overview

Title: MCP server overview | Casdoor · AI-Native Identity and Access Management (IAM) / SSO Platform with MCP Server

URL Source: https://casdoor.github.io/docs/how-to-connect/mcp/overview

Markdown Content:
MCP server overview | Casdoor · AI-Native Identity and Access Management (IAM) / SSO Platform with MCP Server
===============

[Skip to main content](https://casdoor.github.io/docs/how-to-connect/mcp/overview#__docusaurus_skipToContent_fallback)

[![Image 1: Casdoor](https://cdn.casbin.org/img/casdoor-logo_1185x256_dark.png)](https://casdoor.github.io/)[Docs](https://casdoor.github.io/docs/overview)[LLM & MCP](https://casdoor.github.io/docs/how-to-connect/mcp/overview)[Integrations](https://casdoor.github.io/ecosystem)[Password App](https://casdoor.github.io/docs/how-to-connect/totp-authenticator-app)[Blog](https://casdoor.github.io/blog)[Help](https://casdoor.github.io/help)[For Enterprise](https://casdoor.com/)

[English](https://casdoor.github.io/docs/how-to-connect/mcp/overview#)
*   [English](https://casdoor.github.io/docs/how-to-connect/mcp/overview)
*   [Español](https://casdoor.github.io/es/docs/how-to-connect/mcp/overview)
*   [Français](https://casdoor.github.io/fr/docs/how-to-connect/mcp/overview)
*   [Deutsch](https://casdoor.github.io/de/docs/how-to-connect/mcp/overview)
*   [日本語](https://casdoor.github.io/ja/docs/how-to-connect/mcp/overview)
*   [中文](https://casdoor.github.io/zh/docs/how-to-connect/mcp/overview)
*   [Tiếng Việt](https://casdoor.github.io/vi/docs/how-to-connect/mcp/overview)
*   [Português](https://casdoor.github.io/pt/docs/how-to-connect/mcp/overview)
*   [Türkçe](https://casdoor.github.io/tr/docs/how-to-connect/mcp/overview)
*   [Polski](https://casdoor.github.io/pl/docs/how-to-connect/mcp/overview)
*   [Українська](https://casdoor.github.io/uk/docs/how-to-connect/mcp/overview)
*   
* * *

*   [Help translate](https://crowdin.com/project/casdoor-website)

[](https://github.com/casdoor/casdoor)[](https://discord.gg/5rPsrAzK7S)

Search Ctrl K

[Online Demo](https://door.casdoor.com/)

*   [The basics](https://casdoor.github.io/docs/category/the-basics) 
    *   [Overview](https://casdoor.github.io/docs/overview)
    *   [Core concepts](https://casdoor.github.io/docs/basic/core-concepts)
    *   [Server installation](https://casdoor.github.io/docs/basic/server-installation)
    *   [Configuration](https://casdoor.github.io/docs/basic/configuration)
    *   [Try with Docker](https://casdoor.github.io/docs/basic/try-with-docker)
    *   [Try with Helm](https://casdoor.github.io/docs/basic/try-with-helm)
    *   [Public API](https://casdoor.github.io/docs/basic/public-api)
    *   [Tutorials](https://casdoor.github.io/docs/basic/tutorials)

*   [Deployment](https://casdoor.github.io/docs/category/deployment) 
    *   [Deploying with Docker](https://casdoor.github.io/docs/deployment/docker)
    *   [Deploying behind Nginx](https://casdoor.github.io/docs/deployment/nginx)
    *   [Deploying to Kubernetes](https://casdoor.github.io/docs/deployment/k8s)
    *   [Data initialization](https://casdoor.github.io/docs/deployment/data-initialization)
    *   [Hosting static files in a CDN](https://casdoor.github.io/docs/deployment/deploy-cdn)
    *   [Hosting static files on an intranet](https://casdoor.github.io/docs/deployment/deploy-intranet)
    *   [Database migration](https://casdoor.github.io/docs/deployment/db-migration)
    *   [Version information](https://casdoor.github.io/docs/deployment/version-info)

*   [Connecting to Casdoor](https://casdoor.github.io/docs/category/connecting-to-casdoor) 
    *   [Overview](https://casdoor.github.io/docs/how-to-connect/overview)
    *   [Standard OIDC client](https://casdoor.github.io/docs/how-to-connect/oidc-client)
    *   [Casdoor SDKs](https://casdoor.github.io/docs/how-to-connect/sdk)
    *   [Single sign-on (SSO)](https://casdoor.github.io/docs/session/single-sign-on)
    *   [Single sign-out (SSO logout)](https://casdoor.github.io/docs/session/single-sign-out)
    *   [Vue SDK](https://casdoor.github.io/docs/how-to-connect/vue-sdk)
    *   [Desktop SDKs](https://casdoor.github.io/docs/category/desktop-sdks) 
    *   [Mobile SDKs](https://casdoor.github.io/docs/category/mobile-sdks) 
    *   [Casdoor CLI](https://casdoor.github.io/docs/how-to-connect/cli)
    *   [Plugins and middlewares](https://casdoor.github.io/docs/how-to-connect/plugin)
    *   [Chrome extension](https://casdoor.github.io/docs/how-to-connect/chrome-extension)
    *   [Next.js](https://casdoor.github.io/docs/how-to-connect/nextjs)
    *   [Nuxt](https://casdoor.github.io/docs/how-to-connect/nuxt)
    *   [OAuth 2.0](https://casdoor.github.io/docs/how-to-connect/oauth)
    *   [Guest authentication](https://casdoor.github.io/docs/how-to-connect/guest-auth)
    *   [Casdoor as a CAS server](https://casdoor.github.io/docs/how-to-connect/cas)
    *   [SAML](https://casdoor.github.io/docs/category/saml) 
    *   [MCP server](https://casdoor.github.io/docs/category/mcp-server) 
        *   [MCP server overview](https://casdoor.github.io/docs/how-to-connect/mcp/overview)
        *   [MCP authentication](https://casdoor.github.io/docs/how-to-connect/mcp/authentication)
        *   [MCP tools reference](https://casdoor.github.io/docs/how-to-connect/mcp/tools)
        *   [MCP authorization and scopes](https://casdoor.github.io/docs/how-to-connect/mcp/authorization)
        *   [MCP integration example](https://casdoor.github.io/docs/how-to-connect/mcp/integration)
        *   [MCP error handling](https://casdoor.github.io/docs/how-to-connect/mcp/error-handling)
        *   [MCP troubleshooting](https://casdoor.github.io/docs/how-to-connect/mcp/troubleshooting)
        *   [Connect Claude Desktop to MCP](https://casdoor.github.io/docs/how-to-connect/mcp/connect-claude-desktop)
        *   [Connect Cursor to MCP](https://casdoor.github.io/docs/how-to-connect/mcp/connect-cursor)
        *   [Connect ChatGPT to MCP](https://casdoor.github.io/docs/how-to-connect/mcp/connect-chatgpt)

    *   [Face ID](https://casdoor.github.io/docs/how-to-connect/face-id)
    *   [WebAuthn](https://casdoor.github.io/docs/how-to-connect/webauthn)

*   [Developer guide](https://casdoor.github.io/docs/category/developer-guide) 
    *   [Frontend](https://casdoor.github.io/docs/developer-guide/frontend)
    *   [Generating Swagger docs](https://casdoor.github.io/docs/developer-guide/swagger)

*   [Organizations](https://casdoor.github.io/docs/category/organizations) 
    *   [Overview](https://casdoor.github.io/docs/organization/overview)
    *   [Organization tree](https://casdoor.github.io/docs/organization/organization-tree)
    *   [Password complexity](https://casdoor.github.io/docs/organization/passwordComplexity)
    *   [Password obfuscator](https://casdoor.github.io/docs/organization/passwordObfuscator)
    *   [Account customization](https://casdoor.github.io/docs/organization/accountCustomization)
    *   [Customize theme](https://casdoor.github.io/docs/organization/customize-theme)
    *   [MFA items](https://casdoor.github.io/docs/organization/mfa-items)

*   [Applications](https://casdoor.github.io/docs/category/applications) 
    *   [Overview](https://casdoor.github.io/docs/application/overview)
    *   [Application terminology](https://casdoor.github.io/docs/application/terminology)
    *   [Application configuration](https://casdoor.github.io/docs/application/config)
    *   [Dynamic client registration](https://casdoor.github.io/docs/application/dynamic-client-registration)
    *   [Application categories](https://casdoor.github.io/docs/application/categories)
    *   [Custom scopes](https://casdoor.github.io/docs/application/scopes)
    *   [Providers](https://casdoor.github.io/docs/application/providers)
    *   [Sign-in methods](https://casdoor.github.io/docs/application/signin-methods)
    *   [Exclusive sign-in](https://casdoor.github.io/docs/application/exclusive-signin)
    *   [Sign-up items table](https://casdoor.github.io/docs/application/signup-items-table)
    *   [Sign-in items table](https://casdoor.github.io/docs/application/signin-items-table)
    *   [Login UI customization](https://casdoor.github.io/docs/application/ui-customization)
    *   [Specify login organization](https://casdoor.github.io/docs/application/specify-login-organization)
    *   [Application tags](https://casdoor.github.io/docs/application/tags)
    *   [Invitation codes](https://casdoor.github.io/docs/application/invitation-code)
    *   [Shared application](https://casdoor.github.io/docs/application/shared-application)

*   [MCP authorization](https://casdoor.github.io/docs/category/mcp-authorization) 
    *   [Casdoor as MCP Auth Provider](https://casdoor.github.io/docs/mcp-auth/overview)
    *   [MCP auth setup](https://casdoor.github.io/docs/mcp-auth/setup)
    *   [Third-party MCP server integration](https://casdoor.github.io/docs/mcp-auth/third-party-integration)

*   [Permissions](https://casdoor.github.io/docs/category/permissions) 
    *   [Overview](https://casdoor.github.io/docs/permission/overview)
    *   [Permission configuration](https://casdoor.github.io/docs/permission/permission-configuration)
    *   [Exposed Casbin APIs](https://casdoor.github.io/docs/permission/exposed-casbin-apis)
    *   [Adapter](https://casdoor.github.io/docs/permission/adapter)

*   [Providers](https://casdoor.github.io/docs/category/providers) 
    *   [Overview](https://casdoor.github.io/docs/provider/overview)
    *   [OAuth](https://casdoor.github.io/docs/category/oauth) 
    *   [Email](https://casdoor.github.io/docs/category/email) 
    *   [SMS](https://casdoor.github.io/docs/category/sms) 
    *   [Notifications](https://casdoor.github.io/docs/category/notifications) 
    *   [Storage](https://casdoor.github.io/docs/category/storage) 
    *   [SAML](https://casdoor.github.io/docs/category/saml-1) 
    *   [Payments](https://casdoor.github.io/docs/category/payments) 
    *   [Captcha](https://casdoor.github.io/docs/category/captcha) 
    *   [Web3](https://casdoor.github.io/docs/category/web3) 
    *   [Face ID](https://casdoor.github.io/docs/category/face-id) 
    *   [Identity verification](https://casdoor.github.io/docs/category/identity-verification) 

*   [Resources](https://casdoor.github.io/docs/category/resources) 
    *   [Overview](https://casdoor.github.io/docs/resources/overview)

*   [SaaS management](https://casdoor.github.io/docs/category/saas-management) 
    *   [Overview](https://casdoor.github.io/docs/pricing/overview)
    *   [Product](https://casdoor.github.io/docs/products/product)
    *   [Product store](https://casdoor.github.io/docs/products/product-store)
    *   [Shopping cart](https://casdoor.github.io/docs/products/cart)
    *   [Payment](https://casdoor.github.io/docs/products/payment)
    *   [Order](https://casdoor.github.io/docs/products/order)
    *   [Plan](https://casdoor.github.io/docs/pricing/plan)
    *   [Pricing](https://casdoor.github.io/docs/pricing/)
    *   [Subscription](https://casdoor.github.io/docs/pricing/subscription)
    *   [Transaction](https://casdoor.github.io/docs/pricing/transaction)

*   [Multi-factor authentication](https://casdoor.github.io/docs/category/multi-factor-authentication) 
    *   [MFA / 2FA](https://casdoor.github.io/docs/user/multi-factor-authentication)
    *   [MFA items](https://casdoor.github.io/docs/organization/mfa-items)
    *   [Casdoor authenticator app](https://casdoor.github.io/docs/how-to-connect/totp-authenticator-app)
    *   [MFA providers](https://casdoor.github.io/docs/category/mfa-providers) 

*   [Users](https://casdoor.github.io/docs/category/users) 
    *   [Overview](https://casdoor.github.io/docs/user/overview)
    *   [User impersonation](https://casdoor.github.io/docs/user/impersonation)
    *   [User roles](https://casdoor.github.io/docs/user/roles)
    *   [User permissions](https://casdoor.github.io/docs/user/permissions)
    *   [Forms](https://casdoor.github.io/docs/user/forms)

*   [Invitations](https://casdoor.github.io/docs/category/invitations) 
    *   [Overview](https://casdoor.github.io/docs/invitation/overview)

*   [IP allowlist](https://casdoor.github.io/docs/category/ip-allowlist) 
    *   [IP allowlist](https://casdoor.github.io/docs/ip-whitelist/)

*   [Syncer](https://casdoor.github.io/docs/category/syncer) 
    *   [Overview](https://casdoor.github.io/docs/syncer/overview)
    *   [Database syncer](https://casdoor.github.io/docs/syncer/Database)
    *   [Azure AD syncer](https://casdoor.github.io/docs/syncer/AzureAD)
    *   [Active Directory syncer](https://casdoor.github.io/docs/syncer/ActiveDirectory)
    *   [Google Workspace syncer](https://casdoor.github.io/docs/syncer/GoogleWorkspace)
    *   [Keycloak syncer](https://casdoor.github.io/docs/syncer/Keycloak)
    *   [WeCom syncer](https://casdoor.github.io/docs/syncer/WeCom)
    *   [DingTalk syncer](https://casdoor.github.io/docs/syncer/DingTalk)

*   [Certificates](https://casdoor.github.io/docs/category/certificates) 
    *   [Overview](https://casdoor.github.io/docs/cert/overview)

*   [Tokens](https://casdoor.github.io/docs/category/tokens) 
    *   [Overview](https://casdoor.github.io/docs/token/overview)

*   [Sessions](https://casdoor.github.io/docs/category/sessions) 
    *   [Overview](https://casdoor.github.io/docs/session/overview)
    *   [Session management](https://casdoor.github.io/docs/session/management)
    *   [Single sign-on (SSO)](https://casdoor.github.io/docs/session/single-sign-on)
    *   [Single sign-out (SSO logout)](https://casdoor.github.io/docs/session/single-sign-out)

*   [Webhooks](https://casdoor.github.io/docs/category/webhooks) 
    *   [Webhooks](https://casdoor.github.io/docs/webhooks/overview)

*   [LDAP](https://casdoor.github.io/docs/category/ldap) 
    *   [Overview](https://casdoor.github.io/docs/ldap/overview)
    *   [LDAP configuration and sync](https://casdoor.github.io/docs/ldap/config)
    *   [LDAP server](https://casdoor.github.io/docs/ldap/ldapserver)

*   [RADIUS](https://casdoor.github.io/docs/category/radius) 
    *   [Overview](https://casdoor.github.io/docs/radius/overview)

*   [SCIM](https://casdoor.github.io/docs/category/scim) 
    *   [Overview](https://casdoor.github.io/docs/scim/overview)

*   [Integrations](https://casdoor.github.io/docs/category/integrations) 
    *   [C++](https://casdoor.github.io/docs/category/cpp) 
    *   [C#](https://casdoor.github.io/docs/category/csharp) 
    *   [Go](https://casdoor.github.io/docs/category/go) 
    *   [Java](https://casdoor.github.io/docs/category/java) 
    *   [JavaScript](https://casdoor.github.io/docs/category/javascript) 
    *   [Lua](https://casdoor.github.io/docs/category/lua) 
    *   [PHP](https://casdoor.github.io/docs/category/php) 
    *   [Ruby](https://casdoor.github.io/docs/category/ruby) 
    *   [Haskell](https://casdoor.github.io/docs/category/haskell) 
    *   [Python](https://casdoor.github.io/docs/category/python) 

*   [Monitoring](https://casdoor.github.io/docs/category/monitoring) 
    *   [Web UI monitoring](https://casdoor.github.io/docs/monitoring/Web-UI)
    *   [Prometheus](https://casdoor.github.io/docs/monitoring/Prometheus)

*   [Internationalization](https://casdoor.github.io/docs/internationalization)
*   [Contributor guide](https://casdoor.github.io/docs/contributing)

*   [](https://casdoor.github.io/)
*   [Connecting to Casdoor](https://casdoor.github.io/docs/category/connecting-to-casdoor)
*   [MCP server](https://casdoor.github.io/docs/category/mcp-server)
*   MCP server overview

On this page

MCP server overview
===================

Casdoor exposes a **Model Context Protocol (MCP)** server at `/api/mcp`. Clients (e.g. AI assistants or automation tools) can call it over JSON-RPC 2.0 to manage applications, users, and other resources without using Casdoor’s REST API directly.

What is MCP?[​](https://casdoor.github.io/docs/how-to-connect/mcp/overview#what-is-mcp "Direct link to What is MCP?")
---------------------------------------------------------------------------------------------------------------------

MCP is a JSON-RPC 2.0 protocol for discovering and calling tools provided by a server. Casdoor’s MCP server exposes tools so clients can manage Casdoor resources in a standard way.

Getting Started[​](https://casdoor.github.io/docs/how-to-connect/mcp/overview#getting-started "Direct link to Getting Started")
-------------------------------------------------------------------------------------------------------------------------------

The MCP endpoint is available at `/api/mcp` and accepts POST requests with JSON-RPC 2.0 payloads. Before making tool calls, clients must complete the initialization handshake:

`POST /api/mcp{  "jsonrpc": "2.0",  "id": 1,  "method": "initialize",  "params": {    "protocolVersion": "2024-11-05",    "capabilities": {},    "clientInfo": {      "name": "my-client",      "version": "1.0.0"    }  }}`

The server responds with its capabilities:

`{  "jsonrpc": "2.0",  "id": 1,  "result": {    "protocolVersion": "2024-11-05",    "capabilities": {      "tools": {        "listChanged": true      }    },    "serverInfo": {      "name": "Casdoor MCP Server",      "version": "1.0.0"    }  }}`

After initialization, send a notification to indicate the client is ready:

`POST /api/mcp{  "jsonrpc": "2.0",  "method": "notifications/initialized"}`

[Edit this page](https://github.com/casdoor/casdoor-website/edit/master/docs/how-to-connect/mcp/overview.md)

Created by[![Image 2: hsluoyz](https://avatars.githubusercontent.com/hsluoyz)hsluoyz](https://github.com/hsluoyz)

[Previous MCP server](https://casdoor.github.io/docs/category/mcp-server)[Next MCP authentication](https://casdoor.github.io/docs/how-to-connect/mcp/authentication)

*   [What is MCP?](https://casdoor.github.io/docs/how-to-connect/mcp/overview#what-is-mcp)
*   [Getting Started](https://casdoor.github.io/docs/how-to-connect/mcp/overview#getting-started)

Docs

*   [Getting Started](https://casdoor.github.io/docs/basic/server-installation)
*   [Overview](https://casdoor.github.io/docs/overview)
*   [Casdoor API](https://door.casdoor.com/swagger/)
*   [SDK](https://casdoor.github.io/docs/how-to-connect/sdk)

Community

*   [Discord](https://discord.gg/5rPsrAzK7S)
*   [Stack Overflow](https://stackoverflow.com/search?q=casdoor)
*   [Google Groups](https://groups.google.com/g/casdoor)

More

*   [Blog](https://casdoor.github.io/blog)
*   [![Image 3: GitHub Repo stars](https://img.shields.io/github/stars/casdoor/casdoor?label=Casdoor&style=social)](https://github.com/casdoor/casdoor)

[![Image 4: CNCF Landscape](https://landscape.cncf.io/images/logo_header.svg)](https://landscape.cncf.io/)

Copyright © 2026 Casdoor contributors. Casdoor is part of [CNCF Landscape](https://landscape.cncf.io/).

Feedback

How would you rate your experience?
-----------------------------------

Hate Love

Next
