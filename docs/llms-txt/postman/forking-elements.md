# Fork collections and environments in Postman

A _fork_ is a new instance of an element. When you modify a fork, its parent element remains unchanged. In Postman, you can fork collections and environments. Forking enables you to contribute to an element without having [Editor access](/docs/administration/roles-and-permissions/#element-based-roles) for that element.

## Create a fork

To fork an element within a public workspace, you must make your profile public in Postman [Settings](https://go.postman.co/settings/me/). For more information, see [Making your profile public](/docs/getting-started/installation/postman-profile/#make-your-profile-public).

When you fork a collection or an environment, you create a copy of it in a different workspace. You must sign in to Postman to create a fork.

To fork an element, do the following:

1. Select the element in the sidebar.
2. Select ![Image 1: Fork icon](https://assets.postman.com/postman-docs/aether-icons/action-fork-stroke.svg#icon) **Fork** in the upper right.
3. Enter a label for your fork, and select a workspace to save it to.
4. (Optional) If you are forking a collection, you can select one or more environments to include with the fork.
5. Select **Fork Collection** or **Fork Environment**.

![Image 2: Create fork tab](https://assets.postman.com/postman-docs/v11/fork-collection-v11.png)

Postman creates your fork in the selected workspace.

If there are any [mocks](/docs/design-apis/mock-apis/set-up-mock-servers/) or [monitors](/docs/monitoring-your-api/intro-monitors/) associated with the parent element, they aren't linked to the forked element. You must create mocks and monitors specifically for the fork if you need them.

If a collection is in a public workspace that you haven't been added to, you won't be able to send a request within that workspace. To send requests or make changes to a collection, you must fork the collection into an internal workspace that belongs to you.

## Edit a fork's name or label

To change a forked element's name or label, do the following:

1. Select the fork in the sidebar.
2. In the tab labeled with the names of the parent element and the fork, select the fork's name.
3. Edit the fork's name.
4. Select anywhere outside the name or label to save your changes.

## View fork information

Fork information shows details about forks and the users who have created them. You will be able to identify the users who are actively consuming and contributing to your APIs.

To view a list of users who have forked a collection or environment, select the number next to ![Image 3: Fork icon](https://assets.postman.com/postman-docs/aether-icons/action-fork-stroke.svg#icon) **Fork**.

![Image 4: View the fork information count](https://assets.postman.com/postman-docs/v11/fork-information-count-v11.jpg)

To access the list of forks for a collection or environment, do the following:

1. Select ![Image 5: Fork icon](https://assets.postman.com/postman-docs/aether-icons/action-fork-stroke.svg#icon) **Forks** in the right sidebar.
2. Select the fork name.

![Image 6: View the list of forks](https://assets.postman.com/postman-docs/v10/fork-information-list-v10.jpg)

You can also select the user's avatar under **Forks** to view the user's public profile.

![Image 7: View the list of forks](https://assets.postman.com/postman-docs/v10/fork-information-list-v10.jpg)

## Pull updates from a parent element

Forked multi-protocol collections don't support pulling updates, merging changes, or resolving conflicts.

You can pull updates from a parent element into a fork without going through the [pull request process](/docs/collaborating-in-postman/using-version-control/creating-pull-requests/).

1. Hover over the fork in the sidebar.
2. Select ![Image 8: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to its name.
3. Select **Pull changes**.
4. Review the diff and select **Pull changes**.

![Image 9: Pull changes into fork](https://assets.postman.com/postman-docs/v10/pull-changes-v10.jpg)

To pull updates from a parent element during the pull request process, see [Pulling updates during a pull request](/docs/collaborating-in-postman/using-version-control/reviewing-pull-requests/#pull-updates-during-a-pull-request).

## Merge changes from a fork

If you have Editor access on the element, you can _merge_ a fork into the parent element without going through the [pull request process](/docs/collaborating-in-postman/using-version-control/creating-pull-requests/). For example, if you're using forks to organize the work in your workspace, you can merge changes in a fork directly back into the parent element. If you're collaborating with others, merging directly lacks the safeguards built into the pull request process. Many teams require pull requests as part of their [version control workflow](/docs/collaborating-in-postman/using-version-control/creating-pull-requests/).

To merge changes from a fork without opening a pull request, do the following:

1. Hover over the fork in the sidebar.
2. Select ![Image 10: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) **View more actions** next to its name.
3. Select **Merge changes**.
4. Review the diff and select **Merge All Changes**.

![Image 11: Merge Fork](https://assets.postman.com/postman-docs/v10/merge-fork-collection-change-v10.jpg)

1. Select one of the following merge options:
    * **Merge changes** - Merge the changes into the parent element. This doesn't make any changes to the fork. You must have Editor access to the parent element.
    * **Merge changes and update source** - Merge the changes into the parent element. Any differences in the parent element are also made to the fork. You must have Editor access to both the parent and forked elements.
    * **Merge changes and delete source** - Merge the changes into the parent element. After the merge process is complete, Postman deletes the fork. You must have Editor access to both the parent and forked elements.
    
    ![Image 12: Merge Fork Options](https://assets.postman.com/postman-docs/merge-fork-options-v9.12.jpg)
    
2. Select **Merge**.

To merge changes during the pull request process, see [Merge changes from a pull request](/docs/collaborating-in-postman/using-version-control/reviewing-pull-requests/#merge-changes-from-a-pull-request).

## Resolve conflicts from a fork

A merge conflict happens when you try to merge changes into an updated parent element and Postman isn't able to automatically resolve the differences between the two. If there's a conflict when you try to merge a fork, you'll need to decide how you want to resolve it before continuing.

Merge conflicts can involve changes in more than one workspace.

To resolve a merge conflict from a fork, do the following:

1. Begin the merge process described in [Merge changes from a fork](#merge-changes-from-a-fork).
2. Select **Pull the changes** for any conflict.

![Image 13: Pull Changes](https://assets.postman.com/postman-docs/v10/conflicts-pull-changes-v10-2.jpg)

For each conflict, choose the version you want to include when you merge. Select **Keep Source** to keep the change on the parent element. Select **Keep Destination** to keep the change on your fork. You can also select the version you want to keep for each conflict.

![Image 14: Pull Changes](https://assets.postman.com/postman-docs/v10/conflicts-keep-source-or-destination-v10-2.jpg)

To keep all changes on your fork, select **Keep all changes to source**. To keep all changes on the parent element, select **Keep all changes to destination**.

After you resolve the conflicts, select **Pull changes** to [pull the updates](#pull-updates-from-a-parent-element).

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

1. Access ![Image 15: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then open a specification.
2. Click ![Image 16: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.

![Image 17: Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)

1. Click ![Image 18: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
4. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
5. Click **Create collection**.

![Image 19: Create Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 20: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then open a specification.
2. Click ![Image 21: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component file in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 22: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Image 23: Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your component file, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 24: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then open a specification.
2. Click ![Image 25: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component in the left sidebar that you'd like to version and publish.
5. Click **Version & Publish** in the upper right corner.

![Image 26: Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

1. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
2. Click **Create Version & Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Image 27: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the Postman header, then open a specification.
2. Click ![Image 28: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of a specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 29: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Image 30: Reference a component in a specification](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

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

## Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 31: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Team** in the Postman header, then select **Team Settings**.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the team's membership. Environments open to collaboration don’t necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the team’s contents.
7. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
8. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
9. Click **Create collection**.

![Image 32: Create Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

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

![Image 33: Create Organization Workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)

1. Determine the Admins for each workspace from the list of workspace users.
2. Review the roles on the workspaces you moved, and align them with these best practices:
    * If the workspaces were previously shared with the Organization, ensure they remain shared with the Organization.
        * If the APIs are intended to be consumed by others, ensure those people still have access to view them.
        * If you require limited sharing, consider sharing APIs with specific Teams that are interested in them, leveraging the Team memberships, rather than inviting individuals.
    * Ensure that workspaces are viewable by the Team it was moved into, unless there is a specific reason it shouldn’t be shared with other Team members.
    * Make the workspace editable by the Team.
        * Because Teams can have both Members and Guests, set up a pattern where Team Members are the primary contributors to the work, and Guests, having only view access, are the consumers.
        * The team membership can continue to grow and change, and the users with edit access to the Team’s workspaces will adapt accordingly.
    * Analyze the remaining, unassigned workspaces. You can define your own process for handling unassigned workspaces, but Postman recommends using the upcoming archival process or creating an archive Team to hold such workspaces if they are no longer needed or active.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

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
6. If you've integrated Postman with Slack or Teams workspaces, which channels do you need to connect each workspace to post workspace updates?
7. If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 34: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 35: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original team’s shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

To migrate your teams to Organizations, contact your Customer Success Manager. Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)