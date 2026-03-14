# Source: https://developers.make.com/api-documentation/authentication/oauth-flow.md

# OAuth 2.0 flow in the Make API

This guide explains how to integrate Make into your application using OAuth 2.0 authorization. For general OAuth 2.0 concepts, refer to the [OAuth 2.0 protocol specification](https://oauth.net/2/).&#x20;

Before implementing OAuth 2.0, you must [register your OAuth 2.0 client](https://developers.make.com/api-documentation/authentication/requesting-an-oauth-2.0-client) with Make's authorization server to obtain:

* **Client ID** (required for all clients)
* **Client Secret** (only for confidential clients)

#### Supported protocols

* **OIDC (OpenID Connect)**: Simplified user authentication
* **PKCE (Proof Key for Code Exchange)**: Enhanced security for public clients (**mandatory** for SPAs and mobile apps)

#### API Endpoints

<table><thead><tr><th width="161.43359375">Endpoint</th><th>URL</th></tr></thead><tbody><tr><td>Authorization</td><td><a href="https://www.make.com/oauth/v2/authorize">https://www.make.com/oauth/v2/authorize </a></td></tr><tr><td>Token</td><td><a href="https://www.make.com/oauth/v2/token">https://www.make.com/oauth/v2/token</a></td></tr><tr><td>JWKS URI</td><td><a href="https://www.make.com/oauth/v2/oidc/jwks">https://www.make.com/oauth/v2/oidc/jwks</a></td></tr><tr><td>User info</td><td><a href="https://www.make.com/oauth/v2/oidc/userinfo">https://www.make.com/oauth/v2/oidc/userinfo </a></td></tr><tr><td>Revocation</td><td><a href="https://www.make.com/oauth/v2/revoke">https://www.make.com/oauth/v2/revoke </a></td></tr><tr><td>OpenID discovery</td><td><a href="https://www.make.com/.well-known/openid-configuration">https://www.make.com/.well-known/openid-configuration</a></td></tr></tbody></table>
