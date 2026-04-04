# Source: https://docs.port.io/sso-rbac/sso-providers/oidc.md

# OIDC

This documentation describes the process of integrating an OIDC application with Port, along with some examples for specific identity providers. In order to integrate Port with an OIDC SSO application, you will need to do the following:

1. Create a new OIDC application in your identity provider and provide an app integration name, like `Port`.

2. Configure the application with the following details:

   <!-- -->

   * Redirect URI: `https://auth.getport.io/login/callback`

   * Login URI:

     <!-- -->

     Setting authorization endpoint based on account region

     Port exposes two API instances, one for the EU region of Port, and one for the US region of Port.<br /><!-- -->Use the correct endpoint based on your account region, and make sure to to replace `{CONNECTION_NAME}` with the value provided to you by Port.

     * EU
     * US

     ```
     https://auth.getport.io/authorize?response_type=token&client_id=96IeqL36Q0UIBxIfV1oqOkDWU6UslfDj&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.getport.io
     ```

     ```
     https://auth.us.getport.io/authorize?response_type=token&client_id=4lHUry3Gkds317lQ3JcgABh0JPbT3rWx&connection={CONNECTION_NAME}&redirect_uri=https%3A%2F%2Fapp.us.getport.io
     ```

     note

     We will provide your `{CONNECTION_NAME}` (Contact us using chat/Slack/mail to [support.port.io](http://support.port.io/)).

3. Expose the application to your organization by either granting access to everyone or restricting it to specific roles.

4. Share information about your SSO application:

   <!-- -->

   * Provide Port with the following details:

     <!-- -->

     * `Client ID`: The client identifier for your OIDC application.
     * `Client Secret`: The client secret for your OIDC application.

5. Add a custom property `email_verified` and configure the OpenID Claims in your identity provider to ensure that Port receives the value `true` for this attribute as part of the connection process. This step may be required specifically for certain identity providers such as [OneLogin](/sso-rbac/sso-providers/oidc/onelogin.md#step-4-add-email_verified-custom-property-to-all-users).

6. Configure the Groups claim in the OpenID Connect Token settings to enable automatic groups or roles support in Port.

   <br />

   <br />

   note

   This step is OPTIONAL and is required only if you wish to pull all of your groups or roles into Port inherently.

<br />

## [ðï¸<!-- --> <!-- -->Microsoft Entra ID (AzureAD)](/sso-rbac/sso-providers/oidc/azure-ad.md)

[Integrate AzureAD with Port using OIDC](/sso-rbac/sso-providers/oidc/azure-ad.md)

## [ðï¸<!-- --> <!-- -->Okta (OIDC)](/sso-rbac/sso-providers/oidc/okta.md)

[Integrate Okta with Port](/sso-rbac/sso-providers/oidc/okta.md)

## [ðï¸<!-- --> <!-- -->Onelogin](/sso-rbac/sso-providers/oidc/onelogin.md)

[Integrate Onelogin with Port](/sso-rbac/sso-providers/oidc/onelogin.md)
