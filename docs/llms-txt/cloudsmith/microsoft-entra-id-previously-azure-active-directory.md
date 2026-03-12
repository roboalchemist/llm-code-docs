# Source: https://help.cloudsmith.io/docs/microsoft-entra-id-previously-azure-active-directory.md

# SCIM with Microsoft Entra ID (previously Azure Active Directory)

Setting Up SCIM with Microsoft Entra ID

SCIM, or System for Cross-domain Identity Management, is an open standard designed to manage user identity information. Cloudsmith is SCIM 2.0-compliant. With Cloudsmith's support for SCIM, you can automatically provision new users, de-provision existing users, and update existing users' profile information based on changes within your Identity Provider (IdP).

To begin using SCIM, you need to enable the SCIM functionality in the [Cloudsmith Workspace Settings](https://help.cloudsmith.io/docs/organisations#scim)

Follow these steps:

1. Navigate to the Cloudsmith Workspace Settings.
2. Navigate to the Authentication Section, then click on the SCIM option. Enable the SCIM functionality by selecting "Allow SCIM."

After enabling SCIM, proceed with the setup process by following the instructions in Microsoft Entra ID's Getting Started Guide. You can find detailed instructions on their support page for SCIM Connectors: [Microsoft Entra SCIM Connector Documentation.](https://learn.microsoft.com/en-us/entra/architecture/sync-scim).

<Image align="center" src="https://files.readme.io/ef96dfb04a805ababf1ccb6d14708e2111d16f5f1a637beea546546b4bd9d409-scim-steps.png" />