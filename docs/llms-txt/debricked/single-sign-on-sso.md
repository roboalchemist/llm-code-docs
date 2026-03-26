# Source: https://docs.debricked.com/tools-and-integrations/single-sign-on-sso.md

# Single Sign-On (SSO)

{% hint style="info" %}
*This feature is currently only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *customers.*
{% endhint %}

This article details the general configuration with an Identity Provider to facilitate SSO with OpenText Core SCA. For details regarding integrations with specific providers, see:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="single-sign-on-sso/single-sign-on-sso-through-okta"><strong>Single Sign-On through Okta (OIDC)</strong></a></td><td></td><td></td><td><a href="single-sign-on-sso/single-sign-on-sso-through-okta">single-sign-on-sso-through-okta</a></td></tr><tr><td><a href="single-sign-on-sso/single-sign-on-sso-through-microsoft-entra-id"><strong>Single Sign-On through Microsoft Entra ID (OIDC)</strong></a></td><td></td><td></td><td><a href="single-sign-on-sso/single-sign-on-sso-through-microsoft-entra-id">single-sign-on-sso-through-microsoft-entra-id</a></td></tr><tr><td><a href="single-sign-on-sso/single-sign-on-sso-through-jumpcloud-oidc"><strong>Single Sign-On through JumpCloud OIDC</strong></a></td><td></td><td></td><td><a href="single-sign-on-sso/single-sign-on-sso-through-jumpcloud-oidc">single-sign-on-sso-through-jumpcloud-oidc</a></td></tr><tr><td><a href="single-sign-on-sso/single-sign-on-sso-through-github"><strong>Single Sign-On through GitHub (OIDC)</strong></a></td><td></td><td></td><td><a href="single-sign-on-sso/single-sign-on-sso-through-github">single-sign-on-sso-through-github</a></td></tr><tr><td><a href="single-sign-on-sso/single-sign-on-sso-through-okta-saml"><strong>Single Sign-On (SSO) through Okta (SAML)</strong></a></td><td></td><td></td><td></td></tr><tr><td><a href="single-sign-on-sso/single-sign-on-sso-through-onelogin-saml"><strong>Single Sign-On (SSO) through OneLogin (SAML)</strong></a></td><td></td><td></td><td></td></tr></tbody></table>

Integrating your Single Sign-On provider with OpenText Core SCA allows for a more streamlined user experience, simplifying user management and enhancing security. You can authenticate with your SSO provider to access the tool, eliminating the need to create and remember separate login credentials. This integration also helps to ensure that access to the OpenText Core SCA tool is only granted to authorized users, as authentication is handled by the SSO provider.

To be able to complete the integration, upgrade to the Enterprise tier and get in touch with OpenText Core SCA support team at [***support@debricked.com***](mailto:support@debricked.com)

### Set up SSO using Open ID Connect (OIDC) <a href="#setupssousing-openidconnect-oidc" id="setupssousing-openidconnect-oidc"></a>

Using OIDC requires an exchange of parameters between your company and OpenText Core SCA. To set up the integration at your Identity Provider, you need to enter the following parameters:

| Parameter                                    | Value                                        |
| -------------------------------------------- | -------------------------------------------- |
| Callback/Redirect URI                        | *<https://debricked.com/app/sso/oidc/auth>*  |
| Sign-out redirect URI                        | *<https://debricked.com/app/en/logout>*      |
| IdP Initiated URI (if supported by provider) | *<https://debricked.com/app/sso/oidc/login>* |
| OAuth Grant Type                             | *Authorization code*                         |

To complete the integration, enter the following information:

* **Issuer URL** (the URL used to fetch OIDC information)
* **Email Domains** (the email domains which will be designated to your organization)
* **Client ID** (identifier of the OpenText Core SCA integration)
* **Client secret** (secret to authorize the integration, also provided when installing the integration in your IdP)

You can forward it to us by either:

* Getting in touch with the support team at [***support@debricked.com***](mailto:support@debricked.com)
* Submitting the configuration data through an API endpoint at <https://debricked.com/api/1.0/open/sso/oidc/request>

### Set up SSO using Open ID Connect (SAML) <a href="#logintodebrickedusingsso" id="logintodebrickedusingsso"></a>

You can contact the OpenText Core SCA support team at [***support@debricked.com***](mailto:support@debricked.com) to request the metadata file for their employer or organization. This metadata file typically includes the following parameters:

| Parameter                                                                   | Value                                                                                                                       |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Entity ID/Audience                                                          | *<https://debricked.com/app/sso/saml/metadata/{Employer\\_id}>* (Refer to the Core SCA's metadata file for the employer ID) |
| <p>Single Sign-On URL (AssertionConsumerServi</p><p>ce(ACS)</p><p>URL) </p> | <p><em><https://debricked.com/app/sso/saml/acs></em>                                                                        |

<br></p>                                                             |
\| <p>SLS (Single Logout</p><p>Service) URL</p>                                | \_<https://debricked.com/app/sso/saml/logout_&#xD;&#xD>;                                                                    |

To complete the integration, enter the following information:

* **Metadata File of the IDP** (The metadata file that contains the Identity Provider (IDP) configuration)
* **Email Domains** (The email domains which is designated to your organization)
* [**Name of Attributes** ](#user-content-fn-1)[^1]\(mapped to below IDP fields)
* **Email** (default value is email)
* **First Name** (default value is fname)
* **Last Name** (default value is lname)

You can send us the configuration using either of the following methods:

* **Contact our support team:** Email your details to [*support@debricked.com*](mailto:support@debricked.com)
* **Submit the configuration through our API:** Use the endpoint *<https://debricked.com/api/1.0/open/sso/saml/submit-saml-configuration>*

### Log in to OpenText Core SCA using SSO <a href="#logintodebrickedusingsso" id="logintodebrickedusingsso"></a>

1. Once the integration is completed, you can log into Debricked by clicking **Login with company SSO** on the [login page](https://debricked.com/app/en/login).
2. In the next step, type your email address, and complete the authentication with your SSO provider.

[^1]:
