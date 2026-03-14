# Source: https://virustotal.readme.io/docs/sso-authentication.md

# Single Sign On Authentication

VT currently supports SSO authentication with the following services:

* Google
* GitHub
* Microsoft

This means, if you have an account in any of those services, you can use it at VT too!

# Create a new VT account using SSO

When creating a new VT account, you can either create it in the traditional way by entering all your personal information or you can do it using SSO with any of the aforementioned services.

![SSO create account form](https://storage.googleapis.com/vtdocresources/guides/account-management/sso_create_20251009.png)

When choosing any SSO option, you’ll be asked to introduce a username to associate with your account:

![SSO create account introduce username](https://storage.googleapis.com/vtdocresources/guides/account-management/sso_username_20251009.png)

After clicking on “Create account”, you’ll have a fully operational VT account. No need to confirm your email address or make any additional steps.

# Login to an existing account using SSO

If you already have a VT account whose email address is also associated with an account at any of our supported SSO providers, you can login with that provider at VT too.

![SSO login links](https://storage.googleapis.com/vtdocresources/guides/account-management/sso_loginlinks_20251009.png)

When login using SSO, no 2FA is necessary. If the login at the SSO provider is successful you’ll be automatically redirected to VirusTotal’s main page.

# Group SSO settings

In the group settings page, a group administrator can choose among a set of already configured SSO identity providers: google.com, github.com and microsoft.com.

When any of these 3 providers is enabled for the group, all group users will be forced to authenticate exclusively through that provider. If no specific provider is enabled, users have the flexibility to sign in using either basic authentication (username and password) or SSO method if their account is linked to any of the listed services.

![SSO group settings](https://storage.googleapis.com/vtdocresources/guides/account-management/sso_groupsettings_20251009.png)

# SAML

Clients with different identity providers can enable SAML for SSO by selecting that option in the drop-down menu and filling out the required details in the displayed form to complete the setup.

Please note that for forcing users to only authenticate via SAML, a checkbox is provided. If this checkbox is not selected, users can use both methods of authentication: SAML and common credentials.

![SSO SAML](https://storage.googleapis.com/vtdocresources/guides/account-management/sso_saml_20251009.png)

We have articles with examples of how to [configure SAML with Okta](https://virustotal.readme.io/docs/saml-okta), [configure SAML with Ping](https://virustotal.readme.io/docs/saml-ping) or [configure SAML with EntraID](https://virustotal.readme.io/docs/saml-entraid)

Please note that you must manually update rotated certificates in the SAML settings on the platform.

# OIDC

Clients with other identity providers that prefer OIDC for SSO, can select that option in the drop-down menu and fill out the required data in the displayed form to complete the setup.

Again note that for forcing users to only authenticate via OIDC, a checkbox is provided. If this checkbox is not selected, users can use both methods of authentication: OIDC and common user/password credentials.

![SSO OIDC](https://storage.googleapis.com/vtdocresources/guides/account-management/sso_oidc_20251009.png)