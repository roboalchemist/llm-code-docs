<!-- Source: https://namespace.so/docs/workspaces/access -->

# Workspace Access Controls

Namespace provides comprehensive access control mechanisms to help you manage who can access your workspace and what actions they can perform.
This page explains the available authentication methods, role-based access controls, and member management features.

## Authentication Methods

Namespace supports multiple authentication methods to accommodate different organizational requirements and security policies.

### Social Login Options

**Google SSO**: Members can sign in using their Google accounts, providing seamless integration with Google Workspace environments.

**GitHub SSO**: Authenticate using GitHub credentials, ideal for development teams already using GitHub for version control.

### Enterprise Authentication

**SAML SSO**: Available for enterprise customers, SAML single sign-on provides integration with your organization's identity provider such as Okta, OneLogin, or Auth0.

Enterprise customers can configure advanced SAML SSO options for enhanced security and user management:

#### Automatic Workspace Joining

Configure your SAML SSO integration to automatically grant workspace access to any member from your organization who authenticates through your identity provider.
You can configure a default role that new members assume on workspace signup.
This streamlines onboarding and ensures all team members have appropriate access.

#### Enforced SSO Authentication

Enhance security by requiring all workspace members to sign in exclusively through your organization's identity provider, ensuring consistent security policies across your organization.
When this option is enabled, social login methods (Google and GitHub) are disabled for all workspace members.

#### Custom Session Durations

Configure custom session durations for SAML SSO logins to meet your organization's security requirements.
Once the maximum session length (default is one hour) is reached, re-authentication is required.
Namespace also supports different session policies for different user roles.

## Adding Members

You can invite new members to your workspace manually using two convenient methods.
Any invite expires after a week unless revoked by the inviter ahead of time.
If your workspace is connected to your organization's identity provider, you can also grant workspace access to [any member from your organization](#automatic-workspace-joining).

### Invite Links

1. Navigate to your [workspace settings](https://cloud.namespace.so/workspace/settings/users)
2. Choose "Generate link"
3. Share the link with the new workspace member

Invite links become invalid after a user accepts the invite.

### Invite Emails

1. Navigate to your [workspace settings](https://cloud.namespace.so/workspace/settings/users)
2. Choose "Invite by email"
3. Enter the email addresses to invite

## Role-Based Access Control (RBAC)

Namespace supports comprehensive role-based access control with five distinct roles, each providing different levels of access and permissions:

### Supported Roles

- **Owner**: Full administrative control, main contact point, cannot be removed from the workspace
- **Admin**: Full administrative control
- **Editor**: Can modify workspace content and configurations
- **Accountant**: Access to billing and usage information
- **Reader**: View-only access to workspace resources

Only business and enterprise accounts have full access to RBAC.
For a full overview of the features included in each plan, visit [the pricing page](https://namespace.so/pricing).

### Role Permissions Matrix

| Action | Owner | Admin | Editor | Accountant | Reader |
| --- | --- | --- | --- | --- | --- |
| User management | Allowed | Allowed | Not allowed | Not allowed | Not allowed |
| Billing and Plan | Allowed | Allowed | Not allowed | Allowed | Not allowed |
| Connect GitHub organizations | Allowed | Allowed | Not allowed | Not allowed | Not allowed |
| Delete a Workspace | Allowed | Allowed | Not allowed | Not allowed | Not allowed |
| View Audit Logs | Allowed | Allowed | Not allowed | Not allowed | Not allowed |
| Notification settings | Allowed | Allowed | Not allowed | Not allowed | Not allowed |
| Start Builds & Instances | Allowed | Allowed | Allowed | Not allowed | Not allowed |
| Release Cache Volumes | Allowed | Allowed | Allowed | Not allowed | Not allowed |
| SSH/VNC | Allowed | Allowed | Allowed | Not allowed | Not allowed |
| View Instances | Allowed | Allowed | Allowed | Allowed | Allowed |
| View Builds | Allowed | Allowed | Allowed | Allowed | Allowed |
| View GitHub Actions | Allowed | Allowed | Allowed | Allowed | Allowed |
| Usage explorer | Allowed | Allowed | Allowed | Allowed | Allowed |
| Access previews | Allowed | Allowed | Allowed | Allowed | Allowed |

## Workload Access

Each [compute instance](/docs/architecture/compute) receives a dedicated workload token, granting access to Namespace features and APIs.
The token uniquely identifies the instance ensuring any entry in our immutable [audit log](/docs/workspaces/security#audit-logs) can be traced back to the source.
By default, workload tokens allow access to any Namespace feature, enabling frictionless feature composition.
These permissions can be dynamically configured, allowing enterprise customers to enforce fine-grained access policies on which features may be accessed.

## Support and Configuration

For assistance with configuring advanced access controls or enterprise SSO integration, contact our [support team](mailto:support@namespace.so).
Our team can help with SAML SSO setup, custom authentication requirements, and security policy implementation.

Last updated March 11, 2026
