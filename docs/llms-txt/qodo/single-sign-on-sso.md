# Source: https://docs.qodo.ai/qodo-documentation/management-portal/single-sign-on-sso.md

# Single Sign-On (SSO)

{% hint style="info" %}
SSO is available on **Enterprise plans** and on **paid plans for an additional cost**. [Contact Qodo](https://www.qodo.ai/contact/) for more information
{% endhint %}

This guide explains how to configure Single Sign-On (SSO) for your Qodo organization. SSO allows team members to authenticate using your organization’s identity provider, enabling a secure and streamlined login experience.

### Prerequisites

Before configuring SSO, make sure you have:

* A Qodo user account with **admin privileges**
* An **Enterprise license** for Qodo
* **Administrator access** to your identity provider

{% hint style="warning" %}
Qodo supports service provider–initiated SSO only. Users must start authentication from the Qodo login page. Identity provider–initiated login (for example, starting login from your identity provider portal, such as clicking an Okta or Entra ID application tile) is not supported.
{% endhint %}

### Configuration&#x20;

#### Step 1: Access Organization Settings

1. Log in to your Qodo account with admin privileges
2. Navigate to the [**Users**](https://app.qodo.ai/account/users-management) page in the Qodo Admin Portal

#### Step 2: Initiate SSO Configuration

In the top right corener on the **Users** page:

1. Click on the **three dots menu** (...)
2. Select **Manage SSO**

<figure><img src="https://2742973941-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnoDWMoicsI0VwDtqoKja%2Fuploads%2FCfRCIiPidd0YIZOJICp9%2Fimage.png?alt=media&#x26;token=476edccf-9dab-40c4-ad70-f880e3628185" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The **Manage SSO** option is only visible to admins with an Enterprise license.
{% endhint %}

#### Step 3: Select your identity provider

Choose one of the supported identity providers:

<details>

<summary><strong>Supported Identity Providers</strong></summary>

* **ADP OpenID Connect** – Workforce identity and HR-integrated authentication
* **Auth0 SAML** – Flexible authentication and identity platform
* **CAS SAML** – Central Authentication Service for single sign-on
* **ClassLink SAML** – Education-focused SSO platform
* **Clever OpenID Connect** – Identity platform for education organizations
* **Cloudflare SAML** – Zero Trust access and identity integration
* **CyberArk SAML** – Privileged access and identity security
* **Duo SAML** – Multi-factor authentication and access security
* **Entra ID (Azure AD) OpenID Connect** – Microsoft identity platform using OIDC
* **Entra ID (Azure AD) SAML** – Microsoft’s cloud-based identity service
* **Google OpenID Connect** – Google Workspace authentication using OIDC
* **Google SAML** – Google Workspace SAML-based SSO
* **JumpCloud SAML** – Cloud directory and device management
* **Keycloak SAML** – Open-source identity and access management
* **LastPass SAML** – Identity and password management SSO
* **Login.gov OpenID Connect** – U.S. government identity provider
* **Microsoft AD FS** – On-premises Active Directory Federation Services
* **miniOrange SAML** – Identity and access management platform
* **NetIQ SAML** – Enterprise identity and access management
* **Okta OpenID Connect** – Okta authentication using OIDC
* **Okta SAML** – Enterprise identity and access management
* **OneLogin** – Cloud-based identity and access management
* **Oracle** – Oracle Identity and Access Management SSO
* **PingFederate** – Enterprise federation and SSO solution
* **PingOne** – Cloud identity platform by Ping Identity
* **Rippling** – Workforce management with integrated SSO
* **Salesforce** – CRM-based identity provider and SSO
* **Shibboleth** – Open-source federated identity solution
* **Shibboleth Generic SAML** – Generic SAML configuration for Shibboleth
* **SimpleSAMLphp SAML** – PHP-based SAML identity provider
* **VMware Workspace ONE** – Unified endpoint and identity management
* **Custom SAML** – Generic SAML 2.0 configuration for unsupported providers

</details>

<figure><img src="https://2742973941-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnoDWMoicsI0VwDtqoKja%2Fuploads%2FU0W0OrzmT0i4c6r9f1TX%2Fimage.png?alt=media&#x26;token=b7f49ce3-1e69-480c-a213-b2009a63a65f" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
Once SSO is configured for your organization, it is **enforced by default**. After enforcement, users must authenticate using the configured identity provider, and other authentication methods (such as Google sign-in) cannot be used in parallel.
{% endhint %}

#### Step 4: Provider-specific configuration

After selecting an identity provider, Qodo guides you through a configuration flow tailored to that provider.

### Example: Configuring Entra ID (Azure AD)

This section provides an example of connecting Qodo to Azure AD.\
Follow the **in-product instructions** for complete and up-to-date steps.

#### Create an enterprise application

{% hint style="danger" %}
**Required Access**: You must have administrator access to your Microsoft Entra admin center to complete these steps.&#x20;
{% endhint %}

<figure><img src="https://2742973941-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnoDWMoicsI0VwDtqoKja%2Fuploads%2F7zxGGgvbhktUnFNPWWzZ%2Fimage.png?alt=media&#x26;token=5b174fea-2b59-419a-a5eb-702afc80a276" alt=""><figcaption></figcaption></figure>

### Next Steps

After completing the provider-specific setup:

* **Test the connection** – Verify SSO using a test user
* **Assign users** – Add team members to the SSO application
* **Confirm enforcement** – SSO is automatically enforced and becomes the only supported authentication method for the organization

### Troubleshooting

If you encounter issue check the follwoing:

* Ensure all URLs are correctly configured in both Qodo and your identity provider
* Verify that user email addresses match between systems
* Check that the SAML response includes required attributes
* **“Wrong authentication method”** error when logging in via identity provider.

  Qodo does not support identity provider–initiated login. Logging in from an identity provider application tile (for example, an Okta tile) will fail. To resolve this, start login from the Qodo login page.

### Support

If your issue are persistent:

* Review the provider-specific documentation.
* Contact your identity provider's support team for provider-side issues.
* Reach out to Qodo support for application-specific questions.
