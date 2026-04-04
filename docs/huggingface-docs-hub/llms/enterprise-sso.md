# Source: https://huggingface.co/docs/hub/enterprise-sso.md

# Single Sign-On (SSO)

> [!WARNING]
> This feature is part of the Team & Enterprise plans.

Single sign-on (SSO) allows organizations to securely manage user authentication through their own identity provider (IdP). Both SAML 2.0 and OpenID Connect (OIDC) protocols are supported.

Please note that this feature is intended to manage access to organization-specific resources such as private models, datasets, and Spaces. However, by default it does not replace the core authentication mechanism for the Hugging Face platform, meaning that users still need to login with their own HF account. To replace the core authentication, i.e. for enhanced capabilities like automated user provisioning (JIT/SCIM) and global SSO enforcement, see our [Advanced SSO documentation](./enterprise-hub-advanced-sso).

  
  

This feature allows organizations to:

- Enforce mandatory authentication through your company's IdP
- Automatically manage user access and roles based on your IdP attributes
- Support popular providers like Okta, OneLogin, and Azure Active Directory
- Maintain security while allowing external collaborators when needed
- Control session timeouts and role mappings

This Enterprise Hub feature helps organizations maintain consistent security policies while giving their teams seamless access to Hugging Face resources.

[Getting started with SSO →](./security-sso)

