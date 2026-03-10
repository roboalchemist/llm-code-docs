# Source: https://render.com/docs/render-dashboard.md

# The Render Dashboard — Manage your Render services, workspaces, and billing.



The Render Dashboard is the web interface for managing everything in your Render workspace—services, team members, billing, and more:

[image: The Render Dashboard]

Your dashboard's main page lists the services in your workspace, along with any [projects](projects) you've organized them into. Click any service to view its details, logs, and settings.

Use the left panel to jump to views for your [Blueprints](infrastructure-as-code) and [environment groups](configure-environment-variables#environment-groups).

This article describes some common dashboard actions to get you up and running. *_Most_ dashboard actions are documented in the article for the corresponding feature.*

> You can also manage Render resources from your terminal with the [Render CLI](cli) or programmatically with the [Render API](api).

## Create a new service

Create a new service by clicking the *+ New* button in the top-right corner of the [Render Dashboard](https://dashboard.render.com):

[image: The New menu in the Render Dashboard]

Select a service type from the list and complete the creation flow to deploy your code.

> *Deploying for the first time?* See [Your First Render Deploy](your-first-deploy).

## Create a workspace

See [Workspaces, Members, and Roles](team-members).

## Navigate the dashboard

Open workspace-wide search with `⌘+K` / `CTRL+K`, then use the arrow keys to jump directly to any resource:

[image: Workspace-wide search in the Render Dashboard]

While viewing a resource, use the breadcrumbs at the top of the page to navigate to a different service, environment, or project:

[image: Breadcrumbs in the Render Dashboard]

Switch workspaces using the dropdown at the top of the left pane:

[image: Switching workspaces in the Render Dashboard]

## Manage billing

From your workspace's homepage in the [Render Dashboard](https://dashboard.render.com) click *Billing* in the left pane:

[image: Opening Billing in the Render Dashboard]

*From this page, you can:*

- View and update your plan
- Update your payment method
- View accrued usage charges for the current billing month
- View invoices for past months
- View usage against your monthly included amounts of:
  - [Free instance hours](free#free-instance-hours)
  - Outbound bandwidth
  - Build pipeline minutes

## Customize appearance

### Set your display theme

The Render Dashboard provides light and dark display themes, along with high-contrast variants of each.

You can also customize the log explorer's theme independently from your main dashboard theme.

*To set your display theme:*

1. Open the account menu in the top-right corner of the [Render Dashboard](https://dashboard.render.com):

     [image: Setting your display theme in the account menu]

2. *If you don't need to toggle high contrast,* click *Theme* to set your display theme and you're all set!

    *If you _do_ need to toggle high contrast,* instead click *Account settings*.

3. Scroll down to the *Appearance* section:

   [image: Theme settings in the Render Dashboard]

4. Click *Edit* to switch between *Light*, *Dark*, and *System* (which follows your operating system's theme).

5. Click *Save changes*.

6. Separately, you can also customize the following from this section:
    - Toggle *High Contrast Mode*.
    - Set the [log explorer's](logging) theme independently from your dashboard theme.

### Set your user avatar

From your [Account Settings page](https://dashboard.render.com/u/settings#profile), click *Edit* under the *Avatar* section:

[image: Editing your user image in the Render Dashboard]

You can upload a custom image or set a text monogram.

By default, Render uses the [Gravatar](https://gravatar.com/) image for your account's email address. If you don't have a Gravatar image, Render sets a text monogram using the first letter of your email address.

### Set your workspace avatar

> Only workspace admins can set the workspace image.

From your workspace's Settings page, click *Edit* under the *Avatar* section:

[image: Editing your user image in the Render Dashboard]

You can upload a custom image or set a text monogram.

By default, Render sets a text monogram using the first letter of your workspace's name.

---

##### Appendix: Glossary definitions

###### outbound bandwidth

The amount of network traffic you send to destinations outside of Render (HTTP responses, third-party API calls, and so on).

Your workspace receives a monthly included amount of outbound bandwidth. If you exceed this amount, Render bills you for a supplementary amount.

Related article: https://render.com/docs/outbound-bandwidth.md

###### pipeline minutes

The amount of time Render spends running *build commands* and *pre-deploy commands* for your services.

Your workspace receives a monthly included amount of pipeline minutes. If you exceed this amount, Render bills you for a supplementary amount.

Related article: https://render.com/docs/build-pipeline.md