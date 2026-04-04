# Source: https://checklyhq.com/docs/admin/team-management/microsoft-azure-ad.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Microsoft Entra ID for Single Sign-on in Checkly

> This page illustrates the standard procedure to follow in order to get started with Microsoft Entra ID SSO (formerly Azure AD) on Checkly. 

## Initial SSO configuration

Setting up SSO for your organisation starts with providing [Checkly Support](mailto:support@checklyhq.com) with the following information:

* Microsoft Entra ID Domain (e.g. company.com)
* [Client ID](https://auth0.com/docs/connections/enterprise/azure-active-directory)
* Client Secret

## Testing the SSO integration

After configuration has taken place on Checkly's side, you will receive confirmation via e-mail. Once that has happened, you should be able to log in to Checkly via SSO already. Entering an email address associated with the domain you have provided in the login prompt should result in the password field disappearing:

<img src="https://mintcdn.com/checkly-422f444a/y0uv0mm_P84z_Jj5/images/docs/images/single-sign-on/checkly-login-prompt-sso.png?fit=max&auto=format&n=y0uv0mm_P84z_Jj5&q=85&s=ac9c563f8212c1b3e1e26a8044319b3d" alt="checkly login prompt without password screenshot" width="745" height="600" data-path="images/docs/images/single-sign-on/checkly-login-prompt-sso.png" />

After submitting the Checkly login form, you should be redirected to your SSO login interface. Completing the login procedure will then lead you to your existing Checkly account, if you have one, or to the new account creation screen, in case you don't.

<Info>
  Once Microsoft Entra ID has been set up, you will still need to invite new users from your organization to your Checkly account, as they will not be added automatically.
</Info>


Built with [Mintlify](https://mintlify.com).