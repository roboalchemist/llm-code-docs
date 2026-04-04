# Source: https://docs.gitguardian.com/nhi-governance/azure-entra-integration.md

# Microsoft Entra Integration

> Integrate Microsoft Entra ID with GitGuardian NHI Governance to collect identity, permission, and credential data using Workload Identity Federation.

# Microsoft Entra Integration

The Microsoft Entra integration provides comprehensive visibility into your Microsoft Entra ID (formerly Azure Active Directory) and Azure RBAC infrastructure, enriching your NHI governance with detailed identity, permission, and credential context.

## Overview

This integration is provided directly in **GitGuardian platform** and does not require to install GitGuardian Scout. It fetches comprehensive identity data from Microsoft Entra ID using Microsoft Graph API and collects Azure RBAC (Role-Based Access Control) data for specified Azure subscriptions. This enriches your security graph with detailed context about service principal credentials, their permissions, and potential blast radius in case of a leak.

## Key Features

- **Comprehensive Identity Discovery**: Fetches all Microsoft Entra data including users, groups, service principals, managed identities, and applications
- **Credential Tracking**: Discovers and tracks service principal credentials (client secrets and certificates)
- **Permission Analysis**: Maps directory roles and Azure RBAC permissions to service principals
- **Security Graph Enrichment**: Provides detailed context about credential sensitivity and blast radius
- **Secure Authentication**: Uses Workload Identity Federation (OIDC), eliminating the need for long-lived credentials

## Data Collected

### Microsoft Graph API Data (Identity Layer)

The integration collects the following identity information:

- **Users**: User profiles, account status, and metadata
- **Groups**: Group information, types, and memberships
- **Service Principals**: Service principal metadata and associations
- **Managed Identities**: System-assigned and user-assigned managed identities
- **Applications**: Application registrations and metadata
- **Client Secrets**: Metadata for service principal client secrets (values are never accessible)
- **Certificates**: Certificate metadata for service principals
- **Directory Roles**: Microsoft Entra directory role assignments

### Azure Management API Data (RBAC Layer)

When Azure subscription IDs are configured, the integration also collects:

- **Role Definitions**: Built-in and custom Azure RBAC role definitions with permission details
- **Role Assignments**: Role assignments for subscriptions and resources
- **Subscriptions**: List of accessible Azure subscriptions

## Required Permissions

### Microsoft Graph API Permissions

The following **Application permissions** are required for the registered application:

- `Application.Read.All`
- `Directory.Read.All` 
- `Group.Read.All`
- `GroupMember.Read.All`
- `User.Read.All`
- `AdministrativeUnit.Read.All` 

**Note**: These are **Application permissions** (not Delegated permissions), which work without a signed-in user and require admin consent.

### Azure Management API Permissions

For Azure RBAC data collection (optional but recommended):

- **Reader** role on each Azure subscription you want to monitor

This can be assigned at subscription level or management group level for multiple subscriptions.

## Getting Started

Follow these steps to configure the Microsoft Entra integration:

### Step 1: Register Application in Azure Entra

