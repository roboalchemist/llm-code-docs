# Capture traffic using the Postman built-in proxy

If you're using APIs to build client-side applications like mobile and desktop apps or websites, you may want to check the HTTP and HTTPS request traffic sent and received in the app. Sometimes you might discover undocumented APIs. You can capture network traffic, including requests, responses, and cookies, using the proxy that's built into Postman.

## How the built-in proxy works

The Postman desktop app has a built-in proxy that can capture HTTP and HTTPS traffic. Here's how it works:

1. The Postman desktop app listens for any calls made by a client app or device using the proxy.
2. The Postman proxy captures the request and forwards it to the server.
3. The server returns a response to the Postman proxy, where it can also be saved.
4. The response is returned back to the client.

![Postman capture proxy](https://assets.postman.com/postman-docs/proxymobile-aa.jpeg)

Similar to the [Interceptor extension](/docs/sending-requests/capturing-request-data/interceptor/), the Postman proxy intercepts and captures your requests. It can also capture responses and cookies.

Starting the Postman proxy begins a _proxy session_, which is a time-bound period of traffic capture. You can pause, restart, and stop a proxy session, then later start another one. Each session is logged in the **History** tab and displays the total session time, a traffic overview, and all traffic captured. You can also send requests and responses to a collection and [save cookies to the Postman cookie jar](/docs/sending-requests/capturing-request-data/syncing-cookies/).

## Using the Postman proxy

In the steps below, you'll use the Postman proxy to inspect HTTP and HTTPS communication going to and from your computer and phone. To get started, make sure your computer and phone are connected to the same local wireless network.

### Step 1: Start a proxy session

You can't use the Postman proxy with the [Postman web app](/docs/getting-started/installation/installation-and-updates/#web-limitations). Make sure you've installed the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/).

