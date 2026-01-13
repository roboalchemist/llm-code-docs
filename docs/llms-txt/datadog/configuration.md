# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/configuration.md

# Source: https://docs.datadoghq.com/containers/kubernetes/configuration.md

# Source: https://docs.datadoghq.com/containers/datadog_operator/configuration.md

# Source: https://docs.datadoghq.com/agent/configuration.md

# Source: https://docs.datadoghq.com/account_management/saml/configuration.md

---
title: Configuring Single Sign-On With SAML
description: >-
  Configure SAML authentication for Datadog with identity providers like Active
  Directory, Auth0, Google, Okta, and Microsoft Entra ID for secure single
  sign-on.
breadcrumbs: >-
  Docs > Account Management > Single Sign On With SAML > Configuring Single
  Sign-On With SAML
source_url: https://docs.datadoghq.com/saml/configuration/index.html
---

# Configuring Single Sign-On With SAML

## Overview{% #overview %}

This page covers how to enable single sign-on (SSO) with SAML in Datadog, as well as how enterprise customers can enable multiple SAML identity providers (IdPs).

**Notes**:

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com

- If you don't have SAML enabled on your Datadog account, reach out to [support](https://docs.datadoghq.com/help/) to enable it.
- This documentation assumes that you already have a SAML Identity Provider (IdP). If you do not have a SAML IdP, there are several IdPs that have integrations with Datadog such as [Active Directory](https://docs.datadoghq.com/account_management/saml/activedirectory/), [Auth0](https://auth0.com/docs/protocols/saml-protocol), [Google](https://cloud.google.com/architecture/identity/single-sign-on), [LastPass](https://support.logmeininc.com/lastpass/help/lastpass-admin-toolkit-using-single-sign-on-sso), [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/architecture/auth-saml), [Okta](https://developer.okta.com/docs/concepts/saml/), and [SafeNet](https://thalesdocs.com/sta/operator/applications/apps_saml/index.html).
- SAML configuration requires [Datadog Administrator](https://docs.datadoghq.com/account_management/users/default_roles/) access, or the `Org Management` permission if you're using custom roles.

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

- This documentation assumes that you already have a SAML Identity Provider (IdP). If you do not have a SAML IdP, there are several IdPs that have integrations with Datadog such as [Active Directory](https://docs.datadoghq.com/account_management/saml/activedirectory/), [Auth0](https://auth0.com/docs/protocols/saml-protocol), [Google](https://cloud.google.com/architecture/identity/single-sign-on), [LastPass](https://support.logmeininc.com/lastpass/help/lastpass-admin-toolkit-using-single-sign-on-sso), [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/architecture/auth-saml), [Okta](https://developer.okta.com/docs/concepts/saml/), and [SafeNet](https://thalesdocs.com/sta/operator/applications/apps_saml/index.html).
- SAML configuration requires [Datadog Administrator](https://docs.datadoghq.com/account_management/users/default_roles/) access, or the `Org Management` permission if you're using custom roles.

{% /callout %}

## Configuring SAML{% #configuring-saml %}

1. To begin configuration, see your IdP's documentation:

   - [Active Directory](https://docs.datadoghq.com/account_management/saml/activedirectory/)
   - [Auth0](https://docs.datadoghq.com/account_management/saml/auth0/)
   - [Google](https://docs.datadoghq.com/account_management/saml/google/)
   - [Microsoft Entra ID](https://docs.datadoghq.com/account_management/saml/entra/)
   - [LastPass](https://docs.datadoghq.com/account_management/saml/lastpass/)
   - [Okta](https://docs.datadoghq.com/account_management/saml/okta/)
   - [SafeNet](https://docs.datadoghq.com/account_management/saml/safenet/)

1. Download Datadog's [Service Provider metadata](https://app.datadoghq.com/account/saml/metadata.xml) to configure your IdP to recognize Datadog as a Service Provider.

1. In Datadog, hover over your username in the bottom left corner and select **Organization Settings**. Select [**Login Methods**](https://docs.datadoghq.com/account_management/login_methods/) and click **Configure** under SAML.

1. Click **Add SAML**.

1. In the configuration modal:

   - Create a user-friendly name for this SAML provider. The name appears to end users when they choose a login method.
   - Upload the IdP metadata from your SAML identity provider by clicking **browse files** or dragging and dropping the XML metadata file onto the modal.Important alert (level: info): The IdP metadata must contain ASCII characters only.

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/saml/saml_configure.25139ec5677b6dae6047fabe1dad6d54.png?auto=format"
      alt="Configure SAML by uploading your IdP metadata" /%}

1. Click **Save**.

**Note**: To configure SAML for a multi-org, see [Managing Multiple-Organization Accounts](https://docs.datadoghq.com/account_management/multi_organization/#setting-up-saml).

## Configuring multiple SAML providers{% #configuring-multiple-saml-providers %}

Enterprise customers can have multiple SAML configurations per organization (up to three at the same time). This feature simplifies identity management across complex environments, such as during IdP changes, mergers, or contractor onboarding.

To configure additional SAML providers:

1. Navigate to **Organization Settings > Login Methods**. Under **SAML**, click **Update**, then **Add SAML**.

1. In the configuration modal:

   - Create a user-friendly name for this SAML provider. The name appears to end users when they choose a login method.Important alert (level: info): All users can see and access all configured IdPs; there is no way to assign specific user groups to specific configurations. Setting clear and descriptive names for each provider helps users select the appropriate IdP during login. Also note that there is no way to set a default configuration.
   - Upload the IdP metadata from your SAML identity provider by clicking **browse files** or dragging and dropping the XML metadata file onto the modal.

1. Click **Save**.

### Role mapping with multiple SAML providers{% #role-mapping-with-multiple-saml-providers %}

If you use SAML [role mapping](https://docs.datadoghq.com/account_management/saml/mapping/#map-saml-attributes-to-datadog-roles) or [team mapping](https://docs.datadoghq.com/account_management/saml/mapping/#map-saml-attributes-to-teams) and want to use the same mappings in any additional providers you add, make sure the attributes in the new IdP(s) match what is defined in your mappings. If you add a new IdP, make sure to either use the same attribute names as your existing IdP, or add new mappings that align with the new IdP's attributes to ensure roles and teams are assigned correctly when users log in with different IdPs.
