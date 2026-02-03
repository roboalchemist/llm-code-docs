# user-groups

Organize users into Postman groups
==================================

**[Groups are available with Postman Enterprise plans.](https://www.postman.com/pricing/)**

With Postman groups, you can arrange users into groups that reflect your organizational structure. You can add users to a group, then assign that group roles and access to the resources they'll be using across Postman. You can also efficiently onboard new team members by adding them to existing groups in your organization, instantly giving them access to the elements they'll be working on. Groups enable you to control access from a single dashboard in Postman and manage it at scale across your Enterprise team.

[Admins and Super Admins](/docs/administration/roles-and-permissions/#team-roles) can create, manage, and delete groups. [Developers](/docs/administration/roles-and-permissions/#team-roles) can also create, manage, and delete Developer-only groups.

## Creating a group

To create a group, select **Team** in the Postman header, then select **Manage Team**. Select **Groups** on the left, then **Create Group**.

![Image 1: Create group](https://assets.postman.com/postman-docs/v10/team-dashboard-manage-groups-v10.15.jpg)

Give your group a name and description, and add your group members. If you're an Admin or Super Admin, you'll also have the option to select the team roles you'd like to assign to the group. If you're a Developer, you'll only have the option to create Developer-only groups.

![Image 2: Create a group](https://assets.postman.com/postman-docs/v10/create-a-group-v10.15.jpg)

When you're ready, select **Create Group**.

Team members will receive an email and in-app notification when added to a group.

If you add a user with a support-only role (Admin or Billing) to a group that gives them a Developer role, they will automatically take up an available paid seat on your Postman team. If no seats are available, you won't be able to grant access to the group with that user.

## Managing a group

You can manage a group's members, roles, and access to Postman elements.

### Managing members of a group

[Admins and Super Admins](/docs/administration/roles-and-permissions/#team-roles) can add and remove members for all groups, but [Developers](/docs/administration/roles-and-permissions/#team-roles) can only add and remove members if they're a [group manager](#managing-group-managers).

To manage the members of a group, select **Team** in the Postman header, then select **Manage Team**. Select **Groups** on the left. Locate the group you'd like to update and select it to edit.

![Image 3: Manage group members](https://assets.postman.com/postman-docs/v10/edit-group-members-v10.15.jpg)

Select \[img alt="Add icon" src="https://assets.postman.com/postman-docs/aether-icons/action-add-stroke-small.svg#icon"\] **Add** to add a user to the group. Select \[img alt="Close icon" src="https://assets.postman.com/postman-docs/aether-icons/action-close-stroke-small.svg#icon"\] **Remove member** next to a user to remove them from the group.

Users will receive an email and in-app notification when added to or removed from a group.

### Managing group managers

Groups that are only assigned the Developer role can have group managers. Group managers can edit the name, description, members, and managers for a group.

When a Developer creates a group they're automatically assigned the role of group manager. Developers with the group manager role, Admins, and Super Admins can add and remove group managers.

To edit the managers of a group, select **Team** in the Postman header, then select **Manage Team**. Select **Groups** on the left. Locate the group you'd like to update and select it to edit.

![Image 4: Manage developer group managers](https://assets.postman.com/postman-docs/v10/edit-group-managers-v10.15.jpg)

Select \[img alt="Add icon" src="https://assets.postman.com/postman-docs/aether-icons/action-add-stroke-small.svg#icon"\] **Add** to add a manager to the group. Select \[img alt="Close icon" src="https://assets.postman.com/postman-docs/aether-icons/action-close-stroke-small.svg#icon"\] **Remove manager** next to a manager to remove them from the group.

### Managing access control for a group

You can control a group's access at the team level, workspace level, and on individual collections, APIs, environments, mock servers, and monitors.

Users will receive an in-app notification when roles are updated.

#### Editing team roles for a group

[Admins and Super Admins](/docs/administration/roles-and-permissions/#team-roles) can manage team roles for groups.

To edit team roles for a group, select **Team** in the Postman header, then select **Manage Team**. Select **Groups** on the left. Locate the group you'd like to update and select it to edit.

![Image 5: Edit group team roles](https://assets.postman.com/postman-docs/v10/manage-roles-for-a-group-v10.15.jpg)

Select the team roles you'd like to assign to the group, or deselect team roles you'd like to remove from the group, then select **Update Roles**.

To learn more about roles and their permissions, see [Team Roles](/docs/administration/roles-and-permissions/#team-roles).

#### Managing roles on workspaces and Postman elements

You can control a group's access to individual workspaces, collections, APIs, environments, mock servers, and monitors. For more information on managing workspaces, see [Share workspaces](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#share-workspaces).

You can use the Postman API to programmatically manage users and user groups for workspaces. For more information, see the [Postman API collection](https://api.postman.com/).

For collections, APIs, environments, mock servers, and monitors, go to the element you'd like to edit roles for. In the sidebar, select \[img alt="Options icon" src="https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon"\] **View more actions**, then select **Share**.

Use the search bar to add the group, then give the group **Editor** or **Viewer** permissions with the dropdown. To remove a group, select **Remove** in the dropdown menu next to the group.

#### See [Defining roles](/docs/administration/roles-and-permissions/) for more information on access control at a team, workspace, API, and collection level.

### Editing details for a group

[Admins, Super Admins](/docs/administration/roles-and-permissions/#team-roles), and [group managers](#managing-group-managers) can edit details for a group.

To edit details for a group, select **Team** in the Postman header, then select **Manage Team**. Select **Groups** on the left. Locate the group you'd like to update and select it to edit.

Select the group's name at the top of the page to edit it. To add a description, select **Add a description** under the group's name. To update an existing description, select it to edit. Changes are automatically saved.

## Deleting a group

[Admins, Super Admins](/docs/administration/roles-and-permissions/#team-roles), and [group managers](#managing-group-managers) can delete a group.

To delete a group, select **Team** in the Postman header, then select **Manage Team**. Select **Groups** on the left. Locate the group you'd like to delete and select it.

Select **Delete Group** to delete the group, then **Delete Group** to confirm.

![Image 6: Delete group](https://assets.postman.com/postman-docs/v10/delete-group-v10.15.jpg)