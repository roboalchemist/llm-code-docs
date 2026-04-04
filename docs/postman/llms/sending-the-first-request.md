# Send your first API request

Postman's API client enables you to create and send API [requests](/docs/getting-started/basics/postman-elements/#requests), including HTTP, GraphQL, and gRPC requests. Using Postman, you can send a request to an endpoint, retrieve data from a data source, or test an API's functionality. You don't need to enter commands in a terminal or write any code. When you create a new request and click **Send**, the API response returns directly in Postman.

## Send an API request

Make sure you've [downloaded and installed the Postman desktop app](/docs/getting-started/first-steps/get-postman/). When you're ready, open the Postman desktop app and send your first API request.

1. Click ![Image 1: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add** in the workbench to open a new [tab](/docs/getting-started/basics/navigating-postman/#tabs).
2. Enter "postman-echo.com/get" for the request URL.
3. Click **Send**.

Postman displays the response data sent from the server in the lower pane.

![Image 2: Sending a request](https://assets.postman.com/postman-docs/v11/send-first-request-v11-71-7.jpg)

## How it works

In this example, Postman acts as the client application and communicates with an API server. Here's what happened when you clicked **Send**:

1. Postman sent a GET request to the [Postman Echo API](/docs/developer/echo-api/) server located at `postman-echo.com`.
2. The API server received the request, processed it, and returned a response to Postman.
3. Postman received the response and displayed it in the **Response** pane.

You used Postman to send an API request and got a response from the API server.

## Next steps

You've sent your first API request, and you're ready to do more with Postman!

* Send more requests to the Postman Echo API, a handy tool you can use to test API requests in Postman. To learn more about using the Echo API, see the [Postman Echo API documentation](/docs/developer/echo-api/).
* When you're ready to learn more about building and sending requests in Postman, see [Create and send API requests in Postman](/docs/sending-requests/create-requests/create-requests/).

## Troubleshoot vault secrets

You can reference vault secrets stored in your Postman Vault by adding the vault secret inside double curly braces (`{{vault:secret-name}}`) and appending the prefix `vault:` to the vault secret's name. For example, to reference a vault secret named "postman-api-key", use the following syntax:

```txt
{{vault:postman-api-key}}
```

To reference a vault secret in your local vault or a cloud vault, put the vault secret inside double curly braces (`{{vault:secret-name}}`) and append the prefix `vault:` to the vault secret's name. For example, to reference a vault secret named "postman-api-key" in a cloud vault named "postman_engineering", use the following syntax:

```txt
{{vault:postman_engineering/postman-api-key}}
```

To learn more about troubleshooting empty and unresolved vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).

## Postman Vault integrations

Integrate your Azure API Gateway with Postman Collections and streamline your testing workflow. The Azure API Gateway app enables developers to troubleshoot and reproduce issues in deployed environments.

## Import APIs from Azure API Gateway to Postman

Before you get started with creating a collection from an imported API, connect your Azure API Gateway to Postman. You can select an API to troubleshoot or test, and create a collection from the information available in the API gateway. To learn more, see [Connect your Azure API Gateway to Postman](#connect-your-azure-api-gateway-to-postman).

## Create collections in Postman from Azure Gateway APIs

Collections created using the API gateway app contain the latest data from the deployed environment. This lets you keep collaborative workspaces up to date by bringing runtime API information to a collection. To learn more, see [Create a collection from an imported API](#create-a-collection-from-an-imported-api).

## Connect your Azure API Gateway to Postman

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

The new installed app appears on the Installed apps page with the status as **Connected**.

## Create a collection from the Azure API Gateway app

You can select an API to troubleshoot or test, and create a collection from the information available in the API gateway. Collections created using the API gateway app contain the latest data from the deployed environment. This lets you keep collaborative workspaces up to date by bringing runtime API information to a collection.

To create a collection from an imported API, do the following:

1. After setting up the connection, you can create a new collection.
2. Click **Collections**, then select **Create from Azure**.
3. In the **Create a new collection from API gateway** popup window, enter the following information:
    * Select an API from the gateway.
    * Select the stage on which the API is deployed.
    * Create an environment (optional). This creates a new environment on Postman for the API variables from the gateway.

4. Click **Create collection**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/organization/roles/#edit-workspace-details).

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click ![Image 3: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Secret Scanner** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also update the policy for workspaces to their default, which is to use the **No policy** option and store detected secrets in the Postman cloud. Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also update the policy for workspaces to their default, which is to use the **No policy** option and store detected secrets in the Postman cloud. Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

To reference a component file, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.
4. In the **Create a new collection from API gateway** popup window, enter the following information:
    * Select an API from the gateway.
    * Select the stage on which the API is deployed.
    * Create an environment (optional). This creates a new environment on Postman for the variables associated with the selected API.

5. Click **Create collection**.

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your specification, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) in your specification.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Organization settings

_Postman Organizations_ streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives each team better control over its membership.

### Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 4: Organization settings](https://assets.postman.com/postman-docs/v11/organization-settings-v11.67.png)
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.

![Image 5: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.

1. Populate the team with the members who are responsible for the team’s contents.
2. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
3. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
4. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
5. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/organization/roles/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click ![Image 6: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 7: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization settings](/docs/administration/organization/settings/)
* [Team roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
* [Organization settings](/docs/administration/organization/settings/)
*