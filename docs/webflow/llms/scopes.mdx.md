# Source: https://developers.webflow.com/data/reference/scopes.mdx

***

title: Scopes
slug: data/reference/scopes
hidden: false
-------------

## Available scopes

Available scopes are determined by the type of token you're creating. For [Data Client apps](/data/reference/oauth-app) and [site tokens](/data/reference/site-token), refer to the site-level scopes. For [workspace tokens](/data/reference/authentication/workspace-token), refer to the workspace-level scopes.

<Tabs>
  <Tab title="Site-level">
    | Resource           | Scopes                                  | Endpoints                                                                     |
    | :----------------- | :-------------------------------------- | :---------------------------------------------------------------------------- |
    | Assets             | `assets:read`, `assets:write`           | → [API Docs](/data/reference/assets/assets/list)                              |
    | Authorized User    | `authorized_user:read`                  | → [API Docs](/data/reference/token/authorized-by)                             |
    | Authorization info | None required                           | → [API Docs](/data/reference/token/introspect)                                |
    | CMS                | `cms:read`, `cms:write`                 | → [API Docs](/data/reference/cms/collections/list)                            |
    | Comments           | `comments:read`, `comments:write`       | → [API Docs](/data/reference/comments/list-comment-threads)                   |
    | Components         | `components:read`, `components:write`   | → [API Docs](/data/reference/pages-and-components/components/list)            |
    | Custom Code        | `custom_code:read`, `custom_code:write` | → [API Docs](/data/reference/custom-code/custom-code/list)                    |
    | Ecommerce          | `ecommerce:read`, `ecommerce:write`     | → [API Docs](/data/reference/ecommerce/products/list)                         |
    | Forms              | `forms:read`, `forms:write`             | → [API Docs](/data/reference/forms/list)                                      |
    | Pages              | `pages:read`, `pages:write`             | → [API Docs](/data/reference/pages-and-components/pages/list)                 |
    | Sites              | `sites:read`, `sites:write`             | → [API Docs](/data/reference/sites/list)                                      |
    | Site Activity      | `site_activity:read`                    | → [API Docs](/data/reference/enterprise/site-activity/list)                   |
    | Site Configuration | `site_config:read`, `site_config:write` | → [API Docs](/data/reference/enterprise/site-configuration/url-redirects/get) |
    | Users              | `users:read`, `users:write`             | → [API Docs](/data/reference/users/users/list)                                |
    | Webhooks           | Depends on `trigger_type`               | → [API Docs](/data/reference/webhooks/list)                                   |
    | Workspace          | `workspace:read`, `workspace:write`     | → [API Docs](/data/reference/enterprise/workspace-management/create)          |
  </Tab>

  <Tab title="Workspace-level">
    | Resource           | Scopes                    | Endpoints                                                         |
    | :----------------- | :------------------------ | :---------------------------------------------------------------- |
    | Workspace Activity | `workspace_activity:read` | → [API Docs](/data/reference/enterprise/workspace-audit-logs/get) |
  </Tab>
</Tabs>

<Note title="Quick tip: Finding required scopes">
  Each API endpoint lists its required scopes in the description. When planning your integration, check the endpoints you'll use to determine which scopes to request.
</Note>

## Understanding scopes

Scopes are permissions that control what data your app can access. Think of them like permissions on your phone - an app might request access to your camera, photos, or contacts. In Webflow's API:

* Each scope gives access to specific [resources](/data/reference/structure-1)
* Scopes usually come in pairs: `:read` for viewing data, `:write` for modifying data
* Users will see and approve these permissions when connecting to your app

<Note title="Best practice">
  Only request scopes your app actually needs. Requesting unnecessary scopes can make users hesitant to approve your app.
</Note>

## Adding scopes

When creating a Data Client App or an API token, you'll first register your required scopes:

<Tabs>
  <Tab title="Data Client App">
    During [app registration](/data/docs/register-an-app), select the scopes that match your app's required functionality. These scopes define what data your app can access.

    <Frame caption="Scope Registration">
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/35db7e8252baa175397b1e7569bda4ead5ab50d15ac0be3c42d512d529a72719/assets/images/28e0ad2-Large_GIF_1064x696.gif" alt="Scope Registration" />
    </Frame>

    <Note title="Using scopes in OAuth">
      After registration, you'll use these same scopes in your [Authorization URL](/data/reference/oauth-app#constructing-the-authorization-link) during the OAuth flow. This shows users an authorization page where they can review and approve your requested permissions.

      See our [authorization guide](/data/reference/oauth-app) for step-by-step OAuth implementation.
    </Note>
  </Tab>

  <Tab title="API Token">
    When creating a [site](/data/reference/site-token) or [workspace](/data/reference/authentication/workspace-token) token, select the scopes that match your integration's required functionality. These scopes define what data your token can access.

    <Frame caption="Scope Registration">
      <div>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/4214985a35cb0f9fa2cc64b81aad2086bb4138a0312c47a1cb2cd9f242281969/products/data/pages/Data API/rest-introduction/assets/scopes.png" alt="Scope Registration" />
      </div>
    </Frame>
  </Tab>
</Tabs>
