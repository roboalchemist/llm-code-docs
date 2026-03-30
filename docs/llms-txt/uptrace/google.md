# Source: https://uptrace.dev/raw/features/sso/google.md

# Google Cloud Single Sign-On

> Configure Google Cloud OpenID Connect SSO with Uptrace using OAuth clients, redirect URIs, and client credentials.

[Google Cloud](https://cloud.google.com/) provides OpenID Connect (OIDC) identity services that you<br />


can use to bring your Google users into Uptrace.

Single Sign-On allows you to manage users using OIDC providers. After logging in, such users are<br />


automatically added to a team and can access team projects. When users are removed from Google, they<br />


automatically lose granted access in Uptrace.

## Step 1. Create OIDC SSO in Uptrace

1. In Uptrace, go to **Organization** -> **Single Sign-On**
2. Click **New SSO** -> **New Google (OIDC)**
3. Fill out the form:
  - **Domain**: your unique domain name (can be any string; it will be used later during the sign-in<br />
  
  
  process)
  - **User team**: select the team that will be automatically assigned to new users
  - **User role**: select the role that will be automatically assigned to new users

![Uptrace Google OIDC](/features/google/uptrace-google-oidc.png)

1. Click **Create** and you will be presented with the redirect URL to configure Google OAuth

![Uptrace OIDC info](/features/google/uptrace-google-oidc-info.png)

Leave this form open â you will need to enter the **Client ID** and **Client Secret** from Google to<br />


finish the setup.

## Step 2. Create Google OAuth client

1. Visit [Google Cloud Console](https://console.cloud.google.com) and open **APIs & Services**
2. Open the **Credentials** tab and click **Create credentials** -> **OAuth client ID**
3. Set **Application type** to **Web application**
4. Under **Authorized redirect URIs**, add the redirect URL you received from Uptrace in Step 1
5. Click **Save** and you will be presented with the **Client ID** and **Client Secret**

![Google OAuth client](/features/google/google-oauth-client-cloud.png)

## Step 3. Finish configuring Uptrace

1. Go back to the OIDC SSO form you left open in Step 1
2. Enter the **Client ID** and **Client Secret** you received from Google in Step 2
3. Click **Save**

![Uptrace OAuth client](/features/google/uptrace-google-oidc-final.png)

You can now log in to Uptrace using Google by opening<br />

`https://uptrace.dev/auth/sso/<your-domain>`.

## Troubleshooting

**Redirect URI mismatch** â The redirect URI configured in Google Cloud must exactly match what<br />


Uptrace uses. Make sure the protocol (`http` vs `https`), host, and port all match.

**User has no email** â Uptrace requires an email address for SSO users. Google accounts always have<br />


an email, so this is typically not an issue.

**OAuth consent screen not configured** â If you see an error about the consent screen, make sure you<br />


have configured the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent)<br />


in Google Cloud Console before creating the OAuth client.
