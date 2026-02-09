# interact

Use Postman to interact with your generated MCP server and an AI model
====================================================================

You can use Postman to interact with your generated MCP server locally and an AI model of your choice.

## Interact with your MCP server and an AI model

To interact with your MCP server and an AI model, do the following:

1. If you haven't already, [set up and start your MCP server](/docs/postman-ai/mcp-servers/set-up-start/).
2. [Create a new MCP request](/docs/postman-ai/mcp-requests/create/#create-a-new-mcp-request) and [save it to a collection](/docs/postman-ai/mcp-requests/create/#save-your-new-mcp-request). When you're prompted, choose your server's communication method:
   - To interact with your [standard input and output](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio) server, choose **STDIO** and enter your server's command. For example, enter:
     ```bash
     node /path/to/your-mcp-server/mcpServer.js
     ```
   - To interact with your [streamable HTTP](https://modelcontextprotocol.io/docs/concepts/transports#streamable-http) server, choose **HTTP** and enter your server's local URL. For example, enter:
     ```bash
     http://localhost:3001/mcp
     ```
3. [Use your MCP request to interact with your MCP server](/docs/postman-ai/mcp-requests/interact/). You can use your request to experiment, test, and evaluate your MCP server.
4. [Create a new AI request](/docs/postman-ai/ai-requests/create/#create-a-new-ai-request) and [save it to a collection](/docs/postman-ai/ai-requests/create/#save-your-new-ai-request). Save your new AI request to the same workspace you saved your MCP request.
5. [Add your MCP request to your AI request](/docs/postman-ai/ai-requests/add-mcp-servers/#add-the-mcp-server). When you're prompted, enter your server's command (STDIO) or URL (streamable HTTP), and search for the MCP request you created in the previous steps.
6. [Use your AI request to interact with your MCP server](/docs/postman-ai/ai-requests/interact/). You can use your request to experiment, test, and evaluate AI models.

To learn more, see [Create MCP requests and add them to your collections](/docs/postman-ai/mcp-requests/overview/) and [Create AI requests and add them to your collections](/docs/postman-ai/ai-requests/overview/).

---

### Postman Vault Integrations

**[Postman Vault integrations](/docs/sending-requests/postman-vault/postman-vault-integrations/)** enable you to link vault secrets with secrets that are stored in an external vault. You can then reference vault secrets in your Postman team, and retrieve the value of external vault secrets using end-to-end encryption when you send HTTP requests. You can [manage and update](#manage-local-secret-protection) your Postman Vault integrations.

**Note:** The component library doesn't support AsyncAPI specifications or [the Postman CLI](/docs/postman-cli/postman-cli-options/#postman-spec-lint).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set Default Protection Policies for New Workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

**Note:** This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

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

### Update Secret Protection Policies

To update a workspace's secret protection policy, do one of the following:

- To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
- To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

## View Secret Scan Metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

---

### Organization Settings

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**Note:** The organization manager (or super admin) creates a Team and assigns a Team Manager to it. The Team Manager is the delegated owner of the Team's content and manages the entire Team, including the users (add/remove/invite/assign) and the resources (view/edit/manage).

**Team Members** can approve the adding of Members and the sharing of content from the Teams they manage.

**Collaborators** can be brought into the team as secondary contributors or consumers. For example, collaborators can be QA teams supporting the team's activities, consumers of the team's APIs, or an entire Organization. On teams that don't require approval, Collaborators can be added automatically. On teams that require approval, an Admin must approve the addition of Collaborators to keep parts of the team private while others are shared.

## Team Roles

Each team within an Organization represents physical members of a functional team, for example, developer or test team, and also contains the workspaces that the group of users wants to keep secure and access controlled.

By creating teams and memberships first, you can establish strategic collaborations and empower your teams to migrate their own work to their teams. For example, even if your QA team hasn't moved all their workspaces to a QA-designated team yet, other teams can still invite the QA team members to collaborate with their team.

Once you define the teams, you can start the process of improving collaboration and security by populating the teams with your workspaces.

To determine the structure of your teams and memberships, do the following:

1. The **Organization Manager (or Super Admin)** creates a Team and assigns a Team Manager to it.
2. Determine how restricted the Team access should be. All Organization Teams have two settings:
   - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
   - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.

3. Populate the team with the members who are responsible for the team's contents.

- If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
- If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.

**Notes:**
- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team’s shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

**To migrate your teams to Organizations, contact your Customer Success Manager.**

Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Create Organization Teams

To create an Organization Team, do the following:

1. Access **Organization Settings** in the Postman header, then select **Organization Teams** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.

**Notes:**
- If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
- You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/) relationship.

![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

## Create Organization Workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the **Home** page, click **Teams** and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit Workspace Details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### View Secret Scan Metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### Organization Roles

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**Organization Managers** are responsible for creating Teams in the Organization and can manage any Team. They're also responsible for assigning individual Team Managers to the teams they create.

**Team Managers** can approve the adding of Members and the sharing of content from the Teams they manage.

**Collaborators** can be brought into the team as secondary contributors or consumers. For example, collaborators can be QA teams supporting the team's activities, consumers of the team's APIs, or an entire Organization. On teams that don't require approval, Collaborators can be added automatically. On teams that require approval, an Admin must approve the addition of Collaborators to keep parts of the team private while others are shared.

## Team Roles

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

**Notes:**
- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team’s shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

**To migrate your teams to Organizations, contact your Customer Success Manager.**

Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Create Organization Teams

To create an Organization Team, do the following:

1. Access **Organization Settings** in the Postman header, then select **Organization Teams** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.

**Notes:**
- If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
- You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/) relationship.

![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

## Create Organization Workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the **Home** page, click **Teams** and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit Workspace Details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### View Secret Scan Metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### Organization Settings

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**Organization Managers** are responsible for creating Teams in the Organization and can manage any Team. They're also responsible for assigning individual Team Managers to the teams they create.

**Team Managers** can approve the adding of Members and the sharing of content from the Teams they manage.

**Collaborators** can be brought into the team as secondary contributors or consumers. For example, collaborators can be QA teams supporting the team's activities, consumers of the team's APIs, or an entire Organization. On teams that don't require approval, Collaborators can be added automatically. On teams that require approval, an Admin must approve the addition of Collaborators to keep parts of the team private while others are shared.

## Team Roles

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

**Notes:**
- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team’s shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

**To migrate your teams to Organizations, contact your Customer Success Manager.**

Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Create Organization Teams

To create an Organization Team, do the following:

1. Access **Organization Settings** in the Postman header, then select **Organization Teams** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.

**Notes:**
- If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
- You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/) relationship.

![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

## Create Organization Workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the **Home** page, click **Teams** and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit Workspace Details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### View Secret Scan Metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### Organization Settings

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives you greater control over your team's security posture and compliance requirements.

**Organization Managers** are responsible for creating Teams in the Organization and can manage any Team. They're also responsible for assigning individual Team Managers to the teams they create.

**Team Managers** can approve the adding of Members and the sharing of content from the Teams they manage.

**Collaborators** can be brought into the team as secondary contributors or consumers. For example, collaborators can be QA teams supporting the team's activities, consumers of the team's APIs, or an entire Organization. On teams that don't require approval, Collaborators can be added automatically. On teams that require approval, an Admin must approve the addition of Collaborators to keep parts of the team private while others are shared.

## Team Roles

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

**Notes:**
- Only a Team Member can create workspaces in the team.
- Sharing an element with a new user triggers the process of adding that user to the Team's user list.
- Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team’s shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

**To migrate your teams to Organizations, contact your Customer Success Manager.**

Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:
- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

### Create Organization Teams

To create an Organization Team, do the following:

1. Access **Organization Settings** in the Postman header, then select **Organization Teams** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.

**Notes:**
- If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
- You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/) relationship.

![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

## Create Organization Workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the **Home** page, click **Teams** and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
5. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
6. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
7. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
8. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit Workspace Details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### View Secret Scan Metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

---

### Organization Settings

**Postman Organizations** streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by