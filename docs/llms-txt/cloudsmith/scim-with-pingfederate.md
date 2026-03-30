# Source: https://help.cloudsmith.io/docs/scim-with-pingfederate.md

# SCIM with PingFederate

Setting Up SCIM with PingFederate

SCIM, or System for Cross-domain Identity Management, is an open standard designed to manage user identity information. Cloudsmith is SCIM 2.0-compliant. With Cloudsmith's support for SCIM, you can automatically provision new users, de-provision existing users, and update existing users' profile information based on changes within your Identity Provider (IdP).

To begin using SCIM, you need to enable the SCIM functionality in the [Cloudsmith Workspace Settings](https://help.cloudsmith.io/docs/organisations#scim)

Follow these steps:

1. Navigate to the Cloudsmith Workspace Settings.
2. Navigate to Authentication >> SCIM and enable the SCIM functionality by selecting "Allow SCIM."

<Image align="center" src="https://files.readme.io/d09aad44bccec4d78046752b2e2c223729431e2f5075cf2cefb78c8310bc9fa3-scim-steps.png" />

After enabling SCIM, proceed to PingFederate's Getting Started Guide to complete the setup process. Follow the detailed instructions on their support page for SCIM Connectors: [Ping Federate SCIM Connector Documentation](https://docs.pingidentity.com/r/en-us/pingfederate-scim-connector/pingfederate_scim_connector).