# Source: https://developers.make.com/api-documentation/authentication/oauth-flow/authorization-code-flow-with-pkce-public-clients.md

# Authorization code flow with PKCE (public clients)

**Use this flow when:** Your application cannot securely store secrets (SPAs, mobile apps).

**Note:** This flow typically does not provide refresh tokens for security reasons.

{% stepper %}
{% step %}

#### Generate PKCE parameters

Before starting authorization, generate:

1. **Code Verifier**: Random string (43-128 characters)
2. **Code Challenge**: SHA256 hash of code\_verifier, Base64url encoded (no padding)

**Example (JavaScript):**

```javascript
javascript// Generate code verifierconst codeVerifier = generateRandomString(128);// Generate code challengeconst codeChallenge = base64URLEncode(sha256(codeVerifier));
```

{% endstep %}

{% step %}

#### Redirect user for authorization

Redirect to the authorization endpoint with PKCE parameters:

```
GET https://www.make.com/oauth/v2/authorize
```

**Required parameters:**

* `client_id`: Your Client ID
* `response_type`: Set to `code`
* `redirect_uri`: Pre-registered callback URL
* `scope`: Requested permissions
* `state`: Random string for CSRF protection
* `code_challenge`: Generated in Step 1
* `code_challenge_method`: Set to `S256`
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

Make a POST request (can be from frontend or backend):

```
POST https://www.make.com/oauth/v2/token
```

**Required Parameters:**

* `client_id`: Your Client ID
* `grant_type`: Set to `authorization_code`
* `code`: Authorization code from Step 3
* `code_verifier`: Original code verifier from Step 1

**Response:**

```json
json{  "access_token": "eyJ...",  "id_token": "eyJ...",  "token_type": "Bearer",  "expires_in": 3600}
```

{% endstep %}
{% endstepper %}
