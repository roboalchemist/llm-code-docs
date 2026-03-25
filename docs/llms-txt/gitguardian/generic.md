# Source: https://docs.gitguardian.com/platform/enterprise-administration/sso-providers/generic.md

# Generic SAML2 IdP

> Configure SAML-based Single Sign-On (SSO) with any SAML2-enabled identity provider for GitGuardian.

For SAML2-enabled Identity Providers not listed in our specific guides, follow this generic procedure.

## 1. Register GitGuardian on your Identity provider

In order to integrate GitGuardian with your Identity Provider, you must first register GitGuardian (Service Provider) as an application on the IdP's side. Follow these steps carefully:

1. Navigate to Settings > [Authentication](https://dashboard.gitguardian.com/settings/workspace/auth)
2. Click on "Configure"

![SSO Service provider info configure](/img/platform/enterprise-administration/sso_sp_info_configure.png)

3. On your IdP:
   1. Fill in the SAML endpoint provided by GitGuardian (ACS url, SP Entity id)
   2. Fill in Email or EmailAddress as the primary identifier (Name ID format).
      Refer to our [FAQ](../saml-sso-configuration#faq) if this Name ID format is not available in your IdP.
   3. Set RSA_SHA256 for the signature algorithm, and SHA256 for the digest algorithm for your response.
      Some Identity Providers (IdPs) may require you to sign either the response message or the response assertions. GitGuardian provides the ability to specify this IdP behavior. Note that at least one of these, either the response message or the response assertions, must be signed.
   4. Configure `first_name` and `last_name` mapped attributes.

![SSO Service provider info](/img/platform/enterprise-administration/sso_sp_info.png)

## 2. Register your IdP on GitGuardian's side

Once GitGuardian is registered as an application on your IdP's side, you need to provide your IdP metadata fields on GitGuardian (Service Provider side) in order to complete the integration:

1. While still on the [Authentication config page](https://dashboard.gitguardian.com/settings/workspace/auth/saml/setup) of your workspace settings, complete the form with:
   - Entity Id [required]
   - Single Sign On Url [required]
   - Single Log Out Url [optional]
   - X509 certificate [required]
   - Ensure that the checkbox **I have mapped the attributes first_name and last_name in my IdP** is checked
2. Submit the form to fully register the SAML integration.
   ![SSO IdP info](/img/platform/enterprise-administration/sso_idp_info.png)
3. The setup is complete. Your workspace will have **a dedicated SSO login url for your collaborators to sign in using your IdP**.
   ![SSO login url](/img/platform/enterprise-administration/sso_login_url.png)

> You can register this SSO login url on the IdP side to enable the SSO flow with one click directly in the IdP interface. However this IdP-Initiated flow carries a security risk and is therefore NOT recommended. Make sure you understand the risks before enabling IdP-initiated SSO.

:::info Next Step
Don't forget to complete the [Email domain reservation](../saml-sso-configuration#email-domain-reservation) step to enable automatic SSO discovery and prevent workspace fragmentation.
:::
