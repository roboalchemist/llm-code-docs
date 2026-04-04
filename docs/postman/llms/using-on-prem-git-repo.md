# Connect to an on-premises Git repository in the Postman API Builder

**[GitHub Enterprise Server, GitLab Self-Managed, and Azure DevOps Server (hosted on-premises) integrations are available with Postman Enterprise plans with the API Builder add-on.](https://www.postman.com/pricing/)**

You can connect your API to an on-premises Git repository to sync your API definition and collections between Postman and the repository. Postman supports connecting to GitHub Enterprise Server, GitLab Self-Managed, or Azure DevOps Server repositories.

After connecting, you can push and pull changes between Postman and branches in the remote repository. When it's time to release, you can publish an API version to make your changes available to consumers.

## Using an on-premises repository overview

If you are on a [Postman Enterprise plan with the API Builder add-on](https://www.postman.com/pricing/), you can connect an API in Postman to your on-premises Git repository. This enables you to sync changes between the repository and Postman.

To connect to [GitHub Enterprise Server or GitLab Self-Managed](#connecting-to-github-enterprise-server-or-gitlab-self-managed), create a new installed app in Postman. To connect to [Azure DevOps server](#connecting-to-azure-devops-server), use a personal access token.

Keep in mind the following when connecting to an on-premises repository:

* **You must be on a [Postman Enterprise plan with the API Builder add-on](https://www.postman.com/pricing/) to connect to a repository hosted on-premises.** If you're not on a Postman Enterprise plan with the API Builder add-on, you won't be able to connect to GitHub Enterprise Server, GitLab Self-Managed, or Azure DevOps Server. You can still [connect to a cloud-hosted repository](/docs/design-apis/api-builder/versioning-an-api/using-cloud-git-repo/).
* **You must use the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/) to connect to GitHub Enterprise Server, GitLab Self-Managed, or Azure DevOps Server.** You can't use the [Postman web app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-web-app) to connect to an on-premises GitHub repository.
* **All communication is between the Postman desktop app on your computer and the on-premises repository.** Your computer must be able to access the repository. No Git requests go through Postman's cloud servers. The Postman desktop app connects directly to your Git server, and you don't need to allow any Postman IP addresses for your repository. The repository will show the IP address of your computer as the source for all Git requests.
* **You can connect one or more APIs to a remote repository.** You can keep your APIs separate in the repository using files or branches. Learn more about [connecting more than one API to the same repository](/docs/design-apis/api-builder/versioning-an-api/connecting-multiple-apis/).

## Connecting to GitHub Enterprise Server or GitLab Self-Managed

To connect to a repository hosted in GitHub Enterprise Server or GitLab Self-Managed, [create an installed app](#creating-an-installed-app) in Postman. To complete this process, you'll also need to create an OAuth app in GitHub Enterprise Server or GitLab Self-Managed. You need to complete this process once for a domain URL. After you create the installed app, anyone on the team can use it to [connect to repositories using the same domain URL](#connecting-an-api-using-an-installed-app).

### Creating an installed app

[Installed apps](/docs/integrations/installed-apps/) streamline the process of adding integrations by enabling all members of a team to use the same stored authorization details. To create an installed app, you must have the [Team Admin role](/docs/administration/roles-and-permissions/#team-roles).

To create an installed app for GitHub Enterprise Server or GitLab Self-Managed, do the following:

1. In Postman, open [Team Settings](https://go.postman.co/settings/team/general) by selecting **Team \u003e Team Settings**.
2. Click **Installed apps**.
3. Select the repository provider you want to add an installed app for (**GitHub Enterprise Server** or **GitLab Self-Managed**).
4. Enter a **Name** to help you recognize the installed app later.
5. Enter the domain URL of your repository. Format the domain URL as follows:
   
   * **GitHub Enterprise Server** - Use the base URL of your Git server, for example: `https://my-github-server.example.com`
   * **GitLab Self-Managed** - Use the base URL of your Git server, for example: `https://gitlab.example.com`

6. Create an OAuth app by following the instructions for your Git provider ([GitHub Enterprise Server](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) or [GitLab Self-Managed](https://docs.gitlab.com/ee/integration/oauth_provider.html)). Use the following values:
   
   * **Homepage URL** - Enter the Postman homepage URL: `https://www.postman.com`
   * **Authorization callback URL** or **Redirect URI** - Enter the authorization callback URL provided in Postman: `https://integration-oauth.pstmn.io/v1/api-git-callback.html`
   * **Scopes** - Make sure to select the appropriate scopes when creating the OAuth app to enable Postman to read and write to your repository. For GitHub, select the `repo` and `user` scopes. For GitLab Self-Managed, select the `api` scope.

7. After registering the OAuth app, copy the app's **Client ID** and **Client secret** and enter them in Postman.
8. Click **Save** to finish creating the installed app.

![Image 1: Creating an installed app](https://assets.postman.com/postman-docs/v10/api-builder-add-installed-app-v10-12b.png)

### Connecting an API using an installed app

After you [create an installed app](#creating-an-installed-app), any API editor on the team can use it to connect an API to GitHub Enterprise Server or GitLab Self-Managed.

To connect an API using an installed app, do the following:

1. Click **APIs** in the sidebar and select an API.
2. Under **Connect repository**, click **Connect** and select **GitHub Enterprise Server** or **GitLab Self-Managed**.
3. Select the authorized domain of your repository and click **Authenticate**.

    ![Image 2: Using an installed app](https://assets.postman.com/postman-docs/v10/api-builder-use-installed-app-v10-12.jpg)

4. A browser tab opens asking you to sign in to your repository. Follow the onscreen instructions. When you're finished, close the browser tab and return to Postman.
5. For GitHub, enter the **Organization** and the **Repository** where the API will be stored. For GitLab, enter the **Group** and **Project** for your API.
6. Select the **Initial branch** for the API. Any changes you make in Postman are stored in the initial active branch. (You can switch to another branch to make it the active branch at any time.)
7. Select an **API schema file** to add to your API. If you're working on a [multi-file API definition](/docs/design-apis/api-builder/develop-apis/defining-an-api/#work-with-multi-file-api-definitions), make sure to select the [root definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#about-root-files) in your repository. The root file is the base file that has references to other files in the API definition. If you leave this field blank, no definition files are added to your API. You can [manually add a definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-an-api-definition-from-a-connected-repository) from your repository later.
8. Select a **Collection directory** where the collections linked to your API will be stored in the repository. If you leave this field blank, a `postman/collections` directory will be created in the root of the repository.
9. Click **Connect Repository**.

    The root definition file you selected is added to your API. For OpenAPI 2.0 and 3.0 APIs, Postman scans for any dependent files referenced in the root definition file and automatically adds them to your API. You can also [manually add more definition files](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-files-from-a-connected-repository) from your repository as needed.

## Connecting to Azure DevOps Server

To connect an API to a repository hosted in Azure DevOps Server, use a personal access token.

1. Click **APIs** in the sidebar and select an API.
2. Under **Connect repository**, click **Connect** and select **Azure DevOps Server**.
3. Enter the **Domain URL** of your repository. You can enter a new domain or select a domain you've used before from the list. Use the name and port of your Git server along with the collection, for example: `https://my-azure-server:8080/my-collection`
4. Enter a **Personal access token** to access the repository. Ensure that the token has the required permissions as specified on the **Connect your repository** page.
5. Click **Next**.

    ![Image 3: Using a personal access token](https://assets.postman.com/postman-docs/v10/api-builder-use-access-token-v10-12.jpg)

6. Enter the **Organization** and the **Repository** where the API will be stored.
7. Select the **Initial branch** for the API. Any changes you make in Postman are stored in the initial active branch. (You can switch to another branch to make it the active branch at any time.)
8. Select an **API schema file** to add to your API. If you're working on a [multi-file API definition](/docs/design-apis/api-builder/develop-apis/defining-an-api/#work-with-multi-file-api-definitions), make sure to select the [root definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#about-root-files) in your repository. The root file is the base file that has references to other files in the API definition. If you leave this field blank, no definition files are added to your API. You can [manually add a definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-an-api-definition-from-a-connected-repository) from your repository later.
9. Select a **Collection directory** where the collections linked to your API will be stored in the repository. If you leave this field blank, a `postman/collections` directory will be created in the root of the repository.
10. Click **Connect Repository**.

    The root definition file you selected is added to your API. For OpenAPI 2.0 and 3.0 APIs, Postman scans for any dependent files referenced in the root definition file and automatically adds them to your API. You can also [manually add more definition files](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-files-from-a-connected-repository) from your repository as needed.

Postman stores your authorized accounts so you can use them to connect to other repositories and services. Learn more about [managing connected accounts for remote repositories](/docs/design-apis/api-builder/versioning-an-api/using-cloud-git-repo/#managing-connected-accounts-for-remote-repositories).

## Disconnecting an on-premises repository

After you disconnect a remote repository, you can no longer sync changes between Postman and the repository.

1. Click **APIs** in the sidebar and select an API.
2. Click \u003cimg alt=\"Branch icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/descriptive-branch-stroke.svg#icon\" width=\"16px\"\u003e **Source Control** in the right sidebar.
3. In the **Source Control** pane, click \u003cimg alt=\"Options icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon\" width=\"16px\" role=\"img\"\u003e and select **Disconnect repository**.
4. Enter the name of the API to confirm, then click **Disconnect**.

## Next steps

After you've connected a remote repository to your API, you can:

* Work with branches, push and pull changes, and resolve conflicts. Learn more about [managing changes using Git](/docs/design-apis/api-builder/versioning-an-api/managing-git-changes/).
* Publish an API version to a workspace or your team's Private API Network. Learn more about [publishing an API version](/docs/design-apis/api-builder/versioning-an-api/api-versions/).

---

**Tip: Plan your Organization setup**

Before you set up your Organization Teams, consider the following:

* How many teams do you need and for which specific step in your API lifecycle?
* How will you name your teams and workspaces?
* Who will be in each group and on which team? Who will manage each team?
* How many workspaces will each team need to begin collaborating?
* If you have Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?

---

**Note:** The component library doesn't support AsyncAPI specifications or [the Postman CLI](/docs/postman-cli/postman-cli-options/#postman-spec-lint).

## Create Organization teams and workspaces

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Teams** in the left sidebar.
2. Click **Create Team**.
    
    ![Image 4: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
3. Name your team. The team will be taggable in the mentions using \`@\`, for example, \`@api-developers\`.
    
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
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click \u003cimg alt=\"Slack icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon\" width=\"16px\"\u003e \u003cimg alt=\"Teams icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon\" width=\"16px\"\u003e **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
    To learn more about:
    
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

---

**Tip: Plan your Organization setup**

Before you set up your Organization Teams, consider the following:

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
    
    ![Image 9: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
3. Name your team. The team will be taggable in the mentions using \`@\`, for example, \`@api-developers\`.
    
    ![Image 10: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:**
    > * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 11: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
    
    ![Image 12: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 13: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
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
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click \u003cimg alt=\"Slack icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon\" width=\"16px\"\u003e \u003cimg alt=\"Teams icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon\" width=\"16px\"\u003e **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
    To learn more about:
    
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

---

**Tip: Plan your Organization setup**

Before you set up your Organization Teams, consider the following:

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
    
    ![Image 14: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
3. Name your team. The team will be taggable in the mentions using \`@\`, for example, \`@api-developers\`.
    
    ![Image 15: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:**
    > * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 16: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
    
    ![Image 17: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 18: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
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
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click \u003cimg alt=\"Slack icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon\" width=\"16px\"\u003e \u003cimg alt=\"Teams icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon\" width=\"16px\"\u003e **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
    To learn more about:
    
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

---

**Tip: Plan your Organization setup**

Before you set up your Organization Teams, consider the following:

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
    
    ![Image 19: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
3. Name your team. The team will be taggable in the mentions using \`@\`, for example, \`@api-developers\`.
    
    ![Image 20: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:**
    > * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 21: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
2. Click **Create Workspace**.
    
    ![Image 22: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
3. Select a blank workspace or a workspace template. Click **Next**.
4. Name the workspace.
    
    ![Image 23: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
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
6. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click \u003cimg alt=\"Slack icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon\" width=\"16px\"\u003e \u003cimg alt=\"Teams icon\" src=\"https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon\" width=\"16px\"\u003e **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
    To learn more about:
    
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

---

**Tip: Plan your Organization setup**

Before you set up your Organization Teams, consider the following:

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
    
    ![Image 24: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
3. Name your team. The team will be taggable in the mentions using \`@\`, for example, \`@api-developers\`.
    
    ![Image 25: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
4. Click **Add Members**. To be added, members need to be part of the organization.
    
    > **Notes:**
    > * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    > * You can use [Groups](/docs