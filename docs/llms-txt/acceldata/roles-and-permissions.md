# Source: https://docs.acceldata.io/documentation/roles-and-permissions.md

# Roles and Permissions

**Roles and Permissions** in ADOC provide fine-grained access control to ensure each user or group can only perform actions necessary for their responsibilities.
 With Roles & Permissions, administrators can:

- Define global (tenant-level) roles for platform-wide access
- Create domain-specific roles for scoped control within projects or business units
- Assign permissions for Create, Modify, and View actions across key features
- Maintain security, compliance, and auditability through structured access policies

Proper role design is essential for minimizing security risks and ensuring smooth workflows.

## 1. Tenant Roles

Tenant roles define platform-wide access controls and are typically used by administrators to assign structured permissions across ADOC. These roles determine what users and groups can see and do at a global level—spanning multiple modules such as **Compute**, **Alerts**, and **Reliability**.

The **Tenant Roles** tab provides an overview of all existing roles along with key details for each. It displays the **role name** (e.g., tenant_admin, viewer, owner), **the number of users and groups assigned to each role** (e.g., Users: 5, Groups: 1), and metadata such as **who created the role** and **who last updated it** and when—useful for auditing and tracking changes over time.

### Creating a Tenant Role

To define a new platform-wide role:

1. Go to the **Tenant Roles** tab.
2. Click **Create Tenant Role**.
3. Enter a unique role name and an optional description.
4. Choose permissions by category (e.g., Administration, Compute, Pipeline).
5. For each category, select applicable actions: **Create**, **Modify**, or **View**.
6. Click **Save**.

The new role will now be listed in the Tenant Roles table, ready to assign to users or groups.

### Tenant Role Detail View

Clicking on a tenant role opens a panel on the right-hand side that displays all role-specific details.

- **Permissions Section**: Permissions are grouped under categories such as:
    - **Administration** – includes User Management, API Keys, Billing, and Account Configuration.
    - **Alerts** – covers permissions related to alerts management.

You can view the assigned access levels for each feature (Create, Modify, View) within these categories.

- **Activity Section**: This section helps with audit tracking and includes:
    - **Created By / On** – identifies who created the role and the date/time it was created.
    - **Last Updated By / On** – shows who last modified the role and when the update occurred.

You can **Edit** or **Delete** the tenant role directly from this panel using the buttons at the top.

## 2. Domain Roles

**Domain Roles** enable fine-grained access control for specific resources like assets, reports, and domains. These roles are used to manage permissions at the domain level, making them ideal for teams working on specific projects or business units.

The **Domain Roles** tab lists all domain-level roles along with essential metadata for each. It includes the **Role Name** (e.g., asset_viewer, report_admin, domain_editor), the number of **Domain User Groups** assigned to that role, the **Created By** field showing who originally created the role, and the **Last Updated By** and **Last Update At** fields indicating who last modified it and when—useful for audit trails and change tracking.

### Creating a Domain Role

Admins can create domain roles to define permissions related to specific domains or domain-bound features.

Steps:

1. Navigate to **the Domain Roles** tab.
2. Click **Create Domain** Role.
3. Enter a **Role Name** (required) and optionally, a **Description** to clarify the role’s purpose.
4. In the **Permissions** section, browse through the following categories:
    1. **Asset Management** – control access to metadata, assets, and lineage.
    2. **Domain Management** – manage domain settings and configurations.
    3. **Report Management** – handle permissions for creating, modifying, and viewing reports.

5. For each feature within a category, select the appropriate access levels:
    1. **Create**
    2. **Modify**
    3. **View**

6. Click **Save** to finalize the role.

### Domain Role Detail Panel

When you click on a domain role, a detailed panel appears on the right side. This view provides a comprehensive breakdown of the role's configuration:

- **Permissions Overview**: 
    - Displays the permission categories and the access levels (Create, Modify, View) assigned to each.
    - You can review these permissions but not modify them directly in this view.

- **Domain User Groups**:
    - Lists all user groups that are currently assigned this domain role.
    - Helps you understand how the role is being used across teams.

- **Activity**:
    - **Created By / On** – Displays who created the role and when.
    - **Last Updated By / On** – Indicates who last modified the role and the timestamp of the change
    - Useful for compliance, auditing, and tracking role evolution over time.

You can **Edit** or **Delete** the domain role directly from this panel using the buttons at the top.

## Permission Categories and Features

ADOC permissions span six key areas. Each permission can be assigned the actions **Create**, **Modify**, or **View**.

| **Category** | **Feature** | **Description** | 
| ---- | ---- | ---- | 
| Pipeline | Pipeline | Create and manage pipelines and pipeline monitors | 
| Compute | Chargeback, Monitors | Budgeting and compute usage insights | 
| Reliability | Assets, Policies, KPIs | Manage data reliability and lineage | 
| Alerts | Alerts | Configure and monitor alerting | 
| Administration | User, API Keys | User and platform setup | 
| General | Data Source, Tags, Audit Logs | General platform management | 


> Assign view permissions broadly within categories to avoid internal dependency issues and UI limitations.

---

## Best Practices

- **Bundle permissions logically.** Assign Modify + View or Create + View together to avoid broken features.
- **Always include View permissions.** Many UI features require them, even with Create or Modify access.
- **Name roles clearly.** Use descriptive, consistent names like `asset_editor` or `alert_viewer`.
- **Use tenant roles for global access** and domain roles for specific projects or domains.
- **Combine tenant and domain roles** if a user needs both global and scoped permissions.
- **Audit regularly.** Remove roles that are unused or redundant.

---

## FAQs

**I have “View Data Source” but can’t see data sources. Why?**

 You also need “View Data Plane” permission for them to appear in the UI.

**Why can’t I modify a policy I can see?** 

You likely only have View permission. Add Create, Modify, or Execute rights to enable changes.

**Can a user have both tenant and domain roles?** 

Yes. Permissions from both are combined.

**Do tenant roles override domain roles?** 

Yes. Tenant roles apply platform-wide.

**How do I check who changed a role?** 

Open the role’s detail view and check the Activity section for who made changes and when.