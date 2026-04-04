# postman-cli-overview

Explore Postman's command-line companion
----------------------------------------

The Postman CLI is a secure command-line companion for Postman. It's signed and supported by Postman, like the Postman app. The Postman CLI supports the following features:

* [Sign in and sign out of Postman](/docs/postman-cli/postman-cli-options/#sign-in-and-out) from the command line.
* [Validate, synchronize, and push local collections and environments](/docs/postman-cli/postman-cli-options/#sync-local-elements-with-workspaces) to Postman workspaces in the cloud.
* [Run a collection](/docs/postman-cli/postman-cli-run-collection/) with its collection ID or path, and send the run results to the Postman cloud by default.
* [Run a monitor](/docs/postman-cli/postman-cli-run-monitor/) in the Postman cloud with its monitor ID.
* [Start a runner](/docs/postman-cli/postman-cli-run-monitor/) in your internal network to monitor APIs with private endpoints.
* Generate a local collection run report with [built-in reporters](/docs/postman-cli/postman-cli-reporters/).
* [Check API definitions](/docs/postman-cli/postman-cli-options/#governance-and-security) against configured API governance and API security rules.

The Postman CLI requires a valid Postman API key. For more information, see [Generate and use Postman API keys](/docs/developer/postman-api/authentication/).

## Comparing the Postman CLI and Newman

The table below shows a high-level comparison of the Postman CLI and [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

| Postman CLI  | Newman  |
|---|---|
| Created by Postman | Created by Postman |
| Maintained and supported by Postman | Open source; supported by community contributions |
| Supports collection runs | Supports collection runs |
| Automatically sends collection run results to Postman by default | Supports ingesting run results to Postman using a reporter |
| Package is signed by Postman | Package isn't signed by Postman |
| Distributed as a downloadable package | Distributed on npm |
| Downloadable programmatically | Downloadable programmatically |
| Not available as a library | Available as a library |
| Supports sign in and sign out | Doesn't support sign in and sign out |
| Checks API specifications against your configured API governance and API security rules | Doesn't check API specifications against your configured API governance and API security rules |

## Decide which command-line companion to use

You can use the Postman CLI or Newman to run and test collections from the command line. One may be a better fit, depending on your use case or preferences.

For example, assume you already manage your own security for open-source software, and you want to run collections from a script. Also assume you want visibility into any software you build into your CI/CD pipeline. Newman would be a good fit for this use case because Newman's repository is public and Newman isn't signed or secured by Postman.

Here's another example. Assume you don't already support or secure any open-source software, and you want the software you use to be signed and secured by its developer. The Postman CLI would be a good fit for this use case because the Postman CLI is signed and secured by Postman.

Learn how to [install the Postman CLI](/docs/postman-cli/postman-cli-installation/).

## About the Postman CLI and Postman API usage

Some Postman CLI commands use the [Postman API](/docs/developer/postman-api/intro-api/) to fetch data from and send data to Postman's servers. These commands count toward your monthly [Postman API usage](/docs/billing/resource-usage/#postman-api-usage). The number of Postman API calls you can make each month depends on your [Postman plan](https://www.postman.com/pricing/).

The following Postman CLI commands make calls to the Postman API and count toward your Postman API usage:

* `postman login` - Uses one call to authenticate a user with a Postman API key.
* `postman collection run` - Uses one call to fetch a collection by ID, one call to fetch an environment (if any), and one call to send data back to Postman.
* `postman monitor run` - Uses one call to fetch a monitor by ID, one call to start a monitor run, and multiple calls that poll Postman for the run's completion.
* `postman spec lint` - Uses one call to fetch the API governance rules and one call to send a report back to Postman.
* `postman api lint` - Uses one call to fetch the API governance and security rules and one call to send a report back to Postman.

Learn more about [Postman CLI command options](/docs/postman-cli/postman-cli-options/).

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

1. Click **Next**.
The new installed app appears on the Installed apps page with the status as **Connected**.

To create a new collection, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).

## Create Organization teams and workspaces

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).

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

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original teamâs shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

### Determine the structure of your teams and memberships

A team within an Organization represents physical members of a functional team, for example, developer or test team, and also contains the workspaces that the group of users wants to keep secure and access controlled.

By creating teams and memberships first, you can establish strategic collaborations and empower your teams to migrate their own work to their teams. For example, even if your QA team hasn't moved all their workspaces to a QA-designated team yet, other teams can still invite the QA team members to collaborate with their team.

Once you define the teams, you can start the process of improving collaboration and security by populating the teams with your workspaces.

To determine the team membership, do the following:

1. The [Organization Manager (or Super Admin)](/docs/administration/organization/roles/) creates a Team and assigns a Team Manager to it.
2. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** â Turn on if you want to strictly control access to Teams and tightly control the teamâs membership. Environments open to collaboration donât necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** â Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
3. Populate the team with the members who are responsible for the teamâs contents.
* If your team is smaller and doesnât use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
* If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
* **Notes**:
    * Only a Team Member can create workspaces in the team.
    * Sharing an element with a new user triggers the process of adding that user to the Team's user list.
    * Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).
* The team membership can continue to grow and change, and the users with edit access to the Teamâs workspaces will adapt accordingly.
* Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
![Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
![Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
5. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
![Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
![Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
5. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
![Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
![Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
5. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
![Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
![Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
5. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
![Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
4. Click **Add Members**. To be added, members need to be part of the organization.
* **Notes**:
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
![Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
5. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/local-secret-protection.md).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior