# Source: https://www.apollographql.com/docs/graphos/platform/access-management/scim.md

# SCIM Provisioning Overview

GraphOS provides automated user management capabilities through the System for Cross-domain Identity Management (SCIM) protocol. SCIM automates user and group management by integrating your identity provider (IdP) with GraphOS.

## Supported SCIM operations

* **Provisioning:** Automatically create new GraphOS users when they are added to your IdP
* **Deprovisioning:** Automatically remove users from GraphOS when they are removed from your IdP
* **Attribute updates:** Sync user attributes (such as name and email) from your IdP to GraphOS
* **GraphOS role assignment:** Assign users GraphOS roles based on IdP group membership

  You can also assign GraphOS roles based on groups in your IdP [via your SSO configuration](https://www.apollographql.com/docs/graphos/platform/access-management/sso/overview#role-assignment).
  Apollo recommends using *either* SCIM or SSO for role assignment. If you use both, role assignments will overwrite one another.

## Prerequisites

* Only GraphOS [Org admins](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/#organization-wide-member-roles) can set up SCIM.
* You must have administrative access to your identity provider (IdP).
* You must configure [SSO](https://www.apollographql.com/docs/graphos/platform/access-management/sso/overview) before configuring SCIM.

## Setup instructions

To set up SCIM, follow the instructions for your configuration method:

* [Okta](https://www.apollographql.com/docs/graphos/platform/access-management/scim/okta)
* [Microsoft Entra ID](https://www.apollographql.com/docs/graphos/platform/access-management/scim/microsoft-entra-id)

If you use another identity provider, the setup instructions are generally similar to those provided above for Okta.

If you encounter any issues or need assistance, please email [support@apollographql.com](mailto:support@apollographql.com)—we're here to help!
