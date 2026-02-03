# Collaborate with the Postman community using public workspaces

Anyone in the Postman community can access a _public workspace_. A public workspace can enhance a new user's onboarding experience with your API, inspire your existing users with new use cases and resources, increase your API's discovery in Postman search results, and enable you to work publicly with partners.

## Make your team profile public

Before other Postman users can work with your team in a public workspace, your team needs to have a public team profile. A public team profile encourages other users to collaborate with you in a public workspace, enables you to ask for contributions and gather feedback, and increases your API's discovery in search results. A public team profile also shows up on the [Postman API Network](https://www.postman.com/explore).

[Team Admins](/docs/administration/roles-and-permissions/#team-roles) manage the team profile and other team settings.

To make your [team profile](https://go.postman.co/settings/team/general) public, do the following:

1. In the upper-right corner of Postman next to your avatar, select **Team > Team settings**.
2. Select **Team profile**.
3. Select **Make team profile public** to set the profile to public.

For information on how to create a public profile, see [Edit your publisher team](/docs/administration/managing-your-team/team-settings/#edit-your-publisher-team).

## Create a public workspace

You can create a public workspace to share your workspace and its elements with the Postman community on the Postman API Network.

Make sure to never expose secrets, such as API keys, in your public workspaces. The [Postman Secret Scanner](/docs/administration/managing-your-team/secret-scanner/overview/) scans your public workspaces to detect any exposed secrets.

To create a public workspace, do the following:

1. Select **Workspaces** from the header, then select **Create Workspace**.

    ![Create new workspace](https://assets.postman.com/postman-docs/v10/create-workspace-from-dropdown-v10.23.0.jpg)

1. You can use [workspace templates](/docs/collaborating-in-postman/using-workspaces/create-workspaces/#apply-a-template-to-a-workspace) to help you set up a new workspace. Select a workspace template to populate the workspace with helpful information and sample collections, or select **Blank workspace** to create an empty workspace. Then select **Next**.

    ![Create new workspace](https://assets.postman.com/postman-docs/v10/create-workspace-and-apply-template-full-screen-v10-2.jpg)

1. Select a unique name for your workspace. You can't have two public workspaces with the same name.
1. Select **Public** as your workspace type.
1. If you're not an admin, add a note for the workspace creation approval.
1. Select **Create**.

    ![Create public workspace](https://assets.postman.com/postman-docs/v11/create-public-workspace-v11.33.jpg)

## Convert an existing workspace to a public workspace

As a [Workspace Admin](/docs/administration/roles-and-permissions/#workspace-roles), you can convert an existing workspace to a public workspace. If you're on a [Postman Professional or Enterprise plan](https://www.postman.com/pricing/), making a workspace public requires a [Community Manager's](/docs/administration/roles-and-permissions/#team-roles) approval. Once you make a workspace public, all elements within that workspace become publicly available on the Postman API Network.

Before you convert your workspace to a public workspace, make sure you aren't exposing any secrets. You can give your API consumers a placeholder [variable](/docs/sending-requests/variables/variables/#setting-values-for-variables-without-a-scope) or [vault secret](/docs/sending-requests/postman-vault/manage-vault-secrets/#set-a-value-for-a-vault-secret-that-doesnt-exist) (recommended). Learn how [the Secret Scanner scans your public workspaces](/docs/administration/managing-your-team/secret-scanner/overview/).

Postman sends in-app and email notifications to all workspace members when the workspace is made public. To view your in-app notifications, select the notification icon ![Changelog icon](https://assets.postman.com/postman-docs/icon-notification-bell-v9.jpg#icon) in the Postman header.

To convert an existing workspace to a public workspace with a Postman Free or Basic plan, do the following:

1. Open the workspace. In the **Overview** tab, select **Settings**.
2. Under **Workspace types**, select **Public**.
3. Select **Save Changes**.

To convert an existing workspace to a public workspace in a Postman Professional or Enterprise plan, do the following:

1. Open the workspace. In the **Overview** tab, select **Settings**.
2. Under **Workspace type**, select **Change**.
3. Select **Public**.
4. Enter a note for approval.
5. Select **Submit Request**.

    ![Request visibility change](https://assets.postman.com/postman-docs/v11/public-workspace-request-v11.33.jpg)

   This sends a request to team members with the Community Manager role for their approval, and triggers the [Secret Scanner](/docs/administration/managing-your-team/secret-scanner/overview/). The workspace's visibility will be set to [internal](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#change-workspace-visibility) until it's [approved](/docs/administration/managing-your-team/manage-team-workspaces/#approve-workspace-creation-requests).

   While you're waiting for the request to be reviewed, you can check the status of the secret scan or cancel the request from the workspace settings.

## Feature collections in public workspaces

You can feature collections in a public workspace to give API consumers quick access to specific collections. On a public workspace's **Overview** tab under **Featured collections**, select ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**, then select the collection you'd like to feature.

![Featured collection in public workspace](https://assets.postman.com/postman-docs/v11/featured-collections-v11-12.jpg)

You can choose an environment for each featured collection you'd like to be active when it's opened from the **Overview** tab. The environment will be active in the [environment selector](/docs/sending-requests/variables/managing-environments/#switch-between-environments).

If you don't feature any collections in a public workspace, Postman will automatically feature popular collections in the public workspace.

To remove a featured collection, hover over the collection and select ![Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon), then select **Remove**.

## Invite collaboration on a public workspace

An informative and inviting public workspace can help increase adoption of your APIs. To invite collaboration from other users on your public workspace, you need to have:

* A complete [public team profile](#make-your-team-profile-public).
* A complete [workspace overview](#edit-public-workspace-details), including a name, summary, and description.
* Descriptive [documentation](/docs/publishing-your-api/api-documentation-overview/) for your APIs.

Signs of a public workspace that invites collaboration include:

* **Active forks of your workspace** - The number of people who [fork your workspace](/docs/collaborating-in-postman/using-version-control/forking-elements/) and work on their forks shows strong collaborator engagement.
* **People watching your workspace** - The number of people who [watch your workspace](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/use-workspaces/#watch-a-workspace) for activity can reflect interest from potential collaborators.
* **Recent activity on the workspace** - A [workspace activity feed](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/use-workspaces/#view-workspace-activity) that shows ongoing work reassures potential collaborators that your team updates and maintains the workspace.

For more information on using a public workspace to help increase adoption of your API, see [Increasing adoption of an API with a public workspace](https://blog.postman.com/increasing-adoption-of-an-api-with-a-public-workspace/) on the Postman blog.

### Share a public workspace

You can share a public workspace by giving collaborators its **workspace URL** directly.

To access a workspace's URL, do the following:

1. Go to the workspace **Overview** page.
2. Select ![Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy link to workspace** next to the workspace name to copy the workspace's URL to your clipboard.

    ![Copy link to workspace](https://assets.postman.com/postman-docs/v10/copy-workspace-link-v10.jpg)

3. Share the workspace URL with others.

When you share a workspace with Postman users who aren't team members, its visibility must be public. If the workspace is an internal workspace, users who don't have access won't be able to open it.

## Announce your workspace updates

Keep the watchers of your workspace and collection informed about any changes to your APIs. You can share updates across multiple collections and link to the specific request, collection, or folder that changed. These watchers get notified and can engage with these updates by commenting and reacting.

### Post an update

To post a workspace update, do the following:

1. Open a workspace and select the **Updates** tab. If this is the first update, select **Post an Update**. Otherwise, you'll see a **Post an update** field above other updates.
2. Enter your update's title and description.
3. Select a tag from the dropdown list: **Improvement**, **New Feature**, **Bug Fix**, **Breaking Change**, or **Announcement**.
4. (Optional) Select **Link a Resource** to include links to collections, requests, and saved examples in your update.

    When you add links to collections or requests, the watchers of the collections, who may not be watching the workspace, are notified about the update alongside workspace watchers.

5. If you've integrated Postman with Slack, you can post a workspace update to a channel. Select **Post Update**.

    If a Slack channel is already subscribed to workspace updates, the checkbox next to **Share on Slack** on the bottom right of the post will be checked. If not, select ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) integrations page.

![Posting a public workspace update](https://assets.postman.com/postman-docs/v11/workspace-post-update-v11-38.jpg)

Your API consumers can respond to a workspace update by adding a comment or reacting with an emoji response.

Teams can connect up to 10 Slack channels to a single public workspace.

### Share workspace updates

To share a workspace update select ![Share icon](https://assets.postman.com/postman-docs/aether-icons/action-share-stroke.svg#icon) the share icon. Select **Share via X** or **Share via LinkedIn** to share on social media, or select **Copy Link** to copy a link to the update.

Viewers in a public workspace (including those inside and outside the team that owns the public workspace) can subscribe to public workspace updates.

### Edit or delete a workspace update

To edit or delete an update, do the following:

1. Open a workspace and select **Updates**.
2. Select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions**.
3. Select **Edit** or **Delete**.

## Manage a public workspace

When a user opens a public workspace, Postman shows an overview of its contents, activity, and members in an **Overview** tab. The user interacts with the contents of the public workspace, including the collections, APIs, environments, and other elements. As a team member with an [Admin role](/docs/administration/roles-and-permissions/#workspace-roles) on the workspace, you can manage the overview, the elements in the workspace, and the members of the workspace.

### Edit public workspace details

Users with an [Admin role](/docs/administration/roles-and-permissions/#workspace-roles) for a workspace can edit workspace details, including updating the workspace's name, summary, description, and visibility. For more information, see [Editing workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

The [Postman API Network](/docs/collaborating-in-postman/public-api-network/public-api-network-overview/) displays your workspace's name and summary. Make your workspace name and summary informative to improve its visibility on the Postman API Network.

### Move elements to a public workspace

You can move Postman elements from your internal workspace into a public workspace. You must have an [Admin or Editor role](/docs/administration/roles-and-permissions/#workspace-roles) for the public workspace to move elements to it.

To move an existing element to a public workspace, do the following:

1. Select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to the collection or environment name, then select **Move**.
2. Select the public workspace to which you want to move the collection or environment, then select **Move Collection** or **Move Environment**.

The Postman element that you move to the public workspace will no longer exist in the original workspace.

If there are monitors, mock servers, or integrations associated with the moved element, they remain in the original workspace.

The API's collections will move with the API to the new workspace.

### Delete elements from a public workspace

You can delete Postman elements from a public workspace for which you have an [Admin or Editor role](/docs/administration/roles-and-permissions/#workspace-roles).

1. Select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to the element's name, then select **Delete**.
2. Select **Delete** to confirm your choice.

Learn more about [deleting a collection](/docs/collections/use-collections/manage-collections/#delete-a-collection) and [restoring a deleted collection](/docs/collections/use-collections/manage-collections/#recover-or-permanently-delete-a-collection).

### Delete a public workspace

To delete a public workspace, you must change its visibility first. You must have an [Admin role](/docs/administration/roles-and-permissions/#workspace-roles) for a workspace to be able to delete it.

1. On the workspace overview, select **Settings**.
2. Under **Workspace type**, select **Change**.
3. Select **Internal**.
4. Select **Save Changes**.
5. After you update its visibility, select **Delete Workspace**.
6. Enter the workspace name to confirm that you want to delete it, then select **Delete workspace**.

    ![Unable to delete a public workspace](https://assets.postman.com/postman-docs/public-workspace-cant-delete-v9.jpg)

### Manage public workspace users and roles

If you're a [Team Admin](/docs/administration/roles-and-permissions/#team-roles), you can manage collaborators and user roles in a public workspace:

* **Invite team members, groups, and external users to collaborate in a public workspace.** To learn more about inviting users to work with you in your public workspace, see [Sharing workspaces](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#share-workspaces).
* **Assign access to elements within a workspace.** Workspace roles control access to elements. You can assign workspace roles to an individual user or to a user group. To learn more about assigning workspace roles or removing a user from a workspace, see [Manage workspace roles](/docs/administration/managing-your-team/team-members/manage-roles/#manage-workspace-roles).

Team members will receive an email and in-app notification when they're added to a public workspace.

## Collaborate in another user's public workspace

To collaborate with someone else in their public workspace, select **Workspaces** from the header, and then select the workspace you want to work in.

For **collections** and **environments**, [create a fork](/docs/collaborating-in-postman/using-version-control/forking-elements/#create-a-fork) and request to merge changes using a [pull request](/docs/collaborating-in-postman/using-version-control/creating-pull-requests/).

For **APIs**, select the API and version. Select the **Definition** tab and then select **Request Access** to request an Editor role.

You can access public workspaces using the Postman Explore page's [**Workspaces** category](https://www.postman.com/explore/workspaces). You can also access the public workspaces that you own or are a member of using **Workspaces** in the header.

The list of avatars in the Postman header shows you who's active in your workspace. This list will include all active users with [public profiles](/docs/getting-started/installation/postman-profile/#make-your-profile-public), and users who've chosen to remain anonymous by not enabling their public profile.

![Active users in public workspace](https://assets.postman.com/postman-docs/presence-public-workspace-v9.19.jpg)

Viewers in a public workspace (including those inside and outside the team that owns the public workspace) can subscribe to public workspace updates.

## Next steps

Once you start working collaboratively in a public workspace, users can fork collections and create pull requests.