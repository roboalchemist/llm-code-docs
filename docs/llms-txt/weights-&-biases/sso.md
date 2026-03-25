# Source: https://docs.wandb.ai/platform/hosting/iam/sso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure SSO with OIDC

> Configure SSO using OpenID Connect with identity providers like Okta, Azure AD, and AWS Cognito for W&B instances.

W\&B's support for OpenID Connect (OIDC) compatible identity providers allows for management of user identities and group memberships through external identity providers like Okta, Keycloak, Auth0, Google, and Entra.

## OpenID Connect (OIDC)

W\&B supports the following OIDC authentication flows for integrating with external Identity Providers (IdPs).

1. Implicit Flow with Form Post
2. Authorization Code Flow with Proof Key for Code Exchange (PKCE)

These flows authenticate users and provide W\&B with the necessary identity information (in the form of ID tokens) to manage access control.

The ID token is a JWT that contains the user's identity information, such as their name, username, email, and group memberships. W\&B uses this token to authenticate the user and map them to appropriate roles or groups in the system.

In the context of W\&B, access tokens authorize requests to APIs on behalf of the user, but since W\&B’s primary concern is user authentication and identity, it only requires the ID token.

You can use environment variables to [configure IAM options](/platform/hosting/iam/advanced_env_vars) for your [Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud) or [Self-Managed](/platform/hosting/hosting-options/self-managed) instance.

To assist with configuring Identity Providers for [Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud) or [Self-Managed](/platform/hosting/hosting-options/self-managed) W\&B installations, follow these guidelines to follow for various IdPs. If you’re using the SaaS version of W\&B, reach out to [support@wandb.com](mailto:support@wandb.com) for assistance in configuring an Auth0 tenant for your organization.

## Configure your IdP

This section shows how to configure your identity provider (IdP) for OIDC. Select the tab for your IdP for details.

