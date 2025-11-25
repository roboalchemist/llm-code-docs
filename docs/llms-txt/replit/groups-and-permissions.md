# Source: https://docs.replit.com/teams/identity-and-access-management/groups-and-permissions.md

# Roles, Groups and Access

> Control team member access with roles and groups. Roles provide default access levels (Admin, Member, Guest, Viewer), while custom groups offer fine-grained access control for specific team members.

Manage your team's access to resources and applications through a comprehensive system built on default roles and custom groups. This approach provides granular control over who can access what, while maintaining organizational security and structure.

## Features

Replit Teams and Enterprise provides comprehensive access control through two complementary systems that work together to manage access across your organization.

<CardGroup cols={2}>
  <Card title="Admin" icon="shield-check">
    Full administrative access to organization settings and all resources
  </Card>

  <Card title="Member" icon="users">
    Can see all other members and create Apps and Projects
  </Card>

  <Card title="Guest" icon="user-plus">
    Limited access to only shared apps and resources
  </Card>

  <Card title="Viewer" icon="eye">
    Read-only access to apps and deployments
  </Card>
</CardGroup>

Key capabilities include:

* **Default roles**: Four built-in access levels that provide baseline access control for all team members
* **Custom groups**: Create specialized groups for fine-grained access control beyond default role limitations
* **Flexible access control**: Use roles and groups to grant precise access for different Apps and resources
* **Easy member management**: Add, remove, and transfer members between groups with simple administrative controls

## Usage

### Roles

Every team member must have a role that defines their baseline access level within your organization. Admins assign roles when adding new members to ensure proper access control from day one.

The four default roles provide different levels of access:

* **Admins**: Have access to every action available in Replit Teams, including organization settings, billing, and member management
* **Members**: Can create and edit Replit Apps and see all other team members, but cannot perform sensitive administrative actions
* **Guests**: Have the lowest access level and can only edit apps specifically shared with them. This role is useful for external contractors or interview candidates
* **Viewers**: Have read-only access to apps and deployments, making them ideal for stakeholders who need visibility without editing capabilities

### Custom groups

Custom groups provide more access control beyond default roles. Create groups to grant specific access to selected team members while maintaining their base role access.

