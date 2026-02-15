# Source: https://developer.zendesk.com/documentation/api-basics/

# Zendesk Authentication & OAuth - Complete Guide

Comprehensive guide to securing API access with API tokens and OAuth 2.0.

## Authentication Methods

Zendesk supports two primary authentication mechanisms:

1. **API Token** - Simple, suitable for server-to-server
2. **OAuth 2.0** - Recommended for third-party apps and user delegation

## API Token Authentication

### Creating an API Token

**Via Admin Panel:**
1. Go to Admin → Apps and integrations → APIs
2. Click "Create API Token"
3. Name the token (descriptive)
4. Note the token value (save securely)
5. Enable/disable as needed

**Via API:**

```bash
# Requires existing authentication
POST /api/v2/api_tokens
{
  "api_token": {
    "description": "Integration Token",
    "active": true
  }
}
```

### Using API Token

**Basic Authorization Header:**

```bash
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
  https://yoursubdomain.zendesk.com/api/v2/tickets

# Alternative: Basic Auth
curl -u email@example.com/token:YOUR_API_TOKEN \
  https://yoursubdomain.zendesk.com/api/v2/tickets
```

**With Email (Required Format):**

```bash
# Email/Token method
Authorization: Bearer email@example.com/token:YOUR_API_TOKEN

# Bearer Token method (if using email prefix)
Authorization: Bearer YOUR_API_TOKEN
```

### Token Security

- **Storage**: Save in secure credential storage (not code)
- **Rotation**: Rotate periodically
- **Scope**: Use account level for full access
- **Monitoring**: Track token usage
- **Revocation**: Delete unused tokens

### Managing API Tokens

```bash
# List tokens
GET /api/v2/api_tokens

# Revoke token
DELETE /api/v2/api_tokens/{id}

# Update token
PUT /api/v2/api_tokens/{id}
{
  "api_token": {
    "active": false
  }
}
```

## OAuth 2.0 Authentication

### Overview

OAuth 2.0 is recommended for:
- Third-party applications
- Mobile apps
- Web applications with user delegation
- Scoped access control
- User authorization workflows

### OAuth Flows

#### Authorization Code Flow (Recommended)

Best for web applications and desktop apps.

**1. Redirect User to Authorization:**

```
https://yoursubdomain.zendesk.com/oauth/authorizations/new?
  client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/oauth/callback
  &scope=read%20write
  &response_type=code
  &state=random_state_value
```

**2. User Logs In & Grants Permission**

User sees authorization screen showing:
- Your application name
- Scopes being requested
- Option to grant/deny

**3. Authorization Code Returned**

Browser redirects with authorization code:

```
https://yourapp.com/oauth/callback?
  code=auth_code_123
  &state=random_state_value
```

**4. Exchange Code for Token**

Backend request:

```bash
POST https://yoursubdomain.zendesk.com/oauth/tokens
{
  "grant_type": "authorization_code",
  "code": "auth_code_123",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "redirect_uri": "https://yourapp.com/oauth/callback"
}

Response:
{
  "access_token": "token_abc123",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh_abc123",
  "scope": "read write"
}
```

**5. Use Access Token**

```bash
curl -H "Authorization: Bearer token_abc123" \
  https://yoursubdomain.zendesk.com/api/v2/tickets
```

**6. Refresh Expired Token**

```bash
POST https://yoursubdomain.zendesk.com/oauth/tokens
{
  "grant_type": "refresh_token",
  "refresh_token": "refresh_abc123",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}

Response:
{
  "access_token": "new_token_xyz789",
  "expires_in": 3600,
  "refresh_token": "new_refresh_xyz789"
}
```

#### Implicit Flow (Legacy)

For single-page applications (SPAs). Less secure than Authorization Code.

```
https://yoursubdomain.zendesk.com/oauth/authorizations/new?
  client_id=YOUR_CLIENT_ID
  &redirect_uri=https://yourapp.com/callback
  &response_type=token
  &scope=read
```

Returns token directly in URL:

```
https://yourapp.com/callback#
  access_token=token_123
  &token_type=Bearer
  &expires_in=3600
  &scope=read
```

### OAuth Scopes

Control what access the application has:

```
read      # Read-only access to resources
write     # Create and modify resources
delete    # Delete resources
execute   # Execute bulk operations
```

**Common Scope Combinations:**

- `read` - Read tickets, users, organizations
- `read write` - Full CRUD access
- `read write delete` - Full access including deletion
- Granular scopes available for fine-grained control

### Creating OAuth Credentials

**Web Application:**

1. Admin → Apps and integrations → OAuth clients
2. Click "Create OAuth Client"
3. Application name: "My Ticketing App"
4. Redirect URL: `https://myapp.com/oauth/callback`
5. Scopes: `read write`
6. Save credentials securely

**Application Registration Response:**

```json
{
  "client_id": "123456789",
  "client_secret": "abc123def456ghi789jkl",
  "redirect_uris": ["https://myapp.com/oauth/callback"]
}
```

### Token Information

Get information about current token:

```bash
GET /oauth/token_info
{
  "access_token": "token_123",
  "token_type": "Bearer",
  "expires_in": 2400,
  "scope": "read write",
  "zendesk_user": {
    "id": 123,
    "email": "user@example.com"
  }
}
```

### Token Revocation

```bash
POST /oauth/revoke
{
  "token": "token_abc123"
}
```

## PKCE (Proof Key for Exchange)