1. Sign in to the [Azure Portal](https://portal.azure.com)
2. Navigate to **Azure Active Directory** â **App registrations** â **New registration**
3. Provide a name (e.g., "GitGuardian NHI Integration")
4. Select **Accounts in this organizational directory only**
5. Click **Register**
6. **Save the following values:**
   - **Application (client) ID** - You'll need this for GitGuardian configuration
   - **Directory (tenant) ID** - You'll need this for GitGuardian configuration

### Step 2: Grant API Permissions

1. In your app registration, go to **API permissions**
2. Click **Add a permission**
3. Select **Microsoft Graph** â **Application permissions**
4. Add the following permissions:
   - `Application.Read.All`
   - `Directory.Read.All`
   - `Group.Read.All`
   - `GroupMember.Read.All`
   - `User.Read.All`
   - `AdministrativeUnit.Read.All`
5. Click **Grant admin consent** for your organization

**Important**: Application permissions require admin consent and work without a signed-in user.

### Step 3: Configure Workload Identity Federation (OIDC)

1. In your app registration, go to **Certificates & secrets**
2. Click the **Federated credentials** tab
3. Click **Add credential**
4. Select **Other issuer** as the federated credential scenario
5. Fill in the following fields:
   - **Issuer**: `https://api.gitguardian.com` (for SaaS) or your self-hosted instance URL
   - **Subject identifier**: `gitguardian-account-id:{your-gitguardian-account-id}`
   - **Name**: A descriptive name (e.g., "gitguardian-federation")
   - **Description**: Optional description
   - **Audience**: Leave as default (`api://AzureADTokenExchange`)
6. Click **Add**

![Configure Federated Credential](/img/nhi-governance/entra/entra_oidc_declaration.png)

**Finding your GitGuardian Account ID**: Your account ID can be found in your GitGuardian dashboard URL: `https://dashboard.gitguardian.com/workspace/{your-gitguardian-account-id}/`

**Example**: If your dashboard URL is `https://dashboard.gitguardian.com/workspace/123456/`, then your GitGuardian account ID is `123456`.

### Step 4: Assign Azure RBAC Permissions (Optional)

If you want to collect Azure RBAC data:

1. Navigate to **Subscriptions** in the Azure Portal
2. Select each subscription you want to monitor
3. Go to **Access control (IAM)** â **Add role assignment**
4. Select the **Reader** role
5. Assign it to your registered application (search by application name)
6. Save the **Subscription ID(s)** for GitGuardian configuration

### Step 5: Configure Integration in GitGuardian

1. In GitGuardian platform, navigate to **Settings > Sources**
2. Click **Add Integration**
3. Select **Microsoft Entra**
4. Provide the following information:
   - **Integration Name**: A friendly name for this integration instance
   - **Tenant ID**: Your Azure AD Directory (tenant) ID from Step 1
   - **Client ID**: Your Application (client) ID from Step 1
   - **Subscription IDs** (optional): Comma-separated list of Azure subscription IDs for RBAC data collection
5. Click **Save**

### Completion

You're all set! GitGuardian will start fetching Microsoft Entra data from your tenant, enriching your security graph with comprehensive identity and permission context.

Once the integration is active, you'll be able to view the enriched Microsoft Entra data in your GitGuardian platform. The NHI inventory will display all discovered entities including service principals, managed identities, client secrets, and certificates with comprehensive metadata.

![Microsoft Entra Identities in GitGuardian Inventory](/img/nhi-governance/entra/entra_dashboard.png)

Each service principal credential will have an enriched security graph showing:
- Which service principal owns the credential
- What directory roles and RBAC roles are assigned to that service principal
- Which groups the service principal belongs to (if any)
- Permission statements from Azure RBAC roles
- Credential validity period and expiration status

## Integration Instances

This integration supports **multiple instances**, allowing you to:
- Monitor multiple Azure AD tenants from a single GitGuardian account
- Separate production and development environments
- Track different organizational units with different tenant configurations

Each integration instance is configured independently with its own tenant ID, client ID, and subscription list.

## Security Considerations

- **No Long-Lived Secrets**: The integration uses Workload Identity Federation, eliminating the need for client secrets
- **Read-Only Access**: All permissions are read-only; the integration cannot modify your Azure environment
- **Short-Lived Tokens**: Access tokens are automatically managed and expire within 1 hour
- **Credential Metadata Only**: Secret values are never accessible through Microsoft Graph API
- **Least Privilege**: Only the minimum required permissions are requested

## Troubleshooting

### Common Issues

**"Insufficient privileges" error:**
- Ensure all required Microsoft Graph API permissions are granted
- Verify admin consent has been granted for application permissions

**"Invalid federated credential" error:**
- Verify the Issuer URL matches your GitGuardian instance (SaaS vs. self-hosted)
- Confirm the Subject identifier format: `gitguardian-account-id:{your-account-id}`
- Check that your GitGuardian account ID is correct

**RBAC data not appearing:**
- Verify Subscription IDs are correctly entered in the integration configuration
- Confirm the Reader role is assigned to your application on each subscription
- Check that the subscriptions are active

**Federated credential not working:**
- Ensure you're using Application permissions (not Delegated permissions)
- Verify the federated credential is added under "Certificates & secrets" â "Federated credentials"
- Check that the credential hasn't expired (federated credentials can have expiration dates)

## Additional Resources

- [Microsoft Entra Workload Identity Federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)
- [Microsoft Graph API Permissions Reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [Azure RBAC Documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/)

## Other Integrations

For information about other integrations including secrets managers, CI/CD systems, and infrastructure sources, please refer to the **[ggscout documentation](/docs/ggscout-docs/integrations.md)**.
