# Source: https://help.cloudsmith.io/docs/jumpcloud.md

# SCIM with JumpCloud

Setting Up SCIM with JumpCloud

SCIM, or System for Cross-domain Identity Management, is an open standard designed to manage user identity information. Cloudsmith is SCIM 2.0-compliant. With Cloudsmith's support for SCIM, you can automatically provision new users, de-provision existing users, and update existing users' profile information based on changes within your Identity Provider (IdP).

> 🚧 Early Access
>
> SCIM integration with JumpCloud is currently available in early access

To begin using SCIM, you need to enable the SCIM functionality in the [Cloudsmith Workspace Settings](https://help.cloudsmith.io/docs/organisations#scim)

Follow these steps:

1. Navigate to the Cloudsmith Workspace Settings.
2. Navigate to Authentication >> SCIM and enable the SCIM functionality by selecting "Allow SCIM."

<Image align="center" src="https://files.readme.io/33a9e7ca325096db9b79c309c47d0ee3fd2741eeac422518b5790d964051833a-scim-steps.png" />

After enabling SCIM, proceed to JumpCloud's Getting Started Guide to complete the setup process. Follow the detailed instructions on their support page for Identity Management Connectors: [JumpCloud Getting Started Guide](https://jumpcloud.com/support/get-started-identity-management-connectors).