# Source: https://docs.anyscale.com/archive/configure-sso.md

# Source: https://docs.anyscale.com/administration/organization/configure-sso.md

# Configure SSO for your Anyscale organization

[View Markdown](/administration/organization/configure-sso.md)

# Configure SSO for your Anyscale organization

Anyscale recommends that all customers use single sign-on (SSO) to manage users in their Anyscale organization.

You must be an organization owner to configure SSO for your organization.

note

Anyscale previously used a legacy flow to configure SSO. If your organization had SSO configured using the legacy flow, you can continue to manage SSO using that flow. See [Configure single sign-on (legacy)](/archive/configure-sso.md).

The new flow offers an improved user experience and new features. Anyscale recommends that organizations migrate to the new flow. To migrate to the new flow, contact [Anyscale support](mailto:support@anyscale.com).

## How does SSO work on Anyscale?[​](#how-does-sso-work-on-anyscale "Direct link to How does SSO work on Anyscale?")

Anyscale integrates with many identity providers (IdP) including Okta, Entra ID, and Google. You can also use custom SAML or OIDC to integrate with other providers.

You configure SSO for Anyscale by completing the following steps:

1. Configure the domain or domains used by your organization.
2. Configure your IdP for SSO.

After claiming a domain and enabling SSO, all organization users with the verified domain must use SSO to log in.

important

If you add users to your organization using emails that aren't in a verified domain, these users can't use SSO and continue to log in with a password or email magic link.

If your organization requires a different authentication policy, contact [Anyscale support](mailto:support@anyscale.com).

## Verify your organization domain[​](#verify-your-organization-domain "Direct link to Verify your organization domain")

Verify one or more domains for your organization before enabling SSO.

Your *organization domain* is the domain used by your company email address. If your organization uses subdomains for managing SSO, you must verify each subdomain that needs access to Anyscale.

To verify a domain, complete the following steps:

1. Navigate to **Organization settings > General > Authentication**.
2. Under **Domain claiming**, click **Claim your domain on Anyscale** or **Add another domain**.
3. Enter your domain and click **Continue**. The console detects how you've configured DNS for your domain.
4. Custom instructions for domain verification display, which requires you to register a DNS record for `anyscale.com`. The console dynamically checks your DNS records and confirms when you've completed the flow successfully.

important

If you are unable to register DNS records for your domain, contact [Anyscale support](mailto:support@anyscale.com) to request manual verification of your domain.

note

You can optionally add the same domain to multiple Anyscale organizations. When you associate a domain with more than one Anyscale organization, Anyscale doesn't support automatic memberships for that domain.

## Configure your IdP[​](#configure-your-idp "Direct link to Configure your IdP")

To configure your IdP and enable SSO, complete the following steps:

1. Navigate to **Organization settings > General > Authentication**.
2. Under **Single sign-on (SSO)**, click **Set up SSO**.
3. Select your identity provider from the list.
   <!-- -->
   * If you don't see your identity provider, you can create a connection using SAML or OIDC.
4. Instructions to configure and test the connection with your IdP displays. Complete these steps.
   <!-- -->
   * If you accidentally navigate away, the UI prompts you to **Continue setup** when you return to the **Select your identity provider** screen.

note

Existing sessions continue to function after configuring SSO.

Enabling SSO doesn't invalidate existing API keys or change their lifetime. You can revoke API keys to force new authentication with SSO. See [Manage API keys](/auth/api-keys.md).
