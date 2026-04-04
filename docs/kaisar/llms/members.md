# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/members.md

# Members

Manage organization members, their roles, and access permissions.

![Members List View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-4ba521ce0b4d2b882e9695acb27ad53ad11d8114%2Fmembers_list_view.png?alt=media)

## Overview

The Members section allows you to invite users to your organization, assign them roles, and manage their access to resources.

**Dashboard Summary**:

* **Total Members**: Total number of registered members
* **Active**: Number of members with active status
* **Inactive**: Number of members with inactive status
* **Pending**: Number of invitations sent but not yet accepted

## Members List

The members table displays:

* **Member**: Name and email address
* **Role**: Assigned role (Admin, Manager, Developer, Analyst, Viewer)
* **Department**: Assigned department (e.g., Engineering, Data Science)
* **Status**: Active (green), Inactive (red), Pending (orange)
* **Last Login**: Time since last activity
* **Actions**: Edit, Delete, etc.

## Creating a Member

Navigate to **Organization** → **Members** → Click **+ Create**

![Create Member Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-afdf4ed5c2c52f282ea48602760a6032f36ca199%2Fmember_create_form.png?alt=media)

### Basic Information

**Full Name**\* (Required)

* Enter the member's full name

**Email Address**\* (Required)

* Enter the member's email address for invitation

**Phone Number**

* Optional contact number

**Department**\* (Required)

* Select or enter department name
* Example: `Engineering`, `Data Science`

**Job Title**

* Optional job title

### Role & Permissions

**Role**\* (Required)

* Select role from dropdown:
  * **Admin**: Full access
  * **Manager**: Manage resources and members
  * **Developer**: Create and deploy resources
  * **Analyst**: View and analyze data
  * **Viewer**: Read-only access

**Status**\* (Required)

* Initial status: `Active` or `Inactive`

**Permissions**

* Granular permissions (e.g., `Manage Users`)

### Group Assignments

**Groups**

* Assign member to specific groups for access control

### Actions

* **Cancel**: Discard changes
* **Create Member**: Send invitation and create member

## Viewing Member Details

To view detailed information about a member:

1. Navigate to **Organization** → **Members**
2. Click on a member from the list
3. View details in the modal dialog

![View Member](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-cd8e34893ed7608974f7363dc5737e1a0ff7c81a%2Fmember_details_view.png?alt=media)

**Details Panel**:

* **Basic Information**: Name, Email, Phone, Department, Job Title
* **Role & Permissions**: Role, Status, Permissions
* **Group Assignments**: Assigned groups

## Editing a Member

To update a member's information or role:

1. Open member details
2. Click **Edit** button (or select Edit from list actions)
3. Modify editable fields in the Edit Member modal

![Edit Member](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-41f8ea1072eecb50ec3987343ec064b6a2631d14%2Fmember_edit_form.png?alt=media)

4. Click **Update Member** to save changes

**Editable Fields**:

* ✅ Basic Information (Name, Email, Phone, Department, Job Title)
* ✅ Role & Permissions (Role, Status, Permissions)
* ✅ Group Assignments

## Member Roles Explained

| Role          | Description        | Key Permissions                                |
| ------------- | ------------------ | ---------------------------------------------- |
| **Admin**     | Full system access | Manage users, billing, settings, all resources |
| **Manager**   | Team management    | Manage team members, view all resources        |
| **Developer** | Builder access     | Create/Edit experiments, models, deployments   |
| **Analyst**   | Data access        | View analytics, experiments, datasets          |
| **Viewer**    | Read-only          | View resources only, no editing                |

## Best Practices

* **Least Privilege**: Assign the lowest role necessary for the user's tasks
* **Groups**: Use groups for managing permissions at scale rather than individual assignments
* **Regular Audits**: Periodically review member list and remove inactive users
* **Department Tagging**: Use accurate department tags for better reporting and organization

## Next Steps

* Organize members into [Groups](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/groups)
* Assign [Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents) to members or groups
