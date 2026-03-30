# Source: https://docs.base44.com/Setting-up-your-app/Setting-up-SSO.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up Single Sign-On (SSO) for your app

> Let your team log in to your Base44 app using providers like Google, Microsoft, GitHub, Okta, Apple, or other OIDC identity providers instead of separate logins.

## Step 1 | Get started with SSO

Single Sign-On (SSO) lets people sign in to your Base44 app using an external identity provider that supports OpenID Connect (OIDC), such as Google, Microsoft, GitHub, Okta, Apple, or Kakao, instead of creating a separate login for your app.

<Note>
  **Notes:**

  * Single sign-on (SSO) is available for Base44 apps on the [**Elite plan**](https://base44.com/pricing) or higher.
  * To connect a provider such as Kakao through SSO, you need your own account with that provider and an app configured there. You are responsible for creating and managing the client ID, client secret, redirect URI, and any other credentials in your identity provider’s dashboard.
</Note>

**To find your Base44 app ID and redirect URI:**

1. Go to your app editor in [Base44](https://app.base44.com).
2. Check your browser’s address bar and find the **app ID** between `/apps/` and `/editor/` in the URL.
3. Build your redirect URI by replacing `{{APP_ID}}` in this format with your app ID:

   [https://app.base44.com/api/apps/\{\{APP\_ID}}/auth/sso/callback](https://app.base44.com/api/apps/\{\{APP_ID}}/auth/sso/callback)

<AccordionGroup>
  <Accordion title="Example: From app URL to redirect URI">
    With the app editor open, the URL might look like this:

    [https://app.base44.com/apps/686404784ac37377589a1f7f/editor/](https://app.base44.com/apps/686404784ac37377589a1f7f/editor/)...

    Here, **686404784ac37377589a1f7f** is the app ID. Plug that into the format:

    [https://app.base44.com/api/apps/686404784ac37377589a1f7f/auth/sso/callback](https://app.base44.com/api/apps/686404784ac37377589a1f7f/auth/sso/callback)

    This is the redirect URI you’ll enter with your SSO provider.
  </Accordion>
</AccordionGroup>

## Step 2 | Choose your provider

Start by choosing the identity provider your team already uses. You can pick a built-in option (Google, Microsoft, GitHub, or Okta), or use Advanced / Manual configuration to connect any OIDC provider, including Kakao, or your own IdP.

<CardGroup cols={2}>
  <Card title="Google Workspace" icon="google" href="#google-workspace">
    Allow sign-in with Google Workspace accounts.
  </Card>

  <Card title="Microsoft 365 / Entra ID" icon="microsoft" href="#microsoft">
    Allow sign-in with Microsoft 365 or Entra ID.
  </Card>

  <Card title="GitHub" icon="github" href="#github">
    Allow sign-in with GitHub accounts.
  </Card>

  <Card title="Okta" icon="lock" href="#okta">
    Allow sign-in with your Okta directory.
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Advanced / Manual configuration" icon="sliders" href="#advanced-/-manual-configuration">
    Connect any OIDC-compatible provider such as Kakao, or a custom IdP using custom endpoints.
  </Card>
</CardGroup>

### Google Workspace

Use Google Workspace as your SSO provider with an OAuth 2.0 Web application. First, create an OAuth 2.0 client in [Google Cloud Console](https://console.cloud.google.com/apis/credentials) for your project, then add those credentials in Base44.

<Tip>
  Before you set up SSO, you’ll need:

  * A client ID and client secret from Google Cloud
  * Your app’s redirect URI (see Step 1)

  Check out [Google’s credential setup guide](https://developers.google.com/workspace/guides/create-credentials)
</Tip>

**To set up Google Workspace SSO in Base44:**

1. In your app editor, click **Dashboard**.
2. Click **Settings**.
3. Click **Authentication**.
4. Click **Set Up** next to **Single sign-on (SSO)**.
5. In **Select SSO provider**, choose **Google Workspace**.
6. Enter your **Client Id** and **Client Secret** from Google.
7. Keep **Scope** as `openid email profile`.
8. Leave **Discovery Url** set to the default value.
9. Click **Enable SSO**.

<Frame caption="Google Workspace SSO settings in your Base44 app">
  <img src="https://mintcdn.com/base44/c9pgaSv8ZgsIBTv-/images/GoogleSSOElite.png?fit=max&auto=format&n=c9pgaSv8ZgsIBTv-&q=85&s=feb7b5feff29700974cb4741dd9d86c9" alt="Base44 Single sign-on settings configured with Google Workspace as the SSO provider" className="mx-auto" style={{ width:"85%" }} title="" width="648" height="379" data-path="images/GoogleSSOElite.png" />
</Frame>

### Microsoft

Use Microsoft Entra ID (Azure AD) as your SSO provider through your [Azure portal](https://portal.azure.com).

<Tip>
  Before you set up SSO, you'll need:

  * Application (client) ID, directory (tenant) ID, and client secret from Azure
  * Your app’s redirect URI (see Step 1)
  * Scopes including `openid`, `email`, `profile`, and `User.Read`

  Check out [Microsoft identity platform registration](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)
</Tip>

**To set up Microsoft SSO in Base44:**

1. In your app editor, click **Dashboard**.
2. Click **Settings**.
3. Click **Authentication**.
4. Click **Set Up** next to **Single sign-on (SSO)**.
5. In **Select SSO provider**, choose **Microsoft Azure AD**.
6. Enter your Azure **Application (client) ID**, **Client Secret**, and **Directory (tenant) ID**.
7. Keep **Scope** as `openid email profile`.
8. For **Discovery Url**, enter:

   [https://login.microsoftonline.com/\{TENANT\_ID}/v2.0/.well-known/openid-configuration](https://login.microsoftonline.com/\{TENANT_ID}/v2.0/.well-known/openid-configuration)

   <Tip>
     Replace `{TENANT_ID}` with your directory (tenant) ID from the Azure portal.
   </Tip>
9. Click **Enable SSO**.

<Frame caption="Microsoft Azure AD SSO settings in your Base44 app">
  <img src="https://mintcdn.com/base44/8mP_E231St55tVaf/images/MicrosoftSSOElite.png?fit=max&auto=format&n=8mP_E231St55tVaf&q=85&s=8014173cb719c9c77d3cc5967ceb1c2e" alt="Base44 Single sign-on settings configured with Microsoft Azure AD as the SSO provider" className="mx-auto" style={{ width:"85%" }} title="" width="648" height="417" data-path="images/MicrosoftSSOElite.png" />
</Frame>

### GitHub

Use a GitHub OAuth app as your SSO provider. Create an OAuth app in [GitHub Developer Settings](https://github.com/settings/developers), then connect it in Base44.

<Tip>
  Before you set up SSO, you'll need:

  * A GitHub OAuth app created in GitHub Developer Settings
  * The app's authorization callback URL set to your redirect URI (see Step 1)
  * Client ID and client secret generated by GitHub for your OAuth app

  Check out [GitHub’s OAuth app guide](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
</Tip>

**To set up GitHub SSO in Base44:**

1. In your app editor, click **Dashboard**.
2. Click **Settings**.
3. Click **Authentication**.
4. Click **Set Up** next to **Single sign-on (SSO)**.
5. In **Select SSO provider**, choose **GitHub**.
6. Enter your GitHub **Client Id** and **Client Secret**.
7. Keep **Scope** as `user:email`.
8. Keep the default **Auth Endpoint**, **Token Endpoint**, and **Userinfo Endpoint** values for GitHub.
9. Click **Enable SSO**.

<Frame caption="GitHub SSO settings in your Base44 app">
  <img src="https://mintcdn.com/base44/c9pgaSv8ZgsIBTv-/images/GitHubSSOElite.png?fit=max&auto=format&n=c9pgaSv8ZgsIBTv-&q=85&s=fa5b9013edba27d1b2014bf6c5d2bb2c" alt="Base44 Single sign-on settings configured with GitHub as the SSO provider" className="mx-auto" style={{ width:"85%" }} title="" width="697" height="450" data-path="images/GitHubSSOElite.png" />
</Frame>

### Okta

Use Okta as your SSO provider. In your Okta Admin Console, create an OIDC Web application for your Base44 app, then add the credentials in Base44.

<Tip>
  Before you set up SSO, you'll need:

  * Okta client ID and client secret
  * Your Okta domain (e.g. `your-company.okta.com`)
  * Discovery URL from Okta issuer, for example: `https://your-company.okta.com/oauth2/default/.well-known/openid-configuration`
  * Scopes including `openid email profile`

  Check out [Okta’s SSO for Native apps guide](https://developer.okta.com/docs/guides/configure-native-sso/main/)
</Tip>

**To set up Okta SSO in Base44:**

1. In your app editor, click **Dashboard**.
2. Click **Settings**.
3. Click **Authentication**.
4. Click **Set Up** next to **Single sign-on (SSO)**.
5. In **Select SSO provider**, choose **Okta**.
6. Enter the following:
   * **Client Id:** Your Okta client ID.
   * **Client Secret:** Your Okta client secret.
   * **Okta Domain:** Your Okta domain (e.g.`your-company.okta.com`).
   * **Scope:** Keep `openid email profile`.
   * **Discovery Url:** Your Okta discovery URL.
7. Click **Enable SSO**.

<Frame caption="Okta SSO settings in your Base44 app">
  <img src="https://mintcdn.com/base44/8mP_E231St55tVaf/images/OKTASSOElite.png?fit=max&auto=format&n=8mP_E231St55tVaf&q=85&s=1c6e09b8f5c2a4925f5e4c8c6886d078" alt="Base44 Single sign-on settings configured with Okta as the SSO provider" className="mx-auto" style={{ width:"85%" }} title="" width="675" height="444" data-path="images/OKTASSOElite.png" />
</Frame>

### Advanced / Manual configuration

Use **Advanced / Manual configuration** to connect any OIDC compatible identity provider that is not covered by the built in options. This includes providers such as Kakao, as long as they support OIDC and you configure them with the correct details from your provider.

<Tip>
  Before you set up SSO, you will need:

  * OIDC client credentials from your provider
  * Your app’s redirect URI (see Step 1)
  * Discovery URL or all OIDC endpoints from your provider
  * Required scopes (`openid email profile` or equivalent)

  Check your provider’s documentation for details.
</Tip>

**To set up Advanced / Manual configuration in Base44:**

1. In your app editor, click **Dashboard**.
2. Click **Settings**.
3. Click **Authentication**.
4. Click **Set Up** next to **Single sign-on (SSO)**.
5. In **Select SSO provider**, choose **Advanced / Manual Configuration**.
6. Fill in the following fields using your provider’s values:
   * **Name:** A name for this SSO configuration (for example, `Auth0`, `Keycloak`, `Kakao`, or your identity provider name).
   * **Client Id:** Your OIDC client ID.
   * **Client Secret:** Your OIDC client secret.
   * **Scope:** Keep `openid email profile`.
   * **Discovery Url:** Your provider’s discovery URL, if available.
   * **Auth Endpoint, Token Endpoint, Userinfo Endpoint, Jwks Uri:** If you are not using a discovery URL, paste each endpoint from your provider’s documentation.
7. Click **Enable SSO**.

<Frame caption="Advanced / Manual SSO configuration in your Base44 app">
  <img src="https://mintcdn.com/base44/w6J-_6VjUqxS2R_Z/images/AdvancedSSOElite.png?fit=max&auto=format&n=w6J-_6VjUqxS2R_Z&q=85&s=a67a327f47a29a4b64b5e490c8e3d8c7" alt="Base44 Single sign-on settings panel configured with Advanced / Manual SSO" className="mx-auto" style={{ width:"85%" }} title="" width="721" height="587" data-path="images/AdvancedSSOElite.png" />
</Frame>

## Step 3 | Test your SSO login

After setting up SSO, test that everything works as expected.

**To test your SSO login:**

1. Log out of your app if you are currently signed in.
2. Go to your app’s login screen.
3. Click **Log in with SSO** or select the provider you configured.
4. Sign in using an email address from your approved domain.

You’ll be logged in automatically.

## FAQs

Click a question to learn more about SSO.

<AccordionGroup>
  <Accordion title="Do I need to set up SSO if I only use one login?">
    No, SSO is optional. You can continue using your existing login method if it works for you. If you want your team to log in with Google, Microsoft, GitHub, Okta, or another OIDC provider, you can set up SSO and configure the provider you use.
  </Accordion>

  <Accordion title="What is a redirect URI and where do I use it?">
    A redirect URI tells your identity provider (like Google or Microsoft) where to send people after they log in. You enter it when you set up SSO in your provider’s dashboard. It should look like this:

    [https://app.base44.com/api/apps/\{\{APP\_ID}}/auth/sso/callback](https://app.base44.com/api/apps/\{\{APP_ID}}/auth/sso/callback)

    <Note>
      Make sure to replace `{{APP_ID}}` with your actual Base44 app ID.
    </Note>
  </Accordion>

  <Accordion title="What is a discovery URL and do I need to add it?">
    A discovery URL tells Base44 how to connect to your identity provider. It helps Base44 automatically find the right endpoints and configuration values. You only need this for some providers.

    * For **Google**, you do not need to enter a discovery URL. Base44 handles it automatically.
    * For **Microsoft (Azure / Entra ID)** and **Okta**, your provider gives you a discovery URL. Copy it into the **Discovery Url** field in your Base44 SSO settings.
    * For **GitHub**, you can leave the discovery URL field blank.
    * For **Advanced / Manual** providers such as Kakao, follow your provider’s documentation. If they give you a discovery URL, paste it into the **Discovery Url** field. If not, enter the individual endpoints instead.

    <Note>
      If your provider gives you a discovery URL, paste it into the **Discovery Url** field in your Base44 SSO settings. If not, you can leave it empty and fill in the endpoints manually.
    </Note>
  </Accordion>

  <Accordion title="What if I see an error when logging in using SSO?">
    Check the following:

    * Your **redirect URI** in Base44 exactly matches the one in your provider’s dashboard.
    * Your **client ID**, **client secret**, and, if used, **Discovery Url** are correct.
    * The **scope** is set as `openid email profile` in both your provider’s configuration and in Base44 (or an equivalent email scope).

    If SSO fails after checking all fields, contact [support](https://app.base44.com/support/conversations) with screenshots of your settings.
  </Accordion>

  <Accordion title="Why does the Google login still show &#x22;base44.com&#x22; instead of my app name after setting up custom SSO?">
    If Google still shows `base44.com` as the app name or badge, your custom Google project has not been fully approved yet. Once Google approves your project, your app’s own name or branding will appear instead of `base44.com`.
  </Accordion>

  <Accordion title="How can I make sure my app name appears in the Google login instead of &#x22;base44.com&#x22;?">
    Finish setting up your custom SSO, publish your app, and submit your Google project for approval. After Google approves the project, your app name or branding will appear during sign-in instead of `base44.com`.
  </Accordion>

  <Accordion title="Which applications commonly use SSO or OAuth?">
    Many services support SSO or OAuth when working with enterprise or managed accounts, including: Langfuse, OpenAI, Anthropic, Mongo, Mixpanel, Mintlify, SendGrid, FeatureBase, Cloudflare, Logfire, GitHub, GCP, Render, AWS, Deno, Gong, Appspot, DocuSign, and Modal.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).