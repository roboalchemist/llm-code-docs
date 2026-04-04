# SCIM provisioning overview

> **[Provisioning with SCIM is available with Postman Enterprise plans.](https://www.postman.com/pricing/)**

Postman supports [SCIM](https://datatracker.ietf.org/doc/html/rfc7642) (System for Cross-domain Identity Management), enabling you to automate user provisioning and de-provisioning for your team. With this feature, you can efficiently deploy Postman at scale across your organization and control access to it with your identity provider (IdP). You can enable SCIM provisioning with the [SCIM API](#configuring-scim-with-the-scim-api), [Okta](/docs/administration/scim-provisioning/configuring-scim-with-okta/), [Microsoft Entra ID](/docs/administration/scim-provisioning/configuring-scim-with-azure-ad/), or [OneLogin](/docs/administration/scim-provisioning/configuring-scim-with-onelogin/).

You must be a [Postman Team Admin or Super Admin](/docs/administration/roles-and-permissions/#team-roles) to enable SCIM for your team. A SCIM key belonging by a Team Admin can be used to provision and de-provision users through SCIM. However, the SCIM key belonging by a Team Admin can't be used to de-provision a Super Admin. Also, account email updates only work if the SCIM key belongs to a user with the Super Admin role.

To ensure complete functionality, you can assign the SCIM key to a user with the Super Admin role. Alternatively, you can create a service account and assign it the Super Admin role, avoiding the risk of service disruption in case a team member leaves the company. Learn more about [assigning the Super Admin role to a service account](/docs/administration/enterprise/enterprise-onboarding/#the-super-admin-role).

With SCIM enabled, users won't have the option to leave your team on their own, and won't be able to change their account email or password. Only Team Admins and Super Admins have permission to remove team members. Only administrators in your IdP have permission to use SCIM to change user account emails if they're associated with a domain your team verified.

With [domain verification](/docs/administration/domain-verification-and-capture/add-and-verify-a-domain/), you can do the following:

* Onboard users faster, by not requiring the [account linking](/docs/getting-started/account/manage/#link-your-account-to-postman) step.
* Update users' emails using SCIM if the user account email domain matches a domain your team verified.

## SCIM features

Postman supports the following provisioning features:

* **Create user** - Creates a new user account in Postman, adds the account to your organization's Postman team, and activates authentication for the user if their email ID isn't attached to an existing Postman account. If a Postman account with the same email ID exists and it's associated with a domain your team has verified, the user will be automatically added to your team. If a Postman account with the same email ID exists, and it's not associated with a verified domain, an email invite to join your Postman team is sent to the user. Once the user accepts the invite, they'll be added to your team.
  
    > The newly added user will have the Developer role in Postman by default. You can later [update account roles in Postman](/docs/administration/managing-your-team/team-members/manage-roles/).
  
* **Update user information**
  
    * **Update user attributes** - Updates a user's first and last name in Postman.
    
    * **Activate user** - Creates a new user on your Postman team, if one doesn't already exist, and activates the user to authenticate into your Postman team.
    
    * **Deactivate user** - Removes a user from your Postman team and deactivates their account, blocking the account from authenticating into Postman.
    
        > User accounts and the data corresponding to them won't be deleted.
    
    * **Reactivate user** - Reactivates an existing deactivated user by unblocking the account's authentication into Postman and adds the account back to your Postman team.
  
* **Create group** - Creates a new [user group](/docs/administration/managing-your-team/user-groups/) in Postman. When you assign the Postman app to a group, Postman creates a new account for each user, adds each account to your organization's Postman team, and activates authentication for each user. If an existing Postman account uses an email that matches a user's email ID, an [email invite](/docs/administration/managing-your-team/team-members/invite-members/#manage-invites) to join your Postman team is sent to that user. Once the user accepts the invite, they'll be added to your team.
  
    > Newly created groups will have the Developer role in Postman by default. You can later [update group roles in Postman](/docs/administration/managing-your-team/user-groups/#editing-team-roles-for-a-group) and [control a group's access to workspaces and individual Postman elements](/docs/administration/managing-your-team/user-groups/#managing-roles-on-workspaces-and-postman-elements), such as collections and APIs.
  
* **Delete group** - Deletes a user group in Postman. User accounts that were part of the deleted group are deactivated in Postman.
  
    > User accounts and the data corresponding to them won't be deleted.
  
* **Update group information**
  
    * **Update group attributes** - Updates a group's name in Postman.
    
    * **Update group members** - Adds or removes users from a group in Postman.
  
* **Set user roles** - Use SCIM to assign roles to users by [creating a user group](/docs/administration/managing-your-team/user-groups/#creating-a-group) in Postman, then assigning roles to the group. When you add users to the group using SCIM, users will get the roles assigned to the group. Learn how to [update team roles for groups](/docs/administration/managing-your-team/user-groups/#editing-team-roles-for-a-group), and [update workspace and elements roles for groups](/docs/administration/managing-your-team/user-groups/#managing-roles-on-workspaces-and-postman-elements).
  
Postman doesn't support the following provisioning features:
* Push groups from Postman to your IdP
* Push or sync password updates
* Push user attribute updates from your IdP to Postman other than name
* Pull user attribute updates from Postman to your IdP

## Enabling SCIM provisioning

You must [configure SSO in Postman](/docs/administration/sso/admin-sso/) before you can enable SCIM for your Postman team.

You can use SCIM with multiple SSO method configurations. To enable SCIM with multiple SSO, contact your customer success manager.

### Enabling SCIM in Postman

1. Open Postman and select **Team > Team Settings** in the Postman header.
2. Click **Authentication** in the left sidebar.
3. Click **Authentication Methods**.
4. Select the **SCIM Provisioning** toggle to turn it on.

    ![Image 1: Enable SCIM in dashboard](https://assets.postman.com/postman-docs/v10/auth-enable-scim-v10-19.jpg)

1. Click **Turn On** to enable SCIM provisioning.

    ![Image 2: Enable SCIM in dashboard](https://assets.postman.com/postman-docs/v10/turn-on-scim-provisioning-v10-19.jpg)

### Generating SCIM API key

1. Under **SCIM Provisioning**, click **Generate SCIM API Key**.

    ![Image 3: Generate SCIM API key](https://assets.postman.com/postman-docs/v10/generate-scim-api-key-v10-19.jpg)

1. Enter a key name, then click **Generate**.
1. Copy your new API key for later use and click **Done**.

You can revisit this page to manage your SCIM API keys. If you regenerate an existing API key, you'll have the option to keep the previous key active while you switch to the new one.

For more information or help with configuring SCIM, [contact Postman support](https://www.postman.com/support/).

## Configuring SCIM with the SCIM API

Visit Postman's [SCIM API documentation](https://www.postman.com/postman/postman-public-workspace/folder/l6yozde/scim) for information on setting up SCIM for your Postman team using the SCIM 2.0 API.

## Next steps

After the SCIM setup is complete, learn how to manage roles and permissions for your team:

* To learn how to enable SCIM provisioning through your IdP, see [Configure SCIM with Okta](/docs/administration/scim-provisioning/configuring-scim-with-okta/), [Configure SCIM with Microsoft Entra ID](/docs/administration/scim-provisioning/configuring-scim-with-azure-ad/), or [Configure SCIM with OneLogin](/docs/administration/scim-provisioning/configuring-scim-with-onelogin/).
* To learn how to enable SCIM using the SCIM 2.0 API, see Postman's [SCIM API documentation](https://www.postman.com/postman/postman-public-workspace/folder/l6yozde/scim).
* Learn more about [defining roles](/docs/administration/roles-and-permissions/) in your team and how to [create user groups](/docs/administration/managing-your-team/user-groups/#creating-a-group).

---

**Tip:** Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

---

**Note:** The component library doesn't support AsyncAPI specifications or [the Postman CLI](/docs/postman-cli/postman-cli-options/#postman-spec-lint).

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Teams** in the left sidebar.
2. Click **Create Team**.
   
    ![Image 4: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
   
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
   
    ![Image 5: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
   
4. Click **Add Members**. To be added, members need to be part of the organization.
   
    > **Notes:**
    > * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
   
    ![Image 6: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
   
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
   
    ![Image 7: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
   
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
   
    ![Image 8: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
   
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

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
2. Click **Post an Update**.
3. Enter a title and a description of your update.
4. Select **Announcement** from the dropdown list.
5. (Optional) Add a summary describing the change.
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
   
    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 9: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 10: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
   
Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** To get started using Postman within your organization, you can walk through the following tasks to set your Postman team up for success.

---

**Note:** If you're on a Free individual plan, create a new team to connect to a remote repository.

---

**Note:** You can't delete component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the Documentation preview, do the following:

1. Under **Documentations** in the left sidebar, click **Documentations**.
2. Click **Preview**.
3. Click **Preview** again to see the live documentation preview.

### Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

> Postman also identifies governance issues for components, but only once they're [referenced in your specification](#reference-a-component-in-a-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click **Documentations** in the left sidebar, then click **Components**.
2. Click **Open Component Library**.
3. Click a component file in the left sidebar.
4. Choose a published version of the component file using the version dropdown list.
5. In the left sidebar, click ![Image 11: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
6. Add the URL to a reference (`$ref`) in your specification.

> From a specification, you can also copy the URL to the latest version of a component. Click ![Image 12: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification. Then hover over a component and click ![Image 13: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy link**.

As you edit your specification, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

---

**Tip:** To get started using Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 14: The Local Secret Protection interface](https://assets.postman.com/postman-docs/v11/local-secret-protection-interface-11-1.jpg)

Postman's automatic secret protection policy offers the following options:

* **No policy** - Ignores any secrets detected by the Secret Scanner and stores them in the Postman cloud. Secret Scanner performs no automated actions or notifications. Partner and internal workspaces use this policy by default.
* **Move to vault** - Automatically moves detected secrets to the Postman Vault. Secrets stored in the Postman Vault aren't synced to the Postman cloud, and the original secret value is replaced with a [variable reference](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) to the vault secret. Public workspaces use this policy by default. Users are notified when Postman detects an exposed secret:

    * If the user's vault is unlocked, they'll receive a notification that their secrets were moved to and secured in their Postman Vault. Users can click **Got it** to dismiss the message, or request to override the policy.
    * If the user's vault is locked, they'll receive a notification to unlock their vault. They can review the detected secrets, then click **Unlock Vault** to move them to their vault. Or, users can click **Ignore** to dismiss the notification, but they'll be required to unlock their vault and move the detected secrets to their vault before they can save their secrets.
    * Users can choose to request a policy override for a detected secret if they click **Override policy** in the notification. They must select a justification to submit to the Team Admin, then click **Override** to submit it.

### Set default detection policies for workspace types

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 15: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 16: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

---

**Tip:** To get started with Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default policy for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 17: Set default policy for new workspaces](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

---

**Tip:** To get started with Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default policy for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 18: Set default policy for new workspaces](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

---

**Tip:** To get started with Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default policy for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 19: Set default policy for new workspaces](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

---

**Tip:** To get started with Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default policy for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 20: Set default policy for new workspaces](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

---

**Tip:** To get started with Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default policy for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can also use the **Search workspaces** text box to search for and select workspaces, or use the **Created by** dropdown list to filter by specific users. You can also use the **Type** dropdown list to filter workspaces by their [visibility](/docs/collaborating-in-postman/using-workspaces/overview/#workspace-types):

* **Public** - [Public](/docs/collaborating-in-postman/using-workspaces/public-workspaces/) workspaces are visible to everyone in the Postman community.
* **Partner** - Only invited team users and partners have access to [Partner Workspaces](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/).
* **Internal** - [Internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/overview/) workspaces are visible to only you or your team.

![Image 21: Set default policy for new workspaces](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

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

---

**Tip:** To get started with Postman in VS Code, choose the supported application where you'd like to install the Postman VS Code extension.

---

**Note:** You can't delete published versions of component files.

### Set default policy for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific