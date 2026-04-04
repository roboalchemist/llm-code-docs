# use-collections-overview

Create and manage request collections in Postman
-----------------------------------------------

A collection is one of the fundamental elements in Postman. Use collections to save all your API requests, keep them organized, and find them when you need them. When you're ready, you can share your collections with other members of your team–or anyone in the world.

## Create new collections

Create a new Postman Collection to save requests you use often, or to group requests for a specific purpose, such as testing APIs or simulating workflows. You can create a collection from scratch or from one of Postman's predefined templates. To learn more, go to [Create collections of API requests in Postman](/docs/collections/use-collections/create-collections/).

## Add API requests

You can save new API requests to a collection, or move existing requests into a collection. A collection can contain HTTP requests, or you can create a multi-protocol collection with other types of requests, such as GraphQL or gRPC. To learn more, go to [Add API requests to Postman Collections](/docs/collections/use-collections/add-requests-to-collections/).

## Keep your collections organized

You can arrange the API requests in a collection in any order you choose, or add folders to group requests together. If you make a change you don't like, or delete a collection by mistake, you can restore it back to an earlier state. To learn more, go to [Manage and organize Postman Collections](/docs/collections/use-collections/manage-collections/).

## Collaborate with others

You can share collections to invite others to collaborate with you, or watch a collection to get notified about changes. Tag collections to make them easier for others to find, and add comments to a collection to let others know what you're thinking. You can also apply status tags to a collection to show its lifecycle status. To learn more, go to [Share and collaborate on Postman Collections](/docs/collections/use-collections/collaborate-with-collections/).

## Create Organization Teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don't necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

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

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.
* The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:
    * The total number of detected secrets automatically moved to the Postman Vault.
    * The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about: [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default