# Source: https://docs.base44.com/Enterprise/Enterprise-SSO-and-app-visibility.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing SSO and visibility for your enterprise apps

> Control how team members access your apps and manage their visibility across the enterprise workspace.

Single Sign-On (SSO) for app access and app visibility management help enterprise admins keep workspaces secure and organized. Using SSO for app access means everyone signs into every app with the same company credentials, streamlining security and access. With app visibility controls, you decide how new apps are shared, making it easy to maintain privacy and regulatory standards across your organization.

***

### Managing SSO for app access

Enterprise admins can enforce SSO across all apps in a workspace through a single provider. This makes it effortless for people to sign in to multiple apps and ensures your security standards are applied everywhere.

For example, if your company has 10 different apps in a Base44 workspace, enabling SSO for app access means all users log in with their central company credentials, instead of creating new logins for each app.

<Warning>
  **Important:**

  * Only enterprise admins can manage SSO for app access. Once enabled, app users will use your organization’s SSO credentials to access every app in the workspace.
  * To enforce workspace SSO for all apps, you must add an additional redirect URI to your identity provider (IdP) configuration: `https://app.base44.com/api/workspace_apps/{{WORKSPACE_ID}}/auth/sso/callback`
</Warning>

**To set up SSO for all apps in the workspace:**

1. Set up your [enterprise workspace SSO](/Enterprise/SSO-for-enterprise-workspace).
2. Click your profile icon at the top right of your account.
3. Click the relevant workspace name.
4. Click **Settings** in your profile menu.
5. Click **Apps configuration**.
6. Click the **Enforce workspace SSO for all apps** toggle.
   * **Enabled:** All apps in your workspace will automatically use the workspace SSO settings, and app-level configuration will be disabled.
   * **Disabled:** Your app builders can decide if they want to turn on the workspace SSO in their [app's authentication settings](https://docs.base44.com/Guides/Managing-login-and-registration) in their app's dashboard.

<Frame caption=" Enforcing workspace SSO for all apps in the enterprise workspace">
    <img src="https://mintcdn.com/base44/iYNb0mom7jmWBtLR/images/enforceworkspaceapps.png?fit=max&auto=format&n=iYNb0mom7jmWBtLR&q=85&s=56172f999570c1251c2686982041f4b9" alt=" Enforcing workspace SSO for all apps in the enterprise workspace" width="1439" height="620" data-path="images/enforceworkspaceapps.png" />
</Frame>

***

## Managing app visibility

App visibility management lets you control how new apps are shared and accessed in your workspace. Set default visibility for every new app and decide who can make apps public. These controls help your team meet your organization’s privacy and collaboration rules from the start.

**To configure app visibility and policies:**

1. Click your profile icon at the top right of your account.
2. Click the relevant workspace name.
3. Click **Settings** in your profile menu.
4. Click **Apps configuration**.
5. Click the **Allow members to create public apps** toggle:
   * **Enabled:** Members can create apps with public visibility, making them accessible to anyone on the internet.
   * **Disabled:** Members can only create private apps or apps that are visible to workspace members.
6. Under **Initial app visibility**, choose the starting visibility for all new apps created in this workspace:
   * **Private**: Only specific users can access the app. Log in required.
   * **Workspace**: All workspace members can access the app. Log in required.
   * **Public (Login Required)**: Anyone on the internet can access the app, but must log in.
   * **Public (No Login)**: Anyone on the internet can access the app. No login required.

<Frame caption="Configuring the app visibility in your workspace">
    <img src="https://mintcdn.com/base44/cIC2yESELhBeWgV3/images/appsconfig.png?fit=max&auto=format&n=cIC2yESELhBeWgV3&q=85&s=385685a6d9b94c7f47310b840f9453cd" alt="Configuring the app visibility in your workspace" width="1444" height="615" data-path="images/appsconfig.png" />
</Frame>

***

## FAQs

Select a question below to learn more about app SSO and visibilty.

<AccordionGroup>
  <Accordion title="What happens to existing apps when I enable workspace SSO?">
    Existing apps automatically use your workspace SSO settings if enforcement is enabled. App-level SSO settings are locked and can only be managed by enterprise admins.
  </Accordion>

  <Accordion title="Can app builders override workspace SSO?">
    No. When workspace SSO enforcement is enabled, all workspace apps use the company’s SSO provider. App builders can choose SSO settings only if enforcement is disabled by an admin.
  </Accordion>

  <Accordion title="Can I update visibility after an app is created?">
    Yes, you can change an app’s visibility in the app settings at any time, unless restricted by workspace policies.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).