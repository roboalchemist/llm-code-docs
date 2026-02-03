# Source: https://docs.datadoghq.com/account_management/saml/google.md

---
title: Google SAML IdP
description: >-
  Configure Google as a SAML identity provider for Datadog with service provider
  details and attribute mapping for secure single sign-on.
breadcrumbs: Docs > Account Management > Single Sign On With SAML > Google SAML IdP
---

# Google SAML IdP

## Setting up Google as a SAML IdP{% #setting-up-google-as-a-saml-idp %}

[See the dedicated Google instructions](https://support.google.com/a/answer/7553768)

## Service provider details{% #service-provider-details %}

As a prerequisite, **IDP initiated SSO** must be checked on the Datadog [SAML configuration page](https://app.datadoghq.com/saml/saml_setup).

{% dl %}

{% dt %}
Application Name
{% /dt %}

{% dd %}
Can be anything
{% /dd %}

{% dt %}
Description
{% /dt %}

{% dd %}
Can be anything
{% /dd %}

{% dt %}
ACS URL
{% /dt %}

{% dd %}
Use the URL shown under **Assertion Consumer Service URL** on the [SAML setup page](https://app.datadoghq.com/saml/saml_setup) (the one containing `/id/`). If there is more than one value shown for Assertion Consumer Service URL, only enter one of them here.
{% /dd %}

{% dt %}
Entity ID
{% /dt %}

{% dd %}
Use the URL shown under **Entity ID** on the [SAML setup page](https://app.datadoghq.com/saml/saml_setup).
{% /dd %}

{% dt %}
Start URL
{% /dt %}

{% dd %}
Can be blank, or use the **Single Sign On Login URL** listed on the [SAML setup page](https://app.datadoghq.com/saml/saml_setup).
{% /dd %}

{% dt %}
Signed Response
{% /dt %}

{% dd %}
Leave Unchecked
{% /dd %}

{% dt %}
Name ID
{% /dt %}

{% dd %}
Select **Basic Information** and **Primary Email**
{% /dd %}

{% /dl %}

## Attribute mapping{% #attribute-mapping %}

- "urn:oid:1.3.6.1.4.1.5923.1.1.1.6" "Basic Information" "Primary Email"

Also add:

- "urn:oid:2.5.4.4" "Basic Information" "Last Name"
- "urn:oid:2.5.4.42" "Basic Information" "First Name"

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/zAttributeMapping.2ad6e7d91e429c691b44b06f1324f842.png?auto=format"
   alt="zAttributeMapping" /%}

## Further Reading{% #further-reading %}

- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
- [Configuring Teams & Organizations with Multiple Accounts](https://docs.datadoghq.com/account_management/multi_organization/)