<Note>
  For information on syncing IdP groups to Replit for easier bulk user access management, see [SCIM](https://docs.replit.com/teams/identity-and-access-management/scim).
</Note>

The list of groups is available via the "Groups" tab in the sidebar. Each group card shows the name of the group, an icon with its color, and the number of group members. Members will only see groups to which they have at least viewer access.

<Frame>
  <img src="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=469c873bdfec88e84d47a1f657669fbd" alt="Viewing groups" data-og-width="2992" width="2992" data-og-height="1696" height="1696" data-path="images/teams/identity-and-access-management/groups-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?w=280&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=518778c5b04ef112fc462f16b3595f7f 280w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?w=560&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=4beeb5a1f1918e88b38e44ac1da9d1d3 560w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?w=840&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=7194ff222836b5781b5cc9ab6cb8cb33 840w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?w=1100&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=e36f066507299a86a0f6f9c0657207dd 1100w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?w=1650&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=3ba708c23c6cc6a814e79b77bc7f8e61 1650w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/groups-view.png?w=2500&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=9480d76a1000de19e5a2204912fcccc8 2500w" />
</Frame>

#### Creating a group

Admins can create unlimited custom groups from the groups page. Select the **Add** button in the top right corner to open the creation modal where you can:

* **Name your group**: The group name is the only required field
* **Add visual identifiers**: Choose colors and icons to distinguish groups
* **Assign members**: Add team members to groups individually or in bulk
* **Grant access**: Groups can later receive access to specific apps through each app's **Access** button

<Frame>
  <img src="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=edfe4c8a934e7548ce1972d97300f6ab" alt="Creating a custom group modal with name field and color picker" data-og-width="2992" width="2992" data-og-height="1696" height="1696" data-path="images/teams/identity-and-access-management/creating-a-custom-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?w=280&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=2160c4b123349ca916b1b7f879fa6b7f 280w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?w=560&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=f5126ac938d5a35e622a16c633f34bad 560w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?w=840&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=53b18a6a2ae09aa64ca8f3859a0c4df4 840w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?w=1100&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=7f9679823c8c1b3f806ca501a015bf4d 1100w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?w=1650&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=3e72d0545a49b87079309224f44e5b95 1650w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/creating-a-custom-group.png?w=2500&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=993c9fdc060a2a87e4569b863186d40f 2500w" />
</Frame>

After creating the group, the group details view loads where you can add members and configure organizational permissions.

#### Managing groups

Select any group card to access its management interface. Group management includes member addition, removal, and permissions configuration.

<Frame>
  <img src="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=5e7f338deaf3db378230713f3fa0a906" alt="View group members" data-og-width="2992" width="2992" data-og-height="1696" height="1696" data-path="images/teams/identity-and-access-management/group-members-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?w=280&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=2d36ceb4d5249d8460128609456688f4 280w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?w=560&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=b676fbf2338331fa123d68ebf09de2f5 560w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?w=840&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=635f2ac4905740c23bd60040fe8b6886 840w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?w=1100&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=63fa9f3c7383abfe8b1c363860281231 1100w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?w=1650&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=aa0f07c8c73b2f9890a8bd3f83350318 1650w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/group-members-view.png?w=2500&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=3a84f00ed2d85a7a390f17be0aa7934c 2500w" />
</Frame>

**Adding members to groups:**

To add a member to a group, select the **Add** button in the top right corner. This action becomes disabled if the person you're adding is not part of the organization and there are insufficient seats available.

<Frame>
  <img src="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=f654dd3b1dc3a4d8d64489e5a45283e9" alt="Adding a group member dialog with search field for username or email" data-og-width="2992" width="2992" data-og-height="1696" height="1696" data-path="images/teams/identity-and-access-management/adding-a-group-member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?w=280&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=cd399599e6ccc976b13d445acb8f2f40 280w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?w=560&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=b27cabd9713b6904941d793df8761125 560w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?w=840&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=82c267d2a6dca3403744cdb51fb61977 840w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?w=1100&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=e7cd3abd5916157ee8b389bbe0bf6846 1100w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?w=1650&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=7fac03e9afc917e1c53accc96bca6c1b 1650w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/adding-a-group-member.png?w=2500&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=56bf62ab5d2b36730e642378a60df9fe 2500w" />
</Frame>

You can search for new members by username or email. If the new member is not part of the organization, a warning appears to confirm the action.

<Frame>
  <img src="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=b3311824356ff9e0ac4aca26b5c9de2d" alt="Warning dialog for adding non-organization members to groups" data-og-width="2992" width="2992" data-og-height="1696" height="1696" data-path="images/teams/identity-and-access-management/non-member-warning.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?w=280&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=e68c47d682905d2547e4e77828ab7679 280w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?w=560&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=ecfcebe6684587d017287cb181b78ab2 560w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?w=840&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=2003a27d2e7a9c9c88d324e5010fdf82 840w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?w=1100&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=af5e2fd37f4138e99cc8e1200745a1ee 1100w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?w=1650&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=d6a0f2a082a8aefaa3671240a26df6ff 1650w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/non-member-warning.png?w=2500&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=78c83aec2aee98c20488668eb6ae4793 2500w" />
</Frame>

After adding the new member, they appear in the group member list. They immediately gain access to Replit Apps and other resources available to the group.

**Removing members from groups:**

To remove a group member, select the trash icon on the right side of the member row. You can also open the actions menu using the three-dot button and select **Remove from group**. This opens a confirmation modal.

<Frame>
  <img src="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=c04eef1c2a87b23d471bfad1d97b9dcd" alt="Group member removal confirmation dialog" data-og-width="2992" width="2992" data-og-height="1696" height="1696" data-path="images/teams/identity-and-access-management/removing-a-group-member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?w=280&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=ce9bfe98802bc4e4c3611c6b8e1f7028 280w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?w=560&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=37afba339a9d6a8c040e2b3285f4a0cb 560w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?w=840&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=e4b681845d5eed0fa4f77725c1db343f 840w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?w=1100&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=06b52fd71b5c714b5b8a03d8277beba2 1100w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?w=1650&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=272545f0fad5d4bed34ba6dbddf3c4ab 1650w, https://mintcdn.com/replit/tqsDQtRVOjunuR_a/images/teams/identity-and-access-management/removing-a-group-member.png?w=2500&fit=max&auto=format&n=tqsDQtRVOjunuR_a&q=85&s=35c9edc0b4daa655c06dffbc8195b4ad 2500w" />
</Frame>

When removing members from custom groups, they retain their base role access but lose their group-specific access.

#### Setting group permissions

Assign organizational permissions to groups to define what level of access group members must have in your organization. To set group permissions, select the created group and choose the **permissions** tab in the left navigation.

The available permissions levels are:

* **Owner**: Can perform all organization actions, including deleting the organization
* **Billing manager**: Can update the organization's payment information, add and remove seats, and set spending limits
* **Manager**: Can create and manage groups, add and remove organization members, and view billing information
* **Editor**: Can create new Apps and view usage information
* **Viewer**: Can see basic information about the organization

These group permissions are separate from app-specific access, which you manage through individual apps using the Access feature.

You can see which apps groups have access to by selecting a group. Select **permissions** in the left navigation, and then go to **Apps**.

### App access control

Control who can access and collaborate on your apps using Replit's Access feature. Assign access to roles and groups to share specific apps with the right team members while maintaining security across your organization.

#### Setting app access

<Accordion title="How to manage app access">
  From any app, select **Access** in the upper right corner (to the left of **Publish**) to open the Access panel.
</Accordion>

The Access panel displays all available roles and allows you to search for custom groups:

* **Default roles**: Admin, Members, Guests, and Viewers appear automatically in the Access panel
* **Custom groups**: Use the search functionality to find and grant app access to specific custom groups

#### Access levels

You can assign different access levels to each role and group for fine-grained control:

* **Owner**: Full access including app deletion and administrative control
* **Publisher**: Can edit code, republish apps, and manage app resources, and settings
* **Editor**: Can edit code and view app resources without publishing capabilities
* **Viewer**: Read-only access to code with the ability to fork apps for their own use
* **None**: No access to search, view, or edit the app

Select the appropriate access level for each role or group based on collaboration requirements and security needs.
