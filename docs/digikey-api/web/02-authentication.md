# Digi-Key API Authentication

## OAuth 2.0 Overview

Digi-Key uses OAuth 2.0 Authorization Code Grant for API access. This guide covers the complete authentication flow.

## Prerequisites

1. **Developer Account**: Create at https://developer.digikey.com/
2. **Registered Application**: Register your app to receive:
   - Client ID
   - Client Secret
3. **Redirect URI**: Configure where OAuth provider redirects after authorization

## Authentication Flow

### Step 1: Authorization Request

User is redirected to Digi-Key's authorization endpoint:

```
GET https://api.digikey.com/oauth
  ?client_id=YOUR_CLIENT_ID
  &redirect_uri=YOUR_REDIRECT_URI
  &response_type=code
  &scope=products:search products:details
```

User logs in and grants permission to your application.

### Step 2: Authorization Code Callback

After user authorizes, Digi-Key redirects to your redirect_uri with authorization code:

```
https://your-app.com/callback?code=AUTH_CODE&state=STATE_VALUE
```

### Step 3: Token Exchange

Exchange authorization code for access token:

```bash
curl -X POST https://api.digikey.com/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=AUTH_CODE" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "redirect_uri=YOUR_REDIRECT_URI"
```

### Step 4: Access Token Response

Successful response includes:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh_token_here"
}
```

## Using Access Token

Include in API requests as Bearer token:

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  https://api.digikey.com/products/v4/PRODUCT_NUMBER
```

## Token Refresh

When access token expires, use refresh token:

```bash
curl -X POST https://api.digikey.com/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=YOUR_REFRESH_TOKEN" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET"
```

## API Scopes

Available OAuth scopes:

| Scope | Purpose |
|-------|---------|
| `products:search` | Search product catalog |
| `products:details` | Retrieve product specifications |
| `orders:read` | View order history |
| `orders:write` | Create and modify orders |

## Best Practices

1. **Never hardcode credentials** - Use environment variables
2. **Store tokens securely** - Use encrypted storage for refresh tokens
3. **Handle token expiration** - Implement automatic refresh
4. **Implement PKCE** - For mobile/SPA applications
5. **Validate state parameter** - Prevent CSRF attacks

## Security Considerations

- Use HTTPS for all OAuth requests
- Validate redirect URI matches registered value
- Keep client secret confidential
- Implement proper CSRF protection
- Monitor token usage for anomalies

## Troubleshooting

### Invalid Client ID
Ensure client ID matches registered application in Digi-Key developer portal.

### Invalid Redirect URI
Redirect URI must exactly match configuration in developer portal (including protocol and query parameters).

### Expired Token
Implement token refresh logic to automatically renew before expiration.

### Scope Issues
Verify requested scopes match those authorized for your application.

---

**Source**: Digi-Key Developer Portal Authentication Docs
**Last Updated**: 2026-01-08
