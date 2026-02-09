# About resource usage

Postman provides you with a specified number of resources you can use each month, depending on your [Postman plan](https://www.postman.com/pricing/). Monthly resources include calls to the Postman API, requests made by monitors and scheduled collection runs, mock server requests, and Cloud Agent requests. Your Postman plan also has other limits, such as the number of integrations you can create, the number of custom domains, and storage for uploaded images.

To find out what the resource limits are for your plan, go to the [Postman Plans and Pricing page](https://www.postman.com/pricing/). To view the resources you are using, go to your [Resource Usage dashboard](https://go.postman.co/billing/add-ons/overview). You can view how close you are to your limits and when your monthly limits will reset. If you need more resources, you can [purchase add-on resources](/docs/billing/billing/#purchasing-add-on-resources) or [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

Refer to the following sections to understand what happens when your resource usage reaches the limits set by your Postman plan.

## Team usage limits

Your team's usage limits are based on your [plan type](https://www.postman.com/pricing/) and any [add-ons](/docs/billing/billing/#purchasing-add-on-resources) your team has purchased.

Open the [**Resource usage** dashboard](http://go.postman.co/billing/add-ons/overview) to view your team's usage of mock servers and monitors, APIs created, collection runner runs, image and file storage, flows created by your team, performance tests, integrations, and the Postman Cloud Agent. To open the **Resource usage** dashboard, do one of the following:

* **Free users** - In the Postman header, select ![Down Large icon](https://assets.postman.com/postman-docs/aether-icons/direction-down-large.svg#icon) next to **Upgrade**.
* **Paid users** - In the Postman header, select **Team**.

To learn more about the resources included with your Postman plan and what happens when you reach your usage limits, go to [About resource usage](/docs/billing/resource-usage/).

![Team resource usage information](https://assets.postman.com/postman-docs/v10/team-dropdown-resource-usage-v10-22.jpg)

Team members with the [Billing role](/docs/administration/roles-and-permissions/#team-roles) can [purchase extra blocks](/docs/billing/billing/#purchasing-add-on-resources) of monitoring requests, mock server calls, and custom domains in the [billing dashboard](http://go.postman.co/billing).

## Mock server usage

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of requests that can be sent to your [Postman mock servers](/docs/design-apis/mock-apis/set-up-mock-servers/) each month. Requests to all of your mock servers count toward this same limit. After the limit is reached, you will get a `Usage limit reached` error message in the response body when sending a request to one of your mock servers.

To make more requests to your mock servers before your monthly limit resets, you can [enable pay-as-you-go](/docs/billing/billing/#managing-resources), [purchase add-on resources](/docs/billing/billing/#purchasing-add-on-resources), or [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Monitoring usage

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of requests that can be run by your [Postman Monitors](/docs/monitoring-your-api/setting-up-monitor/) each month. Requests run by your [scheduled collection runs](/docs/collections/running-collections/scheduling-collection-runs/) and [Private API Monitoring](/docs/monitoring-your-api/runners/overview/) count toward this same limit. After the limit is reached, you will get a notification by email and in the Postman app letting you know that you've reached the usage limit for monitors.

Once you've reached your usage limit, your monitors and scheduled collection runs will no longer run on their configured schedules and can't be run manually. To resume running your monitors and scheduled collection runs before your monthly limit resets, you can [enable pay-as-you-go](/docs/billing/billing/#managing-resources), [purchase add-on resources](/docs/billing/billing/#purchasing-add-on-resources), or [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

Learn more about [viewing and managing your monitor usage](/docs/monitoring-your-api/monitor-usage/).

## Custom domains

Postman paid [plans](https://www.postman.com/pricing/) give you a limited number of [custom domains](/docs/publishing-your-api/custom-doc-domains/) you can use when publishing API documentation. After the limit is reached, you won't be able to add a new custom domain.

To add a new custom domain, delete one of your existing custom domains, [purchase add-on resources](/docs/billing/billing/#purchasing-add-on-resources), or [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## API Builder resources

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of APIs you can create in the [API Builder](/docs/design-apis/api-builder/overview/). After the limit is reached, you won't be able to create new APIs in API Builder. To create a new API, delete one of your existing API Builder APIs, or [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Manual Collection Runner runs

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of [collection runs](/docs/collections/running-collections/intro-to-collection-runs/) you can use each month. This limit applies to collections that you run in a workspace using the **Run manually** option. This is separate from the limits for [scheduled collection runs](/docs/collections/running-collections/scheduling-collection-runs/) in the Postman cloud. A collection run with multiple iterations counts as a single run.

You can check your manual collection run usage in the [Resource Usage dashboard](https://go.postman.co/billing/add-ons/overview). Also, a message will display in the Collection Runner when you're approaching your usage limit.

Once you've reached your usage limit, you will no longer be able to run your collections using the **Run manually** option. To resume running collections before your monthly limit resets, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes), [schedule collection runs](/docs/collections/running-collections/scheduling-collection-runs/) in the Postman cloud, or run collections using the [Postman CLI](/docs/postman-cli/postman-cli-run-collection/) or [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

Requests run in the Postman cloud by your [scheduled collection runs](/docs/collections/running-collections/scheduling-collection-runs/) count toward your [monitoring usage](#monitoring-usage). Scheduled collection runs don't count toward your manual collection runs usage.

## Storage usage

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited amount of storage for [uploaded images](/docs/publishing-your-api/authoring-your-documentation/#uploading-an-image) in your API documentation. You will get an error message if you try to upload an image that would exceed your storage limit.

To upgrade your available storage, contact [Postman support](https://www.postman.com/support/).

Learn more about [image storage limits](/docs/publishing-your-api/authoring-your-documentation/#image-storage-limits) for API documentation.

## Flows usage

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of credits that can be consumed by AI blocks like the [**Create with AI** block](/docs/postman-flows/reference/blocks/create-with-ai/) in [Postman Flows](/docs/postman-flows/overview/). Credits are shared across all users on a team. To get more credits, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes). Learn about [flows usage](/docs/billing/flows-usage/).

## Performance test limit

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of [performance test runs](/docs/collections/performance-testing/testing-api-performance/) you can use each month. This limit applies to collections that you run using the **Performance** tab in the Collection Runner. This is separate from the limits for functional tests ([manual collection runs](/docs/collections/running-collections/intro-to-collection-runs/) and [scheduled collection runs](/docs/collections/running-collections/scheduling-collection-runs/)).

You can check your performance test usage in the [Resource Usage dashboard](https://go.postman.co/billing/add-ons/overview). Also, a message will display in the Collection Runner when you're approaching your usage limit.

Once you've reached your usage limit, you will no longer be able to run performance tests. To resume running performance tests before your monthly limit resets, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Specifications

Your [Postman plan](https://www.postman.com/pricing/) gives your team a limited number of [specifications](/docs/design-apis/specifications/overview/) to create in Spec Hub in internal workspaces. In the [Resource Usage dashboard](https://go.postman.co/billing/add-ons/overview), you can see how many specification have been created in internal workspaces. To create more specifications in internal workspaces, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Packages

Your [Postman plan](https://www.postman.com/pricing/) gives your team a limited number of [packages](/docs/tests-and-scripts/write-scripts/packages/package-library/) to create in the Postman Package Library. In the [Resource Usage dashboard](https://go.postman.co/billing/add-ons/overview), you can see how many packages have been created. To create more, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

As a [Team Admin](/docs/administration/roles-and-permissions/#team-roles), you can select **View detailed usage** to view a detailed list of packages in your team. For each package, you can view the package name, who created the package, and when the package was created. You can also view when the package was last used. The last used date increases when one of the following occurs:

* A teammate views the package in the package library.
* A teammate sends an HTTP request that imports the package, and this is the first time they send the request after opening Postman.

To work with packages in your team, do any of the following:

* To filter the list by package name, start typing in the search box.
* To filter the list by the user who created the package, select a team member in the **Uploaded by** dropdown list.
* To delete a package, hover over a package and select ![Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) > ![Delete icon](https://assets.postman.com/postman-docs/aether-icons/action-delete-stroke.svg#icon) **Delete**.

![Manage test data](https://assets.postman.com/postman-docs/v11/test-data-manage-v11-40.jpg)

Once you've reached your test data storage limit, you won't be able to upload more test data files. You can delete files to free up storage space, or you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

Once you're reached your test data retrieval limit, requests that use uploaded data files won't be able to retrieve those files before being sent. This includes requests that are sent manually or automatically from a scheduled collection run, monitor, flow, or the Postman CLI. To resume using test data before your monthly limit resets, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Agent Mode usage

With [Agent Mode](/docs/agent-mode/overview/), you get a monthly AI credit allowance on Free, Basic, and Professional plans.

On the Free plan, when your team members reach their monthly credit limit, you can purchase the Postman AI add-on to get more monthly credits. On Basic and Professional plans, you can keep using Agent Mode after reaching your limit if credit overages are enabled by an Admin. If overages arenât enabled, Agent Mode pauses until credits renew.

To learn more, see [Manage your Postman Agent Mode credits](/docs/billing/agent-mode-usage/).

## Postbot usage

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of Postbot activities each month. Postbot will notify you when you reach the monthly activity limit. You can't use it for the remaining month unless you [purchase Postbot as an add-on](/docs/billing/billing/#purchasing-add-on-products).

## Postman API usage

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of requests that can be sent to the [Postman API](/docs/developer/postman-api/intro-api/) each month. After the limit is reached, you will get a `Service limit exhausted` error message in the response body when sending a request to the Postman API.

To make more requests to the Postman API before your monthly limit resets, you can [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Integrations

Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of [integrations](/docs/integrations/intro-integrations/) for connecting Postman to third-party tools you use for API development. After the limit is reached, you won't be able to add a new integration. You will get a notification in the Postman app when attempting to add a new integration.

To add a new integration, delete one of your existing integrations or [upgrade your plan](/docs/billing/billing/#team-and-plan-changes).

## Cloud Agent usage

The [Postman Cloud Agent](/docs/getting-started/basics/about-postman-agent/#postman-cloud-agent) enables you to send requests from the [Postman web app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-web-app) without encountering cross-origin resource sharing (CORS) limitations. Your [Postman plan](https://www.postman.com/pricing/) gives you a limited number of requests that can be sent using the Cloud Agent each month. After the limit is reached, you will get a `Cloud Agent Error` message in the response body when sending a request from the Postman web app using the Cloud Agent.

To continue sending requests from the Postman web app before your monthly limit resets, [upgrade your plan](/docs/billing/billing/#team-and-plan-changes) or switch to the Postman Desktop Agent. In the error message, select **Use Postman's Desktop Agent**. If you haven't already installed the Desktop Agent, you'll be prompted to download it.

Learn more about [installing and using the Postman Desktop Agent](/docs/getting-started/basics/about-postman-agent/#postman-desktop-agent).