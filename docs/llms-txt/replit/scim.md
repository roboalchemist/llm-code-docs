# Source: https://docs.replit.com/teams/identity-and-access-management/scim.md

# SCIM

> Learn how to set up and manage SCIM to simplify provisioning and managing user roles within your Replit Enterprise Team.

## Introduction

<Note>
  SCIM is available exclusively for Enterprise customers. Contact our sales team at [sales@replit.com](mailto:sales@replit.com) to enable this feature for your organization.
</Note>

System for Cross-domain Identity Management ([SCIM](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management)) is a standardized protocol that automates user provisioning and deprovisioning between your enterprise identity provider (IdP) and Replit.

The SCIM integration is built on the [WorkOS](https://workos.com/) platform, ensuring enterprise-grade reliability and security.

## Key Features

<CardGroup cols={2}>
  <Card title="Automated User Management" icon="user-plus">
    Automatically provision and deprovision users based on your IdP's directory
  </Card>

  <Card title="Role Synchronization" icon="shield">
    Keep user roles and permissions in sync with your organizational structure
  </Card>

  <Card title="Bulk Operations" icon="users">
    Efficiently manage large teams with bulk user operations
  </Card>

  <Card title="Major IdP Support" icon="plug">
    Direct integration with Azure AD, Okta, and other leading identity providers
  </Card>
</CardGroup>

## Benefits

SCIM integration provides several advantages for Enterprise teams:

* **Enhanced Security**: Leverage your existing identity management systems for robust access control
* **Simplified Administration**: Automatically manage team members through your identity provider
* **Efficient Onboarding**: Seamlessly provision large teams without manual intervention
* **Consistent Access Control**: Maintain uniform access policies across your organization

## Getting Started

<Steps>
  <Step title="Enable SCIM">
    Go to your **Organization Settings** > **Authentication** tab to enable SCIM for your Enterprise organization
  </Step>

  <Step title="Configure Your IdP">
    Access the SCIM onboarding portal directly from the Authentication settings page. The onboarding portal provides step-by-step instructions specific to your identity provider for synchronizing your user directory
  </Step>

  <Step title="Test Integration">
    Verify the connection by provisioning a test user
  </Step>

  <Step title="Go Live">
    Begin using SCIM for automated user management
  </Step>
</Steps>

## Best Practices

* Document role allocations for existing Replit users before enabling SCIM
* Configure groups for each Replit role, keeping in mind that users without a group will default to the **Viewer** role
* Test your configuration by provisioning a small group of users before enabling bulk provisioning
* Document your SCIM configuration for future reference

## FAQs

### What happens to users who already have accounts on replit.com before SCIM was setup?

When SCIM is enabled, existing users are handled in two ways:

1. **Users provisioned through SCIM**:
   * Their roles will be updated to match those provided by your IdP
   * These users can only be added, removed, or have their roles changed through your IdP
   * To ensure permissions remain synchronized, admins will no longer be able to edit roles or invite new users within Replit

2. **Users not provisioned through SCIM**:
   * These users remain unchanged and are considered "legacy" users
   * We do not automatically revoke access, to prevent accidental deprovisioning
   * Legacy users can be removed through the Replit interface by organization admins if needed

<Warning>
  After implementing SCIM, all users provisioned through your IdP must be managed through your identity provider to maintain synchronization. Only legacy users (those not provisioned through SCIM) can be deprovisioned directly in Replit.
</Warning>

### What roles can be provisioned with SCIM?

SCIM users can be assigned to three roles:

* **Admin**: Full access to organization settings and resources
* **Member**: Standard access to create and edit Replit Apps
* **Viewer**: Read-only access to published applications

We recommend using dedicated groups for each role. During the SCIM onboarding process, you can configure the mapping between your IdP groups and Replit roles. For example, you might map your "Engineering" group to the Member role and your "Stakeholders" group to the Viewer role.

For detailed information about role permissions, see [Groups & Permissions](/teams/identity-and-access-management/groups-and-permissions). To learn more about viewer access, see [Viewer Seats](/teams/identity-and-access-management/viewer-seats).

### What if I need to edit the role mapping later?

Organization admins can edit SCIM configuration at any time by navigating to **Organization Settings** > **Authentication** > **SCIM**. Here you can access the SCIM portal to update group mappings and manage your integration settings.

## Related Resources

<CardGroup cols={2}>
  <Card title="SAML SSO" icon="key" href="/teams/identity-and-access-management/saml">
    Learn about SAML single sign-on integration
  </Card>

  <Card title="Groups & Permissions" icon="shield" href="/teams/identity-and-access-management/groups-and-permissions">
    Understand how to manage user roles and access
  </Card>
</CardGroup>
