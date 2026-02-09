# Assign input values with scenarios

_SCenarios_ are sets of values assigned to [**Start**](/docs/postman-flows/reference/blocks/start/) block inputs. You can define multiple scenarios with different values for inputs, and change between scenarios for different use cases. For example, scenarios are convenient when you're testing flow modules or actions that require the same inputs but different values for each test. They're also useful when you want to use different input values for a beta or production deployment.

## Start block inputs

You can [add inputs to the **Start** block](/docs/postman-flows/reference/blocks/start/#receive-data-with-inputs) to receive data from a scenario. The **Start** block can then pass that data to other blocks as key-value pairs. The key is the input's name and the value is any data received by the input.

## Create a scenario

When you add inputs to the **Start** block, you can assign them values with a scenario. Your flow module or action will then use the scenario's values when it runs. To create a scenario, do the following:

1. Create a new flow [module](/docs/postman-flows/get-started/build-your-first-flow/) or [action](/docs/postman-flows/build-flows/structure/actions/#create-an-action).
2. If you created a flow module, [add one or more inputs to your **Start** block.](/docs/postman-flows/reference/blocks/start/#receive-data-with-inputs)
3. In the right sidebar, click \u003cimg alt=\"Scenarios\" src=\"https://assets.postman.com/postman-docs/v11/flows-scenarios-icon-v11.png#icon\" width=\"16px\"\u003e **Scenarios** \u003e **Create scenario**. The scenario editor appears with editable fields for each input in the **Start** block.
4. Enter data for each input field.
5. Click **Save**.

## Run a flow module or action using scenario data

Once you've created a scenario, you can run the flow module or action using the scenario's data as values assigned to the **Start** block's inputs. To run a flow module or action using a scenario's data, do the following:

1. Click \u003cimg alt=\"Scenarios\" src=\"https://assets.postman.com/postman-docs/v11/flows-scenarios-icon-v11.png#icon\" width=\"16px\"\u003e **Scenarios**.
2. Hover over the scenario you want to use and click **Run**. The flow runs using data defined in the scenario.

## Secrets in scenarios

When adding inputs to the [**Start** block](/docs/postman-flows/reference/blocks/start/), you can designate an input as \u003cimg alt=\"Locked icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/state-locked-stroke.svg#icon\" width=\"16px\"\u003e **Secret** provided its value will be a string. Postman encrypts the values of **Secret** inputs and stores them securely, giving you a safe way to handle API keys or other sensitive values in your modules. Postman redacts them in run logs, **Output** blocks, and the Console, even when used in nested modules.

When you clone a module that has a secret input, the input appears in the **Start** block and scenarios pane, but its value is left blank and is never present in the clone.

In the Scenarios pane, inputs designated as \u003cimg alt=\"Locked icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/state-locked-stroke.svg#icon\" width=\"16px\"\u003e **Secret** in the **Start** block:

* Also have type \u003cimg alt=\"Locked icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/state-locked-stroke.svg#icon\" width=\"16px\"\u003e **Secret**.
* Are shown with their values masked by default.

What you can do with secret inputs depends on your permissions:

* Flow Editors can unmask secret inputs by clicking \u003cimg alt=\"View icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-view-stroke.svg#icon\" width=\"16px\"\u003e **Show**. They can create, edit, and save secret input values.
* Runners can run modules with secret inputs, but can't view their values. At runtime, Postman decrypts secret values if needed, without making them visible.
* Viewers can't run modules with secret inputs, and can't view the values of secret inputs.

## Edit a scenario

You can change and save the values in a scenario. To edit a scenario, do the following:

1. Click \u003cimg alt=\"Scenarios\" src=\"https://assets.postman.com/postman-docs/v11/flows-scenarios-icon-v11.png#icon\" width=\"16px\"\u003e **Scenarios**.
2. Hover over the scenario you want to edit and click **Edit**.
3. Enter new values in the input fields.
4. Click **Save**.

## Rename a scenario

You can change a scenario's name. To rename a scenario, do the following:

1. Click \u003cimg alt=\"Scenarios\" src=\"https://assets.postman.com/postman-docs/v11/flows-scenarios-icon-v11.png#icon\" width=\"16px\"\u003e **Scenarios**.
2. Hover over the scenario you want to delete and click \u003cimg alt=\"Options icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon\" width=\"16px\"\u003e the more actions icon \u003e **Rename**.
3. Enter a new name.
4. Press the **Return** or **Enter** key.

## Duplicate a scenario

You can make a copy of an existing scenario. To duplicate a scenario, do the following:

1. Click \u003cimg alt=\"Scenarios\" src=\"https://assets.postman.com/postman-docs/v11/flows-scenarios-icon-v11.png#icon\" width=\"16px\"\u003e **Scenarios**.
2. Hover over the scenario you want to delete and click \u003cimg alt=\"Options icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon\" width=\"16px\"\u003e the more actions icon \u003e **Duplicate**.
3. Click **Save**.

## Delete a scenario

To delete a scenario, do the following:

1. Click \u003cimg alt=\"Scenarios\" src=\"https://assets.postman.com/postman-docs/v11/flows-scenarios-icon-v11.png#icon\" width=\"16px\"\u003e **Scenarios**.
2. Hover over the scenario you want to delete and click \u003cimg alt=\"Options icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon\" width=\"16px\"\u003e the more actions icon \u003e **Delete**.

## Troubleshoot vault secrets

Vault secrets can be empty or unresolved in your HTTP requests. An *empty vault* secret is a vault secret that doesn't have a value but is referenced in your request. An empty vault secret may or may not exist in your Postman Vault. An *unresolved vault secret* is a vault secret that exists in your Postman Vault but the value can't be accessed from your request.

A vault secret in a cloud vault may be empty if the cloud vault's name was updated, but references to the vault secret use the previous cloud vault name. To fix this, update references to the vault secret with the correct cloud vault name.

To learn more about troubleshooting empty and unresolved vault secrets, see [Troubleshoot vault secrets](#troubleshoot-vault-secrets).

## Use vault secrets

You can reference vault secrets stored in your local vault or a cloud vault by adding the vault secret inside double curly braces (`{{ }}`) and append the prefix `vault:` to the vault secret's name. For example, to reference a vault secret named "postman-api-key", use the following syntax:

```txt
{{vault:postman-api-key}}
```

To reference a vault in a cloud vault, do the following:

1. Open the Postman workspace where you created the vault secret.
2. Select the vault secret in the left sidebar.
3. Choose a published version of the vault secret using the version dropdown list.
4. In the left sidebar, click \u003cimg alt=\"Link icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon\" width=\"16px\" role=\"img\"\u003e **Copy** next to a vault. This copies the URL to the version of the vault secret you select in the dropdown list.
5. Add the URL to a reference (`$ref`) in your specification.

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams and workspaces

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
7. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
8. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
9. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
10. Click **Create**.

After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.
4. Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click \u003cimg alt=\"Slack icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon\" width=\"16px\"\u003e \u003cimg alt=\"Teams icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon\" width=\"16px\"\u003e **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then click **Secret Scanner** in the left sidebar.
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

1. Click **Team** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about:

* [The Secret Scanner dashboard](/docs/reports/secret-scanner-reports/)