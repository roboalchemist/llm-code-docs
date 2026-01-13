# Source: https://docs.datadoghq.com/account_management/saml/mobile-idp-login.md

---
title: The Datadog Mobile App with IdP Initiated SAML
description: >-
  Use the Datadog mobile app with IdP-initiated SAML authentication by
  configuring relay states for OneLogin, Okta, and Google identity providers.
breadcrumbs: >-
  Docs > Account Management > Single Sign On With SAML > The Datadog Mobile App
  with IdP Initiated SAML
source_url: https://docs.datadoghq.com/saml/mobile-idp-login/index.html
---

# The Datadog Mobile App with IdP Initiated SAML

## Setup{% #setup %}

In order to use the Datadog mobile app with Identity Provider (IdP) Initiated SAML, you need to pass an additional Relay State through to Datadog to trigger the mobile app landing page on login. Once enabled, all sign ins from SAML for that particular app land on a the interstitial page before proceeding.

- On **mobile devices** with the Datadog mobile app installed, users should **first log in with their identity provider using their mobile browser** (see the example with Google, below). Then, the app automatically captures the request and allows the user to sign in.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/google_idp_tile_sml.3ced43e9480acf22d4ee2508d02ea812.png?auto=format"
   alt="Google IDP relay state" /%}

- On **Desktop devices** or devices where the app is not installed, the user needs to click "Use the Datadog Website" to proceed.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/datadog-mobile-idp-saml-landing-page.147299f3f7fa05bad20f5c4e3520cd6b.png?auto=format"
   alt="Datadog Mobile SAML Interstitial" /%}

## Providers{% #providers %}

**Note:** Datadog IdP Initiated SAML works with most identity providers. If you run into trouble while configuring your identity provider with the Datadog Mobile App, contact [Datadog support](https://docs.datadoghq.com/help/).

### OneLogin{% #onelogin %}

When configuring your OneLogin app, set the Relay State value on the **Application Details** page to `dd_m_idp`.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/one-login-mobile-idp-relay-state.1ab5734fe62525480f8fa929546922b0.png?auto=format"
   alt="One Login's Application Details Page" /%}



### Okta{% #okta %}

When configuring your Okta app, set the Default RelayState value on the **Configure SAML** page to `dd_m_idp`.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/okta-mobile-idp-relay-state.f7319ae4ae62cf2db62a6f25e56a16b9.png?auto=format"
   alt="Okta's Configure SAML page" /%}



### Google{% #google %}

When configuring your Google app for SAML, set the **Start URL** under the Service Provider Details to `dd_m_idp`.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/saml/google-mobile-idp-relay-state.9c193d24d7000fbfacf945a91a39236c.png?auto=format"
   alt="Google's Service Provider Details Page" /%}



## Troubleshooting{% #troubleshooting %}

If you see a `403 Forbidden` error on login after configuring the Relay State, contact [Support](https://docs.datadoghq.com/help/) to ensure that the feature has been enabled for your organization.
