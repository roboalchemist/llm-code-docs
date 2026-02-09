# Source: https://docs.datadoghq.com/account_management/saml/safenet.md

---
title: SafeNet SAML IdP
description: >-
  Configure SafeNet Trusted Access as a SAML identity provider for Datadog with
  metadata upload and two-factor authentication setup.
breadcrumbs: Docs > Account Management > Single Sign On With SAML > SafeNet SAML IdP
---

# SafeNet SAML IdP

## Setup{% #setup %}

Follow the [main SAML configuration instructions](https://docs.datadoghq.com/account_management/saml/#configure-saml), then see the [SafeNet Trusted Access for Datadog](https://resources.safenetid.com/help/Datadog/Index.htm) docs to configure SafeNet as your SAML IdP.

## Datadog{% #datadog %}

- The IdP metadata is available in the SafeNet Trusted Access console by clicking the **Download Metadata** button.
- In Datadog, ensure the **Identity Provider (IdP) Initiated Login** box is checked.
- Datadog's [Service Provider metadata](https://app.datadoghq.com/account/saml/metadata.xml) is needed.

## Verify authentication{% #verify-authentication %}

### Using STA console{% #using-sta-console %}

Navigate to the Datadog login URL. Once redirected to the SafeNet Trusted Access sign-in page, enter your primary directory login information and approve the two-factor authentication. This redirects you back to Datadog after authentication.

**Note**: For IdP initiated mode, enter the **Assertion Consumer Service URL** found in Datadog on the SafeNet Trusted Access console.

### Using STA user portal{% #using-sta-user-portal %}

Navigate to the User Portal URL to log in to the STA User Portal dashboard. The dashboard shows you a list of applications to which you have access. Click on the Datadog application icon, which redirects you to Datadog after authentication.

## Further Reading{% #further-reading %}

- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
