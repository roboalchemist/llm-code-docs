# Source: https://docs.datadoghq.com/account_management/scim.md

---
title: User Provisioning with SCIM
description: >-
  Automate user provisioning and deprovisioning in Datadog using SCIM
  integration with Microsoft Entra ID and Okta identity providers.
breadcrumbs: Docs > Account Management > User Provisioning with SCIM
source_url: https://docs.datadoghq.com/scim/index.html
---

# User Provisioning with SCIM

{% alert level="info" %}
SCIM is available with the Infrastructure Pro and Infrastructure Enterprise plans.
{% /alert %}

## Overview{% #overview %}

The System for Cross-domain Identity Management, or [SCIM](https://scim.cloud/), is an open standard that allows for the automation of user provisioning. Using SCIM, you can automatically provision and deprovision users in your Datadog organization in-sync with your organization's identity provider (IdP).

### Supported capabilities{% #supported-capabilities %}

- Create users in Datadog (Email verification is required for first login, see [email verification](https://docs.datadoghq.com/account_management/scim/#email-verification))
- Remove users in Datadog when they no longer require access
- Keep user attributes synchronized between the identity provider and Datadog
- Single sign-on to Datadog (recommended)
- Managed Teams: Create Datadog Teams from identity provider groups and keep membership of the Datadog Teams synchronized with group membership in the identity provider.

Datadog implements the SCIM server protocol. Datadog supports using SCIM with the Microsoft Entra ID and Okta identity providers. Other identity providers may work, but are not explicitly supported.

To configure SCIM for supported identity providers, see the documentation for your IdP:

- [Microsoft Entra ID](https://docs.datadoghq.com/account_management/scim/azure)
- [Okta](https://docs.datadoghq.com/account_management/scim/okta)

### Prerequisites{% #prerequisites %}

SCIM in Datadog is an advanced feature included in the Infrastructure Pro and Infrastructure Enterprise plans.

This documentation assumes your organization manages user identities using an identity provider.

Datadog strongly recommends that you use a service account application key when configuring SCIM to avoid any disruption in access. For further details, see [using a service account with SCIM](https://docs.datadoghq.com/account_management/scim/#using-a-service-account-with-scim).

When using SAML and SCIM together, Datadog strongly recommends disabling SAML just-in-time (JIT) provisioning to avoid discrepancies in access. Manage user provisioning through SCIM only.

## Using a service account with SCIM{% #using-a-service-account-with-scim %}

To enable SCIM, you must use an [application key](https://docs.datadoghq.com/account_management/api-app-keys) to secure the connection between your identity provider and your Datadog account. A specific user or service account controls each application key.

If you use an application key tied to a user to enable SCIM and that user leaves your organization, their Datadog account becomes deprovisioned. That user-specific application key gets revoked, and you permanently break your SCIM integration, preventing users in your organization from accessing Datadog.

To avoid losing access to your data, Datadog strongly recommends that you create a [service account](https://docs.datadoghq.com/account_management/org_settings/service_accounts) dedicated to SCIM. Within that service account, create an application key to use in the SCIM integration.

## Further Reading{% #further-reading %}

- [Configure SCIM with Azure Active Directory](https://docs.datadoghq.com/account_management/scim/azure/)
- [Configure SCIM with Okta](https://docs.datadoghq.com/account_management/scim/okta)
