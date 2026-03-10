# Source: https://render.com/docs/okta.md

# Enabling Okta SSO and SCIM — Connect Okta to your Render Enterprise organization.


> *These instructions are specific to Okta.*
>
> If you're using a different identity provider, see the primary article on [SAML SSO](saml-sso).

## Prerequisites

Enabling Okta SSO and SCIM requires a Render [Enterprise org](enterprise-orgs).

## Supported features

Enabling [Okta SSO](#sso) for your Render Enterprise org provides the following features:

- Okta-initiated SSO
- Render-initiated SSO
- Just-in-time provisioning of org members with first-time login

Enabling [Okta SCIM](#scim) provides the following additional features:

- Provisioning and deprovisioning org members from Okta

## Configuration steps

> *Before completing these steps, make sure you've [verified ownership](saml-sso#1-verify-domain-ownership) of your organization's domains.*

### SSO

1. From your org's Settings page in the Render Dashboard, scroll down to *SAML SSO* and click *+ Configure connection*:

   [image: Configuring an SSO connection in the Render Dashboard]

   The following dialog appears:

   [image: Configuring an SSO connection in the Render Dashboard]

2. Under *Add Render to provider*, switch to the *Okta* tab and copy your *Connection ID*.

3. Open the [Okta Integration Network App Catalog](https://www.okta.com/integrations/), then find and select the *Render* integration.

4. Click *+ Add Integration* to start configuring the integration for your Okta org.

5. In the *General Settings* tab of the configuration flow, provide your *Connection ID* in the corresponding field.

6. Provide values for other configuration fields as desired and complete the setup.

7. After your Render integration is created, navigate to its *Sign On* tab and copy its SAML 2.0 *Metadata URL*:

   [image: Copying the metadata URL in Okta]

8. Back in the Render Dashboard, return to the SSO configuration dialog. Switch to the *Connect provider to Render* tab:

   [image: Providing your IdP's metadata URL in the Render Dashboard]

9. Paste the Okta metadata URL you copied and click *Configure SAML SSO*.

### SCIM

#### 1. Generate a SCIM token

1. From your organization home in the [Render Dashboard](https://dashboard.render.com), open the org's *Settings* page.
2. Under *Security*, find the *SCIM Provisioning* section and click *+ Create*:

   [image: Creating a SCIM configuration in the Render Dashboard]

   A *SCIM Configuration* dialog appears.

3. Copy the values of *Base URL* and *Token* in the dialog. You'll provide these to Okta.

#### 2. Configure SCIM in Okta

1. From the *Applications* page in your Okta admin console, select the *Render* integration you created during [SSO setup](#sso).

2. Switch to the *Provisioning* tab and click *Configure API Integration*:

   [image: Configuring a SCIM API integration in Okta]

3. Check the *Enable API integration* checkbox. An *API Token* field appears:

   [image: Enabling a SCIM API integration in Okta]

4. Provide the *Token* value you copied during [SCIM token generation](#1-generate-a-scim-token).

5. Click *Test API Credentials* to verify that your API token is valid.

6. Click *Save*.

7. Still under the *Provisioning* tab, click *To App* in the left sidebar.

8. Under *Provisioning to App*, click *Edit* and check the checkbox for each Render provisioning action you want to enable in Okta (usually all of them):

   [image: Enabling SCIM provisioning in Okta]

9. Click *Save*.

You're all set! Okta syncs with Render to enable managing org members from your Okta admin console.

## Signing in with Okta

1. From the [Render login page](https://dashboard.render.com/login), click *Sign in with SSO*:

   [image: Signing in to Render via Okta]

   Note that the login page automatically redirects to the Render Dashboard if you're already signed in with another method. First sign out of Render, then try again.

2. Provide your Okta-managed email address and click *Sign in with SSO*:

   [image: Signing in to Render via Okta]

3. Render redirects you to your Okta sign-on flow.

4. After you successfully authenticate to Okta, you're redirected back to the Render Dashboard.

## Troubleshoot

If you have any issues setting up Okta SSO or SCIM for your org, please [reach out to the Render support team](https://dashboard.render.com?contact-support) in the Render Dashboard.