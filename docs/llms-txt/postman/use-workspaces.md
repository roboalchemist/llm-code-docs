# Use Postman workspaces

When you first open Postman, you'll land in your default internal workspace. You can [create more workspaces](/docs/collaborating-in-postman/using-workspaces/create-workspaces/) for your use and to work with teammates. To create more workspaces, you need to sign in to your [Postman account](/docs/getting-started/account/overview/).

After you access your workspace, you can [tag](#tag-a-workspace), [favorite](#favorite-and-discover-a-workspace), and [connect](#connect-your-workspace-to-internal-team-channels) your workspace to team channels. You can also select to [watch](#watch-a-workspace) a workspace, [pin collections](#pin-collections-to-workspaces), check your [workspace activity](#view-workspace-activity), and more.

## Access a workspace

To open a workspace, select **Workspaces** in the Postman header. Select a workspace to open it, or select **View all workspaces** for a list of all available workspaces. This will only display workspaces that you have access to, based on the [workspace visibility](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#change-workspace-visibility) and your [workspace role](/docs/administration/roles-and-permissions/#workspace-roles).

![New Workspace](https://assets.postman.com/postman-docs/v11/view-workspaces-v11.74.png)

The workspace's **Overview** tab displays a description and summary of the workspace, and any [pinned](#pin-collections-to-workspaces) collections. On the right, you'll find a list of workspace contributors and the option to [view workspace activity](#view-workspace-activity). If you decide to make your workspace public, you can add [featured](/docs/collaborating-in-postman/using-workspaces/public-workspaces/#feature-collections-in-public-workspaces) collections.

![Workspace overview](https://assets.postman.com/postman-docs/v11/workspace-overview-v11-19.jpg)

To learn more about access management, go to [Request and approve access to Postman resources](/docs/collaborating-in-postman/requesting-access-to-elements/).

## Tag a workspace

Tagging workspaces is available with [Postman Enterprise plans](https://www.postman.com/pricing/).

You can apply shared tags to workspaces, collections, and APIs. Tags must be between two and 64 alphanumeric characters, starting with an alphabetical character, and contain only dashes and no spaces. You can add up to five tags. Adding shared tags to workspaces enables you to organize and search for workspaces.

Once you add tags to the workspace, you can select a tag to open search results associated with the tag in a new tab.

To learn more about searching using tag names in Postman, see [Search Postman](/docs/getting-started/basics/navigating-postman/#search-postman). You can use tags when searching [elements in your Private API Network](/docs/collaborating-in-postman/private-api-network/use-private-network/#search-filter-and-sort). You can also use tags to search for [elements to add](/docs/collaborating-in-postman/private-api-network/organizing-private-network/#add-elements-in-your-private-api-network) and [elements to request to add](/docs/collaborating-in-postman/private-api-network/private-network-requests/#request-to-add-elements-in-your-private-api-network) to your Private API Network.

To add tags to a workspace, do the following:

1. Select **Workspaces** in the Postman header, and then select a workspace.
2. On the workspace's **Overview** tab, select the **Tags** field to edit it.

    ![Add tags to a workspace](https://assets.postman.com/postman-docs/v11/add-tags-workspace-v11.19.png)

3. Select an existing tag or enter a new tag. If you're adding a new tag, enter the new tag name and press **Return** or **Enter**.

    ![Add new tags to a workspace](https://assets.postman.com/postman-docs/v11/create-new-tags-workspace-v11.19.png)

Repeat these steps to add more tags.

To remove tags from a collection, do the following:

1. Select **Workspaces** in the Postman header, and then select a workspace.
2. On the workspace's **Overview** tab, select the **Tags** field to edit it.
3. Select ![Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) on the tag.

    ![Remove tags from a workspace](https://assets.postman.com/postman-docs/v11/remove-tags-workspace-v11.19.png)

4. Select the area outside the **Tags** field to save your changes.

## Favorite and discover a workspace

Postman enables you to star and discover workspaces you care about the most. You can preview each workspace from the workspaces dropdown and get the following metadata and options:

* Author name, owner, and elapsed activity time
* Ability to copy workspace ID, get the workspace link, and star the workspace for easier discovery

![Discover a workspace](https://assets.postman.com/postman-docs/v11/workspace-discoverability-v11.74.png)

You can star the workspace from the workspace preview, the top right of the workspace, and the [Workspaces dashboard](https://app.getpostman.com/dashboard).

Starred workspaces appear in the top of the list of workspaces in the sidebar and workspace dropdown.

## Connect your workspace to internal team channels

Postman integrations for [Slack](/docs/integrations/available-integrations/slack/) and [Microsoft Teams](/docs/integrations/available-integrations/microsoft-teams/) enable you to bring your API development workflow into your team channels. Learn how to connect a Postman workspace to [Slack](/docs/integrations/available-integrations/slack/slack-app/#connect-a-postman-workspace-to-slack) or [Teams](/docs/integrations/available-integrations/teams/teams-app/#connect-a-postman-workspace-to-teams).

To subscribe to a channel, click ![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview.

## Watch a workspace

Watch a workspace to receive an email or in-app notification when a team member modifies the workspace. This includes changing the workspace visibility or updating an element in the workspace.

To start watching a workspace, select ![View icon](https://assets.postman.com/postman-docs/aether-icons/action-view-stroke.svg#icon) **Watch** in the workspace's **Overview** tab. Select the count next to **Watch** to access the list of people who are watching the workspace.

To access your notifications, select ![Notification icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-notification-stroke.svg#icon) **Notifications** in the Postman header. The notification list shows details about changes to workspaces you are watching. You will also receive an email with information about the change, who made it, and when.

To stop watching a workspace, select **Unwatch** in the workspace's **Overview** tab.

By default, you are a watcher for any workspace you create. You won't receive notifications for changes you make to a workspace you're watching.

You can also watch a [collection](/docs/collections/use-collections/collaborate-with-collections/#watch-a-collection) and an [API](/docs/design-apis/api-builder/managing-apis/#watching-apis) within a workspace to receive a notification when it's modified.

## Pin collections to workspaces

You can pin collections to an internal or Partner Workspace for quick access on a workspace's **Overview** tab. If you don't have any collections pinned to your workspace, select ![Pin icon](https://assets.postman.com/postman-docs/aether-icons/action-pin-stroke.svg#icon) **Pin Collections**. Otherwise, select ![Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add** under **Pinned collections**. Then select the collection you'd like to pin.

![Pinned collection in a workspace](https://assets.postman.com/postman-docs/v11/pinned-collections-v11-12.jpg)

You can choose an environment for each pinned collection you'd like to be active when it's opened from the **Overview** tab. The environment will be active in the [environment selector](/docs/sending-requests/variables/managing-environments/#switch-between-environments).

If your workspace has pinned collections and you [convert the workspace to a public workspace](/docs/collaborating-in-postman/using-workspaces/public-workspaces/#convert-an-existing-workspace-to-a-public-workspace), the pinned collections will be publicly [featured](/docs/collaborating-in-postman/using-workspaces/public-workspaces/#feature-collections-in-public-workspaces) in the public workspace's **Overview** tab.

To remove a pinned collection, hover over the collection and select ![Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon), then select **Remove**.

## Get the workspace ID

Sometimes you'll need your workspace ID to perform different actions like copying a workspace or setting up an environment.

To copy a workspace ID, do the following:

1. On the workspace's **Overview** tab, select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **Options** and then select **Workspace info**.
2. Select ![Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy workspace ID**. You can also view who created the workspace and when the workspace was last updated.

    ![Workspace ID](https://assets.postman.com/postman-docs/v11/find-workspace-id-v11.jpg)

You can also hover over a workspace in the workspace dropdown and copy the workspace ID from the workspace preview. See [Favorite and discover your workspace](#favorite-and-discover-a-workspace) for more information.

## View workspace activity

Postman maintains activity feeds for workspaces. You can use it to review create, update, transfer, and delete actions made by you and your team on private and shared elements.

You can [access the activity feed in Postman](#access-the-activity-feed-from-postman). The activity feed shows information about who added or removed collections, environments, or elements from the workspace, and users that join or leave the workspace. You can [filter this information](#filter-the-activity-feed) directly within the activity feed. You can also [view who's active in your workspace](#view-who-is-in-your-workspace).

You can programmatically access workspace activity feeds with the [Postman API](https://www.postman.com/postman/postman-public-workspace/request/qq0dqop/get-a-workspace-s-activity-feed).

### Access the activity feed from Postman

To access the activity feed in Postman, select the workspace name in the upper left. On the right, select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** \> **Activity log** to review the events that have occurred in the workspace.

### Filter the activity feed

Filtering the activity feed enables you to display information directly instead of having to scroll through the feed. You can choose to filter by user or by the Postman element. Select **Reset filters** to clear the filters from the activity feed.

* Filtering by a user displays the actions that user carried out. To filter by user, select **People** in the activity feed and select users. You can search for a specific user by entering their name in the search field.

    The user list only shows users that are part of the workspace, not all team members.

* Filtering by element displays the actions carried out on the selected element type. The available elements are **Workspace**, **API**, **Collection**, **Environment**, **Monitor**, **Mock servers**, **Specification**, and **Flows**. To filter by element, select **Elements** at the top of the activity feed and select elements. You can search for an element by entering its name in the search field.

### Export team activity to other platforms

With a Postman Basic, Professional, or Enterprise account, you can send team activity feeds to external communication channels:

* [Slack](/docs/integrations/available-integrations/slack/)
* [Microsoft Teams](/docs/integrations/available-integrations/microsoft-teams/)

## View who is in your workspace

The list of avatars in the Postman header shows you who's active in your workspace. If you're in an internal workspace, this list includes all active team members. The list also includes all team members who are inactive, but have visited the workspace before.

If you're in a public workspace, this list includes all active users with [public profiles](/docs/getting-started/installation/postman-profile/#make-your-profile-public). It also includes users who've chosen to remain anonymous by not enabling their public profile.

![Active users in public workspace](https://assets.postman.com/postman-docs/v11/presence-public-workspace-v11.jpg)