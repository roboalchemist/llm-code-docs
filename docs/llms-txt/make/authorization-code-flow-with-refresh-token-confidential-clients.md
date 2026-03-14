# Source: https://developers.make.com/api-documentation/authentication/oauth-flow/authorization-code-flow-with-refresh-token-confidential-clients.md

# Authorization code flow with refresh token (confidential clients)

**Use this flow when:** Your application can securely store a Client Secret (server-side applications).

**Benefits:** Provides both access tokens and refresh tokens for long-term access.

{% stepper %}
{% step %}

#### Redirect user for authorization

Redirect the user to the authorization endpoint:

```
GET https://www.make.com/oauth/v2/authorize
```

**Required parameters:**

* `client_id`: Your application's Client ID
* `response_type`: Set to `code`
* `redirect_uri`: Pre-registered callback URL
* `scope`: Requested permissions (include `openid` for OpenID Connect)
* `state`: Random string for CSRF protection (recommended)

**Example URL:**

```
https://www.make.com/oauth/v2/authorize?  client_id=your_client_id&  response_ty
```

{% endstep %}

{% step %}

#### User authorization

The user:

1. Logs into Make.com (if not already authenticated)
2. Reviews and approves the requested permissions
3. Gets redirected to your `redirect_uri` with an authorization code

**Callback URL format:**

```
https://yourapp.com/callback?code=authorization_code&state=random_state_strin
```

{% endstep %}

{% step %}

#### Exchange code for tokens

Make a server-side POST request to the token endpoint:

```
POST https://www.make.com/oauth/v2/token
```

**Required Parameters:**

* `client_id`: Your Client ID
* `client_secret`: Your Client Secret
* `grant_type`: Set to `authorization_code`
* `code`: Authorization code from Step 2

**Response:**

```json
json{  "access_token": "eyJ...",  "refresh_token": "eyJ...",  "id_token": "eyJ...",  "token_type": "Bearer",  "expires_in": 3600}
```

{% endstep %}

{% step %}

#### Refresh access token

When the access token expires, use the refresh token:

```
POST https://www.make.com/oauth/v2/token
```

**Required parameters:**

* `client_id`: Your Client ID
* `client_secret`: Your Client Secret
* `grant_type`: Set to `refresh_token`
* `refresh_token`: Refresh token from Step 3
  {% endstep %}
  {% endstepper %}
