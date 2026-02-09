# Source: https://www.activepieces.com/docs/admin-guide/guides/sso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Setup SSO

> Configure Single Sign-On (SSO) to enable secure, centralized authentication for your Activepieces platform

<Snippet file="enterprise-feature.mdx" />

## Overview

Single Sign-On (SSO) allows your team to authenticate using your organization's existing identity provider, eliminating the need for separate Activepieces credentials. This improves security, simplifies user management, and provides a seamless login experience.

## Prerequisites

Before configuring SSO, ensure you have:

* **Admin access** to your Activepieces platform
* **Admin access** to your identity provider (Google, GitHub, Okta, or JumpCloud)
* The **redirect URL** from your Activepieces SSO configuration screen

## Accessing SSO Configuration

Navigate to **Platform Settings** → **SSO** in your Activepieces admin dashboard to access the SSO configuration screen.

<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=88efce2224ae9782860510b0d36a6731" alt="SSO Configuration" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=a38c145973065c56c28f42d2e63a3445 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4e38e550658c3898ecfc94ec66ed6a4f 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=34f845669f80333ad85a97691e91627e 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c2c0dccb12d88efa1e22802a8a57e65e 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=1d1c7e68e1cbbf89837ab8d385ef7d0a 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/sso.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c4cd4418c83c077bfebbd6d74509d52e 2500w" />

## Enforcing SSO

You can enforce SSO by specifying your organization's email domain. When SSO enforcement is enabled:

* Users with matching email domains must authenticate through the SSO provider
* Email/password login can be disabled for enhanced security
* All authentication is routed through your designated identity provider

<Tip>
  We recommend testing SSO with a small group of users before enforcing it organization-wide.
</Tip>

## Supported SSO Providers

Activepieces supports multiple SSO providers to integrate with your existing identity management system.

### Google

