# Capture HTTP traffic and sync cookies in Postman

Capturing HTTP traffic is an important tool for API development and testing. Postman enables you to inspect the requests passing between client applications and your API and save them to a collection. You can use the saved requests to understand how your API is behaving and to assist with debugging.

Postman's built-in proxy and Postman Interceptor provide two ways to capture HTTP and HTTPS traffic in Postman. You can also use the proxy or Interceptor to capture and sync cookies to the Postman cookie jar.

To capture traffic, begin a proxy or Interceptor session. A session represents a specific time frame during which you want to capture traffic. For example, you can capture traffic while a client application is sending a series of requests that you want to observe or debug.

After you stop the session, you can view the captured requests in Postman. You can also use Postman's search and filtering capabilities to narrow down the requests based on the criteria you choose.

## The Postman proxy

A proxy is an intermediary server that sits between a client application (like a mobile app) and the destination server the client is communicating with (like an API). When the Postman proxy is enabled and a client has been configured to use the proxy, a request from the client goes to Postman first. Postman then forwards the request on to the destination server.

If you start a proxy session while the proxy is enabled, Postman can capture any HTTP or HTTPS traffic passing through the proxy. You can then search or filter the requests, or save them to a collection.

To capture requests using the Postman proxy, view the instructions for your operating system and Postman version:

* If you're on macOS (Postman v10.17 or later) or Windows (Postman v10.18 or later), go to [Capture traffic using the Postman built-in proxy](/docs/sending-requests/capturing-request-data/capture-with-proxy/).
* If you're on Linux (all Postman versions), macOS (Postman v10.16 or earlier), or Windows (v10.17 or earlier), go to [Capture HTTP requests in Postman](/docs/sending-requests/capturing-request-data/capturing-http-requests/).
* To capture secure HTTPS traffic from a client device like a phone, you need to install the Postman security certificate on the device. To learn more, go to [Capture HTTPS traffic using the Postman built-in proxy](/docs/sending-requests/capturing-request-data/capturing-https-traffic/).

To check which version of Postman you're using, click ![Image 1: Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings** in the header, click **Settings**, then click **About**.

## Postman Interceptor

Postman Interceptor provides another way to capture requests sent between a client and a server. Interceptor uses a browser extension rather than Postman's built-in proxy. With Postman Interceptor, you can capture HTTP and HTTPS requests sent from a web browser.

Learn more about [using Postman Interceptor](/docs/sending-requests/capturing-request-data/interceptor/).

## Capture and sync cookies

Along with capturing requests, Postman can capture cookies during a proxy or Interceptor session. You can manually add any captured cookies to the [Postman cookie jar](/docs/sending-requests/response-data/cookies/) and use them when sending requests from Postman.

Postman's built-in proxy and Interceptor also support continuous cookie syncing. Once enabled, all captured cookies for the domains you specify are automatically synced to the Postman cookie jar.

Learn more about [syncing cookies](/docs/sending-requests/capturing-request-data/syncing-cookies/).

## Postman Power Pass FAQ

### General Information

* **What is the Postman Power Pass?**
  Your teamâs activity unlocked the best Postman experience. For free, you can explore premium access to unlimited invites, most Enterprise features, and add-on products. Designed to empower seamless collaboration across the entire API development lifecycle, the Postman Power Pass lets you explore our platformâs full potential.
  
* **How long does the Postman Power Pass last?**
  The Postman Power Pass provides you with premium access for an extended period, but we recommend taking full advantage of this opportunity as soon as possible. While thereâs no fixed access period, we encourage you to explore all the premium features and maximize your experience while the Postman Power Pass is active. Weâll keep you informed of any changes or updates regarding your access.
  
* **What features are included in the Postman Power Pass?**
  You have access to almost all of the features with the Enterprise plan, enabling you to unlock seamless collaboration across the API development lifecycle.
  
* **What add-on products are included in the Postman Power Pass?**
  You have complimentary access to the following add-on products:
  * **Unlimited tests with [Collection Runner](/docs/collections/running-collections/intro-to-collection-runs/):** Collection Runner is designed for QA/QE Engineers who want to simplify the complexity of API testing across the entire development lifecycle. With just one click, you can set up regression, end-to-end, and scenario testing, ensuring your APIs are functional and stable within any application.
  * **Unlimited AI support with [Postbot](/docs/getting-started/basics/about-postbot/):** Postbot is an AI assistant within Postman designed to make API development more efficient. It helps you instantly test and document APIs, visualize API responses, and troubleshoot workflows. Postbot also provides expert support for tasks like building and debugging flows, making it a versatile assistant for every stage of your API lifecycle.
  * **Unlimited [Partner Editors](/docs/collaborating-in-postman/using-workspaces/partner-workspaces/overview/):** Accelerate partner onboarding, improve API adoption, and take collaboration with external partners to the next level. Partner Workspaces are secure, access-controlled spaces for you to invite one or multiple external partners to build and collaborate on APIs. With Postman Power Pass, you can invite as many Partner Viewers and Partner Editors as youâd like.
  * **Unlimited [runs on Flows](/docs/postman-flows/overview/):** Postman Flows is a powerful visual tool that simplifies the development and sharing of API-powered applications. An intuitive drag-and-drop interface it helps developers build API workflows from the ground up allowing them to understand how APIs and their components interact, much like an x-ray or blueprint.

