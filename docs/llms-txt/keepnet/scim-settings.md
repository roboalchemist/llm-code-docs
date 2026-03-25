# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings.md

# SCIM Settings

The SCIM (system for cross-domain identity management) is a standard for automating the exchange of user identity information between identity platforms. The platform supports SCIM integration to automate and synchronize target user information from the identity providers to the platform.

## Shortcuts

* [Getting Started](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/getting-started-with-scim)
* [How to integrate Azure AD SCIM](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/azure-ad-scim-integration)
* [How to integrate Okta SCIM](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/okta-scim-integration)
* [How to integrate Onelogin SCIM](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/onelogin-scim-integration)
* [How to integrate JumpCloud SCIM](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/jumpcloud-scim-integration)

## FAQ

### Q: Can I integrate not listed Identity Provider over SCIM on the platform?

A: Yes, by getting help from the documents that the identity provider provides, the SCIM settings can be configured correctly on the identity provider to synchronize users to the platform.

### Q: Where can I find the SCIM endpoint URL address?

A: The SCIM endpoint URL of the platform is <https://scim-api.keepnetlabs.com/scim>

### Q: Under what conditions are target users synced via SCIM set to an "Inactive" status or deleted permanently?

A: When an admin removes a user from the SCIM application, the user will be set to "Inactive" on the platform. However, if an admin permanently deletes the user from their identity provider, the user will be deleted from the platform as well.