<Steps>
  <Step title="Access Google Cloud Console">
    Go to the [Google Cloud Console](https://console.cloud.google.com/) and select your project (or create a new one).
  </Step>

  <Step title="Create OAuth2 Credentials">
    Navigate to **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**.

    Select **Web application** as the application type.
  </Step>

  <Step title="Configure Redirect URI">
    Copy the **Redirect URL** from the Activepieces SSO configuration screen and add it to the **Authorized redirect URIs** in Google Cloud Console.
  </Step>

  <Step title="Copy Credentials to Activepieces">
    Copy the **Client ID** and **Client Secret** from Google and paste them into the corresponding fields in Activepieces.
  </Step>

  <Step title="Save Configuration">
    Click **Finish** to complete the setup.
  </Step>
</Steps>

### GitHub

<Steps>
  <Step title="Access GitHub Developer Settings">
    Go to [GitHub Developer Settings](https://github.com/settings/developers) → **OAuth Apps** → **New OAuth App**.
  </Step>

  <Step title="Register New Application">
    Fill in the application details:

    * **Application name**: Choose a recognizable name (e.g., "Activepieces SSO")
    * **Homepage URL**: Enter your Activepieces instance URL
  </Step>

  <Step title="Configure Authorization Callback">
    Copy the **Redirect URL** from the Activepieces SSO configuration screen and paste it into the **Authorization callback URL** field.
  </Step>

  <Step title="Complete Registration">
    Click **Register application** to create the OAuth App.
  </Step>

  <Step title="Generate Client Secret">
    After registration, click **Generate a new client secret** and copy it immediately (it won't be shown again).
  </Step>

  <Step title="Copy Credentials to Activepieces">
    Copy the **Client ID** and **Client Secret** and paste them into the corresponding fields in Activepieces.
  </Step>

  <Step title="Save Configuration">
    Click **Finish** to complete the setup.
  </Step>
</Steps>

### SAML with Okta

<Steps>
  <Step title="Create New Application in Okta">
    Go to the [Okta Admin Portal](https://login.okta.com/) → **Applications** → **Create App Integration**.
  </Step>

  <Step title="Select SAML 2.0">
    Choose **SAML 2.0** as the sign-on method and click **Next**.
  </Step>

  <Step title="Configure General Settings">
    Enter an **App name** (e.g., "Activepieces") and optionally upload a logo. Click **Next**.
  </Step>

  <Step title="Configure SAML Settings">
    * **Single sign-on URL**: Copy the SSO URL from the Activepieces configuration screen
    * **Audience URI (SP Entity ID)**: Enter `Activepieces`
    * **Name ID format**: Select `EmailAddress`
  </Step>

  <Step title="Add Attribute Statements">
    Add the following attribute mappings:

    | Name        | Value            |
    | ----------- | ---------------- |
    | `firstName` | `user.firstName` |
    | `lastName`  | `user.lastName`  |
    | `email`     | `user.email`     |
  </Step>

  <Step title="Complete Setup in Okta">
    Click **Next**, select the appropriate feedback option, and click **Finish**.
  </Step>

  <Step title="Export IdP Metadata">
    Go to the **Sign On** tab → **View SAML setup instructions** or **View IdP metadata**. Copy the Identity Provider metadata XML.
  </Step>

  <Step title="Configure Activepieces">
    * Paste the **IdP Metadata** XML into the corresponding field
    * Copy the **X.509 Certificate** from Okta and paste it into the **Signing Key** field
  </Step>

  <Step title="Save Configuration">
    Click **Save** to complete the setup.
  </Step>
</Steps>

### SAML with JumpCloud

<Steps>
  <Step title="Create New Application in JumpCloud">
    Go to the [JumpCloud Admin Portal](https://console.jumpcloud.com/) → **SSO Applications** → **Add New Application** → **Custom SAML App**.
  </Step>

  <Step title="Configure ACS URL">
    Copy the **ACS URL** from the Activepieces configuration screen and paste it into the **ACS URLs** field in JumpCloud.

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=850741fb9a122b3aa3be92a9c0f16475" alt="JumpCloud ACS URL" data-og-width="608" width="608" data-og-height="263" height="263" data-path="resources/screenshots/jumpcloud/acl-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=3853f391837d583661225db8f226b3f1 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=81d7c6a37747342a86ff538e942292c9 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=1c90bd2bb6b68e5aecf89e96a648cb7d 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=ee8dcef0a30b25b2f1eac260a3bee5b3 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c915a17d22af793c139f351fbe90f540 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/acl-url.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=21d5aae4e46ebd6cfc5611b4d5d30c88 2500w" />
  </Step>

  <Step title="Configure SP Entity ID">
    Set the **SP Entity ID** (Audience URI) to `Activepieces`.
  </Step>

  <Step title="Add User Attributes">
    Configure the following attribute mappings:

    | Service Provider Attribute | JumpCloud Attribute |
    | -------------------------- | ------------------- |
    | `firstName`                | `firstname`         |
    | `lastName`                 | `lastname`          |
    | `email`                    | `email`             |

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=7ca21b93a70e8b51d392ee06cc6c4d10" alt="JumpCloud User Attributes" data-og-width="599" width="599" data-og-height="368" height="368" data-path="resources/screenshots/jumpcloud/user-attribute.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=9b11f2c145711496b54bba4b9fde63ae 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=ff63eb52f002c277ac7cb88d5e94d659 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=91e139de60e280d8a039f606ba6124d3 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=b6d3556ce3be45b503a64cca40044159 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=13da01ba9e1f96077bef81a43af97664 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-attribute.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=51b3448b758b1e2c90f09646421b87a0 2500w" />
  </Step>

  <Step title="Enable HTTP-Redirect Binding">
    JumpCloud does not include the `HTTP-Redirect` binding by default. You **must** enable this option.

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=8f2daa949a616e4dc98840b7623f00cb" alt="JumpCloud Redirect Binding" data-og-width="597" width="597" data-og-height="243" height="243" data-path="resources/screenshots/jumpcloud/declare-login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=6a1258dcd3e477a8c288803268ace908 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=eddb8daeceb8e64bcb9b3b1ba5ef6c5c 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=12cf214c9df97d556702b1648866622b 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=28ad042e17f5cd91ba04d6b55c54a041 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4510c8a59e1325b04adabe54b2ab2591 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/declare-login.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=5d1e72816ff38b9a77ed29991bf25a57 2500w" />

    <Warning>
      Without HTTP-Redirect binding, the SSO integration will not work correctly.
    </Warning>
  </Step>

  <Step title="Export Metadata">
    Click **Save**, then refresh the page and click **Export Metadata**.

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=9945a82f3b87881deea9dce937968f01" alt="JumpCloud Export Metadata" data-og-width="618" width="618" data-og-height="250" height="250" data-path="resources/screenshots/jumpcloud/export-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=af07b07a7200e82ece93ecc326eb838b 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=87c4d3da4daa9eca3f404ef745e3e299 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=e5ff802c679064d7f1cae8fda6c9e0c0 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=dc25d06fa8a4ec40fe7982e3064d23b7 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4e9485a404ff10c39c1e2470ccfdb883 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/export-metadata.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=b2541f12de981d893e8ea7810ab64dc4 2500w" />

    <Tip>
      Verify that the exported XML contains `Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"` to ensure the binding was properly enabled.
    </Tip>
  </Step>

  <Step title="Configure IdP Metadata in Activepieces">
    Paste the exported metadata XML into the **IdP Metadata** field in Activepieces.
  </Step>

  <Step title="Configure Signing Certificate">
    Locate the `<ds:X509Certificate>` element in the IdP metadata and extract its value. Format it as a PEM certificate:

    ```
    -----BEGIN CERTIFICATE-----
    [PASTE THE CERTIFICATE VALUE HERE]
    -----END CERTIFICATE-----
    ```

    Paste this into the **Signing Key** field.
  </Step>

  <Step title="Assign Users to Application">
    In JumpCloud, assign the application to the appropriate users or user groups.

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=43f7dcb66b7aaeec59a070053fdaf8e7" alt="JumpCloud Assign App" data-og-width="939" width="939" data-og-height="526" height="526" data-path="resources/screenshots/jumpcloud/user-groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=7b7b4b3296cd07f76c8f69b9da045bc1 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=0b376ea0d43933706c35a72c6f21fb03 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=9213f2a911863937ca2e6c2b0b87bd08 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=5ff48a56fc716cce3de983c6049947ff 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4679139dce30955c6a8896b8e4d652ef 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/jumpcloud/user-groups.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=5a829b002dfb0106cf16945b7381cba4 2500w" />
  </Step>

  <Step title="Save Configuration">
    Click **Finish** to complete the setup.
  </Step>
</Steps>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Users cannot log in after SSO configuration">
    * Verify the redirect URL is correctly configured in your identity provider
    * Ensure users are assigned to the application in your identity provider
    * Check that email domains match the SSO enforcement settings
  </Accordion>

  <Accordion title="SAML authentication fails">
    * Confirm the IdP metadata is complete and correctly formatted
    * Verify the signing certificate is properly formatted with BEGIN/END markers
    * Ensure all required attributes (firstName, lastName, email) are mapped
  </Accordion>

  <Accordion title="HTTP-Redirect binding error (JumpCloud)">
    * Enable the HTTP-Redirect binding option in JumpCloud
    * Re-export the metadata after enabling the binding
    * Verify the binding appears in the exported XML
  </Accordion>
</AccordionGroup>

## Need Help?

If you encounter issues during SSO setup, please contact our enterprise support or [sales team](https://www.activepieces.com/sales).
