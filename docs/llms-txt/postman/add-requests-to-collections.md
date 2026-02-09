# Add API requests to Postman Collections

After you [create a Postman Collection](/docs/collections/use-collections/create-collections/), you can use it to save and organize API requests. Use any of the methods below to add requests to a collection. You can add HTTP requests to a collection, or you can add requests that use other protocols to a [multi-protocol collection](#about-multi-protocol-collections).

## Add a request to an empty collection

1. Select the collection in the sidebar.
2. Click ![Image 1: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) or **Add a request**.

    ![Image 2: Add a request to an empty collection](https://assets.postman.com/postman-docs/v11/add-new-request-v11.51.png)

3. Enter a name for the request.
4. Select the collection you want to save the request to.

    > To create a new collection to save the request to, click **New Collection**.
    
    ![Image 3: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

5. Click **Save**.

![Image 4: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 5: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 6: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.

    ![Image 7: Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)

4. Click ![Image 8: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
5. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
6. Click **Create**.

    ![Image 9: Create a component file](https://assets.postman.com/postman-docs/v11/component-library-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 10: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 11: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component file in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 12: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

> From a specification, you can also copy the URL to the latest version of a component. Click ![Image 13: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification. Then hover over a component and click ![Image 14: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy link**.

As you edit your specification, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 15: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 16: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component in the left sidebar that you'd like to version and publish.
5. Click **Version & Publish** in the upper right corner.

    ![Image 17: Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

6. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
7. Click **Create Version & Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

> You can't delete published versions of component files.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Image 18: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

## Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 19: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

## Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

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

1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

## Manage workspace scan policies

Use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 20: The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

* **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
* **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:

    * If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
    * If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.

    Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 21: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

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

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.

    ![Image 22: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 23: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:** * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 24: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)

Postman adds a new team file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.

    ![Image 25: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)

3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 26: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)

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

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.

    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 27: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 28: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.

    ![Image 29: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 30: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:** * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 31: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)

Postman adds a new team file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.

    ![Image 32: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)

3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 33: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)

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

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.

    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 34: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 35: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.

    ![Image 36: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 37: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:** * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 38: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)

Postman adds a new team file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.

    ![Image 39: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)

3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 40: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)

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

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.

    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 41: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 42: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
2. Click **Create Team**.

    ![Image 43: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 44: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)

4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:** * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 45: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)

Postman adds a new team file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.

    ![Image 46: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)

3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 47: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)

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

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.

    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 48: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 49: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/sl