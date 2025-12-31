# Source: https://docs.carv.io/carv-ecosystem/carv-play/carv-intro/carv-id-oauth-2.0.md

# CARV ID OAuth 2.0

## Overview

This guide is intended for developers looking to integrate CARV ID authentication into their applications using OAuth 2.0. OAuth 2.0 is a standard for authorization that enables third-party applications to obtain limited access to an HTTP service. By integrating CARV ID OAuth 2.0, users can securely and conveniently log in to your application using their CARV ID credentials.

## Prerequisites

Before you begin, ensure you have the following:

* A registered application with CARV and your `Client ID` and `Client Secret`.&#x20;
* An understanding of OAuth 2.0 flow.

### Step 1: Register Your Application

1. **Determining Necessary Permissions**: Begin by reviewing the [application scopes available](#scopes) to identify the permissions your application will need.
2. Provide Application Information: Share your application's **Redirect URL** and the **scopes** you've selected based on your needs. Additionally, provide the following information:
   * **Name Displayed on OAuth Screen**: The name of your application as it will appear during the authentication process.
   * **Home Page URL**: The main URL of your application, where users can learn more about your service.
   * **Logo Image URL**: A URL pointing to your logo image, which will be displayed during the authentication process.
   * **Privacy Policy URL**: The URL of your privacy policy page.
   * **Terms of Service URL**: The URL of your terms of service page.
3. After we receive this information, we will set up your OAuth configuration and provide you with a Client ID and Client Secret. Keep these confidential.

### Step 2: Implement the OAuth 2.0 Flow

{% hint style="info" %}
&#x20;OAuth 2.0 flow at a very high level:

* The application renders a “Sign in with CARV ID” link or button.
* The user clicks the sign in button.
* The current web browser is redirected to CARV (or a new browser is opened and directed to CARV).
* The user completes a login and authorization step at CARV if needed.
* CARV redirects back to an URL under the application’s control, passing authorization information for the user.

<img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FcezLQT2eNb3sXh4F7UIR%2Fimage.png?alt=media&#x26;token=dc8c82e2-ee22-4d98-81e3-bf1283d19785" alt="" data-size="original">
{% endhint %}

## API Details

**Discover OAuth Information**

```bash
curl -X GET https://oauth.carv.io/.well-known/openid-configuration
```

#### Authorization Request

Construct and redirect users to the CARV ID authorization page to begin the authentication process:

{% code overflow="wrap" %}

```bash
https://auth.carv.io/auth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=code&scope=YOUR_SCOPE&state=YOUR_STATE
```

{% endcode %}

Parameters:

* `response_type`: Should be `code` for the authorization code flow.
* `client_id`: Your application's Client ID.
* `redirect_uri`: The URL to which CARV ID will send the user after authorization.
* `scope`: The space-separated list of permissions your application requests.
* `state`: A unique state value that your application generates to mitigate CSRF attacks.

After successful login and authorization, user will be redirected to the provided URL with `code` and `state` included in the parameters.

#### **Scopes**

Scopes allow you to set granular access for your application so that your application only has the permissions that it needs.

<table><thead><tr><th width="262">Scope</th><th>Description</th></tr></thead><tbody><tr><td>carv_id_basic_read</td><td>Basic CARV ID info</td></tr><tr><td>email_basic_read</td><td>Email address</td></tr><tr><td>twitter_basic_read</td><td>Basic Twitter account info</td></tr><tr><td>discord_basic_read</td><td>Basic Discord account info</td></tr><tr><td>facebook_basic_read</td><td>Basic Facebook account info</td></tr><tr><td>google_basic_read</td><td>Basic Google account info</td></tr><tr><td>steam_basic_read</td><td>Basic Steam account info</td></tr><tr><td>steam_detailed_read</td><td>Detailed Steam account info</td></tr><tr><td>carv_play_basic_read</td><td>Basic CARV Play account info</td></tr><tr><td>evm_address_basic_read</td><td>EVM address</td></tr><tr><td>solana_address_basic_read</td><td>Solana address</td></tr><tr><td>bitcoin_address_basic_read</td><td>Bitcoin address</td></tr><tr><td>platform_detailed_read</td><td>User's account info from your platform/application/game</td></tr><tr><td>platform_detailed_write</td><td>Update user's account info from your platform/application/game to CARV ID</td></tr></tbody></table>

#### Access Token Request

After the user authorizes your application, they will be redirected to your `redirect_uri` with a `code` parameter. Exchange this code for an access token.

```bash
curl -X POST https://oauth.carv.io/oauth2/token \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Authorization: Basic YOUR_BASE64_ENCODED_CLIENT_ID_AND_SECRET" \
-d "grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=YOUR_REDIRECT_URI"
```

Parameters:

* `grant_type`: Should be `authorization_code`.
* `code`: The authorization code received from the authorization request.
* `redirect_uri`: Must match the redirect URI used in the authorization request.
* `client_id`: Your application's Client ID.
* `client_secret`: Your application's Client Secret.

Sample Python code to encode credentials:

```python
import base64

# Your client ID and client secret
client_id = 'your_client_id_here'
client_secret = 'your_client_secret_here'

# Concatenate the client ID and client secret with a colon
credentials = f"{client_id}:{client_secret}"

# Encode the credentials using base64
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# The result can be used in the Authorization header
print("Basic " + encoded_credentials)
```

Response Sample

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "access_token": "xxxx",
    "token_type": "Bearer",
    "expires_in": "604800",
    "scope": "xxxx",
    "refresh_token": "xxxx",
    "id_token": "xxxx"
  }
}

```

#### Token Refresh Request

Refresh an expired access token using:

```bash
curl -X POST https://oauth.carv.io/oauth2/token \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Authorization: Basic YOUR_BASE64_ENCODED_CLIENT_ID_AND_SECRET" \
-d "grant_type=refresh_token&refresh_token=YOUR_REFRESH_TOKEN&scope=YOUR_SCOPE"
```

Parameters:

* `grant_type`: Should be `refresh_token`.
* `refresh_token`: The `refresh_code` received from the access token request.
* `scope`: The space-separated list of permissions your application requests.
* `client_id`: Your application's Client ID.
* `client_secret`: Your application's Client Secret.

Response Sample

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "access_token": "xxxx",
    "token_type": "Bearer",
    "expires_in": "604800",
    "scope": "xxxx",
    "refresh_token": "xxxx",
    "id_token": "xxxx"
    }
}
```

#### Fetch User Detailed Info&#x20;

Retrieve detailed user information with:

```bash
curl -X GET https://oauth.carv.io/api/userinfo \
-H "Authorization: Bearer ACCESS_TOKEN"
```

Response Sample

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "smart_wallet_address": "xxxx",
    "signer_wallet_address": "xxxx",
    "email_address": "abc@gmail.com",
    "twitter": {
         "id": "xxxx",
         "username": "xxxx"
         }
    // Additional fields
    }
}
```

#### Update User Profile

Third-party data providers can update the user's profile data via:

```bash
curl -X POST https://oauth.carv.io/api/userinfo/update \
-H "Content-Type: application/x-www-form-urlencoded" \
-H "Authorization: Bearer ACCESS_TOKEN" \
-d "user_id=xxx&user_name=xxx&properties={}"
```

Parameters:

* `user_id`: The unique identifier for the user on the third-party platform.
* `user_name`: The name of the user on the third-party platform.
* `properties`: A JSON formatted string containing any additional property data to upload.

Note that to use this API, you will need to apply for the write access scope for the platform.

## Conclusion

This guide outlines the process for securely integrating CARV ID OAuth 2.0 into your applications, enhancing user authentication experiences.
