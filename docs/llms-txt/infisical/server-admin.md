# Source: https://infisical.com/docs/documentation/platform/admin-panel/server-admin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Admin Console

> Configure and manage server related features

The Server Admin Console provides **server administrators** with the ability to
customize settings and manage users for their entire Infisical instance.

<Note>
  The first user to setup an account on your Infisical instance is designated as
  the server administrator by default.
</Note>

## Accessing the Server Admin Console

On the sidebar, hover over **Admin** to access the settings dropdown and press the **Server Admin Console** option.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/access-server-admin-panel.png" alt="Access Server Admin Console" />

## General Tab

Configure general settings for your instance.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/admin-panel-general.png" alt="General Settings" />
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/admin-panel-general-1.png" alt="General Settings 1" />

### Allow User Signups

User signups are enabled by default, allowing **Anyone** with access to your instance to sign up. This can alternatively be **Disabled** to prevent any users from signing up.

### Restrict Signup Domain

Signup can be restricted to users matching one or more email domains, such as your organization's domain, to control who has access to your instance.

### Default Organization

If you're using SAML/LDAP/OIDC for only one organization on your instance, you can specify a default organization to use at login to skip requiring users to manually enter the organization slug.

### Trust Emails

By default, users signing up through SAML/LDAP/OIDC will still need to verify their email address to prevent email spoofing. This requirement can be skipped by enabling the switch to trust logins through the respective method.

### Broadcast Messages

Auth consent content is displayed to users on the login page. They can be used to display important information to users, such as a maintenance message or a new feature announcement. Both HTML and Markdown formatting are supported, allowing for customized styling like below:

```
**You are entering a confidential website**
```

```html  theme={"dark"}
<div style="font-weight: bold;">You are entering a confidential website</div>
```

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/auth-consent-usage.png" alt="Auth Consent Usage" />

Page frame content is displayed as a header and footer in ALL protected pages. Like the auth consent content, both HTML and Markdown formatting are supported here as well.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/page-frame-usage.png" alt="Page Frame Usage" />

## Authentication Tab

From this tab, you can configure which login methods are enabled for your instance.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/admin-panel-auths.png" alt="Authentication Settings" />

## Rate Limit Tab

This tab allows you to set various rate limits for your Infisical instance. You do not need to redeploy when making changes to rate limits as these will be propagated automatically.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/admin-panel-rate-limits.png" alt="Rate Limit Settings" />

<Note>
  Note that rate limit configuration is a paid feature. Please contact
  [sales@infisical.com](mailto:sales@infisical.com) to purchase a license for its use.
</Note>

## User Management Tab

From this tab, you can view all the users who have signed up for your instance. You can search for users using the search bar and remove them from your instance by clicking on the three dots icon on the right. Additionally, the Server Admin can grant server administrator access to other users through this menu.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/admin-panels/admin-panel-users.png" alt="User Management" />

<Note>
  Note that rate limit configuration is a paid feature. Please contact
  [sales@infisical.com](mailto:sales@infisical.com) to purchase a license for its use.
</Note>
