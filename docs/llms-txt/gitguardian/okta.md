# Source: https://docs.gitguardian.com/platform/enterprise-administration/sso-providers/okta.md

# Okta

> Configure SAML-based Single Sign-On (SSO) with Okta for GitGuardian, using either the Okta Integration Network app or a custom SAML app.

You can configure SSO using either the [GitGuardian app from the Okta Integration Network](#okta-oin-app) (recommended) or a [custom SAML app](#okta-custom-saml-app).

## Prerequisites

- An Okta account with administrator privileges
- A GitGuardian workspace with Owner or Manager role
- Your GitGuardian Workspace ID (found in your dashboard URL or workspace settings)

## Supported features

- **SP-initiated SSO**: Users can sign in to GitGuardian directly from the application URL
- **IdP-initiated SSO**: Users can sign in to GitGuardian from the Okta dashboard
- **Just-in-Time (JIT) provisioning**: New users are automatically created in GitGuardian on first login

:::tip
GitGuardian also supports SCIM provisioning for Okta. See the [SCIM configuration guide](../scim-configuration) for setup instructions.
:::

## SP-initiated SSO

Users can sign in directly to GitGuardian without going through Okta first:

1. Navigate to your GitGuardian dashboard URL (e.g., `https://dashboard.gitguardian.com`).
2. Enter your email address.
3. If your email domain is reserved, you will be automatically redirected to Okta for authentication.
4. After authenticating with Okta, you will be redirected back to GitGuardian.

## Okta OIN app

The GitGuardian app is available in the [Okta Integration Network](https://www.okta.com/integrations/gitguardian/).

1. In Okta, go to **Applications > Applications** and click **Browse App Catalog**.
2. Search for "GitGuardian" and select the GitGuardian app.
3. Click **Add Integration**.
4. On the **General Settings** page, configure the following:
   - **Application label**: Enter a name for the app (e.g., "GitGuardian").
   - **GitGuardian Workspace ID**: Enter your GitGuardian workspace ID.
   - **GitGuardian API FQDN**: Enter `api.gitguardian.com` or `api.eu1.gitguardian.com` (or your self-hosted API domain).
   - **GitGuardian Dashboard FQDN**: Enter `dashboard.gitguardian.com` or `dashboard.eu1.gitguardian.com` (or your self-hosted dashboard domain).

   ![okta app general settings](/img/platform/enterprise-administration/sso-providers/okta_app_general_settings.png)

5. Click **Done** to create the application.
6. Go to the **Sign On** tab to view the SAML configuration.
   ![okta app sign on](/img/platform/enterprise-administration/sso-providers/okta_app_sign_on.png)
7. Scroll down to find the SAML metadata and copy the following values:
   - **Sign on URL**
   - **Issuer**
   - **Signing Certificate** (download or copy)

   ![okta app saml metadata](/img/platform/enterprise-administration/sso-providers/okta_app_saml_metadata.png)

8. In your GitGuardian dashboard, navigate to **Settings > [Authentication](https://dashboard.gitguardian.com/settings/workspace/auth)** and click **Configure**.

   ![GitGuardian Authentication settings](/img/platform/enterprise-administration/sso-providers/okta_app_gg_auth_settings.png)

9. Configure the Identity Provider with the values from the previous step:
   - **Entity Id**: paste the **Issuer** value
   - **Single Sign-On URL**: paste the **Sign on URL** value
   - **X509 Cert**: paste the **Signing Certificate** content
   - Ensure that the checkbox **I have mapped the attributes first_name and last_name in my IdP** is checked

   ![GitGuardian IdP configuration](/img/platform/enterprise-administration/sso-providers/okta_app_gg_idp_config.png)

10. Assign users to the app in the **Assignments** tab.
11. **Important:** [Reserve your email domain](../saml-sso-configuration#email-domain-reservation) to enable automatic SSO discovery.

## Okta custom SAML app

If you prefer to create a custom SAML application, follow these steps:

1. In Okta, go to **Applications > Applications** and click **Create New App**.

   ![okta create new app](/img/platform/enterprise-administration/sso-providers/okta_create_new_app.png)

2. Set the general information for your SAML app (name, logo) that users will see when logging in.

   ![okta general](/img/platform/enterprise-administration/sso-providers/okta_general.png)

3. Click **Next** and configure the basic SAML settings:
   - **Single sign on URL**: paste the **ACS URL** value from the GitGuardian dashboard.
   - **Audience URI (SP Entity ID)**: paste the **SP Entity ID** value from the GitGuardian dashboard.
   - **Default RelayState**: leave blank.
   - **Name ID format**: set to **EmailAddress**.

   ![okta basic settings](/img/platform/enterprise-administration/sso-providers/okta_basic_settings.png)

4. Click **Show Advanced Settings** and verify the following:
   - Both **Response** and **Assertion Signature** are set to **Signed**.
   - **Signature Algorithm** is set to **RSA-SHA256**.
   - **Digest Algorithm** is set to **SHA256**.
   - Assertions are not encrypted.

   ![okta advanced settings](/img/platform/enterprise-administration/sso-providers/okta_advanced_settings.png)

5. Complete the remaining app configuration steps.

   ![okta config end](/img/platform/enterprise-administration/sso-providers/okta_config_end.png)

6. Go to the **Sign On** tab and configure attribute mappings:
   - `first_name` is mapped to the user's first name.
   - `last_name` is mapped to the user's last name.

   ![okta mappings](/img/platform/enterprise-administration/sso-providers/okta_mappings.png)

7. Still on the **Sign On** tab, click **View Setup Instructions** and use the provided values to configure the Identity Provider in the GitGuardian dashboard:
   - **Entity Id**: paste the **Identity Provider Issuer** value.
   - **Single Sign-On URL**: paste the **Identity Provider Single Sign-On URL** value.
   - **X509 Cert**: paste the **X.509 Certificate** content.
   - Ensure that the checkbox **I have mapped the attributes first_name and last_name in my IdP** is checked.

   ![okta setup instructions](/img/platform/enterprise-administration/sso-providers/okta_setup_instructions.png)
   ![okta idp_settings](/img/platform/enterprise-administration/sso-providers/okta_idp_settings.png)
8. **Important:** Don't forget to [reserve your email domain](../saml-sso-configuration#email-domain-reservation) to enable automatic SSO discovery.