<Tabs>
  <Tab title="Cognito">
    Follow the procedure below to set up AWS Cognito for authorization:

    1. First, sign in to your AWS account and navigate to the [AWS Cognito](https://aws.amazon.com/cognito/) App.

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/setup_aws_cognito.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=dde958fe22b46bbaa30f14803e4214e6" alt="AWS Cognito setup" width="1672" height="946" data-path="images/hosting/setup_aws_cognito.png" />
       </Frame>

    2. Provide an allowed callback URL to configure the application in your IdP:
       * Add `http(s)://YOUR-W&B-HOST/oidc/callback` as the callback URL. Replace `YOUR-W&B-HOST` with your W\&B host path.

    3. If your IdP supports universal logout, set the Logout URL to `http(s)://YOUR-W&B-HOST`. Replace `YOUR-W&B-HOST` with your W\&B host path.

       For example, if your application was running at `https://wandb.mycompany.com`, you would replace `YOUR-W&B-HOST` with `wandb.mycompany.com`.

       The image below demonstrates how to provide allowed callback and sign-out URLs in AWS Cognito.

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/setup_aws_cognito_ui_settings.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=fe596a7883823850db590d508482626e" alt="Host configuration" width="1658" height="1056" data-path="images/hosting/setup_aws_cognito_ui_settings.png" />
       </Frame>

       *wandb/local* uses the [`implicit` grant with the `form_post` response type](https://auth0.com/docs/get-started/authentication-and-authorization-flow/implicit-flow-with-form-post) by default.

       You can also configure *wandb/local* to perform an `authorization_code` grant that uses the [PKCE Code Exchange](https://www.oauth.com/oauth2-servers/pkce/) flow.

    4. Select one or more OAuth grant types to configure how AWS Cognito delivers tokens to your app.

    5. W\&B requires specific OpenID Connect (OIDC) scopes. Select the following from AWS Cognito App:

       * "openid"
       * "profile"
       * "email"

       For example, your AWS Cognito App UI should look similar to the following image:

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/setup_aws_required_fields.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=32feee999a40b09f8c5b5cc4cfc45c8f" alt="Required fields" width="1656" height="670" data-path="images/hosting/setup_aws_required_fields.png" />
       </Frame>

       Select the **Auth Method** in the settings page or set the OIDC\_AUTH\_METHOD environment variable to tell *wandb/local* which grant to.

       You must set the Auth Method to `pkce`.

    6. You need a Client ID and the URL of your OIDC issuer. The OpenID discovery document must be available at `$OIDC_ISSUER/.well-known/openid-configuration`

       For example, , you can generate your issuer URL by appending your User Pool ID to the Cognito IdP URL from the **App Integration** tab within the **User Pools** section:

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/setup_aws_cognito_issuer_url.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=425e21b41d60903cb3da110ad2873277" alt="AWS Cognito issuer URL" width="3166" height="1616" data-path="images/hosting/setup_aws_cognito_issuer_url.png" />
       </Frame>

       Do not use the "Cognito domain" for the IDP URL. Cognito provides it's discovery document at `https://cognito-idp.$REGION.amazonaws.com/$USER_POOL_ID`

    Next, [Set up SSO in W\&B](#set-up-sso-in-w%26b).
  </Tab>

  <Tab title="Okta">
    Follow the procedure below to set up Okta for authorization:

    1. Log in to the [Okta Portal](https://login.okta.com/).

    2. On the left side, select **Applications** and then **Applications** again.
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/okta_select_applications.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=926c484f006c3c4e17d4b836a31973b7" alt="Okta Applications menu" width="1978" height="1625" data-path="images/hosting/okta_select_applications.png" />
       </Frame>

    3. Click on "Create App integration."
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/okta_create_new_app_integration.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=d7d0d37787dbf752d12742bd7128bb79" alt="Create App integration button" width="2330" height="1319" data-path="images/hosting/okta_create_new_app_integration.png" />
       </Frame>

    4. On the screen named "Create a new app integration," select **OIDC - OpenID Connect** and **Single-Page Application**. Then click "Next."
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/okta_create_a_new_app_integration.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=9b79968cfb3cd7436b2111e19fde1a1f" alt="OIDC Single-Page Application selection" width="1935" height="1690" data-path="images/hosting/okta_create_a_new_app_integration.png" />
       </Frame>

    5. On the screen named "New Single-Page App Integration," fill out the values as follows and click **Save**:
       * App integration name, for example "W\&B"
       * Grant type: Select both **Authorization Code** and **Implicit (hybrid)**
       * Sign-in redirect URIs: https\://YOUR\_W\_AND\_B\_URL/oidc/callback
       * Sign-out redirect URIs: https\://YOUR\_W\_AND\_B\_URL/logout
       * Assignments: Select **Skip group assignment for now**
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/okta_new_single_page_app_integration.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=8fc3cc15c16aa4dbc9ec9c7106bb3a29" alt="Single-Page App configuration" width="1692" height="2675" data-path="images/hosting/okta_new_single_page_app_integration.png" />
       </Frame>

    6. On the overview screen of the Okta application that you just created, make note of the **Client ID** under **Client Credentials** under the **General** tab:
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/okta_make_note_of_client_id.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=0249dcbd9b516dffcafe216b3e8c4973" alt="Okta Client ID location" width="1434" height="1734" data-path="images/hosting/okta_make_note_of_client_id.png" />
       </Frame>

    7. To identify the Okta OIDC Issuer URL, select **Settings** and then **Account** on the left side.
       The Okta UI shows the company name under **Organization Contact**.
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/okta_identify_oidc_issuer_url.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=39ae5e5daafd9477c7f47aada0080a54" alt="Okta organization settings" width="2166" height="1172" data-path="images/hosting/okta_identify_oidc_issuer_url.png" />
       </Frame>

    The OIDC issuer URL has the following format: `https://COMPANY.okta.com`. Replace COMPANY with the corresponding value. Make note of it.

    Next, [Set up SSO in W\&B](#set-up-sso-in-w%26b).
  </Tab>

  <Tab title="Entra">
    Azure AD (Entra ID) supports two OIDC configuration modes for W\&B. Choose the configuration that matches your security requirements:

    * [Public Client](#public-client): Uses PKCE without a client secret. Simpler to configure, suitable for most deployments.
    * [Confidential Client](#confidential-client): Uses PKCE with a client secret for enhanced security. Required if you need to set the `GORILLA_OIDC_SECRET` environment variable.

    <Warning>
      Do not mix configurations. If you select "Single-page application" in Azure AD, do not provide a client secret. If you need a client secret, you must select "Web" as the platform type.
    </Warning>

    <AccordionGroup>
      <Accordion title="Public client" defaultOpen="true">
        Use this configuration if you do not need to specify a client secret. This configuration is suitable for deployments without advanced security requirements.

        1. Log in to the [Azure Portal](https://portal.azure.com/).
        2. Navigate to **Microsoft Entra ID** service and select **App registrations** from the left sidebar.
        3. Click **New registration** at the top of the page.
        4. On the "Register an application" screen, configure the following:
           * **Name**: Enter a descriptive name.
           * **Supported account types**: Keep the default "Single tenant" or modify as needed.
           * **Redirect URI**: Select platform type **Single-page application** and enter `https://YOUR_W_AND_B_URL/oidc/callback`.
           * Click **Register**.
        5. After registration, note the following values from the Overview page:
           * **Application (client) ID**: Your OIDC Client ID.
           * **Directory (tenant) ID**: Your OIDC Issuer URL.
           <Frame>
             <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/entra_app_overview_make_note.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=e68ed7db543a4e87778e4d62eb8b507c" alt="Application and Directory IDs" width="3022" height="1328" data-path="images/hosting/entra_app_overview_make_note.png" />
           </Frame>
        6. Configure authentication settings:
           * Select **Authentication** from the left sidebar.
           * Under **Front-channel logout URL**, enter `https://YOUR_W_AND_B_URL/logout`.
           * Click **Save**.

        Make a note of the following details:

        * **OIDC Client ID**: The Application (client) ID from step 5
        * **OIDC Issuer URL**: `https://login.microsoftonline.com/{TenantID}/v2.0` (replace {TenantID} with your Directory ID from step 5)

        When configuring W\&B, use:

        * **Auth Method**: `pkce`
        * **OIDC Client Secret**: Leave empty (do not set `GORILLA_OIDC_SECRET`)

        Next, [Set up SSO in W\&B](#set-up-sso-in-w%26b).
      </Accordion>

      <Accordion title="Confidential client">
        Use this configuration if you need to authenticate using a client secret.

        1. Log in to the [Azure Portal](https://portal.azure.com/).
        2. Navigate to **Microsoft Entra ID** service and select **App registrations** from the left sidebar.
        3. Click **New registration** at the top of the page.
        4. On the "Register an application" screen, configure the following:
           * **Name**: Enter a descriptive name.
           * **Supported account types**: Keep the default "Single tenant" or modify as needed.
           * **Redirect URI**: Select platform type **Web** and enter `https://YOUR_W_AND_B_URL/oidc/callback`.
           * Click **Register**.
        5. After registration, note the following values from the Overview page:
           * **Application (client) ID**: Your OIDC Client ID.
           * **Directory (tenant) ID**: Your OIDC Issuer URL.
           <Frame>
             <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/entra_app_overview_make_note.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=e68ed7db543a4e87778e4d62eb8b507c" alt="Application and Directory IDs" width="3022" height="1328" data-path="images/hosting/entra_app_overview_make_note.png" />
           </Frame>
        6. Configure authentication settings:
           * Select **Authentication** from the left sidebar.
           * Under **Front-channel logout URL**, enter `https://<YOUR_W_AND_B_URL>/logout`.
           * Click **Save**
        7. Create a client secret:
           * Select **Certificates & secrets** from the left sidebar.
           * Click **New client secret**.
           * Add a description for the secret.
           * Choose an expiration period.
           * Click **Add**. <Warning>Copy and save the secret **Value** immediately (not the Secret ID)</Warning>.
           <Frame>
             <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/entra_make_note_of_secret_value.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=b7992bdb1f347eb66e9ab9d3187d591f" alt="Client secret value" width="2156" height="646" data-path="images/hosting/entra_make_note_of_secret_value.png" />
           </Frame>

        Make a note of the following details:

        * **OIDC Client ID**: The Application (client) ID from step 5.
        * **OIDC Client Secret**: The secret value from step 7.
        * **OIDC Issuer URL**: `https://login.microsoftonline.com/{TenantID}/v2.0` (replace {TenantID} with your Directory ID from step 5).

        When configuring W\&B, use:

        * **Auth Method**: `pkce`
        * **OIDC Client Secret**: Set the `GORILLA_OIDC_SECRET` environment variable to the secret value from step 7

        <Note>
          The v2.0 endpoint supports both personal Microsoft accounts and work/school accounts. If your organization requires the v1.0 endpoint, use `https://login.microsoftonline.com/{TenantID}` instead.
        </Note>

        Next, [Set up SSO in W\&B](#set-up-sso-in-w%26b).
      </Accordion>
    </AccordionGroup>
  </Tab>
</Tabs>

## Set up SSO in W\&B

To set up SSO, you need administrator privileges and the following information:

* OIDC Client ID
* OIDC Auth method (`implicit` or `pkce`)
* OIDC Issuer URL
* OIDC Client Secret (optional; depends on how you have setup your IdP)

If your IdP requires a OIDC Client Secret, specify it by passing the [environment variables](/platform/hosting/env-vars) `GORILLA_OIDC_SECRET`.

* In the W\&B App, go to **System Console** > **Settings** > **Advanced** > **User Spec** and add `GORILLA_OIDC_SECRET` to the `extraENV` section as shown below.
* In Helm, configure `values.global.extraEnv` as shown below.
  ```yaml  theme={null}
  values:
  global:
      extraEnv:
      GORILLA_OIDC_SECRET="<your_secret>"
  ```

<Note>
  If you're unable to log in to your instance after configuring SSO, you can restart the instance with the `LOCAL_RESTORE=true` environment variable set. This outputs a temporary password to the containers logs and disables SSO. Once you've resolved any issues with SSO, you must remove that environment variable to enable SSO again.
</Note>

<Tabs>
  <Tab title="System Console">
    The System Console is the successor to the System Settings page. It is available with the [W\&B Kubernetes Operator](/platform/hosting/operator/) based deployment.

    1. Refer to [Access the W\&B Management Console](/platform/hosting/operator/#access-the-wb-management-console).

    2. Navigate to **Settings**, then **Authentication**. Select **OIDC** in the **Type** dropdown.
       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/sso_configure_via_console.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=42923327cbf90d9a0a3e42ec9d0a6b9f" alt="System Console OIDC configuration" width="2763" height="888" data-path="images/hosting/sso_configure_via_console.png" />
       </Frame>

    3. Enter the values.

    4. Click on **Save**.

    5. Log out and then log back in, this time using the IdP login screen.

    ## Find your customer namespace

    Before you can configure team-level BYOB with CoreWeave storage on W\&B Dedicated Cloud or Self-Managed, you need to obtain your organization's **Customer Namespace**. You can view and copy it from the bottom of the **Authentication** tab.

    For detailed instructions on configuring CoreWeave storage with your Customer Namespace, see [CoreWeave requirements for Dedicated Cloud / Self-Managed](/platform/hosting/data-security/secure-storage-connector#coreweave-customer-namespace).
  </Tab>

  <Tab title="System settings">
    1. Log in to your Weights & Biases instance.

    2. Navigate to the W\&B App.

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/system_settings.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=3fe7f51b022ab4f29742f7d5688286d8" alt="W&B App navigation" width="1041" height="1079" data-path="images/hosting/system_settings.png" />
       </Frame>

    3. From the dropdown, select **System Settings**:

       <Frame>
         <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/system_settings_select_settings.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=a233c35326e9135811c6767188288e2a" alt="System Settings dropdown" width="1049" height="396" data-path="images/hosting/system_settings_select_settings.png" />
       </Frame>

    4. Enter your Issuer, Client ID, and Authentication Method.

    5. Select **Update settings**.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/7mSicW8MfO9qZmb2/images/hosting/system_settings_select_update.png?fit=max&auto=format&n=7mSicW8MfO9qZmb2&q=85&s=1430cb0949f9cde7bd90d30fa6459d1b" alt="Update settings button" width="922" height="1338" data-path="images/hosting/system_settings_select_update.png" />
    </Frame>
  </Tab>
</Tabs>

<Note>
  If you're unable to log in to your instance after configuring SSO, you can restart the instance with the `LOCAL_RESTORE=true` environment variable set. This outputs a temporary password to the containers logs and turn off SSO. Once you've resolved any issues with SSO, you must remove that environment variable to enable SSO again.
</Note>

## Security Assertion Markup Language (SAML)

W\&B does not support SAML.
