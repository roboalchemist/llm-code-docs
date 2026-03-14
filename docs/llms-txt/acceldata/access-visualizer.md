# Source: https://docs.acceldata.io/documentation/access-visualizer.md

# Access Visualizer

The Access Visualizer in ADOC provides an interactive, graphical view of how access permissions are structured across your environment. It helps both administrators and end-users quickly understand:

- Which roles and groups a user belongs to
- How permissions flow from tenant roles and domain roles
- What resources are accessible through these assignments

By turning complex role–resource relationships into a visual map, the Access Visualizer makes permission audits, troubleshooting, and validation far easier.

## Prerequisites to Access

You must have at least **View** permission for **User Management** via any assigned [Tenant Role](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/roles-and-permissions#1-tenant-roles). Without this permission, Access Visualizer will not be visible in the UI.

> A **Tenant Role** in ADOC defines platform-wide permissions that control what users and groups can do across all modules, making it a central tool for administrators to manage global access and governance.

Note If you don’t see the option, contact your Acceldata Support team or an admin with permission to adjust your role.

## Navigating to the Access Visualizer

1. From the left navigation pane, click **Settings**.
2. Under **User Management and Access**, select **Access Visualizer**.

## Using the Visualizer

### 1. Selecting an Entity

You can visualize access relationships for several entity types:

- [User](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/users-and-groups#1-user-management)
- [User Group](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/users-and-groups#2-groups)
- [Tenant Role](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/roles-and-permissions#1-tenant-roles)
- [Domain Role](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/roles-and-permissions#2-domain-roles)
- [Domain](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/domains#what-is-a-domain-in-adoc)
- [Resource Group](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/users-and-groups#1-user-management)

Steps:

1. Choose an entity type from the dropdown menu.
2. Begin typing the entity name; suggestions will appear dynamically.
3. Select the desired entity to load its access relationship diagram.

### 2. Understanding the Visualization

**Example: User Entity**

Selecting a user (e.g., Pulse Cloud) shows:

- Direct role assignments (solid lines labeled “is assigned”)
- Group memberships (solid lines labeled “belongs to”)
- Clicking a node highlights the full permission path from the selected user to connected roles and groups.

**Example: Domain Entity**

Displays:

- User Groups with access to the domain
- Domain Roles mapped to those user groups
- Resource Groups contained within the domain
- Clicking a node (e.g., a domain role) highlights the related permission chain, helping validate domain–role–resource relationships.

### 3. Interacting with the Diagram

- **Zoom & Pan** – Focus in on complex sections or view the full access map.
- **URL Sharing** – The visualization state is encoded in the URL, so you can share a direct link to a specific access view for collaboration or troubleshooting.

## Key Use Cases

- **Access Troubleshooting** – Identify why a user/group does or doesn’t have access to a resource.
- **Configuration Validation** – Visually confirm role mappings after making permission changes.
- **Audit Support** – Provide clear, visual proof of access paths during compliance reviews.