1. Click ![Image 2: Capture icon](https://assets.postman.com/postman-docs/aether-icons/action-capture-stroke.svg#icon) **Start Proxy** in the Postman footer.
2. (Optional) Click the port number to change it. By default, the port is set to 5559. Make a note of the port number, as you'll use it later when configuring clients.
3. Click **Start Proxy Session**.

The first time you start a proxy session, Postman installs the **Postman Proxy CA** certificate on your computer. If prompted, enter your computer password to install the certificate. Installing the certificate enables the Postman proxy to capture secure HTTPS traffic sent from browsers and other client apps on your computer.

![Image 3: Start a proxy session](https://assets.postman.com/postman-docs/v10/proxy-start-session-v10-22.jpg)

### Step 2: Control the proxy session

You can't have more than one proxy or Interceptor session running at the same time.

When you start the proxy session, the Postman proxy begins capturing traffic sent from your computer. After you start a proxy session, you can pause, restart, or stop it. You can also select what traffic you want to capture during the session.

To control an active proxy session, click ![Image 4: Capture icon](https://assets.postman.com/postman-docs/aether-icons/action-capture-stroke.svg#icon) **Proxy active** in the footer to display the proxy session tab. (If the proxy session is paused, click ![Image 5: Capture icon](https://assets.postman.com/postman-docs/aether-icons/action-capture-stroke.svg#icon) **Start Proxy** in the footer.) The proxy tab shows the total duration of the session and the size of the data captured.

With the proxy active, open a web browser and navigate to a website, or open an app that communicates with a server. Requests appear in the proxy session tab as they're captured.

From the proxy session tab, you can take the following actions:

* Click **Pause** to temporarily stop capturing traffic, then click **Resume** when you're ready to begin capturing traffic again. When you're finished capturing traffic, click **Stop** to end the proxy session.
* Click **Save responses for requests** to save each request's response along with the captured request.
* Click **Capture cookies** if you want to capture cookies along with requests during the proxy session.

    \u003e You can also capture cookies and sync them to Postman without starting a proxy session. Learn more about [syncing cookies](/docs/sending-requests/capturing-request-data/syncing-cookies/).
* Click ![Image 6: Sort icon](https://assets.postman.com/postman-docs/aether-icons/table-sort-stroke.svg#icon) in the column headers to sort the results in ascending or descending order.
* Click ![Image 7: Filter icon](https://assets.postman.com/postman-docs/aether-icons/action-filter-stroke.svg#icon) in the column headers to limit the requests and responses that are captured while the session is active. Postman captures requests that match the selected criteria and ignores requests that don't match. You can change the filters at any time during the session:
    
    * **Status** - Limit captured requests to the selected status codes.
    * **Method** - Limit captured requests to the selected methods.
    * **URL** - Limit captured requests to URLs that match the specified criteria. You can specify text that URLs must contain and can't contain, and you can use regular expressions. Click **Enter** to apply the specified filters. To remove a filter, click ![Image 8: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) next to the filter.
    * **Type** - Limit captured requests to the selected content types.
    
    \u003e In responses with a `content-type` that has images, audio, or video, the content is intercepted but not captured. The information captured is response headers, time taken, and the status code.

![Image 9: Control a proxy session](https://assets.postman.com/postman-docs/v10/proxy-control-session-v10-22.jpg)

### Step 3: View the proxy session results

While your proxy session is running, the proxy session tab shows captured traffic as you use a browser or apps on a client device. You can view the status, method, URL, type, response size, response time, and timestamp for each captured request including.

You can view and work with the proxy session results while the session is active or paused, or after you stop the session.

* To rename the proxy session, click **Proxy debug session** and enter a new name.
* Select the **Requests** tab to view information about incoming requests and responses, or select the **Cookies** tab to view information about captured cookies.
* Use the search box to find specific requests or cookies.
* Click a request to view more details.
* Click a request URL to open it as a new API request in Postman.
* To delete a request or cookie, select it and click ![Image 10: Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon) **Delete**.
* To add a cookie to the [Postman cookie jar](/docs/sending-requests/response-data/cookies/), select it and click **+ Add to Cookie Jar**.

![Image 11: View proxy session results](https://assets.postman.com/postman-docs/v10/proxy-view-results-v10-22.jpg)

### Step 4: Stop the proxy session

When you're finished capturing traffic, click **Stop** to end the proxy session. To view the proxy session again later, click **History** in the sidebar, then select the proxy session. You can also click ![Image 12: History icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-history-stroke.svg#icon) **View Past Sessions** on the proxy session tab.

The **Overview** tab shows summary graphs of traffic captured in the proxy session. Use the dropdown menu to group requests by method, domain, content type, or status code. The header also displays the session start time, session size, duration, and source.

To filter the list of requests, click ![Image 13: Filter icon](https://assets.postman.com/postman-docs/aether-icons/action-filter-stroke.svg#icon) in the column headers. Postman displays requests that match the selected filters and hides requests that don't match.

To save captured requests to a collection, do the following:

1. Stop the proxy session if it's still active.
1. Select the checkbox next to the requests you want to save, or select the checkbox in the column header to select all requests.
1. Click **Save Requests**.
1. Select the collection where you want to save the requests, or click **New collection** to create a new collection.
1. Choose how to organize the requests in the collection. You can select the checkboxes to group the requests in folders organized by **Domain name**, **Endpoints**, or both.
1. Click **Save**.

![Image 14: Save captured requests to a collection](https://assets.postman.com/postman-docs/v10/proxy-create-collection-v10-22.jpg)

### Step 5: Configure the proxy on a client device

You can use the Postman proxy to capture traffic from a client device such as a phone.

1. Start a new proxy session. Click ![Image 15: Capture icon](https://assets.postman.com/postman-docs/aether-icons/action-capture-stroke.svg#icon) **Start Proxy** in the Postman footer, then select **Start Proxy Session**.
2. Find the local IP address of the computer running the proxy:
   
   * On macOS, you can find your computer's IP address in **System Settings > Network**. Select a network interface, and if necessary select **Details > TCP/IP** to view your system's IP address.
   * On Windows, select **Start > Settings > Network & Internet > Wi-Fi** or **Ethernet**, and then select your connection. Your IP address is listed under **Properties**.
   
3. Open the wireless settings of your client device and update the configuration of the network connection to use an HTTP Proxy. For example, in iOS:
   
   1. Select **Settings > Wi-Fi**.
   1. Click ![Image 16: Info icon](https://assets.postman.com/postman-docs/aether-icons/state-info-stroke.svg#icon) next to your Wi-Fi connection.
   1. Select **Configure Proxy > Manual**.
   1. Set **Server** and **Port** to the local IP address and proxy port.
   1. Click **Save**.
   
4. Open a web browser or app on the device, then view captured traffic on the proxy session tab in Postman.

\u003e To capture secure HTTPS traffic, you need to install the `postman-proxy-ca.crt` certificate on the client device. To learn how to install the certificate on your device, go to [Capturing HTTPS traffic](/docs/sending-requests/capturing-request-data/capturing-https-traffic/).

#### Configuring a proxy on other devices

The broader development community has published some useful tutorials for setting up a proxy server on various operating systems:

* [macOS](https://support.apple.com/en-gb/guide/mac-help/mchlp2591/mac)
* [Windows](https://support.microsoft.com/en-us/windows/use-a-proxy-server-in-windows-03096c53-0554-4ffe-b6ab-8b1deee8dae1#ID0EFD=Windows_10/)
* [Linux](https://www.shellhacks.com/linux-proxy-server-settings-set-proxy-command-line/)
* [Android](https://proxyway.com/guides/android-proxy-settings)

## Troubleshoot vault secrets

You can reference vault secrets stored in your Postman Vault by adding a vault secret reference in the request body. For example, to reference a vault secret named `postman-api-key`, use the following syntax:

```txt
{{vault:postman-api-key}}
```

To learn more about troubleshooting empty and unresolved vault secrets, see [Troubleshoot vault secrets](#troubleshoot-vault-secrets).

## Postman Vault integrations

Postman supports the following Postman Vault integrations:

* [1Password](/docs/sending-requests/postman-vault/1password/)
* [AWS Secrets Manager](/docs/sending-requests/postman-vault/aws-secrets-manager/)
* [Azure Key Vault](/docs/sending-requests/postman-vault/azure-key-vault/)
* [HashiCorp Vault](/docs/sending-requests/postman-vault/hashicorp-vault/)
* [Postman Vault integrations](/docs/sending-requests/postman-vault/postman-vault-integrations/)

You can create Postman Vault integrations from the Postman desktop app or the Postman web app. If you're using the Postman web app, you can add new vault secrets to your Postman Vault by selecting the appropriate option from the Vault settings.

## Organization settings

To configure your Organization Settings, click **Organization** in the Postman header, then select **Organization Settings**.

![Image 17: Organization settings](https://assets.postman.com/postman-docs/v11/organization-settings-v11.67.png)

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

## Migrate your Enterprise team to an Organization

When you migrate your Enterprise team to an Organization, your Organization initially contains a single team that includes all the original teamâs shared workspaces.

These workspaces continue to be shared with the same users, and all members of the initial team become members of the migrated team.

This single team continues to function as it did before the migration, but Postman recommends that you break up your original, monolithic team into multiple Organization Teams, to take full advantage of Organization benefits.

### Determine the structure of your teams and memberships

A team within an Organization represents physical members of a functional team, for example, developer or test team, and also contains the workspaces that the group of users wants to keep secure and access controlled.

By creating teams and memberships first, you can establish strategic collaborations and empower your teams to migrate their own work to their teams. For example, even if your QA team hasn't moved all their workspaces to a QA-designated team yet, other teams can still invite the QA team members to collaborate with their team.

Once you define the teams, you can start the process of improving collaboration and security by populating the teams with your workspaces.

To determine the team membership, do the following:

1. The [Organization Manager (or Super Admin)](/docs/administration/organization/roles/) creates a Team and assigns a Team Manager to it.

    The Team Manager is the delegated owner of the Teamâs content and membership and controls how the Teamâs content is shared. The Team Manager is the leader of people responsible for the Teamâs content.

1. Determine how restricted the Team access should be. All Organization Teams have two [settings](/docs/administration/organization/settings/):

    * **Allow anyone from the Organization to join as a Member, or require Team Manager approval to join** â Turn on if you want to strictly control access to Teams and tightly control the teamâs membership. Environments open to collaboration donât necessarily require this level of control.
    * **Allow anyone on the Team to share content with the larger Organization, or require Team Manager approval to share outside the Team** â Turn on if your Postman Organization belongs to a highly regulated industry, or you have teams working on sensitive content where the sharing of content must be strictly controlled.

1. Populate the team with the members who are responsible for the teamâs contents.

    * If your team is smaller and doesn’t use technologies to sync users from their Identity Provider through SCIM, your Team Manager can add users, or you can simply leave the Teams open for any user to join.
    * If your team has defined user groups through SCIM, add the groups as members of their teams to automate the process of maintaining Team memberships.

## Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 18: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 19: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.

    ![Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.png)

4. Click ![Image 20: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
5. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
6. Click **Create**.

![Create a component file](https://assets.postman.com/postman-docs/v11/component-library-create-v11.png)

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

## Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 21: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 22: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component file in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 23: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your component file, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 24: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 25: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component in the left sidebar that you'd like to version and publish.
5. Click **Version &amp; Publish** in the upper right corner.

    ![Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

6. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
7. Click **Create Version &amp; Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Image 26: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 27: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of a specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 28: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

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

## Create Organization teams

To create an Organization Team, do the following:

1. Access ![Image 29: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Team Settings** in the Postman header, then click **Organization Settings**.
2. Click **Create Team**.
3. Name your team. The team will be taggable in the mentions using `@`, for example, `@api-developers`.
4. Click **Add Members**. To be added, members need to be part of the organization.
5. Click **Add**.
6. Enter a name for the team.
7. Click **Add Members**. To be added, members need to be part of the organization.
8. Click **Create**.

![Create an Organization Team](https://assets.postman.com/postman-docs/v11/org-team-create-v11.67.png)

Postman adds a new team file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

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

    \u003e If a social channel is already subscribed to workspace updates the checkbox next to **Share on Slack (or Teams)** on the bottom right of the post will be checked. If not, click ![Image 30: Slack icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-slack.svg#icon) ![Image 31: Teams icon](https://assets.postman.com/postman-docs/aether-icons/brandLogo-teams.svg#icon) **Connect** in the workspace overview to subscribe to a channel. Ensure the box is checked to send notifications when someone posts a workspace update. To learn more, visit the [Slack](/docs/integrations/available-integrations/slack/slack-app/) and [Teams](/docs/integrations/available-integrations/teams/teams-app/) integrations pages, respectively.

Learn more about:

* [Organization roles](/docs/administration/organization/roles/)
* [Organization settings](/docs/administration/organization/settings/)

## Manage secret policies with Local Secret Protection

With the Postman Component Library, you can manage reusable components for your team's OpenAPI specifications in [Spec Hub](/docs/design-apis/specifications/overview/). Maintain and standardize commonly used components in a central location, without having to redefine them in each specification. Reusable components can include schemas, responses, parameters, and more. Publish a new version when you're ready to share changes with your team.

### Create a component file

Create a component file in your team's component library. Name the file and specify the OpenAPI specification format the components will be used in. In the file, define components that your teammates can reuse in their specifications.

1. Click ![Image 32: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 33: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.

    ![Open Postman Component Library](https://assets.postman.com/postman-docs/v11/component-library-open-v11.jpg)

4. Click ![Image 34: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add**.
5. Enter a name for the component file and select the OpenAPI specification format it'll be used in. You can't change the name or OpenAPI specification version of a component file later.
6. Click **Create**.

Postman adds a new component file to your team's component library in the OpenAPI specification format you chose. [Add your own components to the file](#edit-a-component-file) so your team can reuse them in their specifications.

### Edit a component file

Add reusable components to new and existing component files. Define reusable components you'd like to standardize in your team's specifications, making the component file the single source of truth. You can edit only the draft version of a component file.

1. Click ![Image 35: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 36: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component file in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 37: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your component file, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 38: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 39: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Click a component in the left sidebar that you'd like to version and publish.
5. Click **Version &amp; Publish** in the upper right corner.

    ![Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

6. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
7. Click **Create Version &amp; Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Image 40: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 41: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of a specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 42: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

![Edit a component file](https://assets.postman.com/postman-docs/v11/component-library-edit-v11.png)

In the upper right of the editor, you can beautify, wrap, copy, and search content in the component file.

As you edit your specification, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

* When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
* When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the