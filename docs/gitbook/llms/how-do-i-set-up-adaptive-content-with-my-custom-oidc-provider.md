# Source: https://gitbook.com/docs/help-center/published-documentation/adaptive-content/how-do-i-set-up-adaptive-content-with-my-custom-oidc-provider.md

# How do I set up Adaptive content with my custom OIDC provider?

Adaptive content works with any identity provider

#### **Using OIDC Integration**

1. Set up the Generic OIDC integration in GitBook
2. Configure your OIDC provider to include custom claims in tokens
3. Map these claims in your GitBook visitor schema
4. The specific claim format depends on your provider's implementation

#### **Common Issues:**

* **Claim scopes:** Ensure your OIDC provider includes custom claims in the token (not just standard OIDC claims)
* **Claim structure:** Custom claims may be nested under provider-specific properties
* **Token validation:** Verify your provider's tokens are properly formatted
* **Provider-Specific Notes:** Different OIDC providers structure custom claims differently. Check your provider's documentation for how to include custom claims in ID tokens.
