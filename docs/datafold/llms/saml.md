# Source: https://docs.datafold.com/security/single-sign-on/saml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SAML

> SAML (Security Assertion Markup Language) is a protocol that enables secure user authentication by integrating Identity Providers (IdPs) with Service Providers (SPs).

<Info>
  **NOTE**

  SAML SSO is available for both SaaS and VPC installations of Datafold.
</Info>

In this case, Datafold is the service provider. The Identity Providers can be anything used by the organization (e.g., Google, Okta, Duo).

We also support SAML SSO [group provisioning](/security/single-sign-on/saml/group-provisioning).

## Generic SAML Identity Providers

<Tip>
  **TIP**

  We also provide SAML identity providers configurations for ([Okta](/security/single-sign-on/saml/examples/okta), [Microsoft Entra ID](/security/single-sign-on/saml/examples/microsoft-entra-id-configuration), and [Google](/security/single-sign-on/saml/examples/google))
</Tip>

To configure a SAML provider:

1. Go to `Datafold`. Create a new integration by navigating to **Settings** → **Integrations** → **SSO** → **Add new integration** → **SAML**.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d664571269b205f66ed0bfb051107a91" data-og-width="2088" width="2088" data-og-height="1452" height="1452" data-path="images/saml_create-3716c6fe01352ea69c647a7856adf189.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=76044b6a16ff8722c525b333d51fbd12 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa234c47b6a466e6cba5e6ab39b26651 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1a6dc91b3981557cbe15b08e888a42aa 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=93bfe67c8679b40af1d1f92daac66ad2 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=642e67455b35e8e364736f993039efbf 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_create-3716c6fe01352ea69c647a7856adf189.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=242b9f474139a637af404a556c3746f2 2500w" />
</Frame>

1. Go to the organization's `Identity Provider`, create a **SAML application** (sometimes called a **single sign-on** or **SSO** method).

If you have the option, enable the SAML Response signature and set it to **whole-response signing**.

1. Copy and paste the Service Provider URLs from the `Datafold` SAML Integration into the `Identity Provider`'s application setup. The only two mandatory fields are **Service Provider Entity ID** and the **Service Provider ACS URL**.

After creation, The `Identity Provider` will show you the metadata XML. It may be presented as raw XML, a URL to the XML, or an XML file to download.

<Info>
  **INFO**

  The Identity Providers sometimes provide additional parameters, such as SSO URLs, ACS URLs, SLO URLs, etc. We gather this information from the XML directly so these can be safely ignored.
</Info>

1. Paste either the **metadata XML** *or* **metadata URL** from your `Identity Provider` into the respective `Datafold` SAML integration fields.
2. Finally, click the **Save** button to create the integration.

After creation, the SAML login button will be available for Datafold users in your organization.

1. In your `Identity Provider`, activate the SAML application for all users or for select groups.

<Warning>
  **CAUTION**

  Only configured users in your identity provider will be able to login into Datafold *using* SAML SSO.
</Warning>

### Auto-create users in Datafold

Go to `Datafold` and navigate to **Settings** → **Integrations** → **SSO** → **SAML**.

Enable the **Allow SAML to auto-create users in Organization** switch and save the integration.

<Tabs>
  <Tab title="SaaS">
    If the **Allow SAML to auto-create users in Organization** switch from the SAML Integration in Datafold is enabled, identity provider-initiated logins will automatically create users in Datafold for authenticated users.
  </Tab>

  <Tab title="Dedicated cloud installations of Datafold">
    If the **Allow SAML to auto-create users in Organization** switch from the SAML Integration in Datafold is enabled, the SAML login button will always be enabled, and all authenticated users will be automatically created in Datafold.
  </Tab>
</Tabs>
