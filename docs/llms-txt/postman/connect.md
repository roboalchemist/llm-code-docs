# Connect a GitHub repository to your collection

Connect a GitHub repository and branch to your collection and collaborate with your team on your collection's releases. For example, connect your repository's primary branch to your collection, [fork that collection in Postman](/docs/integrations/available-integrations/github/collections/collaborate/#fork-a-collection-connected-to-your-github-repository-and-branch), and [collaborate with your team on your collection's next release](/docs/integrations/available-integrations/github/collections/collaborate/#collaborate-on-your-collection).

## Connect a GitHub repository and branch to your collection

Before you get started, create your repository and primary branch.

To connect a GitHub repository and branch to your collection, do the following:

1. Open your collection.
2. Next to your collection, click ![Image 1: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**. Then, click **More** > **Connect repository**.
3. Choose where you host your repository:
   - If you choose **GitHub**, Postman asks you to authenticate. Follow the onscreen instructions.
   - If you choose **GitHub Enterprise Server**, Postman asks you for your GitHub domain. Enter or select it, and click **Authenticate**. Then, follow the onscreen instructions.
4. Select an organization.
5. If you don't see your organization, you may need to [install the GitHub App to your organization first](https://docs.github.com/apps/using-github-apps/installing-a-github-app-from-a-third-party). To get started, follow the onscreen instructions.
6. Select a repository and branch.
7. (Optional) Enter a directory path for your collection file.
8. Click **Connect**.

Postman creates a collection file in the connected repository and branch. The collection's file name is the collection ID. Each time you save your collection in Postman, your changes are committed to the connected GitHub repository and branch.

To start collaborating on your next release, see [Collaborate on your collection's release](/docs/integrations/available-integrations/github/collections/collaborate/).

## Disconnect a GitHub repository and branch from your collection

If you want to connect a different repository or branch to your collection, or need to troubleshoot your connection, you can start by disconnecting GitHub from your collection.

To disconnect a GitHub repository and branch from your collection, do the following:

1. Open your collection.
2. Next to your collection, click ![Image 2: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**. Then, click **More** > **Disconnect repository**.
3. Enter your collection's name. Then, click **Disconnect repository**.

Your collection is no longer connected to the GitHub repository and branch.

---

## Connect Postman with Azure API Gateway

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
   - Azure Tenant ID
   - Azure Client ID
   - Azure Client Secret
   - Azure Subscription ID

5. Click **Next**.
6. The new installed app appears on the Installed apps page with the status as **Connected**.
7. Click **Next**.
8. Select the API you want to import.
9. Select the stage on which the API is deployed.
10. Create an environment (optional). This creates a new environment on Postman for the API variables from the gateway.
11. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
12. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
13. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

### Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.
4. Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

Postman also identifies governance issues for components, but only once they're [referenced in your specification](#reference-a-component-in-a-specification).

### Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 3: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.
4. Postman scans secrets in real time and takes action, storing exposed secrets, like API keys, JWT tokens, or auth tokens, in the [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/). The Postman Vault stores your exposed secrets securely on your device. The original secret value is replaced with a vault secret reference. This prevents your team's secrets from syncing to the Postman cloud and gives you greater control over your team's security posture and compliance requirements.

Postman's Local Secret Protection actively scans for secrets in the following Postman elements when changes are made:

- HTTP collections
- Environments variable values
- Global variable values

Local Secret Protection requires Postman version 11.71.3 or later.

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Manage workspace scan policies

Use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

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

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

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

- To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
- To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

Postman provides tools to help you manage your team's usage of credits in Postman Flows. You get a certain number of credits each month.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

---

## Organization Settings

Postman has a variety of tools you can use to set up, manage, and secure your Postman team.

### Create Organization Teams

To create an Organization Team, do the following:

1. Access ![Image 4: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Organization Settings** in the Postman header, then click **Organization Settings**.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.

### Team roles

Each team within an Organization has its own set of independent roles:

| Team role    | Capabilities |
| -------- | ---- |
| Team Manager (Team Super Admin) | 
- Has edit access to all elements within the Team and the capability to edit the Team's Settings.
- Manages the entire Team, including the users (add/remove/invite/assign) and the resources (view/edit/manage).
|
| Team Member | 
- Can have edit access to all elements on the Team, but doesn't automatically have access to workspaces, collections, and other elements within the Team unless given a role on that element.
- Can view all resources shared throughout the Team and can have Editor or Viewer access to any workspace or resource within the Team.
- Automatically gets access to all workspaces that are shared to the team when the workspace is set to **Everyone in [TeamName]**.
|
| Collaborator | 
- Can have a Developer or Viewer role. Developers can directly edit the element they're assigned, while Viewers can only view or fork the element they're assigned. Additionally, workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
- Has to be granted access to workspaces either by setting the workspace to **Everyone in [OrgName]** or by being invited directly through a user or a Team or Group they belong to.
|

### **Notes**

- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

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
2. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
3. Populate the team with the members who are responsible for the team’s contents.
4. If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
5. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
6. Ensure that workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
7. Make the workspace editable by the Team.
   - Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
   - The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
8. Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

## Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 5: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Organization Settings** in the Postman header, then click **Team Settings**.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
7. If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
8. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
9. Ensure that workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
10. Make the workspace editable by the Team.
   - Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
   - The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
11. Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

### **Notes**

- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

### Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.
4. Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

### View secret scan metrics

Postman provides tools to help you manage your team's usage of credits in Postman Flows. You get a certain number of credits each month.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

---

## Organization roles

_Postman Organizations_ streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives each team better control over its membership.

### Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 6: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Organization Settings** in the Postman header, then click **Team Settings**.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
7. If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
8. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
9. Ensure that workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
10. Make the workspace editable by the Team.
   - Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
   - The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
11. Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

### **Notes**

- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

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
2. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
3. Populate the team with the members who are responsible for the team’s contents.
4. If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
5. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
6. Ensure that workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
7. Make the workspace editable by the Team.
   - Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
   - The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
8. Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

### **Notes**

- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

## Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 7: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Organization Settings** in the Postman header, then click **Team Settings**.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
7. If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
8. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
9. Ensure that workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
10. Make the workspace editable by the Team.
   - Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
   - The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
11. Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

### **Notes**

- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

### Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.
4. Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file