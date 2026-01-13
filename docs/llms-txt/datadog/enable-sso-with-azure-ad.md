# Source: https://docs.datadoghq.com/cloudcraft/account-management/enable-sso-with-azure-ad.md

---
title: Enable SSO with Azure AD
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Account Management > Enable SSO with Azure AD
source_url: >-
  https://docs.datadoghq.com/account-management/enable-sso-with-azure-ad/index.html
---

# Enable SSO with Azure AD

Enabling Single Sign-On (SSO) with Azure AD as your identity provider allows you to simplify authentication and login access to Cloudcraft.

This article helps you set up SSO if your identity provider is Azure AD. For other identity providers, see the following articles:

- [Enable SSO With Okta](https://docs.datadoghq.com/cloudcraft/account-management/enable-sso-with-okta/)
- [Enable SSO With a Generic Identity Provider](https://docs.datadoghq.com/cloudcraft/account-management/enable-sso-with-generic-idp/)

For more general information on using SSO with Cloudcraft, check out [Enable SSO in Your Account](https://docs.datadoghq.com/cloudcraft/account-management/enable-sso/).

## Setting up SAML/SSO{% #setting-up-samlsso %}

{% alert level="info" %}
Only the account owner can configure the SAML SSO feature. If the account owner is unable to configure SSO, [contact the Cloudcraft support team](https://app.cloudcraft.co/app/support "Contact the Cloudcraft support team") to enable this feature.
{% /alert %}

1. In Cloudcraft, navigate to **User** > **Security & SSO**.
1. The details you need to create a new application with Azure can be found in the **Cloudcraft service provider details** section.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-azure-ad/service-provider-details.f325caeac04613338a635d602f26a32f.png?auto=format"
   alt="Screenshot of Cloudcraft service provider details for Identity Provider configuration with entity ID and assertion consumer service URL." /%}
Log in to Azure as an administrator.Click the hamburger menu on the upper-left corner of the screen and select **Azure Active Directory**.In the **Manage** section on the left menu, click **Enterprise applications**.Click **New application** and select **Non-gallery application**.Enter **Cloudcraft** as the name of the application, then click **Add**.
Next, configure the SAML integration using the details provided by Cloudcraft.

1. In the **Getting started** section, select **Set up single sign on**, then click **SAML**.
1. Under the **Basic SAML Configuration** section, click **Edit**.
1. Enter the details provided by Cloudcraft. The fields are mapped as follows, with the first value being the label in Azure AD, and the second being the label in the Cloudcraft dialog.
   - **Identifier**: Service Provider Entity ID
   - **Reply URL**: Assertion Consumer Service URL
   - **Sign on URL**: Leave this blank to allow identity provider-initiated SSO

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-azure-ad/saml-settings.dc8a7b4ada681424ad6fb99384c1dff2.png?auto=format"
   alt="Screenshot of the Basic SAML Configuration interface showing fields for Identifier (Entity ID) and Reply URL (Assertion Consumer Service URL)." /%}
Click **Save** to return to the previous screen.Under the **SAML Signing Certificate** section, select **Federation Metadata XML** and download the XML file to your computer.Navigate back to Cloudcraft and upload your metadata XML file.
{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-azure-ad/upload-metadata.96647bfb9a306bf7c0f15b0ccae08033.png?auto=format"
   alt="Successfully configured SAML Single Sign-On status with identity provider URL visible in security settings interface." /%}
Toggle the **SAML Single Sign-On is enabled** option.Navigate back to the Azure portal.Under the **Test single sign-on with Cloudcraft** section, click **Test** to test your integration.If you prefer to have your users access Cloudcraft only via Azure AD, enable the **Strict mode** option, which disables all other login methods.
**Note**: To grant access to users in your organization, see [the Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/assign-user-or-group-access-portal).