### Organization Settings

To configure your Organization Settings, click **Organization** in the Postman header, then select **Organization Settings**.

![Image 2: Organization settings](https://assets.postman.com/postman-docs/v11/organization-settings-v11.67.png)

The settings enable you to do the following:

* Create [Organization Teams](/docs/administration/organization/create/).
* Configure your [team settings](/docs/administration/managing-your-team/team-settings/).
* Manage [team members](/docs/administration/managing-your-team/team-members/overview/).
* Manage [team resources](/docs/administration/managing-your-team/manage-team-workspaces/).
* Manage [product access](/docs/administration/managing-your-team/manage-team-product-access/).
* Manage [security](/docs/administration/managing-your-team/overview/#secure-your-postman-team).

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Organization roles

* **Organization Managers** are responsible for creating Teams in the Organization and can manage any Team. They're also responsible for assigning individual Team Managers to the teams they create.
* **Team Managers** can approve the adding of Members and the sharing of content from the Teams they manage.
* **Collaborators** can be brought into the team as secondary contributors or consumers. For example, collaborators can be QA teams supporting the team's activities, consumers of the team's APIs, or an entire Organization. On teams that don't require approval, Collaborators can be added automatically. On teams that require approval, an Admin must approve the addition of Collaborators to keep parts of the team private while others are shared.

### Team roles

Each team within an Organization has its own set of independent roles:

| Team role    | Capabilities |
| ------------ | ----------- |
| Team Manager (Team Super Admin) | 
* Has edit access to all elements within the Team and the capability to edit the Team's Settings.
* Manages the entire Team, including the users (add/remove/invite/assign) and the resources (view/edit/manage).
|
| Team Member | 

* Can have edit access to all elements on the Team, but doesn't automatically have access to workspaces, collections, and other elements within the Team unless given a role on that element.
* Can view all resources shared throughout the Team and can have Editor or Viewer access to any workspace or resource within the Team.
* Automatically gets access to all workspaces that are shared to the team when the workspace is set to **Everyone in [TeamName]**.
|
| Collaborator | 

* Can have a Developer or Viewer role. Developers can directly edit the element they're assigned, while Viewers can only view or fork the element they're assigned. Additionally, workspaces that are shared with the Team in the **Workspace Access** settings aren't automatically shared with Collaborators.
* Has to be granted access to workspaces either by setting the workspace to **Everyone in [OrgName]** or by being invited directly through a user or a Team or Group they belong to.
|

### Notes

* Only a Team Member can create workspaces in the team.
* Sharing an element with a new user triggers the process of adding that user to the Team's user list.
* Any time a Team Member or Collaborator is removed from the Team's user list, they lose access to everything in the Team (until they're added back).

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Connect Zoom to your Flows action

You can connect [Zoom](https://www.zoom.com/) to a flow with the Zoom **Connector** block. Use this block to perform the following operations:

* Create Meeting
* Update Meeting
* Get Meeting
* Get Meeting By ID
* Delete Meeting
* Add Meeting Registrant
* Get Meeting Registrant
* Delete Meeting Registrant
* Get Recording By Meeting ID
* Search Recording

To connect Zoom to a Flows action, do the following:

1. In [Postman Flows](/docs/postman-flows/overview/), [create an action](/docs/postman-flows/build-flows/structure/actions/).
1. Click ![Image 3: Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon) **Delete**.
1. Right-click the canvas and select **Zoom** from the list of blocks.
1. Click **Select an operation...** and select the operation you want the action to perform.
1. Click **Select an account...** and follow the prompts to connect your Zoom account.
1. Connect the **Request** block's output ports to the Zoom **Connector** block's input ports, based on the selected operation.
1. Connect the Zoom **Connector** block's **Result** port to the **Response** block's input ports, based on the selected operation.

![Image 4: Connect Zoom to your Flows action](https://assets.postman.com/postman-docs/v11/zoom-connector-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 5: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
1. Click ![Image 6: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
1. Click **Open Component Library**.

![Image 7: Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)

1. Click ![Image 8: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
1. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
1. Click **Create**.

![Image 9: Create a component file](https://assets.postman.com/postman-docs/v11/component-library-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 10: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
1. Click ![Image 11: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
1. Click **Open Component Library**.
1. Click a component file in the left sidebar.
1. Choose a published version of the component file using the version dropdown list.
1. In the left sidebar, click ![Image 12: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
1. Add the URL to a reference (`$ref`) in your specification.

![Image 13: Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your component file, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 14: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
1. Click ![Image 15: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
1. Click **Open Component Library**.
1. Click a component in the left sidebar that you'd like to version and publish.
1. Click **Version &amp; Publish** in the upper right corner.

![Image 16: Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

1. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
1. Click **Create Version &amp; Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

### Notes

You can't delete published versions of component files.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Image 17: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
1. Click ![Image 18: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of a specification.
1. Click **Open Component Library**.
1. Search for a component file and select it in the left sidebar.
1. Choose a published version of the component file using the version dropdown list.
1. In the left sidebar, click ![Image 19: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
1. Add the URL to a reference (`$ref`) in your specification.

![Image 20: Reference a component in a specification](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

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

## Create Organization teams and workspaces

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
1. Click **Create Team**.
    
    ![Image 21: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
1. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 22: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
1. Click **Add Members**. To be added, members need to be part of the organization.
    
    ### Notes
    
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 23: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
1. Click **Create Workspace**.
    
    ![Image 24: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
1. Select a blank workspace or a workspace template. Click **Next**.
1. Name the workspace.
    
    ![Image 25: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
1. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
1. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
1. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
1. Click **Create**.
    
After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
1. Under **About**, add a summary.
1. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
1. Click **Post an Update**.
1. Enter a title and a description of your update.
1. Select **Announcement** from the dropdown list.
1. (Optional) Add a summary describing the change.
1. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
    
    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 26: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 27: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
1. Click **Create Team**.
    
    ![Image 28: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
1. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 29: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
1. Click **Add Members**. To be added, members need to be part of the organization.
    
    ### Notes
    
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 30: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
1. Click **Create Workspace**.
    
    ![Image 31: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
1. Select a blank workspace or a workspace template. Click **Next**.
1. Name the workspace.
    
    ![Image 32: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
1. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
1. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
1. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
1. Click **Create**.
    
After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
1. Under **About**, add a summary.
1. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
1. Click **Post an Update**.
1. Enter a title and a description of your update.
1. Select **Announcement** from the dropdown list.
1. (Optional) Add a summary describing the change.
1. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
    
    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 33: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 34: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
1. Click **Create Team**.
    
    ![Image 35: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
1. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 36: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
1. Click **Add Members**. To be added, members need to be part of the organization.
    
    ### Notes
    
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 37: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
1. Click **Create Workspace**.
    
    ![Image 38: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
1. Select a blank workspace or a workspace template. Click **Next**.
1. Name the workspace.
    
    ![Image 39: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
1. Select the team for which to create a workspace. Otherwise, your team will be prepopulated.
1. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
1. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
1. Click **Create**.
    
After you create one or more workspaces, you can add workspace details, connect the workspace to a Slack or Teams channel, and post a workspace update announcing the workspace is ready for collaboration.

## Edit workspace details

Postman recommends adding a useful workspace description and other details to help Organization Teams start collaborating.

To identify workspaces further, do the following:

1. Under **Workspace description**, add a description.
1. Under **About**, add a summary.
1. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/collaborating-in-postman/using-workspaces/internal-workspaces/manage-workspaces/#edit-workspace-details).

## Announce your team and workspace setup

To post a workspace update, do the following:

1. From the workspace, select **Updates**.
1. Click **Post an Update**.
1. Enter a title and a description of your update.
1. Select **Announcement** from the dropdown list.
1. (Optional) Add a summary describing the change.
1. If you've integrated Postman with Slack or Teams, you can post a team workspace update to a channel on one or both of those apps. Click **Post Update**.
    
    > If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 40: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 41: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
    
Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Create Organization teams

To create an Organization Team, do the following:

1. Access [**Organization Settings**](/docs/administration/organization/settings/), then select [Teams](https://go.postman.co/settings/team/teams).
1. Click **Create Team**.
    
    ![Image 42: Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)
    
1. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
    
    ![Image 43: Name an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-name-v11.jpg)
    
1. Click **Add Members**. To be added, members need to be part of the organization.
    
    ### Notes
    
    * If no Team Manager is assigned, the Organization Manager can continue to manage the Team membership.
    * You can use [Groups](/docs/administration/managing-your-team/user-groups/) to assign Team membership, enabling control through an [Identity Provider (IdP) and SCIM](/docs/administration/scim-provisioning/scim-provisioning-overview/).
    
    ![Image 44: Add Organization Team members](https://assets.postman.com/postman-docs/v11/org-team-member-add.jpg)
    
## Create Organization workspaces

To create workspaces for an Organization Team, do the following:

1. If you're not continuing from the previous step, from the [Home](https://go.postman.co/home) page, click [Teams](https://go.postman.co/teams) and locate the team you for which you want to create workspaces.
1. Click **Create Workspace**.
    
    ![Image 45: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-create-v11.jpg)
    
1. Select a blank workspace or a workspace template. Click **Next**.
1. Name the workspace.
    
    ![Image 46: Create Organization workspaces](https://assets.postman.com/postman-docs/v11/org-workspace-detail-v11.jpg)
    
1. Select the team for