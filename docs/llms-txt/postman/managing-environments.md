# Group sets of variables in Postman using environments

In Postman, an _environment_ is a set of one or more [variables](/docs/sending-requests/variables/variables/) that you can reference when [sending requests](/docs/sending-requests/create-requests/create-requests/), [writing pre-request scripts](/docs/tests-and-scripts/write-scripts/pre-request-scripts/), or [writing post-response scripts](/docs/tests-and-scripts/write-scripts/test-scripts/). You can create environments for the different types of work you do in Postman. When you switch between environments, all of the variables in your requests and scripts will use the values from the current environment. This is helpful if you need to use different values in your requests depending on the context, for example, if you're sending a request to a test server or a production server.

## Create an environment

Create a new environment when you want to be able to change the values of variables depending on your work context in Postman, or to share values with other team members. You can also create a new environment from the environment selector, making it the active environment.

To create a new environment, do the following:

1. Select **Environments** in the sidebar and select ![Image 1: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon). You can also select the environment selector at the top right of the workbench and select ![Image 2: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon).
    
    ![Image 3: Create new environment](https://assets.postman.com/postman-docs/v10/environment-create-new-v10-20.jpg)
    
1. Enter a name for your new environment.
    
    ![Image 4: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
1. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:**
    > * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 5: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
2. Click **Create**.
    
    ![Image 6: Create Organization Team](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.
    
## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.
    
1. Click ![Image 7: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
    
    ![Image 8: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon)
    
1. Click ![Image 9: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
    
    ![Image 10: Components icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon)
    
1. Click **Open Component Library**.
    
    ![Image 11: Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)
    
1. Click ![Image 12: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
    
    ![Image 13: Add Component Library](https://assets.postman.com/postman-docs/v11/component-library-add-v11.png)
    
Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.
    
## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.
    
1. Click ![Image 14: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
    
    ![Image 15: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon)
    
1. Click ![Image 16: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
    
    ![Image 17: Components icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon)
    
1. Click **Open Component Library**.
    
    ![Image 18: Open Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)
    
1. Click a component file in the left sidebar.
    
    * If your team is smaller and doesn't use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
    * If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
    
2. Choose a published version of the component file using the version dropdown list.
    
    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.
    
    * The policy you select is automatically applied to the selected workspaces.
    
## View live documentation

Postman displays a live preview of your API's documentation as you edit your component file. To show the documentation preview, click ![Image 19: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Live preview** in the right sidebar. Click ![Image 20: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) **Close** to hide the documentation preview.
    
## Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.
    
> Postman also identifies governance issues for components, but only once they're [referenced in your specification](#reference-a-component-in-a-specification).
    
## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.
    
1. Click ![Image 21: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
    
    ![Image 22: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon)
    
1. Click ![Image 23: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
    
    ![Image 24: Components icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon)
    
1. Click **Open Component Library**.
    
    ![Image 25: Open Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.jpg)
    
1. Click a component in the left sidebar that you'd like to version and publish.
    
    * Click **Version & Publish** in the upper right corner.
    
    ![Image 26: Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)
    
1. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
    
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
    
    ![Image 27: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)
    
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
        
## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.
    
To access the report, do the following:
    
1. Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
    
    ![Image 28: Secret Scanner](https://assets.postman.com/postman-docs/v11/secret-scanner-v11.67.png)
    
    The settings enable you to do the following:
    
    * Create [Organization Teams](/docs/administration/organization/team-settings/).
    * Configure your [team settings](/docs/administration/managing-your-team/team-settings/).
    * Manage [team members](/docs/administration/managing-your-team/team-members/overview/).
    * Manage [team resources](/docs/administration/managing-your-team/manage-team-workspaces/).
    * Manage [product access](/docs/administration/managing-your-team/manage-team-product-access/).
    * Manage [security](/docs/administration/managing-your-team/overview/#secure-your-postman-team).
    
    Learn more about:
    
    * [Creating organization teams and workspaces](/docs/administration/organization/create/)
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)