# Source: https://uptrace.dev/raw/features/sso/okta.md

# Okta Single Sign-On

> Configure Okta as a SAML 2.0 identity provider for Uptrace SSO using app integrations, attribute statements, and metadata URLs.

[Okta](https://www.okta.com/) is a cloud-based identity and access management platform that supports<br />


SAML 2.0, OpenID Connect, and OAuth 2.0. You can use Okta as a SAML 2.0 Identity Provider to bring<br />


your Okta users into Uptrace.

Single Sign-On allows you to manage users using SAML providers. After logging in, such users are<br />


automatically added to a team and can access team projects. When users are removed from Okta, they<br />


automatically lose granted access in Uptrace.

## Step 1. Create SAML SSO in Uptrace

1. In Uptrace, go to **Organization** -> **Single Sign-On**
2. Click **New SSO** -> **New SAML**
3. Fill out the form:
  - **Domain**: your unique domain name (can be any string; it will be used later during the sign-in<br />
  
  
  process)
  - **User team**: select the team that will be automatically assigned to new users
  - **User role**: select the role that will be automatically assigned to new users

![Uptrace SAML](/features/okta/uptrace-saml-create.png)

1. Click **Create** and you will be presented with the service provider information required to<br />


configure Okta

![Uptrace service provider](/features/okta/uptrace-service-provider-info.png)

Leave this form open â you will need to enter the **Metadata URL** from Okta to finish the setup.

## Step 2. Create an app integration in Okta

1. In Okta, go to **Applications** and click **Create App Integration**
2. In the dialog window, select **SAML 2.0** and click **Next**

![Okta new app](/features/okta/okta-new-app.png)

1. In the **General Settings** tab, use `Uptrace` as the app name and click **Next**

![Okta general settings](/features/okta/okta-general-settings.png)

## Step 3. Configure SAML settings

1. In the **Configure SAML** tab, use the service provider information you received from Uptrace in<br />


Step 1 to fill in the **Single sign-on URL** and **Audience URI (SP Entity ID)** fields

![Okta SAML settings](/features/okta/okta-saml-settings.png)

1. On the same page, scroll down to **Attribute Statements** and add the following attributes:

![Okta Attributes](/features/okta/okta-attributes.png)

1. Click **Next** to go to the feedback page. Select the appropriate option and click **Finish**

![Okta Feedback](/features/okta/okta-feedback.png)

## Step 4. Get metadata URL

1. You should land on the **Sign On** tab for your new application
2. Find and copy the **Metadata URL** â you will need it to finish configuring Uptrace

![Okta Metadata URL](/features/okta/okta-metadata-url.png)

## Step 5. Finish configuring Uptrace

1. Go back to the SAML SSO form you left open in Step 1
2. Enter the **Metadata URL** you copied from Okta in Step 4
3. Click **Save**

![Uptrace metadata URL](/features/okta/uptrace-metadata-url.png)

You can now log in to Uptrace using Okta by opening<br />

`https://uptrace.dev/auth/sso/<your-domain>`.

## Troubleshooting

**Metadata URL not accessible** â Uptrace needs to fetch the metadata URL from Okta to obtain the<br />


SAML certificate and endpoints. Make sure the URL is reachable from the Uptrace host.

**Attribute statements missing** â Uptrace requires email and name attributes from the SAML<br />


assertion. Make sure you configured the attribute statements as described in Step 3.

**User has no email** â Uptrace requires an email address for SSO users. Make sure the Okta user has<br />


an email configured in their profile.
