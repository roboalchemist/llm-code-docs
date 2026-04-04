# Prepare your public workspace for the Postman API Network

Your public workspace is a landing page for your public APIs. It's where API consumers find your public APIs, learn about them, and can [fork your public collections to their own workspace](/docs/collaborating-in-postman/using-version-control/forking-elements/), where they can start using them.

Before you [make your workspace public](/docs/postman-api-network/showcase/publish/public-apis/#make-your-workspace-public), you'll prepare it, [prepare your public collections](/docs/postman-api-network/showcase/prepare/public-collections/), [curate them](/docs/postman-api-network/showcase/prepare/curate/overview/), and [prepare your team workspace for team collaboration](/docs/postman-api-network/showcase/prepare/team-workspace/).

## Create your public workspace

Depending on your team's workflow, you can create a private or team workspace (you'll make it public later). If you want to limit access to invited team members, create a private workspace. If you want to invite everyone from your team, create a team workspace.

You'll make your workspace public when you're ready to [publish your public APIs to the Postman API Network](/docs/postman-api-network/showcase/publish/public-apis/).

To create your public workspace, do the following:

1. From the Postman header, click **Workspaces** > **Create Workspace**.
2. If you want to use a [workspace template](/docs/collaborating-in-postman/using-workspaces/create-workspaces/#apply-a-template-to-a-workspace), select one.
3. Click **Next**.
4. Name your workspace.
5. Click ![Image 1: Team icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-team-stroke.svg#icon) **Internal**. Then, click **Everyone in *team*** or **Only you and invited people**.
6. Click **Create**.

To learn more, see [Create a workspace in Postman](/docs/collaborating-in-postman/using-workspaces/create-workspaces/).

## Invite team members to your workspace

To invite team members to your workspace, do the following:

1. From the Postman header, click ![Image 2: Invite icon](https://assets.postman.com/postman-docs/aether-icons/action-invite-stroke.svg#icon) **Invite**.
2. Use the available options, such as email, to invite your team members.
3. Choose a role for your team members.
4. Click **Invite**.

You can continue to invite team members as your workspace, its collections, and your public APIs evolve.

To learn more, see [Share workspace](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#share-workspaces).

## Edit your workspace details

To edit your workspace details, do the following:

1. If your workspace's ![Image 3: Overview icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-overview-stroke.svg#icon) **Overview** tab isn't open, from the Postman sidebar, click your workspace's name.
2. Under **Workspace description**, add a description.
3. Under **About**, add a summary.
4. If you're on the Postman Enterprise plan, under **Tags**, add tags.

You can continue to edit your workspace details as your workspace, its collections, and your public APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Postman Vault integrations

Postman's Local Secret Protection is available with [Postman Enterprise plans](https://www.postman.com/pricing/).

With the Secret Scanner's Local Secret Protection, [Team Admins](/docs/administration/roles-and-permissions/#team-roles) can configure where Postman stores the team's exposed secrets in the workspaces or types of workspaces you've defined.

When [enabled](#enable-local-secret-protection), Postman scans secrets in real time and takes action, storing exposed secrets, like API keys, JWT tokens, or auth tokens, in the [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/). The Postman Vault stores your exposed secrets securely on your device. The original secret value is replaced with a vault secret reference. This prevents your team's secrets from syncing to the Postman cloud and gives you greater control over your team's security posture and compliance requirements.

Postman's Local Secret Protection actively scans for secrets in the following Postman elements when changes are made:

- HTTP collections
- Environments variable values
- Global variable values

Local Secret Protection requires Postman version 11.71.3 or later.

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click ![Image 4: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Team** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 5: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** > **Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.
- Any endpoint errors reported during a performance test.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Connect Zoom to your Flows action

You can connect [Zoom](https://www.zoom.com/) to a flow with the Zoom **Connector** block. Use this block to perform the following operations:

- Create Meeting
- Update Meeting
- Get Meeting
- Get Meeting By ID
- Delete Meeting
- Add Meeting Registrant
- Get Meeting Registrant
- Delete Meeting Registrant
- Get Recording By Meeting ID
- Search Recording
- Create Folder
- Move Folder
- Get Folder By ID
- Search Folders
- Delete Folder
- Download File

To connect Zoom to a Flows action, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
2. Click ![Image 6: Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon) **Delete**.
3. Right-click the canvas and select **Zoom** from the list of blocks.
4. Click **Select an operation...** and select the operation you want the action to perform.
5. Click **Select an account...** and follow the prompts to connect your Zoom account.
6. Connect the **Request** block's output ports to the Zoom **Connector** block's input ports, based on the selected operation.
7. Connect the Zoom **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

![Image 7: Connect Zoom to your Flows action](https://assets.postman.com/postman-docs/v11/zoom-connector-v11.67.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 8: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 9: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.

![Image 10: Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)

1. Click ![Image 11: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
2. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
3. Click **Create**.

![Image 12: Create a component file](https://assets.postman.com/postman-docs/v11/component-library-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 13: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 14: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component file in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 15: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Image 16: Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your component file, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

- When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
- When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams and workspaces

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team's contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click ![Image 17: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 18: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

- When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
- When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Team** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team's contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click ![Image 19: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 20: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

- When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
- When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Team** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team's contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click ![Image 21: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 22: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

- When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
- When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Team** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team's contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click ![Image 23: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 24: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

- When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
- When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Team** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    - **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    - **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team's contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click ![Image 25: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 26: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

- [Organization roles](/docs