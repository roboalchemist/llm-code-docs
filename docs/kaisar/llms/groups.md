# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/groups.md

# Groups

Manage groups within your organization for team-based access control and hierarchy.

![Groups List View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-9c61b2040ae8351cf83cfc7dea33204d43644370%2Fgroups_list_view.png?alt=media)

## Overview

Groups allow you to organize members into logical units (e.g., teams, departments, projects) and assign permissions or resources to them collectively. Groups can be nested to create an organizational hierarchy.

**Dashboard Summary**:

* **Total Groups**: Total number of groups configured
* **Parent Groups**: Number of root-level groups
* **Sub Groups**: Number of nested groups
* **Total Members**: Total users assigned to groups

## Groups List

The groups table displays:

* **Group Name**: Name and description (e.g., "Quality Assurance", "Frontend Team")
* **Parent Group**: The parent group name or "Root" if top-level
* **Members**: Number of members in the group
* **Status**: Active (green) or Inactive (gray)
* **Created**: Date of creation
* **Actions**: Edit, Delete, etc.

## Creating a Group

Navigate to **Organization** → **Groups** → Click **+ Create**

![Create Group Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-b57ab29531817cee20743ca3f03d5b006c3e856d%2Fgroup_create_form.png?alt=media)

### Group Information

**Group Name**\* (Required)

* Enter a descriptive name for the group
* Example: `Quality Assurance`, `Engineering`, `Sales`
* Helper text: "Enter a descriptive name for the group"

**Description**

* Optional description of the group's purpose
* Example: "Testing and quality control team"

**Parent Group**

* Select a parent group to create hierarchy
* Dropdown selection of existing groups
* Helper text: "Select a parent group to create hierarchy"

**Status**\* (Required)

* Current status of the group
* Options: `Active`, `Inactive`
* Default: `Active`

### Actions

* **Cancel**: Discard changes
* **Create Group**: Save the new group

## Viewing Group Details

To view detailed information about a group:

1. Navigate to **Organization** → **Groups**
2. Click on a group from the list
3. View details in the modal dialog

![View Group](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-9890467664ecffa38904c9c9134a3c732741ad75%2Fgroup_view_details.png?alt=media)

**Details Panel**:

* **Group Name**: e.g., "Quality Assurance"
* **Description**: e.g., "Testing and quality control team"
* **Parent Group**: Shows selected parent if any
* **Status**: Active or Inactive

## Editing a Group

To update a group:

1. Open group details
2. Click **Edit** button
3. Modify editable fields in the Edit Group modal

![Edit Group](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-8c403b8032ab96c1f874e0eb62e20f46b2641db0%2Fgroup_edit_form.png?alt=media)

4. Click **Update Group** to save changes

**Editable Fields**:

* ✅ Group Name
* ✅ Description
* ✅ Parent Group
* ✅ Status

## Group Hierarchy

**Parent-Child Relationships**:

* Groups can have one parent group
* A parent group can have multiple child groups
* Permissions and access can be inherited (depending on configuration)

**Example Structure**:

* **Engineering** (Parent)
  * **Backend Team** (Child)
  * **Frontend Team** (Child)
  * **QA Team** (Child)

## Managing Group Members

(See [Members](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/members) for details on adding users to groups)

## Best Practices

* **Naming**: Use clear, consistent naming conventions
* **Hierarchy**: Reflect your actual organizational structure
* **Descriptions**: Provide clear descriptions for easier management
* **Maintenance**: Deactivate groups that are no longer in use instead of deleting them immediately to preserve history

## Next Steps

* Add [Members](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/members) to your groups
* Assign [Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents) to groups
* Configure group-level permissions
