# Source: https://docs.acceldata.io/documentation/service-users.md

# Service Users

Service Users provide secure, non-human identities for automated access and integrations. They are designed to replace personal user–based API keys, ensuring uninterrupted connectivity and improved access control for system-to-system communication.

They operate independently of individual user accounts, removing the risk of access loss when a user leaves the organization or their account is deactivated. Each Service User has its own lifecycle, permissions, and API keys, enabling administrators to centrally control and audit all automated connections.

**Benefits:**

- Prevents downtime caused by expired or deleted personal API keys
- Enables secure, auditable API access
- Supports role-based permissions for automation accounts
- Simplifies access governance at the tenant level

## Accessing Service Users

To access **Service Users:**

1. Navigate to **Settings &gt; User Management and Access**.
2. Select **Service Users**.
3. The **Service Users** page displays all existing service accounts, including their:
    1. **Name**
    2. **Status** (Active or Disabled)
    3. **Roles** (Tenant-level roles assigned)
    4. **Number of API Keys**
    5. **Created By** and **Created On** details

From this page, administrators can create new Service Users, view existing ones, and manage associated API keys.

## Creating a Service User

1. Click **Create** in the Service Users page.
2. Enter a **name** for the new service account (for example, `dataplane-v1`).
3. Assign a **Tenant-level role** such as Viewer, Editor, or Admin.
4. Click **Save** to create the Service User.

Once created, the Service User appears in the list with its assigned role and creation details.

Note Service Users currently support **Tenant-level roles** only. Domain roles and user group assignments are not yet available.

## Managing API Keys

Each Service User can have one or more API keys associated with it. Administrators can:

- **Generate API Keys:** Create a new key for authentication.
- **Set Expiry:** Optionally define an expiration date for the key.
- **Download Key:** Keys can be downloaded once at the time of creation.
- **Revoke or Regenerate Keys:** Disable or regenerate keys as needed to maintain security.

Once revoked, API keys will lose access shortly after revocation.

## Audit and Security Controls

All Service User–related activities are captured in the **Audit Logs**, including:

- Account creation and deletion
- Role changes
- API key creation, download, and revocation

Administrators can enable or disable Service Users at any time, and access will be revoked shortly after the change.