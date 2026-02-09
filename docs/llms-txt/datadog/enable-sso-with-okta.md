# Source: https://docs.datadoghq.com/cloudcraft/account-management/enable-sso-with-okta.md

---
title: Enable SSO with Okta
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > Account Management > Enable SSO with Okta
---

# Enable SSO with Okta

Enabling Single Sign-On (SSO) with Okta as your identity provider allows you to simplify authentication and login access to Cloudcraft.

This article helps you set up SSO if your identity provider is Okta. For other identity providers, see the following articles:

- [Enable SSO With Azure AD](https://docs.datadoghq.com/cloudcraft/account-management/enable-sso-with-azure-ad/)
- [Enable SSO With a Generic Identity Provider](https://docs.datadoghq.com/cloudcraft/account-management/enable-sso-with-generic-idp/)

For general information on using SSO with Cloudcraft, check out [Enable SSO in Your Account](https://docs.datadoghq.com/cloudcraft/account-management/enable-sso/).

## Setting Up SAML/SSO{% #setting-up-samlsso %}

{% alert level="info" %}
Only the account owner can configure the SAML SSO feature. If the account owner is unable to configure SSO, [contact the Cloudcraft support team](https://app.cloudcraft.co/app/support "Contact the Cloudcraft support team") to enable this feature.
{% /alert %}

1. In Cloudcraft, navigate to **User** > **Security & SSO**.
1. The details you need to create a new application with Okta can be found in the **Cloudcraft service provider details** section.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-okta/service-provider-details.f325caeac04613338a635d602f26a32f.png?auto=format"
   alt="Screenshot of Cloudcraft service provider details for Identity Provider configuration with entity ID and assertion consumer service URL." /%}
Log in to Okta as an administrator.Click **Application**.Click **Add Application**, then click **Create New App**.Select **SAML 2.0** as the sign on method and click **Create**.Enter **Cloudcraft** as the name of the application and leave the remaining values as-is.Click **Next**.
{% alert level="info" %}
If you prefer to use an app logo, you can use this logo which adheres to Okta's size restrictions.
{% /alert %}
Next, configure the SAML integration using the details provided by Cloudcraft. The fields are mapped as follows, with the first one being the label in Okta, and the second one being the label at Cloudcraft.
- **Single sign on URL**: Assertion Consumer Service URL
- **Audience URI**: Service Provider Entity ID

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-okta/saml-settings.be30791f58b0c4fe839d4622213d8dbc.png?auto=format"
   alt="Screenshot of SAML settings interface with fields for single sign-on URL and entity ID configuration." /%}
On the **Name ID format** dropdown, select **EmailAddress**.Proceed to the next screen and select **I'm an Okta customer adding an internal app** to answer the question "Are you a customer or partner?".Click **Finish**. Now that the application is set up in Okta, you can assign your users to it and once you're done, navigate to the **Sign On** tab.
{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-okta/sign-on-settings.0c31ba1e592c0f28dd045650a4e68de4.png?auto=format"
   alt="Screenshot displaying SAML 2.0 configuration settings in a Okta application integration interface." /%}
Under the **View Setup Instructions** button, click the blue link to download the file required for upload to Cloudcraft.Navigate back to Cloudcraft and upload your config file.
{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/account-management/enable-sso-with-okta/upload-metadata.ac805362516cf79e21546b9ade304133.png?auto=format"
   alt="Successfully configured SAML Single Sign-On status with identity provider URL visible in security settings interface." /%}
Toggle the **SAML Single Sign-On is enabled** option.If you prefer to have your users access Cloudcraft only via your identity provider, enable the **Strict mode** option.