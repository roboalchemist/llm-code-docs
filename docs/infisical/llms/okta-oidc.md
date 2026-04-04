# Source: https://infisical.com/docs/documentation/platform/sso/okta-oidc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta OIDC

> Learn how to configure Okta OIDC for Infisical SSO.

<Info>
  Okta OIDC SSO is a paid feature. If you're using Infisical Cloud, then it is
  available under the **Pro Tier**. If you're self-hosting Infisical, then you
  should contact [sales@infisical.com](mailto:sales@infisical.com) to purchase a self-hosted license to use
  it.
</Info>

<Steps>
  <Step title="Create an OIDC application in Okta">
    In the Okta Admin Portal, select Applications > Applications from the navigation. On the Applications screen, click the **Create App Integration** button.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/create-app-integration.png" alt="Okta Applications page" />

    In the Create a New Application Integration dialog, select **OIDC - OpenID Connect** as the Sign-in method and **Web Application** as the Application type, then click **Next**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/create-oidc-app.png" alt="Create OIDC app integration" />

    On the New Web App Integration screen, configure the following settings:

    * **App integration name**: Enter a name like `Infisical`
    * **Grant type**: Ensure **Authorization Code** is checked
    * **Sign-in redirect URIs**: Set to `https://app.infisical.com/api/v1/sso/oidc/callback`
    * **Sign-out redirect URIs**: (Optional) Set to `https://app.infisical.com`
    * **Controlled access**: Select the appropriate access level for your organization

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/app-settings.png" alt="App settings configuration" />

    <Note>
      If you're self-hosting Infisical, replace `https://app.infisical.com` with your own domain in the redirect URIs.
    </Note>

    Click **Save** to create the application.

    After saving, scroll down to the **General Settings** section and click **Edit**. Ensure the **Proof of possession** setting labeled "Require Demonstrating Proof of Possession (DPoP) header in token requests" is **unchecked**.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/dpop-setting.png" alt="DPoP setting disabled" />

    <Warning>
      Infisical does not currently support DPoP for OIDC authentication.
    </Warning>
  </Step>

  <Step title="Retrieve Identity Provider (IdP) Information from Okta">
    After creating the application, you will be taken to the application's settings page. From the **General** tab, copy the **Client ID** and **Client Secret** values.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/client-credentials.png" alt="Client credentials" />

    Next, you need to obtain the Discovery Document URL (also known as the OpenID Configuration URL). This URL follows the format: `https://<your-okta-domain>/.well-known/openid-configuration`.

    To find your Okta domain, look at the URL in your browser's address bar while in the Okta Admin Portal. It typically looks like `https://your-company.okta.com` or `https://your-company.oktapreview.com`.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/okta-domain.png" alt="Okta domain in browser" />

    Your Discovery Document URL will be: `https://<your-okta-domain>/.well-known/openid-configuration`

    For example: `https://your-company.okta.com/.well-known/openid-configuration`
  </Step>

  <Step title="Finish configuring OIDC in Infisical">
    Back in Infisical, on the OIDC configuration page, set the **Configuration Type** to **Discovery URL**.

    Fill in the following fields:
    Fill in the following fields:

    * **Discovery Document URL**: Enter the OpenID Configuration URL from step 2 (e.g., `https://your-company.okta.com/.well-known/openid-configuration`)
    * **Client ID**: Enter the Client ID from step 2
    * **Client Secret**: Enter the Client Secret from step 2
    * **JWT Signature Algorithm**: Select **RS256** (this is the default algorithm used by Okta)

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/infisical-oidc-config.png" alt="Infisical OIDC configuration" />

    <Info>
      Currently, the following JWT signature algorithms are supported: RS256, RS512, HS256, and EdDSA. Okta typically uses RS256.
    </Info>

    Optionally, you can define a whitelist of allowed email domains to restrict which users can authenticate.

    Once you've filled in all the required fields, click **Update** to save the configuration.
  </Step>

  <Step title="Assign users in Okta to the application">
    Back in Okta, navigate to the **Assignments** tab of your Infisical application and click **Assign**. You can assign access to the application on a user-by-user basis using the **Assign to People** option, or in bulk using the **Assign to Groups** option.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/okta-oidc/assignment.png" alt="Okta user assignment" />

    At this point, you have configured everything you need within the context of the Okta Admin Portal.
  </Step>

  <Step title="Enable OIDC SSO in Infisical">
    Enabling OIDC SSO allows members in your organization to log into Infisical via Okta.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/sso/enable-oidc.png" alt="OIDC Okta enable OIDC" />
  </Step>

  <Step title="Enforce OIDC SSO in Infisical">
    Enforcing OIDC SSO ensures that members in your organization can only access Infisical
    by logging into the organization via Okta.

    To enforce OIDC SSO, you're required to test out the OpenID connection by successfully authenticating at least one Okta user with Infisical.
    Once you've completed this requirement, you can toggle the **Enforce OIDC SSO** button to enforce OIDC SSO.

    <Warning>
      We recommend ensuring that your account is provisioned using the application in Okta
      prior to enforcing OIDC SSO to prevent any unintended issues.
    </Warning>

    <Info>
      In case of a lockout, an organization admin can use the [Admin Login Portal](https://infisical.com/docs/documentation/platform/sso/overview#admin-login-portal) in the `/login/admin` path e.g. [https://app.infisical.com/login/admin](https://app.infisical.com/login/admin).
    </Info>
  </Step>
</Steps>

<Tip>
  If you are only using one organization on your Infisical instance, you can configure a default organization in the [Server Admin Console](../admin-panel/server-admin#default-organization) to expedite OIDC login.
</Tip>

<Note>
  If you're configuring OIDC SSO on a self-hosted instance of Infisical, make
  sure to set the `AUTH_SECRET` and `SITE_URL` environment variable for it to
  work:

  <div class="height:1px;" />

  * `AUTH_SECRET`: A secret key used for signing and verifying JWT. This
    can be a random 32-byte base64 string generated with `openssl rand -base64
      32`.

  <div class="height:1px;" />

  * `SITE_URL`: The absolute URL of your self-hosted instance of Infisical including the protocol (e.g. [https://app.infisical.com](https://app.infisical.com))
</Note>
