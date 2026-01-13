# Source: https://docs.datadoghq.com/account_management/scim/entra.md

# Source: https://docs.datadoghq.com/account_management/saml/entra.md

---
title: Microsoft Entra ID SAML IdP
description: >-
  Configure Microsoft Entra ID as a SAML identity provider for Datadog single
  sign-on authentication.
breadcrumbs: >-
  Docs > Account Management > Single Sign On With SAML > Microsoft Entra ID SAML
  IdP
source_url: https://docs.datadoghq.com/saml/entra/index.html
---

# Microsoft Entra ID SAML IdP

## Setup{% #setup %}

Follow the [Microsoft Entra single sign-on (SSO) integration with Datadog](https://learn.microsoft.com/en-us/entra/identity/saas-apps/datadog-tutorial) tutorial to configure Entra ID as a SAML identity provider (IdP). **Note**: An Entra ID subscription is required. If you don't have a subscription, sign up for a [free account](https://azure.microsoft.com/free/).

### Datadog{% #datadog %}

1. Go to the [Datadog SAML page](https://app.datadoghq.com/saml/saml_setup).

1. Choose and upload the **SAML XML Metadata** file downloaded from Microsoft.

1. You should see the messages **SAML is ready** and **Valid IdP metadata installed**:

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/saml/SAML_Configuration___Datadog11.8b3c5a1c4b8c27d7a0c9d32f87de2160.png?auto=format"
      alt="SAML_Configuration___Datadog11" /%}

1. Click **Enable** to start using Entra ID single sign-on with SAML:

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/saml/SAML_Configuration___Datadog12.ceec013cb878938f961208c72ecab683.png?auto=format"
      alt="SAML_Configuration___Datadog12" /%}

### Advanced URL{% #advanced-url %}

If you are using SSO with a Datadog button or link, a sign-on URL is required:

1. Retrieve your Single Sign-on URL from the [Datadog SAML page](https://app.datadoghq.com/saml/saml_setup):

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/saml/SAML_Configuration___Datadog13.f30170a3c57c9033a1e8eea3eb62ce5a.png?auto=format"
      alt="SAML_Configuration___Datadog13" /%}

1. In Microsoft Entra ID, navigate to the SSO Configuration section of your application, check **Show advanced URL settings**, and add your single sign-on URL.

## Further Reading{% #further-reading %}

- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
- [Configuring Teams & Organizations with Multiple Accounts](https://docs.datadoghq.com/account_management/multi_organization/)
