# Source: https://docs.gitguardian.com/platform/enterprise-administration/email-domain-management.md

# Manage email domain

> Reserve email domains for your GitGuardian workspace to control user registration and enforce SSO.

## How to reserve an email domain

Once an SAML SSO integration is completed, the users of your GitGuardian workspace (usually the Owner or a Manager)
can request to **reserve one or several specific email domains that belong to them or your company**.
This feature goes one step further in the authentication/security aspect. It is independent from the âforce SSOâ feature.

- When you reserve a domain `company.com`, you **restrict users with an email address "xxxx@company.com" from signing up to GitGuardian and creating their own workspace**. It is a guarantee that there will only be one workspace for users having an email address âxxx@company.comâ.
- When users try to sign up with a reserved email domain address, they are alerted that **they are required to sign up via SSO**.
- Also, reserving an email domain will allow users to **find your custom SSO page just by filling in their email**. Without this
  option you would need to bookmark your SSO login url.

![SSO reserved email domain](/img/platform/enterprise-administration/sso_reserved_email_domain.png)

Users who already have a workspace and are impacted by a newly reserved email domain will not be affected. They will be able to join the workspace that requested these domains be reserved for SSO.

:::info
This feature is reserved to workspaces with Business access (Business or Business trial plans). After the end of a Business trial, the email domains
will no longer be reserved.
This feature is not accessible with GitGuardian self-hosted instances.
:::

## Domain synchronization between regions

Reserved domains are synchronized between the EU and US regions. This ensures that once a domain is reserved in either region, users are prevented from signing up in one region if they already have an account in the other.