Enhanced security for mobile and desktop apps.

### Flow

**1. Generate Code Verifier & Challenge:**

```
code_verifier = random(43-128 characters)
code_challenge = base64url(sha256(code_verifier))
```

**2. Authorization Request with Challenge:**

```
GET /oauth/authorizations/new?
  client_id=YOUR_CLIENT_ID
  &redirect_uri=https://app.example.com/callback
  &scope=read
  &response_type=code
  &code_challenge=E9Mrozoa2owUedPyAPhnCXC_aF2guW5AJstw3zYpOm8
  &code_challenge_method=S256
```

**3. Token Exchange with Verifier:**

```bash
POST /oauth/tokens
{
  "grant_type": "authorization_code",
  "code": "auth_code_123",
  "client_id": "YOUR_CLIENT_ID",
  "code_verifier": "original_random_string_123456"
}
```

### Benefits

- No client secret required
- Resistant to authorization code interception
- Recommended for mobile and desktop apps

## Two-Factor Authentication (2FA)

When users have 2FA enabled, additional steps required:

```bash
# Initial request returns 2FA required
POST /api/v2/tickets
{
  "error": "Unauthorized",
  "description": "Two-factor authentication required"
}

# User provides 2FA code
curl -H "Authorization: Bearer token" \
  -H "X-Zendesk-2FA-Code: 123456" \
  https://yoursubdomain.zendesk.com/api/v2/tickets
```

## SSO Integration

When Single Sign-On (SSO) enabled:

```bash
# OAuth flow still works
# SSO credentials used for authorization
# User authenticated via SSO provider (Okta, Azure AD, etc.)
```

## API Rate Limiting

Rate limits apply per user/token:

**Standard Limits:**
- 200 requests per minute for most endpoints
- 60 requests per minute for Search API
- 40 requests per minute for Incremental Exports

**Tracking Limits:**

```bash
curl -i https://yoursubdomain.zendesk.com/api/v2/tickets

Response Headers:
X-RateLimit-Limit: 200
X-RateLimit-Remaining: 157
X-RateLimit-Reset: 1392033960
```

**Handling Rate Limits:**

```bash
# Check for 429 status
if (response.status === 429) {
  const resetTime = response.headers['x-ratelimit-reset'];
  const waitTime = resetTime - Date.now() / 1000;
  // Wait waitTime seconds before retrying
}
```

## Best Practices

### Token Management

- **Use OAuth for public apps** - More secure, user-authorized
- **Use API tokens for integrations** - Server-to-server trust
- **Rotate credentials regularly** - Every 90 days recommended
- **Use secrets management** - Environment variables, vaults
- **Never commit credentials** - Use .gitignore

### Security

- **Validate redirect URIs** - Prevent authorization code interception
- **Use PKCE for mobile apps** - Adds verification layer
- **Verify state parameter** - Prevent CSRF attacks
- **HTTPS only** - All OAuth flows must use HTTPS
- **Secure refresh tokens** - Store in secure storage

### Error Handling

```bash
# Invalid token
{
  "error": "invalid_grant",
  "error_description": "Invalid authorization code"
}

# Expired token
{
  "error": "unauthorized",
  "error_description": "Unauthorized"
}

# Insufficient scopes
{
  "error": "insufficient_scope",
  "error_description": "Required scopes: write"
}
```

### Implementation Examples

**Python:**

```python
import requests
from requests.auth import HTTPBasicAuth

# Using API Token
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.get(
  "https://yoursubdomain.zendesk.com/api/v2/tickets",
  headers=headers
)

# OAuth flow
token_url = "https://yoursubdomain.zendesk.com/oauth/tokens"
token_data = {
  "grant_type": "authorization_code",
  "code": code,
  "client_id": client_id,
  "client_secret": client_secret,
  "redirect_uri": redirect_uri
}
response = requests.post(token_url, json=token_data)
access_token = response.json()["access_token"]
```

**JavaScript/Node.js:**

```javascript
// Using API Token
const headers = {
  "Authorization": `Bearer ${apiToken}`
};
const response = await fetch(
  "https://yoursubdomain.zendesk.com/api/v2/tickets",
  { headers }
);

// OAuth flow
const tokenResponse = await fetch(
  "https://yoursubdomain.zendesk.com/oauth/tokens",
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      grant_type: "authorization_code",
      code: code,
      client_id: clientId,
      client_secret: clientSecret,
      redirect_uri: redirectUri
    })
  }
);
const { access_token } = await tokenResponse.json();
```

## Troubleshooting

### Common Issues

**"Invalid token"**
- Token expired or revoked
- Incorrect token value
- Wrong subdomain

**"Unauthorized"**
- Missing Authorization header
- Malformed header value
- User not authenticated (OAuth)

**"Invalid redirect_uri"**
- Mismatched redirect URI
- Typo in URI
- Not registered in OAuth client

**"insufficient_scope"**
- API call requires additional scopes
- Need to request new scopes in OAuth flow
- Token doesn't have required permission

## Resources

- [API Basics Guide](https://developer.zendesk.com/documentation/api-basics/)
- [OAuth Documentation](https://developer.zendesk.com/documentation/api-basics/authentication/oauth/)
- [API Tokens](https://developer.zendesk.com/documentation/api-basics/authentication/api-tokens/)
- [PKCE Implementation](https://developer.zendesk.com/documentation/api-basics/authentication/pkce/)
