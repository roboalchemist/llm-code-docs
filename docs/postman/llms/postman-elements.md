# About Postman elements

As a comprehensive API development platform, Postman helps you organize and document your work and complete different phases of the [API development lifecycle](https://www.postman.com/api-platform/api-lifecycle/). Learn more about integral parts of Postman like collections and environments.

## Collections

A [_collection_](/docs/collections/collections-overview/) is a set of requests sent to API endpoints. A collection can also include saved responses from those requests, along with each endpoint's authorization type, parameters, headers, request bodies, tests, and settings.

Collections enable you to organize your requests using folders and subfolders according to the requirements of your API project. For example, you can group your API actions into tasks.

You can design your APIs using an HTTP collection with types. Define types, such as data type and possible values, that describe your API's request parameters, headers, and body data. Adding details to your collection can help others better understand your API and send valid API requests. You can also generate an OpenAPI 3.0 specification in Spec Hub from a collection and keep them in sync. To learn more, see [Design your APIs with Postman Collections](/docs/design-apis/collections/overview/).

To try a quick example, see [Create your first collection](/docs/getting-started/first-steps/creating-the-first-collection/).

## Requests

A _request_ is a way for one application to access the capabilities of another application over the internet by way of an API server. A client application (like a mobile app) sends a request to the server, and after the request is processed the server returns a response to the client.

In Postman, you can make [requests](/docs/sending-requests/requests/) using HTTP protocol, MQTT protocol, GraphQL, gRPC, WebSocket, and Socket.IO. An _API endpoint_ is a URL that acts as the point of contact between an API client and an API server. API clients send requests to API endpoints to access the API's functionality and data.

The request _method_ indicates the action you want the API to perform. The most common methods include:

* GET retrieves data from an API.
* POST sends new data to an API.
* PATCH and PUT update existing data.
* DELETE removes existing data.

To try a quick example, see [Send your first API request](/docs/getting-started/first-steps/sending-the-first-request/).

To learn more about requests, see [Send a request with the Postman API client](/docs/sending-requests/create-requests/request-basics/).

## Documentation

_API documentation_ is a set of human-readable instructions for using and integrating with an API. Documentation includes information about an API's endpoints, methods, resources, authentication protocols, parameters, and headers. It also includes examples of common requests and responses.

Postman automatically generates [documentation](/docs/publishing-your-api/api-documentation-overview/) for your collection. To access it, click the collection's **Overview** tab and click **View complete documentation**. You can improve your documentation by adding descriptions for your collection, folders, and requests.

## Environments

An _environment_ is a set of [variables](/docs/sending-requests/variables/environment-variables/) that you can reuse in your requests and share with your team. You can reference them in request authentication, query and path parameters, request bodies, and scripts. Variables help you work efficiently, collaborate with teammates, and set up dynamic workflows.

You can [use environment variables](/docs/sending-requests/variables/environment-variables/) to call the same request against different servers, such as local, stage, or production. Each environment has its own set of variable values. When you change environments, selecting the correct environment points your request at the correct host (server) with the proper authentication and its defined variables. Global variables are useful in cases where you need to use the same variable across several collections.

Environments can also help you to collaborate on Postman data if you're working as part of a team. You can use environments to share variables and manage the visibility of sensitive data such as API keys, passwords, or tokens. Learn more about [working with environments as a team in Postman](/docs/sending-requests/variables/team-environments/).

To learn more about how variables are used in Postman in general, see [Reuse data with variables and environments in Postman](/docs/sending-requests/variables/variables-intro/).

## Flows

_Postman Flows_ is a visual, low-code tool designed to streamline API workflows, making it easier for you to create, manage, and collaborate on API projects. Postman Flows provides an infinite canvas where you can functionally represent your APIs as blocks that can be connected to simulate data flow. The blocks are a set of visual abstractions. To form and visualize an application, you drag blocks, build an application, and run your workflow.

To learn more, see [Build API applications visually using Postman Flows](/docs/postman-flows/overview/).

## Spec Hub

[Spec Hub](/docs/design-apis/specifications/overview/) enables you to [design your API](https://www.postman.com/api-first/) in an OpenAPI 3.0 or AsyncAPI 2.0 specification. You can generate a collection from your API specification. If the collection was generated from an OpenAPI 3.0 specification, you can keep the collection and specification in sync with your latest changes.

## API Builder

Postman supports [API-first development](https://www.postman.com/api-first/) with the API Builder. You can use the [API Builder](/docs/design-apis/api-builder/overview/) to design your API in Postman and then take your API through the complete development lifecycle by developing, testing, deploying, and observing it. Your [API definition](/docs/design-apis/api-builder/develop-apis/defining-an-api/) can then act as the single source of truth for your API project.

When you create a new API in the Postman API Builder, you can start your API development by [connecting to a repository](/docs/design-apis/api-builder/versioning-an-api/overview/) or clicking **continue without a repository**.

## Mock servers

A _mock server_ enables you to simulate your API without having to configure a real API server. You can use any HTTP collection to set up a mock server. When you send a request to the mock server, Postman returns a real-world response using data from your collection.

To learn more about how to get started with mock servers in Postman, see [Simulate your API in Postman with a mock server](/docs/design-apis/mock-apis/overview/).

## Monitors

_Postman Monitors_ enable you to [continuously check the health and performance of your APIs](https://www.postman.com/api-platform/api-observability/). You can create monitors that run requests in selected collections. Requests can run API test scripts, chain together multiple requests, and more. You can also schedule how often Postman runs monitored collections.

You'll be alerted to any test failures once the monitor is running, so you can identify and address issues before your API's consumers are affected.

To learn more about monitors, see [Monitor health and performance of your APIs in Postman](/docs/monitoring-your-api/intro-monitors/).

## Troubleshoot vault secrets

Vault secrets can be empty or unresolved in your HTTP requests. An *empty vault* secret is a vault secret that doesn't have a value but is referenced in your request. An empty vault secret may or may not exist in your Postman Vault. An *unresolved vault secret* is a vault secret that exists in your Postman Vault but the value can't be accessed from your request.

A vault secret in a cloud vault may be empty if the cloud vault's name was updated, but references to the vault secret use the previous cloud vault name. To fix this, update references to the vault secret with the correct cloud vault name.

To learn more about troubleshooting empty and unresolved vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

To reference a component in a specification, do the following:

1. Click **Docs** in the Postman header, then select **Specs** in the left sidebar.
2. Click **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

To learn more, see [Edit component file](#edit-a-component-file).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Organization settings

_Postman Organizations_ streamline API collaboration, reduce clutter in teams, maintain tighter access controls, and prevent the unwanted exposure of work and secrets. Organizations enable you to replicate your internal structure by creating independent teams, each with its own set of managers and members. This setup prevents sharing sensitive information and gives each team better control over its membership.

Organization Teams can directly invite other Teams to collaborate or consume the Teams' content, improving collaboration scaling. By default, a given Organization Team's content is shared with the entire Organization. However, content sharing can be limited to just the team or specific team members, helping to reduce clutter and oversharing in your Organization.

To migrate your teams to Organizations, contact your Customer Success Manager. Your teams will be migrated to a single team that you can then reorganize and redistribute. Also see [Migrate your Enterprise team to an Organization](/docs/administration/organization/migrate/) for further steps.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original teamâs shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

To set up a productive Enterprise team in Postman, walk through the following general tasks.

1. Access [**Organization Settings**](/docs/administration/organization/settings/) in the Postman header, then click **Team** in the left sidebar.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):
    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** – Turn on if you want to strictly control access to Teams and tightly control the teamâs membership. Environments open to collaboration donât necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** – Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.
6. Populate the team with the members who are responsible for the teamâs contents.
7. If your team is smaller and doesnât use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
8. If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.
9. Select **Internal** for workspace type. You can update the workspace visibility at any time. As a best practice, workspaces need to remain internal until all the work has been completed and approved.
10. Select **Everyone in [TeamName]** to allow all Team Members with access to the workspace, whether invited or shared, to edit the workspace elements. Collaborators will still have to be added to the workspace roles to enable their access. For stricter access, select **Only you and invited people**. If there's a specific need to open the workspaces to all people in the Organization, select **Everyone in [OrgName]**.
11. Click **Create**.

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
* If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click **![Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon)** **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.
* Learn more about:
    * [Organization roles](/docs/administration/organization/roles/)
    * [Organization settings](/docs/administration/organization/settings/)

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

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

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

To reference a component in a specification, do the following:

1. Click **Docs** in the Postman header, then select **Specs** in the left sidebar.
2. Click **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

To learn more, see [Edit component file](#edit-a-component-file).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

* [Creating organization teams and workspaces](/docs/administration/organization/create/)
* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

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