# Source: https://developers.make.com/api-documentation/authentication/oauth-flow/token-expiration.md

# Token expiration

To ensure security and support proper token rotation, the tokens issued during the OAuth flow have the following defined expiration periods:

### **Access token: 5 minutes**

The Access token has a short lifespan and is intended for immediate use. It is  recommended to refresh the token to obtain a new access token when the current one expires.

### **Refresh token: 6 months**

The Refresh token provides long-term access without requiring the user to re-authorize frequently. The Refresh token should be securely stored and used to acquire new access tokens. In case of a token leak or compromise, the Refresh token can be immediately revoked by from your user profile in the **API access** section.

### **Authorization code: 5 minutes**

The Authorization code is intended for single-use and must be exchanged for an Access token and Refresh token within it's expiration window.
