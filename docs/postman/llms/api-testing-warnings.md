# View security warnings in API requests

Postman applies security rules configured for your API requests when you send requests to any API using either the Postman web app or the Postman desktop app. A security warning doesn't mean your API is broken. Instead, it indicates there are potential security risks your API might be vulnerable to. Postman highlights these security warnings and helps you understand their implications and possible ways to fix the warnings.

> [Enterprise teams](https://www.postman.com/pricing/) can also customize the rules that Postman applies to API requests. For more information, see [Configure API Governance rules](/docs/api-governance/configurable-rules/configuring-api-governance-rules/).

When you [send an API request](/docs/sending-requests/create-requests/request-basics/#send-a-request), Postman scans it for potential security risks. If any are found, Postman adds the number of warnings to the **Security** tab in the response.

![Security tab showing one warning](https://assets.postman.com/postman-docs/v10/api-response-security-tab-v10.jpg)

To learn about API security warnings and how to hide warnings that aren't relevant to your team, see [Security warnings](/docs/sending-requests/response-data/responses/#security-warnings).

For the list of all the security warnings that Postman might show for API requests, see [Security warnings in API requests](/docs/api-governance/api-testing/security-warnings/).

---

## Postman Vault integrations

Integrate your Azure API Gateway with Postman Collections and streamline your testing workflow. The Azure API Gateway app enables developers to troubleshoot and reproduce issues in deployed environments.

### Import APIs from Azure API Gateway to Postman

Before you get started with creating a collection from an imported API, connect your Azure API Gateway to Postman. You can select an API to troubleshoot or test, and create a collection from the information available in the API gateway. To learn more, see [Connect your Azure API Gateway to Postman](#connect-your-azure-api-gateway-to-postman).

### Create collections in Postman from Azure Gateway APIs

Collections created using the API gateway app contain the latest data from the deployed environment. This lets you keep collaborative workspaces up to date by bringing runtime API information to a collection. To learn more, see [Create a collection from an imported API](#create-a-collection-from-an-imported-api).

### Connect your Azure API Gateway to Postman

Once connected to the Azure API Gateway, any one of the available APIs can be automatically imported, along with the environment and the associated environment variables.

To connect your Azure API Gateway to Postman, do the following:

1. In Postman, select **Team > Team Settings**.
2. Click **Installed apps**.
3. Select the Azure Gateway app and click **Install**. A popup window displays, click **Allow**.
4. Enter the following information to authorize installation of the app:
   * Azure Tenant ID
   * Azure Client ID
   * Azure Client Secret
   * Azure Subscription ID

5. Click **Next**.
6. Select the **Type** dropdown list.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

### Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

### Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.

    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

## Organization Settings

_Postman Organizations_ streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

### Create Organization teams

To create an Organization Team, do the following:

1. Access ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team’s membership. Environments open to collaboration don’t necessarily require this level of control.
   * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.

### Manage workspace scan policies

Use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** – [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** – Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** – [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

* **No policy** – Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
* **Move to vault** – Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:

    * If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
    * If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
    * Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

* This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

* The policy you select is automatically applied to the selected workspaces.

---

## Organization roles

### Team roles

Each team within an Organization has its own set of independent roles:

| Team role    | Capabilities |
| -------- | ---- |
| Team Manager (Team Super Admin) | 
* Has edit access to all elements within the Team and the capability to edit the Team's Settings.
* Manages the entire Team, including the users (add/remove/invite/assign) and the resources (view/edit/manage).
|
| Team Member | 
* Can have edit access to all elements on the Team, but doesn't automatically have access to workspaces, collections, and other elements within the Team unless given a role on that element.
* Can view all resources shared throughout the Team and can have Editor or Viewer access to any workspace or resource within the Team.
* Automatically gets access to all workspaces that are shared to the team when the workspace is set to **Everyone in [TeamName]**.
|
| Collaborator | 
* Can have a Developer or Viewer role. Developers can directly edit the element they're assigned, while Viewers can only view or fork the element they're assigned. Additionally, workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
* Has to be granted access to workspaces either by setting the workspace to **Everyone in [OrgName]** or by being invited directly through a user or a Team or Group they belong to.
|

* **Notes:**
* Only a Team Member can create workspaces in the team.
* Sharing an element with a new user triggers the process of adding that user to the Team's user list.
* Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team’s shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

### Determine the structure of your teams and memberships

A team within an Organization represents physical members of a functional team, for example, developer or test team, and also contains the workspaces that the group of users wants to keep secure and access controlled.

By creating teams and memberships first, you can establish strategic collaborations and empower your teams to migrate their own work to their teams. For example, even if your QA team hasn't moved all their workspaces to a QA-designated team yet, other teams can still invite the QA team members to collaborate with their team.

Once you define the teams, you can start the process of improving collaboration and security by populating the teams with your workspaces.

To determine the team membership, do the following:

1. The [Organization Manager (or Super Admin)](/docs/administration/organization/roles/) creates a Team and assigns a Team Manager to it.

    The Team Manager is the delegated owner of the Team’s content and membership and controls how the Team’s content is shared. The Team Manager is the leader of people responsible for the Team’s content.

1. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):

    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team’s membership. Environments open to collaboration don’t necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.

1. Populate the team with the members who are responsible for the team’s contents.

    * If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
    * If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
    
### Move work into Teams

You can move work into Teams manually, but if a significant number of workspaces need to be moved, you can move it in bulk.

Any Workspace Admin can move their workspaces into any team where they are a member, so the responsibility of migrating work can be delegated to all the members of the Team that was created.

If you can identify team workspaces ahead of time, Postman provides public API endpoints and collections that you can use to move large numbers of workspaces in bulk.

After you move workspaces, do the following:

1. Determine the Admins for each workspace from the list of workspace users.
1. Review the roles on the workspaces you moved, and align them with these best practices:

    * If the workspaces were previously shared with the Organization, ensure they remain shared with the Organization.
        * If the APIs are intended to be consumed by others, ensure those people still have access to view them.
        * If you require limited sharing, consider sharing APIs with specific Teams that are interested in them, leveraging the Team memberships, rather than inviting individuals.
    * Ensure that workspaces are viewable by the Team it was moved into, unless there is a specific reason it shouldn’t be shared with other Team members.
    * Make the workspace editable by the Team.
        * Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
        * The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
    * Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

## Create Organization teams

To create an Organization Team, do the following:

1. Access ![Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then select [Teams](https://go.postman.co/teams) and open a specification.
2. Click ![Image 12: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.

![Image 13: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

1. Click ![Image 14: Add Organization Team members](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add Organization Team members**.
1. Enter a name for the team and select the OpenAPI specification format it’ll be used in. You can’t change the name or OpenAPI specification version of a team file later.
1. Click **Create**.

![Image 15: Create Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)

Postman adds a new team file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you’d like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 16: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 17: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click ![Image 18: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
4. Enter a name for the component file and select the OpenAPI specification format it’ll be used in. You can’t change the name or OpenAPI specification version of a component file later.
5. Click **Create**.

![Image 19: Create a component file](https://assets.postman.com/postman-docs/v11/component-library-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Under **Workspace description**, add a description.
1. Under **About**, add a summary.
1. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

## Organization roles

### Team roles

Each team within an Organization has its own set of independent roles:

| Team role    | Capabilities |
| -------- | ---- |
| Team Manager (Team Super Admin) | 
* Has edit access to all elements within the Team and the capability to edit the Team's Settings.
* Manages the entire Team, including the users (add/remove/invite/assign) and the resources (view/edit/manage).
|
| Team Member | 
* Can have edit access to all elements on the Team, but doesn't automatically have access to workspaces, collections, and other elements within the Team unless given a role on that element.
* Can view all resources shared throughout the Team and can have Editor or Viewer access to any workspace or resource within the Team.
* Automatically gets access to all workspaces that are shared to the team when the workspace is set to **Everyone in [TeamName]**.
|
| Collaborator | 
* Can have a Developer or Viewer role. Developers can directly edit the element they're assigned, while Viewers can only view or fork the element they're assigned. Additionally, workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
* Has to be granted access to workspaces either by setting the workspace to **Everyone in [OrgName]** or by being invited directly through a user or a Team or Group they belong to.
|

* **Notes:**
* Only a Team Member can create workspaces in the team.
* Sharing an element with a new user triggers the process of adding that user to the Team's user list.
* Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).