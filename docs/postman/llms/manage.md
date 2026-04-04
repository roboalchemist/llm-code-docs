# Manage Partner Workspaces in Postman

**[Partner Workspaces are available with Postman Professional and Enterprise plans.](https://www.postman.com/pricing/)**

Workspace Admins and Partner Managers manage workspace settings, users, and roles within a Partner Workspace. Partner Leads also manage users and roles of partners in Partner Workspaces. Learn how to manage users and roles in a Partner Workspace and scale your collaboration by adding and updating Partner licenses and Partner Workspaces.

From May 2025, you can begin creating _team-to-team Partner Workspaces_, which ensures easier and more secure collaboration between you and your partners. Your partners can use domain capture and SSO to authenticate to your Partner Workspaces and you can track your partnerships in a new team setting called [**Partnerships**](#manage-your-partnerships). That means no switching between teams and more control over partnerships.

See the [FAQ](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/faq/) about team-to-team partnerships.

## Manage users and roles

You can assign team and Partner Workspace roles based on the functions team members and partners require. You can assign team roles for Partner Workspace roles at the [team level](/docs/administration/managing-your-team/team-members/manage-roles/), and you can assign Partner Workspace roles at the [workspace level](/docs/administration/managing-your-team/team-members/manage-roles/#manage-workspace-roles) and [collection level](/docs/administration/managing-your-team/team-members/manage-roles/#manage-element-based-roles). Learn more about [team and Partner Workspace roles](/docs/administration/roles-and-permissions/#partner-team-and-partner-workspace-roles).

To learn more about collaborating as a team member or partner, see [Collaborate in a Partner Workspace](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/collaborate/).

## Add Partner licenses

A paid seat is consumed when a Partner is assigned at least one Editor role (at the workspace or collection level) in at least one Partner Workspace. Assigning a Partner the Workspace Viewer or Collection Viewer role doesn't consume paid seats.

To purchase more Partner licenses, contact your Postman Account Manager or [contact Postman's sales team](mailto:sales@postman.com).

Your team must have [available seats](/docs/billing/billing/#changing-your-plan) or [Auto-Flex enabled](/docs/billing/billing/#using-auto-flex) to [invite a partner](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/setup/#invite-collaborators-to-a-partner-workspace) as a Workspace Editor. Otherwise, the Partner will be assigned the Workspace Viewer role, giving the Partner permission to view all workspace resources. Also, your team must have available seats to assign a Partner as a Collection Editor.

## Manage workspace elements

To move elements to a Partner Workspace, see [Move elements to a Partner Workspace](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/setup/#move-elements-to-a-partner-workspace).

To remove elements from a Partner Workspace, see [Remove elements from a Partner Workspace](#remove-elements-from-a-partner-workspace).

## Edit workspace details

Workspace Admins and Partner Managers can edit Partner Workspace details. On the workspace's Overview tab, select the workspace name, summary, or description to edit it. You can add Markdown to the description. Select **Save** when you're done.

## Manage your partnerships

API publishers [invite partners](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/setup/#invite-collaborators-to-a-partner-workspace) using their email. When accepting the invite to collaborate, the Partner selects an existing team or creates a new one. This team is then listed on the API publisher's [**Partnerships**](https://go.postman.co/settings/team/partnerships/external-partners) page.

To collaborate within the Partner Workspace, the Partner authenticates using their team's login method: username and password, or SSO.

From the **Partnerships** page, [Partner Managers](/docs/administration/roles-and-permissions/#partner-team-and-partner-workspace-roles) can verify which partners use or don't use \[![Image 1: Sso icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-sso-stroke.svg#icon)](#manage-your-partnerships) **SSO** to authenticate. They can also see individual partners, who access the Partner Workspace using a Postman account.

In the header, select **Team > Team Settings**. Then, select **Partnerships**.

![Image 2: Partnerships](https://assets.postman.com/postman-docs/v11/partnerships-v11.67.png)

Workspace Admins and Partner Managers can view and control whether their members of their team can accept Partner invites from other teams.

![Image 3: Partner invites](https://assets.postman.com/postman-docs/v11/partner-view-v11.jpg)

Use the **As a publisher** tab to view and manage the partnerships you own as a publisher. You can see all the partners invited by your team to collaborate.

The **As a partner** tab contains the list of the teams who have invited your team members as Partners to collaborate in their Partner Workspaces.

## View resources a Partner can access

A [Partner Manager](/docs/administration/roles-and-permissions/#partner-team-and-partner-workspace-roles) can view the Partner Workspaces and collections a Partner can access. A Partner Manager can also view the Workspace role partners are assigned in each workspace, and the Collection role partners are assigned in each collection. Open your [team dashboard](https://go.postman.co/settings/team/members) and select **View resources** next to a partner. Select a Partner Workspace or collection name to open it in a new tab.

![Image 4: View Partner Workspaces and roles](https://assets.postman.com/postman-docs/v10/view-partner-workspaces-and-roles-v10-3.jpg)

## Remove elements from a Partner Workspace

You must be at least an Editor on an API, collection, or environment to remove an element from a Partner Workspace. You can also be a Workspace Admin, Partner Manager, or Super Admin to remove any element from a Partner Workspace.

To remove an element by moving it to another workspace, do the following:

1. Select \[![Image 5: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon)\] **View more actions** next to the element you want to move, then select **Move**.
2. Use the search bar to find the workspace you'd like to move the element to, or use \[![Image 6: Filter icon](https://assets.postman.com/postman-docs/aether-icons/action-filter-stroke.svg#icon)\] **Filter by visibility**.
   - You can only move elements to workspaces that you have access to.
3. Select the workspace, then select **Move** (**Collection**, **API**, **Flow**, **Environment**, or **Mock Server**).
   
   While not recommended, you can choose to delete an element entirely. To do so, select \[![Image 7: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon)\] **View more actions** next to the element you want to remove, then select **Delete**.

   Deleted APIs and environments aren't recoverable. You can recover collections smaller than 30 MB for up to 90 days on an Enterprise plan. To do so, select \[![Image 8: Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon)\] **Trash** from the Postman footer.

## Remove partners from a Partner Workspace

You can remove partners from individual Partner Workspaces. To remove a Partner from a Partner Workspace, see [Manage workspace roles](/docs/administration/managing-your-team/team-members/manage-roles/#manage-workspace-roles).

You can remove partners from a team. Removing a Partner from a team removes them from all Partner Workspaces. If you remove the last Admin from the team, users assigned the Partner Manager role will be assigned the Admin role. Also, if you remove a Partner from their last Partner Workspace, they'll be removed from the team. To remove a Partner from a team, see [Remove team members](/docs/administration/managing-your-team/team-members/scale-team/#remove-team-members).

**NEW** From May 2025, if a Partner leaves or is removed from their own team, they lose access to the Partner Workspace.

## Delete a Partner Workspace

Workspace Admins and Partner Managers can delete Partner Workspaces.

1. On the workspace's **Overview** tab, select **Settings**.
2. [Change the type of the workspace](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#change-workspace-visibility) to **Internal**.
3. Select **Remove all partners**, then select **Update**.
4. Select **Delete Workspace**.

Postman notifies all workspace members in-app and by email when you delete a Partner Workspace.

## Postman Power Pass FAQ

### Tips

Before you set up your Organization Teams, consider the following:

- How many teams do you need and for which specific step in your API lifecycle?
- How will you name your teams and workspaces?
- Who will be in each group and on which team? Who will manage each team?
- How many workspaces will each team need to begin collaborating?
- If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

### Steps

To migrate your teams to Organizations, contact your Customer Success Manager. Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

### Determine the structure of your teams and memberships

A team within an Organization represents physical members of a functional team, for example, developer or test team, and also contains the workspaces that the group of users wants to keep secure and access controlled.

By creating teams and memberships first, you can establish strategic collaborations and empower your teams to migrate their own work to their teams. For example, even if your QA team hasn't moved all their workspaces to a QA-designated team yet, other teams can still invite the QA team members to collaborate with their team.

Once you define the teams, you can start the process of improving collaboration and security by populating the teams with your workspaces.

To determine the team membership, do the following:

1. The [Organization Manager (or Super Admin)](/docs/administration/organization/roles/) creates a Team and assigns a Team Manager to it.
2. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team’s membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
3. Populate the team with the members who are responsible for the team’s contents.
   - If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
   - If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
   - The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
   - Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
- **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

- **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
- **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:
  - If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
  - If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
  - Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

- **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
- **Partner** - Only